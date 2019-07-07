import logging
from logging.handlers import TimedRotatingFileHandler
from app.constants.main import *

# create logger
# logger.info(), logger.warning(), logger.error()
logHandler = TimedRotatingFileHandler(LOGS_PATH, when="midnight", interval=1, backupCount=7)
logFormatter = logging.Formatter('%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s')
logHandler.setFormatter(logFormatter)

logger = logging.getLogger()
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

def helper_test(*args):
    pass