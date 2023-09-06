import Web3 from 'web3';
const web3 = new Web3('http://localhost:5500'); // Replace 'http://localhost:8545' with the actual URL of your Ethereum node or the provider you want to connect to.


Coin.Sent().watch({}, '', function(error, result) {
    if (!error) {
        console.log("Coin transfer: " + result.args.amount + " coins were sent from " + result.args.from + " to " + result.args.to + ".");
        console.log("Balances now:\n" + "Sender: " + Coin.balances.call(result.args.from) + "\nReceiver: " + Coin.balances.call(result.args.to));
    }
});


//Here's an example of using Web3.js to retrieve the latest block number:
web3.eth.getBlockNumber()
.then((blockNumber) => {
  console.log('Latest block number:', blockNumber);
})
.catch((error) => {
  console.error('Error:', error);
});