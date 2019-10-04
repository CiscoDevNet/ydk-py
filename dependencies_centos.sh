#!/bin/sh

yum install -y epel-release
yum install -y which cmake3 make sudo gcc
yum install -y libxslt-devel libssh-devel python36-devel python36-pip
yum install -y https://devhub.cisco.com/artifactory/rpm-ydk/0.8.4/libydk-0.8.4-1.x86_64.rpm

#yum install centos-release-scl -y > /dev/null
#yum install devtoolset-4-gcc* -y > /dev/null

#ln -sf /opt/rh/devtoolset-4/root/usr/bin/gcc /usr/bin/cc
#ln -sf /opt/rh/devtoolset-4/root/usr/bin/g++ /usr/bin/c++

