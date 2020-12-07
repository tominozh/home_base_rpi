from flask import jsonify, request,g, Response
from . import api
import logging, time
from ..common import constants,utils
from ..models.weather_model import Weather_model
# try:
#     from sense_hat import SenseHat
# except:
#     from sense_emu import SenseHat
# from ..sense_hat.sense_hat_controler import get_random_matrix_coordinates,get_rgb_values


@api.route('/hello_esp', methods=['GET','POST'])
def hello_esp():
#     m = SenseHat()
#     m.set_pixel(0,0,get_rgb_values())
    t = utils.get_parameter(request,name="temp",required=False)
    h = utils.get_parameter(request, name="hum",required=False)
    json = {}
    is_saved = False
    if t is not None and h is not None:
#         m.set_pixel(0, 1, get_rgb_values())
        logging.info("Params: t %s and h %s " % t, h)
        is_saved = Weather_model.save_to_db(constants.DHT11_temp,t)
        if is_saved:
            json[constants.DHT11_temp] = t
#             m.set_pixel(0, 2, get_rgb_values())
        is_saved = Weather_model.save_to_db(constants.DHT11_humidity,h)
        if is_saved:
            json[constants.DHT11_humidity] = h
#             m.set_pixel(0, 3, get_rgb_values())
        json = {"Temperature: %s , Humidity: %s " % temperature,humidity}
        logging.info(json)
#     m.set_pixel(0, 4, get_rgb_values())
#     m.clear()
    return jsonify(route={'route': 'ESP8266', 'records_saved': is_saved}, json=json)


@api.route('/post_data_from_dht11',methods=['POST'])
def post_data_from_dht11():
    start_time = time.time()
#     m = SenseHat()
#     m.set_pixel(0, 0, get_rgb_values())
    req_data = request.get_json()
    logging.info(req_data)
    temp = req_data['temp']
    hum = req_data['hum']
    error = []
    is_saved = False
    json = {}
    if temp is not None and hum is not None:
#         m.set_pixel(0, 1, get_rgb_values())
        # logging.info("Params: t %s and h %s " % t, h)
        is_saved = Weather_model.save_to_db(constants.DHT11_temp, temp)
        if is_saved:
            json[constants.DHT11_temp] = temp
#             m.set_pixel(0, 2, get_rgb_values())
        else:
            error.append("Temperature not saved")
        is_saved = Weather_model.save_to_db(constants.DHT11_humidity, hum)
        if is_saved:
            json[constants.DHT11_humidity] = hum
#             m.set_pixel(0, 3, get_rgb_values())
        else:
            error.append("Humidity not saved")
#         json = {"Temperature: %s , Humidity: %s " % temp, hum}
        logging.info(json)
#     m.set_pixel(0, 4, get_rgb_values())
#     m.clear()
    elapsed_time = time.time() - start_time
    return jsonify(sever={'route': 'post_data_from_dht11', 'request_method': request.method, 'errors': error,
                          'elapsed_time':elapsed_time}, data=json)
