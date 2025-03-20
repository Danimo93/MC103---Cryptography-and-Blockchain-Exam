# Bidirectional Token Exchange

This project consists of:
- **MyFirstToken** (MFT) and **MySecondToken** (MST) – both ERC20 tokens with capped supply and permit functionality.
- **TokenExchange** – a contract that allows swapping MFT ↔ MST at an owner-controlled ratio, plus deposit functions.



## Quick Start

1. **Install Dependencies**  

- npm install
 
- npx hardhat node
 
- Compile Contracts

- npx hardhat compile

This creates artifacts in artifacts/ and cache/.

4. Deploy Contracts

	- npx hardhat run scripts/deployAll.js --network sepolia
	- The script logs deployed addresses for MFT, MST, and TokenExchange.

5.	Update Front-End In front-end/app.js, set:

	- const EXCHANGE_ADDRESS = "0xYourExchangeAddress";
	- const TOKEN1_ADDRESS   = "0xYourMFTAddress";
	- const TOKEN2_ADDRESS   = "0xYourMSTAddress";

These should match the console output from the deployment script.

6.	Launch Front-End

	- cd front-end
	- npx http-server .
	- Open http://127.0.0.1:8080 in your browser.

7.	Import MFT and MST in MetaMask
	- Open MetaMask → “Import tokens.”
	- Paste each token address (MFT, MST) to see your balances.

Using the DApp

1.	Connect Wallet
	-	Click “Connect Wallet”. Approve in MetaMask.
	-	Ensure you are on Sepolia (or whichever network used for deployment).
2.	Approve a Token
	-	Under “Approve,” choose MFT or MST.
	-	Enter the amount you want the contract to spend (e.g., 100).
	-	Click “Approve.” Confirm in MetaMask.
3.	Deposit (Owner Only)
	-	If you want the exchange to hold tokens for swaps:
	-	Approve first, then under “Deposit,” set an amount for MFT or MST.
	-	Click “Deposit MFT” or “Deposit MST.” Confirm in MetaMask.
	-	This increases the “Exchange MFT” or “Exchange MST” balance in the UI.
4.	Swap
	-	Select MFT→MST or MST→MFT in the dropdown.
	-	Enter the token amount to swap (cannot exceed your approval & actual balance).
	-	Click “Swap.” Confirm in MetaMask.
	-	Your personal balance updates if the contract has enough tokens for payout.
5.	Update Ratio (Owner Only)
	-	Enter a scaled integer (e.g., 2000000000000000000 for 2.0).
	-	Click “Update.” Confirm in MetaMask.
	-	Future swaps use the new ratio.

Done!

You’ve successfully deployed tokens, set up an exchange, and tested approvals, deposits, and swaps.