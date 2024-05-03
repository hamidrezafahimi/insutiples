cmake_minimum_required(VERSION 3.0)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")

project(main)

set(INCLUDE_DIR include)

file(GLOB_RECURSE SOURCES
    lib/*.cpp
    main.cpp
)


add_executable(main ${SOURCES})
target_include_directories(main PRIVATE ${INCLUDE_DIR})


