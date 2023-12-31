import tkinter as tk
import logging
from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient

logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':
    # binance = BinanceFuturesClient("4038f752a4108e0b48cfb2d31e7f7c71736459b0be41c4f15d47c2861fb0af1c",
    #                                "0bb8ecc7bf707677cc8a9fae1ee32d860ecee6a8b1cc8d5fa8388a9cec5ae11a",
    #                                True)
    # print(binance.get_bid_ask('BTCUSDT'))
    #print(binance.get_contracts())
    # print(binance.get_historical_candles("BTCUSDT", "1h"))
    # print(binance.get_balances())
    # print(binance.place_oder("BTCUSDT", "BUY", 0.01, "LIMIT", 20000, "GTC"))
    # print(binance.get_order_status("BTCUSDT", 3502370794))
    # print(binance.cancel_order("BTCUSDT", "3502370794"))
    # print(binance.cancel_order("BTCUSDT", "3502371451"))

    # create root first

    bitmex = BitmexClient("",
                          "", True)

    # print(bitmex.contracts['XBTU14'].base_asset, bitmex.contracts['XBTU14'].price_decimals)
    # print(bitmex.balances['XBt'].wallet_balance)

    # print(bitmex.place_order(bitmex.contracts['XBTUSD'], "Limit", 100, "Buy", price=50000, tif="GoodTillCancel").order_id)

    # print(bitmex.get_order_status("", bitmex.contracts["XBTUSD"]).status)

    print(bitmex.cancel_order("").status)
    root = tk.Tk()

    root.mainloop()