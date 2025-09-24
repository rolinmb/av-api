from consts import *
import requests
import csv

class AlphaVantageAPI:
    def __init__(self, avkey):
        self.avkey = avkey
    
    def getDailyEquities(self, ticker, csvname):
        url = f"{BASEURL}{EQUITIES}&symbol={ticker.upper()}&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        ts = data.get("Time Series (Daily)")
        if not ts:
            print("src/api.py :: No equity time series data found.")
            return
        
        sorted_dates = sorted(ts.keys())
        with open(csvname, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Open", "High", "Low", "Close", "Volume"])
            for date in sorted_dates:
                day = ts[date]
                writer.writerow([
                    date,
                    day["1. open"],
                    day["2. high"],
                    day["3. low"],
                    day["4. close"],
                    day["5. volume"]
                ])
        
        print(f"src/api.py :: {csvname} saved successfully")

    
    def getCurrentOptionChain(self, ticker, csvname):
        url = f"{BASEURL}{OPTIONS}&symbol={ticker.upper()}&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        self._writeOptionCSV(data, csvname)

    def getHistoricalOptionChain(self, ticker, csvname, date=""):
        if date == "":
            self.getCurrentOptionChain(ticker, csvname)
        else:
            url = f"{BASEURL}{OPTIONS}&symbol={ticker.upper()}&date={date}&apikey={self.avkey}"
            response = requests.get(url)
            data = response.json()
            self._writeOptionCSV(data, csvname)

    def _writeOptionCSV(self, data, csvname):
        options = data.get("data")
        if not options:
            print("src/api.py :: No options data found")
            return
        # Define columns to include in CSV
        columns = [
            "contractID", "symbol", "expiration", "strike", "type",
            "last", "mark", "bid", "bid_size", "ask", "ask_size",
            "volume", "open_interest", "date", "implied_volatility",
            "delta", "gamma", "theta", "vega", "rho"
        ]

        with open(csvname, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            for row in options:
                # Only keep keys that exist in columns
                writer.writerow({k: row.get(k, "") for k in columns})

        print(f"src/api.py :: {csvname} saved successfully!")

    def getDailyForex(self, cfrom, cto, csvname):
        url = f"{BASEURL}{FOREX}&from_symbol={cfrom.upper()}&to_symbol={cto.upper()}&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        ts = data.get("Time Series FX (Daily)")
        if not ts:
            print("src/api.py :: No forex time series data found.")
            return
        
        sorted_dates = sorted(ts.keys())
        with open(csvname, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Open", "High", "Low", "Close", "Volume"])
            for date in sorted_dates:
                day = ts[date]
                writer.writerow([
                    date,
                    day["1. open"],
                    day["2. high"],
                    day["3. low"],
                    day["4. close"],
                    day["5. volume"]
                ])
        
        print(f"src/api.py :: {csvname} saved successfully")

    def getDailyCrypto(self, symbol, csvname):
        url = f"{BASEURL}{CRYPTO}&symbol={symbol.upper()}&market=USD&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        ts = data.get("Time Series (Digital Currency Daily)")
        if not ts:
            print("src/api.py :: No crypto time series data found.")
            return
        
        sorted_dates = sorted(ts.keys())
        with open(csvname, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Open", "High", "Low", "Close", "Volume"])
            for date in sorted_dates:
                day = ts[date]
                writer.writerow([
                    date,
                    day["1. open"],
                    day["2. high"],
                    day["3. low"],
                    day["4. close"],
                    day["5. volume"]
                ])
        
        print(f"src/api.py :: {csvname} saved successfully")

    def _writeOtherCsv(self, data, csvname):
        series_data = data.get("data")
        if not series_data:
            print("No bond data found")
            return
        # Sort by date ascending
        series_data.sort(key=lambda x: x["date"])

        with open(csvname, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Value"])
            for row in series_data:
                writer.writerow([row["date"], row["value"]])

        print(f"src/api.py :: {csvname} saved successfully!")

    def getDailyBonds(self, maturity, csvname):
        url = f"{BASEURL}{BONDS}&interval=daily&maturity={maturity}&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        self._writeOtherCSV(data, csvname)

    def getDailyWti(self, csvname):
        url = f"{BASEURL}{WTI}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        self._writeOtherCSV(data, csvname)

    def getDailyBrent(self, csvname):
        url = f"{BASEURL}{BRENT}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        self._writeOtherCSV(data, csvname)

    def getDailyNatgas(self, csvname):
        url = f"{BASEURL}{NATGAS}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        self._writeOtherCSV(data, csvname)

    def getDailyCopper(self, csvname):
        url = f"{BASEURL}{COPPER}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        self._writeOtherCSV(data, csvname)

    def getDailyAluminum(self, csvname):
        url = f"{BASEURL}{ALUMINUM}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        self._writeOtherCSV(data, csvname)

    def getDailyWheat(self, csvname):
        url = f"{BASEURL}{WHEAT}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        self._writeOtherCSV(data, csvname)

    def getDailyCorn(self, csvname):
        url = f"{BASEURL}{CORN}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        self._writeOtherCSV(data, csvname)

    def getDailyCotton(self, csvname):
        url = f"{BASEURL}{COTTON}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        self._writeOtherCSV(data, csvname)

    def getDailySugar(self, csvname):
        url = f"{BASEURL}{SUGAR}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        self._writeOtherCSV(data, csvname)

    def getDailyGci(self, csvname):
        url = f"{BASEURL}{GCI}&interval=daily&apikey={self.avkey}"
        response = requests.get(url)
        data = response.json()
        self._writeOtherCSV(data, csvname)
