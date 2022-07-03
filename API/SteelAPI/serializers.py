from rest_framework import serializers
from .models import TradeDetails, Trade

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = {
            'buySellIndicator','price','quantity'
        }

class TradeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeDetails
        fields = {
            'asset_class','counterparty','instrument_id','instrument_name',
            'trade_date_time','trade_details','trade_id','trader'
        }