#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, UltrasonicSensor, TouchSensor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Play a sound.
brick.sound.beep()

# Initialize two motors and a drive base
left = Motor(Port.C)
right = Motor(Port.D)
robot = DriveBase(left, right, 28, 121.6)

#right.run_time(100,100000)
Color = ColorSensor(Port.S3)
touch = TouchSensor(Port.S2)
robot.drive(-1000,0)
#print(touch.pressed())
while not touch.pressed():
    wait(1)
robot.stop(0)

robot.drive(1000,0)
while Color.color() != Color.BROWN:
    wait(1)
robot.stop(0)