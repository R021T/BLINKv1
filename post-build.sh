#!/bin/bash

set -e

# Install CMake
curl -L -o cmake.sh $CMAKE_BINARY_URL
chmod +x cmake.sh
./cmake.sh --skip-license

# Clean up
rm cmake.sh
