# Quant-Finance
A repository intended to implement and experiment with various concepts within quantitative finance, including but not limited to, Interest Rate Modeling, Stochastic Processes, Time Series Analysis, Asset Allocation, Statistical Arbitrage and Derivatives Pricing.


## Contents:

* Monte Carlo Simulation: Monte Carlo simulations are used to model the probability of different outcomes in a process that cannot easily be predicted due to the intervention of random variables. It is a technique used to understand the impact of risk and uncertainty in prediction and forecasting models.

* Efficient Frontier: Optimal portfolio allocation of a bucket of 5 Indian Mid Cap and Large Cap Equities based on the Efficient Frontier concept. Best allocation percentages were derived for maximum Sharpe Ratio and minimum Standard Deviation portfolios.

* A basic implementation of Generalized Autoregressive Conditional Heteroscedastic modelling.

Interest Rate Modeling:

* Vasicek Model: The model describes the movement of an interest rate as a factor composed of market risk, time, and equilibrium value, where the rate tends to revert towards the mean of those factors over time. Essentially, it predicts where interest rates will end up at the end of a given period of time, given current market volatility, the long-run mean interest rate value, and a given market risk factor.

* Cox-Ingersoll-Ross: The CIR model describes the evolution of interest rates. It is a type of "one factor model" (short rate model) as it describes interest rate movements as driven by only one source of market risk. The model can be used in the valuation of interest rate derivatives as an extensoin of the Vasice Model.

* Ho-Lee: A short rate model widely used in the pricing of bond options, swaptions and other interest rate derivatives, and in modeling future interest rates. Market price calibration and the subsequent valuation of bond options, swaptions and other interest rate derivatives, is typically performed via a binomial lattice based model. This model does allow the generation of negative rates and is alos not mean reverting. Hence, models like Hull-White have come up which are mean reverting with availabel lognormal variants.

* Hull-White: In its most generic formulation, the Hull-White belongs to the class of no-arbitrage models that are able to fit today's term structure of interest rates. It is relatively straightforward to translate the mathematical description of the evolution of future interest rates onto a tree or lattice and so interest rate derivatives such as bermudan swaptions can be valued in the model. 
