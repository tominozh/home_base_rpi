import logging
from app import db
from ..api import api


@api.teardown_request
def teardown_request(exception):
    if exception:
        logging.error(exception)
    try:
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
        db.session.remove()