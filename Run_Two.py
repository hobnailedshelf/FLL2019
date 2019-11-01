#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
import logging # this is used for logging

def Go_To_Tree():
    logging.info("Starting of the tree mission.")
    #go_straight(2000,1,"l",-1,"d",800,"l","b")
    go_straight(150,1,"l",-1,"l",35,"l","b")
    Robot.stop(0)

    logging.info("here")
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0) 
    Right_Motor.run_angle(-200, 650)


    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    while d < 1600:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
        logging.info(str(d))
    Robot.stop(0)
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    logging.info("out of the loop")
    wait(600)
    Med_Motor_1.run_time(75,1000)
    Med_Motor_1.run_time(-1000,400)
    Robot.drive_time(1000, 0, 4000)
    Med_Motor_1.run_time(-1000,500)
    wait(4500)
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    while d < 1800:
        Robot.drive(300,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
        logging.info(str(d))
    Robot.stop(0)   
    Robot.drive_time(-1000, 0, 3000)


    """Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0) 
    #Right_Motor.run_angle(-200, 310)
    #go_straight(2000,1,"l",-1,"d",3200,"l","b")
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    while d < 2750:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2

    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)

    wait(600)
    Med_Motor_1.run_time(100,750)
    Med_Motor_1.run_time(-1000,400)
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
        d = (l+r)/2""" 