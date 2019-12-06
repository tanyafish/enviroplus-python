#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from bme280 import BME280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus


# We will only change things below here. The code above is to set up the sensor.

# Try adding a different message on startup.
# Change the text between the triple quote marks.

print("""weather.py - Print readings from the BME280 weather sensor.
Press Ctrl+C to exit!
""")

# How about adding a little rest here so you have time to read the message?
# Delete the hashtag/hash symbol/pound symbol before the next line and increase or decrease the time.

# time.sleep(1)

# This bit sets up communication between the Pi and the sensor so it can send commands.
# Do not change this bit.

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

# This is the loop that carries on taking readings until you stop the program.
# 
while True:
    temperature = bme280.get_temperature()
    pressure = bme280.get_pressure()
    humidity = bme280.get_humidity()
    print("""Temperature: {:05.2f} °C
Pressure: {:05.2f} hPa
Relative humidity: {:05.2f} %
""".format(temperature, pressure, humidity))
    time.sleep(1)
