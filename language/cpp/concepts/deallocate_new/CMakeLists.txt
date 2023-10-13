cmake_minimum_required(VERSION 3.0)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17")

project(main)

add_executable(
    main
    main.cpp
)

add_executable(
    inherited
    inherited.cpp
)
