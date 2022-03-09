from web3 import Web3
import json, requests

with open(
    "D:/Python/MyNFT/Backend/eternitybackend/cryptoassets/SingleNFT.json", "r"
) as file:
    contract = json.load(file)
ABI = contract["abi"]

w3 = Web3(
    Web3.HTTPProvider("https://mainnet.infura.io/v3/af7a38f98bcd4ebbbc7c0c844640104f")
)


def check_contract_existance(contract_address):
    response = requests.get(
        url="http://localhost:8000/assets/checkcontractexistance",
        params={"contract": contract_address},
    )
    return response.json()["answer"]


def add_contract_data(contract_address, block):
    this_contract = w3.eth.contract(address=contract_address, abi=ABI)
    try:
        name = this_contract.functions.name().call()
        symbol = this_contract.functions.symbol().call()
        first_token_URI = this_contract.functions.tokenURI(1).call()
        post_data = {
            "name": name,
            "symbol": symbol,
            "first_token_URI": first_token_URI,
            "block": block,
            "address": contract_address,
        }
        requests.post("http://localhost:8000/assets/addcontracts", data=post_data)

    except:
        print("Data Failed to comply.")


def add_contracts(start_block, end_block):
    for block in range(start_block, end_block):
        print("Block:")
        print(block)
        tx_hash_list = w3.eth.get_block(block).transactions
        for tx_hash in tx_hash_list:
            tx = w3.eth.get_transaction(tx_hash.hex())
            print(tx["to"])
            try:
                if len(tx["to"]) < 40 and not check_contract_existance(tx["to"]):
                    print("Transaction to ----------------")
                    print(tx["to"])
                    add_contract_data(tx["to"], block=block)
            except:
                print("Address invalid.")
            print(tx["from"])
            try:
                if len(tx["from"]) < 40 and not check_contract_existance(tx["from"]):
                    print("Transaction from ----------------")
                    print(tx["from"])
                    add_contract_data(tx["from"], block=block)
            except:
                print("Address invalid.")
    response = requests.post(
        "http://localhost:8000/assets/scannedBlocks",
        data={"start_block": start_block, "end_block": end_block},
    )


add_contracts(14282000, 14282399)


# trans = w3.eth.get_block("latest").transactions[2].hex()

# contract_address = w3.eth.get_transaction(
#     "0xf0489d65f4c4fef1ed2a00d40731b3146b804b7ac0d4ef456062f0a610580170"
# ).to

# contract_address = "0xdA858C5183e9024C0D5301ee85AE1e41dbe0F880"
# abi = contract["abi"]
# nft = w3.eth.contract(address=contract_address, abi=abi)
# owner = nft.functions.ownerOf(1).call()

# print(owner)
