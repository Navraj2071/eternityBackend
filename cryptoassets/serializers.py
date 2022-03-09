from rest_framework import serializers
from .models import profile, assets, erc721contracts, blocks_scanned


class profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = "__all__"


class assets_serializer(serializers.ModelSerializer):
    class Meta:
        model = assets
        fields = "__all__"


class erc721contracts_serializer(serializers.ModelSerializer):
    class Meta:
        model = erc721contracts
        fields = "__all__"


class scanned_blocks_serializer(serializers.ModelSerializer):
    class Meta:
        model = blocks_scanned
        fields = "__all__"
