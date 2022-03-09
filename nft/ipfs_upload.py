from pathlib import Path
import requests


PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"

headers = {
    "pinata_api_key": "5d349f3841ee16d7e668",
    "pinata_secret_api_key": "a6f32583de5736824a606746f0b9b9bc365a5c81b3d1c9f1a98822a39ddfbb6d",
}


def pin_ipfs(filename, filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
        return response.json()


# def pin_ipfs_json(filename, json_object):
#     response = requests.post(
#         PINATA_BASE_URL + endpoint,
#         files={"file": json_object},
#         headers=headers,
#     )
#     return response.json()
