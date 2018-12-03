#!/bin/sh

function print_msg {
    echo -e "${MSG_COLOR}*** $(date): dependencies_xenial.sh | $@ ${NOCOLOR}"
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
apt-get install gdebi-core python-dev python-pip libtool-bin wget sudo -y > /dev/null
add-apt-repository ppa:ubuntu-toolchain-r/test -y
apt-get update > /dev/null
apt-get install gcc-5 g++-5 -y > /dev/null
ln -f -s /usr/bin/g++-5 /usr/bin/c++
ln -f -s /usr/bin/gcc-5 /usr/bin/cc

print_msg "Installing YDK 0.8.0 core library"
if [[ $os_info == *"xenial"* ]]; then
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.0/xenial/libydk_0.8.0-1_amd64.deb
elif [[ $os_info == *"bionic"* ]]; then
    run_cmd wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.0/bionic/libydk_0.8.0-1_amd64.deb
else
    MSG_COLOR=$RED
    print_msg "There are no pre-compiled YDK libraries for this Linux distribution"
    exit 1
fi
gdebi -n libydk_0.8.0-1_amd64.deb

#wget https://devhub.cisco.com/artifactory/debian-ydk/0.8.0/xenial/libydk_0.8.0-1_amd64.deb

sudo easy_install pip
