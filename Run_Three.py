#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
import logging # this is used for logging


def lift_traffic():
    logging.info("Starting of the traffic mission.")

    go_straight(300,-1,"l",1,"d",1079,"l","b")
    #logging.info("step 1 completed.")
    #go_straight(300,-1,"l",1,"l",20,"l","b")
    #logging.info("step 2 completed.")

    line_follower(500,1,"l",1,"d",1100,"l","w")
    #logging.info("step 3 completed.")

    Left_Motor.run_time(300, 3000)
    Left_Motor.run_time(-1000, 1000)
    Robot.drive_time(-1000,0,5000)



