from api import AlphaVantageAPI
from key import AVKEY
import os

if __name__ == "__main__":
    dirs = ["img", "data"]
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)

    ticker = "NVDA"
    date = "2025-09-09"
    
    api = AlphaVantageAPI(AVKEY)

    api.getDailyEquities(ticker, f"data/{ticker}daily.csv")
    api.getCurrentOptionChain(ticker, f"data/{ticker}chain.csv")
    api.getHistoricalOptionChain(ticker, date, f"data/{ticker}{date}chain.csv")

    cfrom = "NZD"
    cto = "USD"

    api.getDailyForex(cfrom, cto, f"data/{cfrom}{cto}daily.csv")

    symbol = "DOGE"

    api.getDailyCrypto(symbol, f"data/{symbol}daily.csv")