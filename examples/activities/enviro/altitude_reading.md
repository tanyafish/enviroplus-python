## Things to try - Altitude Readings

#### Taking the reading
First of all, what is altitude? It's the distance above sea level, and it's measured using air pressure. It's useful to know if you're flying a plane, or climbing mountains!

The altitude is calculated by measuring the air pressure, and comparing it to the air pressure at a known height. The **higher** up you are, the **lower** the air pressure is.

If you can, try taking an altitude reading holding your Pi in the air, or on a different floor if you're in a multi-storey building.

When you take a reading with your enviro or enviroplus, what do you notice about the reading?

When we take a reading at Pirate Towers, it shows us:

        -37.96

If that is right, it means we're *below* sea level! Although the local shopping centre is at 29m above sea level, we are somewhere around 60m above sea level. To find out the altitude at your location, search on the internet (we searched "sheffield height above sea level").

----
#### Fixing the reading

There is a bit in the library for the sensor that sets a base pressure level to compare against. When pilots fly, they can input the base level to their systems so that the altimeter (height display) is right. 
As you can imagine, it's very important for pilots! The base level is called the QNH. It doesn't actually stand for anything, it's from when morse code was used over the radio, and it was quick to send!
Some people remember it as Query - Not Here! because it changes depending on where you are in the world.

The software has the QNH set at 1013.25.

To change the QNH in the program, find this line:

        altitude = short.weather.get_altitude()
        
In the brackets we can specify our own choice of QNH (and now we feel like pilots, yes?)

Handily, airports have a really regular bulletin called a METAR that has the QNH and loads of other cool weather data. Find an airfield near you and search for its name and "METAR".

Here is the METAR for an airfield called Cranfield (picked for sentimental reasons).

```
METAR
EGTC 101450Z 26006KT 210V280 9999 FEW020 08/05 Q1026
Our last available update is from 10 January, 14:50 UTC. There is a Westerly wind of 6 knots .
Wind varying between South-westerly and Westerly directions. Current visibility is 10 km or more.
There are a few clouds at 2,000 feet. The temperature is 8°C. The dewpoint is 5°C. The QNH is 1026mb.
```
The QNH is 1026, so all we have to do is change the line of code to:

        altitude = short.weather.get_altitude(qnh=1026)
        

See if changing the QNH to match your area gives you a more accurate reading. And then go and fall down the rabbit hole of METAR forecasts.

