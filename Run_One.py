#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
from threading import Thread
import logging # this is used for logging


def Go_To_Crane():
    t = Thread(target=reset_arm)
    
    #Start the thread so that the attachment can go up and stay there    
    t.start()
    #reset motors
    d = 0 

    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)

    #turn
    Left_Motor.run_angle (1000,280)

    #Go straight
    while d < 750:
        Robot.drive(250,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
        logging.info(str(d))
    Robot.stop(0)
    wait(200)
    #reset motors
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    Right_Motor.run_angle (250,340)

    #stop
    Robot.stop(0)
    wait(200)
    #turn to get into angle for crane
    #Left_Motor.run_angle (1000,20)
    #wait(200)
    #Right_Motor.run_angle (-1000,6)

    #go to crane
    go_straight(2000,-1,"r",1,"d",1800,"l","w")
    go_straight(480,-1,"r",1,"d",100,"l","w")
    #Left_Motor.run_angle(-1000, 50)
    wait(2000)

    Med_Motor_2.run_angle(100,65)
    Med_Motor_2.run_angle(25,40)
    Med_Motor_2.run_angle(-100,90)
    wait(500)
    Med_Motor_2.run_angle(100,65)
    Med_Motor_2.run_angle(25,50)
    wait(250)  
    """ #lower the block
    Med_Motor_2.run_time(100,750)
    Med_Motor_2.run_time(-500,300)
    wait(1500)
    #come back
    Med_Motor_2.run_time(100,750)
    """
    #Robot.drive_time(-1000,0,2000)
    #Robot.drive_time(-20,45,18000)

    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    Left_Motor.run_angle(-1000,180)
    while d < 959:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
        logging.info(str(d))
    Robot.stop(0)

    Right_Motor.run_angle(-1000, 1000)

    d = 0 
    #Left_Motor.reset_angle(0)
    #Right_Motor.reset_angle(0)
    while d < 3000:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
        logging.info(str(d))
    Robot.stop(0)


def reset_arm():
    Med_Motor_2.run_time(-50,5000)
    Med_Motor_2.run_angle(100,5)
    Med_Motor_2.run_angle(50,50)