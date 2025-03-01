import random

class Trader:
    def __init__(self):
        self.position = 0  # 현재 보유 포지션

    def execute_trade(self):
        action = random.choice(["buy", "sell", "hold"])
        if action == "buy":
            self.buy()
        elif action == "sell":
            self.sell()
        else:
            print("🔍 대기중...")

    def buy(self):
        self.position += 1
        print(f"🟢 매수 실행! 현재 포지션: {self.position}")

    def sell(self):
        if self.position > 0:
            self.position -= 1
            print(f"🔴 매도 실행! 현재 포지션: {self.position}")
        else:
            print("⚠️ 매도 실패: 보유 포지션 없음")
