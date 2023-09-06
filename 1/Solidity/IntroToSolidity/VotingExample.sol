// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.8;

/// @title Voting with delegation 
contract Ballot{
    //This declares a complex type that will be used for variables later

    //It will represent a single voter
    struct Voter{
        uint weight; //weight is accumulated by delegation
        bool voted; // if true, person voted before
        address delegate; //person delegate to
        uint vote; //index of the voted proposal
    }

    //This is the type for a single proposal
    struct Proposal{
        bytes32 name; //name of the proposal in 32 bytes
        uint voteCount; //Number of acumulated votes
    }

    address public chairperson;

    //This delcares a variable that stores the struct Voter for each possible address
    mapping (address => Voter) public voters;                                                

    //Dinamiclly-sized array of 'Proposal' structs
    Proposal[] public proposals;

    //Create a new ballot to choose one of 'proposalNames' 
    constructor(bytes32[] memory proposalNames){
        chairperson = msg.sender;
        voters[chairperson].weight = 1;
    
        //For each proposalName will be created a new proposal object and will be added to the array
        for(uint i = 0; i < proposalNames.length; i++){
            //Creating a temporary Proposal object and it will append it to the array
            proposals.push(Proposal({
                name: proposalNames[i],
                voteCount: 0
            }));
        }
    }

    //Give voter the right to vote on this ballot
    function giveRightToVote(address voter) external{
        require(
            msg.sender == chairperson,
            "Only chairperson can give right to vote"
        );
        require(
            !voters[voter].voted,
            "The voter already voted."
        );
        require(voters[voter].weight == 0);
        voters[voter].weight = 1;
    }

    //Delegate voter's vote
    function delegate(address to) external{
        Voter storage sender = voters[msg.sender];
        require(sender.weight != 0, "You have no rights");
        require(!sender.voted, "You already voted.");
        require ( to != msg.sender, "Delegation is disallowed");

        while (voters[to].delegate != address(0)){
            to = voters[to].delegate;   
            require(to != msg.sender);
        }
        Voter storage delegate_ = voters[to];

        //voters cant delegate to ppl that cant vote
        require(delegate_.weight >= 1);
        sender.voted = true;
        sender.delegate = to;

        if (delegate_.voted){
            //If the delegate already voted add the number of votes
            proposals[delegate_.vote].voteCount += sender.weight;
        }
        else{
            delegate_.weight += sender.weight;
        }
    } 
    //Give your vote and delegated votes to proposal
    function vote(uint proposal) external{
        Voter storage sender = voters[msg.sender];
        require(sender.weight != 0, "You have no rights");
        require(!sender.voted, "You already voted.");
        sender.voted = true;
        sender.vote = proposal;

        //If proposal is out of array range, this will revert all changes
        proposals[proposal].voteCount += sender.weight;
    }

    // previous votes into account.
    function winningProposal() public view returns (uint winningProposal_) {
        uint winningVoteCount = 0;
        for (uint p = 0; p < proposals.length; p++) {
            if (proposals[p].voteCount > winningVoteCount) {
                winningVoteCount = proposals[p].voteCount;
                winningProposal_ = p;
            }
        }
    }
    
    // Calls winningProposal() function to get the index
    // of the winner contained in the proposals array and then
    // returns the name of the winner
    function winnerName() external view returns (bytes32 winnerName_) {
        winnerName_ = proposals[winningProposal()].name;
        }
    }
