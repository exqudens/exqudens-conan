#!/bin/bash

set -e

rm -rf ~/.conan/data/glfw/
rm -rf build/
./download.sh
./export.sh
echo 'BUILD_SUCCESSFUL' || (echo 'BUILD_FAILED' && false)
