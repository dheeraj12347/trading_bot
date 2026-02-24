def validate_order_input(symbol, side, order_type, quantity, price=None):
    """
    Returns (True, None) if valid, or (False, "Error Message") if invalid.
    """
    if not symbol.endswith("USDT"):
        return False, "Symbol must end with 'USDT' (e.g., BTCUSDT)."
    
    if side not in ['BUY', 'SELL']:
        return False, "Side must be BUY or SELL."
    
    if order_type not in ['MARKET', 'LIMIT']:
        return False, "Type must be MARKET or LIMIT."
    
    if quantity <= 0:
        return False, "Quantity must be greater than 0."
    
    if order_type == 'LIMIT' and (price is None or price <= 0):
        return False, "A valid price is required for LIMIT orders."
    
    return True, None