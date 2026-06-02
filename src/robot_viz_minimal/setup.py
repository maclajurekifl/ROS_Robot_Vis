from setuptools import setup
from glob import glob
import os

package_name = "robot_viz_minimal"

setup(
    name=package_name,
    version="0.1.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name, "launch"), glob("launch/*.launch.py")),
        (os.path.join("share", package_name, "urdf"), glob("urdf/*.urdf")),
        (os.path.join("share", package_name, "rviz"), glob("rviz/*.rviz")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="macla",
    maintainer_email="macla@todo.todo",
    description="Minimal standalone robot visualization package for RViz.",
    license="MIT",
    entry_points={
        "console_scripts": [
            "robot_vis_joint_publisher = robot_viz_minimal.robot_vis_joint_publisher:main",
        ],
    },
)
