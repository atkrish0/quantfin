from pandas_datareader import data as web
import datetime


start1 = datetime.datetime(2016, 9, 21)
end1 = datetime.datetime(2016, 9, 21)
start2 = datetime.datetime(2016, 9, 22)
end2 = datetime.datetime(2016, 9, 22)

SPY = web.DataReader("SPY", 'yahoo', start1, end1)
VIX = web.DataReader("VIX",'yahoo', start1, end1)


SPY['Time of Download'] = datetime.datetime.time(datetime.datetime.now())
print(SPY)

path = ''
SPY.to_csv(path+'DATA1.csv')
VIX.to_csv(path+'DATA1a.csv')
