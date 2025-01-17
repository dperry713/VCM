import pytest
from logger import Logger
import os

@pytest.fixture
def logger(tmp_path):
    log_file = tmp_path / "test.log"
    return Logger(str(log_file))

def test_logger_initialization(logger):
    assert logger.logger is not None

def test_logging_levels(logger):
    test_message = "Test message"
    logger.info(test_message)
    logger.error(test_message)
    logger.debug(test_message)
    logger.warning(test_message)
    logger.critical(test_message)
    assert os.path.exists(logger.logger.handlers[0].baseFilename)
