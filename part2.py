from stock_simulations import *

import matplotlib.pyplot as plt
import numpy as np

# Fitting
bestDist1 = fitStock("stock1.csv")["lognorm"]
bestDist2 = fitStock("stock2.csv")["lognorm"]

def stock_price(dist):
    return dist["scale"]*np.random.lognormal(sigma=dist["s"]) + dist["loc"]

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
    stock1_prices.append(stock_price(bestDist1))
    stock2_prices.append(stock_price(bestDist2))
    Time -= dt

# Generate a set of sample paths
for i in range(0, paths):
    price_paths.append(BetaMotion(initial_price, drift, volatility, dt, T).prices)
    
    
call_payoffs_average = []
call_payoffs_max = []
# Compare option value to estimated prices for stocks 1 and 2
cp = Comparative_Payoff(stock1_prices, stock2_prices)
risk_free_rate = .01
for price_path in price_paths:
    call_payoffs_average.append(cp.get_payoff_average(price_path[-1])/(1 + risk_free_rate))  # We get the last stock price in the series generated by GBM to determine the payoff and discount it by one year
    call_payoffs_max.append(cp.get_payoff_max(price_path[-1])/(1 + risk_free_rate))
# Plot the set of generated sample paths
for price_path in price_paths:
    plt.plot(price_path)
plt.show()

print(f"Best Price for European Call Option based on average value of Stock 1 and Stock 2:\n{np.average(call_payoffs_average)*100}")  # Options are in blocks of 100
print(f"Best Price for European Call Option based on max value of Stock 1 and Stock 2:\n{np.average(call_payoffs_max)*100}")  # Options are in blocks of 100

