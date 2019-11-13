#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
import logging # this is used for logging


def lift_traffic():
    logging.info("Starting of the traffic mission.")

    #old attachment code
    go_straight(300,-1,"l",1,"d",850,"l","b")
    line_follower(500,1,"l",1,"d",700,"l","w")
    #old attchment code end
   
    #go_straight(700,-1,"r",1,"d",1500,"l","w")

    Left_Motor.run_time(1000, 1000)
    wait(300)
    Left_Motor.run_time(-1000, 800)
    Robot.drive_time(-1000,0,4000)



