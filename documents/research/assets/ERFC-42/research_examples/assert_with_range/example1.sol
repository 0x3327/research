// SPDX-License-Identifier: GNU Affero
pragma solidity ^0.8.9;

contract Example1 {
    bool public condition;

    function f(uint8 value) public returns(bool){
        if(value == 50) {
            condition = true;
        }
        return condition;
    }
}
