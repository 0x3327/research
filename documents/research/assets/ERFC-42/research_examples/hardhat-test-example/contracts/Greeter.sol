//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

contract Greeter is Ownable{
    bool public availableGreeting;

    function greet() public onlyOwner {
        availableGreeting = true;
    }
}
