#!/bin/bash
#========================================================
# The script is designed to install ydk-py components
# in Python3 development environment.
# 
# NOTE-2! This script is designed for LINUX platform only  
#========================================================

function print_msg {
    echo -e "${MSG_COLOR}*** $(date): tests_py3.sh | $@ ${NOCOLOR}"
}

function run_cmd {
    local cmd=$@
    print_msg "Running command: $cmd"
    $cmd
    local status=$?
    if [ $status -ne 0 ]; then
        MSG_COLOR=$RED
        print_msg "Exiting '$cmd' with status=$status"
        exit $status
    fi
    return $status
}

function test_python_installation {
    PYTHON_BIN=python3
    PIP_BIN=pip3

    print_msg "Checking installation of ${PYTHON_BIN}"
    ${PYTHON_BIN} -V
    status=$?
    if [ $status -ne 0 ]; then
        MSG_COLOR=$RED
        print_msg "Could not locate ${PYTHON_BIN}"
        exit $status
    fi
    print_msg "Checking installation of ${PIP_BIN}"
    ${PIP_BIN} -V
    status=$?
    if [ $status -ne 0 ]; then
        MSG_COLOR=$RED
        print_msg "Could not locate ${PIP_BIN}"
        exit $status
    fi
    print_msg "Python location: $(which ${PYTHON_BIN})"
    print_msg "Pip location: $(which ${PIP_BIN})"
}

function pip_check_install {
    if [[ ${os_info} == *"fedora"* ]]; then
        print_msg "Custom pip install of $@ for centos"
        sudo ${PIP_BIN} install --install-option="--install-purelib=/usr/lib64/python2.7/site-packages" --no-deps $@
        return
    fi
    sudo ${PIP_BIN} install --no-deps $@
}

# Terminal colors
RED="\033[0;31m"
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

test_python_installation

os_type=$(uname)
if [[ ${os_type} == "Linux" ]] ; then
    os_info=$(cat /etc/*-release)
else
    os_info=$(sw_vers)
fi

YDK_HOME=`pwd`

if [[ $(uname) == "Linux" && ${os_info} == *"fedora"* ]] ; then
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$YDK_HOME/grpc/libs/opt:$YDK_HOME/protobuf-3.5.0/src/.libs:/usr/local/lib64
   print_msg "LD_LIBRARY_PATH is set to: $LD_LIBRARY_PATH"
fi

print_msg "Installing YDK core package"
cd core
${PYTHON_BIN} setup.py sdist
sudo ${PIP_BIN} install  dist/ydk*.tar.gz

print_msg "Testing YDK core installation"
${PYTHON_BIN} -c "import ydk.types"
status=$?
if [ $status -ne 0 ]; then
    MSG_COLOR=$RED
    print_msg "Exiting with status=$status"
    exit $status
fi

print_msg "Installing YDK gNMI package"
cd ../gnmi
${PYTHON_BIN} setup.py sdist
sudo ${PIP_BIN} install dist/ydk*.tar.gz

print_msg "Testing YDK gNMI installation"
${PYTHON_BIN} -c "import ydk.gnmi.providers"
status=$?
if [ $status -ne 0 ]; then
    MSG_COLOR=$RED
    print_msg "Exiting with status=$status"
    exit $status
fi

print_msg "Installing ietf bundle package"
cd ../ietf
${PYTHON_BIN} setup.py  sdist
pip_check_install  dist/*.tar.gz

print_msg "Installing openconfig bundle package"
cd ../openconfig
${PYTHON_BIN} setup.py sdist
pip_check_install  dist/*.tar.gz

print_msg "Installing cisco-ios-xr bundle package"
cd ../cisco-ios-xr
${PYTHON_BIN} setup.py sdist
pip_check_install  dist/*.tar.gz

print_msg "Installing cisco-ios-xe bundle package"
cd ../cisco-ios-xe
${PYTHON_BIN} setup.py sdist
pip_check_install  dist/*.tar.gz

print_msg "Installing cisco-nx-os bundle package"
cd ../cisco-nx-os
${PYTHON_BIN} setup.py sdist
pip_check_install  dist/*.tar.gz

print_msg "Checking ${PYTHON_BIN} environment"
run_cmd ${PIP_BIN} list

print_msg "Running codec sample test"
cd ../core/samples
${PYTHON_BIN} bgp_codec.py
