# Generated by Django 3.1.1 on 2020-12-01 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_remove_listing_categor'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='categorys',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auctions.category'),
        ),
        migrations.DeleteModel(
            name='relationship',
        ),
    ]
