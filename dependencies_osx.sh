#!/bin/bash

function print_msg {
    echo -e "${MSG_COLOR}*** $(date): dependencies_osx.sh | $@ ${NOCOLOR}"
}

function install_os_dependencies {
    brew install curl xml2 doxygen pybind11
}

function install_libssh {
    print_msg "Checking installation of libssh"
    locate libssh_threads.dylib
    local status=$?
    if [[ ${status} == 0 ]]; then
        return
    fi
    print_msg "Installing libssh-0.7.6"
    brew reinstall openssl
    export OPENSSL_ROOT_DIR=/usr/local/opt/openssl
    wget https://git.libssh.org/projects/libssh.git/snapshot/libssh-0.7.6.tar.gz
    tar zxf libssh-0.7.6.tar.gz && rm -f libssh-0.7.6.tar.gz
    mkdir libssh-0.7.6/build && cd libssh-0.7.6/build
    cmake ..
    sudo make install
    cd -
}

function install_libydk {
    print_msg "Installing YDK C++ core library"
    curl -O https://devhub.cisco.com/artifactory/osx-ydk/0.8.3/libydk-0.8.3-Darwin.pkg
    sudo installer -pkg libydk-0.8.3-Darwin.pkg -target /

    print_msg "Installing YDK gNMI service library"
    curl -O https://devhub.cisco.com/artifactory/osx-ydk/0.8.3/libydk_gnmi-0.4.0-2_Darwin.pkg
    sudo installer -pkg libydk_gnmi-0.4.0-2_Darwin.pkg -target /
}

function check_python_installation {
    locate libpython2.7.dylib
    print_msg "Checking python3 and pip3 installation"
    python3 -V
    status=$?
    if [ $status -ne 0 ]; then
        print_msg "Installing python3"
        brew install python@3
    fi
    pip3 -V
    status=$?
    if [ $status -ne 0 ]; then
        print_msg "Installing pip3"
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        sudo -H python3 get-pip.py
    fi
}

# Terminal colors
RED="\033[0;31m"
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

install_os_dependencies

install_libssh

./dependencies_gnmi.sh

install_libydk

check_python_installation
