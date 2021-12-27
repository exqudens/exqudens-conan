#!/bin/bash

set -e

rm -rf "build"
./download.sh
./export.sh
rm -rf "build"
echo 'BUILD_SUCCESSFUL' || (echo 'BUILD_FAILED' && false)
