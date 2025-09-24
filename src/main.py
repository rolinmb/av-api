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
    api.getDailyEquities(ticker, f"data/{ticker}daily.csv")
    api.getWeeklyEquities(ticker, f"data/{ticker}weekly.csv")
    api.getMonthyEquities(ticker, f"data/{ticker}monthly.csv")

    date = "2025-09-22"
    api.getCurrentOptionChain(ticker, f"data/{ticker}chain.csv")
    api.getHistoricalOptionChain(ticker, date, f"data/{ticker}{date}chain.csv")

    cfrom = "NZD"
    cto = "USD"
    api.getDailyForex(cfrom, cto, f"data/{cfrom}{cto}daily.csv")
    api.getWeeklyForex(cfrom, cto, f"data/{cfrom}{cto}weekly.csv")
    api.getMonthlyForex(cfrom, cto, f"data/{cfrom}{cto}monthly.csv")

    symbol = "DOGE"
    api.getDailyCrypto(symbol, f"data/{symbol}daily.csv")
    api.getWeeklyCrypto(symbol, f"data/{symbol}weekly.csv")
    api.getMonthlyCrypto(symbol, f"data/{symbol}monthly.csv")

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
    api.getGci("monthly", "data/GCImonthly.csv")

    createSeriesChart(f"data/{cfrom}{cto}daily.csv", f"img/{cfrom}{cto}daily.png")

    createSeriesChart("data/GCIdaily.csv", "img/GCIdaily.csv")

    createOptionSurface(f"data/{ticker}chain.csv", f"img/{ticker}civ.png", f"img/{ticker}piv.png")