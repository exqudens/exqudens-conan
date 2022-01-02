cmake_minimum_required(VERSION 3.21 FATAL_ERROR)
get_filename_component(RAW_NAME "${CMAKE_CURRENT_SOURCE_DIR}" NAME)
string(REPLACE " " "_" NAME "${RAW_NAME}")
file(READ "${CMAKE_CURRENT_SOURCE_DIR}/version.txt" RAW_VERSION)
string(STRIP "${RAW_VERSION}" VERSION)
project("${NAME}" VERSION "${VERSION}" LANGUAGES "NONE")

message("project: '${PROJECT_NAME}-${PROJECT_VERSION}'")

find_program(CONAN_COMMAND NAMES "conan.exe" "conan")

add_custom_target("${PROJECT_NAME}-clean"
    COMMAND "${CMAKE_COMMAND}" -E rm -rf "${PROJECT_BINARY_DIR}/build"
    WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
    VERBATIM
)

add_custom_target("${PROJECT_NAME}-mkdir-build"
    COMMAND "${CMAKE_COMMAND}" -E make_directory "${PROJECT_BINARY_DIR}/build"
    DEPENDS "${PROJECT_NAME}-clean"
    WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
    VERBATIM
)

add_custom_target("${PROJECT_NAME}-download"
    COMMAND "${CMAKE_COMMAND}" -P "${CMAKE_SOURCE_DIR}/download.cmake"
            --url
            #"https://github.com/g-truc/glm/releases/download/0.9.9.8/glm-0.9.9.8.zip"
            "file:///C:/install/glm-0.9.9.8.zip"
            --file
            "${PROJECT_BINARY_DIR}/build/glm-0.9.9.8.zip"
    DEPENDS "${PROJECT_NAME}-mkdir-build"
    WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
    VERBATIM
)

add_custom_target("${PROJECT_NAME}-extract"
    COMMAND "${CMAKE_COMMAND}" -E tar x glm-0.9.9.8.zip --format=zip
    DEPENDS "${PROJECT_NAME}-download"
    WORKING_DIRECTORY "${PROJECT_BINARY_DIR}/build"
    VERBATIM
)

add_custom_target("${PROJECT_NAME}-copy-files"
    COMMAND "${CMAKE_COMMAND}" -E copy "${PROJECT_SOURCE_DIR}/conanfile.py" "${PROJECT_BINARY_DIR}/build"
    COMMAND "${CMAKE_COMMAND}" -E copy "${PROJECT_SOURCE_DIR}/version.txt" "${PROJECT_BINARY_DIR}/build"
    DEPENDS "${PROJECT_NAME}-extract"
    WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
    VERBATIM
)

add_custom_target("${PROJECT_NAME}-conan-remove-all"
    COMMAND "${CONAN_COMMAND}" remove --force "${PROJECT_NAME}/${PROJECT_VERSION}"
    WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
    VERBATIM
)

add_custom_target("${PROJECT_NAME}-conan-export"
    COMMAND "${CONAN_COMMAND}"
    export-pkg
    "${PROJECT_BINARY_DIR}/build/conanfile.py"
    #${CONAN_PACKAGE_USER_CHANNEL}
    DEPENDS "${PROJECT_NAME}-extract"
            "${PROJECT_NAME}-copy-files"
    WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
    VERBATIM
)

add_custom_target("${PROJECT_NAME}-conan-export-all" ALL
    COMMAND "${CMAKE_COMMAND}" -E echo "BUILD_SUCCESSFUL"
    DEPENDS "${PROJECT_NAME}-conan-export"
    WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
    VERBATIM
)
