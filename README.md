# Running the Code

- To run Part 1, type `python part1.py`
    - This will output the average payoff for a block of 100 options
    - It will also create a graph of the price paths for the stock
- To run Part 2, type `python part2.py`
    - This will fit stock1.csv and stock2.csv to distributions
        - It will then plot the distributions against the histograms for stock 1 and stock 2
    - The program will then output the average payoff for 100 options when the value of each option is calculated by outperforming the average value of the distributions.
    - The program does the same for outperforming the max value of the distributions. 


# Part 1

## Idea
- Refactor the `europeanMonteCarlo.py` to use 
`np.beta(14,6) - 0.65` instead of the Brownian Motion.
- Instead of 100 paths, do 5000.
- Change Volatility and drift

## Results

- The ideal price of the option is approximately $900 (for a block of 100 options). 

# Part 2

- After fitting the data to all distributions (using `get_distributions()`), the results were as follows:
- For stock 1, an f distribution did the best, with a sum square error of 0.029197
    - Best 5: f, levy_stable, chi, geninvgauss, powernorm
- For stock 2, an alpha distribution fit best, with a sum square error of 0.022781
    - Best 5: alpha, genhyperbolic, chi2, invgamma, skewnorm
- From the common distributions, the lognormal distribution fits both datasets best, with a sum square error of 0.029207 and 0.022877 respectively
- For simplicity, we will use the lognormal distribution as the fit distribution to calculate option value

## Idea

- Fit the stock data to its best distribution
    - f distribution for stock 1, alpha distribution for stock 2
    - Each stock gets its own distribution (2 total)
- Pull down 365 values from each distribution as the estimated prices for each stock
- For outperforming the average of the two stocks:
    - If the value of the option at expiry is greater than the average value of the two stocks AT EXPIRY (last element in price list), then the payoff is option_price - average(stock1_expiry_price, stock2_expiry_price)
    - Else, the payoff of the option is 0
- For outperforming the max of the two stocks:
    - If the value of the option at expiry is greater than the max value of the two stocks AT EXPIRY (last element in price list), then the payoff is option_price - max(stock1_expiry_price, stock2_expiry_price)
    - Else, the payoff of the option is 0

## Results

Results according to distributions fit for stocks 1 and 2:

- The average payoff has a large volatility, varying between about $500 and $1500 when computed using the average value and varying from about $200 to $1200 when computed using the max value. This is because the payoff of the option all depends on the random draws obtained for the stock prices at expiry