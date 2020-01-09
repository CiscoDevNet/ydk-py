""" Cisco_IOS_XR_infra_correlator_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-correlator package operational data.

This module contains definitions
for the following management objects\:
  suppression\: Suppression operational data
  correlator\: correlator

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
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



class AcRuleState(Enum):
    """
    AcRuleState (Enum Class)

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
        return meta._meta_table['AcRuleState']


class AlAlarmBistate(Enum):
    """
    AlAlarmBistate (Enum Class)

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
        return meta._meta_table['AlAlarmBistate']


class AlAlarmSeverity(Enum):
    """
    AlAlarmSeverity (Enum Class)

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
        return meta._meta_table['AlAlarmSeverity']



class Suppression(_Entity_):
    """
    Suppression operational data
    
    .. attribute:: rule_summaries
    
    	Table that contains the database of suppression rule summary
    	**type**\:  :py:class:`RuleSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Suppression.RuleSummaries>`
    
    	**config**\: False
    
    .. attribute:: rule_details
    
    	Table that contains the database of suppression rule details
    	**type**\:  :py:class:`RuleDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Suppression.RuleDetails>`
    
    	**config**\: False
    
    

    """

    _prefix = 'infra-correlator-oper'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Suppression, self).__init__()
        self._top_entity = None

        self.yang_name = "suppression"
        self.yang_parent_name = "Cisco-IOS-XR-infra-correlator-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("rule-summaries", ("rule_summaries", Suppression.RuleSummaries)), ("rule-details", ("rule_details", Suppression.RuleDetails))])
        self._leafs = OrderedDict()

        self.rule_summaries = Suppression.RuleSummaries()
        self.rule_summaries.parent = self
        self._children_name_map["rule_summaries"] = "rule-summaries"

        self.rule_details = Suppression.RuleDetails()
        self.rule_details.parent = self
        self._children_name_map["rule_details"] = "rule-details"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:suppression"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Suppression, [], name, value)


    class RuleSummaries(_Entity_):
        """
        Table that contains the database of suppression
        rule summary
        
        .. attribute:: rule_summary
        
        	One of the suppression rules
        	**type**\: list of  		 :py:class:`RuleSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Suppression.RuleSummaries.RuleSummary>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Suppression.RuleSummaries, self).__init__()

            self.yang_name = "rule-summaries"
            self.yang_parent_name = "suppression"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rule-summary", ("rule_summary", Suppression.RuleSummaries.RuleSummary))])
            self._leafs = OrderedDict()

            self.rule_summary = YList(self)
            self._segment_path = lambda: "rule-summaries"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:suppression/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Suppression.RuleSummaries, [], name, value)


        class RuleSummary(_Entity_):
            """
            One of the suppression rules
            
            .. attribute:: rule_name  (key)
            
            	Suppression Rule Name
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: rule_name_xr
            
            	Suppress Rule Name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rule_state
            
            	Applied state of the rule It could be not applied, applied or applied to all
            	**type**\:  :py:class:`AcRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleState>`
            
            	**config**\: False
            
            .. attribute:: suppressed_alarms_count
            
            	Number of suppressed alarms associated with this rule
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Suppression.RuleSummaries.RuleSummary, self).__init__()

                self.yang_name = "rule-summary"
                self.yang_parent_name = "rule-summaries"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rule_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rule_name', (YLeaf(YType.str, 'rule-name'), ['str'])),
                    ('rule_name_xr', (YLeaf(YType.str, 'rule-name-xr'), ['str'])),
                    ('rule_state', (YLeaf(YType.enumeration, 'rule-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AcRuleState', '')])),
                    ('suppressed_alarms_count', (YLeaf(YType.uint32, 'suppressed-alarms-count'), ['int'])),
                ])
                self.rule_name = None
                self.rule_name_xr = None
                self.rule_state = None
                self.suppressed_alarms_count = None
                self._segment_path = lambda: "rule-summary" + "[rule-name='" + str(self.rule_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:suppression/rule-summaries/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Suppression.RuleSummaries.RuleSummary, ['rule_name', 'rule_name_xr', 'rule_state', 'suppressed_alarms_count'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Suppression.RuleSummaries.RuleSummary']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Suppression.RuleSummaries']['meta_info']


    class RuleDetails(_Entity_):
        """
        Table that contains the database of suppression
        rule details
        
        .. attribute:: rule_detail
        
        	Details of one of the suppression rules
        	**type**\: list of  		 :py:class:`RuleDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Suppression.RuleDetails.RuleDetail>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Suppression.RuleDetails, self).__init__()

            self.yang_name = "rule-details"
            self.yang_parent_name = "suppression"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rule-detail", ("rule_detail", Suppression.RuleDetails.RuleDetail))])
            self._leafs = OrderedDict()

            self.rule_detail = YList(self)
            self._segment_path = lambda: "rule-details"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:suppression/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Suppression.RuleDetails, [], name, value)


        class RuleDetail(_Entity_):
            """
            Details of one of the suppression rules
            
            .. attribute:: rule_name  (key)
            
            	Suppression Rule Name
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: rule_summary
            
            	Rule summary, name, etc
            	**type**\:  :py:class:`RuleSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Suppression.RuleDetails.RuleDetail.RuleSummary>`
            
            	**config**\: False
            
            .. attribute:: all_alarms
            
            	Match any alarm
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: alarm_severity
            
            	Severity level to suppress
            	**type**\:  :py:class:`AlAlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AlAlarmSeverity>`
            
            	**config**\: False
            
            .. attribute:: apply_source
            
            	Sources (R/S/M) to which the rule is applied
            	**type**\: list of str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: codes
            
            	Message codes defining the rule
            	**type**\: list of  		 :py:class:`Codes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Suppression.RuleDetails.RuleDetail.Codes>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Suppression.RuleDetails.RuleDetail, self).__init__()

                self.yang_name = "rule-detail"
                self.yang_parent_name = "rule-details"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rule_name']
                self._child_classes = OrderedDict([("rule-summary", ("rule_summary", Suppression.RuleDetails.RuleDetail.RuleSummary)), ("codes", ("codes", Suppression.RuleDetails.RuleDetail.Codes))])
                self._leafs = OrderedDict([
                    ('rule_name', (YLeaf(YType.str, 'rule-name'), ['str'])),
                    ('all_alarms', (YLeaf(YType.boolean, 'all-alarms'), ['bool'])),
                    ('alarm_severity', (YLeaf(YType.enumeration, 'alarm-severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AlAlarmSeverity', '')])),
                    ('apply_source', (YLeafList(YType.str, 'apply-source'), ['str'])),
                ])
                self.rule_name = None
                self.all_alarms = None
                self.alarm_severity = None
                self.apply_source = []

                self.rule_summary = Suppression.RuleDetails.RuleDetail.RuleSummary()
                self.rule_summary.parent = self
                self._children_name_map["rule_summary"] = "rule-summary"

                self.codes = YList(self)
                self._segment_path = lambda: "rule-detail" + "[rule-name='" + str(self.rule_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:suppression/rule-details/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Suppression.RuleDetails.RuleDetail, ['rule_name', 'all_alarms', 'alarm_severity', 'apply_source'], name, value)


            class RuleSummary(_Entity_):
                """
                Rule summary, name, etc
                
                .. attribute:: rule_name_xr
                
                	Suppress Rule Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: rule_state
                
                	Applied state of the rule It could be not applied, applied or applied to all
                	**type**\:  :py:class:`AcRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleState>`
                
                	**config**\: False
                
                .. attribute:: suppressed_alarms_count
                
                	Number of suppressed alarms associated with this rule
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Suppression.RuleDetails.RuleDetail.RuleSummary, self).__init__()

                    self.yang_name = "rule-summary"
                    self.yang_parent_name = "rule-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rule_name_xr', (YLeaf(YType.str, 'rule-name-xr'), ['str'])),
                        ('rule_state', (YLeaf(YType.enumeration, 'rule-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AcRuleState', '')])),
                        ('suppressed_alarms_count', (YLeaf(YType.uint32, 'suppressed-alarms-count'), ['int'])),
                    ])
                    self.rule_name_xr = None
                    self.rule_state = None
                    self.suppressed_alarms_count = None
                    self._segment_path = lambda: "rule-summary"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Suppression.RuleDetails.RuleDetail.RuleSummary, ['rule_name_xr', 'rule_state', 'suppressed_alarms_count'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                    return meta._meta_table['Suppression.RuleDetails.RuleDetail.RuleSummary']['meta_info']


            class Codes(_Entity_):
                """
                Message codes defining the rule.
                
                .. attribute:: category
                
                	Category of messages to which this alarm belongs
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: group
                
                	Group of messages to which this alarm belongs
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: code
                
                	Alarm code which further qualifies the alarm within a message group
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Suppression.RuleDetails.RuleDetail.Codes, self).__init__()

                    self.yang_name = "codes"
                    self.yang_parent_name = "rule-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('category', (YLeaf(YType.str, 'category'), ['str'])),
                        ('group', (YLeaf(YType.str, 'group'), ['str'])),
                        ('code', (YLeaf(YType.str, 'code'), ['str'])),
                    ])
                    self.category = None
                    self.group = None
                    self.code = None
                    self._segment_path = lambda: "codes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Suppression.RuleDetails.RuleDetail.Codes, ['category', 'group', 'code'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                    return meta._meta_table['Suppression.RuleDetails.RuleDetail.Codes']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Suppression.RuleDetails.RuleDetail']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Suppression.RuleDetails']['meta_info']

    def clone_ptr(self):
        self._top_entity = Suppression()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
        return meta._meta_table['Suppression']['meta_info']


class Correlator(_Entity_):
    """
    correlator
    
    .. attribute:: rules
    
    	Table that contains the database of correlation rules
    	**type**\:  :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Rules>`
    
    	**config**\: False
    
    .. attribute:: buffer_status
    
    	Describes buffer utilization and parameters configured
    	**type**\:  :py:class:`BufferStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.BufferStatus>`
    
    	**config**\: False
    
    .. attribute:: alarms
    
    	Correlated alarms Table
    	**type**\:  :py:class:`Alarms <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Alarms>`
    
    	**config**\: False
    
    .. attribute:: rule_set_summaries
    
    	Table that contains the ruleset summary info
    	**type**\:  :py:class:`RuleSetSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSetSummaries>`
    
    	**config**\: False
    
    .. attribute:: rule_set_details
    
    	Table that contains the ruleset detail info
    	**type**\:  :py:class:`RuleSetDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSetDetails>`
    
    	**config**\: False
    
    .. attribute:: rule_details
    
    	Table that contains the database of correlation rule details
    	**type**\:  :py:class:`RuleDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleDetails>`
    
    	**config**\: False
    
    .. attribute:: rule_summaries
    
    	Table that contains the database of correlation rule summary
    	**type**\:  :py:class:`RuleSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSummaries>`
    
    	**config**\: False
    
    

    """

    _prefix = 'infra-correlator-oper'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Correlator, self).__init__()
        self._top_entity = None

        self.yang_name = "correlator"
        self.yang_parent_name = "Cisco-IOS-XR-infra-correlator-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("rules", ("rules", Correlator.Rules)), ("buffer-status", ("buffer_status", Correlator.BufferStatus)), ("alarms", ("alarms", Correlator.Alarms)), ("rule-set-summaries", ("rule_set_summaries", Correlator.RuleSetSummaries)), ("rule-set-details", ("rule_set_details", Correlator.RuleSetDetails)), ("rule-details", ("rule_details", Correlator.RuleDetails)), ("rule-summaries", ("rule_summaries", Correlator.RuleSummaries))])
        self._leafs = OrderedDict()

        self.rules = Correlator.Rules()
        self.rules.parent = self
        self._children_name_map["rules"] = "rules"

        self.buffer_status = Correlator.BufferStatus()
        self.buffer_status.parent = self
        self._children_name_map["buffer_status"] = "buffer-status"

        self.alarms = Correlator.Alarms()
        self.alarms.parent = self
        self._children_name_map["alarms"] = "alarms"

        self.rule_set_summaries = Correlator.RuleSetSummaries()
        self.rule_set_summaries.parent = self
        self._children_name_map["rule_set_summaries"] = "rule-set-summaries"

        self.rule_set_details = Correlator.RuleSetDetails()
        self.rule_set_details.parent = self
        self._children_name_map["rule_set_details"] = "rule-set-details"

        self.rule_details = Correlator.RuleDetails()
        self.rule_details.parent = self
        self._children_name_map["rule_details"] = "rule-details"

        self.rule_summaries = Correlator.RuleSummaries()
        self.rule_summaries.parent = self
        self._children_name_map["rule_summaries"] = "rule-summaries"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Correlator, [], name, value)


    class Rules(_Entity_):
        """
        Table that contains the database of correlation
        rules
        
        .. attribute:: rule
        
        	One of the correlation rules
        	**type**\: list of  		 :py:class:`Rule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Rules.Rule>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Correlator.Rules, self).__init__()

            self.yang_name = "rules"
            self.yang_parent_name = "correlator"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rule", ("rule", Correlator.Rules.Rule))])
            self._leafs = OrderedDict()

            self.rule = YList(self)
            self._segment_path = lambda: "rules"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Correlator.Rules, [], name, value)


        class Rule(_Entity_):
            """
            One of the correlation rules
            
            .. attribute:: rule_name  (key)
            
            	Correlation Rule Name
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: rule_name_xr
            
            	Correlation Rule Name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: timeout
            
            	Time window (in ms) for which root/all messages are kept in correlater before sending them to the logger
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rule_state
            
            	Applied state of the rule It could be not applied, applied or applied to all
            	**type**\:  :py:class:`AcRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleState>`
            
            	**config**\: False
            
            .. attribute:: apply_location
            
            	Locations (R/S/M) to which the rule is  applied
            	**type**\: list of str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: apply_context
            
            	Contexts (Interfaces) to which the rule is applied
            	**type**\: list of str
            
            	**length:** 0..33
            
            	**config**\: False
            
            .. attribute:: codes
            
            	Message codes defining the rule
            	**type**\: list of  		 :py:class:`Codes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Rules.Rule.Codes>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Correlator.Rules.Rule, self).__init__()

                self.yang_name = "rule"
                self.yang_parent_name = "rules"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rule_name']
                self._child_classes = OrderedDict([("codes", ("codes", Correlator.Rules.Rule.Codes))])
                self._leafs = OrderedDict([
                    ('rule_name', (YLeaf(YType.str, 'rule-name'), ['str'])),
                    ('rule_name_xr', (YLeaf(YType.str, 'rule-name-xr'), ['str'])),
                    ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                    ('rule_state', (YLeaf(YType.enumeration, 'rule-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AcRuleState', '')])),
                    ('apply_location', (YLeafList(YType.str, 'apply-location'), ['str'])),
                    ('apply_context', (YLeafList(YType.str, 'apply-context'), ['str'])),
                ])
                self.rule_name = None
                self.rule_name_xr = None
                self.timeout = None
                self.rule_state = None
                self.apply_location = []
                self.apply_context = []

                self.codes = YList(self)
                self._segment_path = lambda: "rule" + "[rule-name='" + str(self.rule_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/rules/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Correlator.Rules.Rule, ['rule_name', 'rule_name_xr', 'timeout', 'rule_state', 'apply_location', 'apply_context'], name, value)


            class Codes(_Entity_):
                """
                Message codes defining the rule.
                
                .. attribute:: category
                
                	Category of messages to which this alarm belongs
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: group
                
                	Group of messages to which this alarm belongs
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: code
                
                	Alarm code which further qualifies the alarm within a message group
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Correlator.Rules.Rule.Codes, self).__init__()

                    self.yang_name = "codes"
                    self.yang_parent_name = "rule"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('category', (YLeaf(YType.str, 'category'), ['str'])),
                        ('group', (YLeaf(YType.str, 'group'), ['str'])),
                        ('code', (YLeaf(YType.str, 'code'), ['str'])),
                    ])
                    self.category = None
                    self.group = None
                    self.code = None
                    self._segment_path = lambda: "codes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Correlator.Rules.Rule.Codes, ['category', 'group', 'code'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                    return meta._meta_table['Correlator.Rules.Rule.Codes']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Correlator.Rules.Rule']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Correlator.Rules']['meta_info']


    class BufferStatus(_Entity_):
        """
        Describes buffer utilization and parameters
        configured
        
        .. attribute:: current_size
        
        	Current buffer usage
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: configured_size
        
        	Configured buffer size
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Correlator.BufferStatus, self).__init__()

            self.yang_name = "buffer-status"
            self.yang_parent_name = "correlator"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('current_size', (YLeaf(YType.uint32, 'current-size'), ['int'])),
                ('configured_size', (YLeaf(YType.uint32, 'configured-size'), ['int'])),
            ])
            self.current_size = None
            self.configured_size = None
            self._segment_path = lambda: "buffer-status"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Correlator.BufferStatus, ['current_size', 'configured_size'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Correlator.BufferStatus']['meta_info']


    class Alarms(_Entity_):
        """
        Correlated alarms Table
        
        .. attribute:: alarm
        
        	One of the correlated alarms
        	**type**\: list of  		 :py:class:`Alarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Alarms.Alarm>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Correlator.Alarms, self).__init__()

            self.yang_name = "alarms"
            self.yang_parent_name = "correlator"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("alarm", ("alarm", Correlator.Alarms.Alarm))])
            self._leafs = OrderedDict()

            self.alarm = YList(self)
            self._segment_path = lambda: "alarms"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Correlator.Alarms, [], name, value)


        class Alarm(_Entity_):
            """
            One of the correlated alarms
            
            .. attribute:: alarm_id  (key)
            
            	Alarm ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: alarm_info
            
            	Correlated alarm information
            	**type**\:  :py:class:`AlarmInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Alarms.Alarm.AlarmInfo>`
            
            	**config**\: False
            
            .. attribute:: rule_name
            
            	Correlation rule name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: context
            
            	Context string  for the alarm
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Correlator.Alarms.Alarm, self).__init__()

                self.yang_name = "alarm"
                self.yang_parent_name = "alarms"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['alarm_id']
                self._child_classes = OrderedDict([("alarm-info", ("alarm_info", Correlator.Alarms.Alarm.AlarmInfo))])
                self._leafs = OrderedDict([
                    ('alarm_id', (YLeaf(YType.uint32, 'alarm-id'), ['int'])),
                    ('rule_name', (YLeaf(YType.str, 'rule-name'), ['str'])),
                    ('context', (YLeaf(YType.str, 'context'), ['str'])),
                ])
                self.alarm_id = None
                self.rule_name = None
                self.context = None

                self.alarm_info = Correlator.Alarms.Alarm.AlarmInfo()
                self.alarm_info.parent = self
                self._children_name_map["alarm_info"] = "alarm-info"
                self._segment_path = lambda: "alarm" + "[alarm-id='" + str(self.alarm_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/alarms/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Correlator.Alarms.Alarm, ['alarm_id', 'rule_name', 'context'], name, value)


            class AlarmInfo(_Entity_):
                """
                Correlated alarm information
                
                .. attribute:: source_id
                
                	Source Identifier(Location).Indicates the node in which the alarm was generated
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: timestamp
                
                	Time when the alarm was generated. It is expressed in number of milliseconds since 00\:00 \:00 UTC, January 1, 1970
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: millisecond
                
                .. attribute:: category
                
                	Category of the alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: group
                
                	Group of messages to which this alarm belongs to
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: code
                
                	Alarm code which further qualifies the alarm within a message group
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: severity
                
                	Severity of the alarm
                	**type**\:  :py:class:`AlAlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AlAlarmSeverity>`
                
                	**config**\: False
                
                .. attribute:: state
                
                	State of the alarm (bistate alarms only)
                	**type**\:  :py:class:`AlAlarmBistate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AlAlarmBistate>`
                
                	**config**\: False
                
                .. attribute:: correlation_id
                
                	Correlation Identifier
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: is_admin
                
                	Indicates the event id admin\-level
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: additional_text
                
                	Full text of the Alarm
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Correlator.Alarms.Alarm.AlarmInfo, self).__init__()

                    self.yang_name = "alarm-info"
                    self.yang_parent_name = "alarm"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('source_id', (YLeaf(YType.str, 'source-id'), ['str'])),
                        ('timestamp', (YLeaf(YType.uint64, 'timestamp'), ['int'])),
                        ('category', (YLeaf(YType.str, 'category'), ['str'])),
                        ('group', (YLeaf(YType.str, 'group'), ['str'])),
                        ('code', (YLeaf(YType.str, 'code'), ['str'])),
                        ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AlAlarmSeverity', '')])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AlAlarmBistate', '')])),
                        ('correlation_id', (YLeaf(YType.uint32, 'correlation-id'), ['int'])),
                        ('is_admin', (YLeaf(YType.boolean, 'is-admin'), ['bool'])),
                        ('additional_text', (YLeaf(YType.str, 'additional-text'), ['str'])),
                    ])
                    self.source_id = None
                    self.timestamp = None
                    self.category = None
                    self.group = None
                    self.code = None
                    self.severity = None
                    self.state = None
                    self.correlation_id = None
                    self.is_admin = None
                    self.additional_text = None
                    self._segment_path = lambda: "alarm-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Correlator.Alarms.Alarm.AlarmInfo, ['source_id', 'timestamp', 'category', 'group', 'code', 'severity', 'state', 'correlation_id', 'is_admin', 'additional_text'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                    return meta._meta_table['Correlator.Alarms.Alarm.AlarmInfo']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Correlator.Alarms.Alarm']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Correlator.Alarms']['meta_info']


    class RuleSetSummaries(_Entity_):
        """
        Table that contains the ruleset summary info
        
        .. attribute:: rule_set_summary
        
        	Summary of one of the correlation rulesets
        	**type**\: list of  		 :py:class:`RuleSetSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSetSummaries.RuleSetSummary>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Correlator.RuleSetSummaries, self).__init__()

            self.yang_name = "rule-set-summaries"
            self.yang_parent_name = "correlator"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rule-set-summary", ("rule_set_summary", Correlator.RuleSetSummaries.RuleSetSummary))])
            self._leafs = OrderedDict()

            self.rule_set_summary = YList(self)
            self._segment_path = lambda: "rule-set-summaries"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Correlator.RuleSetSummaries, [], name, value)


        class RuleSetSummary(_Entity_):
            """
            Summary of one of the correlation rulesets
            
            .. attribute:: rule_set_name  (key)
            
            	Ruleset Name
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: rule_set_name_xr
            
            	Ruleset Name
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Correlator.RuleSetSummaries.RuleSetSummary, self).__init__()

                self.yang_name = "rule-set-summary"
                self.yang_parent_name = "rule-set-summaries"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rule_set_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rule_set_name', (YLeaf(YType.str, 'rule-set-name'), ['str'])),
                    ('rule_set_name_xr', (YLeaf(YType.str, 'rule-set-name-xr'), ['str'])),
                ])
                self.rule_set_name = None
                self.rule_set_name_xr = None
                self._segment_path = lambda: "rule-set-summary" + "[rule-set-name='" + str(self.rule_set_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/rule-set-summaries/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Correlator.RuleSetSummaries.RuleSetSummary, ['rule_set_name', 'rule_set_name_xr'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Correlator.RuleSetSummaries.RuleSetSummary']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Correlator.RuleSetSummaries']['meta_info']


    class RuleSetDetails(_Entity_):
        """
        Table that contains the ruleset detail info
        
        .. attribute:: rule_set_detail
        
        	Detail of one of the correlation rulesets
        	**type**\: list of  		 :py:class:`RuleSetDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSetDetails.RuleSetDetail>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Correlator.RuleSetDetails, self).__init__()

            self.yang_name = "rule-set-details"
            self.yang_parent_name = "correlator"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rule-set-detail", ("rule_set_detail", Correlator.RuleSetDetails.RuleSetDetail))])
            self._leafs = OrderedDict()

            self.rule_set_detail = YList(self)
            self._segment_path = lambda: "rule-set-details"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Correlator.RuleSetDetails, [], name, value)


        class RuleSetDetail(_Entity_):
            """
            Detail of one of the correlation rulesets
            
            .. attribute:: rule_set_name  (key)
            
            	Ruleset Name
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: rule_set_name_xr
            
            	Ruleset Name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: rules
            
            	Rules contained in a ruleset
            	**type**\: list of  		 :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSetDetails.RuleSetDetail.Rules>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Correlator.RuleSetDetails.RuleSetDetail, self).__init__()

                self.yang_name = "rule-set-detail"
                self.yang_parent_name = "rule-set-details"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rule_set_name']
                self._child_classes = OrderedDict([("rules", ("rules", Correlator.RuleSetDetails.RuleSetDetail.Rules))])
                self._leafs = OrderedDict([
                    ('rule_set_name', (YLeaf(YType.str, 'rule-set-name'), ['str'])),
                    ('rule_set_name_xr', (YLeaf(YType.str, 'rule-set-name-xr'), ['str'])),
                ])
                self.rule_set_name = None
                self.rule_set_name_xr = None

                self.rules = YList(self)
                self._segment_path = lambda: "rule-set-detail" + "[rule-set-name='" + str(self.rule_set_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/rule-set-details/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Correlator.RuleSetDetails.RuleSetDetail, ['rule_set_name', 'rule_set_name_xr'], name, value)


            class Rules(_Entity_):
                """
                Rules contained in a ruleset
                
                .. attribute:: rule_name_xr
                
                	Correlation Rule Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: stateful
                
                	Whether the rule is stateful
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: rule_state
                
                	Applied state of the rule It could be not applied, applied or applied to all
                	**type**\:  :py:class:`AcRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleState>`
                
                	**config**\: False
                
                .. attribute:: buffered_alarms_count
                
                	Number of buffered alarms correlated to this rule
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Correlator.RuleSetDetails.RuleSetDetail.Rules, self).__init__()

                    self.yang_name = "rules"
                    self.yang_parent_name = "rule-set-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rule_name_xr', (YLeaf(YType.str, 'rule-name-xr'), ['str'])),
                        ('stateful', (YLeaf(YType.boolean, 'stateful'), ['bool'])),
                        ('rule_state', (YLeaf(YType.enumeration, 'rule-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AcRuleState', '')])),
                        ('buffered_alarms_count', (YLeaf(YType.uint32, 'buffered-alarms-count'), ['int'])),
                    ])
                    self.rule_name_xr = None
                    self.stateful = None
                    self.rule_state = None
                    self.buffered_alarms_count = None
                    self._segment_path = lambda: "rules"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Correlator.RuleSetDetails.RuleSetDetail.Rules, ['rule_name_xr', 'stateful', 'rule_state', 'buffered_alarms_count'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                    return meta._meta_table['Correlator.RuleSetDetails.RuleSetDetail.Rules']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Correlator.RuleSetDetails.RuleSetDetail']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Correlator.RuleSetDetails']['meta_info']


    class RuleDetails(_Entity_):
        """
        Table that contains the database of correlation
        rule details
        
        .. attribute:: rule_detail
        
        	Details of one of the correlation rules
        	**type**\: list of  		 :py:class:`RuleDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleDetails.RuleDetail>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Correlator.RuleDetails, self).__init__()

            self.yang_name = "rule-details"
            self.yang_parent_name = "correlator"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rule-detail", ("rule_detail", Correlator.RuleDetails.RuleDetail))])
            self._leafs = OrderedDict()

            self.rule_detail = YList(self)
            self._segment_path = lambda: "rule-details"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Correlator.RuleDetails, [], name, value)


        class RuleDetail(_Entity_):
            """
            Details of one of the correlation rules
            
            .. attribute:: rule_name  (key)
            
            	Correlation Rule Name
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: rule_summary
            
            	Rule summary, name, etc
            	**type**\:  :py:class:`RuleSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleDetails.RuleDetail.RuleSummary>`
            
            	**config**\: False
            
            .. attribute:: timeout
            
            	Time window (in ms) for which root/all messages are kept in correlater before sending them to the logger
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: root_cause_timeout
            
            	Timeout before root cause alarm
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: internal
            
            	True if the rule is internal
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: reissue_non_bistate
            
            	Whether to reissue non\-bistate alarms
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: reparent
            
            	Reparent
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: context_correlation
            
            	Whether context correlation is enabled
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: apply_location
            
            	Locations (R/S/M) to which the rule is applied
            	**type**\: list of str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: apply_context
            
            	Contexts (Interfaces) to which the rule is applied
            	**type**\: list of str
            
            	**length:** 0..33
            
            	**config**\: False
            
            .. attribute:: codes
            
            	Message codes defining the rule
            	**type**\: list of  		 :py:class:`Codes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleDetails.RuleDetail.Codes>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Correlator.RuleDetails.RuleDetail, self).__init__()

                self.yang_name = "rule-detail"
                self.yang_parent_name = "rule-details"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rule_name']
                self._child_classes = OrderedDict([("rule-summary", ("rule_summary", Correlator.RuleDetails.RuleDetail.RuleSummary)), ("codes", ("codes", Correlator.RuleDetails.RuleDetail.Codes))])
                self._leafs = OrderedDict([
                    ('rule_name', (YLeaf(YType.str, 'rule-name'), ['str'])),
                    ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                    ('root_cause_timeout', (YLeaf(YType.uint32, 'root-cause-timeout'), ['int'])),
                    ('internal', (YLeaf(YType.boolean, 'internal'), ['bool'])),
                    ('reissue_non_bistate', (YLeaf(YType.boolean, 'reissue-non-bistate'), ['bool'])),
                    ('reparent', (YLeaf(YType.boolean, 'reparent'), ['bool'])),
                    ('context_correlation', (YLeaf(YType.boolean, 'context-correlation'), ['bool'])),
                    ('apply_location', (YLeafList(YType.str, 'apply-location'), ['str'])),
                    ('apply_context', (YLeafList(YType.str, 'apply-context'), ['str'])),
                ])
                self.rule_name = None
                self.timeout = None
                self.root_cause_timeout = None
                self.internal = None
                self.reissue_non_bistate = None
                self.reparent = None
                self.context_correlation = None
                self.apply_location = []
                self.apply_context = []

                self.rule_summary = Correlator.RuleDetails.RuleDetail.RuleSummary()
                self.rule_summary.parent = self
                self._children_name_map["rule_summary"] = "rule-summary"

                self.codes = YList(self)
                self._segment_path = lambda: "rule-detail" + "[rule-name='" + str(self.rule_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/rule-details/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Correlator.RuleDetails.RuleDetail, ['rule_name', 'timeout', 'root_cause_timeout', 'internal', 'reissue_non_bistate', 'reparent', 'context_correlation', 'apply_location', 'apply_context'], name, value)


            class RuleSummary(_Entity_):
                """
                Rule summary, name, etc
                
                .. attribute:: rule_name_xr
                
                	Correlation Rule Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: stateful
                
                	Whether the rule is stateful
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: rule_state
                
                	Applied state of the rule It could be not applied, applied or applied to all
                	**type**\:  :py:class:`AcRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleState>`
                
                	**config**\: False
                
                .. attribute:: buffered_alarms_count
                
                	Number of buffered alarms correlated to this rule
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Correlator.RuleDetails.RuleDetail.RuleSummary, self).__init__()

                    self.yang_name = "rule-summary"
                    self.yang_parent_name = "rule-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rule_name_xr', (YLeaf(YType.str, 'rule-name-xr'), ['str'])),
                        ('stateful', (YLeaf(YType.boolean, 'stateful'), ['bool'])),
                        ('rule_state', (YLeaf(YType.enumeration, 'rule-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AcRuleState', '')])),
                        ('buffered_alarms_count', (YLeaf(YType.uint32, 'buffered-alarms-count'), ['int'])),
                    ])
                    self.rule_name_xr = None
                    self.stateful = None
                    self.rule_state = None
                    self.buffered_alarms_count = None
                    self._segment_path = lambda: "rule-summary"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Correlator.RuleDetails.RuleDetail.RuleSummary, ['rule_name_xr', 'stateful', 'rule_state', 'buffered_alarms_count'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                    return meta._meta_table['Correlator.RuleDetails.RuleDetail.RuleSummary']['meta_info']


            class Codes(_Entity_):
                """
                Message codes defining the rule.
                
                .. attribute:: category
                
                	Category of messages to which this alarm belongs
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: group
                
                	Group of messages to which this alarm belongs
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: code
                
                	Alarm code which further qualifies the alarm within a message group
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Correlator.RuleDetails.RuleDetail.Codes, self).__init__()

                    self.yang_name = "codes"
                    self.yang_parent_name = "rule-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('category', (YLeaf(YType.str, 'category'), ['str'])),
                        ('group', (YLeaf(YType.str, 'group'), ['str'])),
                        ('code', (YLeaf(YType.str, 'code'), ['str'])),
                    ])
                    self.category = None
                    self.group = None
                    self.code = None
                    self._segment_path = lambda: "codes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Correlator.RuleDetails.RuleDetail.Codes, ['category', 'group', 'code'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                    return meta._meta_table['Correlator.RuleDetails.RuleDetail.Codes']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Correlator.RuleDetails.RuleDetail']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Correlator.RuleDetails']['meta_info']


    class RuleSummaries(_Entity_):
        """
        Table that contains the database of correlation
        rule summary
        
        .. attribute:: rule_summary
        
        	One of the correlation rules
        	**type**\: list of  		 :py:class:`RuleSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSummaries.RuleSummary>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Correlator.RuleSummaries, self).__init__()

            self.yang_name = "rule-summaries"
            self.yang_parent_name = "correlator"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rule-summary", ("rule_summary", Correlator.RuleSummaries.RuleSummary))])
            self._leafs = OrderedDict()

            self.rule_summary = YList(self)
            self._segment_path = lambda: "rule-summaries"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Correlator.RuleSummaries, [], name, value)


        class RuleSummary(_Entity_):
            """
            One of the correlation rules
            
            .. attribute:: rule_name  (key)
            
            	Correlation Rule Name
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: rule_name_xr
            
            	Correlation Rule Name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: stateful
            
            	Whether the rule is stateful
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rule_state
            
            	Applied state of the rule It could be not applied, applied or applied to all
            	**type**\:  :py:class:`AcRuleState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleState>`
            
            	**config**\: False
            
            .. attribute:: buffered_alarms_count
            
            	Number of buffered alarms correlated to this rule
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Correlator.RuleSummaries.RuleSummary, self).__init__()

                self.yang_name = "rule-summary"
                self.yang_parent_name = "rule-summaries"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rule_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rule_name', (YLeaf(YType.str, 'rule-name'), ['str'])),
                    ('rule_name_xr', (YLeaf(YType.str, 'rule-name-xr'), ['str'])),
                    ('stateful', (YLeaf(YType.boolean, 'stateful'), ['bool'])),
                    ('rule_state', (YLeaf(YType.enumeration, 'rule-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AcRuleState', '')])),
                    ('buffered_alarms_count', (YLeaf(YType.uint32, 'buffered-alarms-count'), ['int'])),
                ])
                self.rule_name = None
                self.rule_name_xr = None
                self.stateful = None
                self.rule_state = None
                self.buffered_alarms_count = None
                self._segment_path = lambda: "rule-summary" + "[rule-name='" + str(self.rule_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-correlator-oper:correlator/rule-summaries/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Correlator.RuleSummaries.RuleSummary, ['rule_name', 'rule_name_xr', 'stateful', 'rule_state', 'buffered_alarms_count'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Correlator.RuleSummaries.RuleSummary']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Correlator.RuleSummaries']['meta_info']

    def clone_ptr(self):
        self._top_entity = Correlator()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
        return meta._meta_table['Correlator']['meta_info']


