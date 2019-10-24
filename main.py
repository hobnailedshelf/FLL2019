#!/usr/bin/env pybricks-micropython
from Initialize import *
init_robot() # We initialize the robot here. All the sensors, motors, brick, etc.

from Common_Functions import *
from Run_One import *
from Run_Two import *
from Run_Three import *
from Run_Four import *
import logging # this is used for logging
#joe is here Dont mind me
logging.info("Beginning of the Runs.")

#uncomment one of the functions below to run your missions
#Go_To_Crane()
#Go_To_Tree()
Go_To_Swing()
#lift_traffic()

def control_runs():
    #Code to manage runs with buttons
    brick.display.clear()
    brick.display.text("Ready to Run", (60, 50))
    voltage = str(brick.battery.voltage())
    brick.display.text("Voltage = " + voltage)
    brick.light(Color.ORANGE)
    pressed = str(brick.buttons())

    logging.info(pressed)
    while True:
        if str(brick.buttons())=="16":
            brick.display.clear()
            brick.display.text("Run 4", (60, 50))
        pressed = str(brick.buttons())
        logging.info(pressed)