""" Cisco_IOS_XR_ipv4_smiap_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-smiap package configuration.

This module contains definitions
for the following management objects\:
  ipv4\-virtual\: IPv4 virtual address for management interfaces

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Ipv4Virtual(Entity):
    """
    IPv4 virtual address for management interfaces
    
    .. attribute:: vrfs
    
    	VRFs for the virtual IPv4 addresses
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_smiap_cfg.Ipv4Virtual.Vrfs>`
    
    .. attribute:: use_as_source_address
    
    	Enable use as default source address on sourced packets
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'ipv4-smiap-cfg'
    _revision = '2016-07-04'

    def __init__(self):
        super(Ipv4Virtual, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-virtual"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-smiap-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrfs", ("vrfs", Ipv4Virtual.Vrfs))])
        self._leafs = OrderedDict([
            ('use_as_source_address', (YLeaf(YType.empty, 'use-as-source-address'), ['Empty'])),
        ])
        self.use_as_source_address = None

        self.vrfs = Ipv4Virtual.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-smiap-cfg:ipv4-virtual"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv4Virtual, ['use_as_source_address'], name, value)


    class Vrfs(Entity):
        """
        VRFs for the virtual IPv4 addresses
        
        .. attribute:: vrf
        
        	A VRF for a virtual IPv4 address.  Specify 'default' for VRF default
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_smiap_cfg.Ipv4Virtual.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-smiap-cfg'
        _revision = '2016-07-04'

        def __init__(self):
            super(Ipv4Virtual.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "ipv4-virtual"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", Ipv4Virtual.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-smiap-cfg:ipv4-virtual/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Virtual.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            A VRF for a virtual IPv4 address.  Specify
            'default' for VRF default
            
            .. attribute:: vrf_name  (key)
            
            	Name of VRF
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: address
            
            	IPv4 sddress and mask
            	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_smiap_cfg.Ipv4Virtual.Vrfs.Vrf.Address>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ipv4-smiap-cfg'
            _revision = '2016-07-04'

            def __init__(self):
                super(Ipv4Virtual.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("address", ("address", Ipv4Virtual.Vrfs.Vrf.Address))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.address = None
                self._children_name_map["address"] = "address"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-smiap-cfg:ipv4-virtual/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Virtual.Vrfs.Vrf, ['vrf_name'], name, value)


            class Address(Entity):
                """
                IPv4 sddress and mask
                
                .. attribute:: address
                
                	IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                .. attribute:: netmask
                
                	IPv4 address mask
                	**type**\: int
                
                	**range:** 0..32
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-smiap-cfg'
                _revision = '2016-07-04'

                def __init__(self):
                    super(Ipv4Virtual.Vrfs.Vrf.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                        ('netmask', (YLeaf(YType.uint8, 'netmask'), ['int'])),
                    ])
                    self.address = None
                    self.netmask = None
                    self._segment_path = lambda: "address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Virtual.Vrfs.Vrf.Address, ['address', 'netmask'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv4Virtual()
        return self._top_entity

