# Part 1

- Idea: Refactor the `europeanMonteCarlo.py` to use 
`np.beta(14,6) - 0.65` instead of the Brownian Motion.
- Instead of 100 paths, do 5000.
- Change Volatility and drift


# Part 2

- After fitting the data to all distributions (using `get_distributions()`), the results were as follows:
- For stock 1, an f distribution did the best, with a sum square error of 0.029197
    - Best 5: f, levy_stable, chi, geninvgauss, powernorm
- For stock 2, an alpha distribution fit best, with a sum square error of 0.022781
    - Best 5: alpha, genhyperbolic, chi2, invgamma, skewnorm
- From the common distributions, the lognormal distribution fits both datasets best, with a sum square error of 0.029207 and 0.022877 respectively
- For simplicity, we will use the lognormal distribution as the fit distribution