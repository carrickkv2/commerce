# Generated by Django 3.2.8 on 2021-10-21 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bids',
            old_name='listing',
            new_name='listings',
        ),
    ]