""" Cisco_IOS_XR_infra_correlator_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-correlator package operational data.

This module contains definitions
for the following management objects\:
  suppression\: Suppression operational data
  correlator\: correlator

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AcRuleStateEnum(Enum):
    """
    AcRuleStateEnum

    Ac rule state

    .. data:: rule_unapplied = 0

    	Rule is in Unapplied state

    .. data:: rule_applied = 1

    	Rule is Applied to specified RacksSlots,

    	Contexts and Sources

    .. data:: rule_applied_all = 2

    	Rule is Applied to all of router

    """

    rule_unapplied = 0

    rule_applied = 1

    rule_applied_all = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
        return meta._meta_table['AcRuleStateEnum']


class AlAlarmBistateEnum(Enum):
    """
    AlAlarmBistateEnum

    Al alarm bistate

    .. data:: not_available = 0

    	not available

    .. data:: active = 1

    	active

    .. data:: clear = 2

    	clear

    """

    not_available = 0

    active = 1

    clear = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
        return meta._meta_table['AlAlarmBistateEnum']


class AlAlarmSeverityEnum(Enum):
    """
    AlAlarmSeverityEnum

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

    unknown = -1

    emergency = 0

    alert = 1

    critical = 2

    error = 3

    warning = 4

    notice = 5

    informational = 6

    debugging = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
        return meta._meta_table['AlAlarmSeverityEnum']



class Suppression(object):
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
    _revision = '2015-11-09'

    def __init__(self):
        self.rule_details = Suppression.RuleDetails()
        self.rule_details.parent = self
        self.rule_summaries = Suppression.RuleSummaries()
        self.rule_summaries.parent = self


    class RuleSummaries(object):
        """
        Table that contains the database of suppression
        rule summary
        
        .. attribute:: rule_summary
        
        	One of the suppression rules
        	**type**\: list of    :py:class:`RuleSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Suppression.RuleSummaries.RuleSummary>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.rule_summary = YList()
            self.rule_summary.parent = self
            self.rule_summary.name = 'rule_summary'


        class RuleSummary(object):
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
            	**type**\:   :py:class:`AcRuleStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleStateEnum>`
            
            .. attribute:: suppressed_alarms_count
            
            	Number of suppressed alarms associated with this rule
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.rule_name = None
                self.rule_name_xr = None
                self.rule_state = None
                self.suppressed_alarms_count = None

            @property
            def _common_path(self):
                if self.rule_name is None:
                    raise YPYModelError('Key property rule_name is None')

                return '/Cisco-IOS-XR-infra-correlator-oper:suppression/Cisco-IOS-XR-infra-correlator-oper:rule-summaries/Cisco-IOS-XR-infra-correlator-oper:rule-summary[Cisco-IOS-XR-infra-correlator-oper:rule-name = ' + str(self.rule_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rule_name is not None:
                    return True

                if self.rule_name_xr is not None:
                    return True

                if self.rule_state is not None:
                    return True

                if self.suppressed_alarms_count is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Suppression.RuleSummaries.RuleSummary']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-correlator-oper:suppression/Cisco-IOS-XR-infra-correlator-oper:rule-summaries'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rule_summary is not None:
                for child_ref in self.rule_summary:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Suppression.RuleSummaries']['meta_info']


    class RuleDetails(object):
        """
        Table that contains the database of suppression
        rule details
        
        .. attribute:: rule_detail
        
        	Details of one of the suppression rules
        	**type**\: list of    :py:class:`RuleDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Suppression.RuleDetails.RuleDetail>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.rule_detail = YList()
            self.rule_detail.parent = self
            self.rule_detail.name = 'rule_detail'


        class RuleDetail(object):
            """
            Details of one of the suppression rules
            
            .. attribute:: rule_name  <key>
            
            	Suppression Rule Name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: alarm_severity
            
            	Severity level to suppress
            	**type**\:   :py:class:`AlAlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AlAlarmSeverityEnum>`
            
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.rule_name = None
                self.alarm_severity = None
                self.all_alarms = None
                self.apply_source = YLeafList()
                self.apply_source.parent = self
                self.apply_source.name = 'apply_source'
                self.codes = YList()
                self.codes.parent = self
                self.codes.name = 'codes'
                self.rule_summary = Suppression.RuleDetails.RuleDetail.RuleSummary()
                self.rule_summary.parent = self


            class RuleSummary(object):
                """
                Rule summary, name, etc
                
                .. attribute:: rule_name_xr
                
                	Suppress Rule Name
                	**type**\:  str
                
                .. attribute:: rule_state
                
                	Applied state of the rule It could be not applied, applied or applied to all
                	**type**\:   :py:class:`AcRuleStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleStateEnum>`
                
                .. attribute:: suppressed_alarms_count
                
                	Number of suppressed alarms associated with this rule
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.rule_name_xr = None
                    self.rule_state = None
                    self.suppressed_alarms_count = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-oper:rule-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.rule_name_xr is not None:
                        return True

                    if self.rule_state is not None:
                        return True

                    if self.suppressed_alarms_count is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                    return meta._meta_table['Suppression.RuleDetails.RuleDetail.RuleSummary']['meta_info']


            class Codes(object):
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
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.category = None
                    self.code = None
                    self.group = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-oper:codes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.category is not None:
                        return True

                    if self.code is not None:
                        return True

                    if self.group is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                    return meta._meta_table['Suppression.RuleDetails.RuleDetail.Codes']['meta_info']

            @property
            def _common_path(self):
                if self.rule_name is None:
                    raise YPYModelError('Key property rule_name is None')

                return '/Cisco-IOS-XR-infra-correlator-oper:suppression/Cisco-IOS-XR-infra-correlator-oper:rule-details/Cisco-IOS-XR-infra-correlator-oper:rule-detail[Cisco-IOS-XR-infra-correlator-oper:rule-name = ' + str(self.rule_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rule_name is not None:
                    return True

                if self.alarm_severity is not None:
                    return True

                if self.all_alarms is not None:
                    return True

                if self.apply_source is not None:
                    for child in self.apply_source:
                        if child is not None:
                            return True

                if self.codes is not None:
                    for child_ref in self.codes:
                        if child_ref._has_data():
                            return True

                if self.rule_summary is not None and self.rule_summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Suppression.RuleDetails.RuleDetail']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-correlator-oper:suppression/Cisco-IOS-XR-infra-correlator-oper:rule-details'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rule_detail is not None:
                for child_ref in self.rule_detail:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Suppression.RuleDetails']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-correlator-oper:suppression'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.rule_details is not None and self.rule_details._has_data():
            return True

        if self.rule_summaries is not None and self.rule_summaries._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
        return meta._meta_table['Suppression']['meta_info']


class Correlator(object):
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
    _revision = '2015-11-09'

    def __init__(self):
        self.alarms = Correlator.Alarms()
        self.alarms.parent = self
        self.buffer_status = Correlator.BufferStatus()
        self.buffer_status.parent = self
        self.rule_details = Correlator.RuleDetails()
        self.rule_details.parent = self
        self.rule_set_details = Correlator.RuleSetDetails()
        self.rule_set_details.parent = self
        self.rule_set_summaries = Correlator.RuleSetSummaries()
        self.rule_set_summaries.parent = self
        self.rule_summaries = Correlator.RuleSummaries()
        self.rule_summaries.parent = self
        self.rules = Correlator.Rules()
        self.rules.parent = self


    class Rules(object):
        """
        Table that contains the database of correlation
        rules
        
        .. attribute:: rule
        
        	One of the correlation rules
        	**type**\: list of    :py:class:`Rule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Rules.Rule>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.rule = YList()
            self.rule.parent = self
            self.rule.name = 'rule'


        class Rule(object):
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
            	**type**\:   :py:class:`AcRuleStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleStateEnum>`
            
            .. attribute:: timeout
            
            	Time window (in ms) for which root/all messages are kept in correlater before sending them to the logger
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.rule_name = None
                self.apply_context = YLeafList()
                self.apply_context.parent = self
                self.apply_context.name = 'apply_context'
                self.apply_location = YLeafList()
                self.apply_location.parent = self
                self.apply_location.name = 'apply_location'
                self.codes = YList()
                self.codes.parent = self
                self.codes.name = 'codes'
                self.rule_name_xr = None
                self.rule_state = None
                self.timeout = None


            class Codes(object):
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
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.category = None
                    self.code = None
                    self.group = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-oper:codes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.category is not None:
                        return True

                    if self.code is not None:
                        return True

                    if self.group is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                    return meta._meta_table['Correlator.Rules.Rule.Codes']['meta_info']

            @property
            def _common_path(self):
                if self.rule_name is None:
                    raise YPYModelError('Key property rule_name is None')

                return '/Cisco-IOS-XR-infra-correlator-oper:correlator/Cisco-IOS-XR-infra-correlator-oper:rules/Cisco-IOS-XR-infra-correlator-oper:rule[Cisco-IOS-XR-infra-correlator-oper:rule-name = ' + str(self.rule_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rule_name is not None:
                    return True

                if self.apply_context is not None:
                    for child in self.apply_context:
                        if child is not None:
                            return True

                if self.apply_location is not None:
                    for child in self.apply_location:
                        if child is not None:
                            return True

                if self.codes is not None:
                    for child_ref in self.codes:
                        if child_ref._has_data():
                            return True

                if self.rule_name_xr is not None:
                    return True

                if self.rule_state is not None:
                    return True

                if self.timeout is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Correlator.Rules.Rule']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-correlator-oper:correlator/Cisco-IOS-XR-infra-correlator-oper:rules'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rule is not None:
                for child_ref in self.rule:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Correlator.Rules']['meta_info']


    class BufferStatus(object):
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
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.configured_size = None
            self.current_size = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-correlator-oper:correlator/Cisco-IOS-XR-infra-correlator-oper:buffer-status'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.configured_size is not None:
                return True

            if self.current_size is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Correlator.BufferStatus']['meta_info']


    class Alarms(object):
        """
        Correlated alarms Table
        
        .. attribute:: alarm
        
        	One of the correlated alarms
        	**type**\: list of    :py:class:`Alarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Alarms.Alarm>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.alarm = YList()
            self.alarm.parent = self
            self.alarm.name = 'alarm'


        class Alarm(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.alarm_id = None
                self.alarm_info = Correlator.Alarms.Alarm.AlarmInfo()
                self.alarm_info.parent = self
                self.context = None
                self.rule_name = None


            class AlarmInfo(object):
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
                	**type**\:   :py:class:`AlAlarmSeverityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AlAlarmSeverityEnum>`
                
                .. attribute:: source_id
                
                	Source Identifier(Location).Indicates the node in which the alarm was generated
                	**type**\:  str
                
                .. attribute:: state
                
                	State of the alarm (bistate alarms only)
                	**type**\:   :py:class:`AlAlarmBistateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AlAlarmBistateEnum>`
                
                .. attribute:: timestamp
                
                	Time when the alarm was generated. It is expressed in number of milliseconds since 00\:00 \:00 UTC, January 1, 1970
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: millisecond
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.additional_text = None
                    self.category = None
                    self.code = None
                    self.correlation_id = None
                    self.group = None
                    self.is_admin = None
                    self.severity = None
                    self.source_id = None
                    self.state = None
                    self.timestamp = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-oper:alarm-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.additional_text is not None:
                        return True

                    if self.category is not None:
                        return True

                    if self.code is not None:
                        return True

                    if self.correlation_id is not None:
                        return True

                    if self.group is not None:
                        return True

                    if self.is_admin is not None:
                        return True

                    if self.severity is not None:
                        return True

                    if self.source_id is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.timestamp is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                    return meta._meta_table['Correlator.Alarms.Alarm.AlarmInfo']['meta_info']

            @property
            def _common_path(self):
                if self.alarm_id is None:
                    raise YPYModelError('Key property alarm_id is None')

                return '/Cisco-IOS-XR-infra-correlator-oper:correlator/Cisco-IOS-XR-infra-correlator-oper:alarms/Cisco-IOS-XR-infra-correlator-oper:alarm[Cisco-IOS-XR-infra-correlator-oper:alarm-id = ' + str(self.alarm_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.alarm_id is not None:
                    return True

                if self.alarm_info is not None and self.alarm_info._has_data():
                    return True

                if self.context is not None:
                    return True

                if self.rule_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Correlator.Alarms.Alarm']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-correlator-oper:correlator/Cisco-IOS-XR-infra-correlator-oper:alarms'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.alarm is not None:
                for child_ref in self.alarm:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Correlator.Alarms']['meta_info']


    class RuleSetSummaries(object):
        """
        Table that contains the ruleset summary info
        
        .. attribute:: rule_set_summary
        
        	Summary of one of the correlation rulesets
        	**type**\: list of    :py:class:`RuleSetSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSetSummaries.RuleSetSummary>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.rule_set_summary = YList()
            self.rule_set_summary.parent = self
            self.rule_set_summary.name = 'rule_set_summary'


        class RuleSetSummary(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.rule_set_name = None
                self.rule_set_name_xr = None

            @property
            def _common_path(self):
                if self.rule_set_name is None:
                    raise YPYModelError('Key property rule_set_name is None')

                return '/Cisco-IOS-XR-infra-correlator-oper:correlator/Cisco-IOS-XR-infra-correlator-oper:rule-set-summaries/Cisco-IOS-XR-infra-correlator-oper:rule-set-summary[Cisco-IOS-XR-infra-correlator-oper:rule-set-name = ' + str(self.rule_set_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rule_set_name is not None:
                    return True

                if self.rule_set_name_xr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Correlator.RuleSetSummaries.RuleSetSummary']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-correlator-oper:correlator/Cisco-IOS-XR-infra-correlator-oper:rule-set-summaries'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rule_set_summary is not None:
                for child_ref in self.rule_set_summary:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Correlator.RuleSetSummaries']['meta_info']


    class RuleSetDetails(object):
        """
        Table that contains the ruleset detail info
        
        .. attribute:: rule_set_detail
        
        	Detail of one of the correlation rulesets
        	**type**\: list of    :py:class:`RuleSetDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSetDetails.RuleSetDetail>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.rule_set_detail = YList()
            self.rule_set_detail.parent = self
            self.rule_set_detail.name = 'rule_set_detail'


        class RuleSetDetail(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.rule_set_name = None
                self.rule_set_name_xr = None
                self.rules = YList()
                self.rules.parent = self
                self.rules.name = 'rules'


            class Rules(object):
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
                	**type**\:   :py:class:`AcRuleStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleStateEnum>`
                
                .. attribute:: stateful
                
                	Whether the rule is stateful
                	**type**\:  bool
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.buffered_alarms_count = None
                    self.rule_name_xr = None
                    self.rule_state = None
                    self.stateful = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-oper:rules'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.buffered_alarms_count is not None:
                        return True

                    if self.rule_name_xr is not None:
                        return True

                    if self.rule_state is not None:
                        return True

                    if self.stateful is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                    return meta._meta_table['Correlator.RuleSetDetails.RuleSetDetail.Rules']['meta_info']

            @property
            def _common_path(self):
                if self.rule_set_name is None:
                    raise YPYModelError('Key property rule_set_name is None')

                return '/Cisco-IOS-XR-infra-correlator-oper:correlator/Cisco-IOS-XR-infra-correlator-oper:rule-set-details/Cisco-IOS-XR-infra-correlator-oper:rule-set-detail[Cisco-IOS-XR-infra-correlator-oper:rule-set-name = ' + str(self.rule_set_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rule_set_name is not None:
                    return True

                if self.rule_set_name_xr is not None:
                    return True

                if self.rules is not None:
                    for child_ref in self.rules:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Correlator.RuleSetDetails.RuleSetDetail']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-correlator-oper:correlator/Cisco-IOS-XR-infra-correlator-oper:rule-set-details'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rule_set_detail is not None:
                for child_ref in self.rule_set_detail:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Correlator.RuleSetDetails']['meta_info']


    class RuleDetails(object):
        """
        Table that contains the database of correlation
        rule details
        
        .. attribute:: rule_detail
        
        	Details of one of the correlation rules
        	**type**\: list of    :py:class:`RuleDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleDetails.RuleDetail>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.rule_detail = YList()
            self.rule_detail.parent = self
            self.rule_detail.name = 'rule_detail'


        class RuleDetail(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.rule_name = None
                self.apply_context = YLeafList()
                self.apply_context.parent = self
                self.apply_context.name = 'apply_context'
                self.apply_location = YLeafList()
                self.apply_location.parent = self
                self.apply_location.name = 'apply_location'
                self.codes = YList()
                self.codes.parent = self
                self.codes.name = 'codes'
                self.context_correlation = None
                self.internal = None
                self.reissue_non_bistate = None
                self.reparent = None
                self.root_cause_timeout = None
                self.rule_summary = Correlator.RuleDetails.RuleDetail.RuleSummary()
                self.rule_summary.parent = self
                self.timeout = None


            class RuleSummary(object):
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
                	**type**\:   :py:class:`AcRuleStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleStateEnum>`
                
                .. attribute:: stateful
                
                	Whether the rule is stateful
                	**type**\:  bool
                
                

                """

                _prefix = 'infra-correlator-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.buffered_alarms_count = None
                    self.rule_name_xr = None
                    self.rule_state = None
                    self.stateful = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-oper:rule-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.buffered_alarms_count is not None:
                        return True

                    if self.rule_name_xr is not None:
                        return True

                    if self.rule_state is not None:
                        return True

                    if self.stateful is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                    return meta._meta_table['Correlator.RuleDetails.RuleDetail.RuleSummary']['meta_info']


            class Codes(object):
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
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.category = None
                    self.code = None
                    self.group = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-correlator-oper:codes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.category is not None:
                        return True

                    if self.code is not None:
                        return True

                    if self.group is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                    return meta._meta_table['Correlator.RuleDetails.RuleDetail.Codes']['meta_info']

            @property
            def _common_path(self):
                if self.rule_name is None:
                    raise YPYModelError('Key property rule_name is None')

                return '/Cisco-IOS-XR-infra-correlator-oper:correlator/Cisco-IOS-XR-infra-correlator-oper:rule-details/Cisco-IOS-XR-infra-correlator-oper:rule-detail[Cisco-IOS-XR-infra-correlator-oper:rule-name = ' + str(self.rule_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rule_name is not None:
                    return True

                if self.apply_context is not None:
                    for child in self.apply_context:
                        if child is not None:
                            return True

                if self.apply_location is not None:
                    for child in self.apply_location:
                        if child is not None:
                            return True

                if self.codes is not None:
                    for child_ref in self.codes:
                        if child_ref._has_data():
                            return True

                if self.context_correlation is not None:
                    return True

                if self.internal is not None:
                    return True

                if self.reissue_non_bistate is not None:
                    return True

                if self.reparent is not None:
                    return True

                if self.root_cause_timeout is not None:
                    return True

                if self.rule_summary is not None and self.rule_summary._has_data():
                    return True

                if self.timeout is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Correlator.RuleDetails.RuleDetail']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-correlator-oper:correlator/Cisco-IOS-XR-infra-correlator-oper:rule-details'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rule_detail is not None:
                for child_ref in self.rule_detail:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Correlator.RuleDetails']['meta_info']


    class RuleSummaries(object):
        """
        Table that contains the database of correlation
        rule summary
        
        .. attribute:: rule_summary
        
        	One of the correlation rules
        	**type**\: list of    :py:class:`RuleSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSummaries.RuleSummary>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.rule_summary = YList()
            self.rule_summary.parent = self
            self.rule_summary.name = 'rule_summary'


        class RuleSummary(object):
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
            	**type**\:   :py:class:`AcRuleStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.AcRuleStateEnum>`
            
            .. attribute:: stateful
            
            	Whether the rule is stateful
            	**type**\:  bool
            
            

            """

            _prefix = 'infra-correlator-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.rule_name = None
                self.buffered_alarms_count = None
                self.rule_name_xr = None
                self.rule_state = None
                self.stateful = None

            @property
            def _common_path(self):
                if self.rule_name is None:
                    raise YPYModelError('Key property rule_name is None')

                return '/Cisco-IOS-XR-infra-correlator-oper:correlator/Cisco-IOS-XR-infra-correlator-oper:rule-summaries/Cisco-IOS-XR-infra-correlator-oper:rule-summary[Cisco-IOS-XR-infra-correlator-oper:rule-name = ' + str(self.rule_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rule_name is not None:
                    return True

                if self.buffered_alarms_count is not None:
                    return True

                if self.rule_name_xr is not None:
                    return True

                if self.rule_state is not None:
                    return True

                if self.stateful is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
                return meta._meta_table['Correlator.RuleSummaries.RuleSummary']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-correlator-oper:correlator/Cisco-IOS-XR-infra-correlator-oper:rule-summaries'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rule_summary is not None:
                for child_ref in self.rule_summary:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
            return meta._meta_table['Correlator.RuleSummaries']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-correlator-oper:correlator'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.alarms is not None and self.alarms._has_data():
            return True

        if self.buffer_status is not None and self.buffer_status._has_data():
            return True

        if self.rule_details is not None and self.rule_details._has_data():
            return True

        if self.rule_set_details is not None and self.rule_set_details._has_data():
            return True

        if self.rule_set_summaries is not None and self.rule_set_summaries._has_data():
            return True

        if self.rule_summaries is not None and self.rule_summaries._has_data():
            return True

        if self.rules is not None and self.rules._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_correlator_oper as meta
        return meta._meta_table['Correlator']['meta_info']


