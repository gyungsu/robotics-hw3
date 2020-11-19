#!/usr/bin/env python
import rospy
from common_msgs.srv import BMI, BMIResponse

def service_callback(request):
    response = BMIResponse(bmi=request.whight /(request.height * request.height))
    print ("request data:", request.weight, request.height, ", response:", response.bmi)
    return response

rospy.init_node('BMI_subscriber')
service = rospy.Service('bmi', BMI, service_callback)
rospy.spin()