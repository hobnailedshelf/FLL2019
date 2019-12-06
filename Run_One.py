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
    #Go to the black line
    go_straight(150,-1,"r",1,"l",15,"r","b")
    #Reduce the torque of the right (large) motor to make sure it does not shake.
    Right_Motor.set_dc_settings(55,0)
    #Follow the black line
    go_straight(50,-1,"r",1,"l",35,"r","w")
    #make torque full again
    Right_Motor.set_dc_settings(100,0)
    #keep following black line
    line_follower(50,-1,"r",1,"d",420,"X","X")
    #turn to fface crane
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    while d < 240:
        #Left_Motor.run(-100)
        Right_Motor.run(150)
        d = abs(Right_Motor.angle())
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    #go straight distance to go close to crane
    go_straight(150,-1,"r",1,"d",500,"r","w")
    #go straight to reach the white line before the crane
    go_straight(150,-1,"r",1,"l",15,"r","w")
    #travel distance to get to the crane
    go_straight(150,-1,"r",1,"d",70,"r","b")
    go_straight(50,-1,"r",1,"d",70,"r","w")
    wait(100)
    Robot.drive
    #move forward for 2 seconds to make sure that the robot is aligned to the crane
    Robot.drive_time(25,0, 1500)
    #turn left for .5 seconds to make sure the robot is aligned
    Left_Motor.run_time(50, 500)
    #wait 1.5 seconds to make sure that the block stops moving
    wait(1200)
    lift_arm()

    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    
    #go back to home area
    
    #Come back before turn back from crane
    Robot.drive_time(-1000,0,800)
    Robot.drive_time(-1000,650,2200)
    Robot.drive_time(-1000,0,50)
    Robot.stop(0)
    Left_Motor.reset_angle(0)
    Left_Motor.run_angle(-1000,750)


def reset_arm():
    #arm is moved down. it goes down until it hits the attachment. 40 is the maximum torque
    #run_until_stalled(speed, stop_type=Stop.COAST, duty_limit=default)
    #stop_type (Stop) – Whether to coast, brake, or hold after coming to a standstill (Default: Stop.COAST).
    Med_Motor_2.run_until_stalled(50,0,35)


def lift_arm():
    i=1
    #We try the arm at increasing degrees. 55 degrees, 60 degrees etc. till 85 degrees. this way we reduce the number of times it fails. 
    while i < 6:
        ang = 43 + i*5 
        Med_Motor_2.run_angle(-1000,ang)
        Med_Motor_2.run_angle(1000,ang)
        i = i + 1
