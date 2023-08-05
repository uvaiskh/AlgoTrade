from rest_framework import serializers
from backend.models import *

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scripts
        fields = ['token', 'symbol', 'name', 'expiry', 'expiry', 'strike', 'lotsize', 'instrumenttype', 'exch_seg', 'tick_size']

    def __init__(self, instance=None, data=..., **kwargs):
        super(ScriptSerializer, self).__init__(instance, data, **kwargs)
        if "expiry" not in self.fields:
            self.fields['expiry'] = None
        
        if "instrumenttype" not in self.fields:
            self.fields['instrumenttype'] = None

class PlaceOrderSerializer(serializers.Serializer):
    exchange = serializers.CharField() # BSE, NSE NFO MCX
    transactiontype = serializers.CharField() # BUY SELL
    ordertype = serializers.CharField() # MARKET LIMIT STOPLOSS_LIMIT STOPLOSS_MARKET
    lot = serializers.IntegerField()
    producttype = serializers.CharField() # DELIVERY CARRYFORWARD MARGIN INTRADAY BO
    script = serializers.DictField()
    # variety = serializers.CharField() # NORMAL STOPLOSS AMO ROBO
    # Duration = serializers.CharField() # DAY IOC
    

