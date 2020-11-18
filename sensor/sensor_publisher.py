
import rospy
import random
from geometry_msgs.msg import Vector3
from common_msgs.msg import Random


rospy.init_node('sensor_publisher')
msg = Random()
while(1):
     msg.pose = Vector3(x = random.randint(1,100), y = random.randint(1,100), z = 0)
     msg.pose.z = msg.pose.x + msg.pose.y
     print("x + y = z")
     print(msg.pose.x, end = "")
     print("+", msg.pose.y, end = "")
     print("=", msg.pose.z)


