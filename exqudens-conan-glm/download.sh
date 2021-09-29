#!/bin/bash

set -e

rm -rf "build"
mkdir "build"
pushd "build"
curl -LJO "file:///C:/install/glm-0.9.9.8.zip" #"https://github.com/g-truc/glm/releases/download/0.9.9.8/glm-0.9.9.8.zip"
unzip -qq "glm-0.9.9.8.zip"
popd
echo 'BUILD_SUCCESSFUL' || (echo 'BUILD_FAILED' && false)
