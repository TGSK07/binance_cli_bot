ALLOWED_ACTIONS = {"BUY", "SELL"}
ALLOWED_ORDER_TYPES = {"MARKET", "LIMIT"}



def validate_symbol(symbol):
    """
    Validate and normalize trading symbol.
    
    Raises:
        ValueError: If symbol format is invalid.
    """

    if not symbol.upper().endswith("USDT"):
        raise ValueError("Symbol must end with USDT (e.g. BITCUSDT)")
    return symbol.upper()

def validate_action(action):
    """
    Docstring for validate_action
    
    :param action: Description
    """

    if action.upper() not in ALLOWED_ACTIONS:
        raise ValueError("Action must be BUY or SELL")

    return action.upper() 

def validate_order_type(order):
    """
    Docstring for validate_order_type
    
    :param order: Description
    """

    if not order:
        raise ValueError("Order type is mandatory.")
    
    if order.upper() not in ALLOWED_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT")
    
    return order
    
def validate_quantity(qty):
    """
    Docstring for validate_quantity
    
    :param qty: Description
    """
    if qty <= 0:
        raise ValueError("Quantity must be greater than 0.")
    return qty

def validate_price(price, order_type):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
    
        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        return price
    return price

def validate_order_input(args):
    """
    Docstring for validate_order_input
    
    :param args: Description
    """
    r = {
        "symbol": validate_symbol(args.sym),
        "side": validate_action(args.s),
        "order_type": validate_order_type(args.ot),
        "qty": validate_quantity(args.qty),
        "price": validate_price(args.p, args.ot.upper())
    }
    print(r)
    return r
