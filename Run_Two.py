#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
import logging # this is used for logging

def Go_To_Tree():
    logging.info("Starting of the tree mission.")
    #go_straight(2000,1,"l",-1,"d",800,"l","b")

    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)

    while d < 1500:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2

    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)

    Left_Motor.run_angle(900,95)
    #go_straight(2000,1,"l",-1,"d",3200,"l","b")

    while d < 3000:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2

    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)

    wait(600)
    Med_Motor_1.run_time(110,1000)
    Med_Motor_1.run_time(-1000,1000)
    Robot.drive_time(1000, 0, 6000)
    wait(4555)
    #go_straight(2000,-1,"l",-1,"d",2200,"l","b")
    #go_straight(2000,1,"l",-1,"d",1700,"l","b")

    Robot.drive_time(1000, 0, 2500)

    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)

    while d < 900:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2