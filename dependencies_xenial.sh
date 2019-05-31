#!/bin/bash

function print_msg {
    echo -e "$MSG_COLOR*** $(date): dependencies_xenial.sh | $@ $NOCOLOR"
}

function run_cmd {
    print_msg "Running command: $@"
    $@
    local status=$?
    if [ $status -ne 0 ]; then
        MSG_COLOR=$RED
        print_msg "Exiting '$@' with status=$status"
        exit $status
    fi
    return $status
}

function check_install_gcc {
  print_msg "Checking g++ installation"
  which g++
  local status=$?
  if [[ $status == 0 ]]
  then
    gpp_version=$(echo $(g++ --version) | awk '{ print $3 }' | cut -d '-' -f 1)
    print_msg "Current g++ version is $gpp_version"
  else
    print_msg "The g++ is not installed"
    gpp_version="4.0"
  fi

  if [[ $(echo $gpp_version | cut -d '.' -f 1) < 5 ]]
  then
    print_msg "Upgrading gcc/g++ to version 5"
    sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y
    sudo apt-get update > /dev/null
    sudo apt-get install gcc-5 g++-5 -y > /dev/null
    sudo ln -fs /usr/bin/g++-5 /usr/bin/c++
    sudo ln -fs /usr/bin/gcc-5 /usr/bin/cc
    gcc_version=$(echo $(gcc --version) | awk '{ print $3 }' | cut -d '-' -f 1)
    print_msg "Installed gcc version is $gcc_version"
    gpp_version=$(echo $(g++ --version) | awk '{ print $3 }' | cut -d '-' -f 1)
    print_msg "Installed g++ version is $gpp_version"
  fi
}

function install_ydk_core {
  print_msg "Installing YDK core and gNMI service libraries"
  if [[ $os_info == *"xenial"* ]]; then
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.3/xenial/libydk-0.8.3-1.amd64.deb
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.3/xenial/libydk_gnmi-0.4.0-2.amd64.deb
  elif [[ $os_info == *"bionic"* ]]; then
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.3/bionic/libydk-0.8.3-1.amd64.deb
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.3/bionic/libydk_gnmi-0.4.0-2.amd64.deb
  else
    MSG_COLOR=$RED
    print_msg "There are no pre-compiled YDK libraries for this Linux distribution"
    exit 1
  fi
  gdebi -n libydk-0.8.3-1.amd64.deb
  gdebi -n libydk_gnmi-0.4.0-2.amd64.deb
}

# Terminal colors
RED="\033[0;31m"
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

os_info=$(cat /etc/*-release)
print_msg "OS info: $os_info"

apt-get update -y > /dev/null
apt-get install gdebi-core python-dev python-pip python3-dev python3-pip libtool-bin wget sudo unzip git -y
apt-get install libpcre3-dev libpcre++-dev libssh-dev libxml2-dev libxslt1-dev -y

check_install_gcc

./dependencies_gnmi.sh

install_ydk_core
