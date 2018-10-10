""" Cisco_IOS_XE_nat_oper 

This module contains a collection of YANG definitions
for NAT operational data.
Copyright (c) 2017\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class NatData(Entity):
    """
    NAT statistics
    
    .. attribute:: ip_nat_statistics
    
    	Global NAT statistics
    	**type**\:  :py:class:`IpNatStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_nat_oper.NatData.IpNatStatistics>`
    
    	**presence node**\: True
    
    .. attribute:: ip_nat_translation
    
    	IP NAT translations
    	**type**\: list of  		 :py:class:`IpNatTranslation <ydk.models.cisco_ios_xe.Cisco_IOS_XE_nat_oper.NatData.IpNatTranslation>`
    
    

    """

    _prefix = 'nat-ios-xe-oper'
    _revision = '2018-03-17'

    def __init__(self):
        super(NatData, self).__init__()
        self._top_entity = None

        self.yang_name = "nat-data"
        self.yang_parent_name = "Cisco-IOS-XE-nat-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ip-nat-statistics", ("ip_nat_statistics", NatData.IpNatStatistics)), ("ip-nat-translation", ("ip_nat_translation", NatData.IpNatTranslation))])
        self._leafs = OrderedDict()

        self.ip_nat_statistics = None
        self._children_name_map["ip_nat_statistics"] = "ip-nat-statistics"

        self.ip_nat_translation = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-nat-oper:nat-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(NatData, [], name, value)


    class IpNatStatistics(Entity):
        """
        Global NAT statistics
        
        .. attribute:: initialized
        
        	Indicates if the NAT feature has been initialized
        	**type**\: bool
        
        .. attribute:: entries
        
        	Total translations
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: statics
        
        	Total static translations
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: statics_sorted
        
        	Sorted static translations by domain
        	**type**\: list of int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: flows
        
        	Total flows
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: insides
        
        	Number of inside interfaces
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: outsides
        
        	Number of outside interfaces
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: entry_timeouts
        
        	Number of entries which timed out 
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: hits
        
        	Successful searches with matching NAT session
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: misses
        
        	Unsuccessful searches without matching NAT session
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: interrupt_switched
        
        	Translated in interrupt switching
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: packets_punted
        
        	Packets punted to process
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: frag_pak_count
        
        	Counter for saved fragment packets
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: pool_stats_drop
        
        	Dropped pool stats from platform
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: mapping_stats_drop
        
        	Dropped mapping stats from platform
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: portlist_req_fail
        
        	Counter for port block alloc req fails
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ipalias_add_fail
        
        	Counter for add ipalias fails drops
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: limit_entry_add_fail
        
        	Counter for add limit\_entry fails drops
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: in2out_drops
        
        	Counter for NAT inside\->outside drops
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: out2in_drops
        
        	Counter for NAT outside\->inside drops
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: mib_addr_binds
        
        	MIB counter for address binds
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mib_addport_binds
        
        	MIB counter for address port binds
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'nat-ios-xe-oper'
        _revision = '2018-03-17'

        def __init__(self):
            super(NatData.IpNatStatistics, self).__init__()

            self.yang_name = "ip-nat-statistics"
            self.yang_parent_name = "nat-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('initialized', (YLeaf(YType.boolean, 'initialized'), ['bool'])),
                ('entries', (YLeaf(YType.uint64, 'entries'), ['int'])),
                ('statics', (YLeaf(YType.uint64, 'statics'), ['int'])),
                ('statics_sorted', (YLeafList(YType.uint64, 'statics-sorted'), ['int'])),
                ('flows', (YLeaf(YType.uint64, 'flows'), ['int'])),
                ('insides', (YLeaf(YType.uint64, 'insides'), ['int'])),
                ('outsides', (YLeaf(YType.uint64, 'outsides'), ['int'])),
                ('entry_timeouts', (YLeaf(YType.uint64, 'entry-timeouts'), ['int'])),
                ('hits', (YLeaf(YType.uint64, 'hits'), ['int'])),
                ('misses', (YLeaf(YType.uint64, 'misses'), ['int'])),
                ('interrupt_switched', (YLeaf(YType.uint64, 'interrupt-switched'), ['int'])),
                ('packets_punted', (YLeaf(YType.uint64, 'packets-punted'), ['int'])),
                ('frag_pak_count', (YLeaf(YType.uint64, 'frag-pak-count'), ['int'])),
                ('pool_stats_drop', (YLeaf(YType.uint64, 'pool-stats-drop'), ['int'])),
                ('mapping_stats_drop', (YLeaf(YType.uint64, 'mapping-stats-drop'), ['int'])),
                ('portlist_req_fail', (YLeaf(YType.uint64, 'portlist-req-fail'), ['int'])),
                ('ipalias_add_fail', (YLeaf(YType.uint64, 'ipalias-add-fail'), ['int'])),
                ('limit_entry_add_fail', (YLeaf(YType.uint64, 'limit-entry-add-fail'), ['int'])),
                ('in2out_drops', (YLeaf(YType.uint64, 'in2out-drops'), ['int'])),
                ('out2in_drops', (YLeaf(YType.uint64, 'out2in-drops'), ['int'])),
                ('mib_addr_binds', (YLeaf(YType.uint32, 'mib-addr-binds'), ['int'])),
                ('mib_addport_binds', (YLeaf(YType.uint32, 'mib-addport-binds'), ['int'])),
            ])
            self.initialized = None
            self.entries = None
            self.statics = None
            self.statics_sorted = []
            self.flows = None
            self.insides = None
            self.outsides = None
            self.entry_timeouts = None
            self.hits = None
            self.misses = None
            self.interrupt_switched = None
            self.packets_punted = None
            self.frag_pak_count = None
            self.pool_stats_drop = None
            self.mapping_stats_drop = None
            self.portlist_req_fail = None
            self.ipalias_add_fail = None
            self.limit_entry_add_fail = None
            self.in2out_drops = None
            self.out2in_drops = None
            self.mib_addr_binds = None
            self.mib_addport_binds = None
            self._segment_path = lambda: "ip-nat-statistics"
            self._absolute_path = lambda: "Cisco-IOS-XE-nat-oper:nat-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NatData.IpNatStatistics, ['initialized', 'entries', 'statics', 'statics_sorted', 'flows', 'insides', 'outsides', 'entry_timeouts', 'hits', 'misses', 'interrupt_switched', 'packets_punted', 'frag_pak_count', 'pool_stats_drop', 'mapping_stats_drop', 'portlist_req_fail', 'ipalias_add_fail', 'limit_entry_add_fail', 'in2out_drops', 'out2in_drops', 'mib_addr_binds', 'mib_addport_binds'], name, value)


    class IpNatTranslation(Entity):
        """
        IP NAT translations
        
        .. attribute:: inside_local_addr  (key)
        
        	Inside local address
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: outside_local_addr  (key)
        
        	Outside local address
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: inside_local_port  (key)
        
        	Inside local port
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: outside_local_port  (key)
        
        	Outside local port
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: vrfid  (key)
        
        	VRF ID
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: protocol  (key)
        
        	Protocol
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: inside_global_addr
        
        	Inside global address
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: outside_global_addr
        
        	Outside global address
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: inside_global_port
        
        	Inside global port
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: outside_global_port
        
        	Outside global port
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: flags
        
        	Translation flags
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: application_type
        
        	Application type
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: vrf_name
        
        	Virtual Routing and Forwarding name
        	**type**\: str
        
        

        """

        _prefix = 'nat-ios-xe-oper'
        _revision = '2018-03-17'

        def __init__(self):
            super(NatData.IpNatTranslation, self).__init__()

            self.yang_name = "ip-nat-translation"
            self.yang_parent_name = "nat-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['inside_local_addr','outside_local_addr','inside_local_port','outside_local_port','vrfid','protocol']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('inside_local_addr', (YLeaf(YType.str, 'inside-local-addr'), ['str'])),
                ('outside_local_addr', (YLeaf(YType.str, 'outside-local-addr'), ['str'])),
                ('inside_local_port', (YLeaf(YType.uint16, 'inside-local-port'), ['int'])),
                ('outside_local_port', (YLeaf(YType.uint16, 'outside-local-port'), ['int'])),
                ('vrfid', (YLeaf(YType.uint16, 'vrfid'), ['int'])),
                ('protocol', (YLeaf(YType.uint8, 'protocol'), ['int'])),
                ('inside_global_addr', (YLeaf(YType.str, 'inside-global-addr'), ['str'])),
                ('outside_global_addr', (YLeaf(YType.str, 'outside-global-addr'), ['str'])),
                ('inside_global_port', (YLeaf(YType.uint16, 'inside-global-port'), ['int'])),
                ('outside_global_port', (YLeaf(YType.uint16, 'outside-global-port'), ['int'])),
                ('flags', (YLeaf(YType.uint32, 'flags'), ['int'])),
                ('application_type', (YLeaf(YType.uint8, 'application-type'), ['int'])),
                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
            ])
            self.inside_local_addr = None
            self.outside_local_addr = None
            self.inside_local_port = None
            self.outside_local_port = None
            self.vrfid = None
            self.protocol = None
            self.inside_global_addr = None
            self.outside_global_addr = None
            self.inside_global_port = None
            self.outside_global_port = None
            self.flags = None
            self.application_type = None
            self.vrf_name = None
            self._segment_path = lambda: "ip-nat-translation" + "[inside-local-addr='" + str(self.inside_local_addr) + "']" + "[outside-local-addr='" + str(self.outside_local_addr) + "']" + "[inside-local-port='" + str(self.inside_local_port) + "']" + "[outside-local-port='" + str(self.outside_local_port) + "']" + "[vrfid='" + str(self.vrfid) + "']" + "[protocol='" + str(self.protocol) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-nat-oper:nat-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NatData.IpNatTranslation, ['inside_local_addr', 'outside_local_addr', 'inside_local_port', 'outside_local_port', 'vrfid', 'protocol', 'inside_global_addr', 'outside_global_addr', 'inside_global_port', 'outside_global_port', 'flags', 'application_type', 'vrf_name'], name, value)

    def clone_ptr(self):
        self._top_entity = NatData()
        return self._top_entity

