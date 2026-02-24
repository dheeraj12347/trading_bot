import argparse
import sys
from bot.client import BinanceTestnetClient
from bot.orders import OrderManager
from bot.validators import validate_order_input
from bot.logging_config import setup_logging

def main():
    # 1. Setup Logging
    setup_logging()
    
    # 2. Setup Command Line Arguments
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol", type=str, required=True, help="e.g., BTCUSDT")
    parser.add_argument("--side", type=str, choices=['BUY', 'SELL'], required=True)
    parser.add_argument("--type", type=str, choices=['MARKET', 'LIMIT'], required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    # 3. Validate Input
    is_valid, error_msg = validate_order_input(args.symbol, args.side, args.type, args.qty, args.price)
    if not is_valid:
        print(f"Validation Error: {error_msg}")
        sys.exit(1)

    # 4. Execute Order
    try:
        client_wrapper = BinanceTestnetClient()
        manager = OrderManager(client_wrapper.get_client())
        
        print(f"Sending {args.type} {args.side} order for {args.symbol}...")
        
        response = manager.place_futures_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.qty,
            price=args.price
        )

        print("\n✅ ORDER PLACED SUCCESSFULLY")
        print(f"Order ID: {response['orderId']}")
        print(f"Status: {response['status']}")
        print(f"Average Price: {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        print(f"\n❌ ORDER FAILED")
        print(f"Reason: {e}")

if __name__ == "__main__":
    main()