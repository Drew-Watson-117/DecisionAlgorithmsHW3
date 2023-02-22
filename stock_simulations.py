import numpy as np
import pandas as pd
from fitter import Fitter
import matplotlib.pyplot as plt


class European_Call_Payoff:

    def __init__(self, strike):
        self.strike = strike

    def get_payoff(self, stock_price):
        if stock_price > self.strike:
            return stock_price - self.strike
        else:
            return 0

class Comparative_Payoff:

    def __init__(self, payoff1, payoff2):
        self.values = np.union1d(payoff1,payoff2)

    def get_payoff_average(self, stock_price):
        comparisonValue = np.average(self.values)
        if stock_price > comparisonValue:
            return stock_price - comparisonValue
        else:
            return 0

    def get_payoff_max(self, stock_price):
        comparisonValue = np.max(self.values)
        if stock_price > comparisonValue:
            return stock_price - comparisonValue
        else:
            return 0

class Comparative_Payoff_2:

    def __init__(self, payoff1, payoff2):
        self.payoff1 = payoff1
        self.payoff2 = payoff2
        self.N = len(self.payoff1)

    def get_payoff_average(self, stock_price):
        comparisonValue = np.average([self.payoff1[self.N-1], self.payoff2[self.N-1]])
        if stock_price > comparisonValue:
            return stock_price - comparisonValue
        else:
            return 0

    def get_payoff_max(self, stock_price):
        comparisonValue = np.max([self.payoff1[self.N-1], self.payoff2[self.N-1]])
        if stock_price > comparisonValue:
            return stock_price - comparisonValue
        else:
            return 0


class BetaMotion:

    def simulate_paths(self):
        while(self.T - self.dt > 0):
            dWt = np.random.beta(14, 6) - 0.65 # Beta Motion
            dYt = self.drift*self.dt + self.volatility*dWt  # Change in price
            self.current_price += dYt  # Add the change to the current price
            self.prices.append(self.current_price)  # Append new price to series
            self.T -= self.dt  # Account for the step in time

    def __init__(self, initial_price, drift, volatility, dt, T):
        self.current_price = initial_price
        self.initial_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.simulate_paths()

def fitStock(fileName):
    stock = pd.read_csv(fileName, names=["Data"])
    f = Fitter(stock, distributions=["f", "alpha", "gamma", "burr", "norm", "beta","lognorm"])
    f.fit()
    print(f.summary())
    bestDistribution = f.get_best(method = 'sumsquare_error')
    print(bestDistribution)
    
    plt.show()
    return bestDistribution