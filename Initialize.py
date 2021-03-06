#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, UltrasonicSensor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color, Button
from pybricks.tools import wait
from pybricks.robotics import DriveBase

import logging
Left_Motor = None
Right_Motor = None
Med_Motor_1 = None
Med_Motor_2 = None
Right_Color_Sensor = None
Left_Color_Sensor = None
Gyro = None
Touch_Sensor = None
Robot = None
Max_Speed = None
Target_Reflection = None
def init_robot():
    #####Initialization###########################################################################
    logging.info("####################################")

    logging.info("Initializing the robot.")
    
    #Define Global Variables
    global Left_Motor
    global Right_Motor
    global Med_Motor_1
    global Med_Motor_2
    global Right_Color_Sensor
    global Left_Color_Sensor
    global Gyro
    global Touch_Sensor
    global Robot
    global Max_Speed
    global Target_Reflection 
    Target_Reflection = 35
    
    #initialize Motors
    Left_Motor = Motor(Port.C)
    Right_Motor = Motor(Port.D)
    Med_Motor_1 = Motor(Port.A)
    Med_Motor_2 = Motor(Port.B)
    #Left_Motor.set_run_settings(1000, 100)
    #Right_Motor.set_run_settings(1000, 100)

    #Initialize Sensors
    Left_Color_Sensor = ColorSensor(Port.S2)
    Right_Color_Sensor = ColorSensor(Port.S3)


    #Set Wheel Diameters and Axle Length
    WheelDiameter = 55 #42 # diameter of the wheel in mm
    AxleLength = 128 #112 # distance between the middle of the two wheels in mm

    #####The drivebase function helps to drive the robot. This is initialization of the drivebase 
    Robot = DriveBase(Left_Motor, Right_Motor, WheelDiameter, AxleLength)

    Max_Speed = 70
    Robot.stop(0)

    brick.sound.file('/home/robot/FLL2019/boing_spring.wav')

    logging.info("Initializing complete.")
    logging.info("####################################")
    ##### initialization complete ##############################################################################