#!/bin/bash

function print_msg {
    echo -e "${MSG_COLOR}*** $(date): dependencies_osx.sh | $@ ${NOCOLOR}"
}

function pip_check_install {
    if [[ $(uname) == "Linux" ]] ; then
        os_info=$(cat /etc/*-release)
        if [[ ${os_info} == *"fedora"* ]]; then
            echo "custom pip install of $@ for centos"
            pip install --install-option="--install-purelib=/usr/lib64/python2.7/site-packages" --no-deps $@
            return
        fi
    elif [[ $(uname) == "Darwin" ]] ; then
        pip install $@
        return
    fi
    pip install $@
}

# Terminal colors
RED="\033[0;31m"
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

print_msg "Installing YDK core package"
cd core
python setup.py sdist
pip install  dist/*.tar.gz

print_msg "Installing ietf bundle package"
cd ../ietf
python setup.py  sdist
pip_check_install  dist/*.tar.gz

print_msg "Installing openconfig bundle package"
cd ../openconfig
python setup.py sdist
pip_check_install  dist/*.tar.gz

print_msg "Installing cisco-ios-xr bundle package"
cd ../cisco-ios-xr
python setup.py sdist
pip_check_install  dist/*.tar.gz

print_msg "Installing cisco-ios-xe bundle package"
cd ../cisco-ios-xe
python setup.py sdist
pip_check_install  dist/*.tar.gz
c
print_msg "Installing cisco-nx-os bundle package"
d ../cisco-nx-os
python setup.py sdist
pip_check_install  dist/*.tar.gz

print_msg "Running codec sample"
cd ../core/samples
./bgp_codec.py
