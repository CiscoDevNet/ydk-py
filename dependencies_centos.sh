#!/bin/sh

function print_msg {
    echo -e "${MSG_COLOR}*** $(date): dependencies_centos.sh | $@ ${NOCOLOR}"
}

function check_install_gcc {
  which gcc
  local status=$?
  if [[ $status == 0 ]]
  then
    gcc_version=$(echo $(gcc --version) | awk '{ print $3 }')
    print_msg "Current gcc/g++ version is $gcc_version"
  else
    print_msg "The gcc/g++ not installed"
    gcc_version="4.0"
  fi
  if [[ $(echo $gcc_version | cut -d '.' -f 1) < 5 ]]
  then
    print_msg "Upgrading gcc/g++ to version 5"
    yum install centos-release-scl -y > /dev/null
    yum install devtoolset-4-gcc* -y > /dev/null

    ln -sf /opt/rh/devtoolset-4/root/usr/bin/gcc /usr/bin/cc
    ln -sf /opt/rh/devtoolset-4/root/usr/bin/g++ /usr/bin/c++

    ln -sf /opt/rh/devtoolset-4/root/usr/bin/gcc /usr/bin/gcc
    ln -sf /opt/rh/devtoolset-4/root/usr/bin/g++ /usr/bin/g++

    ln -sf /opt/rh/devtoolset-4/root/usr/bin/gcov /usr/bin/gcov

    gcc_version=$(echo $(gcc --version) | awk '{ print $3 }')
    print_msg "Installed gcc/g++ version is $gcc_version"
  fi
}

function install_ydk_core {
    print_msg "Installing YDK core libraries"
    yum install -y https://devhub.cisco.com/artifactory/rpm-ydk/0.8.2/libydk-0.8.2-1.x86_64.rpm > /dev/null
    print_msg "Installing YDK gNMI Service library"
    yum install -y https://devhub.cisco.com/artifactory/rpm-ydk/0.8.2/libydk_gnmi-0.4.0-2.x86_64.rpm > /dev/null
}

# Terminal colors
RED="\033[0;31m"
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

os_info=$(cat /etc/*-release)
print_msg "OS info: $os_info"

yum install -y epel-release
yum install -y libxslt-devel libssh-devel python-devel cmake3 python-pip which make sudo > /dev/null

check_install_gcc

./dependencies_gnmi.sh

install_ydk_core
