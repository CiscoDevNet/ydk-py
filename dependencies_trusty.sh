#!/bin/bash

sudo apt-get update > /dev/null
sudo apt-get install libssh-dev libtool gdebi-core python3-dev python-dev -y > /dev/null
sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y > /dev/null
sudo apt-get update > /dev/null
sudo apt-get install cmake gcc-5 g++-5 -y > /dev/null
sudo ln -f -s /usr/bin/g++-5 /usr/bin/c++
sudo ln -f -s /usr/bin/gcc-5 /usr/bin/cc
git clone https://github.com/ciscodevnet/ydk-cpp.git -b 0.7.2
mkdir ydk-cpp/core/ydk/build
cd ydk-cpp/core/ydk/build
cmake -DCMAKE_BUILD_TYPE=Release .. 
sudo make install
cd -
sudo easy_install pip
sudo pip install pybind11
