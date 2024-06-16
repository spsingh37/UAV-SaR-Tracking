#!/usr/bin/env python

import pid
from geometry_msgs.msg import Twist
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point
import matplotlib.pyplot as plt	

class Waypoint:

	def __init__(self):

		self.vel = rospy.Publisher('/quadrotor/cmd_vel', Twist, queue_size = 1)
	
	def publish(self, des_x, des_y, des_z):


		pid_x = pid.PID(0.5, 0.001, 0.1)
		pid_y = pid.PID(0.5, 0.001, 0.1)
		pid_z = pid.PID(0.5, 0.001, 0.1)

		self.flag = True

		while True:

			data = rospy.wait_for_message('/quadrotor/ground_truth/state', Odometry, timeout=1)
		   	error_x = des_x - data.pose.pose.position.x
			error_y = des_y - data.pose.pose.position.y
			error_z = des_z - data.pose.pose.position.z
		
			com = Twist()

			com.linear.x = pid_x.Update(error_x)
			com.linear.y = pid_y.Update(error_y)
			com.linear.z = pid_z.Update(error_z)
			com.angular.z = 0.0

			self.vel.publish(com)

			if(abs(error_x)<0.05 and abs(error_y)<0.05 and abs(error_z)<0.05):
				com.linear.x = 0
				com.linear.y = 0
				com.linear.z = 0
				self.vel.publish(com)
				break

