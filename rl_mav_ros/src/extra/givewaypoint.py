#!/usr/bin/env python
import rospy
import sys
import tf
import numpy as np

from trajectory_msgs.msg import MultiDOFJointTrajectory, MultiDOFJointTrajectoryPoint
from geometry_msgs.msg import Twist 
from geometry_msgs.msg import Transform

def publish_waypoint(x,y,z,yaw):
	"""
	Publish a waypoint to 
	"""

	command_publisher = rospy.Publisher('/hummingbird/command/trajectory', MultiDOFJointTrajectory, queue_size = 10)

	# create trajectory msg
	traj = MultiDOFJointTrajectory()
	traj.header.stamp = rospy.Time.now()
	traj.joint_names.append('base_link')

	# create end point for trajectory
	transforms = Transform()
	transforms.translation.x = x
	transforms.translation.y = y
	transforms.translation.z = z 

	quat = tf.transformations.quaternion_from_euler(yaw*np.pi/180.0, 0, 0, axes = 'rzyx')
	transforms.rotation.x = quat[0]
	transforms.rotation.y = quat[1]
	transforms.rotation.z = quat[2]
	transforms.rotation.w = quat[3]

	velocities = Twist()
	accel = Twist()
	point = MultiDOFJointTrajectoryPoint([transforms],[velocities],[accel], rospy.Time(1))
	traj.points.append(point)

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
