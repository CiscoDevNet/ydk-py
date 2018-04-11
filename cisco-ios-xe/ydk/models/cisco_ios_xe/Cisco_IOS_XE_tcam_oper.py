""" Cisco_IOS_XE_tcam_oper 

This module contains a collection of YANG definitions
for ASIC TCAM Memory Utilization Statistics.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class TcamDetails(Entity):
    """
    ASIC TCAM Memory Statistics
    
    .. attribute:: tcam_detail
    
    	FED ASIC TCAM Utilization
    	**type**\: list of  		 :py:class:`TcamDetail <ydk.models.cisco_ios_xe.Cisco_IOS_XE_tcam_oper.TcamDetails.TcamDetail>`
    
    

    """

    _prefix = 'tcam-ios-xe-oper'
    _revision = '2017-06-06'

    def __init__(self):
        super(TcamDetails, self).__init__()
        self._top_entity = None

        self.yang_name = "tcam-details"
        self.yang_parent_name = "Cisco-IOS-XE-tcam-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("tcam-detail", ("tcam_detail", TcamDetails.TcamDetail))])
        self._leafs = OrderedDict()

        self.tcam_detail = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-tcam-oper:tcam-details"

    def __setattr__(self, name, value):
        self._perform_setattr(TcamDetails, [], name, value)


    class TcamDetail(Entity):
        """
        FED ASIC TCAM Utilization
        
        .. attribute:: asic_no  (key)
        
        	Asic Number of Switch
        	**type**\: int
        
        	**range:** 0..8
        
        .. attribute:: name  (key)
        
        	Protocol Name
        	**type**\: str
        
        .. attribute:: hash_entries_max
        
        	Maximum Hash Entries
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcam_entries_max
        
        	Maximum Tcam Entries
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: hash_entries_used
        
        	Hash Entries Used
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: tcam_entries_used
        
        	Tcam Entries Used
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'tcam-ios-xe-oper'
        _revision = '2017-06-06'

        def __init__(self):
            super(TcamDetails.TcamDetail, self).__init__()

            self.yang_name = "tcam-detail"
            self.yang_parent_name = "tcam-details"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['asic_no','name']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('asic_no', YLeaf(YType.uint8, 'asic-no')),
                ('name', YLeaf(YType.str, 'name')),
                ('hash_entries_max', YLeaf(YType.uint32, 'hash-entries-max')),
                ('tcam_entries_max', YLeaf(YType.uint32, 'tcam-entries-max')),
                ('hash_entries_used', YLeaf(YType.uint32, 'hash-entries-used')),
                ('tcam_entries_used', YLeaf(YType.uint32, 'tcam-entries-used')),
            ])
            self.asic_no = None
            self.name = None
            self.hash_entries_max = None
            self.tcam_entries_max = None
            self.hash_entries_used = None
            self.tcam_entries_used = None
            self._segment_path = lambda: "tcam-detail" + "[asic-no='" + str(self.asic_no) + "']" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-tcam-oper:tcam-details/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TcamDetails.TcamDetail, ['asic_no', 'name', 'hash_entries_max', 'tcam_entries_max', 'hash_entries_used', 'tcam_entries_used'], name, value)

    def clone_ptr(self):
        self._top_entity = TcamDetails()
        return self._top_entity

