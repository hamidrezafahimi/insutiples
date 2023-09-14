cmake_minimum_required(VERSION 3.4)
set(CMAKE_CXX_STANDARD 17 CACHE STRING "C++ version selection")  # or 11, 14, 17, 20

project(pybindtest)
add_subdirectory($ENV{HOME}/pybind11 build)
# include_directories( $ENV{HOME}/pybind11/include )
# include_directories( /usr/incldue/python3.8 )

file( GLOB SOURCE lib.cpp )
file( GLOB HEADER header.h )
add_library( ProjectLib ${SOURCE} ${HEADER} )

pybind11_add_module(module_name interface.cpp)
target_link_libraries( module_name PUBLIC ProjectLib )

# add_executable( test test.cpp)
# target_link_libraries( test ProjectLib )
