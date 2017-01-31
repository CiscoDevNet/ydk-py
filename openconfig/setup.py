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
from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

INSTALL_REQUIREMENTS = ['ecdsa==0.13',
                        'enum34==1.1.3',
                        'lxml==3.4.4',
                        'paramiko==1.15.2',
                        'pyang==1.6',
                        'pycrypto==2.6.1',
                        'ncclient>=0.4.7',
                        'ydk>=0.5.2']

NMSP_PKG_NAME = "ydk-models-openconfig"
NMSP_PKG_VERSION = "0.1.1"
NMSP_PKG_DEPENDENCIES = ['ydk-models-ietf>=0.1.1']


if NMSP_PKG_DEPENDENCIES != "$DEPENDENCY$":
    INSTALL_REQUIREMENTS.extend(NMSP_PKG_DEPENDENCIES)

NMSP_PACKAGES = ['ydk', 'ydk.models']
YDK_PACKAGES = find_packages(exclude=['contrib', 'docs*', 'tests*',
                                      'ncclient', 'samples'])


LONG_DESCRIPTION = '''
                   The YANG Development Kit (YDK) is a Software Development Kit
                    that provides API's that are modeled in YANG. The main goal
                    of YDK is to reduce the learning curve of YANG data models by
                    expressing the model semantics in an API and abstracting
                    protocol/encoding details. YDK is composed of a core package
                    that defines services and providers, plus one or more module
                    bundles that are based on YANG models. Each module bundle
                    is generated using a bundle profile and the ydk-gen tool.
                   '''

setup(
    name=NMSP_PKG_NAME,
    version=NMSP_PKG_VERSION,
    description='YDK Python SDK',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/CiscoDevNet/ydk-py',
    author='Cisco Systems',
    author_email='yang-dk@cisco.com',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: C++'
    ],
    keywords='yang, C++11, python bindings',
    packages=YDK_PACKAGES,
    namespace_packages=NMSP_PACKAGES,
    install_requires=INSTALL_REQUIREMENTS
)
