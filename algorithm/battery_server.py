#!/usr/bin/env python
import rospy
from common_msgs.srv import BATTERY, BATTERYResponse

def service_callback(request):
    response = BATTERYResponse(battery=request.total)
    print ("TOTAL:", request.total,"% USE:", request.use, "% BATTERY:", response.battery,"%")
    return response

rospy.init_node('battery_server')
service = rospy.Service('battery', BATTERY, service_callback)
rospy.spin()
