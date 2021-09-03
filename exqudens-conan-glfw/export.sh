#!/bin/bash

set -e

cp "conanfile.py" "build"
pushd "build"
conan export-pkg conanfile.py glfw/3.3.4 \
-s arch=x86 \
-s os=Windows \
-s compiler="Visual Studio" \
-s compiler.version=16 \
-s compiler.runtime=MD \
-s build_type=Release \
-o shared=True
conan export-pkg conanfile.py glfw/3.3.4 \
-s arch=x86 \
-s os=Windows \
-s compiler="Visual Studio" \
-s compiler.version=16 \
-s compiler.runtime=MT \
-s build_type=Release \
-o shared=False
conan export-pkg conanfile.py glfw/3.3.4 \
-s arch=x86_64 \
-s os=Windows \
-s compiler="Visual Studio" \
-s compiler.version=16 \
-s compiler.runtime=MD \
-s build_type=Release \
-o shared=True
conan export-pkg conanfile.py glfw/3.3.4 \
-s arch=x86_64 \
-s os=Windows \
-s compiler="Visual Studio" \
-s compiler.version=16 \
-s compiler.runtime=MT \
-s build_type=Release \
-o shared=False
popd
echo 'BUILD_SUCCESSFUL' || (echo 'BUILD_FAILED' && false)
