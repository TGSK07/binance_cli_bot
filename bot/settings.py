import os
from dotenv import load_dotenv


def load_settings():
    load_dotenv()

    API_KEY = os.getenv("BINANCE_API_KEY")
    SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")
    BINANCE_BASE_URL = os.getenv("BINANCE_BASE_URL")

    if not API_KEY or not SECRET_KEY:
        raise EnvironmentError("Binance keys not set in env.")
    
    return {
        "BINANCE_API_KEY":API_KEY,
        "BINANCE_SECRET_KEY":SECRET_KEY,
        "BINANCE_BASE_URL":BINANCE_BASE_URL
    }