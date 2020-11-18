#!/usr/bin/env python
import rospy
from common_msgs.msg import Random

def callback(msg):
    print ("subscribe:", msg.pose.x, msg.pose.y, msg.pose.z)

rospy.init_node('algorithm_subscriber')
sub = rospy.Subscriber('sensor_msg', Random, callback)
rospy.spin()
