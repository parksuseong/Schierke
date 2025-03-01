from daemon.daemon import TradingDaemon

def main():
    daemon = TradingDaemon()
    daemon.run()

if __name__ == "__main__":
    main()
