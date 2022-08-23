---
title: Access NFT Tools - Overview And Space For Improvements
author: Milos Novitovic
date: 2/21/2022 
---



# Executive Summary

NFT Access tokens are primarily used to join private Discord and Telegram communities. Still, a significantly larger opportunity lies in many online and offline communities and events that might utilize this technology.[^1]

On the other side, there is a privacy concern with some tools that might be a deal-breaker. More precisely, tools used to identify whether a specific user holds an NFT might connect a user's identity (e.g., Discord/Telegram name, SM account, etc.) with their wallet address and the amount of money they possess.
Yet, we believe that ZK technology can be used to bridge that gap between privacy and utility.

However, before we deep-dive into creating a tech spec and building a PoC solution, we wanted to research whether our presumptions are correct, whether current collusion works as we assumed and whether there is space for technical improvement (innovation).

# Introduction

This research is about understanding the state-of-the-art within the Access NFT tools niche, tools used to gate content (websites, blog posts, Discord, Telegram communities, etc.) and allow users to access it only if they hold a specific token (NFT).

Additionally, it is about verifying our presumption that there is privacy concern and space for technical improvement within current tools that allow access to Discord and Telegram communities.

Once the above is carried out, and if our presumption is confirmed to be accurate, we will have a chance to work on tech innovation, which will utilize the ZK technology.

Such a tool will do the same job as existing solutions by providing information to Discord and Telegram servers whether a specific user holds an NFT or not, but, it won't keep track and centrally store connections between the users' ID and their wallet addresses (the amount of crypto they possess).

Also, this research and idea are not about creating better and more user-friendly solutions. The current ones are fine from that point of view, but it is about creating more secure and privacy-improved solutions.

# Goals & Methodology

## Goals

1.  Identifying content gating tools (that works).
2.  Understanding how they work.
3.  Recognizing use cases that they are used for, the problems they aim to solve.

It is essential to overview current solutions in the field we aim to dive into. Both, short-term, for this research and experiment, ut also long-term, for being able to actively track all the innovation in this field from now on.

4.  Verify our presumption about how current solutions are used to gate Telegram and Discord communities: Through using centralized services and storing the user's private information (wallet address and username), existing solutions periodically verify the user's possession of specific NFT.

The main goal of this research is to verify our presumption that there is privacy concern and space for tech improvement within the Access NFT tool niche.
If it is accurate, and if the current solution keeps track and connection between private users' data, we can conclude that there are reasons to move forward with this idea and start working on technical specifications and research how it can be developed.

## Methodology

-   Trying out and using existing solutions.
    We aimed to try each solution available on the market as we believe it is the only way to understand how it works and what problems it solves.

-   Consult and discuss with team and community members via contact forms or community servers
    We want to confirm that our understanding of how a specific tool works and what lies under the hood is correct. Hence, the best way is to receive confirmation from the people building and using it, especially when those tools are not open-sourced.

-   Analyze other reviews
    There are blog posts, websites, and apps that have already analyzed and gathered information about the current state of Access NFT tools. Thus, we do not need to do all of this work again, as we can benefit from their insights and overviews. Still, this does not mean that we will take it for granted. We want to do our research as well.

\*We were not looking under the hood (going through the code).
Most of the solutions are not open-sourced. Also, we could understand how they work by consulting with the community and team members behind these solutions.

# Results & Discussion

First of all, our hypothesis/assumption appeared to be correct:
By using centralized services and storing the user's private information (wallet address and username), current solutions periodically verify the user's possession of specific NFT. Thereafter they inform apps such as Discord and Telegram whether a particular user should be kept inside the Discord/Telegram channel or not.

There are 2 solutions used to gate access to the Discord and Telegram communities, Swordy-bot and Collab.Land. Additionally, there are other solutions used for content gating, but we will cover them later as we primarily focused on researching a solution used to verify whether the user owns a specific NFT required to access Discord and Telegram community channels or not and thereafter test our hypothesis.

## Collab.Land

[Collab.Land](https://collab.land/) is a sovereign ruler and tool that is used by almost all Discord and Telegram Access communities.

The Collab.Land [documentation](https://collab-land.gitbook.io/collab-land/bots/discord) is scarce and it is focused on explaining how to connect their bot rather than explaining how it works. Also, we could not find any other useful information and as their solution was not open-sourced, we reached out directly to them looking for answers that will help us test our hypothesis.

Based on the answers we received, Collab.Land does store connections between users personal information and their wallet address.

However, before we could conclude that our hypothesis was correct, we had to research Swordy-bot.

## Swordy Bot

[Swordy-bot](https://swordybot.com/) is a Discord bot used to verify and grant access to a specific Discord channel (server) if a user has required token(s).

Compared to Collab.Land, Swordy-bot is built on top of decentralized Unlock Protocol. However, as well as Collab.Land it does store and keep a connection between user's personal information (Discord id) and wallet address in their centralized database.
We came to that conclusion (again) [based on the information](https://discord.com/channels/817286182890242059/817286182890242062/940232661773996043) provided by their team members. .

Another common thing with Collab.Land is that Sowrdy-bot is not open-sourced as well.

Worth mentioning is that, even though Collab.Land is sovereign ruler, Swordy-bot is used as a gate keeper by more than 100 Discord communities.

Finally, we could confirm that our presumption was correct based on the fact that both of these solutions do store and keep track of the user's wallet address and username centrally.

Thereafter we went a step further and analyzed other solutions used for content gating. All of them can be divided into 3 categories:

1.  Protocols
2.  Platforms
3.  Apps/Tools

Also each of them is either centralized or decentralized.

We have already covered Swordy-bot and Collab.land which are centralized tools.

## Unlock Protocol \[Decentralized Protocol\]

[Unlock Protocol](https://unlock-protocol.com/) is an open-source protocol, not a centralized platform, used to create an underlying infrastructure for token gating content (communities, application, websites pages, and sections, images, videos, etc.)

It enables:

-   user (admin) to deploy a set of smart contracts (on Mainnet, xDAI, Polygon, BSC, or Optimism) and define gating details (number of keys, key price and key duration).
-   regular users to purchase key (an NFT) and access content.

UP is the underlying layer that allows other tools to build on top of it and utilize its functionalities. Bellow are listed use cases enabled through community-developed integrations (apps and plugins) build on top of Unlock Protocol:

-   [Swordy-bot](https://docs.unlock-protocol.com/unlock/creators/plugins-and-integrations/discord) - gating Discord communities (servers and channels).  
-   [Discourse plugin](https://unlock.community/t/unlock-discourse-plugin/64) - gated content on Discourse.
-   [WP](https://docs.unlock-protocol.com/unlock/creators/plugins-and-integrations/wordpress-plugin) and [Webflow plugins](https://unlock-integration.webflow.io/) - gated website pages or section.
-   [Durap module](https://www.drupal.org/project/unlock) - gating content on Durap.
-   Slack plugin - gated Slack servers.
-   [Shopify app](https://github.com/pwagner/unlock-shopify-app) - allows merchants to offer special memberships to their customers.

Plugins and other integration tools are the ones that connect blockchain with specific apps (Discord, Slack, etc.). Hence, they are centralized solutions that monitor what's happening on a blockchain (whether the wallet address still holds an NFT) and inform apps about that. Something like reverse oracles.

All in all, Unlock Protocol is a customized set of smart contracts with the following functionalities:

-   Minting and sending NFTs (locks) to users.
-   Collecting and withdrawing crypto on behalf of admin.

Also, if needed, it can support more traditional (web2) authentication methods by storing private keys on behalf of a user. Also, UP support CC payments.

You are right if you think that all of the above may be done without UP. However, it is much easier and faster to implement all of these functionalities by using Unlock Protocol than developing all of the smart contracts and features from scratch.

## Whale room \[Centralized Platform\]

[Whale room](https://www.whaleroom.org/) is a centralized platform that enables users to create their chat rooms within the platform and gate them by setting up the access requirements (required tokens). Also, it supports token mining and distribution (to the community members).

Whale room is an alternative for using Discord (or Telegram) in combination with Collab.Land (or Swordy-bot) as it offers both, chat rooms (as Telegram and Discord) and token gating functionality (as Collab.Land and Swordy-bot).

## MintGate \[Centralized Tool & Platform\]

[MintGate](https://www.mintgate.io/) is a tool that allows users to hide content (URL) and present it only to the ones that possess specific NFT. Users can use MintGate to deploy new NFTs required to access content, but it also supports using other NFTs, minted in the other way.

In addition, MintGate recently created a centralized platform that offers the creation of your store and gating it with MintGate technology.

## Guild \[Centralized Platform\]

In combination with its Medusa bot, [Guild](https://guild.xyz/) gate the access to Discord private channels rather than the whole discord server. Compared to other solutions, it supports more complex requirements logic by combining the following requirement options: possession of an NFT, amount of an ERC20 token, and opportunity to whitelist wallet addresses.

Besides this feature and difference, it offers the same options as using some of the previously mentioned bots combined with Discord or Telegram (that you also need if you want to use Guild).

# Conclusion

After using available tools, going through their documentation, and discussing with their team members and community, we concluded that our presumptions are correct. There is a privacy concern as these tools are centralized solutions that store and keep the connection between users' identity (Discord/Telegram names) and their wallet addresses.

The challenge is constructing the middle layer that connects blockchain and apps (Discord and Telegram) and making it more decentralized and anonymous. Today, those solutions are centralized bots that keep an eye on what's happening on blockchain, whether wallet address (user) still holds an NFT, and inform apps about that. Something like "reverse oracles," which tell the off-chain world what is happening on-chain or a protocol with similar specification that results in yes or no answers if the token is still in possetion.

Finally, based on the research and insights we gathered, we can conclude that there is a space for technical improvement and reason to move to the next step. The next step requires working on the decentralized and open-source solution that utilizes the ZK tech and provides the same functionality as current solutions. It checks whether users hold an NFT and informs Disord or Telegram about it without storing and keeping the connection between users' identity (Discord/Telegram names) and their wallet addresses.

Precisely, solution has to:

-   Know whether the user possesses a specific NFT (contract address, ID, Blockchain, Token Standard) and inform the Discord server about that
-   Recognize when a user does not possess NFT anymore and inform the Discord server about that. Ensure that the user has access to discord channels as long as he/she keeps NFT. Once NFT is no longer in possession of the user, he/she losses access to Discord channels.
-   Be open-source

What solution must not do:

-   Keep track (connection) between user's wallet address and user (his discord/telegram username)
-   Allow more than one user to access Discord channels using the same NFT

# Appendices

# Bibliography

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-cowdreyAccessTokenNFTs2021" class="csl-entry">

Cowdrey, Ryan, 'Access Token NFTs How They Work and What The Future Holds', *NFT QT - QuHarrison's NFT Newsletter*, 2021 \<<https://www.nftqt.com/access-token-nfts-how-they-work-and-what-the-future-holds/>\> \[accessed 27 January 2022\]

</div>

</div>

[^1]: [Ryan Cowdrey, 'Access Token NFTs How They Work and What The Future Holds', *NFT QT - QuHarrison's NFT Newsletter*, 2021 \<<https://www.nftqt.com/access-token-nfts-how-they-work-and-what-the-future-holds/>\> \[accessed 27 January 2022\]](#ref-cowdreyAccessTokenNFTs2021).
