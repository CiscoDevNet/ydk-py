#!/bin/sh

function print_msg {
    echo -e "${MSG_COLOR}*** $(date) *** dependencies_centos.sh | $@ ${NOCOLOR}"
}

function install_confd {
    print_msg "Installing confd"

    wget https://github.com/CiscoDevNet/ydk-gen/files/562538/confd-basic-6.2.linux.x86_64.zip &> /dev/null
    unzip confd-basic-6.2.linux.x86_64.zip
    ./confd-basic-6.2.linux.x86_64.installer.bin ../confd
}

function install_openssl {
    print_msg "Installing openssl 0.1.0u for confd"

    wget https://www.openssl.org/source/openssl-1.0.1u.tar.gz &> /dev/null
    tar -xvzf openssl-1.0.1u.tar.gz > /dev/null
    cd openssl-1.0.1u
    ./config shared  > /dev/null && make all > /dev/null
#    cp libcrypto.so.1.0.0 ../../confd/lib
    cd -
}

function install_dependencies {
    print_msg "Installing dependencies"

    yum update -y > /dev/null
    yum install epel-release -y > /dev/null
    yum install https://centos7.iuscommunity.org/ius-release.rpm -y > /dev/null
    yum install git which libxml2-devel libxslt-devel libssh-devel libtool gcc-c++ pcre-devel -y > /dev/null
    yum install cmake3 wget curl-devel unzip make sudo -y > /dev/null
    yum install python3-devel -y

    print_msg "Python3 location: $(which python3)"
    print_msg "Pip3 location: $(which pip3)"
}

########################## EXECUTION STARTS HERE #############################
# Terminal colors
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

install_dependencies
install_openssl
# install_confd

print_msg "Installing YDK C++ core package"
yum install -y https://devhub.cisco.com/artifactory/rpm-ydk/0.8.4/libydk-0.8.4-1.x86_64.rpm
