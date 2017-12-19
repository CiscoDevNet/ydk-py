""" Cisco_IOS_XE_cfm_oper 

This module contains a collection of YANG definitions for
monitoring the Connectivity Fault Management protocol operation in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CfmLastClearedType(Enum):
    """
    CfmLastClearedType

    Describes whether CFM stats have been cleared

    .. data:: never_cleared = 0

    	CFM stats have never been cleared

    .. data:: cleared_before = 1

    	CFM stats have been cleared once before

    """

    never_cleared = Enum.YLeaf(0, "never-cleared")

    cleared_before = Enum.YLeaf(1, "cleared-before")



class CfmStatistics(Entity):
    """
    Data nodes for CFM Statistics
    
    .. attribute:: cfm_meps
    
    	CFM statistics
    	**type**\:  :py:class:`CfmMeps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper.CfmStatistics.CfmMeps>`
    
    

    """

    _prefix = 'cfm-stats-ios-xe-oper'
    _revision = '2017-06-06'

    def __init__(self):
        super(CfmStatistics, self).__init__()
        self._top_entity = None

        self.yang_name = "cfm-statistics"
        self.yang_parent_name = "Cisco-IOS-XE-cfm-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"cfm-meps" : ("cfm_meps", CfmStatistics.CfmMeps)}
        self._child_list_classes = {}

        self.cfm_meps = CfmStatistics.CfmMeps()
        self.cfm_meps.parent = self
        self._children_name_map["cfm_meps"] = "cfm-meps"
        self._children_yang_names.add("cfm-meps")
        self._segment_path = lambda: "Cisco-IOS-XE-cfm-oper:cfm-statistics"


    class CfmMeps(Entity):
        """
        CFM statistics
        
        .. attribute:: cfm_mep
        
        	The list of MEP entries in the system
        	**type**\: list of  		 :py:class:`CfmMep <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper.CfmStatistics.CfmMeps.CfmMep>`
        
        

        """

        _prefix = 'cfm-stats-ios-xe-oper'
        _revision = '2017-06-06'

        def __init__(self):
            super(CfmStatistics.CfmMeps, self).__init__()

            self.yang_name = "cfm-meps"
            self.yang_parent_name = "cfm-statistics"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cfm-mep" : ("cfm_mep", CfmStatistics.CfmMeps.CfmMep)}

            self.cfm_mep = YList(self)
            self._segment_path = lambda: "cfm-meps"
            self._absolute_path = lambda: "Cisco-IOS-XE-cfm-oper:cfm-statistics/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CfmStatistics.CfmMeps, [], name, value)


        class CfmMep(Entity):
            """
            The list of MEP entries in the system
            
            .. attribute:: domain_name  <key>
            
            	The name of the Domain corresponding the the MEP
            	**type**\: str
            
            .. attribute:: ma_name  <key>
            
            	The name of the MA corresponding the the MEP
            	**type**\: str
            
            .. attribute:: mpid  <key>
            
            	ID of the MEP
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: last_cleared
            
            	Info on when the stats were last cleared
            	**type**\:  :py:class:`LastCleared <ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper.CfmStatistics.CfmMeps.CfmMep.LastCleared>`
            
            .. attribute:: ccm_transmitted
            
            	The number of CCMs transmitted from the local MEP
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ccm_seq_errors
            
            	The number of CCM sequence number errors detected
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ltr_unexpected
            
            	The number of unexpected linktrace reply packets  received at this MEP
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: lbr_transmitted
            
            	The number of loopback reply packets transmitted from the local MEP
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: lbr_seq_errors
            
            	The number of loopback reply packets received  with sequence number errors
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: lbr_received_ok
            
            	The number of valid loopback reply packets received
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: lbr_received_bad
            
            	The number of loopback reply packets received  with corrupted data pattern
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'cfm-stats-ios-xe-oper'
            _revision = '2017-06-06'

            def __init__(self):
                super(CfmStatistics.CfmMeps.CfmMep, self).__init__()

                self.yang_name = "cfm-mep"
                self.yang_parent_name = "cfm-meps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"last-cleared" : ("last_cleared", CfmStatistics.CfmMeps.CfmMep.LastCleared)}
                self._child_list_classes = {}

                self.domain_name = YLeaf(YType.str, "domain-name")

                self.ma_name = YLeaf(YType.str, "ma-name")

                self.mpid = YLeaf(YType.uint32, "mpid")

                self.ccm_transmitted = YLeaf(YType.uint64, "ccm-transmitted")

                self.ccm_seq_errors = YLeaf(YType.uint64, "ccm-seq-errors")

                self.ltr_unexpected = YLeaf(YType.uint64, "ltr-unexpected")

                self.lbr_transmitted = YLeaf(YType.uint64, "lbr-transmitted")

                self.lbr_seq_errors = YLeaf(YType.uint64, "lbr-seq-errors")

                self.lbr_received_ok = YLeaf(YType.uint64, "lbr-received-ok")

                self.lbr_received_bad = YLeaf(YType.uint64, "lbr-received-bad")

                self.last_cleared = CfmStatistics.CfmMeps.CfmMep.LastCleared()
                self.last_cleared.parent = self
                self._children_name_map["last_cleared"] = "last-cleared"
                self._children_yang_names.add("last-cleared")
                self._segment_path = lambda: "cfm-mep" + "[domain-name='" + self.domain_name.get() + "']" + "[ma-name='" + self.ma_name.get() + "']" + "[mpid='" + self.mpid.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-cfm-oper:cfm-statistics/cfm-meps/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CfmStatistics.CfmMeps.CfmMep, ['domain_name', 'ma_name', 'mpid', 'ccm_transmitted', 'ccm_seq_errors', 'ltr_unexpected', 'lbr_transmitted', 'lbr_seq_errors', 'lbr_received_ok', 'lbr_received_bad'], name, value)


            class LastCleared(Entity):
                """
                Info on when the stats were last cleared
                
                .. attribute:: never
                
                	Never been cleared
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: time
                
                	Date and time of the last time stats were cleared
                	**type**\: str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                

                """

                _prefix = 'cfm-stats-ios-xe-oper'
                _revision = '2017-06-06'

                def __init__(self):
                    super(CfmStatistics.CfmMeps.CfmMep.LastCleared, self).__init__()

                    self.yang_name = "last-cleared"
                    self.yang_parent_name = "cfm-mep"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.never = YLeaf(YType.empty, "never")

                    self.time = YLeaf(YType.str, "time")
                    self._segment_path = lambda: "last-cleared"

                def __setattr__(self, name, value):
                    self._perform_setattr(CfmStatistics.CfmMeps.CfmMep.LastCleared, ['never', 'time'], name, value)

    def clone_ptr(self):
        self._top_entity = CfmStatistics()
        return self._top_entity

