""" Cisco_IOS_XR_infra_correlator_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-correlator package operational data.

This module contains definitions
for the following management objects\:
  suppression\: Suppression operational data
  correlator\: correlator

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AcRuleState(Enum):
    """
    AcRuleState

    Ac rule state

    .. data:: rule_unapplied = 0

    	Rule is in Unapplied state

    .. data:: rule_applied = 1

    	Rule is Applied to specified RacksSlots,

    	Contexts and Sources

    .. data:: rule_applied_all = 2

    	Rule is Applied to all of router

    """

    rule_unapplied = Enum.YLeaf(0, "rule-unapplied")

    rule_applied = Enum.YLeaf(1, "rule-applied")

    rule_applied_all = Enum.YLeaf(2, "rule-applied-all")


class AlAlarmBistate(Enum):
    """
    AlAlarmBistate

    Al alarm bistate

    .. data:: not_available = 0

    	not available

    .. data:: active = 1

    	active

    .. data:: clear = 2

    	clear

    """

    not_available = Enum.YLeaf(0, "not-available")

    active = Enum.YLeaf(1, "active")

    clear = Enum.YLeaf(2, "clear")


class AlAlarmSeverity(Enum):
    """
    AlAlarmSeverity

    Al alarm severity

    .. data:: unknown = -1

    	unknown

    .. data:: emergency = 0

    	emergency

    .. data:: alert = 1

    	alert

    .. data:: critical = 2

    	critical

    .. data:: error = 3

    	error

    .. data:: warning = 4

    	warning

    .. data:: notice = 5

    	notice

    .. data:: informational = 6

    	informational

    .. data:: debugging = 7

    	debugging

    """

    unknown = Enum.YLeaf(-1, "unknown")

    emergency = Enum.YLeaf(0, "emergency")

    alert = Enum.YLeaf(1, "alert")

    critical = Enum.YLeaf(2, "critical")

    error = Enum.YLeaf(3, "error")

    warning = Enum.YLeaf(4, "warning")

    notice = Enum.YLeaf(5, "notice")

    informational = Enum.YLeaf(6, "informational")

    debugging = Enum.YLeaf(7, "debugging")



class Correlator(Entity):
    """
    correlator
    
    .. attribute:: alarms
    
    	Correlated alarms Table
    	**type**\:   :py:class:`Alarms <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Alarms>`
    
    .. attribute:: buffer_status
    
    	Describes buffer utilization and parameters configured
    	**type**\:   :py:class:`BufferStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.BufferStatus>`
    
    .. attribute:: rule_details
    
    	Table that contains the database of correlation rule details
    	**type**\:   :py:class:`RuleDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleDetails>`
    
    .. attribute:: rule_set_details
    
    	Table that contains the ruleset detail info
    	**type**\:   :py:class:`RuleSetDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSetDetails>`
    
    .. attribute:: rule_set_summaries
    
    	Table that contains the ruleset summary info
    	**type**\:   :py:class:`RuleSetSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSetSummaries>`
    
    .. attribute:: rule_summaries
    
    	Table that contains the database of correlation rule summary
    	**type**\:   :py:class:`RuleSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSummaries>`
    
    .. attribute:: rules
    
    	Table that contains the database of correlation rules
    	**type**\:   :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Rules>`
    
    

    """

    _prefix = 'infra-correlator-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Correlator, self).__init__()
        self._top_entity = None

        self.yang_name = "correlator"
        self.yang_parent_name = "Cisco-IOS-XR-infra-correlator-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"alarms" : ("alarms", Correlator.Alarms), "buffer-status" : ("buffer_status", Correlator.BufferStatus), "rule-details" : ("rule_details", Correlator.RuleDetails), "rule-set-details" : ("rule_set_details", Correlator.RuleSetDetails), "rule-set-summaries" : ("rule_set_summaries", Correlator.RuleSetSummaries), "rule-summaries" : ("rule_summaries", Correlator.RuleSummaries), "rules" : ("rules", Correlator.Rules)}
        self._child_list_classes = {}

        self.alarms = Correlator.Alarms()
        self.alarms.parent = self
        self._children_name_map["alarms"] = "alarms"
        self._children_yang_names.add("alarms")

        self.buffer_status = Correlator.BufferStatus()
        self.buffer_status.parent = self
        self._children_name_map["buffer_status"] = "buffer-status"
        self._children_yang_names.add("buffer-status")

        self.rule_details = Correlator.RuleDetails()
        self.rule_details.parent = self
        self._children_name_map["rule_details"] = "rule-details"
        self._children_yang_names.add("rule-details")

        self.rule_set_details = Correlator.RuleSetDetails()
        self.rule_set_details.parent = self
        self._children_name_map["rule_set_details"] = "rule-set-details"
        self._children_yang_names.add("rule-set-details")

        self.rule_set_summaries = Correlator.RuleSetSummaries()
        self.rule_set_summaries.parent = self
        self._children_name_map["rule_set_summaries"] = "rule-set-summaries"
        self._children_yang_names.add("rule-set-summaries")

        self.rule_summaries = Correlator.RuleSummaries()
        self.rule_summaries.parent = self
        self._children_name_map["rule_summaries"] = "rule-summaries"
        self._children_yang_names.add("rule-summaries")

        self.rules = Correlator.Rules()
        self.rules.parent = self
        self._children_name_map["rules"] = "rules"
        self._children_yang_names.add("rules")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator"


    class Alarms(Entity):
        """
        Correlated alarms Table
        
        .. attribute:: alarm
        
        	One of the correlated alarms
        	**type**\: list of    :py:class:`Alarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Alarms.Alarm>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Correlator.Alarms, self).__init__()

            self.yang_name = "alarms"
            self.yang_parent_name = "correlator"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"alarm" : ("alarm", Correlator.Alarms.Alarm)}

            self.alarm = YList(self)
            self._segment_path = lambda: "alarms"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Correlator.Alarms, [], name, value)


        class Alarm(Entity):
            """
            One of the correlated alarms
            
            .. attribute:: alarm_id  <key>
            
            	Alarm ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: alarm_info
            
            	Correlated alarm information
            	**type**\:   :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Alarms.Alarm.AlarmInfo>`
            
            .. attribute:: context
            
            	Context string  for the alarm
            	**type**\:  str
            
            .. attribute:: rule_name
            
            	Correlation rule name
            	**type**\:  str
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Correlator.Alarms.Alarm, self).__init__()

                self.yang_name = "alarm"
                self.yang_parent_name = "alarms"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"alarm-info" : ("alarm_info", Correlator.Alarms.Alarm.AlarmInfo)}
                self._child_list_classes = {}

                self.alarm_id = YLeaf(YType.int32, "alarm-id")

                self.context = YLeaf(YType.str, "context")

                self.rule_name = YLeaf(YType.str, "rule-name")

                self.alarm_info = Correlator.Alarms.Alarm.AlarmInfo()
                self.alarm_info.parent = self
                self._children_name_map["alarm_info"] = "alarm-info"
                self._children_yang_names.add("alarm-info")
                self._segment_path = lambda: "alarm" + "[alarm-id='" + self.alarm_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/alarms/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Correlator.Alarms.Alarm, ['alarm_id', 'context', 'rule_name'], name, value)


            class AlarmInfo(Entity):
                """
                Correlated alarm information
                
                .. attribute:: additional_text
                
                	Full text of the Alarm
                	**type**\:  str
                
                .. attribute:: category
                
                	Category of the alarm
                	**type**\:  str
                
                .. attribute:: code
                
                	Alarm code which further qualifies the alarm within a message group
                	**type**\:  str
                
                .. attribute:: correlation_id
                
                	Correlation Identifier
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: group
                
                	Group of messages to which this alarm belongs to
                	**type**\:  str
                
                .. attribute:: is_admin
                
                	Indicates the event id admin\-level
                	**type**\:  bool
                
                .. attribute:: severity
                
                	Severity of the alarm
                	**type**\:   :py:class:`AlAlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AlAlarmSeverity>`
                
                .. attribute:: source_id
                
                	Source Identifier(Location).Indicates the node in which the alarm was generated
                	**type**\:  str
                
                .. attribute:: state
                
                	State of the alarm (bistate alarms only)
                	**type**\:   :py:class:`AlAlarmBistate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AlAlarmBistate>`
                
                .. attribute:: timestamp
                
                	Time when the alarm was generated. It is expressed in number of milliseconds since 00\:00 \:00 UTC, January 1, 1970
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: millisecond
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Correlator.Alarms.Alarm.AlarmInfo, self).__init__()

                    self.yang_name = "alarm-info"
                    self.yang_parent_name = "alarm"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.additional_text = YLeaf(YType.str, "additional-text")

                    self.category = YLeaf(YType.str, "category")

                    self.code = YLeaf(YType.str, "code")

                    self.correlation_id = YLeaf(YType.uint32, "correlation-id")

                    self.group = YLeaf(YType.str, "group")

                    self.is_admin = YLeaf(YType.boolean, "is-admin")

                    self.severity = YLeaf(YType.enumeration, "severity")

                    self.source_id = YLeaf(YType.str, "source-id")

                    self.state = YLeaf(YType.enumeration, "state")

                    self.timestamp = YLeaf(YType.uint64, "timestamp")
                    self._segment_path = lambda: "alarm-info"

                def __setattr__(self, name, value):
                    self._perform_setattr(Correlator.Alarms.Alarm.AlarmInfo, ['additional_text', 'category', 'code', 'correlation_id', 'group', 'is_admin', 'severity', 'source_id', 'state', 'timestamp'], name, value)


    class BufferStatus(Entity):
        """
        Describes buffer utilization and parameters
        configured
        
        .. attribute:: configured_size
        
        	Configured buffer size
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: current_size
        
        	Current buffer usage
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Correlator.BufferStatus, self).__init__()

            self.yang_name = "buffer-status"
            self.yang_parent_name = "correlator"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.configured_size = YLeaf(YType.uint32, "configured-size")

            self.current_size = YLeaf(YType.uint32, "current-size")
            self._segment_path = lambda: "buffer-status"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Correlator.BufferStatus, ['configured_size', 'current_size'], name, value)


    class RuleDetails(Entity):
        """
        Table that contains the database of correlation
        rule details
        
        .. attribute:: rule_detail
        
        	Details of one of the correlation rules
        	**type**\: list of    :py:class:`RuleDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleDetails.RuleDetail>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Correlator.RuleDetails, self).__init__()

            self.yang_name = "rule-details"
            self.yang_parent_name = "correlator"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rule-detail" : ("rule_detail", Correlator.RuleDetails.RuleDetail)}

            self.rule_detail = YList(self)
            self._segment_path = lambda: "rule-details"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Correlator.RuleDetails, [], name, value)


        class RuleDetail(Entity):
            """
            Details of one of the correlation rules
            
            .. attribute:: rule_name  <key>
            
            	Correlation Rule Name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: apply_context
            
            	Contexts (Interfaces) to which the rule is applied
            	**type**\:  list of str
            
            	**length:** 0..33
            
            .. attribute:: apply_location
            
            	Locations (R/S/M) to which the rule is applied
            	**type**\:  list of str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: codes
            
            	Message codes defining the rule
            	**type**\: list of    :py:class:`Codes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleDetails.RuleDetail.Codes>`
            
            .. attribute:: context_correlation
            
            	Whether context correlation is enabled
            	**type**\:  bool
            
            .. attribute:: internal
            
            	True if the rule is internal
            	**type**\:  bool
            
            .. attribute:: reissue_non_bistate
            
            	Whether to reissue non\-bistate alarms
            	**type**\:  bool
            
            .. attribute:: reparent
            
            	Reparent
            	**type**\:  bool
            
            .. attribute:: root_cause_timeout
            
            	Timeout before root cause alarm
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rule_summary
            
            	Rule summary, name, etc
            	**type**\:   :py:class:`RuleSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleDetails.RuleDetail.RuleSummary>`
            
            .. attribute:: timeout
            
            	Time window (in ms) for which root/all messages are kept in correlater before sending them to the logger
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Correlator.RuleDetails.RuleDetail, self).__init__()

                self.yang_name = "rule-detail"
                self.yang_parent_name = "rule-details"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"rule-summary" : ("rule_summary", Correlator.RuleDetails.RuleDetail.RuleSummary)}
                self._child_list_classes = {"codes" : ("codes", Correlator.RuleDetails.RuleDetail.Codes)}

                self.rule_name = YLeaf(YType.str, "rule-name")

                self.apply_context = YLeafList(YType.str, "apply-context")

                self.apply_location = YLeafList(YType.str, "apply-location")

                self.context_correlation = YLeaf(YType.boolean, "context-correlation")

                self.internal = YLeaf(YType.boolean, "internal")

                self.reissue_non_bistate = YLeaf(YType.boolean, "reissue-non-bistate")

                self.reparent = YLeaf(YType.boolean, "reparent")

                self.root_cause_timeout = YLeaf(YType.uint32, "root-cause-timeout")

                self.timeout = YLeaf(YType.uint32, "timeout")

                self.rule_summary = Correlator.RuleDetails.RuleDetail.RuleSummary()
                self.rule_summary.parent = self
                self._children_name_map["rule_summary"] = "rule-summary"
                self._children_yang_names.add("rule-summary")

                self.codes = YList(self)
                self._segment_path = lambda: "rule-detail" + "[rule-name='" + self.rule_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/rule-details/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Correlator.RuleDetails.RuleDetail, ['rule_name', 'apply_context', 'apply_location', 'context_correlation', 'internal', 'reissue_non_bistate', 'reparent', 'root_cause_timeout', 'timeout'], name, value)


            class Codes(Entity):
                """
                Message codes defining the rule.
                
                .. attribute:: category
                
                	Category of messages to which this alarm belongs
                	**type**\:  str
                
                .. attribute:: code
                
                	Alarm code which further qualifies the alarm within a message group
                	**type**\:  str
                
                .. attribute:: group
                
                	Group of messages to which this alarm belongs
                	**type**\:  str
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Correlator.RuleDetails.RuleDetail.Codes, self).__init__()

                    self.yang_name = "codes"
                    self.yang_parent_name = "rule-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.category = YLeaf(YType.str, "category")

                    self.code = YLeaf(YType.str, "code")

                    self.group = YLeaf(YType.str, "group")
                    self._segment_path = lambda: "codes"

                def __setattr__(self, name, value):
                    self._perform_setattr(Correlator.RuleDetails.RuleDetail.Codes, ['category', 'code', 'group'], name, value)


            class RuleSummary(Entity):
                """
                Rule summary, name, etc
                
                .. attribute:: buffered_alarms_count
                
                	Number of buffered alarms correlated to this rule
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rule_name_xr
                
                	Correlation Rule Name
                	**type**\:  str
                
                .. attribute:: rule_state
                
                	Applied state of the rule It could be not applied, applied or applied to all
                	**type**\:   :py:class:`AcRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleState>`
                
                .. attribute:: stateful
                
                	Whether the rule is stateful
                	**type**\:  bool
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Correlator.RuleDetails.RuleDetail.RuleSummary, self).__init__()

                    self.yang_name = "rule-summary"
                    self.yang_parent_name = "rule-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.buffered_alarms_count = YLeaf(YType.uint32, "buffered-alarms-count")

                    self.rule_name_xr = YLeaf(YType.str, "rule-name-xr")

                    self.rule_state = YLeaf(YType.enumeration, "rule-state")

                    self.stateful = YLeaf(YType.boolean, "stateful")
                    self._segment_path = lambda: "rule-summary"

                def __setattr__(self, name, value):
                    self._perform_setattr(Correlator.RuleDetails.RuleDetail.RuleSummary, ['buffered_alarms_count', 'rule_name_xr', 'rule_state', 'stateful'], name, value)


    class RuleSetDetails(Entity):
        """
        Table that contains the ruleset detail info
        
        .. attribute:: rule_set_detail
        
        	Detail of one of the correlation rulesets
        	**type**\: list of    :py:class:`RuleSetDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSetDetails.RuleSetDetail>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Correlator.RuleSetDetails, self).__init__()

            self.yang_name = "rule-set-details"
            self.yang_parent_name = "correlator"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rule-set-detail" : ("rule_set_detail", Correlator.RuleSetDetails.RuleSetDetail)}

            self.rule_set_detail = YList(self)
            self._segment_path = lambda: "rule-set-details"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Correlator.RuleSetDetails, [], name, value)


        class RuleSetDetail(Entity):
            """
            Detail of one of the correlation rulesets
            
            .. attribute:: rule_set_name  <key>
            
            	Ruleset Name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: rule_set_name_xr
            
            	Ruleset Name
            	**type**\:  str
            
            .. attribute:: rules
            
            	Rules contained in a ruleset
            	**type**\: list of    :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSetDetails.RuleSetDetail.Rules>`
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Correlator.RuleSetDetails.RuleSetDetail, self).__init__()

                self.yang_name = "rule-set-detail"
                self.yang_parent_name = "rule-set-details"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"rules" : ("rules", Correlator.RuleSetDetails.RuleSetDetail.Rules)}

                self.rule_set_name = YLeaf(YType.str, "rule-set-name")

                self.rule_set_name_xr = YLeaf(YType.str, "rule-set-name-xr")

                self.rules = YList(self)
                self._segment_path = lambda: "rule-set-detail" + "[rule-set-name='" + self.rule_set_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/rule-set-details/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Correlator.RuleSetDetails.RuleSetDetail, ['rule_set_name', 'rule_set_name_xr'], name, value)


            class Rules(Entity):
                """
                Rules contained in a ruleset
                
                .. attribute:: buffered_alarms_count
                
                	Number of buffered alarms correlated to this rule
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rule_name_xr
                
                	Correlation Rule Name
                	**type**\:  str
                
                .. attribute:: rule_state
                
                	Applied state of the rule It could be not applied, applied or applied to all
                	**type**\:   :py:class:`AcRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleState>`
                
                .. attribute:: stateful
                
                	Whether the rule is stateful
                	**type**\:  bool
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Correlator.RuleSetDetails.RuleSetDetail.Rules, self).__init__()

                    self.yang_name = "rules"
                    self.yang_parent_name = "rule-set-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.buffered_alarms_count = YLeaf(YType.uint32, "buffered-alarms-count")

                    self.rule_name_xr = YLeaf(YType.str, "rule-name-xr")

                    self.rule_state = YLeaf(YType.enumeration, "rule-state")

                    self.stateful = YLeaf(YType.boolean, "stateful")
                    self._segment_path = lambda: "rules"

                def __setattr__(self, name, value):
                    self._perform_setattr(Correlator.RuleSetDetails.RuleSetDetail.Rules, ['buffered_alarms_count', 'rule_name_xr', 'rule_state', 'stateful'], name, value)


    class RuleSetSummaries(Entity):
        """
        Table that contains the ruleset summary info
        
        .. attribute:: rule_set_summary
        
        	Summary of one of the correlation rulesets
        	**type**\: list of    :py:class:`RuleSetSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSetSummaries.RuleSetSummary>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Correlator.RuleSetSummaries, self).__init__()

            self.yang_name = "rule-set-summaries"
            self.yang_parent_name = "correlator"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rule-set-summary" : ("rule_set_summary", Correlator.RuleSetSummaries.RuleSetSummary)}

            self.rule_set_summary = YList(self)
            self._segment_path = lambda: "rule-set-summaries"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Correlator.RuleSetSummaries, [], name, value)


        class RuleSetSummary(Entity):
            """
            Summary of one of the correlation rulesets
            
            .. attribute:: rule_set_name  <key>
            
            	Ruleset Name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: rule_set_name_xr
            
            	Ruleset Name
            	**type**\:  str
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Correlator.RuleSetSummaries.RuleSetSummary, self).__init__()

                self.yang_name = "rule-set-summary"
                self.yang_parent_name = "rule-set-summaries"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.rule_set_name = YLeaf(YType.str, "rule-set-name")

                self.rule_set_name_xr = YLeaf(YType.str, "rule-set-name-xr")
                self._segment_path = lambda: "rule-set-summary" + "[rule-set-name='" + self.rule_set_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/rule-set-summaries/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Correlator.RuleSetSummaries.RuleSetSummary, ['rule_set_name', 'rule_set_name_xr'], name, value)


    class RuleSummaries(Entity):
        """
        Table that contains the database of correlation
        rule summary
        
        .. attribute:: rule_summary
        
        	One of the correlation rules
        	**type**\: list of    :py:class:`RuleSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSummaries.RuleSummary>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Correlator.RuleSummaries, self).__init__()

            self.yang_name = "rule-summaries"
            self.yang_parent_name = "correlator"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rule-summary" : ("rule_summary", Correlator.RuleSummaries.RuleSummary)}

            self.rule_summary = YList(self)
            self._segment_path = lambda: "rule-summaries"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Correlator.RuleSummaries, [], name, value)


        class RuleSummary(Entity):
            """
            One of the correlation rules
            
            .. attribute:: rule_name  <key>
            
            	Correlation Rule Name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: buffered_alarms_count
            
            	Number of buffered alarms correlated to this rule
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rule_name_xr
            
            	Correlation Rule Name
            	**type**\:  str
            
            .. attribute:: rule_state
            
            	Applied state of the rule It could be not applied, applied or applied to all
            	**type**\:   :py:class:`AcRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleState>`
            
            .. attribute:: stateful
            
            	Whether the rule is stateful
            	**type**\:  bool
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Correlator.RuleSummaries.RuleSummary, self).__init__()

                self.yang_name = "rule-summary"
                self.yang_parent_name = "rule-summaries"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.rule_name = YLeaf(YType.str, "rule-name")

                self.buffered_alarms_count = YLeaf(YType.uint32, "buffered-alarms-count")

                self.rule_name_xr = YLeaf(YType.str, "rule-name-xr")

                self.rule_state = YLeaf(YType.enumeration, "rule-state")

                self.stateful = YLeaf(YType.boolean, "stateful")
                self._segment_path = lambda: "rule-summary" + "[rule-name='" + self.rule_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/rule-summaries/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Correlator.RuleSummaries.RuleSummary, ['rule_name', 'buffered_alarms_count', 'rule_name_xr', 'rule_state', 'stateful'], name, value)


    class Rules(Entity):
        """
        Table that contains the database of correlation
        rules
        
        .. attribute:: rule
        
        	One of the correlation rules
        	**type**\: list of    :py:class:`Rule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Rules.Rule>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Correlator.Rules, self).__init__()

            self.yang_name = "rules"
            self.yang_parent_name = "correlator"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rule" : ("rule", Correlator.Rules.Rule)}

            self.rule = YList(self)
            self._segment_path = lambda: "rules"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Correlator.Rules, [], name, value)


        class Rule(Entity):
            """
            One of the correlation rules
            
            .. attribute:: rule_name  <key>
            
            	Correlation Rule Name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: apply_context
            
            	Contexts (Interfaces) to which the rule is applied
            	**type**\:  list of str
            
            	**length:** 0..33
            
            .. attribute:: apply_location
            
            	Locations (R/S/M) to which the rule is  applied
            	**type**\:  list of str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: codes
            
            	Message codes defining the rule
            	**type**\: list of    :py:class:`Codes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Rules.Rule.Codes>`
            
            .. attribute:: rule_name_xr
            
            	Correlation Rule Name
            	**type**\:  str
            
            .. attribute:: rule_state
            
            	Applied state of the rule It could be not applied, applied or applied to all
            	**type**\:   :py:class:`AcRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleState>`
            
            .. attribute:: timeout
            
            	Time window (in ms) for which root/all messages are kept in correlater before sending them to the logger
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Correlator.Rules.Rule, self).__init__()

                self.yang_name = "rule"
                self.yang_parent_name = "rules"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"codes" : ("codes", Correlator.Rules.Rule.Codes)}

                self.rule_name = YLeaf(YType.str, "rule-name")

                self.apply_context = YLeafList(YType.str, "apply-context")

                self.apply_location = YLeafList(YType.str, "apply-location")

                self.rule_name_xr = YLeaf(YType.str, "rule-name-xr")

                self.rule_state = YLeaf(YType.enumeration, "rule-state")

                self.timeout = YLeaf(YType.uint32, "timeout")

                self.codes = YList(self)
                self._segment_path = lambda: "rule" + "[rule-name='" + self.rule_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/rules/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Correlator.Rules.Rule, ['rule_name', 'apply_context', 'apply_location', 'rule_name_xr', 'rule_state', 'timeout'], name, value)


            class Codes(Entity):
                """
                Message codes defining the rule.
                
                .. attribute:: category
                
                	Category of messages to which this alarm belongs
                	**type**\:  str
                
                .. attribute:: code
                
                	Alarm code which further qualifies the alarm within a message group
                	**type**\:  str
                
                .. attribute:: group
                
                	Group of messages to which this alarm belongs
                	**type**\:  str
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Correlator.Rules.Rule.Codes, self).__init__()

                    self.yang_name = "codes"
                    self.yang_parent_name = "rule"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.category = YLeaf(YType.str, "category")

                    self.code = YLeaf(YType.str, "code")

                    self.group = YLeaf(YType.str, "group")
                    self._segment_path = lambda: "codes"

                def __setattr__(self, name, value):
                    self._perform_setattr(Correlator.Rules.Rule.Codes, ['category', 'code', 'group'], name, value)

    def clone_ptr(self):
        self._top_entity = Correlator()
        return self._top_entity

class Suppression(Entity):
    """
    Suppression operational data
    
    .. attribute:: rule_details
    
    	Table that contains the database of suppression rule details
    	**type**\:   :py:class:`RuleDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Suppression.RuleDetails>`
    
    .. attribute:: rule_summaries
    
    	Table that contains the database of suppression rule summary
    	**type**\:   :py:class:`RuleSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Suppression.RuleSummaries>`
    
    

    """

    _prefix = 'infra-correlator-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Suppression, self).__init__()
        self._top_entity = None

        self.yang_name = "suppression"
        self.yang_parent_name = "Cisco-IOS-XR-infra-correlator-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"rule-details" : ("rule_details", Suppression.RuleDetails), "rule-summaries" : ("rule_summaries", Suppression.RuleSummaries)}
        self._child_list_classes = {}

        self.rule_details = Suppression.RuleDetails()
        self.rule_details.parent = self
        self._children_name_map["rule_details"] = "rule-details"
        self._children_yang_names.add("rule-details")

        self.rule_summaries = Suppression.RuleSummaries()
        self.rule_summaries.parent = self
        self._children_name_map["rule_summaries"] = "rule-summaries"
        self._children_yang_names.add("rule-summaries")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:suppression"


    class RuleDetails(Entity):
        """
        Table that contains the database of suppression
        rule details
        
        .. attribute:: rule_detail
        
        	Details of one of the suppression rules
        	**type**\: list of    :py:class:`RuleDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Suppression.RuleDetails.RuleDetail>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Suppression.RuleDetails, self).__init__()

            self.yang_name = "rule-details"
            self.yang_parent_name = "suppression"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rule-detail" : ("rule_detail", Suppression.RuleDetails.RuleDetail)}

            self.rule_detail = YList(self)
            self._segment_path = lambda: "rule-details"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:suppression/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Suppression.RuleDetails, [], name, value)


        class RuleDetail(Entity):
            """
            Details of one of the suppression rules
            
            .. attribute:: rule_name  <key>
            
            	Suppression Rule Name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: alarm_severity
            
            	Severity level to suppress
            	**type**\:   :py:class:`AlAlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AlAlarmSeverity>`
            
            .. attribute:: all_alarms
            
            	Match any alarm
            	**type**\:  bool
            
            .. attribute:: apply_source
            
            	Sources (R/S/M) to which the rule is applied
            	**type**\:  list of str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: codes
            
            	Message codes defining the rule
            	**type**\: list of    :py:class:`Codes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Suppression.RuleDetails.RuleDetail.Codes>`
            
            .. attribute:: rule_summary
            
            	Rule summary, name, etc
            	**type**\:   :py:class:`RuleSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Suppression.RuleDetails.RuleDetail.RuleSummary>`
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Suppression.RuleDetails.RuleDetail, self).__init__()

                self.yang_name = "rule-detail"
                self.yang_parent_name = "rule-details"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"rule-summary" : ("rule_summary", Suppression.RuleDetails.RuleDetail.RuleSummary)}
                self._child_list_classes = {"codes" : ("codes", Suppression.RuleDetails.RuleDetail.Codes)}

                self.rule_name = YLeaf(YType.str, "rule-name")

                self.alarm_severity = YLeaf(YType.enumeration, "alarm-severity")

                self.all_alarms = YLeaf(YType.boolean, "all-alarms")

                self.apply_source = YLeafList(YType.str, "apply-source")

                self.rule_summary = Suppression.RuleDetails.RuleDetail.RuleSummary()
                self.rule_summary.parent = self
                self._children_name_map["rule_summary"] = "rule-summary"
                self._children_yang_names.add("rule-summary")

                self.codes = YList(self)
                self._segment_path = lambda: "rule-detail" + "[rule-name='" + self.rule_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:suppression/rule-details/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Suppression.RuleDetails.RuleDetail, ['rule_name', 'alarm_severity', 'all_alarms', 'apply_source'], name, value)


            class Codes(Entity):
                """
                Message codes defining the rule.
                
                .. attribute:: category
                
                	Category of messages to which this alarm belongs
                	**type**\:  str
                
                .. attribute:: code
                
                	Alarm code which further qualifies the alarm within a message group
                	**type**\:  str
                
                .. attribute:: group
                
                	Group of messages to which this alarm belongs
                	**type**\:  str
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Suppression.RuleDetails.RuleDetail.Codes, self).__init__()

                    self.yang_name = "codes"
                    self.yang_parent_name = "rule-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.category = YLeaf(YType.str, "category")

                    self.code = YLeaf(YType.str, "code")

                    self.group = YLeaf(YType.str, "group")
                    self._segment_path = lambda: "codes"

                def __setattr__(self, name, value):
                    self._perform_setattr(Suppression.RuleDetails.RuleDetail.Codes, ['category', 'code', 'group'], name, value)


            class RuleSummary(Entity):
                """
                Rule summary, name, etc
                
                .. attribute:: rule_name_xr
                
                	Suppress Rule Name
                	**type**\:  str
                
                .. attribute:: rule_state
                
                	Applied state of the rule It could be not applied, applied or applied to all
                	**type**\:   :py:class:`AcRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleState>`
                
                .. attribute:: suppressed_alarms_count
                
                	Number of suppressed alarms associated with this rule
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Suppression.RuleDetails.RuleDetail.RuleSummary, self).__init__()

                    self.yang_name = "rule-summary"
                    self.yang_parent_name = "rule-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.rule_name_xr = YLeaf(YType.str, "rule-name-xr")

                    self.rule_state = YLeaf(YType.enumeration, "rule-state")

                    self.suppressed_alarms_count = YLeaf(YType.uint32, "suppressed-alarms-count")
                    self._segment_path = lambda: "rule-summary"

                def __setattr__(self, name, value):
                    self._perform_setattr(Suppression.RuleDetails.RuleDetail.RuleSummary, ['rule_name_xr', 'rule_state', 'suppressed_alarms_count'], name, value)


    class RuleSummaries(Entity):
        """
        Table that contains the database of suppression
        rule summary
        
        .. attribute:: rule_summary
        
        	One of the suppression rules
        	**type**\: list of    :py:class:`RuleSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Suppression.RuleSummaries.RuleSummary>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Suppression.RuleSummaries, self).__init__()

            self.yang_name = "rule-summaries"
            self.yang_parent_name = "suppression"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rule-summary" : ("rule_summary", Suppression.RuleSummaries.RuleSummary)}

            self.rule_summary = YList(self)
            self._segment_path = lambda: "rule-summaries"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:suppression/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Suppression.RuleSummaries, [], name, value)


        class RuleSummary(Entity):
            """
            One of the suppression rules
            
            .. attribute:: rule_name  <key>
            
            	Suppression Rule Name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: rule_name_xr
            
            	Suppress Rule Name
            	**type**\:  str
            
            .. attribute:: rule_state
            
            	Applied state of the rule It could be not applied, applied or applied to all
            	**type**\:   :py:class:`AcRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleState>`
            
            .. attribute:: suppressed_alarms_count
            
            	Number of suppressed alarms associated with this rule
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Suppression.RuleSummaries.RuleSummary, self).__init__()

                self.yang_name = "rule-summary"
                self.yang_parent_name = "rule-summaries"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.rule_name = YLeaf(YType.str, "rule-name")

                self.rule_name_xr = YLeaf(YType.str, "rule-name-xr")

                self.rule_state = YLeaf(YType.enumeration, "rule-state")

                self.suppressed_alarms_count = YLeaf(YType.uint32, "suppressed-alarms-count")
                self._segment_path = lambda: "rule-summary" + "[rule-name='" + self.rule_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:suppression/rule-summaries/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Suppression.RuleSummaries.RuleSummary, ['rule_name', 'rule_name_xr', 'rule_state', 'suppressed_alarms_count'], name, value)

    def clone_ptr(self):
        self._top_entity = Suppression()
        return self._top_entity

