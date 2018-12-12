import backtrader as bt
from datetime import datetime, timedelta
from pprint import pprint

class firstStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.indicators.RSI_SMA(self.data.close, period=14)

    def next(self):
        # if not self.position:
        if self.rsi < 30:
            self.buy(size=0.2)
            print(self.position)
            # print(self.cash)

        # else:
        if self.rsi > 70:
            self.sell(size=0.2)
            print(self.position)


#Variable for our starting cash
startcash = 1000

#Create an instance of cerebro
cerebro = bt.Cerebro()

#Add our strategy
cerebro.addstrategy(firstStrategy)

#Get Apple data from Yahoo Finance.
# data = bt.feeds.Quandl(
#     dataname='AAPL',
#     fromdate = datetime(2016,1,1),
#     todate = datetime(2017,1,1),
#     buffered= True
#     )

hist_start_date = datetime.utcnow() - timedelta(days=1)
hist_end_date = datetime.utcnow() - timedelta(days=0)

data = bt.feeds.CCXT(exchange='bitmex', symbol='BTC/USD',
                     timeframe=bt.TimeFrame.Minutes, fromdate=hist_start_date, todate=hist_end_date, ohlcv_limit=500)

#Add the data to Cerebro
cerebro.adddata(data)

# Set our desired cash start
cerebro.broker.setcash(startcash)

# Run over everything
cerebro.run()

#Get final portfolio Value
portvalue = cerebro.broker.getvalue()
pnl = portvalue - startcash

#Print out the final result
print('Final Portfolio Value: ${}'.format(portvalue))
print('P/L: ${}'.format(pnl))

#Finally plot the end results
cerebro.plot(style='candlestick')