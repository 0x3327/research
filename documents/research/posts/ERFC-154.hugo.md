---
title: Blacklisting Platform based on untransferable NFTs
author: Aleksandar Damjanovic
date: 3/31/2022
---



# Executive Summary

The main topic of this research is exploring the possibility and the need to create the "Authority" protocol that would handle blacklisting based on community voting and assessment. This protocol would mint the untransferable NFT to the blacklisted address. Creating this solutions (both the platform and the NFT) would not be challenging but the need for these solutions is questionable to the author. This paper explored the current blacklist cases and the possibility of creating the said NFTs. The Tether case is in the main focus since the solutions are similar and simple.
The main takeaway is that creating this solution is not necessary per se, but the issue is open for discussion.

# Introduction

When it comes to Web3, security breaches, hacks and malicious behaviour are a big issue. That is why some protocols resort to blacklisting the addressses they deem malicious. Blacklisting is essentially putting the addresses that have engaged in unethical or unacceptable activities on a list which in turn would limit their usage of said protocols.[^1]

Initial idea for this research is to explore the possibility of creating a platform that would blacklist addresses and send them an untransferable NFT. This platform would take it upon itself to take care of blacklisting for other protocols and users. The cases would be reported and voted on i.e Nexus Mutual model (for more info on their voting model check ERFC-91). When it comes to problems that this solution would solve the main problem is taking care of blacklisting for other protocols, this in turn makes our solution (even with voting) a point of centralization but more on that in later paragraphs.

# Goals & Methodology

The goal of this research is to explore how was blacklisting taken care of so far and to explore the possibility and need of creating a protocol that would do this with utilizing untransferable NFTs. Untransferable NFTs have been a topic of interest in the field for a while, otherwise there is no explicit point of including them except for "flagging" the addresses for the world to see.

This will be done by examining the source code of protocols that have done blacklisting in the past. After the examination we will draw some conclusions.

# Results & Discussion

## Blacklisting

As we pointed above we did a deep-dive into contracts that utilize blacklisting. In the beginning of the research we have searched for contracts that previously used blacklisting and we have come across the Tether case as it is the biggest one. There are various contracts that use the blacklist contracts but it is the exact same approach. When it comes to individual sites and addresses MetaMask already blocks sites that are known to steal funds.[^2]

Stablecoin issuer Tether froze the ethereum [address](https://etherscan.io/tx/0x60891b856cdae4fd0878d45d2768e640be2dc2a50876d20138797a09877a7cd6#eventlog) holding over \$715,000 worth of USDT. This address is the address of hackers who stole \$3 million on the Multichain bridge. This means that they cannot move the funds.

-   The question here is how did Tether manage to do that?

They managed that by importing the Blacklist contract in their main contract. We will try to explain the contract in the code-box comments below:

    contract BlackList is Ownable, BasicToken {

        // Getters to allow the same blacklist to be used also by other contracts.(including upgraded Tether) 
        function getBlackListStatus(address _maker) external constant returns (bool) {
            return isBlackListed[_maker];
        }

        // Returns the owner of the contract address.
        function getOwner() external constant returns (address) {
            return owner;
        }

        // Puts the blacklisted addresses in the mapping for checking and later use.
        mapping (address => bool) public isBlackListed;

        // Self explanatory, adds the address to the isBlacklisted mapping. Only owner of the contract can call the function
        function addBlackList (address _evilUser) public onlyOwner {
            isBlackListed[_evilUser] = true;
            AddedBlackList(_evilUser);
        }

        // Removes the address from the blacklist and "unfreezes the assets". Only owner of the contract can call the function.
        function removeBlackList (address _clearedUser) public onlyOwner {
            isBlackListed[_clearedUser] = false;
            RemovedBlackList(_clearedUser);
        }

        // Destroys the funds of the blacklisted address and reduces the total suply by the same amount. Only owner of the contract can call this function.
        function destroyBlackFunds (address _blackListedUser) public onlyOwner {
            require(isBlackListed[_blackListedUser]);
            uint dirtyFunds = balanceOf(_blackListedUser);
            balances[_blackListedUser] = 0;
            _totalSupply -= dirtyFunds;
            DestroyedBlackFunds(_blackListedUser, dirtyFunds);
        }
        // Simple events for transaction logs.
        event DestroyedBlackFunds(address _blackListedUser, uint _balance);

        event AddedBlackList(address _user);

        event RemovedBlackList(address _user);

    }

Then they simply put the require statement in all their main contract functions(except for the ones with the "Only Owner modifier") for example:

    // Require statement above makes sure the blacklisted address can't access the function.
    function transferFrom(address _from, address _to, uint _value) public whenNotPaused {
            require(!isBlackListed[_from]);
            if (deprecated) {
                return UpgradedStandardToken(upgradedAddress).transferFromByLegacy(msg.sender, _from, _to, _value);
            } else {
                return super.transferFrom(_from, _to, _value);
            }
        }

This approach to blacklisting gives the Tether the absolute control in what addresses it blacklists and for how long.

As we can see in the getBlacklistStatus the other contracts can use the same Blacklist to limit their usage as Tether thus leaning on their decision making.

In theory a blacklist protocol can be created where the voting what address to blacklist could be done by the community. The said addresses would be stored in the contract and those addresses could be whitelisted by voting again. Then, other contracts could lean on the "list" and block the addresses from using their functions. This would also make our solution the major point of centralization and considering how easy it is to set up blacklisting individually this proposes a question is the such solution needed?

Implementing a separate blacklist functions is not challenging and any contract can include them and have the complete control in what addresses it freezes and for how long.

## Untransferable NFTs

Untrasferable NFTs have been a topic of interest for a while in Web3 and there are various use cases that have been explored. Such as:

-   identity
-   badges
-   achievements, etc

Vitalik Buterin in his blog post showed his interest in "soulbound NFTs". If we want these NFTs to be truly soulbound (untrasferable) we would need to block transferability thus limiting them to only one address. When it comes to badges and achievements there are already POAPs. POAP has made the decision not to block transferability of POAPs themselves since the owners might want to change addresses and migrate assets for various reasons. There are various cases where they have been sold or even given out for free and after that sold for the highest bidder.[^3]

When it comes to creating a "soulbound NFT" we think that it is possible and that it can be done by modifying the transfer function from the ERC-721 standard.

The main issue here is utilizing them in the Blacklisting sense, the mint function from the ERC-721 interface can be included in the addBlacklist() function which would mint the said token to the said address. But so far we haven't come to the use-case except for "flagging" the addresses for the world to see, so it seems unnecessary at the moment.

# Conclusion

When exploring blacklisting we have come to conclusion that it is already implemented in some contracts and that creating a protocol that marks the "malicious" addresses is possible. The untransferable NFTs are possible to create also. The main question here is are those solutions needed? Creating a protocol that others can lean on can be useful but it would also be a major point of centralization and a lot of effort for a feature that simple. Not to mention including untransferable NFTs in the process which at this stage of the research seem unnecessary. What if the address is removed from the blacklist for various reasons does the NFT stay?

# Bibliography

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-Soulbound" class="csl-entry">

'Soulbound' \<<https://vitalik.ca/general/2022/01/26/soulbound.html>\> \[accessed 12 April 2022\]

</div>

<div id="ref-WhatBlacklist" class="csl-entry">

'What Is a Blacklist?', *Investopedia* \<<https://www.investopedia.com/terms/b/blacklist.asp>\> \[accessed 12 April 2022\]

</div>

</div>

[^1]: ['What Is a Blacklist?', *Investopedia* \<<https://www.investopedia.com/terms/b/blacklist.asp>\> \[accessed 12 April 2022\]](#ref-WhatBlacklist).

[^2]: [**metamaskmetamaskMetaMaskAutomaticallyBlocks2018?**](#ref-metamaskmetamaskMetaMaskAutomaticallyBlocks2018)

[^3]: ['Soulbound' \<<https://vitalik.ca/general/2022/01/26/soulbound.html>\> \[accessed 12 April 2022\]](#ref-Soulbound).
