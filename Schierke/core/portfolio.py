import random

class Portfolio:
    def __init__(self):
        self.initial_balance = 10000  # 초기 자본
        self.balance = self.initial_balance

    def calculate_pnl(self):
        profit = random.uniform(-50, 50)  # 임의의 수익/손실 시뮬레이션
        self.balance += profit
        pnl_percentage = ((self.balance - self.initial_balance) / self.initial_balance) * 100
        return {"balance": round(self.balance, 2), "pnl": round(pnl_percentage, 2)}
