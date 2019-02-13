#!/bin/sh

yum install -y epel-release
yum install -y libxslt-devel libssh-devel python-devel cmake3 python-pip which make sudo > /dev/null
./dependencies_gnmi.sh

yum install -y https://devhub.cisco.com/artifactory/rpm-ydk/0.8.1/libydk-0.8.1-1.x86_64.rpm > /dev/null
yum install https://devhub.cisco.com/artifactory/rpm-ydk/0.8.1/libydk_gnmi_0.4.0-1.x86_64.rpm > /dev/null

yum install centos-release-scl -y > /dev/null
yum install devtoolset-4-gcc* -y > /dev/null

ln -sf /opt/rh/devtoolset-4/root/usr/bin/gcc /usr/bin/cc
ln -sf /opt/rh/devtoolset-4/root/usr/bin/g++ /usr/bin/c++

sudo easy_install pip
