#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
import logging # this is used for logging


#line_follower (m_speed, Direction, WhichSensor, Forward_BackWard,Condition,Target_Condition,Condition_Sensor, What_ColReflect):
#m_speed - Maximum Speed
#Direction - Direction that therobot has to turn for correction -1 or +1
#WhichSensor - Sensor that follows the line l for leftsensor and r for rightsensor and b for backsensor
#Forward_Backward - Direction of the robot movement 1 for forward and -1 for backward
#Condition - d for distance or l for lightsensor. This flag will let the robot know when to stop, after travelling a distance or after the sensor detects target value
#Target_Condition - This will be the rotation angles or the target light reflection that it has to reach
#ConditionSensor - Which sensor should be detecting the Target_Condition
#What_ColReflect - w - white, b - black

def Go_To_Crane():
    Left_Motor.run_angle (200,370)
    go_straight(100,-1,"r",1,"d",800,"l","w")
    Right_Motor.run_angle (200,390)
    go_straight(2000,-1,"r",1,"d",1400,"l","w")
    go_straight(80,-1,"r",1,"d",300,"l","w")
    wait(2000)
    Med_Motor_2.run_time(90,1400)
    Med_Motor_2.run_time(-90,1200)
    wait(3000)
    Med_Motor_2.run_time(100,1500)
    wait(500)
    #Coming Back
    go_straight(2000,1,"r",-1,"d",1440,"l","w")
    Left_Motor.run_angle (800,720)
    go_straight(2000,1,"r",-1,"d",2700,"l","w")
    Left_Motor.run_angle (-800,720)


def Go_To_Crane_1():
    logging.info("Mission 1 - Going to Crane.")
    #go_straight_distance(0,0,0,0)
    #Med_Motor_2.run_time(-100,500)
    #Med_Motor_2.run_time(100,200)
    go_straight(2000,-1,"r",1,"d",2300,"l","w")
    go_straight(2000,-1,"r",1,"d",380,"l","w")
    wait(1000)
    go_straight(40,-1,"r",1,"d",100,"l","w")
    go_straight(40,1,"r",-1,"d",80,"l","w")
    Med_Motor_2.run_time(100,1200)
    Med_Motor_2.run_time(-100,1200)
    wait(2000)
    Med_Motor_2.run_time(100,1500)
    wait(500)
    go_straight(2000,1,"r",-1,"d",2450,"l","w")



    logging.info("Mission 1 - Reached Crane")
    #Do Something here
    logging.info("Mission 1 - Pushed Blue Block")




