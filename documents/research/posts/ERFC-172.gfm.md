---
title: Developing with Ape
subtitle: ERFC - 172
author: Aleksandar Damjanovic
date: 4/30/2022  
---

# Executive Summary

This research examines Ape The Ethereum Development Framework For Python
Developers. It examines its plugin system and ease of use. As a
conclusion Web3 Tech Radar location is suggested.

# Introduction

Ape is a new tool for creating and exploring on Ethereum and other
blockchains. This framework is written in python with a goal of
onboarding more python developers to Web3 thus providing much needed
inclusivity in the space.

Their goal is to make development smoother with their modular approach.
Ape is centered around their open-source plugins written in python; some
of them are:

1.  Ape-hardhat - Hardhat network provider for Ape
2.  Ape-infura - Infura provider plugins for Ethereum-based networks
3.  Ape-solidity - Support for Solidity smart contracts
4.  Ape-ledger - Ledger Nano S and X plugin for Ape
5.  Ape-alchemy - Alchemy Provider plugins for Ethereum-based networks

*There are over 20 plugins Ape offers. Considering the open-source
nature of the project a lot of new plugins are on the way.*

Current version of Ape is **v0.2.1** and some of the new interesting
features offered are:

1.  Polygon, Binance Smart Chain, and Fantom support. Developers can
    build multi-chain applications with ape’s network switching feature.
2.  Impersonated account. This let’s the developers test their project
    and interact with the contract on a fork network pretending to be
    any account. If you want to impersonate Vitalik, Ape makes that
    possible.

They are also working on Ape Project Templates which should increase
productivity and enhance developers’ experience when using this
framework. Some of the templates Ape is currently developing are:

1.  NFT template
2.  Token template
3.  Various other templates for airdrops,minting
4.  Templates for different ERC standards

Ape is also set out to be the “first professional-grade smart contract
development framework to support multi-chain application development,
including non-EVM chains like StarkWare” .\[^1\]

Another sign that Ape is growing is that a Yearn.Finance repo has
[officially
migrated](https://github.com/yearn/veYFI/pull/98?utm_campaign=Updates%20from%20ApeWorX&utm_medium=email&utm_source=Revue%20newsletter)
over from Brownie to Ape.

As previosly mentioned, this is a new framework and we are expecting
more adoption and improvements in the coming months, especially as more
developers “take it for a spin”.

Another interesting thing is that there is a possibility of developers
switching to Ape from Brownie framework, as Brownie updates [have slowed
down](https://github.com/eth-brownie/brownie/issues/1515).

# Goals & Methodology

The goal of this research paper is to explore this new player in the
smart contract frameworks market, this is an opportunity to explore a
new framework that is python oriented.

This will be done by writing a simple smart contract, deployment script
for rinkeby and a couple tests for said contract and examining the
documentation and tutorials present. That way we can research the ease
of use for both beginners and experienced developers, and see what is
the approach to development process this open-source framework is
taking.

As a result Web3 Tech Radar location for this framework will be
suggested.

# Results & Discussion

**Beginner friendly?**

After initial testing of this framework and considering the state of the
documentation at this stage I would recommend this framework to
experienced python developers venturing into Web3. Documentation is well
written, still in the works and continuously updated with contributions
from the community around this framework. Apeworx Team and Apeworx
community is currently working on workshops to get developers up to
speed and tutorials are in the works.

Currently, there is little materials for newcomers. Considering this is a
new open-source project this is understandable. However, for absolute
beginners, going through the Brownie framework first is recommended at
this stage of Ape’s development. The reason for that is abundance of
tutorials, workshops and well written documentation. After Brownie,
switch to Ape and its plugin system is smooth.

**Performance:**

Ape framework performs well. Smart contract was developed and deployed
to Rinkeby test network using a python script without any problems.
Verification of the contract on Etherscan via a python script is not yet
possible but is in the works in the Etherscan plugin.

Testing works well both locally and when using network forks, which
makes exhaustive testing possible. Currently Ape doesn’t include
built-in smart contract fuzz-testing tool.

Currently the speed of the framework is satisfactory and more
improvements are on the way.

**Plugins:**

Open-source modular plugins are definitely the highlight of this
framework. It allows developers to easily install and remove the
functionality they need in their development process and I could see
this being a way to onboard new developers from the python world and a
way to incentivize developers to develop their own plugins. Some of the
interesting Ape plugins are:

**ape-tokens** is an interesting plugin which allows developers to get
token contracts without putting in the addresses themselves.

Example:

``` python
from ape_tokens import tokens

link = tokens["LINK"]

print(link.address)
```

This will print out the eth adress of the LINK token. “link” can now be
used in various python scripts, be it testing or development.

**ape-ledger** is a plugin for Ape Framework which integrates with
Ledger devices to load and create accounts, sign messages, and sign
transactions.

Requirements

-   have the Ledger USB device connected
-   have the Ledger USB device unlocked (by entering the passcode)
-   have the Ethereum app open.

Ledger accounts have the following capabilities in ape:

-   Can sign transactions
-   Can sign messages using the default EIP-191 specification
-   Can sign messages using the EIP-712 specification

**ape-trezor** is a plugin for Ape Framework which integrates Trezorlib
ethereum.py to load and create accounts, sign messages, and sign
transactions.

You can load the account like any other account in Ape console and then
use it to sign transactions like this:

``` python
ape trezor sign-message [YOUR TREZOR ALIAS] "hello world"
ape trezor verify "hello world
```

The output of verify should be the same address as the account
\$account_name.

**Ape Polygon Ecosystem Plugin** - Ecosystem Plugin for Polygon support
in Ape

**Ape Fantom Ecosystem Plugin - Ecosystem Plugin for Fantom support in
Ape**

**ape-addressbook** is plugin that allows tracking addresses and
contracts in projects and globally. This is an interesting way to
improve developers user experience and is currently in development.

*…And many more.*

# Conclusion

**Tech Radar Proposal:**

Recommended location is the Assess ring at this stage. The reason for
that is the sheer novelty of this framework. However, the development
team is great, community is growing, and we are seeing new projects
emerging using Ape. This framework is with its simplicity aiming to
become the industry standard in Ethereum development for python
developers and is on a great way to do so.


