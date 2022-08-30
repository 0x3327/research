---
title: NFT that is bound by time
author: Marija Mijailovic
date: 3/14/2022 
---



# Executive Summary

NFTs have a unique ID and belong to a single wallet. Two standards define what an NFT is and should do: ERC721 and ERC1155, aiming to distinguish each token to be unique. The development of NFT is still in the early stage, and this research shows how NFTs can change their properties. We go through some existing solutions where some events fundamentally affect the NFT, changing its state, properties, or value. We give an overview of those solutions with a desire to cover how they work under the hood and notice potential problems. In the end, are presented possible use cases that open a new door into the NFT word.

# Introduction

NFTs (Non-Fungible Tokens) reached incredible popularity in 2021 Ryan Browne[^1].
Most of created NFTs are static. We collect it, and we hope its
market value will increase. In the case of *static* NFT, it's
characteristic that its properties and data are immutable and recorded
on the blockchain, so such NFTs can't be changed. Otherwise, there are
*dynamic* NFT for which it's characteristic that properties and data are
mutable, often through oracles that trigger events off-chain system or by
interaction with on-chain components, for example, smart contracts other
NFTs.

> "Dynamic NFTs are the logical next step for the NFT space, allowing unique items to evolve, and sometimes decay. This replicates the ephemeral nature of the real world and potentially gives exceptional value to a collected item because of its current state. NFTs transitioning from being 'only' static to being dynamic can be thought of as progressing from 2D to 3D, it enables an immense possibility of use cases." --- Adrien Berthou, Head of Crypto-Native Comms at DoinGud

# Goals & Methodology

The goals of this research:

-   Introduce with dynamic NFT
-   Search for project that make evolvable NFTs
-   Research how they work, find some leak
-   Suggest improvements

Methodology for accomplishing those goals:

-   Getting under the hood of open source solutions
-   Testing existing approach
-   Solidity

# Results & Discussion

First of all, let's briefly review some existing projects:

-   [EtherCards](https://ether.cards/)
    -   EtherCards is a dynamic NFT platform that allows anyone to give a base set of traits and requirements and launch their NFT collection so that the EtherCards team can create unique NFTs. Traits can be discounts, special access rights, connections to real-world events, airdrops, upgrades, and other benefits. The ability to have traits allows the creator to maximize the value of their art. Ether Cards is an integrated ecosystem composed of two major parts. Those are the platform and the Ether Cards (an advanced membership NFT card). Anybody can use the EtherCards platform, but the owner of the EtherCards card has certain privileges. Under the hood, EtherCards integrate Chainlink VRF to provide verifiable randomness on-chain. Chainlink allows developers to read data from any external API and blockchain network and perform off-chain computation. That will enable NFTs to be connected to the external world to trigger real-world events, in a word, to be dynamic.
    -   EtherCards have supported and worked with [LaMelo Ball](https://blog.ether.cards/lamelo-ball-nft/), [Mike Tyson](https://nfttyson.com/), [Steve Aoki](https://blog.ether.cards/steve-aoki-partners-with-ether-cards-to-produce-new-animated-nft-collection-dominion-x/) and [DirtyRobot](https://blog.ether.cards/artist-profile-dirty-robot/). In the above collections, all NFTs metadata are stored `https://client-metadata.ether.cards` on the central server. Within that metadata is a link that points to NFTs image on IPFS. So, inside the smart contract, we store points to metadata JSON URIs to all variants of one NFT. Later, inside `tokenURI` function with the support of Chainlink return dynamically created URI of NFT, only one variant.
-   [Loopheads](https://www.loopheads.info/)
    -   Loopheads is a Loopring 'Loopring - <span class="nocase">zkRollup Layer2</span> for Trading and Payment'[^2] *Moody Brains* NFT collection, minted on Looprings Layer 2. There are 25 variants for one Loophead avatar(5 different backgrounds and 5 different brain sizes), which one will be displayed depending on the LRC token price using Uniswap Oracles.
    -   All NFT metadata are stored on decentralized storage - IPFS, within that metadata, is a link that sends to NFT's image on IPFS. So, inside the smart contract, we store points to metadata JSON URIs to all of the Loophead's variations. When a Loophead NFT is accessed because Loopheads use ERC1155 standard, the Loophead NFT runs the `uri` function, the start point of dynamic calculation, to show the loophead avatar. The calculation is done with the support of Uniswwap V3 Oracles. That changes parts of the metadata link based on LRC price and returns only one variant.
-   [Uniswap LP NFT](https://docs.uniswap.org/protocol/reference/periphery/libraries/NFTDescriptor)
    -   On Uniswap V3 liquidity provider(LP) position is represented as NFT. This NFT shows information about liquidity position. Based on the pool and your parameters selected on the liquidity providing interface. The unique NFT will be minted, representing your position in that specific pool. As the owner of this NFT, you can modify or save the position. The best part of this project is that NFT is SVG generated entirely on-chain. Because of that, it is secure as an image not rely on any other service that is not on the blockchain, and it affects the price of that NFT.
    -   All liquidity parameters for NFT are stored on-chain. Interesting is that SVG generation is done inside a pure function, and it returns base64 encoded metadata from the view function.
    -   When a Uniswap V3 LP NFT is accessed because it uses the ERC721 standard, it runs the `tokenURI` function, which is the start point that generates SVG from liquidity parameters and returns base64 encoded metadata.
-   [Aavegotchi](https://www.aavegotchi.com/)
    -   Aavegotchi is a crypto collectible game. It was developed to provide users with a new blockchain-based game powered by dynamic NFTs. Aavegotchi information such as Aavegotchi name, traits, and SVG files themselves are saved as contract calldata because it is less gas cost than store in contract storage. The fundamental element of Aavegotchi's game is randomness. Because of that, they use Chainlink VRF. The main idea behind the game is that the more you love your Aavegotchi character, the more rewards it will give you.
    -   To store SVG, we pass one or more SVG images as a string, along with the information of SVG category type(aavegotchi, collaterals, eyeShapes, wearables) and size of passed SVG images. So inside `tokenURI` we have all NFTs prepared to return only one determined based on real-life events.

You can quickly determine where your NFT is by calling the `tokenURI` or `uri` function on the contract, which returns a URI that points to metadata that shows where NFT lives. Above project for NFT storage use:

-   Centralized server
-   Decentralized storage (IPFS, Filecoin, Arweave)
-   On-chain storage

The problem with the central server is that the possibility for manipulation is vast. The server owner can change the JSON scheme of your NFT whenever he wants.

The problem with IPFS is that there is no defined way of data replication. It just happens depending on the relevance of the content. In addition, the IPFS node can become offline. The problem is that if the relevance of our data is minor, the bigger is chance to lose data. To resolve the issue, Filecoin and Arweave come into play. Filecoin is a solution where we pay some price to store data for a set time. The problem is that we are limited by time, so our data are not stored permanently. Arweave is a solution that incentivizes the nodes to hold data permanently by paying only one fee in the Arweave token and keeping data forever. The most significant leak here is that it all comes down to having one storage layer that is separate from the blockchain and from the NFT itself on which it is located.

When it comes to on-chain storage, the SVG is scalable because it does not rely on pixels to display the image. SVG is used for vector graphics where we can describe shapes and lines mathematically. But, if we want to present a more complex image in this format, we get a massive SVG file, which will lead to a considerable gas cost. Additionally, the worth of mention is [EIP-2569](https://eips.ethereum.org/EIPS/eip-2569).

-   EIP-2569 is an Ethereum improvement proposal to allow a smart contract to save and retrieve an SVG image. Based on that, the two methods contract must have: `getTokenImageSvg(uint256) view returns (string memory)` and `setTokenImageSvg(uint256 tokenId, string memory imagesvg) internal`. As we can see, the potential flaw of function `setTokenImageSvg` as input parameter accepts SVG image string, which can lead to a considerable gas cost in case of complex SVG.

There is no obstacle to the realization of any project that would require the evolution of NFT. Everything needed is that our contract overrides the `tokenURI` or `uri` function from ERC721 or ERC1155. Therefore, the precondition is that we have prepared all parameters variants for the dynamic generation of potential variants. The project specification itself decides which variants to return within it.

``` javascript
  function tokenURI(uint256 tokenId) public view override(ERC721) returns (string memory) {
    require(_exists(tokenId));
    return generateDynamicNFT(tokenId);
  }
```

``` javascript
  function uri(uint256 tokenId) public view override(ERC1155) returns (string memory) {
    require(_exists(tokenId));
    return generateDynamicNFT(tokenId);
  }
```

Inside `generateDynamicNFT`, the user defines how and under what conditions NFT to generate, usually using oracles.

# Conclusion

This research has shown that it is possible to change the data and properties of NFTs, and the next evaluation in NFT is moving from static NFTs to dynamic NFTs. With dynamic NTFs, some use cases could be:

-   An NFT ticket that could retain a value after the event is finished can turn as a discount for a related event or, as some bonus, gifts.
-   Sports NFT cards can evolve, such as updating their player's stats or having a limited edition of sports event cards if the player got a super score in a match.
-   Sport NFT cards that receive bonuses or losses based on wins/losses.
-   Artist NFT cards that change on a daily/monthly based.
-   NFTs affected by social media/real-life events.
-   NFTs that affect the real world, where a user can receive a physical item in exchange for NFT.
-   Kata NFTs were on the users' progress the Kata NFT will change.
-   Geometric shape that change as price change

The only related problem is about on-chain storage assets. Most NFTs do not store their assets directly on the blockchain because the cost of keeping them on-chain is expensive, as every action and every byte of information we hold on the blockchain has a fee. In addition, the Ethereum blockchain is designed to keep a record of transactions and not to serve as a data warehouse. Second, on-chain geometrical arts can quickly present, but for the more complex SVG files, it is possible to use *the bottom-top* approach. The idea is to have one zero-based image as a base and then add traits dynamically to the base image. Where will store only characteristics on-chain, and the NFT image is created dynamically.
On-chain storage reduces external dependence, increasing reliability, durability, ownership, and decentralization. Keeping assets on-chain has excellent value. Users can rely on the same guarantees of immutability they use to secure property ownership, and the value of such art is more significant. When the asset is being followed on the Ethereum, we also want that asset to be placed on the Ethereum somehow.

# Bibliography

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-browneTradingNFTsSpiked2022" class="csl-entry">

Browne, Ryan, 'Trading in NFTs Spiked 21,000% to More Than \$17 Billion in 2021, Report Says', *CNBC*, 2022 \<<https://www.cnbc.com/2022/03/10/trading-in-nfts-spiked-21000percent-to-top-17-billion-in-2021-report.html>\> \[accessed 24 March 2022\]

</div>

<div id="ref-LoopringZkRollupLayer2" class="csl-entry">

'Loopring - <span class="nocase">zkRollup Layer2</span> for Trading and Payment', *Loopring* \<<https://loopring.org/#/>\> \[accessed 24 March 2022\]

</div>

</div>

[^1]: ['Trading in NFTs Spiked 21,000% to More Than \$17 Billion in 2021, Report Says', *CNBC*, 2022 \<<https://www.cnbc.com/2022/03/10/trading-in-nfts-spiked-21000percent-to-top-17-billion-in-2021-report.html>\> \[accessed 24 March 2022\]](#ref-browneTradingNFTsSpiked2022).

[^2]: [*Loopring* \<<https://loopring.org/#/>\> \[accessed 24 March 2022\]](#ref-LoopringZkRollupLayer2).
