# Generated by Django 3.2.8 on 2021-10-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20211021_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='bid_price',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]