project(Bender)
cmake_minimum_required(VERSION 2.8)
aux_source_directory(. SRC_LIST)
include_directories(inc)
add_executable(${PROJECT_NAME} ${SRC_LIST})

