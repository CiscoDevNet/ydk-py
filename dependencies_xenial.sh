#!/bin/sh

apt-get update -y > /dev/null
apt-get install gdebi-core python-dev python-pip libtool-bin wget sudo -y > /dev/null
add-apt-repository ppa:ubuntu-toolchain-r/test -y
apt-get update > /dev/null
apt-get install gcc-5 g++-5 -y > /dev/null
ln -f -s /usr/bin/g++-5 /usr/bin/c++
ln -f -s /usr/bin/gcc-5 /usr/bin/cc
wget https://devhub.cisco.com/artifactory/debian-ydk/0.7.1/libydk_0.7.1-1_amd64.deb
gdebi -n libydk_0.7.1-1_amd64.deb
sudo easy_install pip
