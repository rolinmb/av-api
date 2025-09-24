from api import AlphaVantageAPI
from key import AVKEY
from utils import *
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
    api.getBonds("daily", maturity, f"data/{maturity}daily.csv")

    api.getWti("daily", "data/WTIdaily.csv")
    api.getBrent("daily", "data/BRENTdaily.csv")
    api.getNatgas("daily", "data/NATGASdaily.csv")
    api.getCopper("daily", "data/COPPERdaily.csv")
    api.getAluminum("daily", "data/ALUMINUMdaily.csv")
    api.getWheat("daily", "data/WHEATdaily.csv")
    api.getCorn("daily", "data/CORNdaily.csv")
    api.getCotton("daily", "data/COTTONdaily.csv")
    api.getSugar("daily", "data/SUGARdaily.csv")
    api.getCoffee("daily", "data/COFFEEdaily.csv")
    api.getGci("daily", "data/GCIdaily.csv")

    createSeriesChart(f"data/{cfrom}{cto}daily.csv", f"img/{cfrom}{cto}daily.png")
    
    createSeriesChart("data/GCIdaily.csv", "img/GCIdaily.csv")

    createOptionSurface(f"data/{ticker}chain.csv", f"img/{ticker}civ.png", f"img/{ticker}piv.png")