#!/bin/bash

set -e

CONAN_PACKAGE_NAME="$(basename $(pwd))"
CONAN_PACKAGE_VERSION="$(cat version.txt)"
CONAN_PACKAGE_USER=''
CONAN_PACKAGE_CHANNEL=''
CONAN_PACKAGE_REFERENCE="${CONAN_PACKAGE_NAME}/${CONAN_PACKAGE_VERSION}" # 'name/version@user/channel'
CONAN_PACKAGE_USER_CHANNEL='' # 'user/channel'

cp "conanfile.py" "build"
pushd "build"
conan remove --force "${CONAN_PACKAGE_REFERENCE}"
conan export-pkg conanfile.py ${CONAN_PACKAGE_USER_CHANNEL}
popd
echo 'BUILD_SUCCESSFUL' || (echo 'BUILD_FAILED' && false)
