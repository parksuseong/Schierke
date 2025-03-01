from dotenv import load_dotenv
from data.market_data import MarketData

# 환경 변수 불러오기
load_dotenv()

def main():
    market_data = MarketData()
    price = market_data.get_price("BTCUSDT")
    print(f"📊 BTCUSDT 현재 가격: ${price}")

if __name__ == "__main__":
    main()
