// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Capped.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MySecondToken is ERC20, ERC20Capped, ERC20Permit, Ownable {
    constructor(
        uint256 initialSupply,
        uint256 maxSupply,
        address initialOwner
    )
        ERC20("MySecondToken", "MST")
        ERC20Capped(maxSupply * 10**decimals())
        ERC20Permit("MySecondToken")
        Ownable(initialOwner)
    {
        require(initialSupply <= maxSupply, "Initial supply exceeds max");
        _mint(initialOwner, initialSupply * 10**decimals());
    }

    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= cap(), "Exceeds max supply");
        _mint(to, amount);
    }

    function _update(address from, address to, uint256 amount)
        internal
        override(ERC20, ERC20Capped)
    {
        super._update(from, to, amount);
    }
}
