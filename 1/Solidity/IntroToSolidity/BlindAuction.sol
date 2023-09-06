//SPDX-License-Identifier:  UNLICENSED
pragma solidity ^0.8.4

contract SipleAucton{
    //Parameters of the auction
    address payable public beneficiary;
    
    //Current state of the Auction
    address public highestBidder;
    uint public highestBid;

    //Allowed withdrawals
    mapping(address => uint) pendingReturns;

    //Setting TRUE disallow any change. Default FALSE
    bool ended;

    //Event declaring changes on the Bid
    event  HighestBidIncreased( address Bidder, uint amount){
        
    }
}
