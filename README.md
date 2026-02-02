# Binance Futures CLI Trading Bot (Testnet)

A command-line Python application to place **MARKET** and **LIMIT** orders on **Binance USDT-M Futures Testnet**.  
Built with clean architecture, input validation, logging, and proper error handling.

---

## Features

- Place **MARKET** and **LIMIT** orders
- Supports **BUY** and **SELL**
- Binance **Futures Testnet (USDT-M)**
- CLI-based input using `argparse`
- Input validation before API calls
- File-based structured logging
- Graceful handling of API and network errors
- Modular and reusable codebase

---

## Tech Stack

- Python 3.13.3

---

## 📁 Project Structure

binance_cli_bot/
│
├── bot/
│ ├── cli.py # CLI argument parsing & output
│ ├── validators.py # Input validation logic
│ ├── client.py # Binance API wrapper
│ ├── logger.py # Logging configuration
│ ├── settings.py # Environment & config loader
│
├── logs/
│ └── bot.log # Application logs
│
├── .env # API credentials (not committed)
├── .gitignore 
├── main.py # Application entry point
├── requirements.txt
└── README.md

---

## Setup Steps

### 1. Clone the Repository
```bash
git clone https://github.com/TGSK07/binance_cli_bot.git
cd binance_cli_bot
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Add creds in .env file. 

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key
BINANCE_BASE_URL=https://testnet.binancefuture.com

## How to Run
All commands are executed from the project root.

### 1. Market Order Example
python main.py --sym BTCUSDT --s BUY --ot MARKET --qty 0.01

### 2. Limit Order Example
python main.py --sym BTCUSDT --s SELL --ot LIMIT --qty 0.01 --p 42000


## Assumptions

- User is trading on Binance USDT-M Futures Testnet.

- API keys are valid and funded with test USDT.

- Symbol provided exists on Binance Futures.

- No leverage or margin configuration is handled.

- No retry logic is implemented (intentional for simplicity).

- Quantity and price precision rules are enforced by Binance API.