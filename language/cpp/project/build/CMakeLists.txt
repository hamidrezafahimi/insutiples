cmake_minimum_required(VERSION 3.0)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")

project(main)

set(INCLUDE_DIR ../include)
set(LIB_DIR ../lib)
set(SCRIPTS_DIR ../scripts)

file(GLOB_RECURSE SOURCES
    ${LIB_DIR}/*.cpp
    ${SCRIPTS_DIR}/*.cpp
)

add_executable(main ${SOURCES})
target_include_directories(main PRIVATE ${INCLUDE_DIR})


