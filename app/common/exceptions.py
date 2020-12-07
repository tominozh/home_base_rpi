__author__ = 'chenfeiyu'
from . import constants
import logging


class CommonError(ValueError):
    def __init__(self, message, root_tag=constants.XML_ROOT_TAG):
        ValueError.__init__(self, message)
        self.root_tag = root_tag


class ValidationError(CommonError):
    pass


class ProcessingError(CommonError):
    logging.info("Processing error");
    pass


class RequestTimeoutError(CommonError):
    pass


class NotFoundError(CommonError):
    pass

class HttpError(CommonError):
    pass

class DBError(CommonError):
    pass

class ForbiddenError(CommonError):
    pass

