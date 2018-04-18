# Robotics
Catherine Zhao, Roop Pal, Chris Conte

## Context
We have switched to use Baxter Robots and are upgrading the research of XXX

The current repo is https://github.com/Yinxiaoli/iros2015_folding

The current directory does not adhere to Catkin directory format. The current structure is

```
iros2015_folding
   \images
      test_pants.jpg
      test_sweater.jpg
      test_towel.jpg
   \src
      \folding_control
         \launch
         \src
      \folding_planner
         \launch
         \src
      \folding_pplanner_cmake
         \lib
         \project
         CMakeList.txt
   LICENSE
   README.md
   keypoints.sweater.png
```
This will not run on ROS and will need additional packages. 

We used ROS Kinetic for this project In

To start, a MoveIt package 
