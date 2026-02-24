import os
from binance.client import Client
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class BinanceTestnetClient:
    def __init__(self):
        self.api_key = os.getenv('BINANCE_API_KEY')
        self.api_secret = os.getenv('BINANCE_API_SECRET')
        
        if not self.api_key or not self.api_secret:
            raise ValueError("API Keys not found. Please check your .env file.")
        
        # Connect to Testnet
        self.client = Client(self.api_key, self.api_secret, testnet=True)

    def get_client(self):
        return self.client