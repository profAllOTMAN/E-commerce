# Generated by Django 3.1.1 on 2020-12-20 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_auto_20201220_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='listings',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='listing_bided', to='auctions.listing'),
        ),
    ]