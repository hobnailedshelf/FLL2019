#!/usr/bin/env pybricks-micropython
from Initialize import *
from Common_Functions import * # import all the main functions
import logging # this is used for logging

#def Go_To_Tree():   
#   logging.info("Starting of the tree mission.")
#  go_straight(300,-1,"l",1,"l",35,"l","b")
# logging.info("reached black line.")
#    line_follower(100,-1,"l",1,"d",720,"X","X")
#    go_straight(300,-1,"r",1,"d",1200,"x","x")
#    go_straight(50,-1,"r",1,"d",400,"x","x")
#    wait(5000)
    #go_straight(1000,-1,"r",-1,"d",2500,"x","x")
    #go_straight(300,-1,"r",1,"l",5,"r","w")
    #wait(5)
    #go_straight(50,-1,"r",1,"d",150,"l","w")
    #wait(5)
    #go_straight(300,1,"r",-1,"d",3000,"l","w")

# Testing with Medium Motor

def Go_To_Tree():   
    logging.info("Starting of the tree mission.")
    go_straight(300,-1,"l",1,"l",35,"l","b")
    Med_Motor_1.run_time(90,1400)
    