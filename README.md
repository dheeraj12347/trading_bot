Simplified Trading Bot (Binance Futures Testnet)
This is a Python-based Command Line Interface (CLI) application designed to place orders on the Binance Futures Testnet (USDT-M). The bot is built with a modular structure to ensure clean code, proper logging, and robust error handling.

🛠 Setup Instructions
Clone the Repository:

Bash
git clone (https://github.com/dheeraj12347/trading_bot)
cd trading_bot
Create a Virtual Environment:

Bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install Dependencies:

Bash
pip install -r requirements.txt
API Configuration:
Create a .env file in the root directory and add your Binance Testnet credentials:

Code snippet
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key
Note: Ensure you are using keys from testnet.binancefuture.com.

🚀 How to Run Examples
1. Place a Market Order
Bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.002
2. Place a Limit Order
Bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.002 --price 50000
📝 Assumptions
Minimum Notional: The bot assumes the user is aware of the Binance Testnet minimum notional requirement (currently 100 USDT for BTCUSDT).

Asset Balance: It is assumed the Testnet account has a sufficient USDT-M balance to cover the margin.

Symbol Format: Symbols must be entered in the format recognized by Binance (e.g., BTCUSDT).

📂 Project Structure
bot/client.py: Initializes the Binance client for the Testnet environment.

bot/orders.py: Contains logic for executing various order types.

bot/validators.py: Validates user input before sending API requests.

bot/logging_config.py: Configures structured logging to logs/app.log.

cli.py: The entry point for the application using argparse.

📊 Logging
All API requests, successful responses, and errors are logged with timestamps in:
logs/app.log
