# uses short names instead of sensor references (eg weather not bme280)

import short
import time

# takes a temperature reading from the bme280 (weather) and calls it "temp"
# prints the temperature reading on the screen
# waits 1 second before doing it again

while True:
    temp = short.weather.get_temperature()
    print(temp)
    time.sleep(1)
