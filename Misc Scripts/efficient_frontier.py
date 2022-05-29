# Author: Atheesh Krishnan

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

axis = pd.read_csv('D:/DS/AXISBANK.csv')
cipla = pd.read_csv('D:/DS/CIPLA.csv')
fortis = pd.read_csv('D:/DS/FORTIS.csv')
jet = pd.read_csv('D:/DS/JETAIRWAYS.csv')
titan = pd.read_csv('D:/DS/TITAN.csv')
axis = axis.rename(index = str, columns={"Close Price": "axis_cp"})
cipla = cipla.rename(index = str, columns={"Close Price": "cipla_cp"})
fortis = fortis.rename(index = str, columns={"Close Price": "fortis_cp"})
jet = jet.rename(index = str, columns={"Close Price": "jet_cp"})
titan = titan.rename(index = str, columns={"Close Price": "titan_cp"})

# create new df with close prices for all 5 stocks
portfolio = pd.DataFrame(axis.axis_cp)
cipla, portfolio = [d.reset_index(drop=True) for d in (cipla, portfolio)]
portfolio = portfolio.join(cipla['cipla_cp'])
fortis, portfolio = [d.reset_index(drop=True) for d in (fortis, portfolio)]
portfolio = portfolio.join(fortis['fortis_cp'])
jet, portfolio = [d.reset_index(drop=True) for d in (jet, portfolio)]
portfolio = portfolio.join(jet['jet_cp'])
titan, portfolio = [d.reset_index(drop=True) for d in (titan, portfolio)]
portfolio = portfolio.join(titan['titan_cp'])

# create the correlation matrix
corr_matrix = np.corrcoef(portfolio)

#convert daily stock prices into daily returns
returns = portfolio.pct_change()

#calculate mean daily return and covariance of daily returns
mean_daily_returns = returns.mean()
cov_matrix = returns.cov()
volatility = returns.std()

#set number of runs of random portfolio weights
num_portfolios = 50000
stock = ['Axis', 'Cipla', 'Fortis', 'Jet', 'Titan']

#increased the size of the array to hold the weight values for each stock
results = np.zeros((4+len(stock)-1,num_portfolios))

for i in range(num_portfolios):
    #select random weights for portfolio holdings
    w = np.array(np.random.random(5))
    #rebalance weights to sum to 1, so that total portfolio alloc stays within 100%
    w /= np.sum(w)
    portfolio_return = np.sum(mean_daily_returns * w) * 252
    portfolio_vol = np.sqrt(np.dot(w.T,np.dot(cov_matrix, w))) * np.sqrt(252)
    results[0,i] = portfolio_return
    results[1,i] = portfolio_vol
    #portfolio_sharpe = portfolio_return / portfolio_vol 
    results[2,i] = results[0,i]/results[1,i]
    #iterate through the weight vector and add data to results array
    for j in range(len(w)):
        results[j+3,i] = w[j]

result_frame = pd.DataFrame(results.T,columns=['ret','stdev','sharpe',stock[0],stock[1],stock[2],stock[3],stock[4]])

#locate position of portfolio with highest Sharpe Ratio
max_sharpe_port = result_frame.iloc[result_frame['sharpe'].idxmax()]
#locate positon of portfolio with minimum standard deviation
min_vol_port = result_frame.iloc[result_frame['stdev'].idxmin()]

stdev = np.asarray(result_frame.stdev)
ret = np.asarray(result_frame.ret)
sharpe = np.asarray(result_frame.sharpe)

# plotting the efficient frontier
plt.xlabel('Volatility')
plt.ylabel('Returns')
plt.title('Efficient Frontier')
plt.scatter(stdev, ret,c =sharpe,cmap='viridis')
plt.colorbar()
plt.scatter(max_sharpe_port[1],max_sharpe_port[0],marker=(5,1,0),color='r',s=1000)
plt.scatter(min_vol_port[1],min_vol_port[0],marker=(5,1,0),color='g',s=1000)
print(plt.plot())

# percentage allocation
print('Portfolio Allocation for Minimum Volatility: ')
print(min_vol_port)
print('Portfolio Alocation for Maximum Sharpe Ratio: ')
print(max_sharpe_port)
