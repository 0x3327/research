---
title: Solidity++ (S++)
subtitle: ERFC - 57
author: Aleksandar Veljković
date: 2/24/2022
---

# Executive Summary

Writing efficient code in modern languages is mostly reflected in
writing efficient algorithms and business logic. Writing efficient code
in Solidity is mostly reflected in thinking as an assembler, moving
focus from logic implementation to memory optimisations and low level
hacks. Highly optimised code may become unreadable and unmaintainable
with possible bugs hidden between the lines of bit level operations. To
solve this problem, this project proposes multiple automatic
optimisation techniques that will be all summed up into a transpiler and
Solidity language extensions called Solidity++.

# Introduction

Javascript introduced classes in ES6 which are very useful construct for
writing clean and readable code. Browser, however, could not understand
ES6 code so the code needed to be transpiled into ES5. Programmers could
use classes to write logic and transpiler took care of transforming the
code into an optimised ES5. The same parallel could be made with
Solidity. Programmers should be focused on writing business logic in
Solidity-like S++ code and the code should be automatically transpiled
into efficient Solidity code. S++ should not drastically modify basic
Solidity syntax, but introduce new annotations and helper functions that
would enable efficient transpiling to pure Solidity code.

There are multiple ways to improve the smart contract code on bytecode
level. This project will focus on improvements on Solidity code level
but the end product - optimised Solidity code will be compiled into
bytecode and further optimisations on bytecode level can be performed.

Optimisations on code level include variable declaration ordering (state
variables, local variables and structs), which correlates with the order
of memory block stacking and directly influences the costs of storing
the data. Some variables might occupy more space than needed to store
values in ranges that require less bits than the closest Solidity data
type. The most extreme example is boolean data type which stores
true/false values, that could be stored in 1 bit of memory, but really
use an entire byte. Accessing storage structs requires more operations
than accessing a local variable, which becomes obvious problem when it
is done in loops. Any fixed sized data type, like, int64, bytes32 and so
on, are always cheaper than dynamic data types, such as string, and
those dynamic types should be replaced with fixed ones wherever is
possible (wherever the value range of the variable is known). Cost
reduction can even be achieved by deleting variables - freeing
blockchain space. Execution of a code that performs *delete* command on
some variable/mapping value/… rewards executor with a refund of up to
50% of transaction cost, depending on the amount of freed space. There
were some attempts to remove this feature
(https://eips.ethereum.org/EIPS/eip-3298) but so far it is still valid
and exploitable. Usage of lazy evaluation is, an in other languages,
preferred way of saving execution steps, which for Solidity directly
equals saved money.

### Existing solutions

There are optimisations on loop level \[1\] that do not include variable
level optimisations but recognise code patterns that are classified into
several categories that can be automatically optimised. Also, there are
papers \[2\] that uncover additional space for optimisation, such as
removing conditions that always equal the same value or values in the
loops that never change. There are also blog advices for writing
optimised smart contracts, such as \[3\], that can and will be
referenced when implementing automatisation methods.

# Goals & Methodology

So far, there is no tool or IDE that either automates these
optimisations or includes multiple improvements in one software. The
goal of this project is to evaluate feasibility of implementing such
tool and Solidity language extensions that could allow its easier
implementation. End PoC toll planned as a result of this project focuses
on space optimisation techniques and includes: \* Implementing parser
for Solidity language that enables language semantic and syntax analysis
\* Implementing optimisation methods: \* Variable declaration reordering
\* Struct values declaration reordering \* Defining data type extensions
for storing custom-sized data (i.e. integers with values between 20 and
40) and implementing language parser extensions \* Implementing
generator for optimised code

# Results & Discussion

Proto-parser for Solidity code, which includes basic PoC constructs was
implemented, as well as variable declaration reordering to enable more
efficient space usage; The plan is to extend the parser and to include
other optimisation techniques listed in the previous segment.

### Variable declaration reordering

Variable declaration reordering is a problem synonymous to binning
problem, where the goal is to pack objects of a certain size into bins
of fixed size *in any order* using the least number of bins. The problem
is a known optimisation problem which comes from NP
(non-deterministically polynomial) class and has no known efficient
solution. The approach for implementing variable declaration reordering
was using branch-and-bound algorithm which resulted in decent reordering
time of less than 10 seconds for up to 16 variables in one block. The
reordering was performed per block. The same algorithm will be performed
on structs.

### Data type extensions

To enable extensions of data types there are two steps: \* Defining
language extensions \* Map variables to bits of memory blocks and create
getters and setters

New data types will be mapped to memory blocks, variables of 256 bits,
on bit level using bit masks. Packing of those values will be optimised
using the previously defined variable stacking algorithm

Proposed language extension of integer data types consists of using the
existing base type (int, uint) followed by value range given in
brackets. Example custom type uint\<10, 1030\> represents unsigned
integer values between 12 and 98. The optimiser would determine the
closest known data type that covers the range (in this case uint16). The
real number of bits required to store value 1030 is 11 and the closest
data type is 16 bits long which means that 5 bits are redundant. First
level of optimisation may be using 11 bits mapped to a memory block of
256 bits and implementing getters and setters to interact with the
value, which is casted to uint16 when used. But there is another hidden
optimisation that can further improve space management. Notice that the
upper limit of the interval is indeed 1030 which required 11 bits to
store but the lower limit is 10 which means that total number of values
is 1030 - 10 = 1020 and that many values can be stored in 10 bits of
memory, so the optimisation will take into account the overall interval
range and generate getters / setters that will include offsets before
storing/loading values.

Boolean type optimisation will be straight forward and, while it will
keep the type name, it will be mapped to only one bit of memory.

String data types would be extended with indicator of the number of
characters as string\<10\> will represent fixed sized string that will
be mapped to bytes.

### Code generation

The parser generates three-like structure of the Solidity code. Every
statement or declaration is stored as an object with parameters related
to the nature of the statement/declaration. For example, declaration
uint256 private var1 is stored as VariableDeclaration object with
attributes type=uint256, modifier=private identifier=var1. Each object
contains information to reconstruct itself back to string from. This
type of organisation enables easy traversal through code, easy
recognition of higher-level constructs, such are infinite loops, and
easy reconstruction to Solidity code (in this case - optimised code).

# Conclusion

The feasibility of the proposed project is confirmed by implementing PoC
prototype, the optimisation evaluation on the existing smart contracts
is yet to come but even the simple reordering of variables that reduces
the number of used memory blocks clearly shows benefits of money savings
(saved memory) and time savings (eliminated thinking about such generic
problem that can and should be automatised). The borderline is - it
makes no harm to use it, it can only be an improvement.

The value of this project is assumed, but still has to be confirmed.
That is why the next step of this research should be further assessment
by target user group, which should include developers that are actively
using Solidity in their everyday work and domain experts. \# Appendices

# Bibliography

\[1\] B Mariano, Y. Chen, Y. Feng *Demystifying Loops in Smart
Contracts* https://fredfeng.github.io/papers/ase20-consul.pdf 

\[2\] T.Brandstaetter *Optimisation of Solidity Smart Contracts*
https://repositum.tuwien.at/bitstream/20.500.12708/1428/2/Brandstaetter%20Tamara%20-%202020%20-%20Optimization%20of%20solidity%20smart%20contracts.pdf

\[3\] https://mudit.blog/solidity-gas-optimization-tips/
