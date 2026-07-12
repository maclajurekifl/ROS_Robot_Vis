# ROS 2 Robot Visualisation (EEE3017)

Minimal RViz + URDF visualisation for the Year 3 Jetson Orin SLAM robot.

**Main stack:** [jetson-orin-lidar-slam](https://github.com/maclajurekifl/jetson-orin-lidar-slam)

## Run
`ash
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
ros2 launch robot_viz_minimal robot_viz.launch.py
`

## Docs
- `docs/EEE3017_Dissertation.pdf`

## Author
Jude Burton
