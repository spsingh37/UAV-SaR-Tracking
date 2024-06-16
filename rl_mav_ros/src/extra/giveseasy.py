#!/usr/bin/env python
import rospy
import sys
import tf
import numpy as np

from geometry_msgs.msg import PoseStamped

def publish_waypoint(x,y,z,yaw):
	"""
	Publish a waypoint to 
	"""

	command_publisher = rospy.Publisher('/firefly/command/pose', PoseStamped, queue_size = 1)

	traj = PoseStamped()
	traj.pose.position.x = x
	traj.pose.position.y = y
	traj.pose.position.z = z

	rospy.sleep(1)
	command_publisher.publish(traj)


if __name__ == '__main__':
	try:

		rospy.init_node("riseq_rotors_waypoint_publisher", anonymous = True)

		# get command line params
		x_des = float(sys.argv[1])
		y_des = float(sys.argv[2])
		z_des = float(sys.argv[3])
		yaw_des = float(sys.argv[4])

		publish_waypoint(x_des, y_des, z_des, yaw_des)

		#rospy.spinOnce()
		rospy.loginfo(" >> Published waypoint: x: {}, y: {}, z: {}, yaw: {}".format(x_des, y_des, z_des, yaw_des))


	except rospy.ROSInterruptException:
		print("ROS Terminated")
		pass
