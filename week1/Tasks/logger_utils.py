import logging
import time

class Logger:

    def __init__(self,logfile="app.log"):
        self.logger = logging.getLogger("RPA BOT")
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(logfile)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def info(self,message):
            self.logger.info(message)

    def error(self,message):
            self.logger.error(message)

    def debug(self,message):
            self.logger.debug(message)

    def warning(self,message):
            self.logger.warning(message)

    print("Logger initialized successfully")
