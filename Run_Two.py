#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
import logging # this is used for logging

def Go_To_Tree():
    logging.info("Starting of the tree mission.")
    go_straight(2000,1,"l",-1,"d",800,"l","b")
    Left_Motor.run_angle(200,278)
    go_straight(2000,1,"l",-1,"d",3200,"l","b")
    wait(500)
    Med_Motor_1.run_time(110,1000)
    Robot.drive_time(1000, 0, 4000)
    wait(6000)
    go_straight(2000,1,"l",-1,"d",1900,"l","b")
    go_straight(2000,-1,"l",1,"d",1900,"l","b")