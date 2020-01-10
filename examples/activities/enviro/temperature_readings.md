#### Things to try - Temperature Readings

The temperature reading is given very precisely, for example: 23.307827006519073

This is great for some applications, but what if you wanted to just have a rough idea?

Try changing line 12. It was originally:

        print(temp)

If we change it to:

        print(round(temp))
        
The temperature should round to the nearest whole number.

----

What if you only want one decimal place (one digit after the decimal point)? The code is a little more complex, but it's easy to modify for different numbers of decimal places once you know how it works.

        print(round(temp))
        
changes to:

        print(round(temp, 2))
        
It's actually not that tricky! Can you round the temperature to 3 decimal places? To 5 decimal places?

----

Now we have a nice looking temperature reading, how about adding on the units that the temperature is measured in?

In the world of science we use degrees centigrade (C) or Kelvin (K). The most widely used is C, and that's what this sensor gives you readings in.

Let's look at that print line again.

        print(round(temp, 2))
        
We want it to print the temperature, and then print the letter C afterwards. Because C is a text string, it needs to be in double quote marks (on most keyboards these are above the number 2, or above the single quote mark next to the enter key).

Here is the new line:

        print(round(temp, 2), "C")
        
Look at the order things go in. Print the rounded temperature to 2 decimal places, followed by a letter "C". That makes sense, right?

Can you figure out where you would put the word "temperature" if you wanted to display that too?
