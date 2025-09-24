from api import AlphaVantageAPI
from key import AVKEY

if __name__ == "__main__":
    ticker = "NVDA"
    date = "2025-09-09"
    api = AlphaVantageAPI(AVKEY)
    api.getDailyEquities(ticker)
    api.getCurrentOptionChain(ticker)
    api.getHistoricalOptionChain(ticker)
    api.getHistoricalOptionChain(ticker, date)