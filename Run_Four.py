#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
from threading import Thread
import logging # this is used for logging



def drop_blocks():
    logging.info("lifting blocks up")
    Med_Motor_1.run_time(50,2500)

    Med_Motor_1.run_time(-50,2500)

def Go_To_Swing():
    logging.info("Mission x - Going to Swing.")
    
    #define and set run variable for the thread control
    global run
    run = True
    t = Thread(target=lift_medium_motor)
    
    #Start the thread so that the attachment can go up and stay there    
    t.start()
    #lift the back motor up
    #star thread to keep the back motor up
    global run_back

    #turn North towards the black line
    Right_Motor.run_angle(500,270)
    #go to black line
    Condition_Reflection = Right_Color_Sensor.reflection()
    while Condition_Reflection > 20:
        Robot.drive(200,0)
        Condition_Reflection = Right_Color_Sensor.reflection()
    while Condition_Reflection < 35:
        Robot.drive(50,0)
        Condition_Reflection = Right_Color_Sensor.reflection()

    #Go to the turn at full speed-
    line_follower(2000,-1,"r",1,"d",1950,"X","X")
    run_back = True
    t_back = Thread(target=lift_back_motor)
    Med_Motor_1.run_time(-200,760)
    t_back.start()
    wait(300)
    line_follower(2000,-1,"r",1,"d",200,"X","X")
    #follow line slowly till the left sensor hits white
    line_follower(50,-1,"r",1,"l",60,"l","w")

    #turn *North*
    Right_Motor.run_angle(1000,360)
    
    #reset the motors and set d variable so that we can travel using robot.drive this is faster than the common function
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)

    while d < 1000:
        Robot.drive(1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    
    #straighten to face the house
    #For some reason this only works if we reset the motors
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    #**** THIS ANGLE IS FLAKY TEST MORE***********
    Right_Motor.run_angle(-100,60)
    #set the run variable as false so that the attachment can come down
    run = False
    #move the attachment down
    Med_Motor_2.run_time(100,2000)
    run = True
    t2 = Thread(target=down_medium_motor)
    t2.start
    #move forward for 2 seconds so that the robot goes and moves the blue stilts
    Robot.drive_time(300,0,2000)
    #Run the left motor so that the attachment completely goes in
    Left_Motor.run_angle(50,100)
    run = False
    
    #pull back for 300 degrees so that the attachment comes loose
    go_straight(500,1,"r",-1,"d",300,"l","w")


    
    #set the run variable as true so that we can lift the motor and the partial attachment up
    run = True
    #start the thread so that the attachment can go up
    t.start()
    #Turn towards the swing
    Right_Motor.run_angle(-1000,450)

    #reset the motors and the d variable
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    #move forward to knock the swing
    while d < 1300:
        Robot.drive(1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    
    #reset the motors and the d varible
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    
    #travel back towards elevator
    while d < 1900:
        Robot.drive(-700,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    Robot.stop()
    wait(150)
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    logging.info(str(Left_Motor.angle()))
    Left_Motor.run_angle(-1000,200)
    logging.info(str(Left_Motor.angle()))
   
    run_back = False
    Med_Motor_1.run_time(80,2500)
    Left_Motor.run_angle(1000,1000)
    Med_Motor_1.run_angle(-200,180)
    Do_Elevator()


def lift_medium_motor():
    global run
    while run:
        Med_Motor_2.run(-100)
    logging.info("Thread stopped.")

def lift_back_motor():
    global run_back
    while run_back:
        Med_Motor_1.run(-2)
    logging.info("Thread stopped.")

def down_medium_motor():
    global run
    while run:
        Med_Motor_2.run(50)
    logging.info("Thread stopped.")

def Do_Elevator():
    #reset the motors and the d varible
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    
    #travel back towards elevator
    while d < 1250:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    Robot.stop()

    #reset the motors and the d varible
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    
    #travel back towards elevator
    while d < 1250:
        Robot.drive(1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    Robot.stop()