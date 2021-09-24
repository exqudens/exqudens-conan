#!/bin/bash

set -e

CONAN_PACKAGE_USER_CHANNEL=''

cp "conanfile.py" "build"
pushd "build"
conan export-pkg conanfile.py ${CONAN_PACKAGE_USER_CHANNEL} \
-s arch=x86 \
-s os=Windows \
-s compiler="Visual Studio" \
-s compiler.version=16 \
-s compiler.runtime=MD \
-s build_type=Release \
-o type=interface
conan export-pkg conanfile.py ${CONAN_PACKAGE_USER_CHANNEL} \
-s arch=x86_64 \
-s os=Windows \
-s compiler="Visual Studio" \
-s compiler.version=16 \
-s compiler.runtime=MD \
-s build_type=Release \
-o type=interface
popd
echo 'BUILD_SUCCESSFUL' || (echo 'BUILD_FAILED' && false)