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

"""Setup for YDK
"""
from __future__ import print_function
import os
'''import shutil
import platform
import subprocess
from git import Repo'''
from codecs import open as copen

from setuptools import setup, find_packages

NMSP_PKG_NAME = "$PACKAGE$"
NMSP_PKG_VERSION = "$VERSION$"
NMSP_PKG_DEPENDENCIES = ["$DEPENDENCY$"]

# Define and modify version number and package name here,
# Namespace packages are share same prefix: "ydk-models"
NAME = 'ydk'
VERSION = '0.5.2'
INSTALL_REQUIREMENTS = ['ecdsa==0.13',
                        'enum34==1.1.3',
                        'lxml==3.4.4',
                        'paramiko==1.15.2',
                        'pyang==1.6',
                        'pycrypto==2.6.1',
                        'Twisted>=16.0.0',
                        'protobuf==3.0.0b2.post2',
                        'ncclient>=0.4.7']

if NMSP_PKG_NAME != "$PACKAGE$":
    NAME = NMSP_PKG_NAME
if NMSP_PKG_VERSION != "$VERSION$":
    VERSION = NMSP_PKG_VERSION
if NMSP_PKG_DEPENDENCIES != ["$DEPENDENCY$"]:
    INSTALL_REQUIREMENTS.extend(NMSP_PKG_DEPENDENCIES)


here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with copen(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

YDK_PACKAGES = find_packages(exclude=['contrib', 'docs*', 'tests*',
                                      'ncclient', 'samples'])
ext = []
'''

lib_path = here + '/.libs'
libnetconf_include_path = here + '/.includes/'
lib_paths = [lib_path]
if platform.system() == 'Darwin' and subprocess.call(['brew info python &> /dev/null'], shell=True) == 0:
    python_homebrew_path='/usr/local/opt/python/Frameworks/Python.framework/Versions/2.7/lib'
    if os.path.isdir(python_homebrew_path) and os.path.exists(python_homebrew_path):
        lib_paths = [lib_path, python_homebrew_path]


def _build_ydk_client_using_prebuilt_libnetconf():
    prebuilt_lib_path = lib_path + '/prebuilt/' + platform.system() + '/libnetconf.a'
    shutil.copy(prebuilt_lib_path, lib_path)
    return subprocess.call(['g++ -I/usr/include/python2.7 -I/usr/include/boost -I' + libnetconf_include_path +
                            ' -shared -fPIC ' + here + '/ydk/providers/_cpp_files/netconf_client.cpp'
                            ' -L/' + lib_path + ' -lnetconf -lpython2.7 -lboost_python -lxml2 -lcurl -lssh -lssh_threads -lxslt'], shell=True)


# Compile the YDK C++ code
if platform.system() != 'Windows':
    libnetconf_path=here + '/.libs/libnetconf/'
    if os.listdir(libnetconf_path) == []:
        print('Checking out libnetconf')
        repo = Repo.clone_from("https://github.com/abhikeshav/libnetconf.git", libnetconf_path)
        repo.git.checkout('57f44ce2425bfb17d231a111995d6537ae4dd7cb')
    exit_status = subprocess.call(['cd ' + here + '/.libs/libnetconf/ && ./configure > /dev/null && make > /dev/null && cp .libs/libnetconf.a .. '], shell=True)
    if exit_status != 0:
        exit_status = _build_ydk_client_using_prebuilt_libnetconf()


    if exit_status != 0:
        print('\nFailed to build libnetconf. Install all the dependencies mentioned in the README. No native code is being built.')
        ext = []
    else:
        ext = [extension.Extension(
                                  'ydk_client',
                                  sources=[here + '/ydk/providers/_cpp_files/netconf_client.cpp'],
                                  language='c++',
                                  libraries=['netconf', 'python2.7', 'boost_python', 'xml2', 'curl', 'ssh', 'ssh_threads', 'xslt'],
                                  extra_compile_args=['-Wall', '-std=c++0x'],
                                  include_dirs=['/usr/include/python2.7', '/usr/include/boost', libnetconf_include_path],
                                  library_dirs=lib_paths
                                  )]
'''
setup(
    name=NAME,
    version=VERSION,
    description='YDK Python SDK',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/CiscoDevNet/ydk-py',
    author='Cisco Systems',
    author_email='yang-dk@cisco.com',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache 2.0 License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='yang',
    packages=YDK_PACKAGES,
    install_requires=INSTALL_REQUIREMENTS,
    ext_modules=ext,
)
