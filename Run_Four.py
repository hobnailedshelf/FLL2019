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

    Right_Motor.run_angle(100,450)
    Left_Motor.run_angle(100,50)
    Right_Motor.run_angle(-100,20)
    Left_Motor.run_angle(100,40)
    Right_Motor.run_angle(-100,40)
    Right_Motor.run_angle(-100,15)

    go_straight(500,-1,"r",1,"d",840,"l","w")
    
    Right_Motor.run_angle(-100,35)
    Left_Motor.run_angle(100,130)
    run = False
    Med_Motor_2.run_time(100,2000)
    go_straight(150,-1,"r",1,"d",900,"l","w")
    Left_Motor.run_angle(50,100)
    go_straight(50,1,"r",-1,"d",400,"l","w")
    go_straight(2000,1,"r",-1,"d",4500,"l","w")




def lift_medium_motor():
    global run
    while run:
        Med_Motor_2.run(-100)
    logging.info("Thread stopped.")