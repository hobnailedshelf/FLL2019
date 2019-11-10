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
battery = str(brick.battery.voltage())
logging.info(battery)


def control_runs():
    #Code to manage runs with buttons
    brick.display.clear()
    brick.display.text("Ready to Run", (60, 50))
    voltage = str(brick.battery.voltage())
    brick.display.text("Voltage = " + voltage)
    brick.light(Color.ORANGE)
    while True:
        if Button.UP in brick.buttons():
            brick.display.clear()
            brick.display.text("UP Button - CRANE", (60, 50))
            Go_To_Crane_2()
        elif Button.RIGHT in brick.buttons():
            brick.display.clear()
            brick.display.text("RIGHT Button - TREE", (60, 50))
            Go_To_Tree_2()   
        elif Button.DOWN in brick.buttons():
            brick.display.clear()
            brick.display.text("DOWN Button - TRAFFIC", (60, 50))
            lift_traffic()
        elif Button.LEFT in brick.buttons():
            brick.display.clear()
            brick.display.text("LEFT+ Button - SWING/SAFETY", (60, 50))
            Go_To_Swing()
        elif Button.CENTER in brick.buttons():
            brick.display.clear()
            brick.display.text("CENTER + Button - STACK", (60, 50))
            move_stack()
            
        

control_runs()
