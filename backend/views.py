
from rest_framework import generics, status
from rest_framework.response import Response
import requests
from backend.models import *
from backend.serializers import *
import datetime
import pytz
import pandas as pd
from common.commonFunctions import AnagelOneConnector

class TestView(generics.ListAPIView):

    def list(self, request, *args, **kwargs):
        return Response({"status": True, "message": "Success", "data": {"Test paased"}}, status=status.HTTP_201_CREATED)
    
def add_scripts_to_db():
    url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
    try:
        data = requests.get(url).json()
    except Exception as err:
        data = list()
    df = pd.DataFrame(data)
    data = df[df['exch_seg'].isin(['NFO', 'BSE', 'NSE'])].to_dict('records')
    Scripts.objects.all().delete()
    print(len(data))
    count = 1
    while data:
        new_data = data[:100]
        serializer = ScriptSerializer(data=new_data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = data[100:]
        print(count)
        count+=1

class TokenView(generics.ListAPIView):
    queryset = Scripts.objects.all()
    serializer_class = ScriptSerializer
    def list(self, request, *args, **kwargs):
        args = request.GET
        expiry = args.get('expiry')
        name = args.get('name')
        strike = args.get('strike')
        exchange = args.grt('exchange')
        qs = self.get_queryset()

        if expiry:
            try:
                expiry = datetime.datetime.strptime(expiry,"%Y-%m-%d")
            except:
                return Response({"status": False, "message": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            utc_datetime = datetime.datetime.now(tz=pytz.UTC)
            local_timezone = pytz.timezone('Asia/Kolkata')
            local_datetime = utc_datetime.astimezone(local_timezone)
            expiry = local_datetime + datetime.timedelta( (3-local_datetime.weekday()) % 7 )

        month = expiry.strftime('%b').upper()
        year = expiry.strftime('%Y')
        day = expiry.strftime('%d')
        expiry = f'{day}{month}{year}'
        qs = qs.filter(expiry=expiry)
        if exchange:
            qs = qs.filter(exchange=exchange)
        if name:
            qs = qs.filter(name__icontains=name)
        if strike:
            qs = qs.filter(strike__icontains=strike)
        response_data = list()
        if qs.count():
            serializer = self.get_serializer(qs,many=True)
            response_data = serializer.data
        return Response({"status": True, "message": "Success", "data": response_data}, status=status.HTTP_200_OK)



class OrdersView(generics.CreateAPIView):
    serializer_class = PlaceOrderSerializer
    def create(self, request, *args, **kwargs):
        try:
            data = dict(request.data)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            ordertype = data['ordertype']
            params = {
                "tradingsymbol": data['script']['symbol'],
                "symboltoken": data['script']['token'],
                "Exchange": data['exchange'],
                "transactiontype": data['transactiontype'],
                "ordertype": ordertype,
                "quantity": data['lot'] * data['script']['lotsize'],
                "producttype": data['producttype'],
                "duration": "DAY"
            }

            if ordertype == 'LIMIT':
                params['price'] = data['price']
            try:
                smartAPI = AnagelOneConnector().connect()
                res = smartAPI.placeOrder(params)
                responseJson = res.json()
            except:
                return Response({"status": False, "message": "Failed to place order"}, status=status.HTTP_400_BAD_REQUEST)

            if not responseJson['status']:
                return Response({"status": False, "message": f"Failed to place order, ERROR: {responseJson['message']}"},
                status=status.HTTP_400_BAD_REQUEST)
            
            orderId = responseJson['data']['orderid']
        except Exception as e:
            return Response({"status": False, "message": "Failed to place order"}, status=status.HTTP_400_BAD_REQUEST)




        

        



            