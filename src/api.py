from consts import *
import requests

class AlphaVantageAPI:
    def __init__(self, avkey):
        self.avkey = avkey
    
    def getDailyEquities(self, ticker, csvname):
        url = f"{BASEURL}{EQUITIES}&symbol={ticker.upper()}&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()

    
    def getCurrentOptionChain(self, ticker, csvname):
        url = f"{BASEURL}{OPTIONS}&symbol={ticker.upper()}&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()


    def getHistoricalOptionChain(self, ticker, csvname, date=""):
        if date == "":
            self.getCurrentOptionChain(ticker, csvname)
        else:
            url = f"{BASEURL}{OPTIONS}&symbol={ticker.upper()}&date={date}&apikey={self.avkey}"
            response = requests.get(url)
            data = response.json()

    def getDailyForex(self, cfrom, cto, csvname):
        url = f"{BASEURL}{FOREX}&from_symbol={cfrom.upper()}&to_symbol={cto.upper()}&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()

    def getDailyCrypto(self, symbol, csvname):
        url = f"{BASEURL}{CRYPTO}&symbol={symbol.upper()}&market=USD&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()

    def getDailyBonds(self, maturity, csvname):
        url = f"{BASEURL}{BONDS}&interval=daily&maturity={maturity}&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()

    def getDailyWti(self, csvname):
        url = f"{BASEURL}{WTI}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()

    def getDailyBrent(self, csvname):
        url = f"{BASEURL}{BRENT}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()

    def getDailyNatgas(self, csvname):
        url = f"{BASEURL}{NATGAS}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()

    def getDailyCopper(self, csvname):
        url = f"{BASEURL}{COPPER}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()

    def getDailyAluminum(self, csvname):
        url = f"{BASEURL}{ALUMINUM}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()

    def getDailyWheat(self, csvname):
        url = f"{BASEURL}{WHEAT}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()

    def getDailyCorn(self, csvname):
        url = f"{BASEURL}{CORN}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()

    def getDailyCotton(self, csvname):
        url = f"{BASEURL}{COTTON}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()

    def getDailySugar(self, csvname):
        url = f"{BASEURL}{SUGAR}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()

    def getDailyGci(self, csvname):
        url = f"{BASEURL}{GCI}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
