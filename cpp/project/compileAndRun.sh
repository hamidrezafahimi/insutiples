#!/bin/bash

cd build/
rm -r CMakeFiles/ CMakeCache.txt cmake_install.cmake Makefile main
set -e
cmake .
make
./main
