#!/bin/bash

set -e

mkdir "build"
pushd "build"
curl -LJO "file:///C:/install/glfw-3.3.4.bin.WIN32.zip" #"https://github.com/glfw/glfw/releases/download/3.3.4/glfw-3.3.4.bin.WIN32.zip"
curl -LJO "file:///C:/install/glfw-3.3.4.bin.WIN64.zip" #"https://github.com/glfw/glfw/releases/download/3.3.4/glfw-3.3.4.bin.WIN64.zip"
unzip -qq "glfw-3.3.4.bin.WIN32.zip"
unzip -qq "glfw-3.3.4.bin.WIN64.zip"
popd
echo 'BUILD_SUCCESSFUL' || (echo 'BUILD_FAILED' && false)
