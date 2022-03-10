// SPDX-License-Identifier: GNU Affero
pragma solidity ^0.8.9;

contract Test {
  uint8 private value;

  function f(uint8 x) public {
    value += x;
  }  
}