.. image::  https://travis-ci.org/CiscoDevNet/ydk-py.svg?branch=master
    :target: https://travis-ci.org/CiscoDevNet/ydk-py

=============================
YANG Development Kit (Python)
=============================

.. contents:: Table of Contents

Overview
--------

The YANG Development Kit (YDK) is a Software Development Kit that provides API's that are modeled in YANG. The main goal of YDK is to reduce the learning curve of YANG data models by expressing the model semantics in an API and abstracting protocol/encoding details.  YDK is composed of a core package that defines services and providers, plus one or more module bundles that are based on YANG models.

Backward Compatibility
----------------------
Please see `the release notes <https://github.com/CiscoDevNet/ydk-py/releases/tag/0.6.0>`_ and `documentation <http://ydk.cisco.com/py/docs/guides/backward_compatibility.html>`_ for details on some backward incompatible changes introduced as part of the 0.6.0 release.


System Requirements
-------------------
Linux
~~~~~
Ubuntu (Debian-based) - The following packages must be present in your system before installing YDK-Py::

   $ sudo apt-get install gdebi-core python3-dev python-dev libtool-bin
   $ wget https://devhub.cisco.com/artifactory/debian-ydk/0.6.0/libydk_0.6.0-1_amd64.deb
   $ sudo gdebi libydk_0.6.0-1_amd64.deb

Centos (Fedora-based) - The following packages must be present in your system before installing YDK-Py::

   $ sudo yum install epel-release libssh-devel gcc-c++
   $ sudo yum install https://devhub.cisco.com/artifactory/rpm-ydk/0.6.0/libydk-0.6.0-1.x86_64.rpm
   $ sudo ln –fs /usr/bin/cmake3 /usr/bin/cmake && export PATH=/usr/bin:$PATH

macOS
~~~~~
It is required to install Xcode command line tools, `homebrew <http://brew.sh>`_ and the following homebrew packages on your system before installing YDK-Py::

   $ xcode-select --install
   $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   $ brew install python pkg-config libssh xml2 curl pcre cmake
   $ curl -O https://devhub.cisco.com/artifactory/osx-ydk/0.6.0/libydk-0.6.0-Darwin.pkg
   $ sudo installer -pkg libydk-0.6.0-Darwin.pkg -target /

Windows
~~~~~~~
Currently, YDK-Py from release 0.6.0 onwards is not supported on Windows.


Python Requirements
-------------------
Both Python 2 and 3 are supported.  At least, Python2.7 or Python 3.4 must be installed in your system.

How to install
--------------
Quick Install
~~~~~~~~~~~~~
You can install the latest model packages from the Python package index.  Note that, in some systems, you need to install the new package as root.  You get a fully operational YDK environment by installing the ``cisco-ios-xr`` bundle which automatically installs all other YDK-related packages (``ydk``, ``cisco-ios-xr``, ``openconfig`` and ``ietf`` packages)::

  $ pip install ydk-models-cisco-ios-xr

Alternatively, you can perform a partial installation.  If you only want to install the ``openconfig`` bundle and its dependencies (``ydk`` and ``ietf`` packages), execute::

  $ pip install ydk-models-openconfig

If you only want to install the ``ietf`` bundle and its dependencies (``ydk`` package), execute::

  $ pip install ydk-models-ietf

Installing from Source
~~~~~~~~~~~~~~~~~~~~~~
If you prefer not to use the YDK packages in the Python package index, you need to install manually the ``ydk`` core package and then the model bundles you plan to use.  To install the ``ydk`` core package, execute::

  $ cd core
  core$ python setup.py sdist
  core$ pip install dist/ydk*.gz

Once you have installed the ``ydk`` core package, you can install one more model bundles.  Note that some bundles have dependencies on other bundles.  Those dependencies are already captured in the bundle package.  Make sure you install the desired bundles in the order below.  To install the ``ietf`` bundle, execute::

  core$ cd ../ietf
  ietf$ python setup.py sdist
  ietf$ pip install dist/ydk*.gz

To install the ``openconfig`` bundle, execute::

  ietf$ cd ../openconfig
  openconfig$ python setup.py sdist
  openconfig$ pip install dist/ydk*.gz

To install the ``cisco-ios-xr`` bundle, execute::

  openconfig$ cd ../cisco-ios-xr
  cisco-ios-xr$ python setup.py sdist
  cisco-ios-xr$ pip install dist/ydk*.gz
  cisco-ios-xr$ cd ..

Using a Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~
You may want to perform the installation under a Python virtual environment (`virtualenv <https://pypi.python.org/pypi/virtualenv/>`_/`virtualenvwrapper  <https://pypi.python.org/pypi/virtualenvwrapper>`_).  A virtual environment allows you to install multiple versions of YDK if needed.  In addition, it prevents any potential conflicts between package dependencies in your system.

To install virtual environment support in your system, execute::

  $ pip install virtualenv virtualenvwrapper
  $ source /usr/local/bin/virtualenvwrapper.sh

In some systems (e.g. Debian-based Linux), you need to install support for Python virtual environments as root::

  $ sudo pip install virtualenv virtualenvwrapper
  $ source /usr/local/bin/virtualenvwrapper.sh

Create a new virtual environment::

  $ mkvirtualenv -p python2.7 ydk-py

At this point, you can perform the quick install or the installation from source described above.  Take into account that must not attempt to install YDK as root under a virtual environment.

Documentation and Support
--------------------------
- Read the `API documentation <http://ydk.cisco.com/py/docs>`_ for details on how to use the API and specific models
- Samples can be found under the `samples directory <https://github.com/CiscoDevNet/ydk-py/tree/master/core/samples>`_
- Hundreds of additional samples can be found in the `YDK-PY samples repository <https://github.com/CiscoDevNet/ydk-py-samples>`_
- Join the `YDK community <https://communities.cisco.com/community/developer/ydk>`_ to connect with other users and with the makers of YDK

Release Notes
--------------
The current YDK release version is 0.6.0 (beta). YDK-Py is licensed under the Apache 2.0 License.
