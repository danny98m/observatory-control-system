""" Dome Control library

Python functions that will open and close astrohaven domes.
"""

import astrohaven
import serialist
from forecastiopy import *


class dome_control:
    """A single dome to be controlled."""
    def __init__(self):
        self.dome = ''
        self.connect()


    def connect(self):
        """Locate and connect to a dome."""
        serlist = serialist.Serialist()
        for port in serlist:
            self.dome = astrohaven.Astrohaven(port)
            if(not self.dome.ready):
                self.dome.closeconn()


    def disconnect(self):
        """Disconnect from the dome."""
        self.dome.closeconn()

    def a_open(self):
        """Open the A side of the dome."""
        self.dome.fullmove('A','Open')

    def b_open(self):
        """Open the B side of the dome."""
        self.dome.fullmove('B','Open')

    def a_close(self):
        """Close the A side of the dome."""
        self.dome.fullmove('A','Close')

    def b_close(self):
        """Close the B side of the dome."""
        self.dome.fullmove('B','Close')

    def full_close(self):
        """Close both sides of the dome."""
        self.dome.fullclose()

    def full_open(self):
        """Open both sides of the dome."""
        self.dome.fullopen()
        