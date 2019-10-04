#!/bin/bash

function print_msg {
    echo -e "$MSG_COLOR*** $(date): dependencies_ubuntu.sh | $@ $NOCOLOR"
}

function run_cmd {
    print_msg "Running command: $@"
    $@
    local status=$?
    if [[ $status -ne 0 ]]; then
        MSG_COLOR=$RED
        print_msg "Exiting '$@' with status=$status"
        exit $status
    fi
    return $status
}

function install_dependencies {
    print_msg "Installing dependencies"

    apt update -y > /dev/null
    apt install sudo -y > /dev/null
    sudo apt-get install -y --no-install-recommends apt-utils
    sudo apt-get update -y > /dev/null
    sudo apt-get install libtool-bin -y > /dev/null
    local status=$?
    if [[ ${status} != 0 ]]; then
        sudo apt-get install libtool -y > /dev/null
    fi
    sudo apt-get install -y bison \
                            curl \
                            doxygen \
                            flex \
                            git \
                            libcmocka0 \
                            libcurl4-openssl-dev \
                            libpcre3-dev \
                            libpcre++-dev \
                            libssh-dev \
                            libxml2-dev \
                            libxslt1-dev \
                            pkg-config \
                            python-dev \
                            python-pip \
                            python3-dev \
                            python-lxml \
                            python3-lxml \
                            python3-pip \
                            python-virtualenv \
                            software-properties-common \
                            unzip \
                            wget \
                            zlib1g-dev\
                            cmake \
                            openjdk-8-jre \
                            gdebi-core\
                            lcov > /dev/null
    sudo apt-get install -y valgrind
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

function install_libydk {
  print_msg "Installing YDK 0.8.4 core library"
  if [[ $os_info == *"xenial"* ]]; then
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.4/xenial/libydk-0.8.4-1.amd64.deb
  elif [[ $os_info == *"bionic"* ]]; then
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.4/bionic/libydk-0.8.4-1.amd64.deb
  else
    MSG_COLOR=$RED
    print_msg "There are no pre-compiled YDK libraries for this Linux distribution"
    exit 1
  fi
  gdebi -n libydk-0.8.4-1.amd64.deb}
}

# Terminal colors
RED="\033[0;31m"
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

os_info=$(cat /etc/*-release)
print_msg "OS info: $os_info"

install_dependencies
check_install_gcc
install_libydk


