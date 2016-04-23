import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

dh = logging.FileHandler('debug.log')
dh.setLevel(logging.DEBUG)

eh = logging.FileHandler('error.log')
eh.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
dh.setFormatter(formatter)
eh.setFormatter(formatter)

logger.addHandler(dh)
logger.addHandler(eh)

logger.debug('Hello World')
logger.info('HEYY')

try:
    fdsa;fjsda
except Exception as e:
    logger.error(e)