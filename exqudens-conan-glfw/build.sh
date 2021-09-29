#!/bin/bash

set -e

rm -rf ~/.conan/data/glfw/
./download.sh
./export.sh
echo 'BUILD_SUCCESSFUL' || (echo 'BUILD_FAILED' && false)
