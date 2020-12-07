from flask import jsonify, request,g, Response
from . import api
import logging
from ..common import constants,utils
from ..models.weather_model import Weather_model


@api.route('/get_records',methods=['GET'])
def get_records():
    sensor = request.args.get('sensor',default='all')
    logging.info("Sensor is %s " % sensor)
    values = Weather_model.get_all_as_json(sensor)
    return jsonify(code=200,json_list = values)


@api.route('/get_latest',methods=['GET'])
def get_latest():
    logging.info("Android application requesting latest readings")
    json = {"ResponseCode":200}
    data = []
    json['Data'] = Weather_model.get_latest_readings()
    return jsonify(json=json)