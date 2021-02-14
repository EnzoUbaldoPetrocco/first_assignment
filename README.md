
# The first assignment

## Introduction
This project involves the creation of two nodes within a package.
The nodes are written in python and comunicate each other through 'randomService.srv' message described in srv folder.
'randomService.srv' request is composed by a pair of float32 variables that tell the server the interval within which the two random coordinates must be; the response contains the two coordinates.

Both nodes are contained inside scripts folder.
- '/robot_controller' controls the robot behavior in the way it can reach the target, if the target is reached calls again the server for a new position.
- '/Server' receive the request for a new target and sends the random target.
(More information in docs folder)

## Computational Graph






## Considerations
This program contains some important semplifications:
-The simulation is a 2D simulation
-The robot is a non-holonomic robot
-The target is reached indipendentely from the orientation

So it is sufficient to set the 2D velocity /cmd_vel, proportional to the distance vector between the corrent position (always updated thanks to Odometry) and the target position (given by Server).
The proportional constant is set experimentaly, until an upper bound which guarantees that the robot doens't pass over the target and must go back to reach it.

## Installation
Follow the guide for installing Ros (melodic version)
Also is suggested to install python.

Then it must be installed stage_ros with the command:
```shellscript
sudo apt-get install ros-<your_ros_version>-stage-ros
```

## How to run it
Now, let's follow these simple step which will let the user to launch the program:

Open the first terminal

```shellscript
roscore &
```


```shellscript
catkin_make
```


```shellscript
rosrun stage_ros stageros $(rospack find assignment1)/world/exercise.world
```


Don't close this terminal and open the second one

```shellscript
rosrun my_assignment1 server.py
```


Don't close this terminal and open the third one
	
	
```shellscript
rosrun my_assignment robot_behavior.py
```


Then, the 2D-robot should move, a 2D environment is opened and:
-if you have a problem with the first terminal, try to check if ros is correctely installed and if stage_ros is correctely installed
-the second terminal should print on the screen: 'Let's serve! I'm executing the main server.py' and then advertise the user every time it is called which is the new target
-the third terminal print on the screen: 'Let's control! I'm in the main function of robot_behavior.py' and then just tell if the target is reached or not and the next target when the target is reached.


















