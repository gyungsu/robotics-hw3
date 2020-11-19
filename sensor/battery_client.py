#!/usr/bin/env python
import rospy
import random
from common_msgs.srv import BATTERY, BATTERYRequest

rospy.init_node('battery_client')
rospy.wait_for_service('battery')
requester = rospy.ServiceProxy('battery', BATTERY)
print ("requester type:", type(requester), ", callable?", callable(requester))
rate = rospy.Rate(10)
count = 0
full = 100
while count < 100:
    if count % 10 == 0:
        random = random.randint(5,15)
        req = BATTERYRequest(total = full - random, random = random)
        res = requester(req)
        print (count, "request:", req.total, req.use, "response:", res.battery)
    rate.sleep()
    count += 1




