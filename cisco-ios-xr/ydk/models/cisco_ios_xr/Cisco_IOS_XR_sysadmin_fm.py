""" Cisco_IOS_XR_sysadmin_fm 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

Fault management YANG model.

Copyright(c) 2014\-2017 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FmActionResultT(Enum):
    """
    FmActionResultT (Enum Class)

    The result of a certain fm action

    .. data:: SUCCESS = 0

    .. data:: FAILURE = 1

    .. data:: NO_OP = 2

    """

    SUCCESS = Enum.YLeaf(0, "SUCCESS")

    FAILURE = Enum.YLeaf(1, "FAILURE")

    NO_OP = Enum.YLeaf(2, "NO-OP")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
        return meta._meta_table['FmActionResultT']


class FmActionT(Enum):
    """
    FmActionT (Enum Class)

    The List of supported Action Types

    .. data:: ISOLATION = 0

    .. data:: MITIGATION = 1

    .. data:: RECOVERY = 2

    .. data:: CORRELATION = 3

    .. data:: ALARM = 4

    .. data:: REPORT = 5

    """

    ISOLATION = Enum.YLeaf(0, "ISOLATION")

    MITIGATION = Enum.YLeaf(1, "MITIGATION")

    RECOVERY = Enum.YLeaf(2, "RECOVERY")

    CORRELATION = Enum.YLeaf(3, "CORRELATION")

    ALARM = Enum.YLeaf(4, "ALARM")

    REPORT = Enum.YLeaf(5, "REPORT")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
        return meta._meta_table['FmActionT']


class FmCorrelationObjQualifierT(Enum):
    """
    FmCorrelationObjQualifierT (Enum Class)

    .. data:: QUALIFIER_IGNORED = 0

    .. data:: QUALIFIER_RACK = 1

    .. data:: QUALIFIER_SLOT = 2

    .. data:: QUALIFIER_OBJECT = 3

    """

    QUALIFIER_IGNORED = Enum.YLeaf(0, "QUALIFIER_IGNORED")

    QUALIFIER_RACK = Enum.YLeaf(1, "QUALIFIER_RACK")

    QUALIFIER_SLOT = Enum.YLeaf(2, "QUALIFIER_SLOT")

    QUALIFIER_OBJECT = Enum.YLeaf(3, "QUALIFIER_OBJECT")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
        return meta._meta_table['FmCorrelationObjQualifierT']


class FmFaultSeverityT(Enum):
    """
    FmFaultSeverityT (Enum Class)

    .. data:: CRITICAL = 0

    .. data:: MAJOR = 1

    .. data:: MINOR = 2

    .. data:: NR = 3

    """

    CRITICAL = Enum.YLeaf(0, "CRITICAL")

    MAJOR = Enum.YLeaf(1, "MAJOR")

    MINOR = Enum.YLeaf(2, "MINOR")

    NR = Enum.YLeaf(3, "NR")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
        return meta._meta_table['FmFaultSeverityT']


class FmFaultStateT(Enum):
    """
    FmFaultStateT (Enum Class)

    The status value for a given fault condition.

    .. data:: SET = 0

    .. data:: CLEAR = 1

    .. data:: INFO = 2

    .. data:: INVALID = 3

    .. data:: PARTIALLY_QUALIFIED = 4

    .. data:: SOAKING_BEFORE_SET = 5

    .. data:: SOAKING_BEFORE_CLEAR = 6

    .. data:: SUPPRESSED = 7

    .. data:: UPDATE = 8

    """

    SET = Enum.YLeaf(0, "SET")

    CLEAR = Enum.YLeaf(1, "CLEAR")

    INFO = Enum.YLeaf(2, "INFO")

    INVALID = Enum.YLeaf(3, "INVALID")

    PARTIALLY_QUALIFIED = Enum.YLeaf(4, "PARTIALLY_QUALIFIED")

    SOAKING_BEFORE_SET = Enum.YLeaf(5, "SOAKING_BEFORE_SET")

    SOAKING_BEFORE_CLEAR = Enum.YLeaf(6, "SOAKING_BEFORE_CLEAR")

    SUPPRESSED = Enum.YLeaf(7, "SUPPRESSED")

    UPDATE = Enum.YLeaf(8, "UPDATE")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
        return meta._meta_table['FmFaultStateT']


class FmHistoryStateT(Enum):
    """
    FmHistoryStateT (Enum Class)

    The fm history entry state.

    .. data:: FM_HISTORY_STATE_ACTIVE = 0

    .. data:: FM_HISTORY_STATE_CLEARED = 1

    .. data:: FM_HISTORY_STATE_INVALID = 2

    """

    FM_HISTORY_STATE_ACTIVE = Enum.YLeaf(0, "FM_HISTORY_STATE_ACTIVE")

    FM_HISTORY_STATE_CLEARED = Enum.YLeaf(1, "FM_HISTORY_STATE_CLEARED")

    FM_HISTORY_STATE_INVALID = Enum.YLeaf(2, "FM_HISTORY_STATE_INVALID")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
        return meta._meta_table['FmHistoryStateT']


class FmRuleEvalResultT(Enum):
    """
    FmRuleEvalResultT (Enum Class)

    The result status of the evaluation of a FM rule.

    .. data:: SUCCESS = 0

    .. data:: FAILURE = 1

    """

    SUCCESS = Enum.YLeaf(0, "SUCCESS")

    FAILURE = Enum.YLeaf(1, "FAILURE")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
        return meta._meta_table['FmRuleEvalResultT']


class FmServiceScopeT(Enum):
    """
    FmServiceScopeT (Enum Class)

    The fm service scope definting type.

    .. data:: FM_SERVICE_NODE_SCOPE = 0

    .. data:: FM_SERVICE_RACK_SCOPE = 1

    .. data:: FM_SERVICE_SYSTEM_SCOPE = 2

    """

    FM_SERVICE_NODE_SCOPE = Enum.YLeaf(0, "FM_SERVICE_NODE_SCOPE")

    FM_SERVICE_RACK_SCOPE = Enum.YLeaf(1, "FM_SERVICE_RACK_SCOPE")

    FM_SERVICE_SYSTEM_SCOPE = Enum.YLeaf(2, "FM_SERVICE_SYSTEM_SCOPE")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
        return meta._meta_table['FmServiceScopeT']


class GenericHaRole(Enum):
    """
    GenericHaRole (Enum Class)

    .. data:: no_ha_role = 0

    .. data:: Active = 1

    .. data:: Standby = 2

    """

    no_ha_role = Enum.YLeaf(0, "no-ha-role")

    Active = Enum.YLeaf(1, "Active")

    Standby = Enum.YLeaf(2, "Standby")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
        return meta._meta_table['GenericHaRole']



class Fm(_Entity_):
    """
    Sysadmin fault management operational data model
    
    .. attribute:: agents
    
    	
    	**type**\: list of  		 :py:class:`Agents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents>`
    
    	**config**\: False
    
    

    """

    _prefix = 'fm'
    _revision = '2016-04-12'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Fm, self).__init__()
        self._top_entity = None

        self.yang_name = "fm"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-fm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("agents", ("agents", Fm.Agents))])
        self._leafs = OrderedDict()

        self.agents = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-fm:fm"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Fm, [], name, value)


    class Agents(_Entity_):
        """
        
        
        .. attribute:: location  (key)
        
        	
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: process  (key)
        
        	
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: subsystem  (key)
        
        	
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: agent  (key)
        
        	
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: fm_initials
        
        	
        	**type**\:  :py:class:`FmInitials <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmInitials>`
        
        	**config**\: False
        
        .. attribute:: fm_table
        
        	
        	**type**\:  :py:class:`FmTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable>`
        
        	**config**\: False
        
        .. attribute:: fm_internals
        
        	
        	**type**\:  :py:class:`FmInternals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmInternals>`
        
        	**config**\: False
        
        .. attribute:: fm_alarm_mapping
        
        	
        	**type**\:  :py:class:`FmAlarmMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmAlarmMapping>`
        
        	**config**\: False
        
        .. attribute:: fm_statistics
        
        	
        	**type**\:  :py:class:`FmStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmStatistics>`
        
        	**config**\: False
        
        

        """

        _prefix = 'fm'
        _revision = '2016-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Fm.Agents, self).__init__()

            self.yang_name = "agents"
            self.yang_parent_name = "fm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['location','process','subsystem','agent']
            self._child_classes = OrderedDict([("fm_initials", ("fm_initials", Fm.Agents.FmInitials)), ("fm_table", ("fm_table", Fm.Agents.FmTable)), ("fm_internals", ("fm_internals", Fm.Agents.FmInternals)), ("fm_alarm_mapping", ("fm_alarm_mapping", Fm.Agents.FmAlarmMapping)), ("fm_statistics", ("fm_statistics", Fm.Agents.FmStatistics))])
            self._leafs = OrderedDict([
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ('process', (YLeaf(YType.str, 'process'), ['str'])),
                ('subsystem', (YLeaf(YType.str, 'subsystem'), ['str'])),
                ('agent', (YLeaf(YType.str, 'agent'), ['str'])),
            ])
            self.location = None
            self.process = None
            self.subsystem = None
            self.agent = None

            self.fm_initials = Fm.Agents.FmInitials()
            self.fm_initials.parent = self
            self._children_name_map["fm_initials"] = "fm_initials"

            self.fm_table = Fm.Agents.FmTable()
            self.fm_table.parent = self
            self._children_name_map["fm_table"] = "fm_table"

            self.fm_internals = Fm.Agents.FmInternals()
            self.fm_internals.parent = self
            self._children_name_map["fm_internals"] = "fm_internals"

            self.fm_alarm_mapping = Fm.Agents.FmAlarmMapping()
            self.fm_alarm_mapping.parent = self
            self._children_name_map["fm_alarm_mapping"] = "fm_alarm_mapping"

            self.fm_statistics = Fm.Agents.FmStatistics()
            self.fm_statistics.parent = self
            self._children_name_map["fm_statistics"] = "fm_statistics"
            self._segment_path = lambda: "agents" + "[location='" + str(self.location) + "']" + "[process='" + str(self.process) + "']" + "[subsystem='" + str(self.subsystem) + "']" + "[agent='" + str(self.agent) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-fm:fm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Fm.Agents, ['location', 'process', 'subsystem', 'agent'], name, value)


        class FmInitials(_Entity_):
            """
            
            
            .. attribute:: levm
            
            	The levm pointer supplied to fm infra
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: comp_id
            
            	The owner component Id
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: process
            
            	The name of the process in which this fm instance is active
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: default_rule_cb
            
            	Default rule callback pointer
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: default_action_cb
            
            	Default action callback pointer
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: default_notif_cb
            
            	Default notification callback pointer
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: default_error_cb
            
            	Default error callback pointer
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: replica_cb
            
            	Data Replica callback pointer
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'fm'
            _revision = '2016-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Fm.Agents.FmInitials, self).__init__()

                self.yang_name = "fm_initials"
                self.yang_parent_name = "agents"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('levm', (YLeaf(YType.uint64, 'levm'), ['int'])),
                    ('comp_id', (YLeaf(YType.uint32, 'comp_id'), ['int'])),
                    ('process', (YLeaf(YType.str, 'process'), ['str'])),
                    ('default_rule_cb', (YLeaf(YType.uint64, 'default_rule_cb'), ['int'])),
                    ('default_action_cb', (YLeaf(YType.uint64, 'default_action_cb'), ['int'])),
                    ('default_notif_cb', (YLeaf(YType.uint64, 'default_notif_cb'), ['int'])),
                    ('default_error_cb', (YLeaf(YType.uint64, 'default_error_cb'), ['int'])),
                    ('replica_cb', (YLeaf(YType.uint64, 'replica_cb'), ['int'])),
                ])
                self.levm = None
                self.comp_id = None
                self.process = None
                self.default_rule_cb = None
                self.default_action_cb = None
                self.default_notif_cb = None
                self.default_error_cb = None
                self.replica_cb = None
                self._segment_path = lambda: "fm_initials"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Fm.Agents.FmInitials, ['levm', 'comp_id', 'process', 'default_rule_cb', 'default_action_cb', 'default_notif_cb', 'default_error_cb', 'replica_cb'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                return meta._meta_table['Fm.Agents.FmInitials']['meta_info']


        class FmTable(_Entity_):
            """
            
            
            .. attribute:: brief
            
            	
            	**type**\: list of  		 :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Brief>`
            
            	**config**\: False
            
            .. attribute:: entry
            
            	
            	**type**\: list of  		 :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry>`
            
            	**config**\: False
            
            

            """

            _prefix = 'fm'
            _revision = '2016-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Fm.Agents.FmTable, self).__init__()

                self.yang_name = "fm_table"
                self.yang_parent_name = "agents"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("brief", ("brief", Fm.Agents.FmTable.Brief)), ("entry", ("entry", Fm.Agents.FmTable.Entry))])
                self._leafs = OrderedDict()

                self.brief = YList(self)
                self.entry = YList(self)
                self._segment_path = lambda: "fm_table"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Fm.Agents.FmTable, [], name, value)


            class Brief(_Entity_):
                """
                
                
                .. attribute:: fm_subsystem_id  (key)
                
                	Fault sub\-system identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: fm_fault_type  (key)
                
                	Fault type identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: fm_fault_tag  (key)
                
                	Fault tag identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: name
                
                	A descriptive name for the fault
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'fm'
                _revision = '2016-04-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Fm.Agents.FmTable.Brief, self).__init__()

                    self.yang_name = "brief"
                    self.yang_parent_name = "fm_table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['fm_subsystem_id','fm_fault_type','fm_fault_tag']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                        ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                        ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.fm_subsystem_id = None
                    self.fm_fault_type = None
                    self.fm_fault_tag = None
                    self.name = None
                    self._segment_path = lambda: "brief" + "[fm_subsystem_id='" + str(self.fm_subsystem_id) + "']" + "[fm_fault_type='" + str(self.fm_fault_type) + "']" + "[fm_fault_tag='" + str(self.fm_fault_tag) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Fm.Agents.FmTable.Brief, ['fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag', 'name'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                    return meta._meta_table['Fm.Agents.FmTable.Brief']['meta_info']


            class Entry(_Entity_):
                """
                
                
                .. attribute:: fm_subsystem_id  (key)
                
                	Fault sub\-system identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: fm_fault_type  (key)
                
                	Fault type identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: fm_fault_tag  (key)
                
                	Fault tag identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: detail
                
                	
                	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.Detail>`
                
                	**config**\: False
                
                .. attribute:: causal_list
                
                	Causal list of fault ids for the specified fault
                	**type**\: list of  		 :py:class:`CausalList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.CausalList>`
                
                	**config**\: False
                
                .. attribute:: dependency_list
                
                	Dependency list of fault ids
                	**type**\: list of  		 :py:class:`DependencyList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.DependencyList>`
                
                	**config**\: False
                
                .. attribute:: propagation_list
                
                	Propagation list of fault agents
                	**type**\: list of  		 :py:class:`PropagationList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.PropagationList>`
                
                	**config**\: False
                
                .. attribute:: notification_list
                
                	Notification list of fault agents
                	**type**\: list of  		 :py:class:`NotificationList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.NotificationList>`
                
                	**config**\: False
                
                .. attribute:: escalation_list
                
                	escalation list of fault agents
                	**type**\: list of  		 :py:class:`EscalationList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.EscalationList>`
                
                	**config**\: False
                
                .. attribute:: faults
                
                	
                	**type**\:  :py:class:`Faults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.Faults>`
                
                	**config**\: False
                
                .. attribute:: waiting_list
                
                	
                	**type**\:  :py:class:`WaitingList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.WaitingList>`
                
                	**config**\: False
                
                

                """

                _prefix = 'fm'
                _revision = '2016-04-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Fm.Agents.FmTable.Entry, self).__init__()

                    self.yang_name = "entry"
                    self.yang_parent_name = "fm_table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['fm_subsystem_id','fm_fault_type','fm_fault_tag']
                    self._child_classes = OrderedDict([("detail", ("detail", Fm.Agents.FmTable.Entry.Detail)), ("causal_list", ("causal_list", Fm.Agents.FmTable.Entry.CausalList)), ("dependency_list", ("dependency_list", Fm.Agents.FmTable.Entry.DependencyList)), ("propagation_list", ("propagation_list", Fm.Agents.FmTable.Entry.PropagationList)), ("notification_list", ("notification_list", Fm.Agents.FmTable.Entry.NotificationList)), ("escalation_list", ("escalation_list", Fm.Agents.FmTable.Entry.EscalationList)), ("faults", ("faults", Fm.Agents.FmTable.Entry.Faults)), ("waiting_list", ("waiting_list", Fm.Agents.FmTable.Entry.WaitingList))])
                    self._leafs = OrderedDict([
                        ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                        ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                        ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                    ])
                    self.fm_subsystem_id = None
                    self.fm_fault_type = None
                    self.fm_fault_tag = None

                    self.detail = Fm.Agents.FmTable.Entry.Detail()
                    self.detail.parent = self
                    self._children_name_map["detail"] = "detail"

                    self.faults = Fm.Agents.FmTable.Entry.Faults()
                    self.faults.parent = self
                    self._children_name_map["faults"] = "faults"

                    self.waiting_list = Fm.Agents.FmTable.Entry.WaitingList()
                    self.waiting_list.parent = self
                    self._children_name_map["waiting_list"] = "waiting_list"

                    self.causal_list = YList(self)
                    self.dependency_list = YList(self)
                    self.propagation_list = YList(self)
                    self.notification_list = YList(self)
                    self.escalation_list = YList(self)
                    self._segment_path = lambda: "entry" + "[fm_subsystem_id='" + str(self.fm_subsystem_id) + "']" + "[fm_fault_type='" + str(self.fm_fault_type) + "']" + "[fm_fault_tag='" + str(self.fm_fault_tag) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Fm.Agents.FmTable.Entry, ['fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag'], name, value)


                class Detail(_Entity_):
                    """
                    
                    
                    .. attribute:: fm_subsystem_id
                    
                    	Fault sub\-system identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: fm_fault_type
                    
                    	Fault type identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: fm_fault_tag
                    
                    	Fault tag identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: name
                    
                    	A descriptive name for the fault
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Description of the fault
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: detection_logic
                    
                    	Fault detection logic
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: corr_obj_qualifier
                    
                    	The qualifier for the object used for correlation
                    	**type**\:  :py:class:`FmCorrelationObjQualifierT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmCorrelationObjQualifierT>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fm'
                    _revision = '2016-04-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Fm.Agents.FmTable.Entry.Detail, self).__init__()

                        self.yang_name = "detail"
                        self.yang_parent_name = "entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                            ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                            ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('detection_logic', (YLeaf(YType.str, 'detection_logic'), ['str'])),
                            ('corr_obj_qualifier', (YLeaf(YType.enumeration, 'corr_obj_qualifier'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmCorrelationObjQualifierT', '')])),
                        ])
                        self.fm_subsystem_id = None
                        self.fm_fault_type = None
                        self.fm_fault_tag = None
                        self.name = None
                        self.description = None
                        self.detection_logic = None
                        self.corr_obj_qualifier = None
                        self._segment_path = lambda: "detail"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fm.Agents.FmTable.Entry.Detail, ['fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag', 'name', 'description', 'detection_logic', 'corr_obj_qualifier'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                        return meta._meta_table['Fm.Agents.FmTable.Entry.Detail']['meta_info']


                class CausalList(_Entity_):
                    """
                    Causal list of fault ids for the specified fault.
                    
                    .. attribute:: fm_subsystem_id  (key)
                    
                    	Fault sub\-system identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: fm_fault_type  (key)
                    
                    	Fault type identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: fm_fault_tag  (key)
                    
                    	Fault tag identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fm'
                    _revision = '2016-04-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Fm.Agents.FmTable.Entry.CausalList, self).__init__()

                        self.yang_name = "causal_list"
                        self.yang_parent_name = "entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['fm_subsystem_id','fm_fault_type','fm_fault_tag']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                            ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                            ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                        ])
                        self.fm_subsystem_id = None
                        self.fm_fault_type = None
                        self.fm_fault_tag = None
                        self._segment_path = lambda: "causal_list" + "[fm_subsystem_id='" + str(self.fm_subsystem_id) + "']" + "[fm_fault_type='" + str(self.fm_fault_type) + "']" + "[fm_fault_tag='" + str(self.fm_fault_tag) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fm.Agents.FmTable.Entry.CausalList, ['fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                        return meta._meta_table['Fm.Agents.FmTable.Entry.CausalList']['meta_info']


                class DependencyList(_Entity_):
                    """
                    Dependency list of fault ids.
                    
                    .. attribute:: fm_subsystem_id  (key)
                    
                    	Fault sub\-system identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: fm_fault_type  (key)
                    
                    	Fault type identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: fm_fault_tag  (key)
                    
                    	Fault tag identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fm'
                    _revision = '2016-04-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Fm.Agents.FmTable.Entry.DependencyList, self).__init__()

                        self.yang_name = "dependency_list"
                        self.yang_parent_name = "entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['fm_subsystem_id','fm_fault_type','fm_fault_tag']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                            ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                            ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                        ])
                        self.fm_subsystem_id = None
                        self.fm_fault_type = None
                        self.fm_fault_tag = None
                        self._segment_path = lambda: "dependency_list" + "[fm_subsystem_id='" + str(self.fm_subsystem_id) + "']" + "[fm_fault_type='" + str(self.fm_fault_type) + "']" + "[fm_fault_tag='" + str(self.fm_fault_tag) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fm.Agents.FmTable.Entry.DependencyList, ['fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                        return meta._meta_table['Fm.Agents.FmTable.Entry.DependencyList']['meta_info']


                class PropagationList(_Entity_):
                    """
                    Propagation list of fault agents.
                    
                    .. attribute:: fm_subsystem_id  (key)
                    
                    	Fault sub\-system identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: fm_fault_type  (key)
                    
                    	Fault type identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: fm_fault_tag  (key)
                    
                    	Fault tag identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: remote_agent_id
                    
                    	The remote agent id assocaited with this fault
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fm'
                    _revision = '2016-04-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Fm.Agents.FmTable.Entry.PropagationList, self).__init__()

                        self.yang_name = "propagation_list"
                        self.yang_parent_name = "entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['fm_subsystem_id','fm_fault_type','fm_fault_tag']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                            ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                            ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                            ('remote_agent_id', (YLeaf(YType.str, 'remote_agent_id'), ['str'])),
                        ])
                        self.fm_subsystem_id = None
                        self.fm_fault_type = None
                        self.fm_fault_tag = None
                        self.remote_agent_id = None
                        self._segment_path = lambda: "propagation_list" + "[fm_subsystem_id='" + str(self.fm_subsystem_id) + "']" + "[fm_fault_type='" + str(self.fm_fault_type) + "']" + "[fm_fault_tag='" + str(self.fm_fault_tag) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fm.Agents.FmTable.Entry.PropagationList, ['fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag', 'remote_agent_id'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                        return meta._meta_table['Fm.Agents.FmTable.Entry.PropagationList']['meta_info']


                class NotificationList(_Entity_):
                    """
                    Notification list of fault agents.
                    
                    .. attribute:: fm_subsystem_id  (key)
                    
                    	Fault sub\-system identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: fm_fault_type  (key)
                    
                    	Fault type identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: fm_fault_tag  (key)
                    
                    	Fault tag identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: remote_agent_id
                    
                    	The remote agent id assocaited with this fault
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fm'
                    _revision = '2016-04-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Fm.Agents.FmTable.Entry.NotificationList, self).__init__()

                        self.yang_name = "notification_list"
                        self.yang_parent_name = "entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['fm_subsystem_id','fm_fault_type','fm_fault_tag']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                            ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                            ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                            ('remote_agent_id', (YLeaf(YType.str, 'remote_agent_id'), ['str'])),
                        ])
                        self.fm_subsystem_id = None
                        self.fm_fault_type = None
                        self.fm_fault_tag = None
                        self.remote_agent_id = None
                        self._segment_path = lambda: "notification_list" + "[fm_subsystem_id='" + str(self.fm_subsystem_id) + "']" + "[fm_fault_type='" + str(self.fm_fault_type) + "']" + "[fm_fault_tag='" + str(self.fm_fault_tag) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fm.Agents.FmTable.Entry.NotificationList, ['fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag', 'remote_agent_id'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                        return meta._meta_table['Fm.Agents.FmTable.Entry.NotificationList']['meta_info']


                class EscalationList(_Entity_):
                    """
                    escalation list of fault agents.
                    
                    .. attribute:: fm_subsystem_id  (key)
                    
                    	Fault sub\-system identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: fm_fault_type  (key)
                    
                    	Fault type identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: fm_fault_tag  (key)
                    
                    	Fault tag identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: remote_agent_id
                    
                    	The remote agent id assocaited with this fault
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fm'
                    _revision = '2016-04-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Fm.Agents.FmTable.Entry.EscalationList, self).__init__()

                        self.yang_name = "escalation_list"
                        self.yang_parent_name = "entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['fm_subsystem_id','fm_fault_type','fm_fault_tag']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                            ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                            ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                            ('remote_agent_id', (YLeaf(YType.str, 'remote_agent_id'), ['str'])),
                        ])
                        self.fm_subsystem_id = None
                        self.fm_fault_type = None
                        self.fm_fault_tag = None
                        self.remote_agent_id = None
                        self._segment_path = lambda: "escalation_list" + "[fm_subsystem_id='" + str(self.fm_subsystem_id) + "']" + "[fm_fault_type='" + str(self.fm_fault_type) + "']" + "[fm_fault_tag='" + str(self.fm_fault_tag) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fm.Agents.FmTable.Entry.EscalationList, ['fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag', 'remote_agent_id'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                        return meta._meta_table['Fm.Agents.FmTable.Entry.EscalationList']['meta_info']


                class Faults(_Entity_):
                    """
                    
                    
                    .. attribute:: active
                    
                    	
                    	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.Faults.Active>`
                    
                    	**config**\: False
                    
                    .. attribute:: history
                    
                    	
                    	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.Faults.History>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fm'
                    _revision = '2016-04-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Fm.Agents.FmTable.Entry.Faults, self).__init__()

                        self.yang_name = "faults"
                        self.yang_parent_name = "entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("active", ("active", Fm.Agents.FmTable.Entry.Faults.Active)), ("history", ("history", Fm.Agents.FmTable.Entry.Faults.History))])
                        self._leafs = OrderedDict()

                        self.active = Fm.Agents.FmTable.Entry.Faults.Active()
                        self.active.parent = self
                        self._children_name_map["active"] = "active"

                        self.history = Fm.Agents.FmTable.Entry.Faults.History()
                        self.history.parent = self
                        self._children_name_map["history"] = "history"
                        self._segment_path = lambda: "faults"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fm.Agents.FmTable.Entry.Faults, [], name, value)


                    class Active(_Entity_):
                        """
                        
                        
                        .. attribute:: brief
                        
                        	
                        	**type**\: list of  		 :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.Faults.Active.Brief>`
                        
                        	**config**\: False
                        
                        .. attribute:: detail
                        
                        	
                        	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.Faults.Active.Detail>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'fm'
                        _revision = '2016-04-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Fm.Agents.FmTable.Entry.Faults.Active, self).__init__()

                            self.yang_name = "active"
                            self.yang_parent_name = "faults"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("brief", ("brief", Fm.Agents.FmTable.Entry.Faults.Active.Brief)), ("detail", ("detail", Fm.Agents.FmTable.Entry.Faults.Active.Detail))])
                            self._leafs = OrderedDict()

                            self.brief = YList(self)
                            self.detail = YList(self)
                            self._segment_path = lambda: "active"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Fm.Agents.FmTable.Entry.Faults.Active, [], name, value)


                        class Brief(_Entity_):
                            """
                            
                            
                            .. attribute:: object_id  (key)
                            
                            	The fault object ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fault_timestamp
                            
                            	The fault occurence timestamp
                            	**type**\: str
                            
                            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fm'
                            _revision = '2016-04-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Fm.Agents.FmTable.Entry.Faults.Active.Brief, self).__init__()

                                self.yang_name = "brief"
                                self.yang_parent_name = "active"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['object_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('object_id', (YLeaf(YType.str, 'object_id'), ['str'])),
                                    ('fault_timestamp', (YLeaf(YType.str, 'fault_timestamp'), ['str'])),
                                ])
                                self.object_id = None
                                self.fault_timestamp = None
                                self._segment_path = lambda: "brief" + "[object_id='" + str(self.object_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Fm.Agents.FmTable.Entry.Faults.Active.Brief, ['object_id', 'fault_timestamp'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                                return meta._meta_table['Fm.Agents.FmTable.Entry.Faults.Active.Brief']['meta_info']


                        class Detail(_Entity_):
                            """
                            
                            
                            .. attribute:: object_id  (key)
                            
                            	The fault object ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fm_subsystem_id
                            
                            	Fault sub\-system identifier
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fm_fault_type
                            
                            	Fault type identifier
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fm_fault_tag
                            
                            	Fault tag identifier
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fault_severity
                            
                            	The severity of the fault reported out
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: fault_state
                            
                            	The state of the fault
                            	**type**\:  :py:class:`FmFaultStateT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmFaultStateT>`
                            
                            	**config**\: False
                            
                            .. attribute:: fault_agent_id
                            
                            	The agent id associated with the fault
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fault_timestamp
                            
                            	The fault occurence timestamp
                            	**type**\: str
                            
                            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                            
                            	**config**\: False
                            
                            .. attribute:: fault_timer_state
                            
                            	The state of the timer associated with this fault
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: fault_processed
                            
                            	The fault is acted on
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: mitigation_result
                            
                            	The result of the mitigation action on the fault
                            	**type**\:  :py:class:`FmActionResultT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmActionResultT>`
                            
                            	**config**\: False
                            
                            .. attribute:: recovery_result
                            
                            	The result of the recovery action on the fault
                            	**type**\:  :py:class:`FmActionResultT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmActionResultT>`
                            
                            	**config**\: False
                            
                            .. attribute:: correlation_result
                            
                            	The result of the correlation action on the fault
                            	**type**\:  :py:class:`FmActionResultT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmActionResultT>`
                            
                            	**config**\: False
                            
                            .. attribute:: alarm_result
                            
                            	The result of the alarm action on the fault
                            	**type**\:  :py:class:`FmActionResultT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmActionResultT>`
                            
                            	**config**\: False
                            
                            .. attribute:: default_result
                            
                            	The result of the default action on the fault
                            	**type**\:  :py:class:`FmActionResultT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmActionResultT>`
                            
                            	**config**\: False
                            
                            .. attribute:: opaque_data_len
                            
                            	The length of opaque data bytes
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: occurrence_count
                            
                            	The occurrence count of the fault
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: history_state
                            
                            	The history state of the fault
                            	**type**\:  :py:class:`FmHistoryStateT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmHistoryStateT>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fm'
                            _revision = '2016-04-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Fm.Agents.FmTable.Entry.Faults.Active.Detail, self).__init__()

                                self.yang_name = "detail"
                                self.yang_parent_name = "active"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['object_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('object_id', (YLeaf(YType.str, 'object_id'), ['str'])),
                                    ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                                    ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                                    ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                                    ('fault_severity', (YLeaf(YType.uint16, 'fault_severity'), ['int'])),
                                    ('fault_state', (YLeaf(YType.enumeration, 'fault_state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmFaultStateT', '')])),
                                    ('fault_agent_id', (YLeaf(YType.str, 'fault_agent_id'), ['str'])),
                                    ('fault_timestamp', (YLeaf(YType.str, 'fault_timestamp'), ['str'])),
                                    ('fault_timer_state', (YLeaf(YType.boolean, 'fault_timer_state'), ['bool'])),
                                    ('fault_processed', (YLeaf(YType.boolean, 'fault_processed'), ['bool'])),
                                    ('mitigation_result', (YLeaf(YType.enumeration, 'mitigation_result'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmActionResultT', '')])),
                                    ('recovery_result', (YLeaf(YType.enumeration, 'recovery_result'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmActionResultT', '')])),
                                    ('correlation_result', (YLeaf(YType.enumeration, 'correlation_result'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmActionResultT', '')])),
                                    ('alarm_result', (YLeaf(YType.enumeration, 'alarm_result'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmActionResultT', '')])),
                                    ('default_result', (YLeaf(YType.enumeration, 'default_result'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmActionResultT', '')])),
                                    ('opaque_data_len', (YLeaf(YType.uint16, 'opaque_data_len'), ['int'])),
                                    ('occurrence_count', (YLeaf(YType.uint64, 'occurrence_count'), ['int'])),
                                    ('history_state', (YLeaf(YType.enumeration, 'history_state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmHistoryStateT', '')])),
                                ])
                                self.object_id = None
                                self.fm_subsystem_id = None
                                self.fm_fault_type = None
                                self.fm_fault_tag = None
                                self.fault_severity = None
                                self.fault_state = None
                                self.fault_agent_id = None
                                self.fault_timestamp = None
                                self.fault_timer_state = None
                                self.fault_processed = None
                                self.mitigation_result = None
                                self.recovery_result = None
                                self.correlation_result = None
                                self.alarm_result = None
                                self.default_result = None
                                self.opaque_data_len = None
                                self.occurrence_count = None
                                self.history_state = None
                                self._segment_path = lambda: "detail" + "[object_id='" + str(self.object_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Fm.Agents.FmTable.Entry.Faults.Active.Detail, ['object_id', 'fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag', 'fault_severity', 'fault_state', 'fault_agent_id', 'fault_timestamp', 'fault_timer_state', 'fault_processed', 'mitigation_result', 'recovery_result', 'correlation_result', 'alarm_result', 'default_result', 'opaque_data_len', 'occurrence_count', 'history_state'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                                return meta._meta_table['Fm.Agents.FmTable.Entry.Faults.Active.Detail']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                            return meta._meta_table['Fm.Agents.FmTable.Entry.Faults.Active']['meta_info']


                    class History(_Entity_):
                        """
                        
                        
                        .. attribute:: brief
                        
                        	
                        	**type**\: list of  		 :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.Faults.History.Brief>`
                        
                        	**config**\: False
                        
                        .. attribute:: detail
                        
                        	
                        	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.Faults.History.Detail>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'fm'
                        _revision = '2016-04-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Fm.Agents.FmTable.Entry.Faults.History, self).__init__()

                            self.yang_name = "history"
                            self.yang_parent_name = "faults"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("brief", ("brief", Fm.Agents.FmTable.Entry.Faults.History.Brief)), ("detail", ("detail", Fm.Agents.FmTable.Entry.Faults.History.Detail))])
                            self._leafs = OrderedDict()

                            self.brief = YList(self)
                            self.detail = YList(self)
                            self._segment_path = lambda: "history"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Fm.Agents.FmTable.Entry.Faults.History, [], name, value)


                        class Brief(_Entity_):
                            """
                            
                            
                            .. attribute:: object_id  (key)
                            
                            	The fault object ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fault_timestamp
                            
                            	The fault occurence timestamp
                            	**type**\: str
                            
                            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fm'
                            _revision = '2016-04-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Fm.Agents.FmTable.Entry.Faults.History.Brief, self).__init__()

                                self.yang_name = "brief"
                                self.yang_parent_name = "history"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['object_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('object_id', (YLeaf(YType.str, 'object_id'), ['str'])),
                                    ('fault_timestamp', (YLeaf(YType.str, 'fault_timestamp'), ['str'])),
                                ])
                                self.object_id = None
                                self.fault_timestamp = None
                                self._segment_path = lambda: "brief" + "[object_id='" + str(self.object_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Fm.Agents.FmTable.Entry.Faults.History.Brief, ['object_id', 'fault_timestamp'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                                return meta._meta_table['Fm.Agents.FmTable.Entry.Faults.History.Brief']['meta_info']


                        class Detail(_Entity_):
                            """
                            
                            
                            .. attribute:: object_id  (key)
                            
                            	The fault object ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fm_subsystem_id
                            
                            	Fault sub\-system identifier
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fm_fault_type
                            
                            	Fault type identifier
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fm_fault_tag
                            
                            	Fault tag identifier
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fault_severity
                            
                            	The severity of the fault reported out
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: fault_state
                            
                            	The state of the fault
                            	**type**\:  :py:class:`FmFaultStateT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmFaultStateT>`
                            
                            	**config**\: False
                            
                            .. attribute:: fault_agent_id
                            
                            	The agent id associated with the fault
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: fault_timestamp
                            
                            	The fault occurence timestamp
                            	**type**\: str
                            
                            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                            
                            	**config**\: False
                            
                            .. attribute:: fault_timer_state
                            
                            	The state of the timer associated with this fault
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: fault_processed
                            
                            	The fault is acted on
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: mitigation_result
                            
                            	The result of the mitigation action on the fault
                            	**type**\:  :py:class:`FmActionResultT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmActionResultT>`
                            
                            	**config**\: False
                            
                            .. attribute:: recovery_result
                            
                            	The result of the recovery action on the fault
                            	**type**\:  :py:class:`FmActionResultT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmActionResultT>`
                            
                            	**config**\: False
                            
                            .. attribute:: correlation_result
                            
                            	The result of the correlation action on the fault
                            	**type**\:  :py:class:`FmActionResultT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmActionResultT>`
                            
                            	**config**\: False
                            
                            .. attribute:: alarm_result
                            
                            	The result of the alarm action on the fault
                            	**type**\:  :py:class:`FmActionResultT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmActionResultT>`
                            
                            	**config**\: False
                            
                            .. attribute:: default_result
                            
                            	The result of the default action on the fault
                            	**type**\:  :py:class:`FmActionResultT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmActionResultT>`
                            
                            	**config**\: False
                            
                            .. attribute:: opaque_data_len
                            
                            	The length of opaque data bytes
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            .. attribute:: occurrence_count
                            
                            	The occurrence count of the fault
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: history_state
                            
                            	The history state of the fault
                            	**type**\:  :py:class:`FmHistoryStateT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmHistoryStateT>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fm'
                            _revision = '2016-04-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Fm.Agents.FmTable.Entry.Faults.History.Detail, self).__init__()

                                self.yang_name = "detail"
                                self.yang_parent_name = "history"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['object_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('object_id', (YLeaf(YType.str, 'object_id'), ['str'])),
                                    ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                                    ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                                    ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                                    ('fault_severity', (YLeaf(YType.uint16, 'fault_severity'), ['int'])),
                                    ('fault_state', (YLeaf(YType.enumeration, 'fault_state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmFaultStateT', '')])),
                                    ('fault_agent_id', (YLeaf(YType.str, 'fault_agent_id'), ['str'])),
                                    ('fault_timestamp', (YLeaf(YType.str, 'fault_timestamp'), ['str'])),
                                    ('fault_timer_state', (YLeaf(YType.boolean, 'fault_timer_state'), ['bool'])),
                                    ('fault_processed', (YLeaf(YType.boolean, 'fault_processed'), ['bool'])),
                                    ('mitigation_result', (YLeaf(YType.enumeration, 'mitigation_result'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmActionResultT', '')])),
                                    ('recovery_result', (YLeaf(YType.enumeration, 'recovery_result'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmActionResultT', '')])),
                                    ('correlation_result', (YLeaf(YType.enumeration, 'correlation_result'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmActionResultT', '')])),
                                    ('alarm_result', (YLeaf(YType.enumeration, 'alarm_result'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmActionResultT', '')])),
                                    ('default_result', (YLeaf(YType.enumeration, 'default_result'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmActionResultT', '')])),
                                    ('opaque_data_len', (YLeaf(YType.uint16, 'opaque_data_len'), ['int'])),
                                    ('occurrence_count', (YLeaf(YType.uint64, 'occurrence_count'), ['int'])),
                                    ('history_state', (YLeaf(YType.enumeration, 'history_state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmHistoryStateT', '')])),
                                ])
                                self.object_id = None
                                self.fm_subsystem_id = None
                                self.fm_fault_type = None
                                self.fm_fault_tag = None
                                self.fault_severity = None
                                self.fault_state = None
                                self.fault_agent_id = None
                                self.fault_timestamp = None
                                self.fault_timer_state = None
                                self.fault_processed = None
                                self.mitigation_result = None
                                self.recovery_result = None
                                self.correlation_result = None
                                self.alarm_result = None
                                self.default_result = None
                                self.opaque_data_len = None
                                self.occurrence_count = None
                                self.history_state = None
                                self._segment_path = lambda: "detail" + "[object_id='" + str(self.object_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Fm.Agents.FmTable.Entry.Faults.History.Detail, ['object_id', 'fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag', 'fault_severity', 'fault_state', 'fault_agent_id', 'fault_timestamp', 'fault_timer_state', 'fault_processed', 'mitigation_result', 'recovery_result', 'correlation_result', 'alarm_result', 'default_result', 'opaque_data_len', 'occurrence_count', 'history_state'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                                return meta._meta_table['Fm.Agents.FmTable.Entry.Faults.History.Detail']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                            return meta._meta_table['Fm.Agents.FmTable.Entry.Faults.History']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                        return meta._meta_table['Fm.Agents.FmTable.Entry.Faults']['meta_info']


                class WaitingList(_Entity_):
                    """
                    
                    
                    .. attribute:: brief
                    
                    	
                    	**type**\: list of  		 :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.WaitingList.Brief>`
                    
                    	**config**\: False
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: list of  		 :py:class:`Entry_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmTable.Entry.WaitingList.Entry_>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fm'
                    _revision = '2016-04-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Fm.Agents.FmTable.Entry.WaitingList, self).__init__()

                        self.yang_name = "waiting_list"
                        self.yang_parent_name = "entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("brief", ("brief", Fm.Agents.FmTable.Entry.WaitingList.Brief)), ("entry", ("entry", Fm.Agents.FmTable.Entry.WaitingList.Entry_))])
                        self._leafs = OrderedDict()

                        self.brief = YList(self)
                        self.entry = YList(self)
                        self._segment_path = lambda: "waiting_list"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fm.Agents.FmTable.Entry.WaitingList, [], name, value)


                    class Brief(_Entity_):
                        """
                        
                        
                        .. attribute:: fm_subsystem_id  (key)
                        
                        	Fault sub\-system identifier
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: fm_fault_type  (key)
                        
                        	Fault type identifier
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: fm_fault_tag  (key)
                        
                        	Fault tag identifier
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: object_id
                        
                        	The object Id of the entity that generated the fault
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: fault_timestamp
                        
                        	The timestamp at which the fault occurred
                        	**type**\: str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        	**config**\: False
                        
                        .. attribute:: fault_state
                        
                        	The state pf tje causal fault
                        	**type**\:  :py:class:`FmFaultStateT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmFaultStateT>`
                        
                        	**config**\: False
                        
                        .. attribute:: fault_count
                        
                        	Count of occurrence of the fault event
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: fault_flag
                        
                        	FM correlation engine flag, internal
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'fm'
                        _revision = '2016-04-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Fm.Agents.FmTable.Entry.WaitingList.Brief, self).__init__()

                            self.yang_name = "brief"
                            self.yang_parent_name = "waiting_list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['fm_subsystem_id','fm_fault_type','fm_fault_tag']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                                ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                                ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                                ('object_id', (YLeaf(YType.str, 'object_id'), ['str'])),
                                ('fault_timestamp', (YLeaf(YType.str, 'fault_timestamp'), ['str'])),
                                ('fault_state', (YLeaf(YType.enumeration, 'fault_state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmFaultStateT', '')])),
                                ('fault_count', (YLeaf(YType.uint64, 'fault_count'), ['int'])),
                                ('fault_flag', (YLeaf(YType.uint64, 'fault_flag'), ['int'])),
                            ])
                            self.fm_subsystem_id = None
                            self.fm_fault_type = None
                            self.fm_fault_tag = None
                            self.object_id = None
                            self.fault_timestamp = None
                            self.fault_state = None
                            self.fault_count = None
                            self.fault_flag = None
                            self._segment_path = lambda: "brief" + "[fm_subsystem_id='" + str(self.fm_subsystem_id) + "']" + "[fm_fault_type='" + str(self.fm_fault_type) + "']" + "[fm_fault_tag='" + str(self.fm_fault_tag) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Fm.Agents.FmTable.Entry.WaitingList.Brief, ['fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag', 'object_id', 'fault_timestamp', 'fault_state', 'fault_count', 'fault_flag'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                            return meta._meta_table['Fm.Agents.FmTable.Entry.WaitingList.Brief']['meta_info']


                    class Entry_(_Entity_):
                        """
                        
                        
                        .. attribute:: fm_subsystem_id  (key)
                        
                        	Fault sub\-system identifier
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: fm_fault_type  (key)
                        
                        	Fault type identifier
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: fm_fault_tag  (key)
                        
                        	Fault tag identifier
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: object_id
                        
                        	The object Id of the entity that generated the fault
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: fault_timestamp
                        
                        	The timestamp at which the fault occurred
                        	**type**\: str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        	**config**\: False
                        
                        .. attribute:: fault_state
                        
                        	The state pf tje causal fault
                        	**type**\:  :py:class:`FmFaultStateT <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.FmFaultStateT>`
                        
                        	**config**\: False
                        
                        .. attribute:: fault_count
                        
                        	Count of occurrence of the fault event
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: fault_flag
                        
                        	FM correlation engine flag, internal
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'fm'
                        _revision = '2016-04-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Fm.Agents.FmTable.Entry.WaitingList.Entry_, self).__init__()

                            self.yang_name = "entry"
                            self.yang_parent_name = "waiting_list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['fm_subsystem_id','fm_fault_type','fm_fault_tag']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                                ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                                ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                                ('object_id', (YLeaf(YType.str, 'object_id'), ['str'])),
                                ('fault_timestamp', (YLeaf(YType.str, 'fault_timestamp'), ['str'])),
                                ('fault_state', (YLeaf(YType.enumeration, 'fault_state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm', 'FmFaultStateT', '')])),
                                ('fault_count', (YLeaf(YType.uint64, 'fault_count'), ['int'])),
                                ('fault_flag', (YLeaf(YType.uint64, 'fault_flag'), ['int'])),
                            ])
                            self.fm_subsystem_id = None
                            self.fm_fault_type = None
                            self.fm_fault_tag = None
                            self.object_id = None
                            self.fault_timestamp = None
                            self.fault_state = None
                            self.fault_count = None
                            self.fault_flag = None
                            self._segment_path = lambda: "entry" + "[fm_subsystem_id='" + str(self.fm_subsystem_id) + "']" + "[fm_fault_type='" + str(self.fm_fault_type) + "']" + "[fm_fault_tag='" + str(self.fm_fault_tag) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Fm.Agents.FmTable.Entry.WaitingList.Entry_, ['fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag', 'object_id', 'fault_timestamp', 'fault_state', 'fault_count', 'fault_flag'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                            return meta._meta_table['Fm.Agents.FmTable.Entry.WaitingList.Entry_']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                        return meta._meta_table['Fm.Agents.FmTable.Entry.WaitingList']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                    return meta._meta_table['Fm.Agents.FmTable.Entry']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                return meta._meta_table['Fm.Agents.FmTable']['meta_info']


        class FmInternals(_Entity_):
            """
            
            
            .. attribute:: detail
            
            	
            	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmInternals.Detail>`
            
            	**config**\: False
            
            

            """

            _prefix = 'fm'
            _revision = '2016-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Fm.Agents.FmInternals, self).__init__()

                self.yang_name = "fm_internals"
                self.yang_parent_name = "agents"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("detail", ("detail", Fm.Agents.FmInternals.Detail))])
                self._leafs = OrderedDict()

                self.detail = YList(self)
                self._segment_path = lambda: "fm_internals"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Fm.Agents.FmInternals, [], name, value)


            class Detail(_Entity_):
                """
                
                
                .. attribute:: fm_subsystem_id  (key)
                
                	Fault sub\-system identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: fm_fault_type  (key)
                
                	Fault type identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: fm_fault_tag  (key)
                
                	Fault tag identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: rules
                
                	list of fault rule declaring callbacks
                	**type**\: list of  		 :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmInternals.Detail.Rules>`
                
                	**config**\: False
                
                .. attribute:: common_action
                
                	Common action data
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: opaque_action
                
                	opaque action data
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: mitigation_cb
                
                	Pointer to the mitigation callback function
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: recovery_cb
                
                	Pointer to the recovery callback function
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: alarm_severity_dirty
                
                	Flag indicates if alarm severity is dirty
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: disable_action
                
                	Flag indicates all actions are disabled
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: repeat_action
                
                	Flag indicates all actions are repeated
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: has_causal_list
                
                	Flag indicates if causal list is present
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: parser_tag
                
                	The parser tag of the XML parser
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: parser_tag_string
                
                	The parser tag string
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'fm'
                _revision = '2016-04-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Fm.Agents.FmInternals.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "fm_internals"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['fm_subsystem_id','fm_fault_type','fm_fault_tag']
                    self._child_classes = OrderedDict([("rules", ("rules", Fm.Agents.FmInternals.Detail.Rules))])
                    self._leafs = OrderedDict([
                        ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                        ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                        ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                        ('common_action', (YLeaf(YType.uint16, 'common_action'), ['int'])),
                        ('opaque_action', (YLeaf(YType.uint16, 'opaque_action'), ['int'])),
                        ('mitigation_cb', (YLeaf(YType.uint64, 'mitigation_cb'), ['int'])),
                        ('recovery_cb', (YLeaf(YType.uint64, 'recovery_cb'), ['int'])),
                        ('alarm_severity_dirty', (YLeaf(YType.boolean, 'alarm_severity_dirty'), ['bool'])),
                        ('disable_action', (YLeaf(YType.boolean, 'disable_action'), ['bool'])),
                        ('repeat_action', (YLeaf(YType.boolean, 'repeat_action'), ['bool'])),
                        ('has_causal_list', (YLeaf(YType.boolean, 'has_causal_list'), ['bool'])),
                        ('parser_tag', (YLeaf(YType.uint64, 'parser_tag'), ['int'])),
                        ('parser_tag_string', (YLeaf(YType.str, 'parser_tag_string'), ['str'])),
                    ])
                    self.fm_subsystem_id = None
                    self.fm_fault_type = None
                    self.fm_fault_tag = None
                    self.common_action = None
                    self.opaque_action = None
                    self.mitigation_cb = None
                    self.recovery_cb = None
                    self.alarm_severity_dirty = None
                    self.disable_action = None
                    self.repeat_action = None
                    self.has_causal_list = None
                    self.parser_tag = None
                    self.parser_tag_string = None

                    self.rules = YList(self)
                    self._segment_path = lambda: "detail" + "[fm_subsystem_id='" + str(self.fm_subsystem_id) + "']" + "[fm_fault_type='" + str(self.fm_fault_type) + "']" + "[fm_fault_tag='" + str(self.fm_fault_tag) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Fm.Agents.FmInternals.Detail, ['fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag', 'common_action', 'opaque_action', 'mitigation_cb', 'recovery_cb', 'alarm_severity_dirty', 'disable_action', 'repeat_action', 'has_causal_list', 'parser_tag', 'parser_tag_string'], name, value)


                class Rules(_Entity_):
                    """
                    list of fault rule declaring callbacks
                    
                    .. attribute:: fault_location
                    
                    	The location associated with the fault
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: rule_cb
                    
                    	The callback function that declares the fault
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fm'
                    _revision = '2016-04-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Fm.Agents.FmInternals.Detail.Rules, self).__init__()

                        self.yang_name = "rules"
                        self.yang_parent_name = "detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('fault_location', (YLeaf(YType.str, 'fault_location'), ['str'])),
                            ('rule_cb', (YLeaf(YType.uint64, 'rule_cb'), ['int'])),
                        ])
                        self.fault_location = None
                        self.rule_cb = None
                        self._segment_path = lambda: "rules"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fm.Agents.FmInternals.Detail.Rules, ['fault_location', 'rule_cb'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                        return meta._meta_table['Fm.Agents.FmInternals.Detail.Rules']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                    return meta._meta_table['Fm.Agents.FmInternals.Detail']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                return meta._meta_table['Fm.Agents.FmInternals']['meta_info']


        class FmAlarmMapping(_Entity_):
            """
            
            
            .. attribute:: detail
            
            	
            	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmAlarmMapping.Detail>`
            
            	**config**\: False
            
            

            """

            _prefix = 'fm'
            _revision = '2016-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Fm.Agents.FmAlarmMapping, self).__init__()

                self.yang_name = "fm_alarm_mapping"
                self.yang_parent_name = "agents"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("detail", ("detail", Fm.Agents.FmAlarmMapping.Detail))])
                self._leafs = OrderedDict()

                self.detail = YList(self)
                self._segment_path = lambda: "fm_alarm_mapping"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Fm.Agents.FmAlarmMapping, [], name, value)


            class Detail(_Entity_):
                """
                
                
                .. attribute:: fm_subsystem_id  (key)
                
                	Fault sub\-system identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: fm_fault_type  (key)
                
                	Fault type identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: fm_fault_tag  (key)
                
                	Fault tag identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: alarm_group
                
                	The alarm grouping for this fault
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: alarm_severity
                
                	The alarm severity for this fault
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                

                """

                _prefix = 'fm'
                _revision = '2016-04-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Fm.Agents.FmAlarmMapping.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "fm_alarm_mapping"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['fm_subsystem_id','fm_fault_type','fm_fault_tag']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                        ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                        ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                        ('alarm_group', (YLeaf(YType.uint16, 'alarm_group'), ['int'])),
                        ('alarm_severity', (YLeaf(YType.uint16, 'alarm_severity'), ['int'])),
                    ])
                    self.fm_subsystem_id = None
                    self.fm_fault_type = None
                    self.fm_fault_tag = None
                    self.alarm_group = None
                    self.alarm_severity = None
                    self._segment_path = lambda: "detail" + "[fm_subsystem_id='" + str(self.fm_subsystem_id) + "']" + "[fm_fault_type='" + str(self.fm_fault_type) + "']" + "[fm_fault_tag='" + str(self.fm_fault_tag) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Fm.Agents.FmAlarmMapping.Detail, ['fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag', 'alarm_group', 'alarm_severity'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                    return meta._meta_table['Fm.Agents.FmAlarmMapping.Detail']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                return meta._meta_table['Fm.Agents.FmAlarmMapping']['meta_info']


        class FmStatistics(_Entity_):
            """
            
            
            .. attribute:: detail
            
            	
            	**type**\: list of  		 :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fm.Fm.Agents.FmStatistics.Detail>`
            
            	**config**\: False
            
            

            """

            _prefix = 'fm'
            _revision = '2016-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Fm.Agents.FmStatistics, self).__init__()

                self.yang_name = "fm_statistics"
                self.yang_parent_name = "agents"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("detail", ("detail", Fm.Agents.FmStatistics.Detail))])
                self._leafs = OrderedDict()

                self.detail = YList(self)
                self._segment_path = lambda: "fm_statistics"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Fm.Agents.FmStatistics, [], name, value)


            class Detail(_Entity_):
                """
                
                
                .. attribute:: fm_subsystem_id  (key)
                
                	Fault sub\-system identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: fm_fault_type  (key)
                
                	Fault type identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: fm_fault_tag  (key)
                
                	Fault tag identifier
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: threshold_count
                
                	Threshold count for the fault
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: all_object_occur_count
                
                	Object occurrence count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: declared_count
                
                	Number of times the fault is declared
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: cleared_count
                
                	Number of times the fault is cleared
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: info_count
                
                	Number of times the fault is info
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: hold_time
                
                	The hold time in ms for soaking the fault
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'fm'
                _revision = '2016-04-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Fm.Agents.FmStatistics.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "fm_statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['fm_subsystem_id','fm_fault_type','fm_fault_tag']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('fm_subsystem_id', (YLeaf(YType.str, 'fm_subsystem_id'), ['str'])),
                        ('fm_fault_type', (YLeaf(YType.str, 'fm_fault_type'), ['str'])),
                        ('fm_fault_tag', (YLeaf(YType.str, 'fm_fault_tag'), ['str'])),
                        ('threshold_count', (YLeaf(YType.uint32, 'threshold_count'), ['int'])),
                        ('all_object_occur_count', (YLeaf(YType.uint32, 'all_object_occur_count'), ['int'])),
                        ('declared_count', (YLeaf(YType.uint32, 'declared_count'), ['int'])),
                        ('cleared_count', (YLeaf(YType.uint32, 'cleared_count'), ['int'])),
                        ('info_count', (YLeaf(YType.uint32, 'info_count'), ['int'])),
                        ('hold_time', (YLeaf(YType.uint32, 'hold_time'), ['int'])),
                    ])
                    self.fm_subsystem_id = None
                    self.fm_fault_type = None
                    self.fm_fault_tag = None
                    self.threshold_count = None
                    self.all_object_occur_count = None
                    self.declared_count = None
                    self.cleared_count = None
                    self.info_count = None
                    self.hold_time = None
                    self._segment_path = lambda: "detail" + "[fm_subsystem_id='" + str(self.fm_subsystem_id) + "']" + "[fm_fault_type='" + str(self.fm_fault_type) + "']" + "[fm_fault_tag='" + str(self.fm_fault_tag) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Fm.Agents.FmStatistics.Detail, ['fm_subsystem_id', 'fm_fault_type', 'fm_fault_tag', 'threshold_count', 'all_object_occur_count', 'declared_count', 'cleared_count', 'info_count', 'hold_time'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                    return meta._meta_table['Fm.Agents.FmStatistics.Detail']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
                return meta._meta_table['Fm.Agents.FmStatistics']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
            return meta._meta_table['Fm.Agents']['meta_info']

    def clone_ptr(self):
        self._top_entity = Fm()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fm as meta
        return meta._meta_table['Fm']['meta_info']


