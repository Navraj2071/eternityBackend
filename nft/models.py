from django.db import models


# Create your models here.


def name_file(instance, filename):
    return "/".join(["nft_files", str(instance.account), filename])


class image(models.Model):
    id = models.AutoField(primary_key=True)
    im = models.ImageField(upload_to=name_file)


class nft(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=100)
    nft_file = models.FileField(upload_to=name_file)


class metadata(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=100)


class nft_collection(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    total_supply = models.IntegerField()
    price = models.FloatField()
    launch_date = models.DateField()
    launch_time = models.TimeField()
    owner = models.CharField(max_length=50)
    nft_data = models.JSONField()
    contract = models.CharField(max_length=50, default='0x')
    network = models.IntegerField(default=1)


class nft_asset(models.Model):
    owner = models.CharField(max_length=50)
    metadataURL = models.URLField()
    collection = models.CharField(max_length=100)
    on_sale = models.BooleanField()
    is_minted = models.BooleanField()
    price = models.FloatField()
    contract_address = models.CharField(max_length=50)
    token_id = models.IntegerField()
    network = models.IntegerField(default=1)
