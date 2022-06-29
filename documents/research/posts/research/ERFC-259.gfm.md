Approaches to Testing Of Smart Contracts
================
Milos Bojinovic
June 4, 2022

-   <a href="#executive-summary" id="toc-executive-summary">Executive
    Summary</a>
-   <a href="#introduction" id="toc-introduction">Introduction</a>
-   <a href="#goals-methodology" id="toc-goals-methodology">Goals &amp;
    Methodology</a>
-   <a href="#results-discussion" id="toc-results-discussion">Results &amp;
    Discussion</a>
    -   <a href="#contract-example" id="toc-contract-example">Contract
        example</a>
        -   <a href="#specification-of-the-transfer-function"
            id="toc-specification-of-the-transfer-function">Specification of the
            <code>transfer</code> function</a>
    -   <a href="#forms-of-testing" id="toc-forms-of-testing">Forms of
        testing</a>
        -   <a href="#unit-testing" id="toc-unit-testing">Unit Testing</a>
        -   <a href="#integration-testing" id="toc-integration-testing">Integration
            Testing</a>
        -   <a href="#static-code-analysis" id="toc-static-code-analysis">Static
            (code) analysis</a>
        -   <a href="#general-considerations"
            id="toc-general-considerations">General Considerations</a>
    -   <a href="#evaluation" id="toc-evaluation">Evaluation</a>
        -   <a href="#code-coverage" id="toc-code-coverage">Code Coverage</a>
        -   <a href="#mutation-testing-mutation-analysis"
            id="toc-mutation-testing-mutation-analysis">Mutation Testing (Mutation
            analysis)</a>
-   <a href="#conclusion" id="toc-conclusion">Conclusion</a>

# Executive Summary

**Smart Contracts** are applications built on blockchain that, once
deployed, cannot be altered or updated. With that in mind, their testing
is crucial, even more so than in traditional software development.

Several different techniques exist in the testing of Smart Contracts,
and it is up to the developers to choose when a technique should be used
with the goal of creating tests that will perform sufficient validation.
This is a non-standardized, individualistic approach as there is no
established methodology for doing this, and the developers’ skill plays
an essential part in it.

This research focuses on testing techniques that are most widely used
and showcases them in order to give a sense of what kind of testing is
possible and where it makes sense.

In testing, there is always the question of whether the collection of
tests (test suite) covers all of the cases - “Who will guard the guards
themselves?”\*.

To answer this question, to a certain degree, the paper elaborates on
evaluation tools that indicate whether or not more tests should be
written or if there’s a case that is overlooked.

As the techniques and tools mature and increase in complexity, we may
see the introduction of standardized methodologies that provide a
thinking framework on how code should be written and/or tested, as well
as a separation of roles between developers and testers.

\*Quis custodiet ipsos custodes? - a Latin phrase found in the work of
the Roman poet Juvenal (Satire VI, lines 347–348)

# Introduction

Testing involves thinking about how code sections should behave in the
wanted (ideal) case, but also what consequences might occur if some
unintended actions are performed by unaware or even malevolent actors.

The logical question occurs of “what needs to get tested … and how ?”.
This is an extremely hard question, and the answer to it lies in the
considerations that the developers consciously/unconsciously make. It is
important that they keep up to date with the latest techniques, now more
than ever, as the past experiences of others can help in establishing
best practices and be used in solving similar or completely new
problems.

Sanity checks can be performed by using evaluation tools that help with
casting light on areas that were previously overlooked. Still, to add
another layer of confidence, a set of completely new, trusted eyes
should separately go through the code and try to find bugs and/or
exploits in it. This is referred to as a Smart Contract audit and is the
last step before the deployment to mainnet.

# Goals & Methodology

The focus of this research is on the testing and evaluation techniques
that are currently being used in the area of Smart Contract development
in the Ethereum Virtual Machine (EVM) ecosystem without going down the
rabbit hole of what the best practices are.

The methodology consists of describing a technique and then giving an
appropriate example that shows when it is adequate to use it. Frameworks
are purposefully not mentioned, as it is more important to first
understand the key concepts of what is being done rather than the unique
and specific details of how something is done.

# Results & Discussion

As to not give too abstract and vague descriptions, an example of a
smart contract is given on which the testing can be performed and
through which a better understanding can be created.

## Contract example

The example contract `DummyToken` can wrap/unwrap Ether through
`deposit` and `withdraw` functions and transfer the tokens between two
addresses using a function of the same name - `transfer`. During the
execution of those functions, a corresponding event is emitted.

The implementation details are purposefully hidden with the intention of
starting the thinking process of how those functions should behave both
when called in intended and non-intended ways.

``` solidity
/**
 * @dev Implementation of the Dummy Token.
 */
contract DummyToken {

    /**
     * @dev Emitted when tokens are moved from one account (`from`) to
     * another (`to`) of the `value` amount.
     */
    event Transfer(address indexed from, address indexed to, uint value);

    /**
     * @dev Emitted when a new Deposit is made
     */
    event Deposit(address indexed to, uint value);

    /**
     * @dev Emitted when new Withdrawal is made
     */
    event Withdrawal(address indexed to, uint value);

    ...

    /**
     * @dev Mints `value` tokens to `msg.sender` that corresponds to `msg.value` .
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * Emits a {Deposit} event.
     */
    function deposit () public payable returns (bool) {...}

    /**
     * @dev Burns `value` tokens if the `msg.sender` balance can cover it.
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * Emits a {Withdraw} event.
     */
    function withdraw (uint value) public returns (bool) {...}

    /**
     * @dev Moves `value` tokens from the caller's account to `to`.
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * Emits a {Transfer} event.
     */
    function transfer (address to, uint value) public returns (bool) {...}

    /**
     * @dev Returns the number of tokens owned by `account`.
     */
    function balanceOf(address account) public view returns (uint) {...}

    /**
     * @dev Returns the total amount of tokens in existence.
     */
    function totalSupply() public view returns (uint) {...}

}
```

### Specification of the `transfer` function

To understand the forms of testing that can be performed, let us write a
specification on what one of the functions needs to accomplish, namely
the `transfer` function.

#### High level specification of the `transfer` function

This function transfers the amount of tokens (`value`) from the
`msg.sender`‘s balance to the `to` address’ balance.

#### Low level specification of the `transfer` function

-   After successful transfer, the balance of `to` address is
    incremented by the `value` amount and the `msg.sender`’s balance is
    decremented by it.
-   If the `msg.sender`’s balance is smaller than the `value`, the
    transaction should revert with the
    `"Transfer amount exceeds balance"` message.
-   If the transfer is successful, the function returns `true` -
    otherwise, it returns `false`
-   If the transfer is successful, the `Transfer` event should be
    emitted with the corresponding fields:
    -   `from` : `msg.sender`
    -   `to` : value of the `to` argument
    -   `value` : value of the `value` argument

## Forms of testing

### Unit Testing

Unit Testing relies on keeping the tests separate from each other and as
simple as possible, with each unit test being responsible for testing a
single module(“unit”).

These tests follow a common pattern referred to as
**Arrange-Act-Assert(AAA)**. First, the “arrangments” are made to put
the system in the desired state, then the “act” is performed (function
call most often) that leads the system to the next state, after which
that state is “asserted” for correctness.

In an individual unit test, most often, only one assertion is made,
which increases the number of tests. This, however, has the benefits of
having a clear indication of why a test has failed and increasing the
code readability.

When thinking about unit testing the `DummyToken` contract, we will take
only the `transfer` function as an example. Following is an incomplete
list of test scenarios for this functionality that should serve as a
starting point.

#### Test Scenarios:

To form a part of a test suite, let us divide the test scenarios into
two sections (**generalized** and **edge cases**) and write some
examples of tests for each of them.

-   **Generalized:**

    -   Valid\* Transfer `amount`\*\* of `DummyToken` from `address0` to
        `address1` where `address0` != `address1`
        -   Tests:
            -   `address0`’s balance is decremented by the `amount`
            -   `address1`’s balance is incremented by the `amount`
            -   balances of other adresses has not changed
            -   `Transfer` event was emitted with the corresponding
                fields
    -   Invalid\* Transfer `amount` of `DummyToken` from `address0` to
        `address1` where `address0` != `address1`
        -   Tests:
            -   transaction was reverted with the right message
                (“Transfer amount exceeds balance”)
    -   …

-   **Edge Cases:**

    -   Valid/Invalid Transfer `amount` of `DummyToken` from `address0`
        to `address1` where `address0` == `address1`
    -   Valid Transfer `0/1` of `DummyToken` from `address0` to
        `address1` where `address0` != `address1`
    -   Valid Transfer `0/1` of `DummyToken` from `address0` to
        `address1` where `address0` == `address1`
    -   …

\*Term “Valid/Invalid” refers to the fact of whether this transfer
should be possible (due to balance amounts).

\*\*`amount` can be any `uint` (including the value being greater than
the total supply)

We can notice that for the first scenario of the generalized section,
four tests need to be written, with each of them being a unit test that
checks a specific thing (i.e., the sender’s balance has been decremented
by the right amount).

It is important to note that a “Property-based Testing” technique was
used in the above list, which is a form of an automated process called
“fuzzing” that is used to find bugs by feeding randomized data into the
system. This technique focuses on the “properties” of the code that
should always hold. The tests are not concerned with the actual values
of `amount`, `address0`, and `address1`, which can be anything in the
allowed range of possibilities. Rather, they aim to say whether the
properties around the balances hold in the test scenario - i.e., if an
account transfers some tokens to another account, only those two
balances should be affected.

### Integration Testing

In the context of Smart Contract testing, integration tests validate
interactions between different components of a single contract or across
multiple different contracts and are more complex when compared to unit
tests.

One form of integration testing is **Stateful testing**, an advanced
method of property-based testing, where a single test is defined by:

-   an **initial state** that can, after deployment, be kept as it is or
    be created by some fixed sequence of **actions**
-   **actions** - transactions that lead to a transition of state
-   **invariants** which are properties that should always hold true

Starting from the **initial state**, a randomized sequence of
**actions** is carried out, where after each action, all of the
**invariants** are tested.

For example, when writing a “stateful” test for the `DummyToken`
contract :

-   **initial state** can be created such that each test account calls a
    `deposit` function with a random amount of Ether provided
-   **actions** can be kept basic (`deposit` , `transfer` and
    `withdraw`) or more complex (nested - i.e. one action can be
    \[`deposit`, `withdraw`, `withdraw`,…\])
-   one of the **invariants** can be that sum of account balances of the
    `DummyToken` must always be equal to the Ether amount that the
    contract holds

Besides being more complex, integration tests require more resources and
execution time.

### Static (code) analysis

Both of the above-mentioned forms of testing are considered a type of
“dynamic code analysis” that searches for bugs during the execution of
the program, and they are the main topic of this research.

It is worth mentioning its counterpart - **Static code analysis** or
just **Static analysis**, which is a debugging method that examines the
source code before a program is run. This is done by analyzing the code
against a set of detection rules that include: timestamp dependency,
integer underflow/overflow, re-entrancy issues, use of tx.origin instead
of msg.sender, … It remains up to the developer to implement or reject
the recommendations of these rules.

### General Considerations

Smart Contracts operate in an extremely hostile environment, and this
should always be taken into account. During development and testing, the
most valuable guiding principle is that everything that can go wrong
will eventually go wrong, especially if someone stands to benefit from
it.

A set of principles can be adopted to make the functionality of a
contract and its complexity more manageable as to reduce the probability
of bugs or exploits happening. Some of those include that:

-   code should be modularized and kept simple (KISS and DRY
    principles\*\*\* should be followed)
-   clarity should be preferred over performance (if possible)
-   latest versions of battle-tested tools and frameworks should be used
-   the blockchain characteristics should be considered
-   the latest security developments should always be incorporated
-   deployment and testing should be done on Testnet before moving to
    Mainnet

\*\*\* KISS (Keep It Simple, Stupid) and DRY (Don’t Repeat Yourself) are
software programming principles where KISS states that the most simple
solutions often work the best, while DRY follows the reasoning that
same/similar code sections should not be replicated across the code
base.

## Evaluation

The purpose of tests is to verify the correctness of the implementation,
which poses the question of whether or not the test suite is sufficient
for the implementation requirements. To address this and to have a
sanity check for a developer’s thought process, evaluation tools have
been created.

### Code Coverage

The term **code coverage** refers to the set of evaluation metrics that
are used to determine how much of the program has been tested by the
test suite - how many functions have been called, how many statements
have been executed, etc.

For example, in the code below, to reach a 100% coverage for the
function `fcn`, at least one of the tests would need to call with
parameters that pass all of the three `if` statements
(i.e. `fcn(32, 300, 500)`).

``` solidity
function fcn (uint a, uint b, uint c) {

    if(a < 100) {
        if(b > 200) {
            if(c > 300 && c < 600) {
                ...
            }
        }
    }
}
```

While a high coverage doesn’t generally equal good tests, low coverage
helps in identifying gaps in the test suite that can be filled by adding
new, carefully designed tests.

#### Coverage-guided Fuzzing

During testing, feeding purely randomized values is often wasteful and
time-consuming. In the example above, parameter `a` is of type `uint`,
which means it can hold any value in the range \[0, 2\*\*64-1\], but the
condition `a < 100` will hold true only for a small portion of time.

Coverage-guided Fuzzing takes into account code coverage information for
each random value it tries, and if that value executes a new code, it is
put in the set of promising values. For example, if `a = 32` has been
generated, fuzzer will keep note of it, as it opens the door to new
code - it can then keep `a` fixed and randomize parameters `b` and `c`,
thus reducing the search space.

### Mutation Testing (Mutation analysis)

Mutation testing is a technique used to evaluate the effectiveness of a
test suite by introducing minor modifications, called “mutations”, in
the code, thus producing “mutants”.

These modifications are performed using a fixed set of mutation
operators like operand replacement, expression modification, statement
modification, etc.

Listed below is an example of an **original** code as well as one
potential **mutant** that can be generated from it.

**Original Code**

``` solidity
function fcn (uint a, uint b) returns (bool) {

    if(a > b){

        return true;
    }

    return false;
}
```

**Mutant \#1** - produced by using an expression modification operator
(replaced `>` with `<`)

``` solidity
function fcn (uint a, uint b) returns (bool) {

    if(a < b){

        return true;
    }

    return false;
}
```

These mutants are then tested, and, ideally, all of them would need to
get caught (killed) by at least one of the tests. The percentage of
killed mutants is referred to as the **mutation score**.

These techniques can give insight into what are the tests missing and
where are the blind spots as well as what tests are rarely killing
mutants - both of which is valuable when improving the test suite.

If a mutant cannot be compiled (i.e., mutation produced a syntax error),
it is called **stillborn** and is not taken into consideration.
Sometimes, mutants can have the same behavior as the original code, in
which case, they are referred to as **equivalent mutants**. These
mutants will not get killed by the test suite and will lower the
mutation score. Detecting and taking them out of consideration is not an
easy task and is the biggest obstacle to the widespread application of
mutation testing.

# Conclusion

This research concludes that the space of testing techniques is vast and
evolving. As the complexity of challenges that the developers are faced
with is rapidly increasing, staying up to date is a task by itself.

With time, we will probably see more and more specialized roles and the
separation of responsibilities as it was done in traditional software.
For this to happen, some standards should be formed that would enable
effective communication between team members, namely clear requirement
specification documents.

While posing a risk of the field becoming too rigid, rather than each
individual/team having a different approach, we may also see the
evolution of techniques and frameworks leading up to complete
standardized methodologies.

Some possible roads for future research on this topic should include
tools that are used when creating a well-documented functional
specification for the project and digging deeper into the evaluation
methods, specifically mutation testing, which is an active area of
research.
