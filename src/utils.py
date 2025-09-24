import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np

def createSeriesChart(csvname, pngname):
    if not os.path.exists(csvname):
        print(f"src/utils.py :: Could not find {csvname}")
        return

    if "chain" in csvname:
        print(f"src/util.py :: Cannot create time series chart from option chain csv {csvname}")
        return
    
    series_df = pd.read_csv(csvname, parse_dates=["Date"])
    print(series_df.head())
    plt.figure(figsize=(10, 5))
    if "Close" in series_df.columns: # We have [O,H,L,C,V] Data
        plt.plot(series_df["Date"], series_df["Close"], label="Close", color="blue")
        plt.title(csvname)
        plt.ylabel("Close Price")
    elif "Value" in series_df.columns: # We have simpler [Date, Value] Data
        plt.plot(series_df["Date"], series_df["Value"], label="Value", color="green")
        plt.title(csvname)
        plt.ylabel("Price")
    else:
        print("src/utils.py :: CSV format not recognized for charting")
        return
        
    plt.xlabel("Date")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(pngname, dpi=150)
    plt.close()
    print(f"src/utils.py :: {pngname} chart saved successfully")

def _plotSurface(data, title, pngname):
    if data.empty:
        print(f"src/utils.py :: No data available for {title}")
        return
    
    surface = data.pivot_table(index="strike", columns="days_to_exp", values="implied_volatility")
    X, Y = np.meshgrid(surface.columns, surface.index)
    Z = surface.values

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")
    surf = ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none", alpha=0.9)

    ax.set_title(title)
    ax.set_xlabel("Days to Expiration")
    ax.set_ylabel("Strike")
    ax.set_zlabel("Implied Volatility")
    fig.colorbar(surf, shrink=0.5, aspect=10, label="IV")

    plt.tight_layout()
    plt.savefig(pngname, dpi=150)
    plt.close()
    print(f"src/utils.py :: {pngname} surface saved successfully")

def createOptionSurface(csvname, pngnamec, pngnamep):
    if not os.path.exists(csvname):
        print(f"src/utils.py :: Could not find {csvname}")
        return
    
    if "daily" in csvname or "weekly" in csvname or "monthly" in csvname:
        print(f"src/utils.py :: Cannot create options surface from time series csv {csvname}")
        return
    
    chain_df = pd.read_csv(csvname, parse_dates=["expiration"])
    chain_df["implied_volatility"] = pd.to_numeric(chain_df["implied_volatility"], errors="coerce")
    chain_df = chain_df.dropna(subset=["implied_volatility", "strike", "expiration", "type"])

    min_exp = chain_df["expiration"].min()
    chain_df["days_to_exp"] = (chain_df["expiration"] - min_exp).dt.days

    calls = chain_df[chain_df["type"].str.lower() == "call"]
    puts = chain_df[chain_df["type"].str.lower() == "put"]

    _plotSurface(calls, "Call Option Implied Vol Surface", pngnamec)
    _plotSurface(puts, "Put Option Implied Vol Surface", pngnamep)