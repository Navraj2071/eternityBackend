from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse


from .models import nft, nft_collection, nft_asset
from .serializers import nft_serializer, nft_collection_serializer, nft_asset_serializer
from .ipfs_upload import pin_ipfs
from .sample_metadata import metadata_template
import json
import os
from django.conf import settings



class MultiNFTViewSet(generics.ListAPIView):
    queryset = nft.objects.all()
    serializer_class = nft_serializer

    def post(self, request, *args, **kwargs):
        # Request objects.
        file = request.data["nft_file"]
        account = request.data["account"]

        nft.objects.create(nft_file=file, account=account)
        filename = str(file.name)
        filepath = "./media/nft_files/" + str(account) + "/" + filename
        pinata_response = pin_ipfs(filename=filename, filepath=filepath)

        nft_name = filename.split(".")[0]
        metadata_file_path = (
            "./media/nft_files/" + str(account) + "/" + nft_name + ".json"
        )
        metadata = metadata_template
        metadata["name"] = request.data["name"]
        metadata["description"] = request.data["description"]
        image_uri = (
            "https://ipfs.io/ipfs/"
            + str(pinata_response["IpfsHash"])
            + "?filename="
            + filename
        )
        metadata["image"] = image_uri
        metadata["traits"] = []
        print("Metadata")
        print(metadata)
        for i in range(int(request.data["trait_number"])):

            metadata["traits"].append(
                {
                    "trait_type": request.data["trait_type" + str(i)],
                    "value": float(request.data["trait_value" + str(i)])
                    # request.data["trait_type" + str(i)]: float(
                    #     request.data["trait_value" + str(i)]
                    # )
                }
            )
        print(metadata)
        with open(metadata_file_path, "w") as file:
            json.dump(metadata, file)
        pinata_response_metadata = pin_ipfs(
            filename=(nft_name + ".json"), filepath=metadata_file_path
        )
        metadata_uri = (
            "https://ipfs.io/ipfs/"
            + str(pinata_response_metadata["IpfsHash"])
            + "?filename="
            + (nft_name + ".json")
        )
        print(metadata_uri)
        response_object = {"image_uri": image_uri, "metadata_uri": metadata_uri}

        return Response(response_object)


class NFTViewSet(generics.ListAPIView):
    queryset = nft.objects.all()
    serializer_class = nft_serializer

    def post(self, request, *args, **kwargs):
        # Request objects.
        file = request.data["nft_file"]
        account = request.data["account"]

        nft.objects.create(nft_file=file, account=account)
        filename = str(file.name)
        filepath = "./media/nft_files/" + str(account) + "/" + filename
        pinata_response = pin_ipfs(filename=filename, filepath=filepath)

        nft_name = filename.split(".")[0]
        metadata_file_path = (
            "./media/nft_files/" + str(account) + "/" + nft_name + ".json"
        )
        metadata = metadata_template
        metadata['traits'] = [{'trait_type': 'trait_type', 'value': 'value'}]
        metadata["name"] = request.data["name"]
        metadata["description"] = request.data["description"]
        image_uri = (
            "https://ipfs.io/ipfs/"
            + str(pinata_response["IpfsHash"])
            + "?filename="
            + filename
        )
        metadata["image"] = image_uri
        metadata["traits"][0]["trait_type"] = request.data["trait_type"]
        metadata["traits"][0]["value"] = request.data["value"]

        with open(metadata_file_path, "w") as file:
            json.dump(metadata, file)
        pinata_response_metadata = pin_ipfs(
            filename=(nft_name + ".json"), filepath=metadata_file_path
        )
        metadata_uri = (
            "https://ipfs.io/ipfs/"
            + str(pinata_response_metadata["IpfsHash"])
            + "?filename="
            + (nft_name + ".json")
        )
        response_object = {"image_uri": image_uri, "metadata_uri": metadata_uri}
        os.remove(os.path.join(settings.MEDIA_ROOT, "./nft_files/" + str(account) + "/" + filename))
        os.remove(os.path.join(settings.MEDIA_ROOT, "./nft_files/" + str(account) + "/" + nft_name + ".json"))
        return Response(response_object)

class CreateNFTViewSet(generics.ListAPIView):
    queryset = nft_asset.objects.all()
    serializer_class = nft_asset_serializer

    def post(self, request, *args, **kwargs):
        # Request objects.
        owner = request.data["owner"]
        metadataURL = request.data["metadataURL"]
        collection = request.data["collection"]
        on_sale = request.data["on_sale"]
        is_minted = request.data["is_minted"]
        contract_address = request.data["contract_address"]
        token_id = request.data["token_id"]
        price = request.data["price"]
        network = request.data["network"]
        nft_asset.objects.create(
                owner=owner,
                metadataURL=metadataURL,
                collection=collection,
                on_sale=get_boolean(on_sale),
                is_minted=get_boolean(is_minted),
                contract_address=contract_address,
                token_id=token_id,
                price=price,
                network=network,
            )


class CollectionViewSet(generics.ListAPIView):
    queryset = nft_collection.objects.all()
    serializer_class = nft_collection_serializer

    def post(self, request, *args, **kwargs):
        id = request.data["collection_id"]
        name = request.data["collection_name"]
        description = request.data["collection_description"]
        total_supply = request.data["total_supply"]
        price = request.data["price"]
        launch_date = request.data["launch_date"]
        launch_time = request.data["launch_time"]
        owner = request.data["owner"]
        nft_data = request.data["metadata"]
        contract = request.data["contract"]
        network = request.data["network"]
        if nft_collection.objects.filter(pk=id).exists():
            nft_collection.objects.filter(pk=id).update(
                name=name,
                description=description,
                total_supply=total_supply,
                price=price,
                launch_date=launch_date,
                launch_time=launch_time,
                owner=owner,
                nft_data=nft_data,
                contract=contract,
                network=network,
            )
        else:
            nft_collection.objects.create(
                id=id,
                name=name,
                description=description,
                total_supply=total_supply,
                price=price,
                launch_date=launch_date,
                launch_time=launch_time,
                owner=owner,
                nft_data=nft_data,
                contract=contract,
                network=network,
            )
        for token_id in range(1, int(total_supply) + 1):
            nft_asset.objects.create(
                owner=owner,
                metadataURL=json.loads(nft_data)["nft" + str(token_id - 1)],
                collection=id,
                on_sale=False,
                is_minted=False,
                contract_address="0x",
                token_id=0,
                price=price,
                network=network,
            )
        return Response("Collection created successfully.")


def get_collection_data(request):
    if nft_collection.objects.filter(pk=request.GET["collectionid"]).exists():
        collection_data = nft_collection.objects.filter(
            pk=request.GET["collectionid"]
        ).values()
        response_data = {
            "response": "Success",
            "name": collection_data[0]["name"],
            "description": collection_data[0]["description"],
            "total_supply": collection_data[0]["total_supply"],
            "price": collection_data[0]["price"],
            "launch_date": collection_data[0]["launch_date"],
            "launch_time": collection_data[0]["launch_time"],
            "owner": collection_data[0]["owner"],
            "nft_data": collection_data[0]["nft_data"],
            "contract": collection_data[0]["contract"],
            "network": collection_data[0]["network"],
        }
        return JsonResponse(response_data)
    else:
        print("Returning doesn't exist")
        return JsonResponse({"response": "Collection doesn't exist"})


def update_collection_contract(request):
    if nft_collection.objects.filter(pk=request.GET["collectionid"]).exists():
        nft_collection.objects.filter(pk=request.GET["collectionid"]).update(
            contract=request.GET["contract"]
        )
        return JsonResponse({"response": "Success"})
    else:
        return JsonResponse({"response": "Collection doesn't exist"})


def get_nft_data(request):
    if request.GET["request_type"] == "withMetadata":
        print(request.GET["metadataURL"])
        if nft_asset.objects.filter(metadataURL=request.GET["metadataURL"]).exists():
            nft_data = nft_asset.objects.filter(
                metadataURL=request.GET["metadataURL"]
            ).values()
            response_data = {
                "response": "Success",
                "owner": nft_data[0]["owner"],
                "metadataURL": nft_data[0]["metadataURL"],
                "collection": nft_data[0]["collection"],
                "on_sale": nft_data[0]["on_sale"],
                "is_minted": nft_data[0]["is_minted"],
                "price": nft_data[0]["price"],
                "contract_address": nft_data[0]["contract_address"],
                "token_id": nft_data[0]["token_id"],
                "network": nft_data[0]["network"],
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({"response": "NFT doesn't exist"})
    elif request.GET["request_type"] == "withContract":
        contract_address = request.GET["asset_id"].split("_")[0]
        token_id = request.GET["asset_id"].split("_")[1]
        if nft_asset.objects.filter(contract_address=contract_address, token_id=token_id).exists():
            print('NFT Found-----')
            nft_data = nft_asset.objects.filter(contract_address=contract_address, token_id=token_id).values()
            response_data = {
                "response": "Success",
                "owner": nft_data[0]["owner"],
                "metadataURL": nft_data[0]["metadataURL"],
                "collection": nft_data[0]["collection"],
                "on_sale": nft_data[0]["on_sale"],
                "is_minted": nft_data[0]["is_minted"],
                "price": nft_data[0]["price"],
                "contract_address": nft_data[0]["contract_address"],
                "token_id": nft_data[0]["token_id"],
                "network": nft_data[0]["network"],
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({"response": "NFT doesn't exist"})

        


def get_boolean(boolean_string):
    if boolean_string == "True":
        return True
    else:
        return False


class NFTUpdateViewSet(generics.ListAPIView):
    queryset = nft_asset.objects.all()
    serializer_class = nft_asset_serializer

    def post(self, request, *args, **kwargs):
        owner = request.data["owner"]
        metadataURL = request.data["metadataURL"]
        collection = request.data["collection"]
        on_sale = get_boolean(request.data["on_sale"])
        is_minted = get_boolean(request.data["is_minted"])
        price = request.data["price"]
        contract_address = request.data["contract_address"]
        token_id = request.data["token_id"]
        network = request.data["network"]
        nft_asset.objects.filter(metadataURL=metadataURL).update(
            owner=owner,
            metadataURL=metadataURL,
            collection=collection,
            on_sale=on_sale,
            is_minted=is_minted,
            contract_address=contract_address,
            token_id=token_id,
            price=price,
            network=network,
        )
        return Response("Success")
