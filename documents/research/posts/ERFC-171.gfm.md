---
title: Royalty Contract Standardization - RCS
subtitle: ERFC - 171
author: Aleksandar Damjanovic
date: 5/12/2022
---

# Executive Summary

This research examines the possibility of hardcoding the royalty logic
for the NFT royalty payments. It also explores how are royalties for NFT
creators/artists taken care of by two largest NFT marketplaces OpenSea
and LooksRare. It examines the EIP-2981 which aims to solve the royalty
implementation problem. Small experiment is conducted with a goal to
modify the transfer function from the ERC-721 standard.

After explorative research and a short experiment we have come to these
conclusions:

1.  The Marketplaces prefer handling the royalties themselves and only
    for the trades on their platform
2.  ERC-2981 contains the optional royalty implementation logic. It’s on
    the platforms to decide whether they will utilize this standard.
3.  Hardcoding royalties without making “a mess” of the NFT
    smart-contract is currently way too complex and would require
    altering the ERC-721 heavily.

# Introduction

Current marketplaces and NFTs have fragmented royalty payment
implementations. This leaves the nft artist/creator with the issue of
unpredictable royalty payments for his art. Each marketplace has
different solutions for this problem. EIP-2981 has basic royalty
implementation. Which doesn’t enforce actual payments. Royalty Contract
Standardization (RCS) could in theory be done by modifying the transfer
functions to enable the transfer of royalties to the creator during
trading of the NFT via transaction splitting.

**This research is the aftermath of a brainstorming session and has some
brave assumptions initially, which is why this short research is
conducted to further validate those assumptions.**

# Goals & Methodology

The goal of this research is to explore how royalties are taken care of
currently and the way EIP-2981 works and the possibility of further
improvement.

This will done by doing an explorative research of current royalty
implementations on OpenSea and LooksRare as they are the biggest
players.

Another examination will be done, maimly of the EIP-2981 standard to
explore the solution it proposes.

Afterwards we will examine the possibility of hardcoding royalty in the
NFT contract itself.

# Results & Discussion

## OpenSea

OpenSea offers royalties for Artists and Creator which are usually
around 10%. They are also applied to secondary sales and the proceeds
after fees go to the seller of the NFT.

Users can check the royalty fees with 3 methods:

1.  Attempting to buy an NFT which will then open up a checkout window
    where the royalty amount is listed under the name of the NFT.
2.  Installing the Flava Chrome extension which shows the royalty next
    to the NFT without needing to open the checkout menu.
3.  Using the NFT analytics tools - There are numerous NFT analytics
    tools that include creator royalties in their stats.[^1]

As we can see royalties are very important part of NFT space and they
are of great importance for both traders and creators.

### How do creators earn their royaties

On OpenSea proceeds from the primary sales of the NFT are immediately
forwarded to the creators address. Royalties are usually held by OpenSea
for 2-4 weeks before paid out to the creator, this includes **both
primary sales and secondary sales**.

Royalties are not automatically set on OpenSea and the creator of the
collection must set the royalty percentage and the payout address on the
collection level.

### OpenSea royalty on other marketplaces

OpenSea royalties are enforced on many other platforms. This is a result
of various legal agreements between platforms.

If we are talking about ERC-721 and ERC-1155 standard tokens there is no
royalty support on token or smart contract level. That is why previosly
mentioned legal agreements are needed to enforce royalty payments.[^2]

## LooksRare

LooksRare is a decentralized NFT marketplace which rewards traders,
token stakers, creators and collectors for participating on the
platform.

It was launched in January 22 with an aim to dethrone Opensea from it’s
spot as a leader in the NFT market.

As a community-first platform all the revenue generated is distributed
to the stakers of LOOKS token.

### Token

LOOKS is the native token that powers the LooksRare marketplace, its
price is \$0.5908 at the time of this writing. It is used for staking
and various rewards.

### Royalties

Whenever the NFT is traded on LooksRare there are 2 types of fee the
seller is charged:

-   Platform fee (2%)
-   Creator royalties

“Creator royalties are fees that are decided by the collection creator.
Collection owners can specify a percentage of royalties they wish to
recieve on their collection management page.”

Royalties are on-chain. Whenever a sale is made through the platform the
royalties are paid in the same transaction as the sale and the creators
instantly recieve their royalty. This is one of the ways LooksRare is
different from OpenSea.

LooksRare also supports EIP-2981 royalty standard which takes precedent
over any royalties specified directly on LooksRare.

## EIP-2981

This standard provides a way to retrieve royalty payment information for
NFTs with a goal to enable universal support for royalty payments across
all NFT marketplaces and ecosystem participants.

This standard enables all marketplaces to retrieve royalty payment
information for a given NFT. This enables accurate royalty payments
regardless of which marketplace the NFT is sold or re-sold at.

This standard only provides a mechanism to fetch the royalty amount and
recipients. The actual funds transfer is something the marketplace needs
to do.

“Royalty amounts are always a percentage of the sale price. If a
marketplace chooses not to implement this EIP, then no funds will be
paid for secondary sales.”

**That is one of the reasons hardcoding royalties idea was proposed.**

EIP-2981 can also be integrated with other contracts to return royalty
payment information. **ERC-2981** is a royalty standard for many asset
types.

It is recomended to read the full specification of the proposal in order
to better understand the issue at hand and the way it is handled in the
[EIP-2981](https://eips.ethereum.org/EIPS/eip-2981).

In the proposal the writers have come to these conclusions:

-   “It is impossible to know which NFT transfers are the result of
    sales, and which are merely wallets moving or consolidating their
    NFTs. Therefore, we cannot force every transfer function, such as
    transferFrom() in ERC-721, to involve a royalty payment as not every
    transfer is a sale that would require such payment.”

-   “It is impossible to fully know and efficiently implement all
    possible types of royalty payments logic. With that said, it is on
    the royalty payment receiver to implement all additional complexity
    and logic for fee splitting, multiple receivers, taxes, accounting,
    etc. in their own receiving contract or off-chain processes.
    Attempting to do this as part of this standard, it would
    dramatically increase the implementation complexity, increase gas
    costs, and could not possibly cover every potential use-case.”

-   “This EIP mandates a percentage-based royalty fee model. It is
    likely that the most common case of percentage calculation will be
    where the royaltyAmount is always calculated from the \_salePrice
    using a fixed percent i.e. if the royalty fee is 10%, then a 10%
    royalty fee must apply whether \_salePrice is 10, 10000 or
    1234567890.”

-   “This EIP does not specify a currency or token used for sales and
    royalty payments. The same percentage-based royalty fee must be paid
    regardless of what currency, or token was used in the sale, paid in
    the same currency or token. This applies to sales in any location
    including on-chain sales, over-the-counter (OTC) sales, and
    off-chain sales using fiat currency such as at auction houses. As
    royalty payments are voluntary, entities that respect this EIP must
    pay no matter where the sale occurred - a sale outside of the
    blockchain is still a sale.”

They also plan on taking on the mechanism for paying and notifying the
recepient in the future EIPs.[^3]

### Our experiment

After trying to implement hardcoding the royalties the same issue with
the transfer function occured.

```js
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "@openzeppelin/contracts@4.5.0/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts@4.5.0/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts@4.5.0/access/Ownable.sol";
import "@openzeppelin/contracts@4.5.0/utils/Counters.sol";
import "@openzeppelin/contracts@4.5.0/interfaces/IERC2981.sol";

contract InstantRoyaltyToken is ERC721, ERC721Enumerable, Ownable, IERC2981 {
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    address royaltyAddress;
    uint256 royalty = 10_000;

    constructor(address _royaltyAddress ) ERC721("InstantRoyaltyToken", "IRT") {
            royaltyAddress = _royaltyAddress;
    }

    function safeMint(address to) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
    }

    // The following functions are overrides required by Solidity.

    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable, IERC165)
        returns (bool)
    {
        return interfaceId == type(IERC2981).interfaceId || super.supportsInterface(interfaceId);
    }

    function royaltyInfo(uint256 tokenId, uint256 salePrice) public view override returns(address receiver, uint256 royaltyAmount) {
        return (royaltyAddress, royalty);
    }
    /* 

        * The function below from ERC721 is the main issue. Making this a
        * payable function would add unecessary complexity to the standard
        * and would make the function payable, thus requiring payment 
        * even when sales are not ocurring.

    */
    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) public virtual override(ERC721,IERC721) {
            require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: transfer caller is not owner nor approved");
            //royaltyInfo and pay royalty for transfer part would go here
            //implementing this would make the function payable
            _transfer(from, to, tokenId);
    }

}
```

# Conclusion

After researching how the royalties are taken care of so far by the
leading NFT marketplaces we have come to these conclusions:

1.  The Marketplaces prefer handling the royalties themselves and only
    for the trades on their platform
2.  ERC-2981 contains the optional royalty implementation logic. It’s on
    the platforms to decide whether they will utilize this standard.
3.  Hardcoding royalties without making a mess of the NFT smart-contract
    is currently way to complex and would require altering the ERC-721
    heavily.

The above reasons are the reason for not going further with this
initiative, however this gave us a better insight of how the NFT
marketplaces operate in terms of royalties and how are the new standards
for NFTs proposed, and what are the limitations.

*Special thanks to Stevan Bogosavljevic for his opinions on this
research and expertize in NFT royalties. Thank you for showing the
fallacies in the logic of this research proposal*


# Bibliography


[^1]: [**NFTAnalyticsTools2022?**](#ref-NFTAnalyticsTools2022)

[^2]: [**10SettingFees?**](#ref-10SettingFees)

[^3]: [**EIP2981NFTRoyalty?**](#ref-EIP2981NFTRoyalty)
