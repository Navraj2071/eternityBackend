import json

with open(
    "D:\Python/MyNFT/Backend/eternitybackend/nft/brownie/build/contracts/SingleNFT.json",
    "r",
) as file:
    nft_contract = json.load(file)

bytecode = nft_contract["bytecode"]
abi = nft_contract["abi"]
print(bytecode)
