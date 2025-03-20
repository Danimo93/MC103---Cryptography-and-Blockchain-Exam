// scripts/deployAll.js
const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();
  console.log("Deploying with deployer:", await deployer.getAddress());

  // Deploy MyFirstToken with 3 args
  const MyFirstToken = await hre.ethers.getContractFactory("MyFirstToken");
  const firstToken = await MyFirstToken.deploy(
    1000000,         // initial supply
    2000000,         // max supply
    deployer.address // owner
  );
  await firstToken.waitForDeployment();
  const firstTokenAddress = await firstToken.getAddress();
  console.log("MyFirstToken deployed at:", firstTokenAddress);

  // Deploy MySecondToken with 3 args
  const MySecondToken = await hre.ethers.getContractFactory("MySecondToken");
  const secondToken = await MySecondToken.deploy(
    500000,
    1000000,
    deployer.address
  );
  await secondToken.waitForDeployment();
  const secondTokenAddress = await secondToken.getAddress();
  console.log("MySecondToken deployed at:", secondTokenAddress);

  // Deploy TokenExchange
  const ExchangeFactory = await hre.ethers.getContractFactory("TokenExchange");
  const ratio = hre.ethers.parseUnits("2", 18);
  const exchange = await ExchangeFactory.deploy(
    firstTokenAddress,
    secondTokenAddress,
    ratio,
    deployer.address
  );
  await exchange.waitForDeployment();
  const exchangeAddress = await exchange.getAddress();
  console.log("TokenExchange deployed at:", exchangeAddress);

  console.log("\nDeployment complete!\n");
  console.log(`MFT = ${firstTokenAddress}`);
  console.log(`MST = ${secondTokenAddress}`);
  console.log(`Exchange = ${exchangeAddress}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
