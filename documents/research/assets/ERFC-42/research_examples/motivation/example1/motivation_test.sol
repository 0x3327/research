// SPDX-License-Identifier: GNU Affero
pragma solidity >=0.4.25;

contract MotivationTest {
    bool private value_found;

    function f(uint256 a, uint256 b, uint256 c, uint256 d) public {
        require(a == 42);
        require(b == 129);
        require(c == d+333);
        value_found = true;
        assert(value_found == false);
    }
}