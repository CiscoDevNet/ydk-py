cmake_minimum_required(VERSION 3.0.0)
cmake_policy(SET CMP0048 NEW)

project(path VERSION 0.4.0 LANGUAGES C CXX)

set(CMAKE_MACOSX_RPATH 1)

set(path_DESCRIPTION "Python C++ wrapper for GNMI service path API using pybind11.")

set(python_src python_gnmi.cpp)

# set default build type if not specified by user
set(CMAKE_CXX_FLAGS         "${CMAKE_CXX_FLAGS} -Wall -Wextra")
set(CMAKE_CXX_FLAGS_RELEASE "-O2 -DNDEBUG")

if(COVERAGE STREQUAL True)
    set(CMAKE_CXX_FLAGS_DEBUG   "-g3 -O0 -fprofile-arcs -ftest-coverage")
    set(CMAKE_BUILD_TYPE debug)
else()
    set(CMAKE_CXX_FLAGS_DEBUG   "-g3 -O0")
endif()

# include custom Modules
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/CMakeModules/")

if(PYTHON_VERSION)
    message( "python version: ${PYTHON_VERSION}" )
else()
    message( FATAL_ERROR "-DPYTHON_VERSION not specified." )
endif()
set(Python_ADDITIONAL_VERSIONS ${PYTHON_VERSION})

# Find dependent libraries
find_library(ydk_location ydk)
find_library(ydk_gnmi_location ydk_gnmi)
find_library(xml2_location xml2)
find_library(curl_location curl)
find_library(ssh_threads_location ssh_threads)
find_library(xslt_location xslt)
find_library(pcre_location pcre)
find_library(ssh_location ssh)
find_package(PythonLibs)
find_package(Protobuf REQUIRED)
find_package(GRPC REQUIRED)

if(PYBIND11_INCLUDE)
    message( "pybind11 include: ${PYBIND11_INCLUDE}")
else()
    message( FATAL_ERROR "-DPYBIND11_INCLUDE not specified." )
endif()

include_directories(SYSTEM ${PYTHON_INCLUDE_PATH} ${PYBIND11_INCLUDE})

# set default build type if not specified by user
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE debug)
endif()

add_library(ydk_gnmi_ MODULE ${python_src})
set_target_properties(ydk_gnmi_ PROPERTIES PREFIX "")
if(WIN32 AND NOT CYGWIN)
    set_target_properties(ydk_gnmi_ PROPERTIES SUFFIX ".pyd")
else()
    set_target_properties(ydk_gnmi_ PROPERTIES SUFFIX ".so")
endif()

set_property(TARGET ydk_gnmi_ PROPERTY CXX_STANDARD 14)
set_property(TARGET ydk_gnmi_ PROPERTY CXX_STANDARD_REQUIRED ON)

target_link_libraries(ydk_gnmi_
            ${ydk_gnmi_location}
            ${ydk_location}
            ${xml2_location}
            ${curl_location}
            ${ssh_threads_location}
            ${pcre_location}
            ${xslt_location}
            ${ssh_location}
            ${PYTHON_LIBRARIES}
            -rdynamic
            ${GRPC_GRPC++_LIBRARY}
            ${PROTOBUF_LIBRARY}
            )
