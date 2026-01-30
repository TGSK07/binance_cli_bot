from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

class BinanceFuturesClient:

    def __init__(self, API_KEY, SECRET_KEY, BASE_URL, logger):
        self.logger = logger
        self.client = Client(API_KEY, SECRET_KEY)
        self.client.FUTURES_URL = BASE_URL

    def place_market_order(self, symbol, action, qty):
        try:
            self.logger.info(f"Placing MARKET {action} order: {symbol}, quantity={qty}")
            res = self.client.futures_create_order(
                symbol=symbol,
                side=action,
                type="MARKET",
                quantity=qty
            )
            self.logger.info(f"Order response: {res}")
            return res
        
        except (BinanceAPIException, BinanceRequestException) as e:
            self.logger.error(f"Binance error: {e}")
            raise
    
    def place_limit_order(self, symbol, action, qty, price):
        try:
            self.logger.info(f"PLacing LIMIT {action}: {symbol}, quantity={qty}, price={price}")
            res = self.client.futures_create_order(
                symbol=symbol,
                side=action,
                type="LIMIT",
                quantity=qty
            )
            self.logger.info(f"Order response: {res}")
            return res
        
        except (BinanceAPIException, BinanceRequestException) as e:
            self.logger.error(f"Bianance error: {e}")
            raise
    
    