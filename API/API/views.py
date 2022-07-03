from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from SteelAPI.serializers import TradeSerializer,TradeSerializer
from SteelAPI.models import Trade,TradeDetails

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        # data = {
        #     'asset_class' : 'Bond',
        #     'counterparty' : 'None',
        #     'instrument_id' : 'AAPL',
        #     'instrument_name' : 'Car',
        #     'trade_details' : 'confirmed',
        #     'trade_id' : 'Tradeid',
        #      'trader' : 'steel'
        # }
        qs = Trade.objects.all()
        serializer = TradeSerializer(qs, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        serializer = TradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)