import rospy
from common_msgs.msg import Random





def callback(msg):
    print ("subscribe:", msg.pose.x, msg.pose.y, msg.pose.z)

rospy.init_node('custom_subscriber')
sub = rospy.Subscriber('custom_msg', Random, callback)
rospy.spin()
