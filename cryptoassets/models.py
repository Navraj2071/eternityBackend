from django.db import models
from eth_account import Account

# Create your models here.


class profile(models.Model):
    account = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, default="Nameless Hero")
    description = models.CharField(max_length=500, default="Coolest guy ever.")
    profilepic = models.URLField(
        default="https://ipfs.io/ipfs/QmPPpYeRvxRitriYWLh532hjgkUffesbCwshRnQppwmtHv?filename=Beyonce.jpg"
    )


class assets(models.Model):
    metadata = models.URLField
    account = models.CharField(max_length=50)
    is_minted = models.BooleanField
    contract_address = models.CharField(max_length=50)
    on_sale = models.BooleanField
    price = models.FloatField


class erc721contracts(models.Model):
    address = models.CharField(max_length=42, primary_key=True)
    block = models.IntegerField()
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    first_token_URI = models.CharField(max_length=100)


class blocks_scanned(models.Model):
    start_block = models.IntegerField()
    end_block = models.IntegerField()
