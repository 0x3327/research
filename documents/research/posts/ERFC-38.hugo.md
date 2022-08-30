---
title: Building on Filecoin and Filecoin Proofs
author: Aleksandar Damjanovic
date: 2/25/2022 
---



## Executive Summary

When looking to build dApps that utilize decentralized storage Filecoin seems like the best option even with its flaws like : absent proof of deletion for the client, absent encryption, impossible modifying of the stored data and the durability problem of Filecoin's Proof of Replication. This research gives an overview of competitors in decentralized storage solution field with a focus on Filecoin protocol. It also shows how its competitor Storj differs from Filecoin and the current grant opportunities for potential building on it. Considering the results of the research Filecoin seems to be the best option considering the popularity and the size of its ecosystem. Currently there is no interest for building on and with Filecoin and this is a purely explorative work without experiments, in order to test the researcher's methodology and the approach to research. However, it proposes a question about a potential way of improving Filecoin, or creating both safer protocol for the user and cheaper for the storage miners.

## Goals & Methodology

The aim of this research is to explore Filecoin protocol and show its fallacies as much as writer is possible with a goal of inspiring building applications that utilize Filecoin, new protocols or improving Filecoin via building for it. The paper will compile the list of all fallacies and possibilities for improvement for Filecoin, opportunities for building on it, and the current state of decentralized storage market mainly comparing Storj and Filecoin.

## Introduction

Unlike a centralized server operated by a single company, decentralized storage systems consist of a peer-to-peer network of user-operators who hold a portion of the overall data. The platforms can store any data sent by the user, with some platforms more focusing on encryption. There is no official data disclosing the types of data stored.
This research will be covering contract-based persistence platforms with a focus on Filecoin.

Contract-based persistence means that data cannot be replicated by every node and stored forever, and instead must be upkept with contract agreements. These are agreements made with multiple nodes that have promised to hold a piece of data for a period of time. They must be refunded or renewed whenever they run out to keep the data persisted. Platforms with contract-based persistence currently present on the market are:

-   Filecoin

-   Skynet

-   Storj

-   0Chain

**Filecoin** is a peer-to-peer network that stores files with built in economic incentives to ensure files are stored reliably over time. Users pay to store their files on storage providers. Storage providers are computers responsible for storing files and proving they have stored the files correctly over time. Available storage and the price of it is not controlled by any company. Anyone who wants to store their files or get paid for storing other users files can join Filecoin is written in its documentation, but is that really the case? It will be further explored in later sections.
Filecoin's native currency is FIL. Storage providers earn units of FIL for storing user's data. Its blockchain records transactions along with proofs from storage providers that they are storing files correctly.

Currently Filecoin stores over **40.0453 PiB** of users data over **1,848,292** deals.[^1]

When users want to store their files on Filecoin they use terminal or different guis that have been built by developers to choose between cost, redundancy and speed and they select the storage provider whose storage offer is best suited for their needs. Applications that implement filecoin negotiate storage with storage providers. There is no need for different API for each provider.[^2]

"While interacting with IPFS does not require using Filecoin, all Filecoin nodes are IPFS nodes under the hood, and (with some manual configuration) can connect to and fetch IPLD-formatted data from other IPFS nodes using libp2p. However, Filecoin nodes don't join or participate in the public IPFS DHT. IPFS alone does not include a built-in mechanism to incentivize the storage of data for other people. This is the challenge Filecoin aims to solve. Filecoin is built on IPFS to create a distributed storage marketplace for long-term storage."[^3]

## Filecoin's Proof System

Filecoin uses Proof of Replication (PoRep) and Proof of Spacetime (poSt).

In a Proof of Replication, a storage miner proves that they are storing a physically unique copy, or replica, of the data. Proof of Replication happens just once, at the time the data is first stored by the miner. As the storage miner receives each piece of client data they place it into a sector, fundamental unit of storage in Filecoin. Sectors can contain pieces from multiple deals and clients. Steps in PoRep:
\### Proof of Replication
1. **Filling sectors and generating the Commd**

Once a sector is full a Commitment of Data (CommD) is created, representing the root node of all the piece CIDs contained in the sector.

2.  **Sealing sectors and producing the Commitment of Replication**

    Sector data is encoded through a sequence of graph and hashing processes to create a unique replica. The root hash of the merkle tree of the resulting replica is called CommRLast. CommRLast is then hashed together with the CommC(another merkle root output from PoRep). This generates the CommR (Commitment of Replication) which is then recorded on Filecoin's Blockchain. CommR, last is saved privately by the miner for future use in Proof of Spacetime but is not saved to the chain.

    Encoding process is slow and computationally heavy. **Filecoin doesn't provide encryption by default so users must encrypt data before adding it to the Filecoin network.** This is the first issue encountered with Filecoin : **Filecoin is optimized for public data and doesn't yet support access controls.**

    The CommR offers clients the proof that the miner is storing a physically unique copy of the client's data. If a client stores the same data with multiple storage miners, or makes multiple storage deals for the same data with the same miner, each deal will yield a different CommR. The sealing process also compresses the Proof of Replication using zk-SNARKs to keep the chain smaller so that it can be stored by all members of the Filecoin network for verification purposes.

    Unlike PoRep which is run once to prove that a miner stored a physically unique copy of the data at the time the sector was sealed. PoSt is run repeteadly to prove that the miners are continuing to dedicate storage space to that same data over time.[^4]
    \### Proof of Spacetime
    PoSt builds on several elements created during PoRep: the replica, the private CommRLast and public Commr.
    PoSt then selects some leaf nodes of the encoded replica and runs merkle inclusion proofs on them to prove that the miner has the specific bytes that indicate that he still holds the clients data. The miner then uses the privately stored CommRLast to prove that they know of a root for the replica which both agrees with the inclusion proofs and can be used to derive the CommR. As the final step PoSt compresses these proofs into a zk-Snark.

    If the miners fail the Proof of Spacetime at any point they will lose their staked collateral. Aside for this fine, there is no other incentive to keep the miners storing the data. That becomes a problem if client's storing private data or data of great significance.[^5]

## Results & Discussion

### Critique From the users perspective:

As of today the price of 1 Filecoin token (FIL) is \$22.05. **The users can store a gigabyte of data for as little as 0.0000006157315278020465 FIL (0.01% the cost of Amazon S3) which means the user can store 100GB of data for \$0.00135.**[^6] From the price perspective the upside of Filecoin is it's cheap storage but there are various downsides such as:

1.  Accesibility: if the user is not tech-savvy there is a big barrier to entry even with GUIs currently available. They are often not simple to install and it is hard to get them to work. Hovewer there are various Apps that make that somewhat easier like ChainSafe Files and Web3.Storage.When it comes to being a storage miner there minimal needs for hardware are:

-   8+ core CPU

-   128 GiB of RAM atleast

-   A strong GPU for SNARK computations

-   1TiB NVMe-based disk space for cache storage is recommended

    This data shows that there needs to be a significant investment on storage miners part which is nothing out of the ordinary but significantly reduces the accessibility to the average person, ofcourse assuming the person wants to be a storage miner.

2.  As the price of FIL tokens fluctuate the price of storage fluctuates as well. There is also a risk if any extra FIL is left in the customers wallet after the storage contract then token could potentially drop/rise in value, not to mention the fees of converting fiat into cryptocurrency.

3.  There is no built in encryption. Users need to encrypt their data on their own. Encryption/decryption of files cost compute resources (RAM, CPU), and therefore money. Most end users would prefer the implementation of this functionality to be handled, optionally, by the Filecoin web, cli or desktop client software they choose to make use of. This problem is seemingly taken care of with apps like ChainSafe Files.[^7]

    ChainSafe Files is an online platform to store, view, and share files. Its main focus is data privacy of the users and self-reliance. When it comes to self-reliance ChainSafe Files makes sure that the users can access the stored files even if the Files platform becomes unavailable. It also offers authentication flow using a decentralized login provider called tKey, by Torus. tKey is a private key generator that can link keys to social accounts among other functions. The Files' backend is built on top of ChainSafe Storage, and any file that is uploaded to Files is also pinned by a node on its infrastructure (each file has an CID) thus making the data retrieval possible even in the case of ChainSafe files app outage. In the case of retrieval users still have to decrypt the data, since all the data stored by ChainSafe Files is encrypted by default. 'ChainSafe Files - Decentralized Cloud Storage'[^8]

4.  If the storage provider doesn't respect his end of the deal he will be penalized and lose his staked FIL. Unless negotiating a great number of deals for the same data and storing a lot of copies in Filecoin, there is no guarantee that the data will be safely stored. These deals for the same data increase the cost of the service if the user wants to have somewhat durable data. Filecoin tries to mittigate this by having storage miners put 100+ FIL in collateral which also lowers the accessibility to the average person to become a storage miner. Currently most of the storage miners are located in China.

5.  Filecoin storage is cold storage. There is no way to modify data. If the user needs to change data , new data must be written.[^9]

6.  If the user issues a deletion command there is no guarantee that the client performs the operation. There is no way yet to Construct a formal Proof of Deletion.

### The issue with Replication and Filecoin

When decentralized storage network is utilized any storage node could go offline thus the stored data would be at risk of getting lost. To achieve a somewhat reliable storage many decentralized providers use replication, which means the only way to keep the users data reliably besides penalizing storage miners is to store multiple copies of it. Replication is not good for the network expansion factor. If Filecoin wants more durability for its data it needs more copies. For every increase of durability (storing or repairing the data) another multiple of the data size in bandwith is needed. Eg. If the durability level requires a replication strategy that makes 10 copies of the data this yields and expansion factor of 1000%. This data needs to be stored on the network, using bandwith in the process. The more replication the bigger the bandwith usage. Hovewer, if the node goes offline , only one of the storage nodes is needed to bring a new replacement node in, which again means that the 100% of the replicated data must be transferred. Excessive expansion factors produce an inefficient allocation of resources.[^10]

Another issue with replication is churn (nodes joining and leaving the network). Quoting Patrick Gerbes and John Gleeson: "Using replication in a high-churn environment is not only impractical, but inevitably doomed to fail. Distributed storage systems have mechanisms to repair data by replacing the pieces that become unavailable due to node churn. However, in distributed cloud storage systems, file repair incurs a cost for the bandwidth utilized during the repair process. Regardless of whether file pieces are simply replicated, or whether erasure coding is used to recreate missing pieces, the file repair process requires pieces to be downloaded from available nodes and uploaded to other uncorrelated and available nodes."[^11]

Currently the circulating supply of FIL token is 162,302,978.00 FIL. The potential circulating FIL could reach 1.977 Billion tokens if the network hits a Yottabyte of storage capacity in under 20 years which is brave considering the current data stored in data centers today is less then a Zettabyte and a Yottabite is 1000 times larger. The 770 Million of which is for baseline minting.

330 million FIL tokens are released on a 6 year half-life based on time. A 6 year half-life means that 97% of these tokens will be released in aproximately 30 years. This amount is amount is minted to provide counter pressure to shocks.

Another 300 million FIL is held back in reserve to incentivize future types of mining. How they are released is up to the Filecoin community.[^12]

<img src="https://filecoin.io/vintage/images/blog/filecoin-circulating-supply-minting.png"  style="height: 250px; width:500px;"/>

*Figure 1: Maximum and Minimum Minting from Storage Mining.*

<img src="https://filecoin.io/vintage/images/blog/filecoin-circulating-supply-baseline.png"  style="height: 250px; width:500px;"/>

*Figure 2: Network Storage Baseline for Max Baseline Minting on Log Scale.*

As of today 29,180,207.338966275 FIL has been slashed.This means that if a network participant misbehaves, part of their FIL collateral or potential FIL rewards is confiscated and burned. FIL is also slashed for various other reasons.

Considering the token release we can expect total supply of FIL token to be almost doubled in the next five years. If we look the rate of slashing so far the dilluting process will exceed the tokens burned. This makes specullating Filecoin token price risky, both for the investors and users.[^13]

## Filecoin and Storj comparission

We will compare Filecoin and Storj by:
1. Consensus Algorithms

Filecoin's consesus mechanism has been covered in the paragraphs above.

Storj does not have its own chain: the platform is built on Ethereum(currently built on PoW). The reason they decided to build on the Ethereum network is because of simplicity of using it as a method exchange. From the start Storj was never intented to be a true decentralized storage network.

2.  Block time

    Filecoin's block time is thirty seconds on average.

    Storj is the only "decentralized storage" solution to not employ their own chain. Storj decided to use the Ethereum network due to the easy deployment of a coin on it. Because of this decision, the block time is twelve seconds and needs to deal with the consequences of sharing blockchain with other projects.

3.  Enforcement of data retention

    Due to the PoSt mentioned in the paragraphs above the entire network is designed around data retention. In the case of miner failing to keep his promise , the only backup of the user's data was irreversibly lost since Filecoin doesn't use redundancy which is also mentioned in the paragraphs above.

    In Storj the actual enforcement of data isn't clearly documented.
    Each Satellite (the interface between the storage operators and the clients) does the enforcement of data retention all on their own. Each Satellite has its own subset of storage nodes that it knows have a good reputation and it trusts, it uses these hosts to upload data to. Then it, at regular intervals, checks random data segments with "Berlekamp-Welch" error correction to make sure that the data is still there. If they fail to prove they store the data the reputation of that host is changed and data migrates to a new host. There is no chain-level enforcement for data retention.

4.  Content distribution

    In Filecoin data has to be sealed to be counted as a provable storage to the chain and because it is computation heavy it isn't practical for the miners to serve data. 1 MiB file can take 5 to 10 minutes to unseal and 32 GiB file takes 3 hours on minimum hardware requirements mentioned above. To battle this Filecoin introduced a method to store cached and unsealed versions of data while storing the same data as sealed in order to provide proofs. This leads to the issue of miner storing the double amount of data while also posing the problem that unless the data is frequently accessed the miners will not store it because it isn't profitable for them. That makes creating Google drive equivalent on Filecoin not practical because the data is not frequent enough to makes sense to cache while also being low latency (because of slow sealing and unsealing).

    In Storj's case data is being accessible only through the S3 gateway of centralized data data Satellites. Users can transform any data to public data and can send anyone a link to that data.

5.  Sector size

    Sector size is the minimum amount of data that can be sent to host and paid for.
    Filecoin has a fixed 32 GiB sector size. For each 256b stored 2b are proofs. Which means 1% of storage paid for is for proof. Also everything sent must be in a .car file which can be computationally heavy on the client-side.

    In Storj's case the sector size is not really clear. Current object fee is \$0.0000022 per file stored. Which means that if there is a large amount of small files stored that would bring extra costs to the user.

6.  Decentralization

    Because of the Filecoin's Hardware requirements for hosts that means not everyone can run a storage node. On the other networks basically anyone can run a storage node( most minimal requirements are 2 cores 8GB of RAM and some storage) but in Filecoin only people with sufficient funds for initial investments can run hosts which reduces the spread of the network. Which makes us question the actuall decentralization of the network.

    Storj isn't decentralized. The blockchain nature of the Storj coin is only designed for for efficient transacting not decentralized enforcement of data retention which means that Storj is actually a distributed storage provider but not fully decentralized.[^14]

## Filecoin Grants

Filecoin offers various types of grants for building with Filecoin.

### Next Step Microgrants

Filecoin offers grants of 5000\$ in FIL to support taking the next step when the initial prototype is created. Their purpose is financing projects in the early stage. Acceptance criteria is simple. Projects must meet these criteria:
1. Applicant has already built something with Filecoin (or closely related technologies such as IPLD, libp2p, or frameworks or services such as NFT.storage, Textile Powergate, etc.), independently or as part of a course or hackathon.
2. Applicant must provide clear description of the Next Step after grant support
3. The project can be completed within 3 months.
4. Project must be open-sourced.
5. The applicant must complete weekly updates and a grant report upon conclusion.

Projects that qualify for Microgrants:
1. Projects that publish data or files to IPFS
2. Projects that don't use IPFS directly
3. Projects that save data or retrieve data from the Filecoin Network
4. Non-coding projects, videos, tutorials etc

These grants are offered on the quarterly basis.
\### Open Grants
Filecoin's focus areas currently are:
1. Core development - core protocol research, specification and implementation work
2. Application Development - applications that utilize Filecoin as a decentralized storage layer
3. Developer tools and libraries - tools and libraries for protocol developers and application developers
4. Integration and adoption - integration into existing app or projects with significant usage
5. Technical design - improvement proposals for the core storage protocol
6. Documentation
7. Community building
8. Metaverse - experiences, applications, communities, tooling, standards, infrastructure, et cetera[^15]
9. Research that explores Filecoin and decentralized storage[^16]

## Conclusion

When it comes to decentralized storage solutions Filecoin draws all the attention compared to its competitors like Storj and Sia. Storj solves Filecoin's replication problem, on the expense of decentralization but the internet search statistics still shows that Filecoin is the main contender in Decentralized storage.
<img src="https://i.imgur.com/Lr2LaBi.png"  style="height: 250px; width:500px;"/>

*Figure 3. Filecoin (blue) vs Storj (red) search interest in the past 12 months.*

Even with unclear tokenomics a nd problematic durability to the writer of this research, building with Filecoin seems like the best solution when building dApps that utilize decentralized storage because of its low cost and grant opportunities, even though storage miners are somewhat centralized. If there is a way to improve current storage miner's/clients experience on Filecoin both in cost and ease of use that would surely be a great grant opportunity. Also there could potentially be a way to draw them to a protocol that is a cheaper alternative. Ofcourse, these are all assumptions, since much of the data on these protocol is unclear and not available.

# Bibliography

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-ChainSafeFilesDecentralized" class="csl-entry">

'ChainSafe Files - Decentralized Cloud Storage' \<<https://files.chainsafe.io/>\> \[accessed 24 February 2022\]

</div>

<div id="ref-filecoinChainSafeFilesBuilding" class="csl-entry">

Filecoin, 'ChainSafe Files <span class="nocase">Building Privacy-preserving Cloud Storage</span>', *Filecoin* \<<https://filecoin.io/blog/posts/chainsafe-files-building-privacy-preserving-cloud-storage/>\> \[accessed 23 February 2022\]

</div>

<div id="ref-Filecoin" class="csl-entry">

'Filecoin', *CoinSupplyCap.com* \<<https://coinsupplycap.com/filecoin/>\> \[accessed 17 February 2022\]

</div>

<div id="ref-filecoinFilecoinPolygonStudios" class="csl-entry">

Filecoin, 'Filecoin and Polygon Studios Deepen Collaboration in NFTs, Games, and the Metaverse', *Filecoin* \<<https://filecoin.io/blog/posts/filecoin-and-polygon-studios-deepen-collaboration-in-nfts-games-and-the-metaverse/>\> \[accessed 17 February 2022\]

</div>

<div id="ref-FilecoinDocumentation" class="csl-entry">

'Filecoin Documentation' \<<https://docs.filecoin.io/>\> \[accessed 16 February 2022\]

</div>

<div id="ref-FilecoinFAQ" class="csl-entry">

'Filecoin FAQ' \<<https://docs.filecoin.io/about-filecoin/faq/>\> \[accessed 17 February 2022\]

</div>

<div id="ref-fischPoRepsProofsSpace2018" class="csl-entry">

Fisch, Ben, *PoReps: Proofs of Space on Useful Data*, 2018 \<<http://eprint.iacr.org/2018/678>\> \[accessed 10 February 2022\]

</div>

<div id="ref-fischProofsReplication" class="csl-entry">

Fisch, Ben, and Joseph Bonneau, 'Proofs of Replication', 25

</div>

<div id="ref-HttpsFileApp" class="csl-entry">

'<span class="nocase">https://file.app</span>' \<<https://file.app>\> \[accessed 17 February 2022\]

</div>

<div id="ref-IPFSFilecoin" class="csl-entry">

'IPFS and Filecoin' \<<https://docs.filecoin.io/about-filecoin/ipfs-and-filecoin/>\> \[accessed 16 February 2022\]

</div>

<div id="ref-labsFilecoinGrants" class="csl-entry">

Labs, Protocol, 'Filecoin Grants', *Filecoin* \<<https://grants.filecoin.io/>\> \[accessed 17 February 2022\]

</div>

<div id="ref-olioReplicationBadDecentralized2018" class="csl-entry">

Olio, JT, 'Replication Is Bad for Decentralized Storage, Part 1: Erasure Codes for Fun and Profit', 2018 \<<https://www.storj.io/blog/replication-is-bad-for-decentralized-storage-part-1-erasure-codes-for-fun-and-profit>\> \[accessed 10 February 2022\]

</div>

<div id="ref-projectUnderstandingFilecoinCirculating" class="csl-entry">

Project, Filecoin, 'Understanding Filecoin Circulating Supply', *Filecoin* \<<https://filecoin.io/blog/filecoin-circulating-supply/>\> \[accessed 16 February 2022\]

</div>

<div id="ref-StorageChainsCompared" class="csl-entry">

'Storage Chains Compared - Skynet Guide' \<<https://skynet.guide/tech/storage-chains-compared.html>\> \[accessed 24 February 2022\]

</div>

<div id="ref-WhyProofofReplication" class="csl-entry">

'Why (<span class="nocase">Proof-of-</span>) Replication Is Bad for Decentralized Storage, Part 2: Churn and Burn' \<<https://www.storj.io/blog/why-proof-of-replication-is-bad-for-decentralized-storage-part-2-churn-and-burn>\> \[accessed 16 February 2022\]

</div>

</div>

[^1]: ['<span class="nocase">https://file.app</span>' \<<https://file.app>\> \[accessed 17 February 2022\]](#ref-HttpsFileApp).

[^2]: ['Filecoin Documentation' \<<https://docs.filecoin.io/>\> \[accessed 16 February 2022\]](#ref-FilecoinDocumentation).

[^3]: ['IPFS and Filecoin' \<<https://docs.filecoin.io/about-filecoin/ipfs-and-filecoin/>\> \[accessed 16 February 2022\]](#ref-IPFSFilecoin).

[^4]: [Ben Fisch and Joseph Bonneau, 'Proofs of Replication', 25](#ref-fischProofsReplication).

[^5]: [Ben Fisch, *PoReps: Proofs of Space on Useful Data*, 2018 \<<http://eprint.iacr.org/2018/678>\> \[accessed 10 February 2022\]](#ref-fischPoRepsProofsSpace2018).

[^6]: ['Https'](#ref-HttpsFileApp).

[^7]: [Filecoin, 'ChainSafe Files <span class="nocase">Building Privacy-preserving Cloud Storage</span>', *Filecoin* \<<https://filecoin.io/blog/posts/chainsafe-files-building-privacy-preserving-cloud-storage/>\> \[accessed 23 February 2022\]](#ref-filecoinChainSafeFilesBuilding).

[^8]: [\<[Https://files.chainsafe.io/](https://files.chainsafe.io/)\> \[accessed 24 February 2022\]](#ref-ChainSafeFilesDecentralized).

[^9]: ['Filecoin FAQ' \<<https://docs.filecoin.io/about-filecoin/faq/>\> \[accessed 17 February 2022\]](#ref-FilecoinFAQ).

[^10]: [JT Olio, 'Replication Is Bad for Decentralized Storage, Part 1: Erasure Codes for Fun and Profit', 2018 \<<https://www.storj.io/blog/replication-is-bad-for-decentralized-storage-part-1-erasure-codes-for-fun-and-profit>\> \[accessed 10 February 2022\]](#ref-olioReplicationBadDecentralized2018).

[^11]: ['Why (<span class="nocase">Proof-of-</span>) Replication Is Bad for Decentralized Storage, Part 2: Churn and Burn' \<<https://www.storj.io/blog/why-proof-of-replication-is-bad-for-decentralized-storage-part-2-churn-and-burn>\> \[accessed 16 February 2022\]](#ref-WhyProofofReplication).

[^12]: [Filecoin Project, 'Understanding Filecoin Circulating Supply', *Filecoin* \<<https://filecoin.io/blog/filecoin-circulating-supply/>\> \[accessed 16 February 2022\]](#ref-projectUnderstandingFilecoinCirculating).

[^13]: ['Filecoin', *CoinSupplyCap.com* \<<https://coinsupplycap.com/filecoin/>\> \[accessed 17 February 2022\]](#ref-Filecoin).

[^14]: ['Storage Chains Compared - Skynet Guide' \<<https://skynet.guide/tech/storage-chains-compared.html>\> \[accessed 24 February 2022\]](#ref-StorageChainsCompared).

[^15]: [Filecoin, 'Filecoin and Polygon Studios Deepen Collaboration in NFTs, Games, and the Metaverse', *Filecoin* \<<https://filecoin.io/blog/posts/filecoin-and-polygon-studios-deepen-collaboration-in-nfts-games-and-the-metaverse/>\> \[accessed 17 February 2022\]](#ref-filecoinFilecoinPolygonStudios).

[^16]: [Protocol Labs, 'Filecoin Grants', *Filecoin* \<<https://grants.filecoin.io/>\> \[accessed 17 February 2022\]](#ref-labsFilecoinGrants).
