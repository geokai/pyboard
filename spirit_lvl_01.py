# PyBoard - exercise using the accelerometer:
# This script utilizes the on-board accelerlmeter to indicate when the board is
# inclined (not level) similar to a spirit level.

# This file was created on 29/03/2017
# Author: George Kaimakis

import pyb

# create the led objects:
xlights = (pyb.LED(2), pyb.LED(3))
ylights = (pyb.LED(1), pyb.LED(4))

# create the accelerometer object:
accel = pyb.Accel()
# set the sensitivity of the system:
SENSITIVITY = 3

while True:
    # read the x axis:
    x = accel.x()

    # check if the x value is within the sensitivity range:
    if x > SENSITIVITY:
        xlights[0].on()
        xlights[1].off()
    elif x < -SENSITIVITY:
        xlights[1].on()
        xlights[0].off()
    else:
        xlights[0].off()
        xlights[1].off()

    # read the y axis:
    y = accel.y()
    # check if the y value is within the sensitivity range:
    if y > SENSITIVITY:
        ylights[0].on()
        ylights[1].off()
    elif y < -SENSITIVITY:
        ylights[1].on()
        ylights[0].off()
    else:
        ylights[0].off()
        ylights[1].off()

    pyb.delay(100)
