#!/bin/bash

function print_msg {
    echo -e "${MSG_COLOR}*** $(date): tests.sh | $@ ${NOCOLOR}"
}

function run_exec_test {
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
  print_msg "Testing Python installation"
  if [[ $(uname) == "Darwin" ]]; then
    PYTHON_BIN=python3
    PIP_BIN=pip3
  else
    python --version &> _version
    status=$?
    if [ $status -ne 0 ]; then
      MSG_COLOR=$RED
      print_msg "Could not locate Python"
      exit $status
    fi
    PYTHON_VERSION=`cat _version` && rm _version
    print_msg "Retrieved Python version ${PYTHON_VERSION}"

    PYTHON_BIN=python
    PIP_BIN=pip
    if [[ ${PYTHON_VERSION} = *"3."* ]]; then
      PYTHON_BIN=python3
      PIP_BIN=pip3
    fi
  fi
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
    if [[ $(uname) == "Linux" ]] ; then
        os_info=$(cat /etc/*-release)
        if [[ ${os_info} == *"fedora"* ]]; then
            print_msg "Custom pip install of $@ for centos"
            sudo ${PIP_BIN} install --install-option="--install-purelib=/usr/lib64/python2.7/site-packages" --no-deps $@
            return
        fi
    elif [[ $(uname) == "Darwin" ]] ; then
        sudo ${PIP_BIN} install $@
        return
    fi
    sudo ${PIP_BIN} install $@
}

# Terminal colors
RED="\033[0;31m"
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

test_python_installation

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

print_msg "Running codec sample"
cd ../core/samples
${PYTHON_BIN} bgp_codec.py
