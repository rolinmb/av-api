from api import AlphaVantageAPI
from consts import DIRS
from key import AVKEY
from utils import *
import os

if __name__ == "__main__":
    for d in DIRS:
        if not os.path.exists(d):
            os.makedirs(d)
    
    api = AlphaVantageAPI(AVKEY)

    ticker = "NVDA"
    api.getDailyEquities(ticker, f"data/{ticker}daily.csv")
    api.getWeeklyEquities(ticker, f"data/{ticker}weekly.csv")
    api.getMonthyEquities(ticker, f"data/{ticker}monthly.csv")
    api.getCurrentOptionChain(ticker, f"data/{ticker}chain.csv")

    date = "2025-09-22"
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
    api.getBrent("weekly", "data/BRENTweekly.csv")
    api.getNatgas("monthly", "data/NATGASmonthly.csv")
    api.getCopper("monthly", "data/COPPERmonthly.csv")
    api.getAluminum("quarterly", "data/ALUMINUMquarterly.csv")
    api.getWheat("annual", "data/WHEATannual.csv")
    api.getCorn("monthly", "data/CORNmonthly.csv")
    api.getCotton("quarterly", "data/COTTONquarterly.csv")
    api.getSugar("annual", "data/SUGARannual.csv")
    api.getCoffee("monthly", "data/COFFEEmonthly.csv")
    api.getGci("quarterly", "data/GCIquarterly.csv")

    createSeriesChart(f"data/{cfrom}{cto}daily.csv", f"img/{cfrom}{cto}daily.png")

    createSeriesChart("data/GCIquarterly.csv", "img/GCIquarterly.png")

    createOptionSurface("implied_volatility", f"data/{ticker}chain.csv", f"img/{ticker}civ.png", f"img/{ticker}piv.png")
    createOptionSurface("delta", f"data/{ticker}chain.csv", f"img/{ticker}cdelta.png", f"img/{ticker}pdelta.png")
    createOptionSurface("gamma", f"data/{ticker}chain.csv", f"img/{ticker}cgamma.png", f"img/{ticker}pgamma.png")
    createOptionSurface("theta", f"data/{ticker}chain.csv", f"img/{ticker}ctheta.png", f"img/{ticker}ptheta.png")
    createOptionSurface("vega", f"data/{ticker}chain.csv", f"img/{ticker}cvega.png", f"img/{ticker}pvega.png")
    createOptionSurface("rho", f"data/{ticker}chain.csv", f"img/{ticker}crho.png", f"img/{ticker}prho.png")
