# uses short names instead of sensor references (eg weather not bme280)

import short
import time

# takes an altitude reading from the bme280 (weather) and calls it "altitude"
# prints the altitude reading on the screen
# waits 5 seconds before doing it again

while True:
    altitude = short.weather.get_altitude()
    print (round(altitude))
    time.sleep(5)
