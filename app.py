from books_recommendation_systeme.exception.exception_handler import AppException
from books_recommendation_systeme.logger.log import logging
import sys



try:
    2+A
except Exception as e:
    logging.info(e)
    raise AppException(e, sys) from e 