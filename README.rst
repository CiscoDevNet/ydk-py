Getting Started
===============

Overview:
----------

YDK or YANG Development Kit is a Software Development Kit that provides API's that are modeled
in YANG. The main goal of YDK is to reduce the learning curve by expressing the model semantics
in API and abstracting protocol/encoding details. The API's are generated from YANG models found
in this profile file `https://github.com/CiscoDevNet/ydk-gen/blob/master/profiles/ydk/ydk_0_4_0.json` using the ydk-gen tool `https://github.com/CiscoDevNet/ydk-gen` .

System Requirements:
--------------------
Linux
  Ubuntu (Debian-based) - The following packages must be present in your system before installing YDK-Py::

    $ sudo apt-get install python-pip zlib1g-dev python-lxml libxml2-dev libxslt1-dev python-dev

Mac
  It is recommended to install homebrew (http://brew.sh) and Xcode command line tools on your system before installing YDK-Py::

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    $ xcode-select --install

Install Tips:
-------------
Create a source distribution::

    $ cd <ydk_py_git_root>
    $ python setup.py sdist

We recommend that you perform the installation under a Python virtual environment (virtualenv).  To install virtualenv, execute::

  $ pip install virtualenv

Create a new virtual environment::

    $ virtualenv -p python2.7 ydk-py
    $ source ydk-py/bin/activate

Install requirements::

    (ydk-py)$ pip install -r requirements.txt

Install YDK-Py::

    (ydk-py)$ pip install dist/ydk-0.4.0.tar.gz

Notes:
------
- YANG Development Kit is a Python SDK that provides an API to access/modify configuration and operational entities that are modeled using YANG
- The modules under the package ydk.models are derived from YANG models
- YDK provides a simple CRUD (Create/Read/Update/Delete) api that allows the developer to perform these operations on entities on a server that supports them


Example Usage
========================

In this example we are going to set some configuration on the openconfig bgp model.
The complete sample is available in samples/bgp.py. The sample can be run with the below steps.
::

    (ydk-py)$ export PYTHONPATH=$PYTHONPATH:`pwd`
    (ydk-py)$ python ./samples/bgp.py -h
    Usage: bgp.py [-h | --help] [options]

    Options:
    -h, --help            show this help message and exit
    -v VERSION, --version=VERSION
                        force NETCONF version 1.0 or 1.1
    -u USERNAME, --user=USERNAME
    -p PASSWORD, --password=PASSWORD
                        password
    --proto=PROTO         Which transport protocol to use, one of ssh or tcp
    --host=HOST           NETCONF agent hostname
    --port=PORT           NETCONF agent SSH port

    (ydk-py)$ python ./samples/bgp.py --host <ip-address-of-netconf-server> -u <username> -p <password> --port <port-number>


Service Providers
------------------------
The first step in any application is create a 'Service Provider Instance'. 'Service Providers'
are responsible for mapping between the CRUD service API and the underlying manageability
protocol. In the current version of YDK we have one service provider which is the
ydk.providers.NetconfServiceProvider . It maps the CRUD api's to netconf rpc.

In this example we instantiate an instance of the service provider that creates a netconf
session to the machine at ip 10.0.0.1 ::

 from ydk.providers import NetconfServiceProvider

 sp_instance = NetconfServiceProvider(address='10.0.0.1',
                                      port=830,
                                      username='test',
                                      password='test',
                                      protocol = 'ssh')

Using the model APIs
------------------------
After establishing the connection, it's time to instantiate the entities and set some data.

First import the types from the module::

 from ydk.models.bgp import bgp

Next set the attributes ::

 # create BGP object
 bgp_cfg = bgp.Bgp()

 # set the Global AS
 bgp_cfg.global_.config.as_ = 65001

 # Create an AFI SAFI config
 ipv4_afsf = bgp_cfg.global_.afi_safis.AfiSafi()
 ipv4_afsf.afi_safi_name = 'ipv4-unicast'
 ipv4_afsf.config.afi_safi_name = 'ipv4-unicast'
 ipv4_afsf.config.enabled = True

 # Add the AFI SAFI config to the global AFI SAFI list
 bgp_cfg.global_.afi_safis.afi_safi.append(ipv4_afsf)

Invoking the CRUDService
--------------------------
First we need to import the CRUDService class::

 from ydk.services import CRUDService

Next we instantiate the CRUDService::

 crud_service = CRUDService()

And finally we invoke the create method of the CRUDService class passing in the
service provider instance and our entity (bgp_cfg)::

 try:
     crud_service.create(sp_instance, bgp_cfg)
 except YPYError:

Note if there were any errors the above API will raise YPYError.

Logging
-------
Uses common Python logging.  All modules are based off "ydk" log::

 import logging
 log = logging.getLogger('ydk')
 log.setLevel(logging.DEBUG)
 ch = logging.StreamHandler()
 log.addHandler(ch)

Release Notes
--------------
The current release version is 0.4.0 (beta). YDK-Py is licensed under the Apache 2.0 License.

Documentation and Support
--------------------------
- Samples can be found under the <git_root>/samples directory
- API documentation can be found at http://ydk.cisco.com/py/docs
- Additional samples can be found at https://github.com/CiscoDevNet/ydk-py-samples
- For queries related to usage of the API, please join the YDK community at https://communities.cisco.com/community/developer/ydk
