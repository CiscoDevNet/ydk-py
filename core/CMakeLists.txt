cmake_minimum_required(VERSION 2.8.9)
cmake_policy(SET CMP0048 NEW)
project(path VERSION 0.5.5 LANGUAGES C CXX)
set(CMAKE_MACOSX_RPATH 1)

set(path_DESCRIPTION "Python wrapper around C++ path API using pybind11.")

set(python_src python.cpp)

# set default build type if not specified by user
set(CMAKE_CXX_FLAGS         "${CMAKE_CXX_FLAGS} -Wall -Wextra")
set(CMAKE_CXX_FLAGS_RELEASE "-O2 -DNDEBUG")
set(CMAKE_CXX_FLAGS_DEBUG   "-g -O0 -fprofile-arcs -ftest-coverage")

# Find dependent libraries
find_library(ydk_location ydk)
find_library(xml2_location xml2)
find_library(curl_location curl)
find_library(ssh_threads_location ssh_threads)
find_library(xslt_location xslt)
find_library(pcre_location pcre)
find_library(ssh_location ssh)

if(PYTHON_LIBRARY)
    message( "python library: ${PYTHON_LIBRARY}" )
else()
    message( FATAL_ERROR "-DPYTHON_LIBRARY not specified." )
endif()

if(PYTHON_INCLUDE)
    message( "python include: ${PYTHON_INCLUDE}" )
else()
    message( FATAL_ERROR "-DPYTHON_INCLUDE not specified." )
endif()

if(PYBIND11_INCLUDE)
    message( "pybind11 include: ${PYBIND11_INCLUDE}")
else()
    message( FATAL_ERROR "-DPYBIND11_INCLUDE not specified." )
endif()

include_directories(SYSTEM ${PYTHON_INCLUDE} ${PYBIND11_INCLUDE})

# set default build type if not specified by user
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE debug)
endif()

add_library(ydk_ MODULE ${python_src})
set_target_properties(ydk_ PROPERTIES PREFIX "")
if(WIN32 AND NOT CYGWIN)
    set_target_properties(ydk_ PROPERTIES SUFFIX ".pyd")
else()
    set_target_properties(ydk_ PROPERTIES SUFFIX ".so")
endif()

set_property(TARGET ydk_ PROPERTY CXX_STANDARD 14)
set_property(TARGET ydk_ PROPERTY CXX_STANDARD_REQUIRED ON)

target_link_libraries(ydk_
            ${ydk_location}
            ${xml2_location}
            ${curl_location}
            ${ssh_threads_location}
            ${pcre_location}
            ${xslt_location}
            ${ssh_location}
            ${PYTHON_LIBRARY}
            -rdynamic
            )
