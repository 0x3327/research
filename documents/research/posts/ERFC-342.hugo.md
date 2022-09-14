---
title: "[ERFC - 342] Intro to the Cosmos Network"
author: Milos Bojinovic
date: 7/24/2022
---



# Executive Summary

Since its inception, Ethereum\[1\] has enabled smart contract
functionality by introducing Ethereum Virtual Machine (EVM). This
enabled the possibility of creating many different decentralized
applications (DApps). Ethereum is a public general purpose blockchain
where everyone can participate, deploy applications and compete for the
chain's resources.

This idea of a general purpose chain capable of handling multiple
applications has certain limitations. The most important is the issue of
scalability, where in times of network congestion, transaction fees
skyrocket, leading to an awful user experience.

The other significant issue is that DApps suffer from a "two-layer"
governance system. Besides honoring its rules, a DApp must honor the
rules imposed by the protocol. It would be unfeasible to alter the
protocol each time there's a need to enable some feature for one of the
DApps.

Besides Ethereum, there are other Layer 1 chains with different
approaches. However, they are in ruthless competition with each other.
They cannot effectively communicate, which leads to the segmentation of
space and slowness of adoption.

Cosmos\[2\] proposes and enables a separate sovereign, parallel, and
optimized chain for each DApp. These independent chains can be
separately altered and upgraded on a protocol level while maintaining
communication. This cross-chain communication can, under certain rules,
be achieved both for new as well as existing chains.

This different way of thinking should be taken seriously as user
experience will most likely be the main factor in the race for mass
adoption. With 68.72 billion USD worth of assets present in the Cosmos
ecosystem\[3\], this approach shows great potential and should be
investigated further.

# Introduction

**Blockchain can be viewed as a replicated state machine that follows a
predefined deterministic transition process.**

From the architecture's standpoint, any blockchain on Cosmos is formed
using three layers:

-   **network layer** meant to discover nodes that form a peer-to-peer
    (P2P) network and propagate transactions as well as consensus
    messages between those nodes
-   **consensus layer** responsible for reaching an agreement between
    nodes of this P2P network
-   **application layer** which defines the state and the rules under
    which a transaction can alter it

This non-monolithic approach to building a blockchain is supported by a
set of tools where:

-   network and consensus layer (responsible for the replication of
    state across the nodes) are handled by the Tendermint Core\[4\],
    which communicates with the application layer through an Application
    Blockchain Interface (ABCI)\*
-   application layer and its equivalent state machine is created using
    the Cosmos SDK\[5\]

*\*Tendermint Core and ABCI together comprise Tendermint BFT*

Using Inter Blockchain Communication (IBC), each Cosmos blockchain can
connect with others. IBC also provides a mechanism for connecting with
other non-cosmos chains.

# Goals & Methodology

This exploratory research into the Cosmos project mainly focuses on
understanding the architecture and its capabilities. The paper showcases
its features and briefly discusses their potential.

However, the research does not go into the specifics of the Cosmos'
tools nor the projects that have been built. Each tool in the Cosmos'
stack should be a part of separate further research.

# Results & Discussion

## Cosmos Blockchain

### Tendermint Core

Tendermint Core handles peer-discovery, validator selection, staking,
upgrades, and consensus. In doing so, it heavily relies on:

-   **Delegated Proof-of-Stake (DPoS)** where validators and delegators
    vote on proposals with weights proportional to the amount they've
    staked.

    -   Validators accept the block by providing their signature. When
        the new block's creator gathers the necessary signatures, it is
        finalized, and it cannot be overturned.
    -   In a blockchain running on Tendermint, transactions have
        absolute finality, and hard forks should not happen.

-   **Practical Byzantine Fault Tolerance** guarantees that the
    blockchain will continue functioning even if up to 1/3rd of machines
    fail or become malevolent.

### ABCI

The ABCI is an interface between Tendermint Core and the application
layer. It consists of three main message types:

-   **AppendTx** - each transaction is delivered with this message. The
    application layer checks the transaction's validity against the
    application's state and protocol. As well as if all of the necessary
    signatures are present.
-   **CheckTX** - performs lower resolution checks (only checks in the
    transaction context are performed)
-   **Commit** - computes a commitment of the current state which will
    be put into the new block's header

### Application layer

It is worth explicitly noting that which was implied in the previous
paragraphs: **Tendermint doesn't concern itself with the interpretation
of transactions and is unopinionated about their meaning - this is the
function of the application layer.**

The main focus for most developers involves making changes to the
application layer through a framework written in Golang - [Cosmos
SDK](https://docs.cosmos.network/). The application layer can be broken
down into "modules," which are built to have a single purpose, thus
achieving separation of concerns. These modules are then combined to
enable the intended functionality of the new blockchain.

Overall, the development process consists of:

-   defining "messages" which are the main part of the transactions, and
    where:
    -   each transaction can contain multiple messages
    -   each message has a destination module responsible for processing
        the message
-   defining "handlers" for those messages that are called when the
    corresponding message is received
-   defining "queries" that will provide a REST API through which the
    information about the chain's state can be retrieved and displayed
    to the user

One additional tool that eases the development, especially in the
beginning, is the [Ignite CLI](https://docs.ignite.com/). This tool
scaffolds pieces of code in the project and is extremely useful for
newcomers.

To connect to the chain and to build, as well as issue, transactions,
developers should use
[CosmJs](https://tutorials.cosmos.network/academy/5-cosmjs/cosmjs-intro.html),
a Javascript/Typescript library with which it's relatively easy to
integrate with [Keplr wallet](https://www.keplr.app/). CosmJs needs to
know the types of messages in order to build a transaction; this is a
somewhat time-consuming process as it needs to be done manually through
a terminal - for more info, visit [Create Custom CosmJS
Interfaces](https://tutorials.cosmos.network/academy/5-cosmjs/create-custom.html)

## IBC

### Zones and Hubs

Each independent Cosmos blockchain is referred to as a "zone". Zones can
be connected to "hubs" - blockchains dedicated to managing the
communication of zones and their assets.

The Cosmos whitepaper\[2\] states:

> From the Hub's perspective, a zone is a multi-asset dynamic-membership
> multi-signature account that can send and receive tokens using IBC
> packets. ...

> Like a cryptocurrency account, a zone cannot transfer more tokens than
> it has, but can receive tokens from others who have them. A zone may
> be designated as an "source" of one or more token types, granting it
> the power to inflate that token supply.

Any of the zones can themselves be hubs to form an acyclic graph.
Currently, only one hub exists - "Cosmos Hub"\[6\], which is the
economic center of the whole ecosystem.

Hubs keep up with the state of each zone by the block commits that each
zone posts. Zones, however, do not keep track of each other's state.
Information packets are transferred from one zone to another by posting
Merkle-proofs which signal that the packet was sent/received.

### IBC layers

IBC is comprised of two layers:

-   Transport (sometimes referred to as the "Transport, Authentication
    and Ordering" (TAO)) layer is responsible for providing the
    infrastructure to establish communication lines between chains in
    order to transport the packets between the source (sending) and
    destination (receiving) chain
-   Application layer specifies how data from the packets should be
    structured and interpreted by the sending/receiving chain

#### Transport layer

The transport layer's components include:

-   **light clients** - which are a blockchain's light representation.
    They are designed to connect to a full node and verify the block
    headers. Two zones (or zone and a hub) interacting over IBC must
    contain light clients of the other chain. Interestingly, these two
    chains do not send messages directly to each other but via
    "relayers".
-   **relayers** - permissionless off-chain processes constantly
    monitoring for the presence of the messages in the chain's state
    machine. To do this, they need access to a full node of both chains
-   **connections** - connect light clients of two different chains and
    can have an arbitrary number of "channels"
-   **channels** - route packets to the intended modules; In order to
    facilitate two-way communication between chains A and B, a 4-step
    handshake is required:
    -   the first message originates from A and signals the
        initialization attempt to chain B
    -   the second message is sent from B that corresponds to the
        attempt to open a channel on chain A
    -   the third message is an acknowledgment message sent from A to B
        that states that A's channel is open
    -   the fourth message is the confirmation sent from chain B to
        chain A that that B's channel is also open

#### Application layer

The application layer sits on top of the TAO layer and supports, among
others, these functionalities :

-   **fungible (ICS20\[7\])** / **non-fungible token (NFT -
    ICS721\[8\])** transfers
-   **Interchain Accounts ICS27\[9\]** enable cross-chain interaction -
    any action that can be performed on the "host" chain can be
    initiated from the "controller" chain. From the host chain's
    perspective, interchain accounts are just regular accounts
    controlled via IBC messages instead of having a private key.
-   **Interchain Security** allows for a "provider" chain to be in
    charge of producing blocks for a "consumer" chain.
-   **Fee middleware** is used to pay the costs and incentivize the
    operation of relayers
-   etc.

# Conclusion

This paper has provided a high-level overview of the Cosmos, which has
taken a seriously thought-out approach to building blockchains. Its
radical way of making the difficulty of developing an
application-specific chain comparable to the development of a DApp on a
general purpose chain is worth considering during the initial design
stage of any project.

There are three major directions in which further research should be
conducted:

1.  diving deep into the projects built using Cosmos. One example of an
    interesting project is Evmos\[2\], a scalable, high-throughput PoS
    blockchain fully compatible and interoperable with Ethereum
2.  assessing the capabilities of the Cosmos SDK
3.  exploring the ways IBC can connect zones with Proof-Of-Work (PoW)
    chains

Tendermint Core shouldn't be a priority as it is a relatively old
consensus mechanism and can be replaced by newer ones as long as they
are adapted to honor the ABCI.

# Bibliography

\[1\] https://ethereum.org/en/whitepaper/

\[2\] https://v1.cosmos.network/resources/whitepaper

\[3\] https://cosmos.network/ecosystem/tokens/ (Accessed on 07/08/22)

\[4\] https://github.com/tendermint/tendermint

\[5\] https://v1.cosmos.network/sdk

\[6\] https://hub.cosmos.network/main/hub-overview/overview.html

\[7\]
https://github.com/cosmos/ibc/blob/main/spec/app/ics-020-fungible-token-transfer/README.md

\[8\]
https://github.com/cosmos/ibc/tree/main/spec/app/ics-721-nft-transfer

\[9\]
https://github.com/cosmos/ibc/blob/main/spec/app/ics-027-interchain-accounts/README.md

<div id="refs">

</div>
