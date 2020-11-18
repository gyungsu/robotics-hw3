cmake_minimum_required(VERSION 3.0.2)
project(topic_custom)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  rospy
  std_msgs
)

add_message_files(
  FILES
  TimePose.msg
)
generate_messages(
  DEPENDENCIES
  geometry_msgs
  std_msgs
)
catkin_package(
 CATKIN_DEPENDS geometry_msgs rospy std_msgs
)

