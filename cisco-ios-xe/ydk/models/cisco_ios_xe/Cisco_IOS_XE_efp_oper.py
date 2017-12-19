""" Cisco_IOS_XE_efp_oper 

This module contains a collection of YANG definitions
for service instance (efp) stats.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EfpStats(Entity):
    """
    Service instance stats
    
    .. attribute:: efp_stat
    
    	List of service instance stats
    	**type**\: list of  		 :py:class:`EfpStat <ydk.models.cisco_ios_xe.Cisco_IOS_XE_efp_oper.EfpStats.EfpStat>`
    
    

    """

    _prefix = 'efp-stats-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(EfpStats, self).__init__()
        self._top_entity = None

        self.yang_name = "efp-stats"
        self.yang_parent_name = "Cisco-IOS-XE-efp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"efp-stat" : ("efp_stat", EfpStats.EfpStat)}

        self.efp_stat = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-efp-oper:efp-stats"

    def __setattr__(self, name, value):
        self._perform_setattr(EfpStats, [], name, value)


    class EfpStat(Entity):
        """
        List of service instance stats
        
        .. attribute:: id  <key>
        
        	EFP id
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: interface  <key>
        
        	Interface name
        	**type**\: str
        
        .. attribute:: in_pkts
        
        	Incoming packets
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: in_bytes
        
        	Incoming bytes
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: out_pkts
        
        	Outgoing packets
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: out_bytes
        
        	Outgoing bytes
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        

        """

        _prefix = 'efp-stats-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(EfpStats.EfpStat, self).__init__()

            self.yang_name = "efp-stat"
            self.yang_parent_name = "efp-stats"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.id = YLeaf(YType.uint32, "id")

            self.interface = YLeaf(YType.str, "interface")

            self.in_pkts = YLeaf(YType.uint64, "in-pkts")

            self.in_bytes = YLeaf(YType.uint64, "in-bytes")

            self.out_pkts = YLeaf(YType.uint64, "out-pkts")

            self.out_bytes = YLeaf(YType.uint64, "out-bytes")
            self._segment_path = lambda: "efp-stat" + "[id='" + self.id.get() + "']" + "[interface='" + self.interface.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-efp-oper:efp-stats/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EfpStats.EfpStat, ['id', 'interface', 'in_pkts', 'in_bytes', 'out_pkts', 'out_bytes'], name, value)

    def clone_ptr(self):
        self._top_entity = EfpStats()
        return self._top_entity

