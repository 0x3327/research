---
title: OWT - Omni Web Token
author: Aleksandar Veljković
date: 4/6/2022
---



# Executive Summary

JSON Web Tokens, or JWT, are the format of JSON encoded data structures for authorizing clients on the Web. Some JWT payloads have a specific standardized structure, defined by the protocol, such as OAuth(2) tokens. Others, however, are designed specifically for particular apps.

Authorization on the Blockchain is done mainly through explicitly whitelisting addresses that are allowed to perform specific actions. Whitelisting introduces high costs when the number of whitelisted addresses is large. A good example is ICO whitelisting, where hundreds or even thousands of participants need to get whitelisted.

This research aims to find an efficient, more cost-effective solution for authorizing users on the Blockchain using a system of authorization tokens issued and received off-chain, without the Blockchain transaction fees, and which will be valid on-chain and off-chain. In addition, the token structure should be transferrable off-chain as a JWT token, compatible with the OAuth2 standard, and reusable in both Web 2.0 and Web 3.0 worlds.

# Introduction

Ethereum Blockhain gas prices are following the price of Ether, resulting in higher transaction fees. The cost of 1 ETH on January 1st, 2019, was \$140.82 \[1\]. On the same day in 2022, the price for 1 ETH was \$3,769.70 \[2\]. That means that the same transaction from 2019 became just three years later became more than 30 times more expensive.

Executing transactions on Blockchain, in general, doesn't require any specific authorization. The transactions are signed using the private key and paid using ETH from the signer's wallet. However, some transactions, such are token purchases during ICOs, require explicit approval by the smart contract owner. The approval on the Blockchain is done by whitelisting wallet addresses that are allowed to perform specific actions, submitting the list of the whitelisted wallets, and storing them on the Blockchain. The price of each transaction for storing whitelisted wallets linearly grows by the number of the wallets.

In a more concrete example, storing one 20 byte address on Blockchain, having ETH at the January 1st, 2022 price, costs approximately 20000 GAS or around \$5.6, having an average gas price of 74 Gwei. With those prices, storing a hundred whitelisted addresses would cost about \$565, with base transaction cost included. It is challenging for technology to expand with such high prices for such basic requirements.

Before introducing the solution this research is proposing, it is essential first to briefly introduce some basic concepts regarding the existing methods for authorization on the Web.

## OAuth standard

Open Authorization, or OAuth for short, is an authorization standard followed by many APIs worldwide. The standard specifies the protocol between client and authorization server and data transferred in protocol messages. There are two versions of OAuth standard, 1 and 2.

OAuth standard doesn't specify the transfer method for sending messages, but one widely adopted standard is using JWT tokens as the authorization data container.

## JWT Tokens

In 2015, Michael Jones, John Bradley and Nat Sakimura introduced JSON Web Tokens (JWT) through RFC-7519 as a compact structure for representing claims transferred between two parties \[3\]. Since then, JWTs have been used for client authentication on the Web. Initially, the authentication was performed between APIs but quickly found use in client authentication following the growth of client-heavy applications.

JWT has a general structure, made of a header, body, and signature segments. The header segment includes the token type and a label of the algorithm used for creating signatures.

Example JWT header

    {
        "type": "JWT",
        "alg": "ES256"
    }

The body segment is a container segment used for storing protocol-specific information. OAuth 2.0 standard, introduced with RFC-6749 \[4\], specifies several fields required for authorization that are members of the body of a JWT token.
Some of those fields are:

-   `aud` (Audience) - Identifier of the user to whom the client will present the token for executing an action
-   `exp` (Expiration) - Token expiration timestamp
-   `iss` (Issuer) - Identifier of the token issuer, authorization service provider
-   `scope` (Action scope) - List of actions for which the token owner would be authorized to perform
-   `sub` (Subject) - Identifier of the token owner
-   `iat` (Issued at) - Isusing timestamp

Example JWT Body

    {
      "sub": "user1",
      "name": "John Doe",
      "iat": 1516239022,
      "aud": "server1",
      "scope": ["data.fetching"]
    }

Field `name` in the JWT body example represents a custom, application-specific data field.

The signature part of the JWT token contains the hash or signature of the token provided by the token issuer.

The three token parts are put together into one base64 encoded string (without trailint `=` symbols), having the tree parts separated by the dot `.` symbol.

Example of a complete JWT string

    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

## General Authorization Protocol

A general protocol for client authorization on the Web using JWT tokens consists of two steps:
- Requesting token from the authorization server for executing some action
- Presenting the authorization token received from the authorization server to the server which would perform the requested action

## Existing Approaches

There are some existing approaches for combining the Blockchain and OAuth tokens. In one such research \[5\], the authors used NFTs as authorization tokens generated on-chain that would be verifiable using the OAuth 2.0 protocol. That approach is inverse to this research: it doesn't reduce costs but puts authorization tokens on the chain.

# Goals & Methodology

The main goal of this research was to find a way to make authorization on the Web cheaper than the existing whitelisting method with the general idea to build a solution analogous to the current, proven methods for authorization on the Web. The key motivation for using tokens as an authorization method is an authorization protocol that shifts significant transaction fees from one authorization entity to many clients that pay only a small additional fee on top of the price they pay for executing the authorized action.

Reducing the price paid by the authorization entity by 100% can be achieved by issuing authorization tokens off-chain. This protocol specification introduces challenges regarding the design of the token, as the token should include all the information that the authorization entity would provide with the Blockchain transaction in the first place.

Reducing the costs of additional fees that clients would now pay for the authorization requires the overhead authorization data submitted on the Blockchain to be as small as possible. This requirement poses the main challenge for token design. Additionally, the Blockchain should not explicitly store authorization data, except as transaction arguments.

Combining these requirements, a perfect authorization schema represents a two-step protocol where the client first acquires the authorization token from the authorization server, off-chain. Second, the client submits the data required for performing the action to the Blockchain with a minor (ideally none) overhead the smart contract would use to confirm the client's authorization.

## Chain token (CT) representation

The essential requirements for the token that would be used on the chain are:
- Efficient verifiability; token should be efficiently verifiable on the chain
- Authenticity; the probability of token forgery should be negligible
- Succinctness; token should be small in byte size
- Non-transferability; token should be used only by the user who received the token

As an example throughout this research, we will use the money checkout allowance problem, where a client needs to be authorized to payout a certain amount of money from the account of the authorizing entity. An existing approach for solving this problem is calling the approval method on the smart contract or whitelisting clients and explicitly approving the total allowed amount for each client. Method signature without a token argument would look like this:

    payout(address account, address receiver, uint256 amount)

A naive approach for constructing a token that would follow JWT logic would be providing all the values bound by the token. In our example, the values that are required for money checkout from the account are:
- account owner identifier; 20 bytes address value
- authorized client identifier; 20 bytes address value
- allowed amount; 32 bytes value

Next, the apparent problem is a forgery. Everyone can create a token with listed values and submit it on the Blockchain. The solution for this problem is to provide a signature made by the authorization entity, which confirms the provided values. Ethereum signatures contain three segments, v, r, and s, 65 bytes long.
All summed up to 137 bytes of memory. Even if this doesn't look like a significant sum, the main issue is that the token size asymptotically grows by $O(n)$, linearly with the number of arguments n. In other words, it would become costly, or even unusable, for methods with more arguments. It is not very efficient, but it is a start.

### Token size optimization

The problem with the naive approach is linear growth with the number of arguments. Solving this problem requires looking closely at the method that is being called. The method `payout` already contains the token values as a method argument, and it would be redundant to provide them again in the token. The same pattern is visible with different use-cases.
This observation suggests that we can avoid providing the values within the token but use only a hash of the approved values and check if the hash of the provided input values matches the token hash. Using the hashing method clears the linear growth of the token as the size of the keccak256 hash is fixed to 32 bytes in length, achieving a constant $O(1)$ size of the token. The hash can also cover other values that could be hard-coded into the smart contract without a token size increase, which will become an essential feature in later sections.

### Signature size optimization

The Ethereum signature size is fixed to 65 bytes. That means that it passes the size of 2 memory words (32 bytes in size) and requires three blocks of memory. The solution for this problem comes with EIP-2098 \[6\], which proposes a simple technique for compact signature representation, reducing its size by 1 byte and allowing it to fit into two memory blocks.

The total token size is now fixed to 32 bytes of token hash plus another 64 bytes of signature data totaling 96 bytes or three blocks of memory.

### Mapping OAuth2.0 parameters

Now that we have a token structure, we need to figure out how to standardize token parameters to comply with the OAuth2.0 standard.

The audience parameter refers to the smart contract containing the payout method. It doesn't need to be provided explicitly as a method argument as it is already encoded in the smart contract.

The token issuer can be deduced from the signature and doesn't need to be explicitly provided.

The subject parameter is provided both as the input argument of the `payout` method. It doesn't have to be provided explicitly. It should not be provided even as the argument, as it is already given as the message sender value.

The scope parameter describes the action that should be executed. It should not be explicitly provided as it should be hardcoded in the method.

The token expiration time is a tricky one. It doesn't naturally belong to method arguments, so it should be provided explicitly. To prevent the token size increase, we can do a simple modification of the token hash. The value of the timestamp can be stored in 8 bytes. A straightforward solution is to provide another method argument with an 8-byte value. A more elegant solution is to transform the keccak256 value into "pseudo-keccak224" (SHA224 \[7\] value, with unchanged initialization value) by truncating the hash size to its 224 bytes prefix and appending 8 bytes extension with expiration timestamp as the last 8 bytes of the token hash. This transformation returns us to the previously proposed token size without extra arguments.

As we can see, all the crucial parameters of the OAuth2.0 protocol can be successfully mapped to the Blockchain transactions and the chain token.

## Token reusability

Some authorization tokens are reusable many times until the expiration date. However, some use-cases require that the tokens may be used only once. An example of such a use case is exactly the example we have used so far. Once the payout method has been executed, the user should not be able to perform double-payout transactions. This problem can be solved the same way as in Web 2.0 - by introducing a payment identifier. The payment identifier should be included as an extra method argument and included in the token hash. This solution also solves the issue of the lost token, as the token can be reissued with the same payment identifier and used for the same payment only once. Specific use cases may require the existence of only one token. In that case, the token (and method arguments) may include `jti` parameter or JWT token ID as a token identifier or use the token hash as an identifier. The smart contract should implement mechanisms for preventing double payments and a potential blacklisting of tokens.

## Action scope schemas

OAuth2.0 proposes a parameter that includes the action scope or label of the action for which the client can use the token. Action scopes are not specified as they can be represented using any string value. The problem here is the cost of using string data types in smart contracts. This research proposes restriction for action type values to numerical data types of 4 bytes. This restriction allows $2^32$ possible scope values that could represent many use cases.

A library of token schemas can help developers properly format their tokens based on scope number schemas. Furthermore, enumeration of action types can introduce standardization for tokens where a smart contract may require, for example, "scope 42" tokens for executing a method. We present the first two token scopes that would be used in the following use-cases:

### Scope 1: Generic Identity

Generic identity scope should be used for verification of the client's identity.
The verification is based on the client's wallet address and unique identifier in the issuer's database. The hash for "scope 1" tokens be made by hashing the following array of values in their respective order:
- `address iss`; token issuer
`address aud`; smart contract address or 0 address for general identification
- `address sub`; client's wallet address
- `uint4 scope`; action scope with value `1` for generic identification
- `bytes32 uuid`; unique identifier of the client in the issuer's
- `uint8 exp`; token expiration timestamp in UNIX timestamp format database
\### Scope 2: Allowance
Allowance tokens, used for crypto cheques, should have hashes made by hashing the following array of values in their respective order:
- `address iss`; token issuer
- `address aud`; smart contract address
- `address sub`; money receiver
- `uint4 scope`; action scope with value `2` for allowance
- `bytes32 paymentId`; payment identifier (NOTE: token hash may be used as payment ID but it can introduce new problems)
- `uint256 amount`; amount to transfer
- `uint8 exp`; token expiration timestamp in UNIX timestamp format

The reader may notice that in both cases, there are two logical groups of parameters:
- general parameters; `iss`, `aud`, sub`,`scope`and`exp`- application-specific parameters;`userId`,`paymentId`,`amount\`

The general parameters are the same for all tokens, and application-specific parameters are different for each scope.

## From Chain Token (CT) to Omni Web Token (OWT)

Now that we have the complete definition of the chain token, we can go one more step and make it usable and transferrable in the Web 2.0 world.
We can do this by packing chain token data as part of theJWT token, following the OAuth 2.0 schema.

### OWT Body

The token scopes define OAuth 2.0 parameters, so the only remaining thing is appropriately packing the chain token into the JWT body and creating a proper JWT signature. The verifier needs to know the CT hash value and the parameters used in the construction of the token.

The proposed OWT body schema is:

    {
        aud: <smart contract address>,
        iss: <issuer's wallet address>,
        scope: <readable name of the scope>,
        exp: <token expiration timestamp>
        chain_token: {
            token_hash: <CT hash with expiration timestamp>,
        r: <signature r value>,
        sv: <compact representation of s and v signature values>
            params: [<
                    ordered list of token parameters
                    in form of:
                     {
                        param: <parameter name>,
                        value: <parameter value>,
                        type: <parameter data type>,
                     }
                >]
        }
    }

### OWT Signature

The JWT standard allows using the Ethereum secp256k1 signatures by providing the `EC256` algorithm type value in the token header. The signature of the OWT token is created using the issuer's private key. To verify the signature, the verifier needs access to the issuer's public key, which should be available from the issuer's `/.well-known/jwks.json` route of the authorization API.

## OWT Issuing

The OAuth 2.0 protocol allows using `client id` and `client secret` parameters when requesting the authorization tokens. OWT requests can be made using wallet address as client's identity and signature of the clients wallet address as the `client secret` parameter

# Results & Discussion

To test our hypothesis and estimate the costs of working with OWTs, a simple NodeJS library for generating and verifying OWTs was implemented together with testing REST API for issuing OWTs following the OAuth 2.0 protocol. An example smart contract for testing the usability of the chain token was also implemented.

The smart contract used for testing included four methods:
- `whitelist(address client, uint256 amount)` method for whitelisting the user for a given amount of money
- `payoutOld(uint256 amount)` method for performing payout in the old fashioned way by checking the whitelisted amount
- `payoutNew(address sender, uint256 amount, bytes32 paymentId, bytes32[3] calldata token)` method for performing payout using the chain token following "scope 2" schema
- `payoutNewShort(address sender, uint256 amount, bytes32[3] calldata token)` method for performing payout using the chain token but without payment identifier, having token hash as a payment identifier
- `verifyIdentity(address issuer, bytes32 userId, bytes32[3] calldata token)` method for simple verification of the client's identity following "scope 1" schema

## Allowance Use Case

The allowance use case tested the token issuing protocol for payout allowances, evaluated the costs of performing payouts using the token, and compared the results with the basic whitelisting protocol.

### Test setup

Authorization entity submitted allowance amount for the client using the `whitelist` smart contract method. The cost of the whitelisting transaction was 44,484 gas.

### Test 1: Payout by Whitelisting

The client executed the `payoutOld` method of the smart contract with a propper allowance amount. The cost of the payout transaction was 22,389 + T gas.

### Test 2: Payout with Token

The client requested an OWT from the authorization server using OAuth 2.0 request schema. The authorization server verified the client's credentials and issued a "scope 2" token to the client with a specified allowance amount. The client verified the OWT data and extracted the chain token and its parameters from the OWT. After the OWT verification step, the client submitted them to the smart contract using the `payoutNew` method. The payout was successful, and the execution cost was 59,935 + T gas.

### Test 3: Payout with Token using Token Hash as Payment Identifier

The protocol for issuing and verifying the OWT was done the same way as in the previous test. The only difference was that the token did not follow the "scope 2" schema but left out the payment identifier. The client performed a payout using the `payoutNewShort` method. Again, the payout was successful, and the execution cost was 59,189 + T gas.

### Cost Analysis

The test results show that the cost of the payout protocol using whitelisting was 44,484 gas for the issuer and 22,389 gas for the client, resulting in 66,873 gas for the entire protocol. Test 2 showed that using the token has reduced the issuer's costs to 0, but the client's cost was increased to 59,935 gas which is 37,546 gas more than in test 1. Interestingly, the overhead cost for the client is lower than the costs of the issuer's whitelisting, which indicates that using the token reduces the issuer's fees, compared to whitelisting, even if the issuer compensates the overhead client's costs by increasing the allowance amount. Test 3 showed that using token hash as payment identifier reduces the costs for extra 746 gas. However, this introduces problems with token reissuing. The exact token needs to be reissued every time the original one gets lost, requiring the expiration timestamp to be the same as the original one for the hashes to match and thus have the same payment identifier. This situation can cause the issuer to be unable to reissue the token as its timestamp has already expired. The results of the cost analysis are presented in Table 1.
</br></br>
<table>
<tr>
<th>
Method
</th>
<th>
Issuer's costs (gas)
</th>
<th>
Client's costs (gas)
</th>
<th>
Total protocol costs (gas)
</th>
</tr>
<tr>
<th>
Whitelisting
</th>
<th>
44,484
</th>
<th>
22,389
</th>
<th>
66,873
</th>
</tr>
<tr>
<th>
OWT allowance
</th>
<th>
0
</th>
<th>
59,935
</th>
<th>
59,935
</th>
</tr>
<tr>
<th>
Short OWT allowance
</th>
<th>
0
</th>
<th>
59,189
</th>
<th>
59,189
</th>
</tr>
</table>
<center>
Table 1. Cost anlysis of the allowance use case methods
</center>

</br></br>

## Generic Identity Use Case

The generic identity use case tested the issuing and verification of the "scope 1" tokens and assessed the costs of using identification tokens on the chain.

The client acquired OWT from the authorization server and submitted the token with the received user id from the issuer's database. The client submitted the token to the `verifyIdentity` method of the smart contract and successfully verified the identity token. The cost of the verification was 36,816 gas, which suggests that the verification proces cost was 15,817 gas, leaving out the base transaction cost.

### Use case analysis

The test showed that the costs for verifying the identity tokens are low and open a new path for the identity representations valid on multiple chains. Additional use cases may specify scope schemas for more specific identity tokens and introduce low-cost decentralized identities to a multi-chain environment.

## General Purpose Token Verification Service (GPTVS)

The entire verification protocol can be summed up into a token verification smart contract that can be deployed and used by multiple users to verify the authorization tokens for their smart contracts. Blacklisting can be introduced for tokens or clients. This service should allow listing approved issuers and smart contract addresses from which the requests may come. Also, the service can be monetized by requiring a certain amount of Ethers or ERC-20 tokens to be submitted monthly by the users to the verification smart contract, or the service will become unavailable for the requests coming from the user's smart contracts.

# Conclusion

The test results show that the OWTs and the chain tokens can cover a variety of use cases while introducing standardization in token construction, issuing, and verification. Operating with OWTs reduces costs for the services requiring whitelisting while enabling new multi-chain use cases thanks to a succinct yet general token structure and easy verification. The following steps would include defining more token schemas covering miscellaneous use cases and implementing the General Purpose Token Verification Service.

# Appendices

## Appendix 1: Chain token verification smart contract

``` solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract VerifierContract {
        mapping(address => uint256) whitelisted;
        mapping(bytes32 => bool ) usedPaymentIds;
        bytes prefix = "\x19Ethereum Signed Message:\n32";
        uint32 genericIdentityScope = 1;
        uint32 payoutScope = 2;

        function checkSignature(bytes32[3] calldata token, address signer) public returns (bool) {
                // Decode r, s, v values
                bytes32 hash = token[0];
                bytes32 sv = token[2];
                bytes32 r = token[1];
                bytes32 s = sv & bytes32((uint((1 << 255) - 1)));
                uint8 v = uint8(uint(sv >> 255) + 27);

                // Create signature hash
                bytes32 prefixedProof = keccak256(abi.encodePacked(prefix, hash));

                // Verify signer
                address recovered = ecrecover(prefixedProof, v, r, s);
                return recovered == signer;
        }
        
        function whitelist(address client, uint256 amount) public {
                whitelisted[client] = amount;
        }

        function payoutOld(uint256 amount) public {
                require(amount <= (whitelisted[msg.sender]));
                whitelisted[msg.sender] -= amount;
        }

        function payoutNew(address sender, uint256 amount, bytes32 paymentId, bytes32[3] calldata token) public{
                // Check if token has already been used
                require(usedPaymentIds[paymentId] == false);

                // Check token expiration
                uint32 exp = uint32(uint256(token[0]));
                require(exp > block.timestamp, "Token expired");

                // Check token signature
                require(this.checkSignature(token, sender) == true, "Invalid signature");

                // Check token values
                bytes32 prefixedProof = keccak256(abi.encodePacked(sender, address(this), msg.sender, payoutScope, exp, paymentId, amount));
                require (bytes32((uint256(prefixedProof >> 32 << 32) | uint256(exp))) == token[0]);

                usedPaymentIds[paymentId] = true;
        }

        function payoutNewShort(address sender, uint256 amount, bytes32[3] calldata token) public{
                // Check if token has already been used
                require(usedPaymentIds[token[0]] == false);

                // Check token expiration
                uint32 exp = uint32(uint256(token[0]));
                require(exp > block.timestamp);

                // Check token signature
                require(this.checkSignature(token, sender) == true);

                // Check token values
                bytes32 prefixedProof = keccak256(abi.encodePacked(sender, address(this), msg.sender, payoutScope, exp, amount));
                require (bytes32((uint256(prefixedProof >> 32 << 32) | uint256(exp))) == token[0]);

                usedPaymentIds[token[0]] = true;
        }

        function verifyIdentity(address issuer, bytes32 userId, bytes32[3] calldata token) public {
                // Check token expiration
                uint32 exp = uint32(uint256(token[0]));
                require(exp > block.timestamp);

                // Check token signature
                require(this.checkSignature(token, issuer) == true);

                // Check token values
                bytes32 prefixedProof = keccak256(abi.encodePacked(issuer, address(this), msg.sender, genericIdentityScope, exp, userId));
                require (bytes32((uint256(prefixedProof >> 32 << 32) | uint256(exp))) == token[0]);
        }
}
```

# Bibliography

<div id="refs">

</div>

1.  Coinmarketcap, Historical snapshot from 2019/01/01, https://coinmarketcap.com/historical/20190101/

2.  Coinmarketcap, Historical snapshot from 2022/01/01, https://coinmarketcap.com/historical/20220101/

3.  M. Jones, J. Bradley, N. Sakimura, RFC-7519: JSON Web Token (JWT), https://datatracker.ietf.org/doc/html/rfc7519

4.  D. Hardt, Ed., RFC-6749: The OAuth 2.0 Authorization Framework, https://datatracker.ietf.org/doc/html/rfc6749

5.  N. Fotiou, I. Pittaras, V. A. Siris, S. Voulgaris, G. C. Polyzosar, OAuth 2.0 authorization using blockchain-based
    tokens, arXiv:2001.10461v1, 28 Jan 2020, https://arxiv.org/pdf/2001.10461.pdf

6.  R Moore, N Johnson, EIP-2098: Compact Signature Representation, https://eips.ethereum.org/EIPS/eip-2098

7.  R. Housley, RFC-3874: A 224-bit One-way Hash Function: SHA-224, https://datatracker.ietf.org/doc/html/rfc3874
