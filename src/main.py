from api import AlphaVantageAPI
from key import AVKEY
import os

DIRS = ["data", "img"]

if __name__ == "__main__":
    for d in DIRS:
        if not os.path.exists(d):
            os.makedirs(d)
    
    api = AlphaVantageAPI(AVKEY)

    ticker = "NVDA"
    date = "2025-09-09"

    api.getDailyEquities(ticker, f"data/{ticker}daily.csv")
    api.getCurrentOptionChain(ticker, f"data/{ticker}chain.csv")
    api.getHistoricalOptionChain(ticker, date, f"data/{ticker}{date}chain.csv")

    cfrom = "NZD"
    cto = "USD"

    api.getDailyForex(cfrom, cto, f"data/{cfrom}{cto}daily.csv")

    symbol = "DOGE"

    api.getDailyCrypto(symbol, f"data/{symbol}daily.csv")

    maturity = "10years"

    api.getDailyBonds(maturity, f"data/{maturity}daily.csv")

    api.getDailyWti("data/WTIdaily.csv")
    api.getDailyBrent("data/BRENTdaily.csv")
    api.getDailyNatgas("data/NATGASdaily.csv")
    api.getDailyCopper("data/COPPERdaily.csv")
    api.getDailyAluminum("data/ALUMINUMdaily.csv")
    api.getDailyWheat("data/WHEATdaily.csv")
    api.getDailyCorn("data/CORNdaily.csv")
    api.getDailyCotton("data/COTTONdaily.csv")
    api.getDailySugar("data/SUGARdaily.csv")
    api.getDailyCoffee("data/COFFEEdaily.csv")
    api.getDailyGci("data/GCIdaily.csv")