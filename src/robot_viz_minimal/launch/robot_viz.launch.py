#!/usr/bin/env python3
from __future__ import annotations

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def _launch_setup(context, *args, **kwargs):
    pkg_share = get_package_share_directory("robot_viz_minimal")

    urdf_default = os.path.join(pkg_share, "urdf", "macla_robot.urdf")
    rviz_default = os.path.join(pkg_share, "rviz", "robot_viz.rviz")

    urdf_path = LaunchConfiguration("urdf_path").perform(context).strip() or urdf_default
    rviz_cfg = LaunchConfiguration("rviz_config").perform(context).strip() or rviz_default

    with open(urdf_path, encoding="utf-8") as f:
        robot_description = f.read()

    use_sim_time_raw = LaunchConfiguration("use_sim_time").perform(context).strip().lower()
    use_sim_time = use_sim_time_raw in ("true", "1", "yes", "on")

    actions = [
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            output="screen",
            parameters=[
                {"robot_description": robot_description},
                {"use_sim_time": use_sim_time},
            ],
        ),
        Node(
            package="robot_viz_minimal",
            executable="robot_vis_joint_publisher",
            name="robot_vis_joint_publisher",
            output="screen",
            parameters=[
                {
                    "odom_topic": LaunchConfiguration("odom_topic"),
                    "publish_rate_hz": LaunchConfiguration("joint_publish_rate_hz"),
                    "use_sim_time": use_sim_time,
                }
            ],
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            arguments=["-d", rviz_cfg],
            output="screen",
            parameters=[{"use_sim_time": use_sim_time}],
            condition=IfCondition(LaunchConfiguration("start_rviz")),
        ),
    ]
    return actions


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument("use_sim_time", default_value="false"),
            DeclareLaunchArgument("start_rviz", default_value="true"),
            DeclareLaunchArgument("odom_topic", default_value="/ekf/odom"),
            DeclareLaunchArgument("joint_publish_rate_hz", default_value="30.0"),
            DeclareLaunchArgument("urdf_path", default_value=""),
            DeclareLaunchArgument("rviz_config", default_value=""),
            OpaqueFunction(function=_launch_setup),
        ]
    )
