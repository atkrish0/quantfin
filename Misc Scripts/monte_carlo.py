# Author: Atheesh Krishnan
# Monte Carlo Simulation of European Call Options using the Black-Scholes-Merton Model

# standard library imports
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# initialization of parameters
S0 = 100 #initial index level
K = 105 #strike price
T = 1.0 #time-to-maturity
r = 0.05 #risk free short rate
sigma = 0.2 #volatility
M = 50
dt = T/M
I = 10000 #numer of simulations

# valuation algorithm
S = np.zeros((M + 1, I))
S[0] = S0

for t in range(1, M + 1):    
    # pseudorandom numbers
    z = np.random.standard_normal(I)      
    S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt+ sigma * np.sqrt(dt) * z)

# monte carlo estimator
C0 = np.exp(-r * T) * np.sum(np.maximum(S[-1] - K, 0)) / I 

print("Value of the European Call Option %5.3f" % C0)

plt.plot(S[:, :10])
plt.grid(True)
plt.xlabel('Time Step')
plt.ylabel('Index Level')

sns.distplot(S[-1], bins=50)
plt.grid(True)
plt.xlabel('Index level')
plt.ylabel('Frequency')


