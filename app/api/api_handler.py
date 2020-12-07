from flask import jsonify, request,g
from . import api
import logging
from ..homebase import gpio_controler as gpio
from ..common import constants,utils

#curl http://localhost:5010/api/get_temperature
# @api.route('/get_temperature', methods=['GET'])
# def get_temperature():
#     val = w.get_temperature_my(w,save=True)
#     logging.info("Back in api handler: Val: %f" % val)
#     response = {"Temperature":val}
#     return jsonify(response)
#
#
# #curl http://localhost:5010/api/get_humidity
# @api.route('/get_humidity', methods=['GET'])
# def get_humidity():
#     w = MySenseHat()
#     val = w.get_humidity(w, save=True)
#     logging.info("Back in api handler: Val: %f" % val)
#     response = {"Humidity":str(val)}
#     logging.info(response)
#     return jsonify(response)
#
# #curl http://localhost:5010/api/get_pressure
# @api.route('/get_pressure', methods=['GET'])
# def get_pressure():
#     w = MySenseHat()
#     val = w.get_pressure(w, save=True)
#     logging.info("Back in api handler: Val: %f" % val)
#     response = {"Pressure":val}
#     return jsonify(response)
#
# @api.route('/sparkle',methods=['GET'])
# def sparkle_on_sense():
#     w = MySenseHat()
#     running = False
#     if w.sparkle_on_sense(w):
#         running = True
#
#     return jsonify({"Sparkle_Running":running})
#
# @api.route('/smiley',methods=['GET'])
# def smiley_on_sense():
#     w = MySenseHat()
#     w.set_smiley(w)
#     return jsonify({"Smiley":"Running"})


@api.route('/multi_temp_reading',methods=['GET'])
def multi_temp_reading():
    return jsonify("")


#curl http://localhost:5010/api/toggle_led
@api.route('/toggle_led',methods=['GET'])
def toggle_led():
    #color = utils.get_parameter(request,name='color',required=False)
    color = request.args.get('color')
    colors = [constants.RED,constants.BLUE,constants.GREEN]
    logging.info("Toggling color %s " % color)
    if color in colors:
        value = gpio.toggle_led(color)
        return jsonify({color: value})
    else:
        return jsonify({'color': 'parameter %s not defined' % color})


#curl http://localhost:5010/api/red_from_dth11
@api.route('/read_from_dth11',methods=['GET'])
def read_save_DTH11():
    v = gpio.read_dth11()
    return jsonify(json_obj = v)


@api.route('/blink_led',methods=['GET'])
def blink_led():
    c = request.args.get('color')
    gpio.blink_led(c)
    return jsonify({'Blink':c})
