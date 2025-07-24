from dotenv import load_dotenv
import os

load_dotenv('./seila.env')

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_SANDBOX_NUMBER = os.environ.get('TWILIO_SANDBOX_NUMBER')