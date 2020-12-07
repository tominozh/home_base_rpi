from .. import db
from datetime import datetime as dt
from ..common.exceptions import DBError

class GPIOTracker(db.Model,):
    __tablename__ = "gpio_tracker"
    id = db.Column(db.Integer, primary_key=True)
    pin = db.Column(db.Integer, nullable=False, unique=True)
    state = db.Column(db.String(10), nullable=False)
    timestamp = db.Column(db.DateTime, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)

    def __init__(self,pin,state,timestamp):
        self.id = None
        self.pin = pin
        self.state = state
        self.timestamp = timestamp

    @staticmethod
    def get_states():
        try:
            result = db.session.query(GPIOTracker).all()
            return [r.selialize for r in result]
        except Exception as e:
            raise DBError(e)

    @property
    def serialize(self):
        return {'pin':self.pin,
                'state':self.state,
                'timestamp':self.timestamp }
