from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from binance.enums import *

class BinanceFuturesClient:
    """
    Wrapper around python-binance client
    for Binance Futures (USDT-M) operations.
    """

    def __init__(self, API_KEY, SECRET_KEY, logger):
        """
        Initialize Binance Futures client.
        """
        self.logger = logger
        self.client = Client(API_KEY, SECRET_KEY, testnet=True)
        

    def place_market_order(self, symbol, side, qty):
        """
        Place a MARKET order on Binance Futures.

        Returns:
            dict: Binance order response.
        """

        try:
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

        except Exception as e:
            self.logger.error(f"Error: {e}")
            raise
    
    def place_limit_order(self, symbol, side, qty, price):
        """
        Place a LIMIT order on Binance Futures.

        Returns:
            dict: Binance order response.
        """
            
        try:
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
            self.logger.error(f"Binance error: {e}")
            raise

        except Exception as e:
            self.logger.error(f"Error: {e}")
            raise