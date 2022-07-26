---
title: ZK NFT Mixer
subtitle: ERFC - 270
author: Aleksandar Veljković
date: 6/5/2022  
---

# Executive Summary

NFTs are growing in popularity, and so are the numbers of transactions
for transferring the NFTs on the Blockchain. One of the main features of
the Blockchain is privacy, but only in terms of pseudo-anonymity. The
pseudo-anonymity implies that the user creating the transaction is
hidden, as he is represented using an opaque, pseudo-random address.
Still, the transactions between the addresses are transparent. By
analyzing the transaction graph and external inputs, such as social
network posts putting the address in a specific context, it is possible
to deduce the address owner and reveal all his transactions. This
research aims to analyze the possibility of creating a solution that can
enable NFT transfers in an environment that supports complete anonymity
but is still compatible with Ethereum. The proposed infrastructure
represents a zero-knowledge mixer supporting shielded transfers of the
NFTs on the side chain with the ability to withdraw NFTs back on the
main chain.

# Introduction

Many existing solutions utilize zero-knowledge proofs to shield
transactions or mix the coins and tokens. Those solutions include Zero
cash, Tornado cash, Monero, and many more. The common thread connecting
all of them is that they are meant for transferring currency. Although
some providers (like Tornadocash \[1\]) announced, ZK solutions for
transferring NFTs are not very popular. Unlike the currency, the NFTs
are unique objects, and it is not easy nor practical to hide them in
plain sight. It is possible to hide what is transferred, but it is easy
to follow the trail if the thing that is transferred is unique.

NFTs are finding their way to the sidechains, as the Ethereum mainnet
transactions often become too much overhead for minting or transferring
NFTs \[2\]. ZK rollups like zkSync are also used for transferring and
minting the NFTs \[3\], but the “ZK” part of the rollup doesn’t refer to
privacy but compression of the transactions as a scalability solution.
Bridges between sidechains and Ethereum allow NFT transfers between the
chains \[4\], enabling cheap transactions on the side chain and final
transfer back on the main chain. None of the general-purpose side chains
provide shielded NFT transfers. A new solution promising shielded
transfers for any assets is Namada \[5, 6\], Blockchain specifically
built for asset privacy. With new updates of Nightfall, Polygon also
announces featuring private NFT exchanges \[7\].

This research investigates the possibilities of using existing, widely
adopted, general-purpose side chains to implement shielded NFT
transfers. If the projects featuring shielded NFTs are scarce, a good
question is if there is a market need for such a solution. The answer to
this may not come from the current state of the market but the
predictions of future trends. As the NFTs gain even more popularity and
move from the hype-regulated market of novelties to more serious use
cases, such as access control, certificate issuing, and similar, there
is an indication that shielding NFTs of such documents will become a
requirement. Such trends are also visible through the projects
announcing future updates supporting this domain.

# Goals & Methodology

The main goal of this research is to investigate the possibilities of
implementing a zero-knowledge mixer for NFTs, using a side chain for
shielding transfers resulting in a proposal of a software architecture
and algorithms that would support such a system.

It is essential first to analyze the building blocks of similar
solutions to be able to come up with a new one. A cross-chain movement
of tokens is enabled using cross-chain bridges. The focus here would be
on two-way decentralized bridges between two EVM chains. The two-way
bridges consist of two smart contracts on each side. The role of smart
contracts is locking tokens on one side and releasing or minting tokens
on the other side. The contracts communicate by firing events on one
side, and validator nodes that listen to those events trigger operations
on the other.

There are two types of blockchains regarding the representation of the
main currency on the chain - wallet-based and UTXO base. The
wallet-based chains represent currency as a gross numerical value stored
in the memory fields associated with specific accounts. When the amount
![X](https://latex.codecogs.com/svg.latex?X "X") is transferred from
wallet A to wallet B, the values are updated so that wallet A has
![X](https://latex.codecogs.com/svg.latex?X "X") coins less and wallet B
has ![X](https://latex.codecogs.com/svg.latex?X "X") coins more in the
associated memory field. This logic is familiar to Ethereum users, as
Ethereum is a wallet-based blockchain.

The chains based on UTXOs have a different philosophy. The UTXO acronym
stands for “Unspent transaction (TX) output,” which may give a clue on
the main structure used for representing the coins. Let’s use Bitcoin as
a representative of a UTXO-based chain. Each transaction on Bitcoin
requires an input amount of coins that should be transferred to the
other address. The user might not see it, but the coins are not just
numbers updated with each transaction, as the transactions on Bitcoin
have a more strict input-output definition. There are no wallets as
memory locations linked with the account, but the coins are represented
as one or many UTXOs. Users own their UTXOs by having them linked with
their public key and transfer them by signing the transactions using the
private key associated with the UTXOs. When the user has a UTXO of five
coins and wants to transfer three of them, the transaction uses a UTXO
of five coins as input. The outputs of the transaction are two new
UTXOs. The first one represents the transferred amount with the value
three labeled with the recipient’s public key. The other is the
remainder, or the unspent amount with the value two, tagged with the
sender’s key. If the user has two UTXOs with two coins each and wants to
transfer three coins, the user would use both UTXOs as transaction
inputs. Again, the output would be two new UTXOs, one with the
transferred amount for the recipient, and the other, the unspent part
for the sender.

Systems that enable shielded transactions utilize UTXO representation
for the shielded tokens even on chains that are not natively UTXO-based,
as that representation is more suitable for the use case. In such
systems, the UTXO values are hidden from the public and only visible to
the recipient with a private key to decrypt it. The workload for
computing transaction parameters is now on the sender’s side, as no
other participant can see the UTXO value. The sender prepares the
transaction’s inputs and outputs and generates a zero-knowledge proof
that the transaction is generated correctly with proper values. The
proof must confirm that the sender knows the non-encrypted UTXO value
and the correct values of the resulting UTXOs after the transfer. Monero
uses additional decoy values as fake UTXOs to spoof the actual token
transfer and blur the overall chain of transfers \[8\]. Preventing
double-spending is mainly done using nullifiers - values representing
“coupons” for spending the UTXO. The UTXO is tied to a nullifier value,
and transferring the UTXO requires the user to submit the nullifier
linked with the UTXO, marking the UTXO as used. One nullifier can be
used only once. When the piece of UTXO is spent, the remainder and the
sent part are converted to new UTXOs with their respective nullifiers.

NFTs represent unique objects, so the methods used for hiding and
splitting the token batches are not directly applicable to NFTs.
Conversely, if the methods could be adapted to support NFTs, most
well-tested algorithms and flows could be reused. Converting NFT to a
UTXO-like object, called commitments, may be straightforward. The
commitment may hide the token address and ID information, but the
quantity value will always be one. Unfortunately, even if the quantity
and token information are hidden, tracking the token in the network is
easy. There is a 1-to-1 mapping between the input token and the
resulting commitment. A solution to this problem may lay in decoys.

<img src="../assets/ERFC-270/decoy.jpeg">

One NFT can be converted to one correct commitment followed by
![N-1](https://latex.codecogs.com/svg.latex?N-1 "N-1") false commitments
constructed as decoys. This schema would fail when only the NFT
commitment is transferred to the other user, revealing which of the
![N](https://latex.codecogs.com/svg.latex?N "N") commitments was the
NFT. To mitigate this problem, each transfer transaction of the NFT
commitment should also include transferring
![K](https://latex.codecogs.com/svg.latex?K "K") additional decoys to
different addresses. When all participants use decoys with their
transfers, the transfer graph is quickly blurred, and finding the actual
NFT commitment needle in a haystack of decoys becomes difficult. One
downside of this approach is a quicker filling of the commitment Merkle
tree, but it can be mitigated using a bigger tree. The other is the cost
increase. Under the assumption that the decoying mechanism provides
reasonable privacy and anonymity, the protocol can reuse the previous
building blocks to complete the system.

## Depositing NFTs from Ethereum to the side chain

User deposits NFTs on the Ethereum smart contract by sending a
transaction allowing the smart contract to take over the NFT. On the
side chain, ![N](https://latex.codecogs.com/svg.latex?N "N") commitments
are minted and added to a Merkle tree. The smart contract can’t say
which commitment resembles the NFT, so the commitment values need to be
constructed in a specific way by the user and submitted to Ethereum
smart contract. The NFT commitment should be a hash of NFT ID, NFT
address, owner’s ephemeral public key, and some secret value. Other,
![N-1](https://latex.codecogs.com/svg.latex?N-1 "N-1"), commitments
should be hashes of a string value NULL, the owner’s ephemeral public
key, and some other secret value. The user must provide ZK proof that
exactly one commitment is the NFT commitment while all other
![N-1](https://latex.codecogs.com/svg.latex?N-1 "N-1") values are
decoys. Each commitment is tied to a nullifier, generated as a hash of
the commitment ID, a Merkle path of the commitment inside the Merkle
tree, and the same secret value used for the specific commitment. The
secrets should be different for each commitment-nullifier pair. By doing
this setup, the public still doesn’t know which commitment is the NFT,
but anyone can verify that one of the commitments indeed is the NFT,
while others are blanks.

## Transfering NFTs on the sidechain

Users on the side chain are identified using their new ephemeral keys,
meaning the keys should be changed frequently. The keys are the private
key, public key, and encryption key. The public key is a private key
hash, while the encryption key is “the real” public key, in the sense of
public-key cryptography, derived from the private key. Transferring NFTs
is similar to tornado cash logic with the addition of decoys. For each
NFT transfer, the user also transfers
![N-1](https://latex.codecogs.com/svg.latex?N-1 "N-1") other decoys to
![N-1](https://latex.codecogs.com/svg.latex?N-1 "N-1") different
addresses. Received decoys from other users can (and should) be used in
further transfers of NFTs, thus enabling further obfuscation of the
trading paths. Each transfer on the sidechain is a shielded transfer,
meaning that it is not performed as a regular token transfer but as a
protocol backed by zero-knowledge proofs. Before explaining the
protocol, let us first see how the commitment is constructed. The
commitment contains two values, the commitment value, defined during
deposit, and a secret value used as a salt while generating the first
value. Both values are stacked in a byte array and encrypted using the
owner’s public key. When the user wants to transfer the commitment, a
new commitment and decoys are sent to the sidechain. ZK proof is also
sent on the chain, proving that all the computations were correct. The
sender proves that the new commitment is derived from the proper input
commitments and nullifiers, and the output commitments are generated in
the way that only one output commitment contains the NFT. The new
commitment is encrypted using the recipient’s public key, so only the
recipient can decrypt it and use it later. The recipient listens to the
sidechain events to see if any new commitment can be decrypted using his
private key and notes down all the commitments that pass the test.

## Withdrawing NFTs from the side chain to Ethereum

The user who initiates withdrawal must prove ownership of the commitment
representing the NFT by providing ZK proof. The user proves the
knowledge of the secret preimage used for generating the initial
commitment. When the proof is verified and valid, the commitment is
nullified. The smart contract on the Ethereum transfers the locked NFT
to the Ethereum address provided within the withdrawal request.

# Results & Discussion

The system’s building blocks are presented in the previous chapter, and
it is time to put them all together. The system architecture consists of
two smart contracts, one on Ethereum and the other on the EVM side
chain, and a validator network that can support the bridge between the
chains.

The commitment format is a slightly modified UTXO Tornado Cash
implementation used for TORN tokens, which benefits the protocol’s
safety, as it is not an entirely new, untested concept. The strength of
the protocol lies in indistinguishable commitments that are
simultaneously transferred to multiple addresses. An external viewer
cannot discern which of the commitments hide the NFT, as with each
transfer step, new
![N-1](https://latex.codecogs.com/svg.latex?N-1 "N-1") commitments are
generated or reused and transferred to obfuscate the token trail
further. The novelty introduced by the protocol lies in the initial
issuing of commitments for NFT as hashes, backed by the zero-knowledge
proofs, which guarantee that strictly one copy of the token is cloned on
the sidechain while the other copies are decoys. The proposed name for
the protocol is “The thimblerig protocol,” as it closely resembles a
street con artist who tries to hide a ball by shuffling it many times
under multiple, same-looking cups.

The downside of the protocol is the volume of commitments generated for
transferring decoys and their respective nullifiers, which are stored
locally in wallets. A proof of concept implementation is needed to
estimate better the protocol cost, efficiency, and practical usability.

# Conclusion

The presented protocol represents a combination of the existing
protocols for shielded transfers and token mixing, adapted for NFT
transfers. Generic in nature, it can be used between any two EVM chains.
The next steps should include selecting the practical use cases that
require the shielded NFT token transfers and evaluating the usability of
the presented protocol against the selected use cases. Further research
may also require a proof of concept implementation between two
designated EVM chains.

# Bibliography

<div id="refs">

</div>

\[1\]
https://www.coindesk.com/tech/2021/12/15/ethereum-mixer-tornado-cash-launches-major-upgrade-as-v3-approaches/

\[2\]
https://www.one37pm.com/nft/alt-chain-nfts-palm-sidechain-loom-network-xdai

\[3\] https://zknft.xyz

\[4\] https://bridge.mintnft.today/

\[5\] https://namada.net/

\[6\]
https://medium.com/anomanetwork/introducing-namada-shielded-transfers-with-any-assets-dce2e579384c

\[7\]
https://blog.polygon.technology/introducing-polygon-nightfall-mainnet-decentralized-private-transactions-for-enterprise/

\[8\]
https://www.coindesk.com/layer2/privacyweek/2022/01/25/monero-the-privacy-coin-explained/
