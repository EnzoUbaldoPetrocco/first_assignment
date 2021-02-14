#!/usr/bin/env python

import rospy
from my_assignment1.srv import randomService, randomServiceResponse
import random

#The aim of this script is get two values that describe an interval
#from the robot controller and give as response the values of the
# x and y which will represent the target for the controller

#function random simply generates a number between a min and
#a max value
def rndm(min, max):
	return random.randrange(min, max)

#Service Callback which generates two random coordinates
#The assignment wants them to belong to (-6.0, 6.0) interval.
def handleRandom(req): 
	x=rndm(req.min, req.max)
	y=rndm(req.min, req.max)
	print("\nI'm handling the random target")
	print("\nthe values are: "+ str(x) +", " + str(y))
	return randomServiceResponse(x, y)

#Initialization of the node and of the service
def main():
	print("\nLet's serve! I'm executing the main server.py")
	rospy.init_node("server")
	s = rospy.Service("server" , randomService, handleRandom)
	rospy.spin()

if __name__ == "__main__":
	main()
