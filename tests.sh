#!/bin/bash

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

cd core
python setup.py sdist
pip install  dist/*.tar.gz
cd ../ietf
python setup.py  sdist
pip_check_install  dist/*.tar.gz
cd ../openconfig
python setup.py sdist
pip_check_install  dist/*.tar.gz
cd ../cisco-ios-xr
python setup.py sdist
pip_check_install  dist/*.tar.gz
cd ../cisco-ios-xe
python setup.py sdist
pip_check_install  dist/*.tar.gz

echo "Running codec sample"
cd ../core/samples
./bgp_codec.py
