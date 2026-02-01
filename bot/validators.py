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
    Validate order side (BUY or SELL).

    Raises:
        ValueError: If side is invalid.
    """

    if action.upper() not in ALLOWED_ACTIONS:
        raise ValueError("Action must be BUY or SELL")

    return action.upper() 

def validate_order_type(order):
    """
    Validate order type (MARKET or LIMIT).

    Raises:
        ValueError: If order type is invalid.
    """

    if not order:
        raise ValueError("Order type is mandatory.")
    
    if order.upper() not in ALLOWED_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT")
    
    return order
    
def validate_quantity(qty):
    """
    Validate order quantity.

    Raises:
        ValueError: If quantity is non-positive.
    """

    if qty <= 0:
        raise ValueError("Quantity must be greater than 0.")
    return qty

def validate_price(price, order_type):
    """
    Validate price for LIMIT orders.

    Raises:
        ValueError: If price is missing or invalid.
    """
    
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
    
        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        return price
    return price

def validate_order_input(args):
    """
    Validate and aggregate all CLI inputs
    into a normalized order payload.

    Returns:
        dict: Validated order parameters.
    """
    return {
        "symbol": validate_symbol(args.sym),
        "side": validate_action(args.s),
        "order_type": validate_order_type(args.ot),
        "qty": validate_quantity(args.qty),
        "price": validate_price(args.p, args.ot.upper())
        }