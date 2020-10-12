import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# import helper


# logger = logging.getLogger(__name__)

# # # create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

# # # set level and format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)


# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('this is a warning')
# logger.error("this is an error")

# import traceback

# try: 
#     a = [1,2,3]
#     val = a[4]
# except:
#     logging.error(f'The error is {traceback.format_exc()}')

# from logging.handlers import RotatingFileHandler

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

# for _ in range(10000):
#     logger.info('Hello world!')

from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s = second, m, h, d, midnight, w0 = monday, w1=tues, etc...
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Hello world!')
    time.sleep(5)

