"""
Source Code for BDD Rounds
"""

import logging
import os

logger = logging.getLogger(__name__)

class Calculator():

    """
    Calculator Class: Handles necessary data
    """

    def __init__(self):
        self.readSuccess = False
        self.distance = 100
        self.connectSpeed = 10
        self.speed = None
        self.size = None

    def read_file(self, filename=None):
        """
        Attempt to read given file.
        For simplicity, city remains uninitialized while distance and connect speed are constant.
        :param filename: The file to be read
        :type filename: str

        :return: None
        """
        if os.path.isfile(filename):
            self.readSuccess = True
            logger.info('File read successful')
        else:
            logger.error('No such file found')

    def get_speed(self, speed=60):
        """
        Accept input regarding driving speed and return that value.
        For simplicity, this does not accept input and always returns 60.
        :param speed: The entered speed
        :type speed: int or float or double

        :return: int or float or double
        """
        self.speed = speed
        return speed

    def get_size(self, hdsize=1000):
        """
        Accept input regarding hard drive size and return that value in GB.
        For simplicity, this does not accept input and always returns 1024.
        :param size: The entered size
        :type size: int

        :return: int
        """
        self.size = hdsize
        return hdsize

    def get_city(self, city='Portland'):
        """
        Accept input regarding the current city and return that string.
        For simplicity, this does not accept input and always returns Portland.
        :param city: The entered city
        :type city: str

        :return: str
        """
        return city

    def compare_speeds(self, fastest=None):
        """
        Compares present data regarding speeds and distances to determine the faster option.

        :return: str
        """
        if (self.size / self.connectSpeed) < ((self.distance / self.speed) * 3600):
            return 'Hard Drive'
        if (self.size / self.connectSpeed) > ((self.distance / self.speed) * 3600):
            return 'Driving'

    def get_time_difference(self):
        """
        Compares present data and returns the time difference between options.

        :return: int or float or double
        """
        if (self.size / self.connectSpeed) < ((self.distance / self.speed) * 3600):
            difference = ((self.distance / self.speed) * 3600) - (self.size / self.connectSpeed)
            return difference
        else:
            difference = (self.size / self.connectSpeed) - ((self.distance / self.speed) * 3600)
            return difference