# Generated by Django 3.2.8 on 2021-10-21 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auctionlistings_current_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='current_bid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auctions.bids'),
        ),
    ]
