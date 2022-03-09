//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract SingleNFT is ERC721URIStorage {
    constructor(string memory tokenName, string memory tokenSymbol, string memory tokenURI) public ERC721 (tokenName, tokenSymbol) {
                
        _safeMint(msg.sender, 1);
        _setTokenURI(1, tokenURI);
    }
}