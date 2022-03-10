// SPDX-License-Identifier: GNU Affero
pragma solidity ^0.8.9;

import "./example1.sol";

contract Test is Example1 {
    uint MIN_BALANCE = 20;
    uint MAX_BALANCE = 60;
    event AssertionFailed(uint counter);

    function condition_always_false() public view returns(bool) {    
        assert (condition == false);
    }


    function condition_assert(uint256 value) public returns(uint256) {
        value = MIN_BALANCE + value % (MAX_BALANCE - MIN_BALANCE);
        assert (condition == false );
        return value;
    }

    function condition_emit_assert(uint256 value) public returns(uint256) {
        value = MIN_BALANCE + value % (MAX_BALANCE - MIN_BALANCE);
        if(condition){
            emit AssertionFailed(value);
        }
        return value;
    }
}
