import logging
from .. import db
from ..common.exceptions import DBError
import datetime
from ..common.utils import dump_datetime,is_float
from sqlalchemy import func, desc

__author__ = 'tomas'


class Weather_model(db.Model):
    __tablename__ = 'weather'
    id = db.Column(db.Integer, primary_key=True)
    reader = db.Column(db.String(20), nullable=False)
    value = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, reader, value, timestamp):
        self.reader = reader
        self.value = value
        self.timestamp = timestamp

    @staticmethod
    def save_to_db(reader, value):
        try:
            v = float(value)
            logging.info("Saving new record , Reader: %s Value: %f" % (reader, v))
            w = Weather_model(reader=reader, value=v, timestamp=datetime.datetime.utcnow())
            db.session.add(w)
            db.session.commit()
            db.session.close()
            return True
        except Exception as e:
            raise DBError(e)
            return False

    @staticmethod
    def get_values_by_date(date,reader=None):
        try:
            query = db.session.query(Weather_model.reader, Weather_model.value, Weather_model.timestamp)
            if reader:
                query = query.filter(Weather_model.reader == reader)
            query = query.filter(Weather_model.timestamp >= date)
            query = query.group_by(Weather_model.reader)
            result = query.all()
            logging.info(result)
            return result
        except Exception as e:
            raise DBError(e)

    @staticmethod
    def get_all(reader):
        try:
            result = []
            if reader == 'all':
                result = db.session.query(Weather_model.id, Weather_model.reader, Weather_model.value,
                                          Weather_model.timestamp).order_by(Weather_model.timestamp.desc()).all()
            else:
                result = db.session.query(Weather_model.id, Weather_model.reader, Weather_model.value,
                                          Weather_model.timestamp).filter(Weather_model.reader == reader)\
                    .order_by(Weather_model.timestamp.desc()).all()
            return result
        except Exception as e:
            raise DBError(e)

    @staticmethod
    def get_all_as_json(reader):
        result = Weather_model.get_all(reader)
        try:
            json_arry = []
            if result:
                for record in result:
                    weather_model = Weather_model(record.reader, record.value, record.timestamp)
                    json_arry.append(weather_model.serialize)
            else:
                json_arry = []
            logging.info("Size %s " % len(json_arry))
            return json_arry
        except Exception as e:
            raise DBError(e)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        json = {
            'reader': self.reader,
            'value': self.value,
            'timestamp': dump_datetime(self.timestamp)}
        logging.info(json)
        return json

    @staticmethod
    def get_latest_readings(reader=None):
        try:
            results = []
            readers = db.session.query(Weather_model.reader).group_by(Weather_model.reader).all()
            a = []
            for r in readers:
                sql_q = '''select * from weather where reader = "%s" order by id desc limit 1''' % r[0]
                resultproxy = db.session.execute(sql_q)
                d = {}
                for row in resultproxy:
                    logging.info("row: %s" %row)
                    i, r, v, t = row
                    w = Weather_model(r,v,t)
                    logging.info("Weather model: ")
                    logging.info(w.serialize)

                    # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
                    # for tup in row.items():
                    #     logging.info(tup)
                    #     # build up the dictionary
                    #     logging.info("------------------------------")
                    #     d = {**d, **{tup[0]: tup[1]}}
                    a.append(w.serialize)
            return a
        except Exception as e:
            raise DBError(e)
