// SPDX-License-Identifier: GNU Affero
pragma solidity ^0.8.9;

contract IntegerBug {
    uint256 MAX_INT = 2**256 - 1;
    uint256 x;

    function f(uint256 _x) public {
        x = MAX_INT + _x;
    }
}