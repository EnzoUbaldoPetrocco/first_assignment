#!/usr/bin/env python

#This is a ROS node, which should have:
#	-a publisher, which will publish the robot speed (cmd_vel)
#	-a subscriber, which will subscribe to the position of the robot(odometry)
#	-a client which will receive the random target at the beginning and every time the robot reaches the coordinate

#imports needed
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from my_assignment1.srv import randomService, randomServiceResponse

#Here I initialize the publisher to the cmd_vel
pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)
#client to randomService and its response
client= rospy.ServiceProxy('server', randomService)
response = client(min=-6.0, max=6.0)
x=response.x
y=response.y

#Initialization of the node and the subscriber to the /odom topic
def main():
	print("\nLet's control! I'm in the main function of robot_behavior.py")
	rospy.init_node('robot_behavior')
	sub = rospy.Subscriber("odom", Odometry, positionCallback)
	rospy.spin()
		
#Here i define the Callback referred to the odom topic
def positionCallback(msg):
	global client
	global x
	global y
	
#Now I have to know if the position is reached:
#	-if yes: call the service which will give newer coordinates
#	-if not: set the velocity
	if abs(pow(x- msg.pose.pose.position.x, 2)+pow(y-msg.pose.pose.position.y, 2))<=0.1:
		print("target reached!")
		response = client(min=-6.0, max=6.0)
		x=response.x
		y=response.y
		print(str(x) + " value of x " + str(y) + " value of y")
		
	else:
		print("target not reached")
		k=5
		pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)
		vel_x=k * (x - msg.pose.pose.position.x)
		vel_y=k * (y - msg.pose.pose.position.y)
		twist= Twist()
		twist.linear.x=vel_x
		twist.linear.y=vel_y
		pub.publish(twist)
		

	

if __name__ == "__main__":
	main()	



















