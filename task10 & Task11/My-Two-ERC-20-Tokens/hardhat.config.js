require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.20",
  networks: {
    sepolia: {
      url: "https://sepolia.infura.io/v3/25dc5a50c633456a81aa7fd821e06846",
      accounts: [
        "0x02b46f30c6d37e18fda44e69f72db585571c109a706a9a4becf2147cfa9e05f8"
      ],
    },
  },
  etherscan: {
    apiKey: {
      sepolia: "U3XVZU34XVDFJY9JAYMPS3B55ZCP4VP3AP"
    }
  }  
};
