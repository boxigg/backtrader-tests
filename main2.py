import ccxt
import time

from binance.client import Client

client = Client("api-key", "api-secret", {"verify": False, "timeout": 20})


from binance.websockets import BinanceSocketManager

info = client.get_exchange_info()

print(info)

def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something

# bm = BinanceSocketManager(client)

from binance.websockets import BinanceSocketManager

bm = BinanceSocketManager(client)


conn_key = bm.start_trade_socket('BTCUSDT', process_message)
bm.start()

