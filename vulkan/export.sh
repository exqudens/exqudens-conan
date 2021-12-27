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
conan remove --force 'vulkan/1.2.182.0@' -q 'arch=x86 AND os=Windows AND compiler="Visual Studio" AND compiler.version=16 AND compiler.runtime=MD AND build_type=Release AND shared=True' || true
conan export-pkg conanfile.py ${CONAN_PACKAGE_USER_CHANNEL} \
-s arch=x86 \
-s os=Windows \
-s compiler="Visual Studio" \
-s compiler.version=16 \
-s compiler.runtime=MD \
-s build_type=Release \
-o shared=True
conan remove --force 'vulkan/1.2.182.0@' -q 'arch=x86 AND os=Windows AND compiler="Visual Studio" AND compiler.version=16 AND compiler.runtime=MT AND build_type=Release AND shared=False' || true
conan export-pkg conanfile.py ${CONAN_PACKAGE_USER_CHANNEL} \
-s arch=x86 \
-s os=Windows \
-s compiler="Visual Studio" \
-s compiler.version=16 \
-s compiler.runtime=MT \
-s build_type=Release \
-o shared=False
conan remove --force 'vulkan/1.2.182.0@' -q 'arch=x86_64 AND os=Windows AND compiler="Visual Studio" AND compiler.version=16 AND compiler.runtime=MD AND build_type=Release AND shared=True' || true
conan export-pkg conanfile.py ${CONAN_PACKAGE_USER_CHANNEL} \
-s arch=x86_64 \
-s os=Windows \
-s compiler="Visual Studio" \
-s compiler.version=16 \
-s compiler.runtime=MD \
-s build_type=Release \
-o shared=True
conan remove --force 'vulkan/1.2.182.0@' -q 'arch=x86_64 AND os=Windows AND compiler="Visual Studio" AND compiler.version=16 AND compiler.runtime=MT AND build_type=Release AND shared=False' || true
conan export-pkg conanfile.py ${CONAN_PACKAGE_USER_CHANNEL} \
-s arch=x86_64 \
-s os=Windows \
-s compiler="Visual Studio" \
-s compiler.version=16 \
-s compiler.runtime=MT \
-s build_type=Release \
-o shared=False
popd
echo 'BUILD_SUCCESSFUL' || (echo 'BUILD_FAILED' && false)
