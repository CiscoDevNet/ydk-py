""" Cisco_IOS_XR_ipv4_telnet_mgmt_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-telnet\-mgmt package configuration.

This module contains definitions
for the following management objects\:
  telnet\: Global Telnet configuration commands

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Telnet(Entity):
    """
    Global Telnet configuration commands
    
    .. attribute:: vrfs
    
    	VRF name for telnet service
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_mgmt_cfg.Telnet.Vrfs>`
    
    

    """

    _prefix = 'ipv4-telnet-mgmt-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Telnet, self).__init__()
        self._top_entity = None

        self.yang_name = "telnet"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-telnet-mgmt-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrfs", ("vrfs", Telnet.Vrfs))])
        self._leafs = OrderedDict()

        self.vrfs = Telnet.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-telnet-mgmt-cfg:telnet"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Telnet, [], name, value)


    class Vrfs(Entity):
        """
        VRF name for telnet service
        
        .. attribute:: vrf
        
        	VRF name for telnet service
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_mgmt_cfg.Telnet.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-telnet-mgmt-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Telnet.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "telnet"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", Telnet.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-telnet-mgmt-cfg:telnet/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Telnet.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            VRF name for telnet service
            
            .. attribute:: vrf_name  (key)
            
            	VRF name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ipv4
            
            	IPv4 configuration
            	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_mgmt_cfg.Telnet.Vrfs.Vrf.Ipv4>`
            
            

            """

            _prefix = 'ipv4-telnet-mgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Telnet.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("ipv4", ("ipv4", Telnet.Vrfs.Vrf.Ipv4))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.ipv4 = Telnet.Vrfs.Vrf.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-telnet-mgmt-cfg:telnet/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Telnet.Vrfs.Vrf, ['vrf_name'], name, value)


            class Ipv4(Entity):
                """
                IPv4 configuration
                
                .. attribute:: dscp
                
                	Specify the DSCP value
                	**type**\: int
                
                	**range:** 0..63
                
                

                """

                _prefix = 'ipv4-telnet-mgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Telnet.Vrfs.Vrf.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('dscp', (YLeaf(YType.uint32, 'dscp'), ['int'])),
                    ])
                    self.dscp = None
                    self._segment_path = lambda: "ipv4"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Telnet.Vrfs.Vrf.Ipv4, ['dscp'], name, value)

    def clone_ptr(self):
        self._top_entity = Telnet()
        return self._top_entity

