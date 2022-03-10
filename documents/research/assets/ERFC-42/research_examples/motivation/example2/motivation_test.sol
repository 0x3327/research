// SPDX-License-Identifier: GNU Affero
pragma solidity >=0.4.25;

contract MotivationTest {
    uint256 private stateA;
    uint256 private stateB;
    uint256 CONST = 32;

    function f(uint256 x) public {
      stateA = x;
    }

    function g(uint256 y) public{
      if (stateA % CONST == 1) {
        stateB = y - 10;
      }
    }

    function h() public view {
      if (stateB == 62) { 
        bug(); 
      }
    }

    function bug() private pure {
      assert(false);
    }
}