import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# simple moving average
def sma(df, periods = 20):
    df['SMA'] = df['Close'].rolling(window = periods).mean()
    return df

# exponential moving average
def ema(df, periods = 20):
    k =2/(periods + 1)
    df.loc[df.index[0], 'EMA'] = df.loc[df.index[0], 'Close']
    for index in df[:-1].index:
        df.loc[index+1, 'EMA'] = k*df.loc[index+1, 'Close']+(1-k)*df.loc[index, 'EMA']
    return df

