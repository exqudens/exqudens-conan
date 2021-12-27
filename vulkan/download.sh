#!/bin/bash

set -e

mkdir "build"
pushd "build"
curl -LJO "file:///C:/install/VulkanSDK-1.2.182.0.zip" #"https://sdk.lunarg.com/sdk/download/1.2.189.2/windows/VulkanSDK-1.2.182.0-Installer.exe"
unzip -qq "VulkanSDK-1.2.182.0.zip"
popd
echo 'BUILD_SUCCESSFUL' || (echo 'BUILD_FAILED' && false)
