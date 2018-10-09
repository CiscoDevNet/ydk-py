""" Cisco_IOS_XR_ipv6_io_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-io package configuration.

This module contains definitions
for the following management objects\:
  ipv6\-configuration\: IPv6 Configuration Data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Ipv6Configuration(Entity):
    """
    IPv6 Configuration Data
    
    .. attribute:: ipv6_assembler
    
    	IPv6 fragmented packet assembler
    	**type**\:  :py:class:`Ipv6Assembler <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg.Ipv6Configuration.Ipv6Assembler>`
    
    .. attribute:: ipv6icmp
    
    	Configure IPv6 ICMP parameters
    	**type**\:  :py:class:`Ipv6icmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg.Ipv6Configuration.Ipv6icmp>`
    
    	**presence node**\: True
    
    .. attribute:: ipv6_pmtu_time_out
    
    	Configure IPv6 Path MTU timeout value in minutes
    	**type**\: int
    
    	**range:** 1..15
    
    	**units**\: minute
    
    .. attribute:: ipv6_source_route
    
    	TRUE if enabled, FALSE if disabled
    	**type**\: bool
    
    	**default value**\: true
    
    .. attribute:: ipv6_pmtu_enable
    
    	TRUE if enabled, FALSE if disabled
    	**type**\: bool
    
    	**default value**\: false
    
    .. attribute:: ipv6_hop_limit
    
    	Configure IPv6 hop count limit
    	**type**\: int
    
    	**range:** 1..255
    
    

    """

    _prefix = 'ipv6-io-cfg'
    _revision = '2016-05-10'

    def __init__(self):
        super(Ipv6Configuration, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-configuration"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-io-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ipv6-assembler", ("ipv6_assembler", Ipv6Configuration.Ipv6Assembler)), ("ipv6icmp", ("ipv6icmp", Ipv6Configuration.Ipv6icmp))])
        self._leafs = OrderedDict([
            ('ipv6_pmtu_time_out', (YLeaf(YType.uint32, 'ipv6-pmtu-time-out'), ['int'])),
            ('ipv6_source_route', (YLeaf(YType.boolean, 'ipv6-source-route'), ['bool'])),
            ('ipv6_pmtu_enable', (YLeaf(YType.boolean, 'ipv6-pmtu-enable'), ['bool'])),
            ('ipv6_hop_limit', (YLeaf(YType.uint32, 'ipv6-hop-limit'), ['int'])),
        ])
        self.ipv6_pmtu_time_out = None
        self.ipv6_source_route = None
        self.ipv6_pmtu_enable = None
        self.ipv6_hop_limit = None

        self.ipv6_assembler = Ipv6Configuration.Ipv6Assembler()
        self.ipv6_assembler.parent = self
        self._children_name_map["ipv6_assembler"] = "ipv6-assembler"

        self.ipv6icmp = None
        self._children_name_map["ipv6icmp"] = "ipv6icmp"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-io-cfg:ipv6-configuration"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv6Configuration, ['ipv6_pmtu_time_out', 'ipv6_source_route', 'ipv6_pmtu_enable', 'ipv6_hop_limit'], name, value)


    class Ipv6Assembler(Entity):
        """
        IPv6 fragmented packet assembler
        
        .. attribute:: timeout
        
        	Number of seconds an assembly queue will hold before timeout
        	**type**\: int
        
        	**range:** 1..120
        
        	**units**\: second
        
        .. attribute:: max_packets
        
        	Maxinum packets allowed in assembly queues (in percent)
        	**type**\: int
        
        	**range:** 1..50
        
        	**units**\: percentage
        
        

        """

        _prefix = 'ipv6-io-cfg'
        _revision = '2016-05-10'

        def __init__(self):
            super(Ipv6Configuration.Ipv6Assembler, self).__init__()

            self.yang_name = "ipv6-assembler"
            self.yang_parent_name = "ipv6-configuration"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                ('max_packets', (YLeaf(YType.uint32, 'max-packets'), ['int'])),
            ])
            self.timeout = None
            self.max_packets = None
            self._segment_path = lambda: "ipv6-assembler"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-io-cfg:ipv6-configuration/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6Configuration.Ipv6Assembler, ['timeout', 'max_packets'], name, value)


    class Ipv6icmp(Entity):
        """
        Configure IPv6 ICMP parameters
        
        .. attribute:: error_interval
        
        	Interval between tokens in milliseconds
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**mandatory**\: True
        
        	**units**\: millisecond
        
        .. attribute:: bucket_size
        
        	Bucket size
        	**type**\: int
        
        	**range:** 1..200
        
        	**default value**\: 10
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv6-io-cfg'
        _revision = '2016-05-10'

        def __init__(self):
            super(Ipv6Configuration.Ipv6icmp, self).__init__()

            self.yang_name = "ipv6icmp"
            self.yang_parent_name = "ipv6-configuration"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('error_interval', (YLeaf(YType.uint32, 'error-interval'), ['int'])),
                ('bucket_size', (YLeaf(YType.uint32, 'bucket-size'), ['int'])),
            ])
            self.error_interval = None
            self.bucket_size = None
            self._segment_path = lambda: "ipv6icmp"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-io-cfg:ipv6-configuration/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6Configuration.Ipv6icmp, ['error_interval', 'bucket_size'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv6Configuration()
        return self._top_entity

