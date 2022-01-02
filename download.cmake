set(USAGE_MESSAGE "usage: cmake -P download.cmake --url <url> --file <file>")

if(NOT "7" STREQUAL "${CMAKE_ARGC}")
    message(FATAL_ERROR "${USAGE_MESSAGE}")
endif()

math(EXPR CMAKE_ARGI_MAX "${CMAKE_ARGC} - 1")

foreach(i RANGE 0 ${CMAKE_ARGI_MAX})
    list(APPEND CMAKE_ARGS "${CMAKE_ARGV${i}}")
endforeach()

list(GET CMAKE_ARGS 3 URL_FLAG)
list(GET CMAKE_ARGS 5 FILE_FLAG)

if(NOT "--url" STREQUAL "${URL_FLAG}" OR NOT "--file" STREQUAL "${FILE_FLAG}")
    message(FATAL_ERROR "${USAGE_MESSAGE}")
endif()

list(GET CMAKE_ARGS 4 URL)
list(GET CMAKE_ARGS 6 FILE)

file(REMOVE "${FILE}")
file(DOWNLOAD "${URL}" "${FILE}")
