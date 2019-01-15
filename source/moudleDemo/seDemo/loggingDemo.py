import logging

logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)

fh=logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

formatter = logging.Formatter
