#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
from threading import Thread
import logging # this is used for logging

def drop_blocks():
    logging.info("lifting blocks up")
    Med_Motor_1.run_time(50,2500)

    Med_Motor_1.run_time(-50,2500)

def Safety_Factor():
    logging.info("Run 4 - Going to Saftery Factor.")
    
    #define and set run variable for the thread control
    global run
    global run_back
    run = True
    t = Thread(target=lift_medium_motor) 
    #Start the thread so that the attachment can go up and stay there    
    t.start()
    #lift the back motor up

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

    #START MISSION TO DROP INNOVATION ACRCHITECTURE AND RED BLOCK IN RED CIRCLE
    #Go to the red circle
    Left_Motor.set_dc_settings(55,0)
    line_follower(350,-1,"r",1,"d",1250,"X","X")
    logging.info("....." + str(Right_Motor.angle()))
    #lift the back motor to release the red and the blue blocks
    run_back = True # This variable is for the thread that will hold the back motor up
    t_back = Thread(target=lift_back_motor) # set the thread so that when we lift the back motor it keep it up and doesn't fall down due to wait
    Med_Motor_1.run_time(-200,650) #lift back motor up
    t_back.start() # start the thread so that the back motor stays up
    #go forward to the turn
    wait(200)

    #END MISSION TO DROP INNOVATION ACRCHITECTURE AND RED BLOCK IN RED CIRCLE

    #START MISSION TO GO TO SAFETY FACTOR
    line_follower(40,-1,"r",1,"d",100,"X","X")
    #follow line slowly till the left sensor hits white line. This is the intersection of the two lines on the board
    #go_straight(75,-1,"r",1,"l",10,"l","b")
    
    line_follower(40,-1,"r",1,"l",50,"l","w")
    Left_Motor.set_dc_settings(100,0)

    #turn towards *North*
    Right_Motor.reset_angle(0)
    wait(100)
    #TURN NORTH
    Right_Motor.run_target(1000,200) #150 if we don't follow line

    #reset the motors and set d variable so that we can travel using robot.drive this is faster than the common function
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    # travel to the house
    while d < 520: #600 of we don't follow line
        Robot.drive(750,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    
    #straighten to face the house
    #For some reason this only works if we reset the motors
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    #Straighten to be at right angle to the house
    Right_Motor.run_angle(-500,60) #80 if we don't follow line
    #set the run variable as false so that the attachment can come down. This will end the thread
    run = False
    #move the attachment down
    Med_Motor_2.run_time(100,2000)
    #move forward for 1.5 seconds so that the robot goes and moves the blue stilts down
    Robot.drive_time(1000,0,1500)
    
    #pull back for 300 degrees so that the attachment comes loose
    go_straight(500,1,"r",-1,"d",300,"l","w")
    #COMPLETED THE  SAFETY FACTOR MISSION

    #START SWING MISSION
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


    #travel back towards beige circle
    while d < 1100:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    Robot.stop()
    wait(100)
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)

    #Turn to center in the beige circle
    Left_Motor.run_angle(1000,90)
   
    #go north a bit to make sure beige block falls in the circle!
    Robot.drive_time(-200,0,500)

    run_back = False
    #drop the block
    Med_Motor_1.run_time(100,2700)

    
    Do_Elevator()
    Go_To_Bridge()

def lift_medium_motor2():
    Med_Motor_1.run_angle(-200,180)

def lift_medium_motor():
    global run
    run = True
    logging.info("here")
    while run:
        Med_Motor_2.run(-50)
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
    logging.info("going to elevator")
    Robot.drive_time(1000,0,600)
    Med_Motor_2.run_time(-1000,500)
    #Left_Motor.run_angle(1000,-1000)
    t3 = Thread(target=lift_medium_motor2)
    #Start the thread so that the attachment can go up and stay there    
    t3.start()

    #reset the motors and the d varible
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0) 

    Left_Motor.run_angle(1000,250)
    Right_Motor.run_angle(1000,-200)

    #reset the motors and the d varible
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    
    #travel back towards elevator
    while d < 800:
        Robot.drive(-1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    Robot.stop()

    #reset the motors and the d varible
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    



def Go_To_Bridge(): 
    #reset the motors and the d varible
    d = 0 
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    
    #travel back towards elevator
    while d < 755:
        Robot.drive(1000,0)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        d = (l+r)/2
    Robot.stop()



    #go to black line
    Condition_Reflection = Left_Color_Sensor.reflection()
    while Condition_Reflection > 15:
        Robot.drive(100,0)
        Condition_Reflection = Left_Color_Sensor.reflection()



    d = 0
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)
    while d < 220:
        Left_Motor.run(100)
        Right_Motor.run(-100)
        d = abs(Left_Motor.angle())
    Condition_Reflection = Left_Color_Sensor.reflection()
    while Condition_Reflection > 15:
        Left_Motor.run(100)
        Right_Motor.run(-100)
        Condition_Reflection = Left_Color_Sensor.reflection()
    line_follower(1000,-1,"l",1,"d",1650,"X","X")