#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
from threading import Thread
import logging # this is used for logging

def Go_To_Swing():
    logging.info("Mission x - Going to Swing.")
    global run
    run = True
    t = Thread(target=lift_medium_motor)
    t.start()
    #Go to the turn at full speed-

    line_follower(2000,-1,"r",1,"d",2450,"X","X")

    #follow line slowly till the left sensor hits white
    line_follower(50,-1,"r",1,"l",50,"l","w")


    Right_Motor.run_angle(1000,360)
    
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)

    while d < 1000:
        Robot.drive(1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    logging.info("done going straight")
    
    #go_straight(1000,-1,"r",1,"d",1000,"l","w")
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    Right_Motor.run_angle(-100,35)
    run = False
    Med_Motor_2.run_time(100,2000)
    Robot.drive_time(300,0,2000)
    #go_straight(250,-1,"r",1,"d",1200,"l","w")
    Left_Motor.run_angle(50,100)
    go_straight(50,1,"r",-1,"d",400,"l","w")
    go_straight(2000,1,"r",-1,"d",4500,"l","w")
    #multithread for medium motor to go down so it does not hit the tree




def lift_medium_motor():
    global run
    while run:
        Med_Motor_2.run(-100)
    logging.info("Thread stopped.")