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
    Left_Motor.run_angle(100, 25)
    wait(200)

    lift_arm()  


    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    #Left_Motor.run_angle(-1000,160)
    
    #go back to home area
    Robot.drive_time(-1000,650,2500)
    Robot.drive_time(-1000,0,550)
    Robot.stop(0)
    Left_Motor.reset_angle(0)
    Left_Motor.run_angle(-1000,800)
    #Left_Motor.reset_angle(0)
    #Left_Motor.run_angle(-1000,400)
   


def Go_To_Crane_3():
    t = Thread(target=reset_arm)
    
    #Start the thread so that the attachment can go up and stay there    
    t.start()
    #reset motors

    #turn
    go_straight(500,-1,"r",1,"d",700,"l","w")
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    d=0
    while d < 140:
        Left_Motor.run(150)
        Right_Motor.run(-150)
        d = abs(Left_Motor.angle())


    go_straight(300,-1,"r",1,"d",450,"l","w")

    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    d=0
    while d < 90:
        Right_Motor.run(150)
        Left_Motor.run(-150)
        d = abs(Right_Motor.angle())
    #stop

    wait(200)


    #go to crane
    go_straight(2000,-1,"r",1,"d",200,"l","w")
    go_straight(50,-1,"r",1,"d",100,"l","w")
    Left_Motor.run_angle(100, 15)
    wait(200)

    lift_arm()  


    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    #Left_Motor.run_angle(-1000,160)
    
    #go back to home area
    Robot.drive_time(-1000,0,1000)
    Robot.drive_time(-1000,799,500)
    Left_Motor.run_angle(1000,190)

    Robot.drive_time(-1000,0,1555)

    #Left_Motor.reset_angle(0)
    #Left_Motor.run_angle(-1000,400)


def lift_arm():
    i=1
    while i < 6:
        ang = 60 + i*5 
        Med_Motor_2.run_angle(1000,ang)
        Med_Motor_2.run_angle(-1000,ang)
        i = i + 1


def reset_arm():
    Med_Motor_2.run_until_stalled(-50,0,40)
