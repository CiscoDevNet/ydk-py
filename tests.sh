#!/bin/bash

function print_msg {
    echo -e "${MSG_COLOR}*** $(date): tests.sh | $@ ${NOCOLOR}"
}

function test_python_installation {
  PYTHON_BIN=python3
  PIP_BIN=pip3

  print_msg "Checking installation of ${PYTHON_BIN}"
  ${PYTHON_BIN} --version &> /dev/null
  status=$?
  if [ $status -ne 0 ]; then
    MSG_COLOR=$RED
    print_msg "Could not locate ${PYTHON_BIN}"
    exit $status
  fi
  print_msg "Checking installation of ${PIP_BIN}"
  ${PIP_BIN} -V &> /dev/null
  status=$?
  if [ $status -ne 0 ]; then
    MSG_COLOR=$RED
    print_msg "Could not locate ${PIP_BIN}"
    exit $status
  fi
  print_msg "Python location: $(which ${PYTHON_BIN})"
  print_msg "Pip location: $(which ${PIP_BIN})"

  if [[ $(uname) == "Darwin" ]] ; then
    python_lib_location=$(dirname $(locate libpython3.7.dylib | head -n 1))
    export CMAKE_LIBRARY_PATH=${python_lib_location}:/usr/local/lib
    print_msg "Setting CMAKE_LIBRARY_PATH to ${CMAKE_LIBRARY_PATH}"
  fi
}

function pip_check_install {
#    if [[ $(uname) == "Linux" ]] ; then
#        os_info=$(cat /etc/*-release)
#        if [[ ${os_info} == *"fedora"* ]]; then
#            print_msg "Custom pip install of $@ for centos"
#            sudo ${PIP_BIN} install --install-option="--install-purelib=/usr/lib64/python2.7/site-packages" --no-deps $@
#            return
#        fi
#    elif [[ $(uname) == "Darwin" ]] ; then
#        sudo ${PIP_BIN} install $@
#        return
#    fi
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
sudo ${PIP_BIN} install -v dist/ydk*.tar.gz
${PYTHON_BIN} -c "import ydk.providers"
status=$?
if [[ ${status} != 0 ]]; then
  MSG_COLOR=${RED}
  print_msg "Simple YDK package installation test failed. Exiting"
  exit 1
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
