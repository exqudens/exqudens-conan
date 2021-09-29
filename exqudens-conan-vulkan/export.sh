#!/bin/bash

set -e

CONAN_PACKAGE_USER_CHANNEL='' # 'test-user/test-channel'

cp "conanfile.py" "build"
pushd "build"
conan export-pkg conanfile.py ${CONAN_PACKAGE_USER_CHANNEL} \
-s arch=x86 \
-s os=Windows \
-s compiler="Visual Studio" \
-s compiler.version=16 \
-s compiler.runtime=MD \
-s build_type=Release \
-o type=shared
conan export-pkg conanfile.py ${CONAN_PACKAGE_USER_CHANNEL} \
-s arch=x86 \
-s os=Windows \
-s compiler="Visual Studio" \
-s compiler.version=16 \
-s compiler.runtime=MT \
-s build_type=Release \
-o type=static
conan export-pkg conanfile.py ${CONAN_PACKAGE_USER_CHANNEL} \
-s arch=x86_64 \
-s os=Windows \
-s compiler="Visual Studio" \
-s compiler.version=16 \
-s compiler.runtime=MD \
-s build_type=Release \
-o type=shared
conan export-pkg conanfile.py ${CONAN_PACKAGE_USER_CHANNEL} \
-s arch=x86_64 \
-s os=Windows \
-s compiler="Visual Studio" \
-s compiler.version=16 \
-s compiler.runtime=MT \
-s build_type=Release \
-o type=static
popd
echo 'BUILD_SUCCESSFUL' || (echo 'BUILD_FAILED' && false)