import logging

logging.basicConfig(filename='trading_bot.log', level=logging.INFO)
logger = logging.getLogger()

def log_trade(date, ticker, action, price):
    logger.info(f"{date} - {action} {ticker} at {price}")
