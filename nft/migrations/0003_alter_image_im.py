# Generated by Django 4.0.1 on 2022-02-05 07:25

from django.db import migrations, models
import nft.models


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0002_alter_image_im'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='im',
            field=models.ImageField(upload_to=nft.models.name_file),
        ),
    ]