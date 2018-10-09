""" Cisco_IOS_XR_infra_rt_check_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rt\-check package configuration.

This module contains definitions
for the following management objects\:
  rcc\: RCC (Route Consistency Checker) configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Rcc(Entity):
    """
    RCC (Route Consistency Checker) configuration
    
    .. attribute:: ipv6
    
    	RCC/LCC configuration for IPv6
    	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg.Rcc.Ipv6>`
    
    .. attribute:: ipv4
    
    	RCC/LCC configuration for IPv4
    	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg.Rcc.Ipv4>`
    
    

    """

    _prefix = 'infra-rt-check-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Rcc, self).__init__()
        self._top_entity = None

        self.yang_name = "rcc"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rt-check-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ipv6", ("ipv6", Rcc.Ipv6)), ("ipv4", ("ipv4", Rcc.Ipv4))])
        self._leafs = OrderedDict()

        self.ipv6 = Rcc.Ipv6()
        self.ipv6.parent = self
        self._children_name_map["ipv6"] = "ipv6"

        self.ipv4 = Rcc.Ipv4()
        self.ipv4.parent = self
        self._children_name_map["ipv4"] = "ipv4"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rt-check-cfg:rcc"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Rcc, [], name, value)


    class Ipv6(Entity):
        """
        RCC/LCC configuration for IPv6
        
        .. attribute:: lcc
        
        	IPv4/IPv6 LCC (Label Consistency Checker) configuration
        	**type**\:  :py:class:`Lcc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg.Rcc.Ipv6.Lcc>`
        
        .. attribute:: unicast
        
        	RCC configuration for unicast
        	**type**\:  :py:class:`Unicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg.Rcc.Ipv6.Unicast>`
        
        .. attribute:: multicast
        
        	RCC configuration for multicast
        	**type**\:  :py:class:`Multicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg.Rcc.Ipv6.Multicast>`
        
        

        """

        _prefix = 'infra-rt-check-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rcc.Ipv6, self).__init__()

            self.yang_name = "ipv6"
            self.yang_parent_name = "rcc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lcc", ("lcc", Rcc.Ipv6.Lcc)), ("unicast", ("unicast", Rcc.Ipv6.Unicast)), ("multicast", ("multicast", Rcc.Ipv6.Multicast))])
            self._leafs = OrderedDict()

            self.lcc = Rcc.Ipv6.Lcc()
            self.lcc.parent = self
            self._children_name_map["lcc"] = "lcc"

            self.unicast = Rcc.Ipv6.Unicast()
            self.unicast.parent = self
            self._children_name_map["unicast"] = "unicast"

            self.multicast = Rcc.Ipv6.Multicast()
            self.multicast.parent = self
            self._children_name_map["multicast"] = "multicast"
            self._segment_path = lambda: "ipv6"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rt-check-cfg:rcc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Rcc.Ipv6, [], name, value)


        class Lcc(Entity):
            """
            IPv4/IPv6 LCC (Label Consistency Checker)
            configuration
            
            .. attribute:: period
            
            	Period of check in milliseconds
            	**type**\: int
            
            	**range:** 100..600000
            
            	**units**\: millisecond
            
            .. attribute:: enable
            
            	Enable RCC/LCC
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rt-check-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rcc.Ipv6.Lcc, self).__init__()

                self.yang_name = "lcc"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('period', (YLeaf(YType.uint32, 'period'), ['int'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.period = None
                self.enable = None
                self._segment_path = lambda: "lcc"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rt-check-cfg:rcc/ipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rcc.Ipv6.Lcc, ['period', 'enable'], name, value)


        class Unicast(Entity):
            """
            RCC configuration for unicast
            
            .. attribute:: period
            
            	Period of check in milliseconds
            	**type**\: int
            
            	**range:** 100..600000
            
            	**units**\: millisecond
            
            .. attribute:: enable
            
            	Enable RCC/LCC
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rt-check-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rcc.Ipv6.Unicast, self).__init__()

                self.yang_name = "unicast"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('period', (YLeaf(YType.uint32, 'period'), ['int'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.period = None
                self.enable = None
                self._segment_path = lambda: "unicast"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rt-check-cfg:rcc/ipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rcc.Ipv6.Unicast, ['period', 'enable'], name, value)


        class Multicast(Entity):
            """
            RCC configuration for multicast
            
            .. attribute:: period
            
            	Period of check in milliseconds
            	**type**\: int
            
            	**range:** 100..600000
            
            	**units**\: millisecond
            
            .. attribute:: enable
            
            	Enable RCC/LCC
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rt-check-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rcc.Ipv6.Multicast, self).__init__()

                self.yang_name = "multicast"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('period', (YLeaf(YType.uint32, 'period'), ['int'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.period = None
                self.enable = None
                self._segment_path = lambda: "multicast"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rt-check-cfg:rcc/ipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rcc.Ipv6.Multicast, ['period', 'enable'], name, value)


    class Ipv4(Entity):
        """
        RCC/LCC configuration for IPv4
        
        .. attribute:: lcc
        
        	IPv4/IPv6 LCC (Label Consistency Checker) configuration
        	**type**\:  :py:class:`Lcc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg.Rcc.Ipv4.Lcc>`
        
        .. attribute:: unicast
        
        	RCC configuration for unicast
        	**type**\:  :py:class:`Unicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg.Rcc.Ipv4.Unicast>`
        
        .. attribute:: multicast
        
        	RCC configuration for multicast
        	**type**\:  :py:class:`Multicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rt_check_cfg.Rcc.Ipv4.Multicast>`
        
        

        """

        _prefix = 'infra-rt-check-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rcc.Ipv4, self).__init__()

            self.yang_name = "ipv4"
            self.yang_parent_name = "rcc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lcc", ("lcc", Rcc.Ipv4.Lcc)), ("unicast", ("unicast", Rcc.Ipv4.Unicast)), ("multicast", ("multicast", Rcc.Ipv4.Multicast))])
            self._leafs = OrderedDict()

            self.lcc = Rcc.Ipv4.Lcc()
            self.lcc.parent = self
            self._children_name_map["lcc"] = "lcc"

            self.unicast = Rcc.Ipv4.Unicast()
            self.unicast.parent = self
            self._children_name_map["unicast"] = "unicast"

            self.multicast = Rcc.Ipv4.Multicast()
            self.multicast.parent = self
            self._children_name_map["multicast"] = "multicast"
            self._segment_path = lambda: "ipv4"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rt-check-cfg:rcc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Rcc.Ipv4, [], name, value)


        class Lcc(Entity):
            """
            IPv4/IPv6 LCC (Label Consistency Checker)
            configuration
            
            .. attribute:: period
            
            	Period of check in milliseconds
            	**type**\: int
            
            	**range:** 100..600000
            
            	**units**\: millisecond
            
            .. attribute:: enable
            
            	Enable RCC/LCC
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rt-check-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rcc.Ipv4.Lcc, self).__init__()

                self.yang_name = "lcc"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('period', (YLeaf(YType.uint32, 'period'), ['int'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.period = None
                self.enable = None
                self._segment_path = lambda: "lcc"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rt-check-cfg:rcc/ipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rcc.Ipv4.Lcc, ['period', 'enable'], name, value)


        class Unicast(Entity):
            """
            RCC configuration for unicast
            
            .. attribute:: period
            
            	Period of check in milliseconds
            	**type**\: int
            
            	**range:** 100..600000
            
            	**units**\: millisecond
            
            .. attribute:: enable
            
            	Enable RCC/LCC
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rt-check-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rcc.Ipv4.Unicast, self).__init__()

                self.yang_name = "unicast"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('period', (YLeaf(YType.uint32, 'period'), ['int'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.period = None
                self.enable = None
                self._segment_path = lambda: "unicast"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rt-check-cfg:rcc/ipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rcc.Ipv4.Unicast, ['period', 'enable'], name, value)


        class Multicast(Entity):
            """
            RCC configuration for multicast
            
            .. attribute:: period
            
            	Period of check in milliseconds
            	**type**\: int
            
            	**range:** 100..600000
            
            	**units**\: millisecond
            
            .. attribute:: enable
            
            	Enable RCC/LCC
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rt-check-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rcc.Ipv4.Multicast, self).__init__()

                self.yang_name = "multicast"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('period', (YLeaf(YType.uint32, 'period'), ['int'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.period = None
                self.enable = None
                self._segment_path = lambda: "multicast"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rt-check-cfg:rcc/ipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rcc.Ipv4.Multicast, ['period', 'enable'], name, value)

    def clone_ptr(self):
        self._top_entity = Rcc()
        return self._top_entity

