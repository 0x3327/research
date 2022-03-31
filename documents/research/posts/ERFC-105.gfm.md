---
title: Transaction splitting
subtitle: ERFC - 105
author: Andrej Rakic
date: 3/8/2022  
---

# Executive Summary

Many companies sell goods with a business model based on donating some
percent of their profit to charity. The problem is that some of these
companies don’t transparently perform these donations. If, for example,
the handmade wristwatch company claims that it donates 90 percent of
earnings to the charity, the buyers can’t be sure whether they indeed
donated the funds to charity or just bought a very expensive product.
They can only believe the company itself. Blockchain technology
eliminates the need for trust.

# Introduction

This paper tends to explain and show how the need for trust can be
eliminated when it comes to donations and setting up business models in
general. Idea is to have a platform that will allow you to set up a use
case in which you want to allow users to buy a product from you where a
specific percentage of the purchase will go to a different wallet(s).

-   X% of purchase transparently goes to verified charity wallet
-   a split transaction between different co-creators or marketplace and
    author

We can develop a fully transparent set of smart contracts and protocols
on some general-purpose blockchain and introduce to sellers and
customers a brand new way for selling goods and doing business in
general.

Additionally, if there are too many different wallet recipients, the
splitting can be done through merkle tree claim model.

# Goals & Methodology

### Goals

-   How to make charity donations and spending transparent
-   Eliminate the need for trusting the brand, and provide customers a
    way to easily verify their spendings
-   Split input transaction to several different wallets by desired
    percentage

### Methodology

-   Write a set of smart contracts in Solidity for this purpose.
    -   Pros:
        -   Portable to any EVM general purpose blockchain
        -   Native support for cryptocurrencies
        -   Possibility for including ERC-20 tokens, as well
        -   Tooling (Hardhat, OpenZeppelin, etc.)
    -   Cons:
        -   Lack of native percentage operator in Solidity, one need to
            decide up to which decimal the result is reliable
        -   Transaction costs
-   Integrate it with [Bizzswap](https://www.npmjs.com/package/bizzswap)
    -   Pros:
        -   Out of the box solution for paying/swapping coins and tokens
    -   Cons:
        -   Third-party dependency
-   Testing
    -   Unit tests
    -   Integration tests
    -   End to end tests
    -   Static analasys
    -   Code coverage
    -   Gas usage
    -   Fuzz testing (optional)
    -   Formal verification (optional)
    -   Audit
    -   Deployment to testnet

The beauty of the end result is that anyone can port a frontend app to
this decentralized protocol and incorporate it in their business models,
already existing platforms, etc.

# Results & Discussion

Transaction can be split among several parties in Solidity like this:

### Step 1)

Smart contract should have the ability to receive native coin or any
other token. There is a need for a `receive()` or `fallback()` function,
depends on the implementation of the smart contract.

`receive()` is called if `msg.data` is empty, otherwise `fallback()` is
called.

``` solidity
    /**
    Which function is called, fallback() or receive()?

           send Ether
               |
         msg.data is empty?
              / \
            yes  no
            /     \
receive() exists?  fallback()
         /   \
        yes   no
        /      \
    receive()   fallback()
    */

    // Function to receive Ether. msg.data must be empty
    receive() external payable {}

    // Fallback function is called when msg.data is not empty
    fallback() external payable {}
```

### Step 2)

Smart contract then needs to split the received amount among other
wallets by defined percentage. Sending funds is trivial and we won’t
focus on that. The most challenging part is proper ratio calculations in
a language with no native support for decimal arithmetics.

In Solidity, one must assume that all numbers have 18 decimal precision.
For example:

-   1 is 1000000000000000000,
-   0.5 is 500000000000000000, and
-   100 is 100000000000000000000

Since there are no native language support for percentage arithmetics in
Solidity, devs are using Basis Points as a unit of measurement equal to
1/100th of 1 percent. This metric is commonly used for loans and bonds
to signify percentage changes or yield spreads in financial instruments,
especially when the difference in material interest rates is less than
one percent.

-   0.01% = 1 BPS
-   0.05% = 5 BPS
-   0.1% = 10 BPS
-   0.5% = 50 BPS
-   1% = 100 BPS
-   10% = 1 000 BPS
-   100% = 10 000 BPS

Possible implementation:

``` solidity
    function calculateFee(uint256 _amount) public pure returns(uint256) {
        // for example 1.85% is fee

        return _amount * 185 / 10000;
    }
```

# Conclusion

There are no blockers for implementing this idea in Solidity. The
tooling is stable, the math is not complex and can be handled by the
language, and the blockchain technology itself is capable for storing
this type of applications.
