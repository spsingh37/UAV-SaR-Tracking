#!/usr/bin/env python
import rospy

from geometry_msgs.msg import PointStamped

def callback(msg):
	print (msg.point.x)
	

rospy.init_node('Sub_Node')
sub = rospy.Subscriber('/hummingbird/odometry_sensor1/position', PointStamped, callback)
rospy.spin()
