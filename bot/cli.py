import argparse
from bot.validators import validate_order_input
from bot.client import BinanceFuturesClient


def parse_args():
    """
    Parse and return CLI arguments
    using argparse.
    """
    
    parser = argparse.ArgumentParser(description="Binance Futures CLI Bot")
    
    parser.add_argument("--sym", required=True, help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("--s", required=True, help="BUY or SELL")
    parser.add_argument("--ot", required=True, help="ORDER TYPE (e.g. MARKET OR LIMIT)")
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--p", type=float, required=False, help="Price is required for LIMIT orders.")

    return parser.parse_args()

def cli(settings, logger):
    """
    Execute CLI workflow: 
    parse input, validate, place order, and display results.
    """

    args = parse_args()

    try:
        order_data = validate_order_input(args)
        
        print("\nOrder Request Summary")
        print("-"*22)
        for k, v in order_data.items():
            if v is not None:
                print(f"{k.capitalize():12}: {v}")
        
        client = BinanceFuturesClient(
            settings["BINANCE_API_KEY"],
            settings["BINANCE_SECRET_KEY"],
            logger
        )

        if order_data["order_type"] == "MARKET":
            res = client.place_market_order(
                order_data["symbol"],
                order_data["side"],
                order_data["qty"]
            )
        
        else:
            res = client.place_limit_order(
                order_data["symbol"],
                order_data["side"],
                order_data["qty"],
                order_data["price"]
            )

        print("\nOrder Placed Successfully.")
        print(f"Order ID    : {res.get('orderId')}")
        print(f"Status      : {res.get('status')}")
        print(f"Executed Qty : {res.get('executedQty')}")
        print(f"Avg. Price  : {res.get('avgPrice', 'N/A')}")

    except Exception as e:
        logger.exception("Order placement failed.")
        print("\nOrder Failed.")
        print(f"Due to: {str(e)}")