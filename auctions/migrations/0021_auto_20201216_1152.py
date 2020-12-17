# Generated by Django 3.1.1 on 2020-12-16 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='user_id',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='user_name',
            field=models.CharField(default=None, max_length=64),
        ),
    ]