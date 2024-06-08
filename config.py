import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
AUTHORIZATION_BASE_URL = os.getenv('AUTHORIZATION_BASE_URL')
TOKEN_URL = os.getenv('TOKEN_URL')
