from conf import ANGEL_TOTP, ANGEL_API_KEY, ANGLE_CLIENT_ID, ANGEL_PIN
from SmartApi import SmartConnect
import pyotp

class AnagelOneConnector:
    def __init__(self):
        self.totp = ANGEL_TOTP
        self.apiKey = ANGEL_API_KEY
        self.clientId = ANGLE_CLIENT_ID
        self.pwd = ANGEL_PIN
        self.authToken = None
        self.refreshToken = None
    

    def connect(self):
        smartApi = SmartConnect(self.apiKey)
        totp = pyotp.TOTP(self.totp).now()
        data = smartApi.generateSession(self.clientId, self.pwd, totp)
        # self.authToken = data['data']['jwtToken']
        # self.refreshToken = data['data']['refreshToken']
        # print(self.authToken)
        # feedToken = smartApi.getfeedToken()
        # smartApi.ltpData()
        exchange = 'NFO' 
        tradingsymbol = 'BANKNIFTY31AUG2345000PE'
        symboltoken = '60496'
        data = smartApi.ltpData(exchange, tradingsymbol, symboltoken)
        print(data)






