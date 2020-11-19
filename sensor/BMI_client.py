#!/usr/bin/env python
import rospy
import random
from common_msgs.srv import BMI, BMIRequest

rospy.init_node('BMI_client')
rospy.wait_for_service('bmi')
requester = rospy.ServiceProxy('bmi', BMI)
print ("requester type:", type(requester), ", callable?", callable(requester))
rate = rospy.Rate(10)
count = 0
while count < 100:
    if count % 10 == 0:
        req = BMIRequest(weight = random.randint(50,130), height = random.randint(150,190))
        res = requester(req)
        print (count, "request:", req.weight, req.height, "response:", res.bmi)
    rate.sleep()
    count += 1




