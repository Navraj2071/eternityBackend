# Generated by Django 4.0.1 on 2022-03-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0010_nft_collection_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft_asset',
            name='network',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='nft_collection',
            name='network',
            field=models.IntegerField(default=1),
        ),
    ]
