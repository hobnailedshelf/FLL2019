#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
from threading import Thread
import logging # this is used for logging


def Go_To_Crane():
    #define thread so that we can move the armm down in parallel down to the attachment
    t = Thread(target=reset_arm)
    
    #Start the thread so that the attachment can go up and stay there    
    t.start()
    #reset motors
    d = 0 

    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)

    #turn
    Left_Motor.run_target (250,100)

    #Go straight
    while d < 1200:
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

    #turn to face crane
    Right_Motor.run_target (250, 85)

    #stop
    Robot.stop(0)
    wait(200)


    #go to crane
    go_straight(2000,-1,"r",1,"d",350,"l","w")
    go_straight(50,-1,"r",1,"d",100,"l","w")
    Left_Motor.run_angle(110, 40)
    wait(200)

    lift_arm()  


    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    
    #go back to home area
    Robot.drive_time(-1000,650,2500)
    Robot.drive_time(-1000,0,550)
    Robot.stop(0)
    Left_Motor.reset_angle(0)
    Left_Motor.run_angle(-1000,800)




def lift_arm():
    i=1
    #We try the arm at increasing degrees. 55 degrees, 60 degrees etc. till 85 degrees. this way we reduce the number of times it fails. 
    while i < 8:
        ang = 50 + i*5 
        Med_Motor_2.run_angle(1000,ang)
        Med_Motor_2.run_angle(-1000,ang)
        i = i + 1


def reset_arm():
    #arm is moved down. it goes down until it hits the attachment. 40 is the maximum torque
    #run_until_stalled(speed, stop_type=Stop.COAST, duty_limit=default)
    #stop_type (Stop) – Whether to coast, brake, or hold after coming to a standstill (Default: Stop.COAST).
    Med_Motor_2.run_until_stalled(-50,0,40)