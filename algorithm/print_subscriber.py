#!/usr/bin/env python
import rospy
from common_msgs.msg import Random

def callback(msg):
    print("Time : ", msg.timestamp.secs%100)
    print("x + y = z")
    print(msg.pose.x, end = "")
    print(" +", msg.pose.y, end = "")
    print(" =", msg.pose.z)

rospy.init_node('algorithm_subscriber')
sub = rospy.Subscriber('sensor_msg', Random, callback)
rospy.spin()
