cmake_minimum_required(VERSION 3.4)
project(pybindtest)
add_subdirectory($ENV{HOME}/pybind11 build)
pybind11_add_module(module_name main.cpp)