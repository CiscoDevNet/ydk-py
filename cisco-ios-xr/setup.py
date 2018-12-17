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

INSTALL_REQUIREMENTS = ['ydk>=0.7.3']

NMSP_PKG_NAME = "ydk-models-cisco-ios-xr"
NMSP_PKG_VERSION = "6.5.1_post1"
NMSP_PKG_DEPENDENCIES = ['ydk-models-ietf>=0.1.5-post2']


if NMSP_PKG_DEPENDENCIES != "$DEPENDENCY$":
    INSTALL_REQUIREMENTS.extend(NMSP_PKG_DEPENDENCIES)

NMSP_PACKAGES = ['ydk', 'ydk.models']
YDK_PACKAGES = find_packages(exclude=['contrib', 'docs*', 'tests*',
                                      'ncclient', 'samples'])


DESCRIPTION = "YDK bundle for Cisco IOS XR models"
LONG_DESCRIPTION = "This YANG Development Kit (YDK) bundle provides APIs for Cisco IOS XR YANG models. YDK facilitates the use of YANG data models by expressing the model semantics in an API and abstracting protocol/encoding details.  YDK is composed of a core package that defines services and providers, plus one or more module bundles.  This YDK bundle for Cisco IOS XR models uses the YDK core package and additional model bundles.  You can find the SDK documentation at http://ydk.cisco.com/py/docs  You can find more details on YDK at http://ydk.io"

setup(
    name=NMSP_PKG_NAME,
    version=NMSP_PKG_VERSION,
    description=DESCRIPTION,
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
    keywords='yang, C++11,  python bindings',
    packages=YDK_PACKAGES,
    namespace_packages=NMSP_PACKAGES,
    install_requires=INSTALL_REQUIREMENTS,
    include_package_data=True
)
