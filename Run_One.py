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
    Left_Motor.run_target (250,280)

    #Go straight
    while d < 1050:
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
    Right_Motor.run_target (250,320)

    #stop
    Robot.stop(0)
    wait(200)


    #go to crane
    go_straight(2000,-1,"r",1,"d",1500,"l","w")
    go_straight(50,-1,"r",1,"d",300,"l","w")
    Left_Motor.run_angle(100, 50)
    wait(200)

    lift_arm()  


    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    Left_Motor.run_angle(-1000,500)

    Robot.drive_time(-1000,650,7000)
    """
    #TESTING CODE
    Left_Motor.run_angle(-1000,500)
    while d < 400:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    Robot.stop(0)
    #Med_Motor_2.run_angle(1000,150)

    Left_Motor.run_angle(1000,400)
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)    
    while d < 600:
        Robot.drive(1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    Robot.stop(0)

    go_straight(50,-1,"l",1,"l",60,"l","w")
    Right_Motor.run_angle(500,400)
    Right_Motor.run_angle(-500,650)
   
    wait(200)

    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    
    while d < 50:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    Robot.stop(0)
    Robot.drive_time(500,0,500)
    Robot.drive_time(-700,300,5000)
    #TESTING CODE


    
    Left_Motor.run_angle(-1000,180)
    while d < 409:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    Robot.stop(0)

    Right_Motor.run_angle(-1000, 1400)

    d = 0 
    #Left_Motor.reset_angle(0)
    #Right_Motor.reset_angle(0)
    while d < 5000:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
        logging.info(str(d))
    Robot.stop(0)
    """

def lift_arm():
    i=1
    while i < 6:
        ang = 60 + i*5 
        Med_Motor_2.run_angle(1000,ang)
        Med_Motor_2.run_angle(-1000,ang)
        i = i + 1


def reset_arm():
    Med_Motor_2.run_until_stalled(-50,0,40)
