// SPDX-License-Identifier: MIT

pragma solidity 0.8.7;

contract ExchangeOffice {
    address public owner;
    uint public exchangeRate;
    mapping (address => uint) public tokenBalances;

    event TokensSold(address indexed by, uint amount, uint withExchangeRate);
    event TokensIssued(address indexed to, uint amount, uint withExchangeRate);

    constructor() {
        owner = msg.sender;
        exchangeRate = 20000;
    }

    function changeExchangeRate(uint newRate) public {
        require(msg.sender == owner, "You are not permitted to change the rate.");
        exchangeRate = newRate;
    }

    function buy_tokens() public payable {
        require(msg.value > 0, "Amount should not be zero");
        uint tokensCount = msg.value * exchangeRate / 1000000000000000000;
        tokenBalances[msg.sender] += tokensCount;
        emit TokensIssued(msg.sender, tokensCount, exchangeRate);
    }

    function sell_tokens(uint amount) public {
        require(tokenBalances[msg.sender] >= amount, "You don't have this amount of tokens.");
        uint etherAmount = amount / exchangeRate;
        require(address(this).balance >= etherAmount, "Sorry. Not enough etherium right now.");
        (bool isSuccess, ) = msg.sender.call{value: etherAmount * 1 ether}("Tokens sold for ETH.");
        require(isSuccess, "Something went wrong while ETH");
        tokenBalances[msg.sender] -= amount;
        emit TokensSold(msg.sender, amount, exchangeRate);
    }
}
