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

# Terminal colors
RED="\033[0;31m"
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

os_info=$(cat /etc/*-release)
print_msg "OS info: $os_info"

apt-get update -y > /dev/null
apt-get install gdebi-core python-dev python-pip libtool-bin wget sudo unzip -y

print_msg "Installing C/C++ version 5"
apt-get install gcc-5 g++-5 -y > /dev/null
ln -fs /usr/bin/g++-5 /usr/bin/c++
ln -fs /usr/bin/gcc-5 /usr/bin/cc

./dependencies_gnmi.sh

print_msg "Installing YDK 0.8.0 core library"
if [[ $os_info == *"xenial"* ]]; then
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.1/xenial/libydk_0.8.1-1_amd64.deb
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.1/xenial/libydk_gnmi_0.4.1-1_amd64.deb
elif [[ $os_info == *"bionic"* ]]; then
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.1/bionic/libydk_0.8.1-1_amd64.deb
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.1/bionic/libydk_gnmi_0.4.0-1_amd64.deb
else
    MSG_COLOR=$RED
    print_msg "There are no pre-compiled YDK libraries for this Linux distribution"
    exit 1
fi
gdebi -n libydk_0.8.1-1_amd64.deb
gdebi -n libydk_gnmi_0.4.0-1_amd64.deb
