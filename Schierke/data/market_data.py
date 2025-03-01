from dotenv import load_dotenv
import os
from binance.client import Client

# 환경 변수 불러오기
load_dotenv()

class MarketData:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        self.client = Client(api_key, api_secret)

    def get_price(self, symbol="BTCUSDT"):
        try:
            ticker = self.client.get_symbol_ticker(symbol=symbol)
            return float(ticker["price"])
        except Exception as e:
            print(f"❌ 시세 조회 실패: {e}")
            return None
