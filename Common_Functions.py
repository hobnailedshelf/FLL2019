from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, UltrasonicSensor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
import logging
from Initialize import *



def line_follower (m_speed, Direction, WhichSensor, Forward_BackWard,Condition,Target_Condition,Condition_Sensor, What_ColReflect):
    #m_speed - Maximum Speed
    #Direction - Direction that the robot has to turn for correction -1 or +1
    #WhichSensor - Sensor that follows the line l for leftsensor and r for rightsensor and b for backsensor
    #Forward_Backward - Direction of the robot movement 1 for forward and -1 for backward
    #Condition - d for distance or l for lightsensor. This flag will let the robot know when to stop, after travelling a distance or after the sensor detects target value
    #Target_Condition - This will be the rotation angles or the target light reflection that it has to reach
    #ConditionSensor - Which sensor should be detecting the Target_Condition
    #What_ColReflect - w - white, b - black
    #Distance is total rotation of the wheel (360*number of rotations)
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)  
    logging.info("Travelling on black line.")
    speed=10
    Current_Distance = 0.0
    #logging.info(str(Current_Distance))
    Light_Reflection = None
    Condition_Reflection = None
    last_error = 0
    integral = 0
    #ki, kp, and kd are constants that are dependent on robot. we selected these after testing the robot.
    kp = 1.5 #1.5
    ki = .15 #.15
    kd = .1 #.1
    last_error = 0
    flag = True
    Robot.drive(speed,0)

    while flag:

        #accelerate to the maximum speed 
        if speed < m_speed:    
            speed = speed + 2
        if WhichSensor == "l":
            Light_Reflection = Left_Color_Sensor.reflection()
        else:
            Light_Reflection = Right_Color_Sensor.reflection()
    
        #Calculate PID
        error = Target_Reflection - Light_Reflection
        p_gain = error*kp
        integral = integral + error
        i_gain = integral*ki
        Derivative = error - last_error
        d_gain = Derivative*kd

        PID = p_gain + i_gain + d_gain
        #drive robot with the PID Calculation. Multiply by direction to calculate which way to turn.
        Robot.drive(speed*Forward_BackWard,PID*Direction)

        last_error = error
        wait(1)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        #calculate distance
        Current_Distance = (l+r)/2
        #check if the robot has to stop for light reflection or distance
        if Condition_Sensor == "l":
            Condition_Reflection = Left_Color_Sensor.reflection()
        else:
            Condition_Reflection = Right_Color_Sensor.reflection()

        #if it is distance see if it has reached the distance
        if Condition == "d":
            if Current_Distance >= Target_Condition:
                flag = False
        else:
            if What_ColReflect == "w":
                if Condition_Reflection >= Target_Condition:
                    flag = False
            else:
                if Condition_Reflection <= Target_Condition:
                    flag = False                
    Robot.stop(0)

def go_straight (m_speed, Direction, WhichSensor, Forward_BackWard,Condition,Target_Condition,Condition_Sensor, What_ColReflect):
    #m_speed - Maximum Speed
    #Direction - Direction that therobot has to turn for correction -1 or +1
    #WhichSensor - Sensor that follows the line l for leftsensor and r for rightsensor and b for backsensor
    #Forward_Backward - Direction of the robot movement 1 for forward and -1 for backward
    #Condition - d for distance or l for lightsensor. This flag will let the robot know when to stop, after travelling a distance or after the sensor detects target value
    #Target_Condition - This will be the rotation angles or the target light reflection that it has to reach
    #ConditionSensor - Which sensor should be detecting the Target_Condition
    #What_ColReflect - w - white, b - black
    #Distance is total rotation of the wheel (360*number of rotations)
    Left_Motor.reset_angle(0)
    Right_Motor.reset_angle(0)  
    logging.info("Travelling straight.")
    speed=30
    Current_Distance = 0.0
    #logging.info(str(Current_Distance))
    Light_Reflection = None
    Condition_Reflection = None
    last_error = 0
    integral = 0
    #ki, kp, and kd are constants that are dependent on robot. we selected these after testing the robot.
    kp = .8 #1.5
    ki = .15 #.15
    kd = .1 #.1
    last_error = 0
    flag = True
    Robot.drive(speed,0)

    while flag:

        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        #accelerate
        if speed < m_speed:    
            speed = speed + 5 #originally 2
        if WhichSensor == "l":
            Light_Reflection = Left_Color_Sensor.reflection()
        else:
            Light_Reflection = Right_Color_Sensor.reflection()

        #calculate PID
        error = l - r 
        p_gain = error*kp
        integral = integral + error
        i_gain = integral*ki
        Derivative = error - last_error
        d_gain = Derivative*kd

        PID = p_gain + i_gain + d_gain
        Robot.drive(speed*Forward_BackWard,PID*Direction)

        last_error = error
        wait(1)
        l = abs(Left_Motor.angle())
        r = abs(Right_Motor.angle())
        Current_Distance = (l+r)/2
        #check if it should stop at sensor or distance
        if Condition_Sensor == "l":
            Condition_Reflection = Left_Color_Sensor.reflection()
        else:
            Condition_Reflection = Right_Color_Sensor.reflection()
        # if it stops at distance check if it has reached the target distance
        if Condition == "d":
            if Target_Condition - Current_Distance < 50:
                speed = 30
            if Current_Distance >= Target_Condition:
                flag = False
            logging.info(str(l)+" - "+str(r))

        else:
            if What_ColReflect == "w":
                if Condition_Reflection >= Target_Condition:
                    flag = False
            else:
                if Condition_Reflection <= Target_Condition:
                    flag = False                
    Robot.stop(0)
    logging.info("done with going straight")

   