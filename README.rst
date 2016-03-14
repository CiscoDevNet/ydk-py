Getting Started
===============

Overview:
----------

YDK or YANG Development Kit is a Software Development Kit that provides API's that are modeled
in YANG. The main goal of YDK is to reduce the learning curve by expressing the model semantics 
in API and abstracting protocol/encoding details. The API's are generated from YANG models found 
in this link `yang.rst` using the ydk-gen tool `https://github.com/CiscoDevNet/ydk-gen` .


Install Tips:
-------------

Run Installation instruction under python virtualenv, once you have virtualenv installed.
To install virtualenv use pip (pip install virtualenv).
::
        
    user-machine# cd <ydk_py_git_root>
    user-machine# python setup.py sdist
	    
    user-machine# virtualenv mypython
    user-machine# source mypython/bin/activate
        ...
    #Now install ydk 
    user-machine(mypython)# pip install dist/ydk-0.3.0.tar.gz



Notes:
------ 
**YANG Development Kit** 
  - Is a Python SDK that provides an API to access/modify configurational and operational entities
    that are modelled using YANG.
  - The modules under the package ydk.models are derived from YANG models
  - YDK provides a simple CRUD (Create/Read/Update/Delete) api that allows the developer to perform
    these operations on entities on a server that supports them
  

Example Usage
========================

In this example we are going to set some configuration on the openconfig bgp model.
The complete sample is available in samples/bgp.py.

Service Providers
------------------------
The first step in any application is create a 'Service Provider Instance'. 'Service Providers' 
are responsible for mapping between the CRUD service API and the underlying manageability 
protocol. In the current version of YDK we have one service provider which is the 
ydk.providers.NetconfServiceProvider . It maps the CRUD api's to netconf rpc.

In this example we instantiate an instance of the service provider that creates a netconf
session to the machine at ip 10.0.0.1 ::
      
      >> from ydk.providers import NetconfServiceProvider
      >> sp_instance = NetconfServiceProvider(address='10.0.0.1',
                                      port=830,
                                      username='test',
                                      password='test',
                                      protocol = 'ssh')
 
 Using the models api
 ------------------------
 After establishing the connection, it's time to instantiate the entities and set some data
 
 First import the types from the module::
 
     >> from ydk.models.bgp import bgp
 
 Next set the attributes ::
 
    >> bgp_cfg = bgp.Bgp()
    
    >> # Set the Global AS
    >> bgp_cfg.global_.config.as_ = 65001
    
    
    >> # Create an AFI SAFI config
    >> ipv4_afsf = bgp_cfg.global_.afi_safis.AfiSafi()
    >> ipv4_afsf.afi_safi_name = 'ipv4-unicast'
    >> ipv4_afsf.config.afi_safi_name = 'ipv4-unicast'
    >> ipv4_afsf.config.enabled = True
    
    
    >> # Add the AFI SAFI config to the global AFI SAFI list
    >> bgp_cfg.global_.afi_safis.afi_safi.append(ipv4_afsf)
    
 Invoking the CRUDService
 --------------------------
 First we need to import the CRUDService class::
    
    >> from ydk.services import CRUDService
    
Next we instantiate the CRUDService ::
    
    >> crud_service = CRUDService()

And finally we invoke the create method of the CRUDService class passing in the 
service provider instance and our entity (bgp_cfg)::
  
    >> try:
    >>     crud_service.create(sp_instance, bgp_cfg)
    >> except YPYError:
 
Note if there were any errors the above API will raise YPYError. 

Logging
-------
Uses common Python logging.  All modules are based off "ydk" log
::
    
    >>> import logging
    >>> log = logging.getLogger('ydk')
    >>> log.setLevel(logging.DEBUG)
    >>> ch = logging.StreamHandler()
    >>> log.addHandler(ch)

Release Notes
--------------
Note: ydk-py is licensed under the Apache 2.0 License. 
The current release is a beta release and the release version is 0.3.0. 

Documentation and Support
--------------------------
For queries related to usage of the API please use the mailer ask-ydk.com. 
Documentation on the API's can be found here `http://ydk.cisco.com/py/docs`.
Samples can be found under the <git_root>/samples directory.
Additional samples can be found here `https://github.com/CiscoDevNet/ydk-py-samples`.

Other useful links
------------------
* :doc:`read_filter`
* :doc:`presence_class`
* :doc:`types_doc`

