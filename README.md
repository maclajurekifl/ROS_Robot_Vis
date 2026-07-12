# Year 3 Project — Robot Visualisation (EEE3017)

Minimal **ROS 2** RViz / URDF visualisation package used with the Year 3 SLAM stack.

**Main deployment repo:** [ROS_Deploy_Orin](https://github.com/maclajurekifl/ROS_Deploy_Orin)

## Package

`src/robot_viz_minimal` — launch file, RViz config, URDF (`macla_robot.urdf`), and a simple joint publisher.

```bash
source /opt/ros/humble/setup.bash
cd <this_repo>
colcon build --symlink-install
source install/setup.bash
ros2 launch robot_viz_minimal robot_viz.launch.py
```

## Documentation

- `docs/EEE3017_Dissertation.pdf` — final Year 3 dissertation (shared with the deploy repo)

## Author

Jude Burton — University of Surrey, Electrical & Electronic Engineering
