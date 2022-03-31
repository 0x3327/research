---
title: ROTOKEN
subtitle: ERFC - 103
author: Aleksandar Veljković
date: 3/3/2022  
---

# Executive Summary

Organisations may include non-founder members with specific roles
(treasurer, secretary, board members…) with higher permission levels,
compared to the regular members. Members that have permission levels
which include control over organisation finances represent a high risk
for the organisation as there is a high risk of losing money if
malicious members perform illegal transfers. That problem is especially
present in the world of cryptocurrency where transfers cannot be
revoked, once transaction is executed there is no rollback. The use of
multisig might be an obvious solution, but the high overhead cost of
writting multiple signatures on blockchain, even if the transaction is
valid, may not be acceptable in many situations where there is a high
frequency of transactions.

This research proposes a solution for this problem, restricted to the
world of crypto-financial transactions, by introducing a rotating token
which guarantees randomised selection of members that would be granted
specified roles over fixed period of time while allowing blockchain
money-transferring transactions to be executed only by the members that
are holding the token. For improved prevention of unwanted transactions,
the transactions may be disputed before their execution, which allows
higher control over money transfers and enables improved protection of
organisation funds. All transactions are transparent to all approved
members, which adds extra layer of transparency over the entire
organisation budget.

# Introduction

Money transfer transactions are the essential parts of any organisation.
Protection of organisation finances and prevention of malicious
transactions is one of the top priorities. There is usually one, or a
few people that are responsible for all money transfers in the
organisation and are often the only members that are actually aware of
those transfers. Malicious member with access to organisation funds may
use the opportunity to leak money from the organisation for the causes
that are against the organisation rules or even against the law. Board
members of the organisation are ofter not aware of those malicious
activities as the members that perform those transaction also prepare
financial reports, hiding their tracks. An example would be a fake
invoice representing payment for the fictive service that actually
represents money laundering. Even invoice payments for the regular
services may be modified with highly increased price.

Current mechanisms for controlling financial transactions in smaller
organisations basically do no exist as every lost cent is easily
trackable when dealing with smaller amounts of money. When dealing with
large number of transactions and bigger funds, the situation is not that
clear. Bigger organisations specify budgets for certain topics,
restricting the maximum amount spent on specific topic, therefore
defining the upper limit on transaction fraud potential \[1\]. Those
budgets are not small, Microsoft Corporation spent more than 20 billion
USD on sales and marketing in 2021 \[2\]. There is a big potential for
hiding malicious transactions.

Choosing members that would be granted access to funds is currently
solved in two ways: - Hiring accounting department \[3\]. In this setup,
the employees are hired for the longer period of time, sharing the
responsibility with each other and the head of the department. -
Electing treasurer \[4\]. In this setup, the treasurer role can be
assigned to different members, often by voting. The job of the treasurer
is a person responsible for observing the accountant department, but in
smaller organisation he is often the only person dedicated to manage and
observe financial flows. The issue appears when the malicious clique
tampers the voting and forces the election of a certain trusted member
as long as they all benefit from it. There is also the case where the
treasurer role is assigned once and never changed, assuming his honest
work.

To prevent the problem, it is important to understand its cause. Newly
granted members with access to organisation funds are often working by
the book, scared of possible consequences when caught performing a
malicious activity. As the time goes by, their actions are not carefully
observed and their position in the organisation becomes stable. At that
point, the risk of malicious transactions becomes higher as the actors
are not observed and there was enough time to form a clique with other
members \[5,6\]. To quote Margaret Murray: “Governments are like
underwear. They start smelling pretty bad if you don’t change them once
in a while.” The same goes with any position of power, even if that
power includes just access to finances.

It seems that there are two main problems, unbiased change of
authorisation and transparent transaction control.

Crypto-world introduced multisig wallets for improved safety. The
problem with this approach is that it introduces costs to multiple
members for executing one transaction even if that transaction is not
malicious. The better approach would be a procedure that would add extra
cost only to prevent malicious transactions, thus saving money when the
transactions are not malicious.

Unbiased selection of participants to perform certain actions is
demonstrated in certain Blockchains where validator nodes are selected
in Round robin manner. Round robin approach may not be adequate for
selecting treasurers as it is predictable and assumes that next
treasurer will be available to accept the role. In general, unbiased
selection should be incorporated wherever there is a high risk involved
with knowing the choice in advance or where all choices should be equaly
probable. Such cases include distributing role, data or duties to
randomly selected entities, selection of randomly generated teams (such
as jury selection) and similar.

# Goals & Methodology

The main goal of this research was to find a solution for having
unbiased selection of personnel with access to finances as well as
transaction control. The way to get to the solution was to present first
all the requirements and restrictions.

The transactions that are focus of this research are blockchain
transactions. This research will focus on Ethereum money-transferring
transactions so the base element of the solutions would be Ethereum
smart contract, for this research named ROTOKEN. ROTOKEN smart contract
includes NFT token and wallet. The wallet is controlled only by the
owner of the NFT.

All listed members of the organisation should be automatically
whitelisted, meaning that all members should be able to get selected for
special roles involving access to finances. This is naturally enforced
as the salary payments are also transactions from organisation funds and
therefore controlled by the ROTOKEN smart contract.

Unbiased selection can only be performed using unbiased probability
distribution over the members that are applying for the position. The
selection needs to take into account that next selected member can’t be
the same as the previous one. Random selection on blockchain is a tricky
part as it relies on values that can be predicted in advance. One of the
sources of pseudo-randomness is the block hash, as it is a result of
SHA3 function. However, the value is predictable by the miners and it
can be tampered so it should not be used as a source of randomness.
Another approach is using verifiable random functions such as Chainlink
VRF. This might be costly but it is a good solution. This research also
proposes another, possibly cheaper approach. Selecting the latest
transaction hashes of ![k](https://latex.codecogs.com/svg.latex?k "k")
wallets outside of the organisation ,with the most frequent
transactions, and hashing them all together may be a good source of
randomness as the main problem with predictable randomness from block
hash is the ability of the miner to reorder transactions until the
desired hash is achieved. By selecting transaction hashes instead of
blocks, the only way to tamper with the randomness is to selectively
mine transactions which leaves much less room for tampered combinations
and transaction hashes are close to random as they are influenced by
many changing variables.

Selection of new members with special roles should happen regularly in
fixed intervals. As transaction of changing the role needs to be
executed on blockchain, it is required that transaction is explicitly
invoked. To incentivise regular changes, organisation funds would be
blocked for transactions until the role is changed. Role change should
not be allowed during before the end of current member’s term unless it
is invoked by the current member. The role transfer to a new member is
done by transferring ROTOKEN NFT.

Transaction that is submitted on blockchain can’t be revoked. The only
way to prevent transaction execution is to prevent its submission.
Proposed solution includes two step execution. The first step is
transaction announcement, which should be executed on smart contract and
contain details about target wallet and the amount being sent. The
second step is transaction execution, which submits pending transaction
to blockchain for execution. Between two steps, certain period of time
should be left for disputes. If the dispute is initiated by enough
participants the transaction will be canceled, where enough should be
\>51% or \>2/3, but the exact limit would be configurable value.

To disincentivise submission of malicious transactions, that would
eventually probably be disputed but also add extra cost for disputing,
submitter should be penalised. For a member to loose money it is
required that the member has the money in first place, so the safest way
to ensure successful penalisation is to include staking. The money
staked by the submitter would be lost in case of successful dispute.

Lost staked money needs to change ownership. If the money is sent to
disputers, there would exist an incentive for members to dispute every
transaction and earn money. To prevent this behaviour, the proposed
solutions is transferring money to the organisation wallet. This
solution may seem problematic and unnatural but there is an explanation
for that. One way to look at staking is to take existing money out of
the pocket. The other way is to take money “from the future”, meaning
that member may have dedicated annual fond which is used to issue
monthly payments as salary and may also be perceived as staked money. In
this case, the penalisation would assume reduction of the future salary
which technically is returning money back to the organisation. To
further disincentivise disputes from the side of the organisation
executives, disputed transaction, defined by the receiver’s address and
the amount of money to be transferred, blocks further transfers to
receiver’s address for certain amount of time. If the disputed
transaction was indeed malicious, this mechanism will block further
transactions to that address, preventing new attempts. If the
transaction was falsely disputed and the receiver is a proper receiver
of organisation’s money, by preventing the transaction and blocking the
transfer to the proper receiver, the behaviour directly disrupts regular
functioning of the organisation.

# Results & Discussion

ROTOKEN smart contract should follow modifier ERC-721 smart contract.
Token transfer should be possible only by internal call and the token
should be transferred to randomly selected whitelisted member.
Additionally, the smart contract should include: - list of whitelisted
members, with getters and setters - list of transactions with statuses -
dispute function - transaction announcement and execution functions -
ownership change function, which would internally call transfer function

Proposed ROTOKEN smart contract interface:

    interface ROTOKEN {
        // + ...ERC-721 interface

        Enum { PENDING, DISPUTED, CANCELED, FAILED, EXECUTED } transactionStatus
        struct (
            transactionStatus status,
            address currentTokenOwner
            address receiver,
            uint256 amount,
        ) transactionData;

        mapping(transactionId => transactionData) public transactions
        address[] whitelistedMembers;

        event TransactionStatusChanged(uint256 indexed transactionId, transactionStatus status)

        function announceTransaction(address receiver, uint256 amount) public returns(uint256 transactionId);
        function executeTransaction(uint256 transactionId) public;
        function dispute(uint256 transactionId) public;
        function changeOwnership();
    }

## Potential markets

Potential markets that might be interested to use ROTOKEN include: -
DAOs - Companies with frequent audits by the investors, board members or
shareholders, mostly startups - Banks - Government organisations related
with public government funds

# Conclusion

ROTOKEN smart contract proposes solutions for unbiased selection of
members for granting control over organisation funds and incentive based
transaction control. Minimal additional operating costs required for
essential control are added, on top of regular transaction costs. The
smart contact extends ERC-721 interface with certain modifications and
extensions which makes ROTOKEN NFT compatible for integration with the
existing systems where the ERC-721 tokens are used. Those systems may
use the information about the ownership of the ROTOKEN to grant the
owners additional privileges, like document signing, voting etc. Next
steps include market evaluation, PoC implementation and detailed
operating cost estimation.

# Bibliography

<div id="refs">

\[1\]
https://corporatefinanceinstitute.com/resources/knowledge/finance/financial-controls/

\[2\]
https://www.statista.com/statistics/506534/microsoft-sales-marketing-expenditure/

\[3\] https://www.investopedia.com/terms/a/accountant.asp

\[4\] https://nonprofitlawblog.com/treasurer-duties/

\[5\]
https://corporatefinanceinstitute.com/resources/knowledge/other/fraud-red-flags/

\[6\]
https://www.nsu.edu/About/Administrative-Offices-Services/Internal-Audit/Making-a-Report/Red-Flags-of-Fraud.aspx

</div>
