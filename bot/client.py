from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from binance.enums import *

class BinanceFuturesClient:

    def __init__(self, API_KEY, SECRET_KEY, logger):
        self.logger = logger
        self.client = Client(API_KEY, SECRET_KEY)
        

    def place_market_order(self, symbol, side, qty):
        try:
            print("MARKET ORDER")
            self.logger.info(f"Placing MARKET {side} order: {symbol}, quantity={qty}")
    
            if side == "BUY":
                order = self.client.order_market_buy(
                    symbol=symbol,
                    quantity=qty
                )
            else:
                order = self.client.order_market_sell(
                    symbol=symbol,
                    quantity=qty
                )
            self.logger.info(f"Order response: {order}")
            if not order:
                raise RuntimeError(
                    "Empty response from Binance. Order was not accepted."
                )
            return order
        
        except (BinanceAPIException, BinanceRequestException) as e:
            self.logger.error(f"Binance error: {e}")
            raise
    
    def place_limit_order(self, symbol, side, qty, price):
        try:
            print("LIMIT ORDER")
            self.logger.info(f"PLacing LIMIT {side}: {symbol}, quantity={qty}, price={price}")
            
            if side == "BUY":
                order = self.client.order_limit_buy(
                    symbol=symbol,
                    quantity=qty,
                    price=price
                )
            else:
                order = self.client.order_limit_sell(
                    symbol=symbol,
                    quantity=qty,
                    price=price
                )
            self.logger.info(f"Order response: {order}")
            if not order:
                raise RuntimeError(
                    "Empty response from Binance. Order was not accepted."
                )
            return order
        
        except (BinanceAPIException, BinanceRequestException) as e:
            self.logger.error(f"Bianance error: {e}")
            raise
    
    def place_oco_order(self, symbol, side, qty, price, sp):
        try:
            self.logger.info(f"Placing OCO {side}: {symbol}, quantity={qty}, price={price}")

            order = self.client.create_oco_order(
                    symbol='BNBBTC',
                    side=SIDE_SELL if side=='SELL' else SIDE_BUY,
                    stopLimitTimeInForce=TIME_IN_FORCE_GTC,
                    quantity=100,
                    stopPrice=sp,
                    price=price
                )

        except (BinanceAPIException, BinanceRequestException) as e:
            self.logger.error(f"Binance error: {e}")