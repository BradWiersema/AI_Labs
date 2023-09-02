#!/usr/bin/env python3
import rospy
import numpy
from geometry_msgs.msg import Twist

rospy.init_node('square', anonymous=True)
pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(10) # 10hz
forwardCounter = 0
turnCounter = 0

print('Starting square . . .')

# TODO: Modify the code below so that the robot moves in a square

while not rospy.is_shutdown():

    twist = Twist()
    """
    twist.linear.x = 0.5
    twist.angular.z = 0.5

    pub.publish(twist)
    """
    #go forward x number of pubs
    #stop movement, rotate 90
    #repeat
    if forwardCounter == 20:
        twist.angular.z = 1.5708
        turnCounter += 1
        if turnCounter == 10:
            forwardCounter = 0
            turnCounter = 0
    else:
        twist.linear.x = 1
        forwardCounter += 1
    pub.publish(twist)
    
    rate.sleep() #sleep until the next time to publish

