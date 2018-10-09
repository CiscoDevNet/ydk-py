""" Cisco_IOS_XR_ip_rib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-rib package configuration.

This module contains definitions
for the following management objects\:
  rib\: RIB configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-infra\-rsi\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Rib(Entity):
    """
    RIB configuration.
    
    .. attribute:: af
    
    	RIB address family configuration
    	**type**\:  :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af>`
    
    .. attribute:: max_recursion_depth
    
    	Set maximum depth for route recursion check
    	**type**\: int
    
    	**range:** 5..16
    
    

    """

    _prefix = 'ip-rib-cfg'
    _revision = '2017-07-31'

    def __init__(self):
        super(Rib, self).__init__()
        self._top_entity = None

        self.yang_name = "rib"
        self.yang_parent_name = "Cisco-IOS-XR-ip-rib-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("af", ("af", Rib.Af))])
        self._leafs = OrderedDict([
            ('max_recursion_depth', (YLeaf(YType.uint32, 'max-recursion-depth'), ['int'])),
        ])
        self.max_recursion_depth = None

        self.af = Rib.Af()
        self.af.parent = self
        self._children_name_map["af"] = "af"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-rib-cfg:rib"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Rib, ['max_recursion_depth'], name, value)


    class Af(Entity):
        """
        RIB address family configuration
        
        .. attribute:: ipv4
        
        	IPv4 configuration
        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv4>`
        
        .. attribute:: ipv6
        
        	IPv6 configuration
        	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv6>`
        
        

        """

        _prefix = 'ip-rib-cfg'
        _revision = '2017-07-31'

        def __init__(self):
            super(Rib.Af, self).__init__()

            self.yang_name = "af"
            self.yang_parent_name = "rib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipv4", ("ipv4", Rib.Af.Ipv4)), ("ipv6", ("ipv6", Rib.Af.Ipv6))])
            self._leafs = OrderedDict()

            self.ipv4 = Rib.Af.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"

            self.ipv6 = Rib.Af.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"
            self._segment_path = lambda: "af"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rib-cfg:rib/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Rib.Af, [], name, value)


        class Ipv4(Entity):
            """
            IPv4 configuration
            
            .. attribute:: next_hop_dampening_disable
            
            	Disable next\-hop dampening
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: redistribution_history
            
            	Redistribution history related configs
            	**type**\:  :py:class:`RedistributionHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv4.RedistributionHistory>`
            
            

            """

            _prefix = 'ip-rib-cfg'
            _revision = '2017-07-31'

            def __init__(self):
                super(Rib.Af.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "af"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("redistribution-history", ("redistribution_history", Rib.Af.Ipv4.RedistributionHistory))])
                self._leafs = OrderedDict([
                    ('next_hop_dampening_disable', (YLeaf(YType.empty, 'next-hop-dampening-disable'), ['Empty'])),
                ])
                self.next_hop_dampening_disable = None

                self.redistribution_history = Rib.Af.Ipv4.RedistributionHistory()
                self.redistribution_history.parent = self
                self._children_name_map["redistribution_history"] = "redistribution-history"
                self._segment_path = lambda: "ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rib-cfg:rib/af/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rib.Af.Ipv4, ['next_hop_dampening_disable'], name, value)


            class RedistributionHistory(Entity):
                """
                Redistribution history related configs
                
                .. attribute:: keep
                
                	Retain redistribution history after disconnect
                	**type**\:  :py:class:`Keep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv4.RedistributionHistory.Keep>`
                
                .. attribute:: bcdl_client
                
                	Maximum BCDL redistribution history size
                	**type**\: int
                
                	**range:** 10..2000000
                
                .. attribute:: protocol_client
                
                	Maximum protocol redistribution history size
                	**type**\: int
                
                	**range:** 10..250000
                
                

                """

                _prefix = 'ip-rib-cfg'
                _revision = '2017-07-31'

                def __init__(self):
                    super(Rib.Af.Ipv4.RedistributionHistory, self).__init__()

                    self.yang_name = "redistribution-history"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("keep", ("keep", Rib.Af.Ipv4.RedistributionHistory.Keep))])
                    self._leafs = OrderedDict([
                        ('bcdl_client', (YLeaf(YType.uint32, 'bcdl-client'), ['int'])),
                        ('protocol_client', (YLeaf(YType.uint32, 'protocol-client'), ['int'])),
                    ])
                    self.bcdl_client = None
                    self.protocol_client = None

                    self.keep = Rib.Af.Ipv4.RedistributionHistory.Keep()
                    self.keep.parent = self
                    self._children_name_map["keep"] = "keep"
                    self._segment_path = lambda: "redistribution-history"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rib-cfg:rib/af/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rib.Af.Ipv4.RedistributionHistory, ['bcdl_client', 'protocol_client'], name, value)


                class Keep(Entity):
                    """
                    Retain redistribution history after disconnect.
                    
                    .. attribute:: bcdl
                    
                    	Enable retain BCDL history
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-rib-cfg'
                    _revision = '2017-07-31'

                    def __init__(self):
                        super(Rib.Af.Ipv4.RedistributionHistory.Keep, self).__init__()

                        self.yang_name = "keep"
                        self.yang_parent_name = "redistribution-history"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('bcdl', (YLeaf(YType.empty, 'bcdl'), ['Empty'])),
                        ])
                        self.bcdl = None
                        self._segment_path = lambda: "keep"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rib-cfg:rib/af/ipv4/redistribution-history/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rib.Af.Ipv4.RedistributionHistory.Keep, ['bcdl'], name, value)


        class Ipv6(Entity):
            """
            IPv6 configuration
            
            .. attribute:: next_hop_dampening_disable
            
            	Disable next\-hop dampening
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: redistribution_history
            
            	Redistribution history related configs
            	**type**\:  :py:class:`RedistributionHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv6.RedistributionHistory>`
            
            

            """

            _prefix = 'ip-rib-cfg'
            _revision = '2017-07-31'

            def __init__(self):
                super(Rib.Af.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "af"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("redistribution-history", ("redistribution_history", Rib.Af.Ipv6.RedistributionHistory))])
                self._leafs = OrderedDict([
                    ('next_hop_dampening_disable', (YLeaf(YType.empty, 'next-hop-dampening-disable'), ['Empty'])),
                ])
                self.next_hop_dampening_disable = None

                self.redistribution_history = Rib.Af.Ipv6.RedistributionHistory()
                self.redistribution_history.parent = self
                self._children_name_map["redistribution_history"] = "redistribution-history"
                self._segment_path = lambda: "ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rib-cfg:rib/af/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rib.Af.Ipv6, ['next_hop_dampening_disable'], name, value)


            class RedistributionHistory(Entity):
                """
                Redistribution history related configs
                
                .. attribute:: keep
                
                	Retain redistribution history after disconnect
                	**type**\:  :py:class:`Keep <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rib_cfg.Rib.Af.Ipv6.RedistributionHistory.Keep>`
                
                .. attribute:: bcdl_client
                
                	Maximum BCDL redistribution history size
                	**type**\: int
                
                	**range:** 10..2000000
                
                .. attribute:: protocol_client
                
                	Maximum protocol redistribution history size
                	**type**\: int
                
                	**range:** 10..250000
                
                

                """

                _prefix = 'ip-rib-cfg'
                _revision = '2017-07-31'

                def __init__(self):
                    super(Rib.Af.Ipv6.RedistributionHistory, self).__init__()

                    self.yang_name = "redistribution-history"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("keep", ("keep", Rib.Af.Ipv6.RedistributionHistory.Keep))])
                    self._leafs = OrderedDict([
                        ('bcdl_client', (YLeaf(YType.uint32, 'bcdl-client'), ['int'])),
                        ('protocol_client', (YLeaf(YType.uint32, 'protocol-client'), ['int'])),
                    ])
                    self.bcdl_client = None
                    self.protocol_client = None

                    self.keep = Rib.Af.Ipv6.RedistributionHistory.Keep()
                    self.keep.parent = self
                    self._children_name_map["keep"] = "keep"
                    self._segment_path = lambda: "redistribution-history"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rib-cfg:rib/af/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rib.Af.Ipv6.RedistributionHistory, ['bcdl_client', 'protocol_client'], name, value)


                class Keep(Entity):
                    """
                    Retain redistribution history after disconnect.
                    
                    .. attribute:: bcdl
                    
                    	Enable retain BCDL history
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ip-rib-cfg'
                    _revision = '2017-07-31'

                    def __init__(self):
                        super(Rib.Af.Ipv6.RedistributionHistory.Keep, self).__init__()

                        self.yang_name = "keep"
                        self.yang_parent_name = "redistribution-history"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('bcdl', (YLeaf(YType.empty, 'bcdl'), ['Empty'])),
                        ])
                        self.bcdl = None
                        self._segment_path = lambda: "keep"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rib-cfg:rib/af/ipv6/redistribution-history/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rib.Af.Ipv6.RedistributionHistory.Keep, ['bcdl'], name, value)

    def clone_ptr(self):
        self._top_entity = Rib()
        return self._top_entity

