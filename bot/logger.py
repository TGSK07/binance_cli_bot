import logging
import os

LOG_DIR = "logs"
LOG_FILE = "bot.log"

def setup_logger():
    """
    Configure and return a file-based application logger.

    Returns: 
        Configured logger instance.
    """

    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger("Binance_CLI_Bot")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(os.path.join(LOG_DIR, LOG_FILE))
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
