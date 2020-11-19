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
req = BATTERYRequest(total = 100, use = 0)
while req.total > 15:
    if count % 10 == 0:
        req.use = random.randint(5,15)
        req.total = req.total - req.use
        res = requester(req)
        print ("use time:", count, "minute")
        if req.total < 16 :
            print("charge please !!")
            break   
        print ("TOTAL:", req.total ,"% USE:",req.use,"% BATTERY:", res.battery,"%")
        
    rate.sleep()
    count += 1




