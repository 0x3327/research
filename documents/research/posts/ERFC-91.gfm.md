---
title: Crypto Insurance - Current state, problems and possibilities of creating new products
subtitle: ERFC - 91
author: Aleksandar Damjanovic
date: 3/9/2022  
---

# Executive Summary

In this paper we covered 5 of the main players in DeFi insurance market
in order to determine the products offered, the problems with these
products, the way the claims are handled and the possibilty of creating
new insurance protocols. Initially we were not familiar with this field
and the effort needed for creating these products, so we conducted this
explorative research.

After the research we came to these conclusions:

1.  In creating these kind of products there needs to be significant
    effort both in developing and inital investment. Protocols covered
    utilize Advisory Boards of insurance experts in order to create
    their products.
2.  State regulation is a big factor in insurance in order to protect
    the policyholders from malicious insurance offerers. This can be a
    problem, depending on the states’ attitude towards cryptocurrency.
3.  Handling claims is often left to the community incentivizing just
    behavior by staking.
4.  Collecting adequate capital initially is also one of the major
    problems.
5.  Protocols with less staked pools have higher premiums in most cases
    which shows us that the risk assessment is usually hard to do with
    new protocols.
6.  There is a limited cover capacity.
7.  Usually there is no cross-chain coverage which limits the protection
    capability of DeFi protocols on other chains.
8.  Lack of protection diversity: most products offered are limited when
    compared to the broad coverage of risk types in the traditional
    insurance market.
9.  Insuring real world Events is almost non-existent. Etherisc offers 2
    products using Oracles but our assumption is that there is still no
    market need for this kind of products thus there is not much
    movement in this direction. However utilizing Oracles in traditional
    products is an interesting thing and we think should be looked more
    into.

However, if You would like to go deeper to understand how these
protocols work we recommend reading the entire paper.

# Introduction

In this paper we will be exploring the current state and problems of the
decentralized/crypto insurance field with an emphasis to exploring the
types of insurance offered, how are claims assessed, processed and
finally paid out to the insured in a decentralized way.

Before we go further in the paper we will be shortly covering some
insurance basics with a goal of reader’s better understanding of this
paper and insurance’s importance in Decentralized Finance (DeFi).
Considering Insurance is one of the oldest ways of dispersing risk over
many individual units there could be many potential use cases for using
this kind of mechanism in Web3, not just for the insurance of loss.
Alas, this paper will be covering the current state and problems of
Insurance and we will leave the potential cases for discussion.

**If you are already familiar with insurance terms you can continue to
the Goals & Methodology paragraph.**

## What is Insurance?

Insurance has a long history, there are claims that it was created
around 2000 BC in Babylon, merchant receiving a loan paid the lender
extra money in exchange for exemption of loan payment if the merchant’s
shipment were stolen. Hovewer, the importance of insurance field cannot
be presented without a mention of London’s Lloyd’s. In the 17th century,
a London coffeehouse was a meeting place for people seeking marine cargo
protection and people willing to take those risks in exchange for
premium. The coffeeshop now is the world famous Lloyds. A sheet of cargo
and ship information would be filled and the individuals who accepted
that risk would sign with their names under it’s description.[^1] That
brings us to a first term in insurance **underwriting**.

-   Underwriting is risk accessment process to determine whether to
    accept or reject the risk we will come into contact with this term a
    lot in the later paragraphs.

-   As we previously mentioned the point of insurance is to **transfer
    and share risks.**

-   The individuals or companies that would like to transfer risk to
    other parties by paying a certain fee (**premium**) are called
    **insured**. The reason why the insured avoid the risk is because
    the loss is too volatile to bear.

-   The party that accepts such risks and and associated fee
    (**premium**) is the **insurer**. Insurers are not averse to
    exposing themselves to the same risks as insured because of
    something called **pooling** and the law of **large numbers**. The
    essence of pooling risk is to **spread losses of the few over the
    entire group.** The law of large numbers states that **the greater
    the number of exposures the more closely will the actual results
    approach to the expected average value**

## Benefits of Insurance and the nature of Insurance

Insurance allows the insureds to “trade” the risk of loss for the
certainty of smaller payments. As a result this ensured the stable cash
flow since there are no extreme losses, and if they happen, they are
covered by the insurance. As a result of this “stability” provided by
insurance there is less need for governments assistance which saves
public resources.[^2]

| Application | Underwriting | Policy Issuance | Claim if a loss occurs |
|-------------|--------------|-----------------|------------------------|

*Figure 1: The process of issuing insurance*

-   The application for insurance often starts with quoting process
    where the amount to be paid in premiums are estimated according to
    the risk the client would like to manage. After the application the
    underwriting process occurs.
-   Underwriter evaluates the information of the application and then
    accepts and then “fine-tunes” the policy using the rating tables
    from the actuaries. Actuaries calculate premiums, in DeFi, this is
    done in a different way, more words on that in the later paragraphs.
-   After the underwriter accepts the application the policy is issued.
-   If a loss occures the claims department examines the claim and asks
    the insured for the proof of loss before they pay the insured
    amount. The payment depends on the amount of damage suffered and the
    decision of the claim department.

The big part of insurance also is its regulation. Insurance is one of
the most actively regulated fields, especially after the financial
crisis in 2008. The regulation aims to ensure solvency of the insurers.
One of the ways the state regulates Insurance companies is limiting
their investment tacticts and portfolio allocation , in other words they
don’t let them invest in risky assets which is de-facto the norm in
cryptocurrency investments. This is one of the first issues encountered
if we were to cooporate with existing insurance companies or create our
own protocol that is regulated.[^3]

# Goals & Methodology

The goal of this research is to explore:

1.  The current state of DeFi Insurance and Insurance with
    cryptocurrency.
2.  The process of applying, policy issuing and insurance claiming in a
    decentralized way of the main competitors in this market
3.  The problems present with this kind of products.
4.  Possibility of insuring material goods with cryptocurrency.

Approach to this research will primarily be reading the whitepapers of
covered protocols and documentation, discord discussions with staff and
reading the reports of other researchers we find online.

Answers to the questions above will give us an insight into this field
of DeFi and will provide us with better of understanding of insurance in
general for creating potential products if we decide to go into that
direction. Considering the effort needed to create this kind of products
this short explorative research is conducted.

Approach to this will be explorative one as previously mentioned. We
will start with presenting the main competitors in this field and we
will analyze their proccesses. Extra attention will be paid to the
biggest competitors. Afterwards the problems of these products with
cryptocurrency will be presented.

# Results & Discussion

## The current state of DeFi Insurance and Insurance with cryptocurrency and insurance processes

When it comes to crypto-insurance with traditional insurers the market
is non-existent, because of the regulation, lack of awareness and the
lack of crypto adoption among general public. That’s why we will be
covering DeFi insurance field.

DeFi Insurance refers to buying coverage against losses cause by events
in Decentralized Finance. With various hacks and exploits over the years
the need for insuring users from the results of these events emerged.
Contrary to the layman’s belief DeFi Insurance field is big and growing
with different protocols emerging in it. However only 2% of all DeFi
value is insured at the moment.[^4]

Main protections offered is capital protection against protocol
hack/exploit risk, smart contract failures or stablecoin crashes. The
premium user pays for a cover depends on the type of the cover,
insurance provider and the duration of the cover.

The Decentralized part in this type of Insurance is that anybody can act
as a coverage provider, which supports the initial writers assumption.
They become providers by locking up capital in a capital pool of the
insurance protocol thus providing needed liquidity. As coverage
providers they choose for which protocols or events they want to provide
coverage, for example: If they are certain that a protocol is safe from
exploits they will prefer providing liquidity to the pool that covers
that event.

Another big part of DeFi Insurance is verifying claims. This is often
done by the Insurance protocol’s community. Considering the nature of
insurance and pooling of risk and collecting coverage from providers
they are often assembled as DAOs (Decentralized Autonomous
Organizations). This means that governance token holders participate in
verifying claims. There are several ways of doing that and we will be
covering it in the next paragraph.

### Main players in this market

The 5 main competitors in DeFi insurance are:

1.  Nexus Mutual
2.  Bridge Mutual
3.  InsurAce
4.  Nsure
5.  Etherisc

*Note: There are more insurance protocols but in order to keep this
research a short overview we will showcase five*

We will be covering them in detail to explore how they work and the type
of products offered.

### Nexus mutual

Nexus mutual is an Ethereum-based platform that offers insurance
products led by community management and financials. Nexus mutual is set
up as a DAO. Nexus offers three kinds of products:

-   Protection against failures in any protocol used by users yield
    bearing token (Ethereum only)
-   Protection against failures in the individual protocol user has
    funds in, on any chain, but not in other protocols it uses.
-   Protection against hacks and halted withdrawals on exchanges or
    custodial wallets[^5]

Simply put, Nexus cover protects against loss of funds, not loss of
value, except in the Yield Token Cover. In the Yield Token Cover Nexus
*may* pay a claim if:

-   During the cover period the face value of the covered token and the
    market value of the covered token differ in price by more than 10%
    for a continuous period of four hours or more; and
-   The Covered Member contributes to the mutual, one unit of face value
    of the covered token in exchange for 0.90 units of cover amount they
    wish to claim; and
-   The Covered Member redeems their claim payment during the cover
    period or within 14 days of the cover period ending.

Nexus does not provide Cover where the covered tokens and the cover
amount are not denominated in the same refference currency. Nexus also
doesn’t provide cover for any material goods loss.

**Claim assessing process:**

-   All Covered members for a particular covered token will be assessed
    together for each claim event; and
-   The face value of the covered token immediately prior to the claim
    event shall be set as part of the claims assessment process; and
-   Following a successful claim vote all Covered Members will be able
    to contribute their covered tokens and redeem their claim payment on
    a proportional basis up to the cover amount.[^6]

We will not cover the other 2 products into great detail, as they are
pretty straight forward. More info on them can be found here:
https://nexusmutual.gitbook.io/docs/welcome/faq/cover-products

All protocols and custodial accounts can be covered by the platform
provided that **risk assesesors** staked enough value against them. Risk
Assessors (experienced auditors, capital providers) can stake value in
the form of NXM token, thereby vouching for the security of the
protocol/custodian and dropping the price of the cover. NXM can be
unstaked at any time subject to a 30-day withdrawal period. When cover
is subsequently sold on a protocol or custodian, Risk Assessors earn
proportional rewards in NXM equivalent to 50% of the cover premium. If a
claim is accepted and a payout occurs, Risk Assessors staked against the
protocol/custodian will have their staked NXM burnt on a proportional
basis to facilitate the payout of the cover amount. This may result in a
Risk Assessor having some or all of their NXM staked against the
protocol/custodian burnt to provide capital for the payout of the claim.

Cover becomes available through one of two ways:

1.  When Risk Assessors stake NXM against a protocol, custodian or cover
    product more cover is made available. The mutual places limits on
    the amount of cover to protect the mutual from being too exposed to
    any single risk. There are two limits a **Specific Risk Limit** and
    a **Global Capacity Limit**.

    1.  **Specific Risk limit** means capacity on any particular risk is
        limited by the amount of staking on that risk. If there is no
        staking the mutual cannot offer any cover. Specific Risk limit
        is equal to : **capacity factor x net_staked_NXM** .

    2.  **Global Capacity Limit** is based on the financial resources of
        the Mutual and is there to ensure the mutual is not overly
        exposed to any particular risk, regardless of how much is
        staked. **Global Capacity Limit = Minimum Capital Requirement In
        ETH (MCReth) x 20%**

2.  As cover policies expire cover becomes available. User can check
    Nexus Tracker for info on cover expiry.[^7]

**Membership issue regarding privacy**

Membership in Nexus requires a one-off membership fee of 0.0020 ETH
(\~\$5.50). However, to become a member users need to verify their
identity following their Know Your Customer process. They also cannot
accept members from 17 countries, Serbia included, thus limiting the
usage of the mutual.

**Transparency**

All deployed contracts of Nexus Mutual can be found here:
https://api.nexusmutual.io/version-data/

All info regarding cover, staking and claims approvals/denies can be
found here: https://nexustracker.io/

**How are Cover purchases taken care of by Nexus?**

Users specify which smart contract address they want cover for. They
specify the cover amount , currency (ETH or DAI) and Cover Period. Quote
will be generated and they need to make the transaction with Metamask.
Users can currently pay with ETH, DAI or NXM (nexus mutual tokens).
Cover Holders can submit a claim for material loss that occured within
the cover period. They can also submit a claim up to 35 days after
expiry. **A loss that ocurs after cover policy is ended won’t be
covered**

**How are claims taken care of?**

Claims are filed by submission. Members must provide cryptographic
evidence of the loss (proof of loss) and their claim is later assessed
by Claim Assessors by voting. Assessors are financially incentivised to
take a longer-term view as they are required to lockup a stake. This
stake is then burned if there is evidence of fradulent voting, which is
addressed by Advisory Board. Advisory board consists of five members of
founding team of the Nexus Mutual and insurance industry experts. They
are said to have :

-   Technical Expertise on Smart Contract Security and blockchain
-   Technical Expertise on Insurance and Mutuals
-   General Expertise

Advisory board is there to provide techniqual guidance to the members of
the mutual as well as to exercize the emergency functions if they are
required.

This proposes a question: How do they keep the Advisory Board “in check”
with Nexus’s decentralization principles?

Nexus does that by enabling members to kick-vote the Advisory Board
members that they think are working maliciously. Board member can be
replaced by another member if the membership base agrees. These
proposals cannot be interfered with by the existing Advisory Board.

### Bridge Mutual

Bridge Mutual has a similar business model as Nexus Mutual (DAO model).
They provide coverage for smart contracts, stablecoins and other
services. Bridge allows users to purchase coverage, provide coverage in
exchange for yield, vote on policy claims and their payouts. We will not
go into great detail as there are various similarities with Nexus Mutual
to avoid repeating ourselves.

**The main difference between Bridge and Nexus Mutual is that that
Bridge doesn’t check customer’s ID and is available for residents all
countries**

Any user on the platform can create any pool for any project as because
the system is permissionless by design.

-   Initial capital (USDT) must be put into the Project Coverage Pool by
    the user that is creating the pool.
-   That project can create incentives for coverage providers to provide
    coverage to their pool by depositing any number of Token into its
    designated Shield Mining pool which gets distributed to Coverage
    Providers alongside the typical yield.

Coverage Provider examines the risk of providing Coverage Capital to the
Project’s Coverage Pool. When they provide capital they are de-facto
telling users that they are sure in the security and stability of the
project. They recieve yield from the users purchasing policies and the
BMI(Bridge Mutual) token staking. When coverage providers supply capital
to the coverage pool they receive a token (bmi(project name)Cover)
representing their share in the capital within this capital pool.
Coverage providers can then stake those tokens in the bmiCover Staking
Contract pool to get additional BMI rewards. They also recieve a BMINFT
Bond that represent the amount of for example DAI staked in Cover
Staking Contract pool. These NFT Bonds are tradable on any NFT
marketplace. The purpose of these NFT bonds is to give the user a way
out of their position without removing DAI from the ecosystem. When the
Coverage Provider sells his NFT he also transfers the ownership of the
staked bmiDAIx.

Policy Holder pays a premium for Coverage to protect against the
Coverage Event that could affect the insured Project and cause them to
lose funds. The total cost of the Premium is split : 80% to coverage 20%
to the Reinsurance Pool. They can buy cover for minimum of 1 week and
maximum of 52 weeks. Three factors determine the price of cover
(premium):

1.  The utilization ratio of the pool (ratio between cover bought and
    cover provided, pools that have higher utilization ratio are riskier
    and more expensive)
2.  Duration of the cover
3.  Amount of cover which user wants to buy

The Reinsurance pool consists of protocol owned funds that are used to
provide liquidity to Coverage Pools. The reinsurance pool is funded
through 20% of all premiums paid as mentioned above.

The Capital Pool aggregates USDT from the Coverage Pools and provides
additional revenue to the protocol. Capital Pool sends USDT to yield
generating platforms they deem to have low risk. We coulnd’t find
exactly what those platforms are. This is a similarity with classic
insurance companies which are limited in what way they invest their
funds.

**Proving a loss**

Policy holders should submit any or all of the following:

1.  Transaction IDs proving that Policy Holder’s wallet deposited assets
    into the protocol and transaction IDs of the Coverable Event
2.  Posts from Protocol team, or an auditing team confirming that there
    was an exploit and providing additional information
3.  A description of the Coverable Event
4.  If the address affected was not the same address that purchased
    coverage, any evidence that proves the Policy Holder is the bonafide
    owner of the address that suffered a Permanent Loss.

They also need to deposit 1% of the claim’s value in BMI to prevent spam
claims. If the claim is valid, USDT is issued to the Claimant. If a
claim is denied they can try again by depositing 1% again.

A successful claim can only recieve up to the policy’s maximum coverable
amount. If the DAO determines that the loss suffered was less then the
maximum coverable amount, policy owners may recieve less funds. The DAO
is incentivized to pay the claimant the exact amount that was lost.

**Voting process**

Votes for claim approval are anonymous and any user holding vBMI can
vote. Voters can wote on multiple Claims before submitting them in a
batch send. This is done to save time and gas. Only users that vote in
the majority are rewarded with BMI for voting. Users that vote in the
minority can lose “reputation” which decreases voting power. If there is
a large diference in voting yes or no (80% to 20%) users that voted no
will lose a portion of their stake.

<img src="https://1853607048-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-McJ-rdy5DzkSkdXp6VM%2F-MdWXc4-iyw6LOwtZ90R%2F-MdWfiqPXhasXmnJESvb%2Fimage.png?alt=media&token=11a1af05-bbde-4941-be28-3274fac85146" style="height: 400px; width:600px;"/>

*Figure 2. High Level Overview of Bridge Mutual’s Mechanism*

### InsureAce.io

InsurAce.io is a multi-chain mutual insurance protocol created in April
2021. It offers products that cover 100+ protocols, 3 CEX and 1 IDO
platform. Currently they are depoloyed on Ethereum, Binance Smart Chain,
Polygon and Avalanche. InsurAce hasn’t yet adopted the DAO governance
mechanism, although they are working on it.

Current state of Insurace.io (Capital pool size, Active cover amount,
Capital Ratios etc ) can be found here:
https://app.insurace.io/Data/Insurance

This protocols has 4 unique selling propositions :

1.  “0” Premium - Which means that the premiums are lower for their
    products. Their team designed portfolio-centric products to embrace
    risk diversification, developed models to optimize the cover cost.
    They did so by using advisors that are experts in the Insurance
    domain.
2.  Enriched Product Line - InsurAce.io also offers products that covers
    non-Ethereum DeFi protocols.
    1.  Types of protocols and smart contract systems covered:
        1.  Lending Protocols
        2.  Decentralized Exchanges
        3.  Derivative (e.g. Synthetix, Nexus Mutual)
        4.  Asset (e.g. Badger, RenVM)
3.  SCR Mining - The participants earn \$INSUR tokens by staking into
    the mining pool. The mutual capitals injected through staking will
    be managed with rigorous risk control models to adjust the Solvency
    Capital Requirement (SCR) dynamically and use the secured free
    capital for investment to control the mining speed accordingly.
4.  InsurAce tries to combat the low investment returns. Nexus mutual
    offers capital return to their providers from the premiums paid by
    users which is low compared to the yield on Compound and Aave. This
    problem makes users prefer putting their funds elsewhere, instead of
    the Insurance Protocol. Insurace combats this with offering users:
    1.  Option to invest directly in the investment product depending on
        their risk aversion
    2.  Option to stake in the mutual pool and get the investment
        carries and \$INSUR tokens as rewards
    3.  Shares of the premium income

InsurAce is operates similarly like the traditional insurance company
using the insurance arm and the investment arm.

“The insurance arm maintains reserve pools which maintain the solvency
for claim coverage based on risk exposure. The investment arm maintains
investment pools that generate carry to subsidize claims and attracts
investors with risk appetite. The free capital in the insurance capital
pool can be placed into the investment pool to gain a higher yield,
while the insurance arm will protect the investment activities.
Meanwhile, the investment arm’s yield will complement the premium on the
insurance side and reduce the cover cost for customers.”[^8]

**Pricing model**

When it comes to before mentioned protocols they rely heavily on the
value staked on individual protocols: the higher value staked the lower
the premium will be priced. InsurAce tries to combat this with adopting
the new actuary-based pricing model to mitigate this in order to assess
the expected loss of insurance products fairly, reduce costs and enhance
capability.

“The model’s main inputs are the number/amount of claims and
number/amount of exposures in a given time period, which will be used
for selecting and training two separate models - the frequency model and
the severity model. Frequency modeling produces a model that calibrates
the probability of a given number of losses occurring during a specific
period, while severity modeling produces the distribution of loss
amounts and sets the level of deductible and limit of the coverage
amount.” These models are then combined to solve aggregate loss. After
that the decided aggregate loss is incorporated into the risk factors of
protocols and the premiums are then calculated. The model’s parameters
rely on historical data to devise and validate. They plan on taking this
further with new Machine Learning methodologies.

**Capital model**

InsurAce’s capital model refers to EIOPA’s Solvency II, this regime is
used for insurance and reinsurance in the European Union. It sets
requirements needed for insurance products in order to protect
policyholdes and beneficiaries.

“Solvency II is an economic risk-based approach that should assess
the”overall solvency” of insurance and reinsurance undertakings through
quantitative and qualitative measures. Under Solvency II, the
undertaking’s solvency requirements are determined based on their risk
profiles and how such risks are managed, providing the right incentives
for sound risk management practices and securing enhanced transparency.”

Solvency II has different tiers of which the SCR (Solvency Capital
Requirement) and MCR (Minimum Capital Requirement) are the two most
important ones.

“The SCR is the capital required to ensure that the insurance company
will be able to meet its obligations over the next 12 months with a
probability of at least 99.5%, while MCR represents the threshold to
correspond to an 85% probability of adequacy over 12 months and is bound
between 25% and 45% of the SCR. For supervisory purposes, the SCR and
MCR can be regarded as”soft” and “hard” floors.”

InsurAce uses SCR to calculate the minimum requirement funds set aside
to pay all the potential claims considering all quantifiable risks. SCR
is calculated with the following inputs:

1.  All the active covers
2.  All the outstanding claims
3.  The potential incurred but not reported claims
4.  The market currency shock risk
5.  The non-life premium & reserve, lapse and catastrophe risks
6.  The potential operational risk

`SCR% = Capital Pool Size / SCR`

A high ratio means the insurance company is financially strong with
sufficient available funds to cover potential claims and other risks so
the company is less likely to be insolvent . **The lowest acceptable
ratio is 100%.**

InsurAce also offers information of their Capital Efficiency ratio which
shows the company’s current success in deploying capital.

`CER% = Active Cover Amount / Capital Pool Size`

A high ratio means the insurance company is increasing the productivity
of its assets to generate income. Desired ratio is between 100% and
300%.

**Risk Assesment by InsurAce.io**

InsuraAce’s Advisory Board performs a preliminary risk assesment on the
new protocols at first. InsurAce will also work with auditing firms if
there is extra complexity or challenges. After that Advisory Board
provides a report and rates the protocol 1 to 5. After they rate it
protocol will go through the community risk assesment. Members who
participate in the assesment get INSUR tokens as incentive.

**Claims Assesment by InsurAce.io**

<img src="https://2557507273-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MOAoQ0O7ivP8Rd-tXSY-887967055%2Fuploads%2FLlbDnXivNTRl7Zwnlcxn%2Fclaim_assess_eng_v2.0%20(1).png?alt=media&token=c9eccb8d-1707-47b5-adc6-dc09f7fc439c" style="height: 700px; width:550px;"/>

*Figure 3: InsureAce’s Claim Assesment process*

This diagram shows us the whole system of claims Assesment in a clear
way. The main difference is the inclusion of the Advisory board members
which consists of various industry experts including the CTO of
InsurAce.

“\$INSUR token holders can stake the \$INSUR tokens to become the
community Claim Assessor. Claim Assessor will be entitled to the right
to vote in each claim assessment and earn \$INSUR tokens as reward if
their votes match with the voting result. During each voting session,
the more tokens the user stake, the more voting tickets they will get
(\* capped at 5% of the total votes), and the more rewards they will
receive.”

### Nsure

Nsure was targeted to be a platform for users to trade risks borrowing
the operation model of previously mentioned Lloyds London. With Nsure
information is transparent and users are allowed not only to be
outsorcing risk but also to become risk takers, capital providers,
governance actors and auditors of the system.

More data on Nsure performance can be found here:
https://app.nsure.network/#/cover/my

**Product**

Nsure offers Smart contract cover like previously mentioned protocols.
The coverage and exclusions are identical so we will not go into great
detail. More info can be found at:
https://docs.nsure.network/nsure-network/docs/nsure-smart-contract-protect-policy-wording

**Capital model**

Capital is sourced from capital mining, with return of Nsure tokens for
the miners to ensure a continuous capital support to the underwriting.
Minimum Capital Requirement (MCR) is calculated based on the volume of
each project and the correlation between them. A low MCR% below a
pre-determined threshold will result into a lock of assets in capital
pool, so as to protect the solvency the business.

**Pricing model**

Nsure uses a Dynamic Pricing Model to set the price. In this model
capital supply and demand from the entire platform determines the price
jointly similar to the pricing mechanism in the free market, by having
Nsure tokens backing the policies bought. The price is self-adjustable
to the movement of supply and demand, subject to the model, moderately
stabilising the price change.

**Rating System**

Nsure uses its N-SCOSS rating system to quantify the code security of
projects by assessing:

1.  History and Team
2.  Exposure
3.  Audit
4.  Code quality
5.  Developer community

**Claim process**

<img src="https://399601259-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fnsure-network%2F-MX6EZjd-IYguhPxsT3i%2F-MX6K9inCZbKlXukrmEm%2F0.png?generation=1617178176984217&alt=media" style="height: 500px; width:700px;"/>

*Figure 4: Nsure claim process*

For each policy sold there is one chance of claim filling for free. If
the first claim was rejected a claim assesment fee of 10% is requested
before new assesment.

Policy holder must provide evidence of loss on the designated project
within the insurance period. Proof of loss must include:

1.  Proof of ownership of affected account - After identifying his
    affected account, policyholder may prove his ownership over the
    account by signature or making a 0 amount payment to a specified
    address.
2.  Evidence of loss - Policy holder should provide:
    1.  the snapshot of the affected address’s balance at blocks before
        and after attack (to assist claim assessors quickly quantify the
        amount of lost
    2.  transaction of selling the damaged assets (loss is only
        recognised when it is realised)
    3.  description of the attack from project team or security
        specialist

**Claim assesment**

Nsure introduced a similar voting mechanism as previously mentioned
protocols. Its features are:

1.  To be registered as a claim assessor candidate, user must deposit a
    considerable amount of Nsure token. At launch, the deposit is set at
    () Nsure token.
2.  Claim assessors are randomly picked from registered candidate. For
    each claim, there will be 5 claim assessors.
3.  As claim assessors’ reward is proportion to premium, users tend to
    register for larger size policy. To get each policy equal and fair
    tender, users do not know the premium of the policy at registration.
4.  The token will be slashed if the claim assessor’s judgment is
    different from the majority.

After claims assessors make a decision, policyholder and other Nsure
token holders can challenge this decision. This will lead to a public
vote for the final conclusion on the issue.

### Etherisc

So far we have been covering only protocols that offer smart contracts
protection. Etherisc tries to include material goods into the story.
Etherisc is a protocol to collectively build insurance products. Common
infrastructure, product templates and insurance license-as-a-service
make a platform that allows anyone to create their own insurance
products. The first product Etherisc offered was FlightDelay Insurance.
Products currently licensed are: Crop Insurance and FlightDelay
Insurance. Products currently in design: Hurricane Protection, Crypto
Wallet Insurance, Collateral Protection for Crypto backed Loans, Social
Insurance (death, heavy illness). They are also open for product
requests. Users have the option to build their own insurance product,
but more information about the user needs to be provided.[^9]

They also launched a Joint Grant Program with Chainlink to accelerate
the adoption of data-driven decentralized insurance products, so we
think that special attention should be paid towards potential building
with Etherisc.[^10]

**Etherisc Token**

DIP Tokens act as the native internal currency that is inseparable from
the protocol and network of its users. DIP tokens are needed to earn
transaction fees (% of insurance premiums or fixed cost), incentivize
and reward platform users to bring risk to the network, build and
maintain risk transfer products. The total supply of Etherisc Tokens is
1 Billion.

DIP tokens give users access to the Decentralized Insurance Platform. By
staking DIP token, participants provide collateral (bond) to guarantee
future performance, availability, and service levels. Staking also
signals quality and reputation. As a result, participants can earn money
monetizing their skills, software (for example risk models or UI/UX),
risk capital, insurance licenses, claim processing, or regulatory
compliance/reporting services.

**FlightDelay Insurance example from the Whitepaper - Launched on
January 20 2022**

In their whitepaper’s FlightDelay Insurance product they use oraclize to
obtain data from their data provider. Oraclize charges Etherisc for
calling their contract. Etherisc incentivize Oraclize to provide their
service correctly by :

1.  In the buyers market (market with many oracles) - Demanding of
    Oraclize to put some tokens in a staking contract which will then
    returns tokens if they deliver in time and forward the tokens to
    Etherisc in case they miss their obligations.
2.  In the sellers market (market with only one or few oracles) -
    Oraclize will earn an additional profit, again by staking tokens in
    a “staking contract”, but with reversed roles: Etherisc will stake
    tokens, and Oraclize will earn these tokens if they deliver, and in
    case they don’t deliver, the tokens are returned to Etherisc.
3.  Both options can be combined with both parties staking tokens from
    historical flight delay

Their experience with the Flight Delay DApp confirmed that insurance
applications need plenty of capital to be able to scale. But that entry
barrier can be overcome with cryptographic tokens that enable highly
customized economics. Their goal is to allow the tokenization of risks
on the platform and to make them available on a global open-access
marketplace.

In this kind of insurance the probability is calculated from historical
flight data. They used flight delay initially as a POC because of low
premiums assosciated with them and under normal circumstances flight
dellays are well-aproximated by independent probability events. Etherisk
leverages ChainLink data.

On January 20th 2022 Etherisc launched FlightDelay on Gnosis Chain
Mainnet. It uses Chainlink Data Feeds to autonomously issue policies and
execute payouts for travelers who experience flight delays or
cancellations. The result of this is insurance policies that are quicker
to settle, cheaper to provision thanks to decreases in human and
technical overhead and more transparent given the blockchain backend.

FlightDelay is now available for passenger flights globally. The
insurance policies are purchasable with USDC using the Gnosis Chain on
Etherisc’s FlightDelay portal. More payment options are in the works.

**Participants in the Etherisc Protocol**

Participants in the protocol are:

1.  Customers - Customers can buy insurance using the token. For
    convenience, third parties can offer payment gateways and
    integrations which remove the necessity to own cryptocurrency from
    the end customer. Furthermore, participants can choose to offer
    insurance products in any native currency - be it a cryptocurrency,
    a token or a fiat currency. **Use of token: Universal currency to
    buy insurance products.**
2.  Risk model Providers and Actuaries - “Risk models are fundamental
    for any insurance product. The correctness of the model is
    precondition for the economic success of the product.Generally,
    because of the magnitude of value affected by errors and deviations
    in the model, a Risk Model Provider won’t take responsibility for
    the economic outcome of his model, but rather for his adherence to
    principles and established guidelines in his trade.” **Use of token:
    Staking/Reward for providing or updating risk models**
3.  Data providers and oracles - Currently, data is collected together
    with the application for an insurance, and the insurance company
    “owns” the data - even after the insurance contract is no longer
    valid. In a blockchain decentralized environment, the collection of
    data could be separated. Customers could get paid for voluntarily
    offering their data to a data pool, which in turn can sell this to
    interested parties, leaving the ownership of the data completely
    with the customer. This is an interesting take on handling events in
    the real world and the real world application of crypto insurance.
    **Use of token: Reward for giving data. Reward for giving access to
    data pools. Staking / Reward for providing reliable oracles.**
4.  Sales Agents - Sales agents are responsible for offering insurance
    products like in the traditional insurance. **Use of token: Reward
    for distribution of products.**
5.  Claim Agents - There are still many cases where automatic detection
    and processing the claims is not possible. Specialized and sometimes
    independent claims agents already exist that can be somewhat
    utilized e.g. in the area of car insurance, where they help insurers
    to process claims in shorter time. These claims agents can
    immediately use a decentralized platform, as soon as adequate
    products are available. **Use of token: Reward for the provided
    service.**
6.  License providers - Insurance in most countries depends on a proper
    license which can be difficult and costly to obtain. There is also a
    model where a license provider can act as an intermediary to
    regulators which is interesting if we are to build a new kind of
    insurance product. **Use of tokens: Staking tokens to provide
    capital for a license provider, paying fees for licenses.**
7.  Product managers - **Use of token: Reward for service.**

Etheriscs’ approach to crypto insurance is interesting but majority of
their products are still in the works.Their first product FlightDelay
Insurance was launched on January 10th 2022.[^11]

# Conclusion

Above we covered 5 of the main players of the DeFi insurance market in
order to determine the products offered,the way the claims are handled
and the possibility of creating new insurance protocols.

Quick recap:

|                 |          **Nexus Mutual**          |      **Bridge Mutual**       |            **InsurAce**             |           **Nsure**            |              **Etherisc**               |
|-----------------|:----------------------------------:|:----------------------------:|:-----------------------------------:|:------------------------------:|:---------------------------------------:|
| Mechanism       |               Mutual               |            Mutual            |               Mutual                |    Open insurance platform     |  Platform to build insurance products   |
| Insurance       |      Protocol failure, hacks       | Smart Contracts, Stablecoins |       Protocols, 3 CEX, 1 IDO       |        Smart Contracts         | Material Goods, Other real-world events |
| Governance      |                DAO                 |             DAO              | Working on DAO governance mechanism |              DAO               |         No data/working on DAO          |
| Identity Check  |                KYC                 |              NO              |                 NO                  |               NO               |                   No                    |
| Availability    |    17 Countries are prohibited     |            Anyone            |               Anyone                |             Anyone             |                 Anyone                  |
| Transparency    |         Fully Transparent          |      Fully Transparent       |          Fully Transparent          |       Fully Transparent        |            Fully Transparent            |
| Claim Assesment | Claim Assessors and Advisory Board |    Voting of vBMI holders    |          Community Voting           | Claim Assessors or Public vote |                 Oracles                 |

We went into detail on those protocols and have come to these
conclusions:

1.  In creating these kind of products there needs to be significant
    effort both in developing and inital investment. Protocols covered
    utilize Advisory Boards of insurance experts in order to create
    their products.
2.  State regulation is a big factor in insurance in order to protect
    the policyholders from malicious insurance offerers. This can be a
    problem, depending on the states’ attitude towards cryptocurrency.
3.  Handling claims is often left to the community incentivizing just
    behavior by staking.
4.  Collecting adequate capital initially is also one of the major
    problems.
5.  Protocols with less staked pools have higher premiums in most cases
    which shows us that the risk assessment is usually hard to do with
    new protocols.
6.  There is a limited cover capacity.
7.  Usually there is no cross-chain coverage which limits the protection
    capability of DeFi protocols on other chains.
8.  Lack of protection diversity: most products offered are limited when
    compared to the broad coverage of risk types in the traditional
    insurance market.
9.  Insuring real world Events is almost non-existent. Etherisc offers 2
    products using Oracles but our assumption is that there is still no
    market need for this kind of products thus there is not much
    movement in this direction. However utilizing Oracles in traditional
    products is an interesting thing and we think should be looked more
    into.

# Bibliography

<div id="refs">

</div>

[^1]: [**HistoryLloydFounding1928?**](#ref-HistoryLloydFounding1928)

[^2]: [**outrevilleInsuranceConcepts1998?**](#ref-outrevilleInsuranceConcepts1998)

[^3]: [**litanRegulatingInsuranceCrisis2009?**](#ref-litanRegulatingInsuranceCrisis2009)

[^4]: [**TopDecentralizedInsurance2021?**](#ref-TopDecentralizedInsurance2021)

[^5]: [**NexusMutualBuy?**](#ref-NexusMutualBuy)

[^6]: [**CoverProducts?**](#ref-CoverProducts)

[^7]: [**CapacityLimits?**](#ref-CapacityLimits)

[^8]: [**Whitepaper?**](#ref-Whitepaper)

[^9]: [**EtheriscDecentralizedInsurance?**](#ref-EtheriscDecentralizedInsurance)

[^10]: [**etheriscEtheriscChainlinkLaunch2022?**](#ref-etheriscEtheriscChainlinkLaunch2022)

[^11]: [**EtheriscLaunchesFlight?**](#ref-EtheriscLaunchesFlight)
