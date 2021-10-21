# Generated by Django 3.2.8 on 2021-10-21 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_auctionlistings_current_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlistings',
            name='current_bid',
        ),
        migrations.AddField(
            model_name='auctionlistings',
            name='starting_bid',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bids',
            name='bid_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_price', to='auctions.auctionlistings'),
        ),
    ]
