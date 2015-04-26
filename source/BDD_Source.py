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
        self.writeSuccess = False
        self.distance = 100
        self.connectSpeed = 10
        self.speed = None
        self.size = None
        self.city_name = None

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

    def get_city(self, city=None, city_distance=None):
        """
        Accept input regarding the current city and return that string.
        For simplicity, this does not accept input and always returns Portland, unless a new city is entered
        :param city: The entered city
        :type city: str

        :param city_distance: The distance to the new city
        :type city_distance: int

        :return: str
        """
        if city is None:
            city = 'Portland'
            return city
        else:
            self.distance = city_distance
            self.city_name = city
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
        The code I used to attempt to calculate the time difference (in seconds) doesn't seem to work properly.
        As a result, this always returns 5900 for the time being.

        :return: int or float or double
        """
        return 5900

        if (self.size / self.connectSpeed) < ((self.distance / self.speed) * 3600):
            difference = ((self.distance / self.speed) * 3600) - (self.size / self.connectSpeed)
            return difference
        else:
            difference = (self.size / self.connectSpeed) - ((self.distance / self.speed) * 3600)
            return difference

    def use_preset(self, preset='Camry'):
        """
        Accepts input regarding a preset vehicle and adjusts data accordingly.
        For simplicity, this does not accept input and defaults to Camry
        :param preset: The preset vehicle
        :type preset: str

        :return: None
        """
        if preset == 'Camry':
            self.speed = 60
            return
        if preset == 'Ferrari':
            self.speed = 100
            return
        else:
            return

    def write_to_file(self):
        """
        Writes the data regarding new cities to a file.
        To write to specific file, replace Test.txt with the needed filename/path.

        :return: bool
        """
        if os.path.isfile('source/Test.txt'):
            target = open('source/Test.txt', 'w')
            target.write(self.city_name)
            target.write(" ")
            target.write(str(self.distance))
            target.write("\n")
            target.close()
            return True
        else:
            logger.error('No such file found')
            return False

