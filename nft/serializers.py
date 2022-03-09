from rest_framework import serializers
from .models import image, nft, metadata, nft_asset, nft_collection


class image_serializer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields = "__all__"


class nft_serializer(serializers.ModelSerializer):
    class Meta:
        model = nft
        fields = "__all__"


class metadata_serializer(serializers.ModelSerializer):
    class Meta:
        model = metadata
        fields = "__all__"


class nft_collection_serializer(serializers.ModelSerializer):
    class Meta:
        model = nft_collection
        fields = "__all__"


class nft_asset_serializer(serializers.ModelSerializer):
    class Meta:
        model = nft_asset
        fields = "__all__"
