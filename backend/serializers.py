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


