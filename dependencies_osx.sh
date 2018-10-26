#!/bin/bash

function print_msg {
    echo -e "${MSG_COLOR}*** $(date): dependencies_osx.sh | $@ ${NOCOLOR}"
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
}

function install_libydk {
    print_msg "Installing YDK C++ core library"
    curl -O https://devhub.cisco.com/artifactory/osx-ydk/0.7.3/libydk-0.7.3-Darwin.pkg
    sudo installer -pkg libydk-0.7.3-Darwin.pkg -target /
}

# Terminal colors
RED="\033[0;31m"
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

brew install pybind11
brew reinstall python@3
#brew rm -f --ignore-dependencies python python3

install_libssh

install_libydk

pip3 -V &> /dev/null
status=$?
if [ $status -ne 0 ]; then
    print_msg "Installing pip"
    sudo easy_install pip3
fi
