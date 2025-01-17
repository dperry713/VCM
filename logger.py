import logging
from datetime import datetime
import os


class Logger:
    def __init__(self, log_file=None):
        """Initialize the logger with advanced configuration"""
        if log_file is None:
            log_file = f"logs/vcm_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

        # Create logs directory
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Configure logging with detailed formatting
        logging.basicConfig(
            filename=log_file,
            filemode='a',
            format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.DEBUG
        )
        self.logger = logging.getLogger('VCM')

        # Add console handler for real-time monitoring
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def info(self, message):
        """Log informational messages"""
        self.logger.info(message)

    def warning(self, message):
        """Log warning messages"""
        self.logger.warning(message)

    def error(self, message):
        """Log error messages"""
        self.logger.error(message)

    def debug(self, message):
        """Log debug messages"""
        self.logger.debug(message)

    def critical(self, message):
        """Log critical messages"""
        self.logger.critical(message)
