// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenExchange is Ownable {
    IERC20 public token1; 
    IERC20 public token2; 
    uint256 public ratio; 

    event TokensSwapped(address indexed user, bool indexed isMFTtoMST, uint256 amountIn, uint256 amountOut);
    event DepositToken1(address indexed depositor, uint256 amount);
    event DepositToken2(address indexed depositor, uint256 amount);

    constructor(
        address _token1,
        address _token2,
        uint256 _initialRatio,
        address _owner
    )
        Ownable(_owner)
    {
        token1 = IERC20(_token1);
        token2 = IERC20(_token2);
        ratio = _initialRatio;
    }

    function swapTokens(bool isMFTtoMST, uint256 amountIn) external returns (uint256) {
        require(amountIn > 0, "Cannot swap 0");

        if (isMFTtoMST) {
            require(token1.transferFrom(msg.sender, address(this), amountIn), "transferFrom MFT failed");
            uint256 amountOut = (amountIn * ratio) / 1e18;
            require(token2.transfer(msg.sender, amountOut), "transfer MST failed");
            emit TokensSwapped(msg.sender, true, amountIn, amountOut);
            return amountOut;
        } else {
            require(token2.transferFrom(msg.sender, address(this), amountIn), "transferFrom MST failed");
            uint256 amountOut = (amountIn * 1e18) / ratio;
            require(token1.transfer(msg.sender, amountOut), "transfer MFT failed");
            emit TokensSwapped(msg.sender, false, amountIn, amountOut);
            return amountOut;
        }
    }

    function updateRatio(uint256 newRatio) external onlyOwner {
        require(newRatio > 0, "Ratio must be > 0");
        ratio = newRatio;
    }

    function depositToken1(uint256 amount) external onlyOwner {
        require(amount > 0, "Cannot deposit 0");
        require(token1.transferFrom(msg.sender, address(this), amount), "deposit MFT failed");
        emit DepositToken1(msg.sender, amount);
    }

    function depositToken2(uint256 amount) external onlyOwner {
        require(amount > 0, "Cannot deposit 0");
        require(token2.transferFrom(msg.sender, address(this), amount), "deposit MST failed");
        emit DepositToken2(msg.sender, amount);
    }
}
