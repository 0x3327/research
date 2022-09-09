---
title: "[ERFC - 278] Meritocratic voting"
author: Milan Pavlovic
date: 7/25/2022
---



# Executive Summary

We considered a setting where a resource or rights are to be distributed among participants/members of a group. One possibility would be to allocate it equally (we can call this system democratic), another possibility would be to allocate it proportionally to relative efforts made, this system is known as meritocratic (based on credits earned).

We are mainly interested in the voting system (for example for DAOs), but believe that a similar system could be used in many other situations.

Prior to June, some of the existing solutions solves a good way process of weighted voting (MACI), and some (Colony) provide the solution for calculating reputation rating. Both have their missings - the role of coordinator in MACI, lack of ZK in Colony, for example. In the last weeks, Polygon came out with their PoligonID - web3 virtual identity which can store various data and uses ZK. It could be a great solution, after some testing and research, and one of its use cases could be Meritocratic voting. We could do deep dive into PolygonID and find others applications of it too, beside Meritocratic voting. It's very new solution and we could be one of first adopters.

# Introduction

We considered setting where a resource or rights are to be distributed among participants/members of group. One possibility would be to allocate it equally (we can call this system democratic), another possibility would be to allocate it proportionaly to relative efforts made, this system is known as meritocratic (based on credits earned).

We are mainly interested in voting system (for example for DAOs), but believe that similar system could be used in many other situations.

# Goals & Methodology

The steps of this research include:

-   Research use of blockchain as infrastructure for governance

-   Researching known practices, solutions, and implementations (eg. Aragon, Polkadot, Colony, MACI, PolygonID)

-   Research how ZK is used, where it is used, and how it could be used in systems which don't use it yet

-   Research the possibility of making dapp

# Results & Discussion

The first question that one meets is who would favor one and who another system. A meritocratic system would favor members that have high rating/a lot of contributions. While it is a good thing to encourage members to make contributions it can disincentivize members with modest contributions from participating. Also if an objectively-good proposal can be vetoed by some small portion of the community, say 1%, then it doesn't do well for the organization. If we are into realizing a project with a technical solution like a dapp, we should find the balance between these two extremes or include the option for user "how much meritocratic system" is wanted. Some further market research could be done in this direction.

The next phase of research shows that there are two groups of existing solutions that partly solves a problem at the root of this research. In one group there are solutions that solve problems of blockchain governance (such as Colony and other systems for the governance of DAOs). Another group is solutions for the voting system, most notable is MACI.

While MACI enables efficient weighted voting by using ZK proofs it has its drawbacks. Besides widely accepted missings such as having a coordinator, MACI does not have an efficiently updatable rating system. For example, if our Meritocratic system is to be used on some forum, the rating of a lot of members is changed daily. With MACI it is hard to register all that changes. If a rating of members in our Meritocratic system is rarely changed (for example we are using it for voting at universities where professors change their status/get a promotion every couple of years), MACI is a good existing solution - members pool does not change too fast and it can be efficiently updated. On the other side, MACI supports weighted voting (which because of ZK proofs is efficient) but relies that before voting we have the complete list of members (and their reputation). In short, MACI does not interfere a lot with members polls, it is mainly concerned with the process of voting alone.

Another group of existing solutions is solutions for the governance of blockchains, and DAOs, such as Colony. Colony supports a reputation system that is updateable and based on contributions but lacks ZK voting. They use simple commitments for voting, downsides are notable: after voting members must 'unlock' their vote; zk based voting system would be much better - more privacy, less cost. Also, even though Colony uses a reputation system, it does not do it on a blockchain (because of costs - the calculation is too large to be done on-chain due to technical and economic limitations
(i.e. the block gas limit and the cost of gas, respectively), this calculation can easily be performed
by a typical user's computer.) so they also assume the role of coordinator. Also, I could not find that they are proving proof of valid reputation calculation, which could be important to some clients.

For a question of calculating reputation there are some nice solutions from Colony which takes into consideration a couple of parameters such as type of contribution, the quantity of contribution, and also the time of inactivity - which brings negative reputation. Reputation rating can be measured with transferable or nontransferable tokens, depending on the use case.

Polkadot is a PoS, mostly-on-chain governed blockchain platform with a number interesting additions, they have for example an elected council and a technical council. Voters require at least 5 DOT to participate in governance and their voting power is based on stake. At a glance, the voters elect councillors, directly vote on referenda and submit proposals. The councilors then have the power to veto dangerous proposals, elect the technical committee, submit proposal of their own for approval by the voters and also control the treasury. The technical council can submit emergency referenda, that are implemented immediately if approved. Identity on Polkadot can be conected with various web2 platforms such as Twitter or Linkedin. They do not use ZK, so that could be tech improvement. For that improvement we could get inspiration from Polygons PolygonID, or simply focus our research on it.

In middle of this research, Polygon came out with blogs that announce their solution for problems of this kind. At it's core is their PolygonID - private identity on blockchain that uses power of ZK proofs. Namely, to someone prove their reputation, one can be in temptation to use it's wallet address. But it comes with cost, it risks revalving whole history, a lot of data from wallet, only because of voting. To address such concerns Polygon came with a new Web3 identity primitive - Polygon ID will serve that purpose, and Polygon DAO will be its testing ground. Polygon only announced this project, saying:

"Over the coming months, the Polygon ID ecosystem will grow to include a set of tools, platform services and examples for developers to learn, test and integrate with their apps or dApps leveraging Polygon ID's unique on-chain capabilities."

Weather we are about to make our demo app or try to improve/understand some of existing ( PolygonID stands out), paper \[2\] from litterature sugests immportant questions to think about, some of which are:
\* Tradeoffs between Privacy vs. Verifiability and Suffrage
\* Proofs of Personhood, Identity-based suffrage and tradeoffs with Privacy
\* Meritocratic suffrage and tradeoffs with privacy
\* ...

If we are about to make ZK solution for weighted voting, or reputation managment, good starting point is paper \[3\] of J. Groth in which there are numerous different votting system as well pseudo code and proofs of correctnes of main ZK attributes such as soundnes. For us, most interesting application would be 'Borda Vote'. In Borda voting, voters cast weighted votes. The worst candidate gets 1 vote, the second worst 2 votes, and so forth. A valid vote is therefore on the form $\prod_{i=1}^{L} \pi(i)M^{i-1}$ for some permutation $\pi$. In paper there is sugested protocool and correctnes argument for it.

# Conclusion

Need for Meritocratic voting system is most cercitnly large, question is how big is need for frequent and large updates in mebembers poll (mostly because of changing reputation rating). If that need is also large, then doing deeper technical research on this subject is jutified. Arguably, without effective governance processes, blockchain technology will fail to reach its full potential

Solution for our Meritocratic voting problem should be mix of the two - reputation mainteinnig system and voting system. For voting phase we could use MACI (or some variation) but we should design more cost-friendly system for mainteing reputation score/updating members list. If members trust coordinators for that part, than Colony solution works.
One upgrade would be to coordinator provide ZK proof for updating reputations of members - proof that state transition is OK. It is elegant solution because it can be done off blockchain an we can chalange coordinator. On the other side, it adds costs to coordinator. If organization does not want that cost it would use Colony.

Another route to go is to monitor closely on PolygonID, try to get some use-case examples, code, and documentation, and dig deeper into their solution. Based on MVP's good collaboration with Polygon, and the top-of-the-class reputation of Polygon's ZK teams, I believe that this is a good route to go. We could find others applications of it too, beside Meritocratic voting; and build dapps on-top-of their solution. It's very new solution and we could be one of first adopters.

# Appendices

# Bibliography

\[1\] Gradstein, M.; Voting on meritocracy. European Economic Review, 48(4), 797--803.; 2004

\[2\] SoK: Blockchain Governance; Aggelos Kiayias, Philip Lazos; 2022

\[3\] https://link.springer.com/chapter/10.1007/11496137_32

\[4\] https://colony.io/whitepaper.pdf

\[5\] https://github.com/privacy-scaling-explorations/maci

\[6\] https://blog.polygon.technology/state-of-governance-2-identity-reputation/

\[7\] https://blog.polygon.technology/polygon-id-x-polygon-dao-integration-launches-to-create-new-zk-based-governance-frameworks/
