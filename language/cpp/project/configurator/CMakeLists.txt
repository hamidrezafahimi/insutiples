cmake_minimum_required(VERSION 3.4)
set(CMAKE_CXX_STANDARD 17 CACHE STRING "C++ version selection")  # or 11, 14, 17, 20

project( main )

find_package(PkgConfig)
pkg_check_modules(YAMLCPP REQUIRED yaml-cpp>=0.5)
include_directories(${YAMLCPP_INCLUDE_DIRS})

add_library(conflib Config.h Config.cpp)

add_executable( main ../main.cpp )
target_link_libraries(main ${YAMLCPP_LIBRARIES} conflib)
