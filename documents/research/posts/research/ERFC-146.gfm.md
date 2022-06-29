Data Analytics in Blockchain
================
Milos Bojinovic
May 7, 2022

-   <a href="#executive-summary" id="toc-executive-summary">Executive
    Summary</a>
-   <a href="#introduction" id="toc-introduction">Introduction</a>
-   <a href="#goals-methodology" id="toc-goals-methodology">Goals &amp;
    Methodology</a>
-   <a href="#results-discussion" id="toc-results-discussion">Results &amp;
    Discussion</a>
    -   <a href="#general-purpose" id="toc-general-purpose">General Purpose</a>
        -   <a href="#tools" id="toc-tools">Tools</a>
        -   <a href="#platforms" id="toc-platforms">Platforms</a>
    -   <a href="#nft-specific" id="toc-nft-specific">NFT specific</a>
        -   <a href="#tools-1" id="toc-tools-1">Tools</a>
        -   <a href="#platforms-1" id="toc-platforms-1">Platforms</a>
    -   <a href="#defi-specific" id="toc-defi-specific">DeFi specific</a>
        -   <a href="#tools-2" id="toc-tools-2">Tools</a>
        -   <a href="#platforms-2" id="toc-platforms-2">Platforms</a>
-   <a href="#conclusion" id="toc-conclusion">Conclusion</a>
-   <a href="#bibliography" id="toc-bibliography">Bibliography</a>

# Executive Summary

**Data Analytics** is the science of analyzing raw data related to a
specific problem and extracting all of the necessary information in
order to make conclusions about as well as derive approaches for solving
it.

In the context of **Blockchain**, Data Analytics revolves around the
process of collecting and parsing of raw transaction data thus
transforming it into usable and actionable data. Parsing of those
transactions requires knowledge about the chain specifics as well as
internal workings of Smart Contract that that are of interest which is
an extremely time consuming process - all of the data on the Blockchain,
while it may be public and unchangable, is unstructured.

Blockchain data, however, holds all of the chain’s history since its
inception, making it possible to see past interactions between addresses
and/or Smart Contracts. This data can then be segmented to include only
a wanted subset for which the analysis will be performed. With this
aggregated information it is then possible to gain insight in the past
trends for a set of Non-Fungible-Tokens(NFTs) and Decentralized
Finance(DeFi) related applications as well as general Crypto related
trends and potentially predict future ones.

Data Analytics platforms in the Blockchain space are gaining users as
the whole crypto ecosystem evolves and is becoming harder to navigate.
With substantial recent investments in this area,[^1][^2] it is clear
that the investors are showing interest in what these platforms can do
and the potential they have in shaping the future of Blockchain.

# Introduction

This research focuses on the type of information that can be extracted
from the blockchain, elaborates on where that information can be used
and signals the utility that lies in it - especially in the NFT and DeFi
related applications that dominate the crypto ecosystem.

Out of the scope of the research falls the
aquiring/storing/organizing/displaying of the raw data which are
extremely hard and complex processes that also open questions about the
decentralization of those processes and the integrity of the collected
data.

Instead, it casts a light on the current state of the Data Analytics /
Blockchain intersection, top platforms that operate in it and the tools
that they provide. These platforms/tools are then categorized based on
area where they are used and their use cases briefly explained.

# Goals & Methodology

Data Analytics platforms/tools enable users to make sense of this
rapidly changing space and so the importance of this explorative
research lies in the fact that they are relatively new with a huge
potential and as such must be investigated further.

**The goal** of this research is to:

-   explore, explain and categorise Data Analytics platforms and their
    tools

**The methodology** of the research includes:

-   taking into account only platforms that support Ethereum Virtual
    Machine (EVM) compatible chains

-   discussing where a platform/tool can be used

-   categorizing a platform/tool as one of the following:

    -   **General Purpose** - contains both of the other categories as
        well as some additional functionality
    -   **NFT specific** - focuses on providing information about a
        collection/NFT or the NFT market in general
    -   **DeFi specific** - focuses on the extracting metrics for
        specific DeFi projects and DeFi market in general

# Results & Discussion

With those three categories explained above, platforms can be
investigated and then grouped. Regarding the distribution of categories
that will be elaborated on it is evident that most platforms/tools are
not general purpose ones. They require a lot of time to develop and so
there is an emerging trend of developing specizalised ones that are
easier to develop and target a single niche.

In the following text categories are listed in order, with each category
being divided into “Tools” and “Platforms” sections. In the “Tools”
section, each entry describes a specific functionality and the
“Platforms” section focuses on illustrative platforms that have those
functionalities (among others) incorporated into them.

Platforms/tools from the same/different categories are not mutually
exclusive and can be combined.

## General Purpose

### Tools

Tools in this category query information about the complete transaction
activity of a specific address (both Externally-Owned-Accounts (EOA) and
Smart Contracts) and groups the extracted information into human
readable metrics.

#### Contract interactions

For any choosen contract it is possible to extract general information
about the:

-   transaction count
-   unique addresses
-   token inflow/outflow

for a specific timeframe. These values can then be organized and
monitored over a larger time periods to provide information about the
latest trends and changes in the number of users, who these users are,
etc.

They can also be used to detect contracts that were recently deployed
that are gaining popularity as to investigate the project with which
those contracts are associated with.

More valuable information would be tied to how the contract is being
used - what methods are being called, their sequence, etc. To extract
meaningfull data, as it was discussed above, there would need to exist a
parser with a specific domain knowledge.

#### Address Profiler

For any user address of interest, it is possible to extract the
information about the :

-   portfolio (all of the assets that the address holds)
-   estimated portfolio value (sum of values of NFT\* and ERC20
    holdings)
-   recent token trades (both ERC20 and NFTs)
-   addresses that the user has interacted with

All of these values can also be monitored since the beginning of the
chain’s history and addresses can be grouped together to provide some
form of live feed for those that are most interesting either to the user
or to the platform itself.

\*Estimated value of an NFT is platform specific (i.e. see[^3])

#### Alerts

Alerts are delivered to the user, via a communication channel of choice
(Telegram, Text Message, Discord, …), when a certain customly defined
condition is met - some address buys an NFT, collection’s floor price
has increased/decreased by some margin, …

### Platforms

Two of the top plaftforms in this category are
[Nansen](https://nansen.ai) and [Dune Analytics](dune.xyz) which can be
used to gather and analyze similar information but take two drastically
different approaches - user oriented and business oriented,
respectively.

#### Nansen.ai

This paid platform doesn’t require or demand from user to have technical
knowledge and it provides detailed non-customizable dashboards for
General purpose, NFT and DeFi specific tools. Almost all of the tools
(from the three categories) listed in this paper, in one form or
another, are supported by Nansen making it the most comprehensive and
beginner friendly platform.

An interesting additional feature that Nansen provides is labeling of
some addresses as being “Smart Money” (addresses that were early
adopters and/or have made smart decisions in the NFT and/or DeFi
space)\*. There exist specific dashboards/sections where it is shown
what the “Smart Money” is doing - what are they minting/buying/selling,
with whom they are interacting, etc. This information can be used by the
user to decide what they think is a good strategy for them when
investing and can be combined with custom alerts when a certain
condition is met.

\*See[^4] for more details on the labeling of these addresses.

#### DuneAnalytics.com

Dune Analytics translates raw on-chain transaction data into SQL
databases such that the information can be requested using SQL queries.
Custom vizualizations (charts, graphs, …) and dashboards can be created
from those queries which can then be embedded into other websites.

Additional benefit of the platform is that there exists an active
community of members who can create dashboards for which both the
visualizations and the SQL queries are publicly avaliable. This enables
them to build upon on another’s work, making a powerfull snowball
effect.

There exist, however, two drawbacks to the platform:

1.  only the platfrom itself can perfom the parsing of smart contracts
    (users can request a contract to be parsed)
2.  doesn’t provide an API (though paid users can export results as a
    CSV file)

## NFT specific

### Tools

#### Market Overview/Trends

Contains information about the whole NFT market and specific
marketplaces, such as:

-   number of distinct users (minters/buyers/sellers)
-   trading volume
-   average price of all NFTs sold
-   floor price (taking into account all NFTs listed)
-   trending collections

These values are then used to analyze the percentage share of a
marketplace compared to the whole market which is useful to determine
the top marketplaces and capture the moment when there is a drastic
shift in the leaderboard.

The tool also helps in discovering new trending NFT collections and on
which marketplace is the most of the trading activity for that
collection happening thus answering the question where to go to when
considering to invest in it.

#### Collection Breakdown

Contains information tied to a specific collection and involves:

-   basic information (number of distinct holders, average price,
    volume, price range, number of trades…)
-   balance changes (how many NFTs were bought/sold/minted by an
    address)
-   rarity stats - what traits are the rarest and thus more valuable
-   recent mints/trades
-   similar collections

This data can be used to determine whether the majority of NFTs from the
collection are held by few addresses which is a bad position for other
holders as those addresses can quickly unload the NFTs, selling them at
lower prices and so driving the floor price for the entire collection
down.

It can also be used to assess the confidence of NFT holders in the
collection by seeing if long term holders are suddenly started selling
or if the collection is gaining momentum (for example, a lot of trades
by different addresses in a short period of time).

All of this can be used by the users to develop unique NFT trading
strategies, making this tool extremely informative.

#### NFT Breakdown

This tool focuses on a specific NFT from a collection and displays

-   history of trades - changes in ownership and price
-   similar NFTs (based on traits)

One of the obvious use case is tracking the price movement of that NFT
but another one is tracking at the same time the price movement of
similar NFTs and buying those that seem undervalued (ofter reffered as
“sniping”).

### Platforms

All of the previously listed tools are supported by Nansen but there are
specialized alternatives that perform limited subset of those
functionalities in a same/slightly different way. Some of the popular
ones are [icy.tools](https://icy.tools), [moby.gg](https://moby.gg) and
[NFTNerds.ai](https://nftnerds.ai).

## DeFi specific

### Tools

#### Total Value Locked (TVL) Tracker

TVL s the overall value of crypto assets deposited in a specific DeFi
protocol – or in DeFi protocols generally. It is often analyzed to
determine the oportunities across chains and protocols. When analyzed
over longer periods of time it can help in discovering new project
trends.

#### Recent Activity Tracker

This tool gathers in real time the latest transactions that happened on
Decentralized Exchanges (DEXs), Lending/borrowing and Derivatives
platforms. Using it, it is possible to detect and take into account
large funds movement by an address that is of interest.

#### Staking/Lending/Liquidity Metrics

These metrics revolve around the number of lenders/borrowers/stakers of
a DeFi platform, their current and past balances (including
deposits/withdrawals/liquidations) as well as the distribution of token
holders.

### Platforms

Dune Analytics is very useful in this area as the most useful
information is DeFi platform specific and needs to be analyzed in a
different way. For general, comparable information there are [DeFi
Pulse](https://www.defipulse.com/) and [DeFi
Llama](https://defillama.com/).

# Conclusion

Using Data Analytics platforms, it is possible to track and analyze the
performance of a portfolio for any address and to learn from their past
experiences. They are also useful in determining the differences between
the most sucessfull and least successful addresses as well as what they
have in common. These groups of addresses can then be monitored for
future transactions and can alert an user when they happen. Users can
then assess the new information and act accordingly.

The bottleneck of this process lies in the human factor that does
information assessing manually and so a lot of time is spent on it.
Improvements can be made by automating the decision process that leads
to the action. Since it would be dealing with real funds, a machine
could suggest a potential sequence of actions and the user would still
need to aprove it by signing the corresponding transactions.

For example, in NFT trading, a bot could monitor all trades in realtime
and detect an increase/decrease in the popularity of a collection which
would signal it to buy/sell an NFT or a set of NFTs and suggest the
price of it - at what price to list an NFT or what offer to make.

This, and other use cases from specific niches would need to be studied
further, as part of a separate research. There exists a question on the
utility of those tools, however, their functionalities are in a large
measure dependant on the Data Analytics and so their whole processing
pipeline would need to be carefully designed.

# Bibliography

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-finsmesDuneAnalyticsRaises2022" class="csl-entry">

FinSMEs, ‘Dune Analytics Raises \$69.42M in Series B Funding’,
*FinSMEs*, 2022
\<<https://www.finsmes.com/2022/02/dune-analytics-raises-69-42m-in-series-b-funding.html>\>
\[accessed 8 May 2022\]

</div>

<div id="ref-NansenWalletLabels" class="csl-entry">

‘Nansen Wallet Labels & Emojis: What Do They Mean?’
\<<https://www.nansen.ai/guides/wallet-labels-emojis-what-do-they-mean>\>
\[accessed 9 May 2022\]

</div>

<div id="ref-UtilizingNansenInvesting" class="csl-entry">

‘Utilizing Nansen: Investing in NFTs’
\<<https://www.nansen.ai/research/utilizing-nansen-investing-in-nfts>\>
\[accessed 9 May 2022\]

</div>

</div>

[^1]: [**NansenRaises7?**](#ref-NansenRaises7)

[^2]: [FinSMEs, ‘Dune Analytics Raises \$69.42M in Series B Funding’,
    *FinSMEs*, 2022
    \<<https://www.finsmes.com/2022/02/dune-analytics-raises-69-42m-in-series-b-funding.html>\>
    \[accessed 8 May 2022\]](#ref-finsmesDuneAnalyticsRaises2022).

[^3]: [‘Utilizing Nansen: Investing in NFTs’
    \<<https://www.nansen.ai/research/utilizing-nansen-investing-in-nfts>\>
    \[accessed 9 May 2022\]](#ref-UtilizingNansenInvesting).

[^4]: [‘Nansen Wallet Labels & Emojis: What Do They Mean?’
    \<<https://www.nansen.ai/guides/wallet-labels-emojis-what-do-they-mean>\>
    \[accessed 9 May 2022\]](#ref-NansenWalletLabels).
