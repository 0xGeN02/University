//SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

contract SimpleAuction {
    //Parameters
    address payable public beneficiary;
    uint public auctionEndTime;

    //Current State
    address public highestBidder;
    uint public highestBid;

    //Allowed withdrawals of previous bids
    mapping(address => uint) pendingReturns;

    //Set True disallows changes
    //Default as False
    bool ended;

    //Events that wil be emmited on changes
    event highestBidIncreased(address bidder, uint amount);
    event AuctionEnded(address winner, uint amount);

    //If auction ended
    error  AuctionAlreadyEnded();

    //If a bid has a higher amount
    error BidNotHighEnough(uint highestBid);

    //If auction not ended
    error AuctionNotYetEnded();

    //The function AuctionEnd() has already been called
    error AuctionEndAlreadyCalled();


    //Create an auction with a bidding time in seconds
    constructor(
        uint biddingTime,
        address payable beneficiaryAddress
        ){
            beneficiary = beneficiaryAddress;
            auctionEndTime = block.timestamp + biddingTime;
        }
    

}