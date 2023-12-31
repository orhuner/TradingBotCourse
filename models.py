
BITMEX_MULTIPLIER = 0.00000001


class Balance:
    def __init__(self, info, exchange):
        if exchange == 'binance':
            self.initial_margin = float(info['initialMargin'])
            self.maintenance_margin = float(info['maintMargin'])
            self.margin_balance = float(info['marginBalance'])
            self.wallet_balance = float(info['walletBalance'])
            self.unrealized_pnl = float(info['unrealizedProfit'])
        elif exchange == 'bitmex':
            self.initial_margin = info['initMargin'] * BITMEX_MULTIPLIER
            self.maintenance_margin = info['maintMargin'] * BITMEX_MULTIPLIER
            self.margin_balance = info['marginBalance'] * BITMEX_MULTIPLIER
            self.wallet_balance = info['walletBalance'] * BITMEX_MULTIPLIER
            self.unrealized_pnl = info['unrealisedPnl'] * BITMEX_MULTIPLIER


class Candle:
    def __init__(self, candles_info, exchange):
        if exchange == "binance":
            self.timestamp = candles_info[0]
            self.open = float(candles_info[1])
            self.high = float(candles_info[2])
            self.low = float(candles_info[3])
            self.close = float(candles_info[4])
            self.volume = float(candles_info[5])
        elif exchange == "bitmex":
            self.timestamp = candles_info["timestamp"]
            self.open = candles_info["open"]
            self.high = candles_info["high"]
            self.low = candles_info["low"]
            self.close = candles_info["close"]
            self.volume = candles_info["volume"]


class Contract:
    def __init__(self, contract_info, exchange):
        if exchange == "binance":
            self.symbol = contract_info['symbol']
            self.base_asset = contract_info['baseAsset']
            self.quote_asset = contract_info['quoteAsset']
            self.price_decimals = contract_info['pricePrecision']
            self.quantity_decimal = contract_info['quantityPrecision']
        elif exchange == "bitmex":
            self.symbol = contract_info["symbol"]
            self.base_asset = contract_info['rootSymbol']
            self.quote_asset = contract_info['quoteCurrency']
            self.price_decimals = contract_info['tickSize']
            self.quantity_decimal = contract_info['lotSize']


class OrderStatus:
    def __init__(self, order_info, exchange):
        if exchange == "binance":
            self.order_id = order_info['orderId']
            self.status = order_info['status']
            self.avg_price = float(order_info['avgPrice'])
        elif exchange == "bitmex":
            self.order_id = order_info['orderID']
            self.status = order_info['ordStatus']
            self.avg_price = order_info['avgPx']
