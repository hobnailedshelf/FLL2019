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
    #reset motors
    d = 0 

    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)

    #turn
    Left_Motor.run_angle (250,280)

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
    go_straight(2000,-1,"r",1,"d",1795,"l","w")
    go_straight(50,-1,"r",1,"d",90,"l","w")
    wait(2000)
    
    #lower the block
    Med_Motor_2.run_time(90,950)
    Med_Motor_2.run_time(-100,500)
    wait(2000)
    #come back
    Med_Motor_2.run_time(100,1500)
    wait(500)
    Robot.drive_time(-1000,0,2000)
    Robot.drive_time(-20,45,18000)
    
    """#Coming Back
    go_straight(2000,1,"r",-1,"d",720,"l","w")
    Right_Motor.run_angle (400,500)
    go_straight(2000,-1,"r",1,"d",800,"l","w")
    Right_Motor.run_angle (-300,650)
    #Right_Motor.run_angle (1000,200)
    Robot.drive_time(-800, 0, 2000)
    #Right_Motor.run_angle (1000000000,200)"""