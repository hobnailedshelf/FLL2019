#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, UltrasonicSensor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color
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
    #####Initialization###################################################################################################################
    logging.info("####################################")

    logging.info("Initializing the robot.")
    
    #Define Global Variables
    global Left_Motor
    global Right_Motor
    global Med_Motor_1
    global Med_Motor_2
    global Right_Color_Sensor
    global Left_Color_Sensor
    global Back_Color_Sensor
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

    #Initialize Sensors
    Left_Color_Sensor = ColorSensor(Port.S2)
    Right_Color_Sensor = ColorSensor(Port.S3)
    #Back_Color_Sensor = ColorSensor(Port.S4)
    #Gyro = ColorSensor(Port.S1)
    #Touch_Sensor = ColorSensor(Port.S4)

    #Set Wheel Diameters and Axle Length
    WheelDiameter = 55 #42 # diameter of the wheel in mm
    AxleLength = 128 #112 # distance between the middle of the two wheels in mm

    #####The drivebase function helps to drive the robot. This is initialization of the drivebase 
    Robot = DriveBase(Left_Motor, Right_Motor, WheelDiameter, AxleLength)

    #####we can collect important information in a log file. this information will help us figure out things like speed, angle, etc. at various points of the run
    #####name of the log file is log.txt
    #####this file is stored on the ev3 brick, you have to download the file to view it


    #reset the gyro angle to zero at the beginning of the program
    #gyro.reset_angle(0)

    Max_Speed = 70
    Robot.stop(0)

    brick.sound.beep()
    logging.info("Initializing complete.")
    logging.info("####################################")
    ##### initialization complete ###################################################################################################################