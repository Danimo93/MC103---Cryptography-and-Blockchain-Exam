// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Capped.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ERC20 with capped supply and EIP-2612 permit, owned by `initialOwner`.
contract MyFirstToken is ERC20, ERC20Capped, ERC20Permit, Ownable {
    constructor(
        uint256 initialSupply,
        uint256 maxSupply,
        address initialOwner
    )
        ERC20("MyFirstToken", "MFT")
        ERC20Capped(maxSupply * 10**decimals())
        Ownable(initialOwner)
        ERC20Permit("MyFirstToken")
    {
        require(initialSupply <= maxSupply, "Initial supply exceeds cap");
        _mint(initialOwner, initialSupply * 10**decimals());
    }

    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= cap(), "Exceeds cap");
        _mint(to, amount);
    }

    function _update(address from, address to, uint256 amount)
        internal
        override(ERC20, ERC20Capped)
    {
        super._update(from, to, amount);
    }
}
