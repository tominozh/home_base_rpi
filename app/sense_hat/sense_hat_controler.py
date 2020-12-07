try:
    from sense_hat import SenseHat
except:
    from sense_emu import SenseHat
import logging
from random import randint
import time
from multiprocessing import Process, process

def esp_request_finished(self):
    self.is_in_use = False


def sparkle():
    while True:
        x,y = get_xy_coordinates()
        r,g,b, = get_rgb_values()
        sense.clear()
        sense.set_pixel(x,1,[r,g,b])
        time.sleep(0.5)
    p = P
    sense.clear()


def esp_request_registered():
    p = Process(target=sparkle)
    p.daemon = True
    p.start()


sense = SenseHat()
sense.clear()
sense.set_rotation(180)
sense.low_light = True

def get_rgb_values():
   x = randint(1, 255)
   y = randint(1, 255)
   z = randint(1, 255)
   c = (x, y, z)
   return c


def get_xy_coordinates():
   x = get_random_matrix_coordinates()
   y = get_random_matrix_coordinates()
   return (x, y)


def get_random_matrix_coordinates():
   return randint(0, 7)

def get_temperature_from_sense():
    return sense.get_temperature()

def get_humidity_from_sense():
    return sense.get_humidity()

def get_pressure_from_sense():
    return sense.get_pressure()

