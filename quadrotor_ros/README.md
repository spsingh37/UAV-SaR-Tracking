# quadrotor_ros 
Implemented everything on ROS Kinetic + Ubuntu 16.04

1. Launch simulation of AR Drone in Gazebo : (forked from [Qlabs](https://github.com/pulver22/QLAB))
```
roslaunch qlab_gazebo drone.launch
```
or
```
roslaunch cvg_sim_gazebo drone.launch
```

2. Teleop the quadrotor using keyboard :
```
rosrun quadrotor_teleop_keyboard quadrotor_teleop_keyboard.py
```

3. Perform PTAM (Parllel Tracking and Mapping) for visual navigation : ([More Info](https://vision.in.tum.de/data/software/tum_ardrone))
```
roslaunch tum_ardrone tum_ardrone.launch
```
