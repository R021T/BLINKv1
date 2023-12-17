#!/bin/bash

set -e

# Download and install CMake
curl -L -o cmake.sh $CMAKE_BINARY_URL
chmod +x cmake.sh
./cmake.sh --skip-license --prefix=$HOME/cmake
export PATH=$HOME/cmake/bin:$PATH

# Clean up
rm cmake.sh
