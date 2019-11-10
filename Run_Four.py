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
    Right_Motor.reset_angle(0)
  
    #turn North towards the black line
    Right_Motor.run_target(300,165)
    logging.info("completed run taret")
    #go to black line
    Condition_Reflection = Right_Color_Sensor.reflection()
    while Condition_Reflection > 15:
        Robot.drive(200,0)
        Condition_Reflection = Right_Color_Sensor.reflection()
    #move forward to get to the half black and half white
    while Condition_Reflection < 35:
        Robot.drive(50,0)
        Condition_Reflection = Right_Color_Sensor.reflection()

    #Go to the red circle
    line_follower(2000,-1,"r",1,"d",1250,"X","X")
    #lift the back motor to release the red and the blue blocks
    run_back = True # This variable is for the thread
    t_back = Thread(target=lift_back_motor) # set the thread so that when we lift the back motor it keep it up and doesn't fall down due to wait
    Med_Motor_1.run_time(-200,650) #lift back motor up
    t_back.start() # start the thread so that the back motor stays up
    #go forward to the turn
    wait(200)
    line_follower(200,-1,"r",1,"d",100,"X","X")
    #follow line slowly till the left sensor hits white line. This is the intersection of the two lines on the board
    go_straight(100,-1,"r",1,"l",50,"l","w")
    #line_follower(40,-1,"r",1,"l",50,"l","w")
    #turn towards *North*
    Right_Motor.reset_angle(0)
    Right_Motor.run_target(1000,150)

    #reset the motors and set d variable so that we can travel using robot.drive this is faster than the common function
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)

    while d < 600:
        Robot.drive(1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    
    #straighten to face the house
    #For some reason this only works if we reset the motors
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    #**** THIS ANGLE IS FLAKY TEST MORE***********
    Right_Motor.run_angle(-1000,80)
    #set the run variable as false so that the attachment can come down
    run = False
    #move the attachment down
    Med_Motor_2.run_time(100,2000)
    run = True
    t2 = Thread(target=down_medium_motor)
    t2.start
    #move forward for 2 seconds so that the robot goes and moves the blue stilts
    Robot.drive_time(1000,0,1500)
    #Run the left motor so that the attachment completely goes in
    #Left_Motor.run_angle(50,100)
    run = False
    
    #pull back for 300 degrees so that the attachment comes loose
    go_straight(500,1,"r",-1,"d",300,"l","w")
    

    
    #set the run variable as true so that we can lift the motor and the partial attachment up
    run = True
    #start the thread so that the attachment can go up
    t.start()
    #Turn towards the swing
    Right_Motor.reset_angle(0)
    Right_Motor.run_target(1000,-235)
    #reset the motors and the d variable
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    #move forward to knock the swing
    while d < 650:
        Robot.drive(1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    
    #reset the motors and the d varible
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)




    #travel back towards elevator
    while d < 1200:
        Robot.drive(-700,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    Robot.stop()
    wait(3000)
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    logging.info(str(Left_Motor.angle()))
    Left_Motor.run_angle(1000,250)
    logging.info(str(Left_Motor.angle()))
   
    run_back = False
    Med_Motor_1.run_time(80,2500)
    Left_Motor.run_angle(1000,-1000)
    t3 = Thread(target=lift_medium_motor2)
    

    #Start the thread so that the attachment can go up and stay there    
    t3.start()
    Do_Elevator()
    Go_To_Bridge()

def lift_medium_motor2():
    Med_Motor_1.run_angle(-200,180)

def lift_medium_motor():
    global run
    while run:
        Med_Motor_2.run(-25)
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
    while d < 1300:
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
    while d < 1100:
        Robot.drive(1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    Robot.stop()

def Go_To_Bridge():
    Condition_Reflection = Left_Color_Sensor.reflection()
    logging.info(str(Condition_Reflection))
    while Condition_Reflection > 8:
        Robot.drive(200,0)
        Condition_Reflection =  Left_Color_Sensor.reflection()
    while Condition_Reflection > 20:
        Robot.drive(50,0)
        Condition_Reflection =  Left_Color_Sensor.reflection()
    Condition_Reflection =  Right_Color_Sensor.reflection()
    while Condition_Reflection > 20:
        Right_Motor.run(50)
        Condition_Reflection =  Right_Color_Sensor.reflection()
    Condition_Reflection =  Left_Color_Sensor.reflection()
    while Condition_Reflection > 20:
        Left_Motor.run(50)
        Condition_Reflection =  Left_Color_Sensor.reflection()
    Right_Motor.reset_angle(0)
    Left_Motor.reset_angle(0)
    Right_Motor.run_angle(100,270)
