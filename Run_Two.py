#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
import logging # this is used for logging

def Go_To_Tree():
    logging.info("Starting of the tree mission.")
    #go_straight(2000,1,"l",-1,"d",800,"l","b")
    go_straight(150,1,"l",-1,"l",35,"l","b")
    Robot.stop(0)

    logging.info("here")
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0) 
    Right_Motor.run_angle(-200, 650)


    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    while d < 1600:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
        logging.info(str(d))
    Robot.stop(0)
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    logging.info("out of the loop")
    wait(600)
    Med_Motor_1.run_time(75,100)
    Med_Motor_1.run_time(-1000,400)
    Robot.drive_time(1000, 0, 4000)
    Med_Motor_1.run_time(-1000,500)

def Go_To_Tree2():
    logging.info("Starting of the tree mission.")
    #go_straight(2000,1,"l",-1,"d",800,"l","b")
    go_straight(150,1,"l",-1,"l",35,"l","b")
    Right_Motor.run_angle(-150,515)
    go_straight(2000,1,"l",-1,"d",2000,"x","x")
    Med_Motor_1.run_time(-75,100)
    Med_Motor_1.run_time(100,400)


def move_stack():
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    go_straight(1000,-1,"l",1,"d",1425,"l","b")
    Robot.drive_time(-1000, 800, 1000)
    Robot.drive_time(-1000, 0, 1500)


def move_stack_tree():
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    go_straight(1000,-1,"l",1,"d",1200,"l","b")
    Robot.drive_time(-1000, 800, 760)
    Robot.drive_time(-1000, 0,2700)


def Go_To_Tree_2():
    logging.info("Starting of the tree mission to smalll branch.")
    # Go to the Black line
    go_straight(150,1,"l",-1,"l",25,"l","b")
    Robot.stop(0)

    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    while d < 340:
        Robot.drive(100,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
        logging.info(str(d))
    Robot.stop(0)


    logging.info("here")
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0) 
    #Turn to face the tree
    Right_Motor.run_angle(-1000, 400)
    Med_Motor_1.run_time(120,550)

    #Move forward to the tree
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    while d < 1850:
        #move slowly first so that the bat doesn't fall off
        if d < 201:
            Robot.drive(-200,0)
        else:
            Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
        logging.info(str(d))
    Robot.stop(0)
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    logging.info("out of the loop")
    wait(600)
    #Move the blue block down
    Med_Motor_1.run_time(75,1500)
    #lift the art to move 
    Med_Motor_1.run_time(-100,400)
    Robot.drive_time(1000, 0, 4000)
    Med_Motor_1.run_time(-1000,500)

def Go_To_Tree_3():
    logging.info("Starting of the tree mission to small branch.")
    #Med_Motor_1.run_time(200,350)
    # Go to the Black line
    go_straight(1000,1,"l",-1,"d",3300,"l","b")

    wait(600)
    #Move the blue block down
    Med_Motor_1.run_time(900,1500)
    #lift the arm to move 
    Med_Motor_1.run_time(-1000,400)

    #come back
    Robot.drive_time(1000, 0, 4000)
