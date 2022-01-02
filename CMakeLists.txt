cmake_minimum_required(VERSION 3.21 FATAL_ERROR)
get_filename_component(RAW_NAME "${CMAKE_CURRENT_SOURCE_DIR}" NAME)
string(REPLACE " " "_" NAME "${RAW_NAME}")
file(READ "${CMAKE_CURRENT_SOURCE_DIR}/version.txt" RAW_VERSION)
string(STRIP "${RAW_VERSION}" VERSION)
project("${NAME}" VERSION "${VERSION}" LANGUAGES "NONE")

message("project: '${PROJECT_NAME}-${PROJECT_VERSION}'")

include("util.cmake")

add_subdirectory("glm")
add_subdirectory("vulkan")
add_subdirectory("glfw")

set_target_names(ALL_TARGETS "${CMAKE_CURRENT_SOURCE_DIR}")
string(JOIN " " ALL_TARGETS ${ALL_TARGETS})
message("all-targets: '${ALL_TARGETS}'")
