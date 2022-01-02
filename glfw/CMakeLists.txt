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
            #"https://github.com/glfw/glfw/releases/download/3.3.4/glfw-3.3.4.bin.WIN32.zip"
            "file:///C:/install/glfw-3.3.4.bin.WIN32.zip"
            --file
            "${PROJECT_BINARY_DIR}/build/glfw-3.3.4.bin.WIN32.zip"
    COMMAND "${CMAKE_COMMAND}" -P "${CMAKE_SOURCE_DIR}/download.cmake"
            --url
            #"https://github.com/glfw/glfw/releases/download/3.3.4/glfw-3.3.4.bin.WIN64.zip"
            "file:///C:/install/glfw-3.3.4.bin.WIN64.zip"
            --file
            "${PROJECT_BINARY_DIR}/build/glfw-3.3.4.bin.WIN64.zip"
    DEPENDS "${PROJECT_NAME}-mkdir-build"
    WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
    VERBATIM
)

add_custom_target("${PROJECT_NAME}-extract"
    COMMAND "${CMAKE_COMMAND}" -E tar x glfw-3.3.4.bin.WIN32.zip --format=zip
    COMMAND "${CMAKE_COMMAND}" -E tar x glfw-3.3.4.bin.WIN64.zip --format=zip
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

add_custom_target("${PROJECT_NAME}-conan-export-recipe"
    COMMAND "${CONAN_COMMAND}"
            export
            "${PROJECT_BINARY_DIR}/build/conanfile.py"
            #${CONAN_PACKAGE_USER_CHANNEL}
    DEPENDS "${PROJECT_NAME}-extract"
            "${PROJECT_NAME}-copy-files"
    WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
    VERBATIM
)

foreach(arch "x86" "x86_64")
    foreach(compiler "Visual Studio")
        if("Visual Studio" STREQUAL "${compiler}")
            foreach(compiler_version "15" "16" "17")
                foreach(shared "True" "False")
                    set(type "shared")
                    set(compiler_runtime "MD")
                    if("False" STREQUAL "${shared}")
                        set(type "static")
                        set(compiler_runtime "MT")
                    endif()
                    string(JOIN " AND " CONAN_REMOVE_QUERY
                        "arch=${arch}"
                        "os=Windows"
                        "compiler=\"Visual Studio\""
                        "compiler.version=${compiler_version}"
                        "compiler.runtime=${compiler_runtime}"
                        "build_type=Release"
                        "shared=${shared}"
                    )
                    add_custom_target("${PROJECT_NAME}-conan-remove-${arch}-vs-${compiler_version}-${type}"
                        COMMAND "${CONAN_COMMAND}" remove --force "${PROJECT_NAME}/${PROJECT_VERSION}@" --query "${CONAN_REMOVE_QUERY}"
                        DEPENDS "${PROJECT_NAME}-conan-export-recipe"
                        WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
                        VERBATIM
                    )
                    set(CONAN_EXPORT_ARGS
                        "-s" "arch=${arch}"
                        "-s" "os=Windows"
                        "-s" "compiler=Visual Studio"
                        "-s" "compiler.version=${compiler_version}"
                        "-s" "compiler.runtime=${compiler_runtime}"
                        "-s" "build_type=Release"
                        "-o" "shared=${shared}"
                    )
                    add_custom_target("${PROJECT_NAME}-conan-export-${arch}-vs-${compiler_version}-${type}"
                        COMMAND "${CONAN_COMMAND}"
                                export-pkg
                                "${PROJECT_BINARY_DIR}/build/conanfile.py"
                                #${CONAN_PACKAGE_USER_CHANNEL}
                                ${CONAN_EXPORT_ARGS}
                        DEPENDS "${PROJECT_NAME}-conan-remove-${arch}-vs-${compiler_version}-${type}"
                        WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
                        VERBATIM
                    )
                    list(APPEND CONAN_EXPORT_ALL_DEPENDS "${PROJECT_NAME}-conan-export-${arch}-vs-${compiler_version}-${type}")
                endforeach()
            endforeach()
        endif()
    endforeach()
endforeach()

add_custom_target("${PROJECT_NAME}-conan-export-all" ALL
    COMMAND "${CMAKE_COMMAND}" -E echo "BUILD_SUCCESSFUL"
    DEPENDS ${CONAN_EXPORT_ALL_DEPENDS}
    WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}"
    VERBATIM
)
