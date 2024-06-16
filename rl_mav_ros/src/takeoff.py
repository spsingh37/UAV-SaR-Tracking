#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
import time

rospy.init_node('Takeoff')
pub = rospy.Publisher('quadrotor/ardrone/takeoff', Empty, queue_size = 10)

count = Empty()
rate=rospy.Rate(2)

start_time = time.time()

while not rospy.is_shutdown():
	m, s = divmod(int(time.time() - start_time), 60)
	if(s>1):
		break
	pub.publish(count)
	rate.sleep()
