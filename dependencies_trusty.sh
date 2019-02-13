#!/bin/bash

function print_msg {
    echo -e "${MSG_COLOR}*** $(date): dependencies_trusty.sh | $@ ${NOCOLOR}"
}

# Terminal colors
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

print_msg "Installing Trusty OS dependencies"
sudo apt-get update && apt-get install -y --no-install-recommends apt-utils > /dev/null
sudo apt-get install libssh-dev libtool gdebi-core python3-dev python-dev wget -y > /dev/null
sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y > /dev/null
sudo apt-get update > /dev/null

print_msg "Installing C++ version 5"
sudo apt-get install cmake gcc-5 g++-5 -y > /dev/null
sudo ln -f -s /usr/bin/g++-5 /usr/bin/c++
sudo ln -f -s /usr/bin/gcc-5 /usr/bin/cc

print_msg "Installing YDK C++ core library"
git clone https://github.com/ciscodevnet/ydk-cpp.git -b 0.8.1
mkdir ydk-cpp/core/ydk/build
cd ydk-cpp/core/ydk/build
cmake -DCMAKE_BUILD_TYPE=Release ..
sudo make install
cd -

pip -V &> /dev/null
status=$?
if [ $status -ne 0 ]; then
  print_msg "Installing pip"
  curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
  python get-pip.py
fi
