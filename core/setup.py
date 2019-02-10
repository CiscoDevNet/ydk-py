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

"""
Setup for YDK core package
"""

from __future__ import print_function
import os
import subprocess
import sysconfig

from setuptools.command.build_ext import build_ext
from setuptools import setup, Extension, find_packages

# Define and modify version number and package name here

NAME = 'ydk'

VERSION = '0.8.1'

INSTALL_REQUIREMENTS = ['pybind11>=2.1.1']

LONG_DESCRIPTION = '''
                   The YANG Development Kit (YDK) is a Software Development Kit
                    that provides API's that are modeled in YANG. The main goal
                    of YDK is to reduce the learning curve of YANG data models by
                    expressing the model semantics in an API and abstracting
                    protocol/encoding details. YDK is composed of a core package
                    that defines services and providers, plus one or more module
                    bundles that are based on YANG models.
                   '''

YDK_PACKAGES = find_packages(exclude=['contrib', 'docs*', 'tests*',
                                      'ncclient', 'samples'])

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class YdkBuildExtension(build_ext):
    def run(self):
        try:
            cmake3_installed = (
            0 == subprocess.call(['which', 'cmake3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
            if not cmake3_installed:
                subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed to build the following extensions: " +
                               ", ".join(e.name for e in self.extensions))

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        try:
            import pybind11
        except ImportError:
            import pip
            pip.main(['install', 'pybind11>=2.1.1'])
            import pybind11

        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        coverage_compiler_flag = '-DCOVERAGE=False'
        if 'YDK_COVERAGE' in os.environ:
            coverage_compiler_flag = '-DCOVERAGE=True'
        cmake_args = ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={0}'.format(extdir),
                      '-DPYBIND11_INCLUDE={0};{1}'.format(
                                      pybind11.get_include(),
                                      pybind11.get_include(user=True)),
                      '-DPYTHON_VERSION={0}'.format(
                                      get_python_version()),
                      '-DCMAKE_BUILD_TYPE=Release',
                      coverage_compiler_flag]

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        cmake3_installed = (0 == subprocess.call(['which', 'cmake3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        if(cmake3_installed):
            cmake_executable = 'cmake3'
        else:
            cmake_executable = 'cmake'

        subprocess.check_call([cmake_executable, ext.sourcedir] + cmake_args, cwd=self.build_temp)
        subprocess.check_call([cmake_executable, '--build', '.'], cwd=self.build_temp)


def get_python_version():
    python_version = sysconfig.get_config_var('LDVERSION')
    if python_version is None or len(python_version) == 0:
        python_version = sysconfig.get_config_var('VERSION')
    return python_version


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
    keywords='yang, C++11, python bindings ',
    packages=YDK_PACKAGES,
    install_requires=INSTALL_REQUIREMENTS,
    ext_modules=[CMakeExtension('ydk_')],
    cmdclass={
             'build_ext' :YdkBuildExtension
             },
    zip_safe=False,
)
