// SPDX-License-Identifier: GNU Affero
pragma solidity ^0.8.9;

contract AssertionFailure {
    uint256 private x;

    function f(uint256 _x) public {
        if(_x == 42) {
            assert(false);
        }
        x = _x;
    }
}