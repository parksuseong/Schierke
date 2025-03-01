class TerminalView:
    def render(self, pnl_data):
        balance = pnl_data["balance"]
        pnl = pnl_data["pnl"]
        status = "📈" if pnl >= 0 else "📉"
        print(f"{status} 현재 잔고: ${balance} | 수익률: {pnl}%")
