#!/bin/sh

yum install -y epel-release
yum install -y libxslt-devel libssh-devel python36-devel cmake3 python36-pip which make sudo > /dev/null
yum install -y https://devhub.cisco.com/artifactory/rpm-ydk/0.8.4/libydk-0.8.4-1.x86_64.rpm > /dev/null

#yum install centos-release-scl -y > /dev/null
#yum install devtoolset-4-gcc* -y > /dev/null

#ln -sf /opt/rh/devtoolset-4/root/usr/bin/gcc /usr/bin/cc
#ln -sf /opt/rh/devtoolset-4/root/usr/bin/g++ /usr/bin/c++

sudo easy_install pip
