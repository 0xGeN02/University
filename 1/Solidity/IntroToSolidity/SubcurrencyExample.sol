//SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

contract Coin{
    //The keyword "public" makes variables accessible to others
    address public minter;
    mapping (address => uint) public balances;

    //Events allow clients to react to specific contract changes you declare
    event Sent( address from, address to, uint amount);
    
    //Constructor code is only run when the contract is created
    constructor(){
        minter = msg.sender;
    }
    //Sends an amount of created tokens to an address
    //This is only called by the contract creator
    function Mint(address reciver, uint amount) public{
        require(msg.sender == minter);
        balances[reciver] += amount;
    }
    //Error allows you to provide info about why an operator failed. They are returned to the caller of the blockchain
    error InssufficientBalance(uint requested, uint avaliable);

    //Sends an amount of tokens from the sender to the receiver
    function Send(address receiver, uint amount) public{
        if (amount > balances[msg.sender])
            revert InssufficientBalance({
                requested: amount,
                avaliable: balances[msg.sender]
            });
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);
    }

    //Returns minter's address
    function getMinter () external view returns (address){
        return minter;
    }

    //Return balances
    function getBalances(address account) external view returns (uint){
        return balances[account]; 
    }

}

/*
address public minter: Esta variable pública almacena la dirección del creador del contrato, también conocido como "minter".

mapping (address => uint) public balances: Este es un mapa que asigna cada dirección a una cantidad de tokens.

event Sent( address from, address to, uint amount): Este evento se emite cada vez que se envían tokens de una dirección a otra.

constructor(): Este es el constructor del contrato que se ejecuta cuando se crea el contrato. En este caso, establece la dirección que crea el contrato como el "minter".

function mint(address reciver, uint amount) public: Esta función solo puede ser ejecutada por el "minter". Agrega una cantidad de tokens a la cuenta del destinatario especificado.

function send(address receiver, uint amount) public: Esta función permite al remitente enviar una cantidad de tokens a una dirección especificada. La función verifica si el remitente tiene suficientes tokens antes de realizar la transacción.

error InssufficientBalance(uint requested, uint avaliable): Este es un mensaje de error personalizado que se lanza el remitente no tiene suficientes tokens para realizar la transacción.

function getMinter () external view returns (address): Esta función devuelve la dirección del "minter".
*/