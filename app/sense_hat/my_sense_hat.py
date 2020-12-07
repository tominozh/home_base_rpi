from multiprocessing import Process, current_process, Manager
from sense_hat import SenseHat
import logging, time
from . sense_hat_controler import get_rgb_values, get_xy_coordinates, sparkle


class MySenseHat(SenseHat):

    def __init__(self):
        SenseHat.__init__(self)
        self.clear()
        self.set_rotation(180)
        self.low_light = True


    def somefunc(self):
        p = Process(target=clear_sense, name="SENSE_HAT_PROCESS")
        logging.info("in some function")
        p.daemon = True
        p.join(timeout=1000)
        logging.info("wake up")
        logging.info("Starting Sense Hat Thread....")
        logging.info("%s" % current_process().name)


def clear_sense():
    sense.clear()

    def sparkle(self):
        while True:
            x, y = get_xy_coordinates()
            r, g, b, = get_rgb_values()
            self.sense.clear()
            self.sense.set_pixel(x, 1, [r, g, b])
            time.sleep(1)
