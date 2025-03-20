// Replace with your addresses
const EXCHANGE_ADDRESS = "0x0bE849a1659557f2159E73DD5E3676feEc10D0E4";
const TOKEN1_ADDRESS   = "0x30dca17485247da9Feab63C5A535E574aaE5d3C6";
const TOKEN2_ADDRESS   = "0x756C60D3abD249B681E1CfEc36e89758e2d576cA";

const EXPLORER_BASE_URL = "https://sepolia.etherscan.io/tx/";

const exchangeAbi = [
  "function swapTokens(bool,uint256) external returns (uint256)",
  "function updateRatio(uint256) external",
  "function ratio() view returns (uint256)",
  "function token1() view returns (address)",
  "function token2() view returns (address)",
  "function depositToken1(uint256) external",
  "function depositToken2(uint256) external",
  "function owner() view returns (address)"
];

const erc20Abi = [
  "function approve(address,uint256) external returns (bool)",
  "function balanceOf(address) view returns (uint256)",
  "function transfer(address,uint256) external returns (bool)",
  "function transferFrom(address,address,uint256) external returns (bool)"
];

let provider, signer, exchangeContract, token1Contract, token2Contract;

document.getElementById("btnConnect").onclick = async () => {
  if (!window.ethereum) {
    alert("Metamask not found");
    return;
  }
  try {
    await window.ethereum.request({ method: "eth_requestAccounts" });
    provider = new ethers.providers.Web3Provider(window.ethereum);
    signer = provider.getSigner();
    exchangeContract = new ethers.Contract(EXCHANGE_ADDRESS, exchangeAbi, signer);
    token1Contract = new ethers.Contract(TOKEN1_ADDRESS, erc20Abi, signer);
    token2Contract = new ethers.Contract(TOKEN2_ADDRESS, erc20Abi, signer);

    alert("Wallet connected!");
    checkIfOwner();
    updateBalances();
    updateContractLiquidity();
  } catch (err) {
    alert("Connect failed: " + err.message);
  }
};

async function checkIfOwner() {
  try {
    const contractOwner = await exchangeContract.owner();
    const userAddr = await signer.getAddress();
    if (contractOwner.toLowerCase() !== userAddr.toLowerCase()) {
      document.getElementById("btnUpdateRatio").disabled = true;
      document.getElementById("btnDepositMFT").disabled = true;
      document.getElementById("btnDepositMST").disabled = true;
    }
  } catch {}
}

async function updateBalances() {
  try {
    const userAddr = await signer.getAddress();
    const balMFT = await token1Contract.balanceOf(userAddr);
    const balMST = await token2Contract.balanceOf(userAddr);
    document.getElementById("mftBalance").innerText = ethers.utils.formatUnits(balMFT, 18);
    document.getElementById("mstBalance").innerText = ethers.utils.formatUnits(balMST, 18);
  } catch {}
}

async function updateContractLiquidity() {
  try {
    const balMFT = await token1Contract.balanceOf(EXCHANGE_ADDRESS);
    const balMST = await token2Contract.balanceOf(EXCHANGE_ADDRESS);
    document.getElementById("contractMftBalance").innerText = ethers.utils.formatUnits(balMFT, 18);
    document.getElementById("contractMstBalance").innerText = ethers.utils.formatUnits(balMST, 18);
  } catch {}
}

document.getElementById("btnApprove").onclick = async () => {
  const tokenSel = document.getElementById("approveToken").value;
  const amountStr = document.getElementById("approveAmount").value;
  if (!amountStr) return;
  let contract = tokenSel === "MFT" ? token1Contract : token2Contract;
  try {
    const amount = ethers.utils.parseUnits(amountStr, 18);
    const tx = await contract.approve(EXCHANGE_ADDRESS, amount);
    const receipt = await tx.wait();
    displayTxHash(receipt.transactionHash);
    alert(`${tokenSel} approved`);
  } catch (err) {
    alert("Approve failed: " + err.message);
  }
};

document.getElementById("btnDepositMFT").onclick = async () => {
  const amtStr = document.getElementById("depositMFTAmount").value;
  if (!amtStr) return;
  try {
    const amt = ethers.utils.parseUnits(amtStr, 18);
    let tx = await token1Contract.approve(EXCHANGE_ADDRESS, amt);
    let receipt = await tx.wait();
    displayTxHash(receipt.transactionHash);
    tx = await exchangeContract.depositToken1(amt);
    receipt = await tx.wait();
    displayTxHash(receipt.transactionHash);
    alert(`Deposited MFT: ${amtStr}`);
    updateBalances();
    updateContractLiquidity();
  } catch (err) {
    alert("Deposit MFT failed: " + err.message);
  }
};

document.getElementById("btnDepositMST").onclick = async () => {
  const amtStr = document.getElementById("depositMSTAmount").value;
  if (!amtStr) return;
  try {
    const amt = ethers.utils.parseUnits(amtStr, 18);
    let tx = await token2Contract.approve(EXCHANGE_ADDRESS, amt);
    let receipt = await tx.wait();
    displayTxHash(receipt.transactionHash);
    tx = await exchangeContract.depositToken2(amt);
    receipt = await tx.wait();
    displayTxHash(receipt.transactionHash);
    alert(`Deposited MST: ${amtStr}`);
    updateBalances();
    updateContractLiquidity();
  } catch (err) {
    alert("Deposit MST failed: " + err.message);
  }
};

document.getElementById("btnSwap").onclick = async () => {
  const dir = document.getElementById("swapDirection").value;
  const amtStr = document.getElementById("swapAmount").value;
  if (!amtStr) return;
  try {
    const amt = ethers.utils.parseUnits(amtStr, 18);
    const isMFTtoMST = dir === "mftToMst";
    const tx = await exchangeContract.swapTokens(isMFTtoMST, amt);
    const receipt = await tx.wait();
    displayTxHash(receipt.transactionHash);
    alert("Swap done");
    updateBalances();
    updateContractLiquidity();
  } catch (err) {
    alert("Swap failed: " + err.message);
  }
};

document.getElementById("btnUpdateRatio").onclick = async () => {
  const ratioStr = document.getElementById("newRatio").value;
  if (!ratioStr) return;
  try {
    const tx = await exchangeContract.updateRatio(ratioStr);
    const receipt = await tx.wait();
    displayTxHash(receipt.transactionHash);
    alert("Ratio updated");
  } catch (err) {
    alert("Ratio update failed: " + err.message);
  }
};

function displayTxHash(hash) {
  const c = document.getElementById("txHashContainer");
  if (c) {
    c.innerHTML = `
      <p>
        Tx:
        <a href="${EXPLORER_BASE_URL + hash}" target="_blank">
          ${hash}
        </a>
      </p>
    `;
  }
}
