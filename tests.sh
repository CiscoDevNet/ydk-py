#!/bin/bash

function print_msg {
    echo -e "${MSG_COLOR}*** $(date): tests.sh | $@ ${NOCOLOR}"
}

function run_cmd {
    print_msg "Running command: $@"
    $@
    local status=$?
    if [[ ${status} -ne 0 ]]; then
        MSG_COLOR=$RED
        print_msg "Exiting '$@' with status=${status}"
        exit ${status}
    fi
    return ${status}
}

function test_python_installation {
  PYTHON_VERSION=3
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

  if [[ $(uname) == "Linux" && ${os_info} == *"fedora"* && ${PYTHON_VERSION} == "3"* ]]; then
    YDK_HOME=$(pwd)
    print_msg "Creating Python3 virtual environment in ${YDK_HOME}/venv"
    run_cmd ${PYTHON_BIN} -m venv ${YDK_HOME}/venv
    run_cmd source ${YDK_HOME}/venv/bin/activate
  fi

  print_msg "Python location: $(which ${PYTHON_BIN})"
  print_msg "Pip location: $(which ${PIP_BIN})"
}

function pip_check_install {
    if [[ $(uname) == "Linux" && ${os_info} == *"fedora"* && ${PYTHON_VERSION} == "2"* ]]; then
        print_msg "Custom pip install of $@ for centos"
        ${PIP_BIN} install --install-option="--install-purelib=/usr/lib64/python2.7/site-packages" --no-deps $@
    else
        ${PIP_BIN} install $@
    fi
}

# Terminal colors
RED="\033[0;31m"
NOCOLOR="\033[0m"
YELLOW='\033[1;33m'
MSG_COLOR=$YELLOW

os_type=$(uname)
if [[ ${os_type} == "Linux" ]] ; then
    os_info=$(cat /etc/*-release)
else
    os_info=$(sw_vers)
fi
print_msg "Running OS type: $os_type"
print_msg "OS info: $os_info"

test_python_installation

if [[ $(uname) == "Linux" && ${os_info} == *"fedora"* ]] ; then
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib64:/usr/local/lib64:/usr/local/lib
   print_msg "LD_LIBRARY_PATH is set to: $LD_LIBRARY_PATH"
fi

print_msg "Installing YDK core package"
cd core
${PYTHON_BIN} setup.py sdist
${PIP_BIN} install -v dist/ydk*.tar.gz

print_msg "Running simple YDK package installation test"
${PYTHON_BIN} -c "from ydk.providers import CodecServiceProvider"
status=$?
if [[ ${status} != 0 ]]; then
  MSG_COLOR=${RED}
  print_msg "YDK package installation test failed. Exiting"
  exit ${status}
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
