# Atheesh Krishnan
# Date: 20th Aug, 2019
# Cox-Ingersoll-Ross Model

import numpy as np
import matplotlib.pyplot as plt

def cir(r0, K, theta, sigma, T=1., N=10,seed=777):
    np.random.seed(seed)
    dt = T/float(N)    
    rates = [r0]
    for i in range(N):
        dr = K*(theta-rates[-1])*dt + \
            sigma*np.sqrt(rates[-1])*np.random.normal()
        rates.append(rates[-1] + dr)
    return range(i+1), rates

if __name__ == "__main__":
    x, y = cir(0.01875, 0.20, 0.01, 0.012, 10., 200)

    
    plt.plot(x,y)
    plt.show()