# Generated by Django 4.0.4 on 2022-07-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_class', models.CharField(max_length=100)),
                ('counterparty', models.CharField(max_length=100)),
                ('instrument_id', models.CharField(max_length=100)),
                ('instrument_name', models.CharField(max_length=100)),
                ('trade_date_time', models.DateTimeField(auto_now=True)),
                ('trade_details', models.CharField(max_length=100)),
                ('trade_id', models.CharField(max_length=100)),
                ('trader', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TradeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buySellIndicator', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
