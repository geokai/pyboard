# PyBoard - exercise using the accelerometer:
# This script utilizes the on-board accelerlmeter to vary the blue led intensity:

# This file was created on 28/03/2017
# Author: George Kaimakis

import pyb

# create accelerometer object:
accel = pyb.Accel()
# create led object:
light = pyb.LED(4)
# set the sensitivity of the system:
SENSITIVITY = 3

while True:
    # read the x axis:
    x = accel.x()

    # check if value is negative and if so, convert to positive:
    if x < 0:
        x *= -1

    # check if value is greater than the set sensitivity:
    if abs(x) > SENSITIVITY:
        # set the led intensity mapping 0 - 255 range to 0 - 30:
        light.intensity(x * 8)
    else:
        light.off()

    # for debugging:
    print(x)

    # small delay to smooth the loop:
    pyb.delay(100)

