from bot.cli import cli
from bot.logger import setup_logger
from bot.settings import load_settings

def main():
    logger = setup_logger()

    try:
        settings = load_settings()
        cli(settings, logger)
    
    except Exception as e:
        logger.exception("Fatal Application Error.")
        print(f"Fatal Error: {str(e)}")


if __name__=="__main__":
    main()