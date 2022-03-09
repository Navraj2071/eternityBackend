from rest_framework import generics
from rest_framework.response import Response
from .models import profile, assets, erc721contracts, blocks_scanned
from .serializers import (
    profile_serializer,
    assets_serializer,
    erc721contracts_serializer,
    scanned_blocks_serializer,
)
from django.http import HttpResponse, JsonResponse


DEFAUL_NAME = "Nameless Hero"
DEFAULT_PROFILEPIC = "https://ipfs.io/ipfs/QmPPpYeRvxRitriYWLh532hjgkUffesbCwshRnQppwmtHv?filename=Beyonce.jpg"
DEFAULT_DESCRIPTION = "Coolest guy ever."


class ProfileViewSet(generics.ListAPIView):
    queryset = profile.objects.all()
    serializer_class = profile_serializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        account = request.data["account"]
        if profile.objects.filter(pk=account).exists():
            existing_profile = profile.objects.get(pk=account)
            if request.data["name"] != "":
                existing_profile.name = request.data["name"]
            if request.data["profilepic"] != "":
                existing_profile.profilepic = request.data["profilepic"]
            if request.data["description"] != "":
                existing_profile.description = request.data["description"]
            existing_profile.save()
            profile_data = {
                "name": existing_profile.name,
                "profilepic": existing_profile.profilepic,
                "description": existing_profile.description,
            }
        else:
            if request.data["name"] != "":
                name = request.data["name"]
            else:
                name = DEFAUL_NAME
            if request.data["profilepic"] != "":
                profilepic = request.data["profilepic"]
            else:
                profilepic = DEFAULT_PROFILEPIC
            if request.data["description"] != "":
                description = request.data["description"]
            else:
                description = DEFAULT_DESCRIPTION
            new_profile = profile.objects.create(
                account=account,
                name=name,
                profilepic=profilepic,
                description=description,
            )
            profile_data = {
                "name": new_profile.name,
                "profilepic": new_profile.profilepic,
                "description": new_profile.description,
            }

        return Response(profile_data)


# def add_contracts(request):
#     start_block = int(request.GET["startBlock"])
#     end_block = int(request.GET["endBlock"])
#     # get_contracts(start_block=start_block, end_block=end_block)

#     return HttpResponse(
#         "<h1>Start Block = </>"
#         + str(start_block)
#         + "<h1>End Block = </>"
#         + str(end_block)
#     )
def check_contract_existance(request):
    value = erc721contracts.objects.filter(pk=request.GET["contract"]).exists()
    return JsonResponse({"answer": value})


class ScannedBlocksViewSet(generics.ListAPIView):
    queryset = blocks_scanned.objects.all()
    serializer_class = scanned_blocks_serializer

    def post(self, request, *args, **kwargs):
        start_block = request.data["start_block"]
        end_block = request.data["end_block"]
        blocks_scanned.objects.create(start_block=start_block, end_block=end_block)
        return Response("Blocks Saved Successfully.")


class ContractsViewSet(generics.ListAPIView):
    queryset = erc721contracts.objects.all()
    serializer_class = erc721contracts_serializer

    def post(self, request, *args, **kwargs):
        address = request.data["address"]
        block = request.data["block"]
        name = request.data["name"]
        symbol = request.data["symbol"]
        first_token_URI = request.data["first_token_URI"]
        erc721contracts.objects.create(
            address=address,
            block=block,
            name=name,
            symbol=symbol,
            first_token_URI=first_token_URI,
        )

        return Response(request.data)
