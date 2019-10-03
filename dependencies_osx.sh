#!/bin/bash

function print_msg {
    echo -e "${MSG_COLOR}*** $(date): dependencies_osx.sh | $@ ${NOCOLOR}"
}

function install_os_dependencies {
    brew install curl xml2 doxygen pybind11
    brew rm -f --ignore-dependencies python python3
}

function install_libssh {
    print_msg "Installing libssh-0.7.6"
    brew reinstall openssl
    export OPENSSL_ROOT_DIR=/usr/local/opt/openssl
    wget https://git.libssh.org/projects/libssh.git/snapshot/libssh-0.7.6.tar.gz
    tar zxf libssh-0.7.6.tar.gz && rm -f libssh-0.7.6.tar.gz
    mkdir libssh-0.7.6/build && cd libssh-0.7.6/build
    cmake ..
    sudo make install
    cd -
#    wget https://devhub.cisco.com/artifactory/osx-ydk/third-party/libssh-0.7.5.pkg
#    sudo installer -pkg libssh-0.7.5.pkg -target /
}

function install_libydk {
    print_msg "Installing YDK C++ core library"
    curl -O https://devhub.cisco.com/artifactory/osx-ydk/0.8.4/libydk-0.8.4-Darwin.pkg
    sudo installer -pkg libydk-0.8.4-Darwin.pkg -target /
}

# Terminal colors
RED="\033[0;31m"
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

install_os_dependencies

install_libssh

install_libydk

print_msg "Checking python3 and pip3 installation"
python3 -V &> /dev/null
status=$?
if [ $status -ne 0 ]; then
    print_msg "Installing python3"
    brew install python@3
fi
pip3 -V &> /dev/null
status=$?
if [ $status -ne 0 ]; then
    print_msg "Installing pip3"
    sudo easy_install pip3
fi
