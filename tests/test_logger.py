from utils.logger import get_logger


logger = get_logger(__name__)


def test_logger():

    logger.debug("This is a DEBUG message")
    logger.info("This is an INFO message")
    logger.warning("This is a WARNING message")
    logger.error("This is an ERROR message")

    assert True