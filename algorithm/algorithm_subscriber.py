import rospy
from common_msgs.msg import Random


while(1):
     print(msg.pose.x, end = "")
     print("+", msg.pose.y, end = "")
     print("=", msg.pose.z)


rospy.init_node('algorithm_subscriber')

