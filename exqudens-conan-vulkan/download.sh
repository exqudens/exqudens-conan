#!/bin/bash

set -e

rm -rf "build"
mkdir "build"
pushd "build"
cp -rv "C:/VulkanSDK/1.2.182.0" "./" #"https://sdk.lunarg.com/sdk/download/1.2.189.2/windows/VulkanSDK-1.2.182.0-Installer.exe"
popd
echo 'BUILD_SUCCESSFUL' || (echo 'BUILD_FAILED' && false)
