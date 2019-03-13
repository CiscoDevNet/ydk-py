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
  which gcc
  local status=$?
  if [[ $status == 0 ]]
  then
    gcc_version=$(echo $(gcc --version) | awk '{ print $3 }' | cut -d '-' -f 1)
    print_msg "Current gcc/g++ version is $gcc_version"
  else
    print_msg "The gcc/g++ not installed"
    gcc_version="4.0"
  fi
  gcc_version=$(echo `gcc --version` | awk '{ print $3 }' | cut -d '-' -f 1)
  print_msg "Current gcc/g++ version is $gcc_version"
  if [[ $(echo $gcc_version | cut -d '.' -f 1) < 5 ]]
  then
    print_msg "Upgrading gcc/g++ to version 5"
    sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y
    sudo apt-get update > /dev/null
    sudo apt-get install gcc-5 g++-5 -y > /dev/null
    sudo ln -fs /usr/bin/g++-5 /usr/bin/c++
    sudo ln -fs /usr/bin/gcc-5 /usr/bin/cc
    gcc_version=$(echo $(gcc --version) | awk '{ print $3 }' | cut -d '-' -f 1)
    print_msg "Installed gcc/g++ version is $gcc_version"
  fi
}

function install_ydk_core {
  print_msg "Installing YDK core and gNMI service libraries"
  if [[ $os_info == *"xenial"* ]]; then
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.2/xenial/libydk_0.8.2-1_amd64.deb
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.2/xenial/libydk_gnmi_0.4.0-2.amd64.deb
  elif [[ $os_info == *"bionic"* ]]; then
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.2/bionic/libydk_0.8.2-1_amd64.deb
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.2/bionic/libydk_gnmi_0.4.0-2.amd64.deb
  else
    MSG_COLOR=$RED
    print_msg "There are no pre-compiled YDK libraries for this Linux distribution"
    exit 1
  fi
  gdebi -n libydk_0.8.2-1_amd64.deb
  gdebi -n libydk_gnmi_0.4.0-2.amd64.deb
}

# Terminal colors
RED="\033[0;31m"
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

os_info=$(cat /etc/*-release)
print_msg "OS info: $os_info"

apt-get update -y > /dev/null
apt-get install gdebi-core python-dev python-pip libtool-bin wget sudo unzip -y

./dependencies_gnmi.sh

check_install_gcc
install_ydk_core
