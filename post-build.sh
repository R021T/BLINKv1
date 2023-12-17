#!/bin/bash

set -e

# Set CMake binary URL
export CMAKE_BINARY_URL="https://cmake.org/files/v3.22/cmake-3.22.1-Linux-x86_64.sh"

# Download and install CMake
curl -L -o cmake.sh $CMAKE_BINARY_URL
chmod +x cmake.sh
./cmake.sh --skip-license --prefix=$HOME/cmake
export PATH=$HOME/cmake/bin:$PATH

# Clean up
rm cmake.sh
