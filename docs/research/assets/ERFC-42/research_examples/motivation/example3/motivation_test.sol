// SPDX-License-Identifier: GNU Affero
pragma solidity >=0.4.25;

contract MotivationTest {
    function f(int256 a, int256 b, int256 c) public pure returns (int256) {
        int256 d = b + c;
        if (d < 1) {
            if (b < 3) {
                return 1;
            }
            if (a == 42) {
                assert(false);
                return 2;
            }
            return 3;
        } else {
            if (c < 42) {
                return 4;
            }
            return 5;
        }
    }
}