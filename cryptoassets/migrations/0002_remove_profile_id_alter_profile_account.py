# Generated by Django 4.0.1 on 2022-02-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoassets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='profile',
            name='account',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
