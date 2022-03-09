from .tools import get_account
from brownie import SingleNFT

token_name = "mynft"
token_symbol = "MNFT"
token_URI = "https://ipfs.io/ipfs/Qmf7H3RkBN9uXB7mrrc1maoAgUxz1DdDNfCLxSHk3vLUC9?filename=file.json"


def deploy_from_api(token_name, token_symbol, token_URI, account):
    token_name = token_name
    token_symbol = token_symbol
    token_URI = token_URI
    nft = SingleNFT.deploy(token_name, token_symbol, token_URI, {"from": account})
    return nft


def main():
    account = get_account()
    SingleNFT.deploy(token_name, token_symbol, token_URI, {"from": account})
    print("NFT deployed. Yay!")
