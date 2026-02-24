import logging

logger = logging.getLogger(__name__)

class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_futures_order(self, symbol, side, order_type, quantity, price=None):
        """
        Places an order on Binance Futures (USDT-M)
        """
        try:
            # Prepare standard parameters
            params = {
                'symbol': symbol.upper(),
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity,
            }

            # Add extra parameters for LIMIT orders
            if order_type.upper() == 'LIMIT':
                if not price:
                    raise ValueError("Price is required for LIMIT orders.")
                params['price'] = str(price)
                params['timeInForce'] = 'GTC'  # Good 'Til Canceled

            logger.info(f"Attempting {side} {order_type} order for {symbol}")
            
            # This calls the Binance Futures API
            response = self.client.futures_create_order(**params)
            
            logger.info(f"Order Successful! Order ID: {response.get('orderId')}")
            return response

        except Exception as e:
            logger.error(f"Failed to place order: {e}")
            raise e