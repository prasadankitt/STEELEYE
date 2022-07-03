from django.db import models

# Create your models here.
class TradeDetails(models.Model):
    buySellIndicator = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()

class Trade(models.Model):
    asset_class = models.CharField(max_length=100) 
    counterparty = models.CharField(max_length=100)
    instrument_id = models.CharField(max_length=100)
    instrument_name = models.CharField(max_length=100)
    trade_date_time = models.DateTimeField(auto_now=True)
    trade_details = models.CharField(max_length=100)
    trade_id = models.CharField(max_length=100)
    trader = models.CharField(max_length=100)

    def __str__(self):
        return self.trader