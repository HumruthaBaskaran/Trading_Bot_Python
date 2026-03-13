from pybit.unified_trading import HTTP
from bot.logging_config import setupLogger

logger = setupLogger()

class BybitClient:
    def __init__(self,api_key,api_secret_key):
        try:
            self.client = HTTP(
                testnet= True,
                api_key=api_key,
                api_secret = api_secret_key
            )
            logger.info("Bybit client initialized successfully")
        except Exception as e:
            logger.error(f"Client initialization failed :{e}")
            raise
    
    def getClient(self):
        return self.client