import os
from dotenv import load_dotenv
import json

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

PAGE_SIZE = 8

SUPER_USER_PASSWORD = os.getenv('SUPER_USER_PASSWORD')
SUPER_USER_NAME = os.getenv('SUPER_USER_NAME')

ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
REFRESH_TOKEN_SECRET = os.getenv('REFRESH_TOKEN_SECRET')

HOSTS_ALLOWED = json.loads(os.getenv('ALLOWED_HOSTS'))

