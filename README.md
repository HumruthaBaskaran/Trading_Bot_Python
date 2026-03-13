Trading Bot – Futures Order CLI

A Python CLI application that places Market and Limit orders on the Bybit Futures Testnet.

The project demonstrates:

API integration with a crypto exchange

CLI-based order placement

structured code architecture

logging and error handling

Features

Place Market orders

Place Limit orders

Place Stop-Limit orders (bonus feature)

Supports BUY and SELL

CLI input validation

Structured logging of:

API requests

API responses

errors

Clean modular architecture

Project Structure
trading_bot/
│
├─ bot/
│  ├─ client.py          # Exchange client wrapper
│  ├─ orders.py          # Order placement logic
│  ├─ validators.py      # CLI input validation
│  └─ logging_config.py  # Logging configuration
│
├─ cli.py                # CLI entry point
├─ requirements.txt
├─ README.md


Setup
1. Clone the repository
git clone <repository_url>
cd trading_bot
2. Create a virtual environment
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Configure API credentials

Create API keys from the Bybit Testnet and add them in cli.py.

Running the Application

Market Order
python cli.py --symbol BTCUSDT --side Buy --type MARKET --quantity 0.001

Limit Order
python cli.py --symbol BTCUSDT --side Buy --type LIMIT --quantity 0.001 --price 60000

Stop-Limit Order (Bonus)
python cli.py --symbol BTCUSDT --side Sell --type STOP_LIMIT --quantity 0.001 --price 64900 --stop_price 65000

Logging

All API requests, responses, and errors are logged to:

trading_bot.log

Example log entry:

INFO - API REQUEST: MARKET order BTCUSDT Buy qty=0.001
INFO - API RESPONSE: {...}

Error Handling

The application handles:

Invalid CLI input

API request errors

Network failures

Errors are displayed to the user and logged.

Assumptions

The original assignment required using the Binance Futures Testnet.
However, Binance Testnet currently requires identity verification in my region.

To proceed with the assignment, the implementation uses the Bybit Testnet API instead.

The application architecture is exchange-agnostic.
Switching to Binance would only require modifying the client implementation.

Requirements

Python 3.x

pybit

Install using:

pip install -r requirements.txt