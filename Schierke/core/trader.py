from binance.client import Client
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()


class Trader:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        self.client = Client(api_key, api_secret)

    def get_balance(self, asset="USDT"):
        """잔고 조회"""
        try:
            balance = self.client.get_asset_balance(asset=asset)
            return float(balance["free"])  # 사용 가능한 잔고만 반환
        except Exception as e:
            print(f"❌ 잔고 조회 실패: {e}")
            return None

    def buy(self, symbol="BTCUSDT", quantity=0.001):
        """매수 주문 실행"""
        try:
            order = self.client.order_market_buy(symbol=symbol, quantity=quantity)
            print(f"✅ 매수 성공! 주문 ID: {order['orderId']}")
            return order
        except Exception as e:
            print(f"❌ 매수 실패: {e}")
            return None

    def sell(self, symbol="BTCUSDT", quantity=0.001):
        """매도 주문 실행"""
        try:
            order = self.client.order_market_sell(symbol=symbol, quantity=quantity)
            print(f"✅ 매도 성공! 주문 ID: {order['orderId']}")
            return order
        except Exception as e:
            print(f"❌ 매도 실패: {e}")
            return None
