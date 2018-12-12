# !/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import sys
import time
from datetime import datetime, timedelta

import backtrader as bt
import ccxt

class TestStrategy(bt.Strategy):

    def start(self):
        self.counter = 0
        print('START')

    def prenext(self):
        self.counter += 1
        print('prenext len %d - counter %d' % (len(self), self.counter))

    def __init__(self):
            self.dmi = bt.indicators.DMI(self.data, period=3)

    def next(self):
        print('------ next len %d - counter %d' % (len(self), self.counter))

        print(self.dmi.plusDI[0], self.dmi.minusDI[0], self.dmi.adx[0])

        self.counter += 1

        print('*' * 5, 'NEXT:', bt.num2date(self.data0.datetime[0]), self.data0._name, self.data0.open[0], self.data0.high[0],
              self.data0.low[0], self.data0.close[0], self.data0.volume[0],
              bt.TimeFrame.getname(self.data0._timeframe), len(self.data0))

if __name__ == '__main__':
    cerebro = bt.Cerebro()

    exchange = sys.argv[1] if len(sys.argv) > 1 else 'bitmex'
    symbol = sys.argv[2] if len(sys.argv) > 2 else 'BTC/USD'

    hist_start_date = datetime.utcnow() - timedelta(minutes=10)
    data = bt.feeds.CCXT(exchange=exchange, symbol=symbol,
                         timeframe=bt.TimeFrame.Minutes, fromdate=hist_start_date, ohlcv_limit=500)

    cerebro.adddata(data)
    cerebro.addstrategy(TestStrategy)
    cerebro.run()