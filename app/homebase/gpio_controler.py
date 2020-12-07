import RPi.GPIO as GPIO
import time, datetime
from ..common import constants, utils
import logging
import Adafruit_DHT
from ..models.weather_model import Weather_model


def stop_led(color):
    if color == constants.RED:
        RED.stop()
    elif color == constants.BLUE:
        BLUE.stop()
    elif color == constants.GREEN:
        GREEN.stop()



def stop_all_led():
    HardwareTracker.set_off()


def start_led(color):
    if color == constants.RED:
        RED.start(1)
    elif color == constants.BLUE:
        BLUE.start(1)
    elif color == constants.GREEN:
        GREEN.start(1)



def blink_green_led():
    for x in range(1,5):
        if x % 2 == 0:
            GREEN.start(1)
        else:
            GREEN.stop()
        time.sleep(0.2)
    GREEN.stop()

def toggle_led(color):
    value = HardwareTracker.toggle_value(color)
    logging.info("in controler, got value: %s " % value)
    if value == constants.VALUE_OFF:
        logging.info("%s stop " % color)
        stop_led(color)
    elif value == constants.VALUE_ON:
        logging.info("%s start " % color)
        start_led(color)
    else:
        logging.info("Value %s not recognized for color %s " %(value, color))
    return value


# def read_dth11():
#     h, t = Adafruit_DHT.read_retry(11, 4)
#     Weather_model.save_to_db(reader=constants.DHT11_temp,value=t)
#     Weather_model.save_to_db(reader=constants.DHT11_humidity,value=h)
#     blink_green_led()
#     logging.info('Temp: %f C  Humidity: %f percent' % (t, h))
#     dt = get_time_as_str()
#     return {"TEMPERATURE":t,"HUMIDITY":h,"TIMESTAMP":dt}


def get_time_as_str():
    d = datetime.datetime.utcnow()
    return utils.dump_datetime(d)



#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#defining the pins
# green = 20
# red = 21
# blue = 22

hardware = dict()
hardware['RED'] = constants.GPIO_PIN_21
hardware['BLUE'] = constants.GPIO_PIN_22
hardware['GREEN'] = constants.GPIO_PIN_20

#defining the pins as output
#GPIO.setup(hardware['RED'], GPIO.OUT)
#GPIO.setup(hardware['GREEN'], GPIO.OUT)
#GPIO.setup(hardware['BLUE'], GPIO.OUT)

#choosing a frequency for pwm
Freq = 1

#RED = GPIO.PWM(hardware['RED'], Freq)
#GREEN = GPIO.PWM(hardware['GREEN'], Freq)
#BLUE = GPIO.PWM(hardware['BLUE'], Freq)


logging.info(hardware)