import time
from Schierke.core.trader import Trader
from Schierke.renderer.terminal_view import TerminalView
from Schierke.core.portfolio import Portfolio

class TradingDaemon:
    def __init__(self):
        self.trader = Trader()
        self.portfolio = Portfolio()
        self.renderer = TerminalView()

    def run(self):
        print("🚀 트레이딩 데몬 시작!")
        try:
            while True:
                self.trader.execute_trade()
                pnl = self.portfolio.calculate_pnl()
                self.renderer.render(pnl)
                time.sleep(5)  # 5초 간격으로 거래 및 업데이트
        except KeyboardInterrupt:
            print("\n🛑 데몬 중지됨.")
