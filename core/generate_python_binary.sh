#! /bin/bash
#  ----------------------------------------------------------------
# Copyright 2016 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------
#
# Script for generating ydk-py binary
#
# ------------------------------------------------------------------


######################################################################
# Utility functions
######################################################################

function check_for_fpm {
    fpm -v &> /dev/null
    local status=$?
    if [ $status -ne 0 ]; then
        printf "${RED}\nERROR: Please install fpm as specified at http://fpm.readthedocs.io/en/latest/installing.html\n\n${NOCOLOR}"
        exit $status
    fi
}

function check_for_setup_py {
    if [[ ! -f "setup.py" ]]; then
        printf "${RED}\nERROR: setup.py not found\n\n${NOCOLOR}"
        exit 1
    fi
}

function get_target_binary_type {
    if [[ $(uname) == "Darwin" ]] ; then
        target_binary_type='osxpkg'
    else
        grep -q "debian" /etc/*-release
        local status=$?
        if [[ "${status}" == "0" ]]; then
            target_binary_type='deb'
        else
            target_binary_type='rpm'
        fi
    fi
}

######################################################################
# Generate python binaries
######################################################################

function compile_and_generate_python2_binaries {
    python26_installed=$(command -v python2.6 2> /dev/null)
    python27_installed=$(command -v python2.7 2> /dev/null)
    if [[ ${python27_installed} ]]; then
        PYTHON_BINARY=python2.7
        PYTHON_PIP=pip2.7
        PYTHON_PREFIX=python27
    elif [[ ${python26_installed} ]]; then
        PYTHON_BINARY=python2.6
        PYTHON_PIP=pip2.6
        PYTHON_PREFIX=python26
    else
        printf "\nWARNING: python2 not installed\n"
    fi
    printf "Generating python2 binary for ${PYTHON_BINARY}...\n\n"
    fpm -s python -t ${target_binary_type} ${verbose} --python-package-name-prefix ${PYTHON_PREFIX} --python-bin ${PYTHON_BINARY} --python-pip ${PYTHON_PIP} --no-python-dependencies setup.py
    local status=$?
    if [ $status -ne 0 ]; then
        exit $status
    fi
    printf "\nSuccessfully generated binaries at $(pwd)\n\n"
}

function compile_and_generate_python3_binaries {
    python36_installed=$(command -v python3.6 2> /dev/null)
    python34_installed=$(command -v python3.4 2> /dev/null)
    if [[ ${python36_installed} ]]; then
        PYTHON_BINARY=python3.6
        PYTHON_PIP=pip3.6
        PYTHON_PREFIX=python36
    elif [[ ${python34_installed} ]]; then
        PYTHON_BINARY=python3.4
        PYTHON_PIP=pip3.4
        PYTHON_PREFIX=python34
    else
        printf "\nWARNING: python3 not installed\n"
    fi
    printf "Generating python3 binary for ${PYTHON_BINARY}...\n\n"
    fpm -s python -t ${target_binary_type} ${verbose} --python-package-name-prefix ${PYTHON_PREFIX} --python-bin ${PYTHON_BINARY} --python-pip ${PYTHON_PIP} --no-python-dependencies setup.py
    local status=$?
    if [ $status -ne 0 ]; then
        exit $status
    fi
    printf "\nSuccessfully generated binaries at $(pwd)\n\n"
}

function compile_and_generate_python_binaries {
    get_target_binary_type

    echo "OS type: ${target_binary_type}"

    compile_and_generate_python2_binaries
    compile_and_generate_python3_binaries
}

########################## EXECUTION STARTS HERE #############################
SCRIPT_LOCATION="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd ${SCRIPT_LOCATION}

target_binary_type=""
verbose=""
RED="\033[0;31m"
NOCOLOR="\033[0m"

for arg in "$@"
do
    if [[ ${arg} == "-v" ]]; then
        verbose="--verbose"
    elif [[ ${arg} == "-h" ]]; then
        printf "\nUsage:\n\t$0 [-v]\n\n"
        exit 0
    fi
done

check_for_setup_py
check_for_fpm
compile_and_generate_python_binaries

cd - &> /dev/null
