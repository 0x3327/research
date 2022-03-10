//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;

import "./Greeter.sol";

contract GreeterTest is Greeter{

  function echidna_false() public view returns(bool){
        return (availableGreeting == false);
    } 
}
