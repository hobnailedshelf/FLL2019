#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
import logging # this is used for logging

def move_stack():
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    go_straight(1000,-1,"l",1,"d",1425,"l","b")
    Robot.drive_time(-1000, 800, 1000)
    Robot.drive_time(-1000, 0, 1500)


def move_stack_tree():
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    go_straight(1000,-1,"l",1,"d",1200,"l","b")
    Robot.drive_time(-1000, 800, 760)
    Robot.drive_time(-1000, 0,2700)

