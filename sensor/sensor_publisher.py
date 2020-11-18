#!/usr/bin/env python
import rospy
import random
from geometry_msgs.msg import Vector3
from common_msgs.msg import Random


rospy.init_node('sensor_publisher')
pub = rospy.Publisher('sensor_msg', Random, queue_size=1)
msg = Random()
rate = rospy.Rate(1)
while not rospy.is_shutdown():   
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs
    msg.pose = Vector3(x = random.randint(1,100), y = random.randint(1,100), z = 0)
    msg.pose.z = msg.pose.x + msg.pose.y
    print("Time : ", msg.timestamp.secs%100)
    print("x + y = z")
    print(msg.pose.x, end = "")
    print("+", msg.pose.y, end = "")
    print("=", msg.pose.z)
    pub.publish(msg)
    rate.sleep()





