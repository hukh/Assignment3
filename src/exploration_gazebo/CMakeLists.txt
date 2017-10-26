cmake_minimum_required(VERSION 2.8.3)
project(exploration_gazebo)

SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -std=c++14 -O3")
## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  gazebo_ros
  sensor_msgs
  std_msgs
  genmsg 
  message_generation
  dynamic_reconfigure
)

#add_message_files(
#  FILES
#)

#generate_messages(
#  DEPENDENCIES
#  std_msgs
#)

# generate dyn reconf
#generate_dynamic_reconfigure_options(
#    cfg/Hydrodynamics.cfg    
#)

find_package(gazebo REQUIRED)
find_package(Boost REQUIRED)
find_package(Eigen3 REQUIRED)

catkin_package(
  INCLUDE_DIRS include
#  LIBRARIES aqua_gazebo
  CATKIN_DEPENDS 
  roscpp
  sensor_msgs
  std_msgs
  gazebo_ros
  message_runtime
  dynamic_reconfigure
  message_runtime
)

###########
## Build ##
###########

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${EIGEN3_INCLUDE_DIR}
  ${GAZEBO_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIRS}
)

link_directories(
  ${GAZEBO_LIBRARY_DIRS}
)

