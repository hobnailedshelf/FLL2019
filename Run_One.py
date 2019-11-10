#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
from threading import Thread
import logging # this is used for logging


def Go_To_Crane_2():
    t = Thread(target=reset_arm)
    
    #Start the thread so that the attachment can go up and stay there    
    t.start()
    #reset motors
    d = 0 

    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)

    #turn
    Left_Motor.run_target (250,90)

    #Go straight
    while d < 1100:
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
    Right_Motor.run_target (250, 55)

    #stop
    Robot.stop(0)
    wait(200)


    #go to crane
    go_straight(2000,-1,"r",1,"d",500,"l","w")
    go_straight(50,-1,"r",1,"d",100,"l","w")
    Left_Motor.run_angle(100, 15)
    wait(200)

    lift_arm()  


    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    Left_Motor.run_angle(-1000,160)

    Robot.drive_time(-1000,675,2500)
    Robot.drive_time(-1000,0,1500)

   
def lift_arm():
    i=1
    while i < 6:
        ang = 60 + i*5 
        Med_Motor_2.run_angle(1000,ang)
        Med_Motor_2.run_angle(-1000,ang)
        i = i + 1


def reset_arm():
    Med_Motor_2.run_until_stalled(-50,0,40)
