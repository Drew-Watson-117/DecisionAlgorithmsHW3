from stock_simulations import *

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Fitting
bestDist1 = fitStock("stock1.csv")["f"]
bestDist2 = fitStock("stock2.csv")["alpha"]


def stock_price(dist, stock):
    if stock == "stock1":
        return stats.f.rvs(dfn=dist["dfn"], dfd=dist["dfd"], loc=dist["loc"], scale=dist["scale"])
        # return dist["scale"]*np.random.lognormal(sigma=dist["s"]) + dist["loc"]
    else:
        # Alpha distribution
        return stats.alpha.rvs(a=dist["a"], loc=dist["loc"], scale=dist["scale"])

# Model Parameters
paths = 5000 #iterations?
initial_price = 100
drift = -0.01
volatility = 0.5
dt = 1/365
T = 1
price_paths = []

# Estimate Future Stock Prices
stock1_prices = []
stock2_prices = []
Time = T
while Time - dt > 0:
    stock1_prices.append(stock_price(bestDist1, "stock1"))
    stock2_prices.append(stock_price(bestDist2, "stock2"))
    Time -= dt

# Generate a set of sample paths
for i in range(0, paths):
    price_paths.append(BetaMotion(initial_price, drift, volatility, dt, T).prices)
    
    
call_payoffs_average = []
call_payoffs_max = []
# Compare option value to estimated prices for stocks 1 and 2
cp = Comparative_Payoff_2(stock1_prices, stock2_prices)
risk_free_rate = .01
max_price = 0.0
for price_path in price_paths:
    if price_path[-1] > max_price:
        max_price = price_path[-1]
    call_payoffs_average.append(cp.get_payoff_average(price_path[-1])/(1 + risk_free_rate))  # We get the last stock price in the series generated by Beta Distribution to determine the payoff and discount it by one year
    call_payoffs_max.append(cp.get_payoff_max(price_path[-1])/(1 + risk_free_rate))
# Plot the set of generated sample paths
for price_path in price_paths:
    plt.plot(price_path)
plt.show()

average_payoff_1 = round(np.average(call_payoffs_average)*100, 2)
average_payoff_2 = round(np.average(call_payoffs_max)*100, 2)
print(f"Average payoff for 100 options based on average value of Stock 1 and Stock 2:\n ${average_payoff_1}")  # Options are in blocks of 100
print(f"Average payoff for 100 options based on max value of Stock 1 and Stock 2:\n ${average_payoff_2}")  # Options are in blocks of 100