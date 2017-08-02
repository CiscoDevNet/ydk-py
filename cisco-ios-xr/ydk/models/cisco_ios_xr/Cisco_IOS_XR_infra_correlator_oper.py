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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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
    _revision = '2015-11-09'

    def __init__(self):
        super(Suppression, self).__init__()
        self._top_entity = None

        self.yang_name = "suppression"
        self.yang_parent_name = "Cisco-IOS-XR-infra-correlator-oper"

        self.rule_details = Suppression.RuleDetails()
        self.rule_details.parent = self
        self._children_name_map["rule_details"] = "rule-details"
        self._children_yang_names.add("rule-details")

        self.rule_summaries = Suppression.RuleSummaries()
        self.rule_summaries.parent = self
        self._children_name_map["rule_summaries"] = "rule-summaries"
        self._children_yang_names.add("rule-summaries")


    class RuleSummaries(Entity):
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
            super(Suppression.RuleSummaries, self).__init__()

            self.yang_name = "rule-summaries"
            self.yang_parent_name = "suppression"

            self.rule_summary = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Suppression.RuleSummaries, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Suppression.RuleSummaries, self).__setattr__(name, value)


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
            _revision = '2015-11-09'

            def __init__(self):
                super(Suppression.RuleSummaries.RuleSummary, self).__init__()

                self.yang_name = "rule-summary"
                self.yang_parent_name = "rule-summaries"

                self.rule_name = YLeaf(YType.str, "rule-name")

                self.rule_name_xr = YLeaf(YType.str, "rule-name-xr")

                self.rule_state = YLeaf(YType.enumeration, "rule-state")

                self.suppressed_alarms_count = YLeaf(YType.uint32, "suppressed-alarms-count")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rule_name",
                                "rule_name_xr",
                                "rule_state",
                                "suppressed_alarms_count") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Suppression.RuleSummaries.RuleSummary, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Suppression.RuleSummaries.RuleSummary, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rule_name.is_set or
                    self.rule_name_xr.is_set or
                    self.rule_state.is_set or
                    self.suppressed_alarms_count.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rule_name.yfilter != YFilter.not_set or
                    self.rule_name_xr.yfilter != YFilter.not_set or
                    self.rule_state.yfilter != YFilter.not_set or
                    self.suppressed_alarms_count.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rule-summary" + "[rule-name='" + self.rule_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-correlator-oper:suppression/rule-summaries/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rule_name.is_set or self.rule_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_name.get_name_leafdata())
                if (self.rule_name_xr.is_set or self.rule_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_name_xr.get_name_leafdata())
                if (self.rule_state.is_set or self.rule_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_state.get_name_leafdata())
                if (self.suppressed_alarms_count.is_set or self.suppressed_alarms_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.suppressed_alarms_count.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rule-name" or name == "rule-name-xr" or name == "rule-state" or name == "suppressed-alarms-count"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rule-name"):
                    self.rule_name = value
                    self.rule_name.value_namespace = name_space
                    self.rule_name.value_namespace_prefix = name_space_prefix
                if(value_path == "rule-name-xr"):
                    self.rule_name_xr = value
                    self.rule_name_xr.value_namespace = name_space
                    self.rule_name_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "rule-state"):
                    self.rule_state = value
                    self.rule_state.value_namespace = name_space
                    self.rule_state.value_namespace_prefix = name_space_prefix
                if(value_path == "suppressed-alarms-count"):
                    self.suppressed_alarms_count = value
                    self.suppressed_alarms_count.value_namespace = name_space
                    self.suppressed_alarms_count.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rule_summary:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rule_summary:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rule-summaries" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-correlator-oper:suppression/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rule-summary"):
                for c in self.rule_summary:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Suppression.RuleSummaries.RuleSummary()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rule_summary.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rule-summary"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class RuleDetails(Entity):
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
            super(Suppression.RuleDetails, self).__init__()

            self.yang_name = "rule-details"
            self.yang_parent_name = "suppression"

            self.rule_detail = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Suppression.RuleDetails, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Suppression.RuleDetails, self).__setattr__(name, value)


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
            _revision = '2015-11-09'

            def __init__(self):
                super(Suppression.RuleDetails.RuleDetail, self).__init__()

                self.yang_name = "rule-detail"
                self.yang_parent_name = "rule-details"

                self.rule_name = YLeaf(YType.str, "rule-name")

                self.alarm_severity = YLeaf(YType.enumeration, "alarm-severity")

                self.all_alarms = YLeaf(YType.boolean, "all-alarms")

                self.apply_source = YLeafList(YType.str, "apply-source")

                self.rule_summary = Suppression.RuleDetails.RuleDetail.RuleSummary()
                self.rule_summary.parent = self
                self._children_name_map["rule_summary"] = "rule-summary"
                self._children_yang_names.add("rule-summary")

                self.codes = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rule_name",
                                "alarm_severity",
                                "all_alarms",
                                "apply_source") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Suppression.RuleDetails.RuleDetail, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Suppression.RuleDetails.RuleDetail, self).__setattr__(name, value)


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(Suppression.RuleDetails.RuleDetail.RuleSummary, self).__init__()

                    self.yang_name = "rule-summary"
                    self.yang_parent_name = "rule-detail"

                    self.rule_name_xr = YLeaf(YType.str, "rule-name-xr")

                    self.rule_state = YLeaf(YType.enumeration, "rule-state")

                    self.suppressed_alarms_count = YLeaf(YType.uint32, "suppressed-alarms-count")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("rule_name_xr",
                                    "rule_state",
                                    "suppressed_alarms_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Suppression.RuleDetails.RuleDetail.RuleSummary, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Suppression.RuleDetails.RuleDetail.RuleSummary, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.rule_name_xr.is_set or
                        self.rule_state.is_set or
                        self.suppressed_alarms_count.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.rule_name_xr.yfilter != YFilter.not_set or
                        self.rule_state.yfilter != YFilter.not_set or
                        self.suppressed_alarms_count.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rule-summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.rule_name_xr.is_set or self.rule_name_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rule_name_xr.get_name_leafdata())
                    if (self.rule_state.is_set or self.rule_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rule_state.get_name_leafdata())
                    if (self.suppressed_alarms_count.is_set or self.suppressed_alarms_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.suppressed_alarms_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "rule-name-xr" or name == "rule-state" or name == "suppressed-alarms-count"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "rule-name-xr"):
                        self.rule_name_xr = value
                        self.rule_name_xr.value_namespace = name_space
                        self.rule_name_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "rule-state"):
                        self.rule_state = value
                        self.rule_state.value_namespace = name_space
                        self.rule_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "suppressed-alarms-count"):
                        self.suppressed_alarms_count = value
                        self.suppressed_alarms_count.value_namespace = name_space
                        self.suppressed_alarms_count.value_namespace_prefix = name_space_prefix


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(Suppression.RuleDetails.RuleDetail.Codes, self).__init__()

                    self.yang_name = "codes"
                    self.yang_parent_name = "rule-detail"

                    self.category = YLeaf(YType.str, "category")

                    self.code = YLeaf(YType.str, "code")

                    self.group = YLeaf(YType.str, "group")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("category",
                                    "code",
                                    "group") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Suppression.RuleDetails.RuleDetail.Codes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Suppression.RuleDetails.RuleDetail.Codes, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.category.is_set or
                        self.code.is_set or
                        self.group.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.category.yfilter != YFilter.not_set or
                        self.code.yfilter != YFilter.not_set or
                        self.group.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "codes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.category.is_set or self.category.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.category.get_name_leafdata())
                    if (self.code.is_set or self.code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.code.get_name_leafdata())
                    if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "category" or name == "code" or name == "group"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "category"):
                        self.category = value
                        self.category.value_namespace = name_space
                        self.category.value_namespace_prefix = name_space_prefix
                    if(value_path == "code"):
                        self.code = value
                        self.code.value_namespace = name_space
                        self.code.value_namespace_prefix = name_space_prefix
                    if(value_path == "group"):
                        self.group = value
                        self.group.value_namespace = name_space
                        self.group.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.codes:
                    if (c.has_data()):
                        return True
                for leaf in self.apply_source.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.rule_name.is_set or
                    self.alarm_severity.is_set or
                    self.all_alarms.is_set or
                    (self.rule_summary is not None and self.rule_summary.has_data()))

            def has_operation(self):
                for c in self.codes:
                    if (c.has_operation()):
                        return True
                for leaf in self.apply_source.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.rule_name.yfilter != YFilter.not_set or
                    self.alarm_severity.yfilter != YFilter.not_set or
                    self.all_alarms.yfilter != YFilter.not_set or
                    self.apply_source.yfilter != YFilter.not_set or
                    (self.rule_summary is not None and self.rule_summary.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rule-detail" + "[rule-name='" + self.rule_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-correlator-oper:suppression/rule-details/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rule_name.is_set or self.rule_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_name.get_name_leafdata())
                if (self.alarm_severity.is_set or self.alarm_severity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.alarm_severity.get_name_leafdata())
                if (self.all_alarms.is_set or self.all_alarms.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.all_alarms.get_name_leafdata())

                leaf_name_data.extend(self.apply_source.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "codes"):
                    for c in self.codes:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Suppression.RuleDetails.RuleDetail.Codes()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.codes.append(c)
                    return c

                if (child_yang_name == "rule-summary"):
                    if (self.rule_summary is None):
                        self.rule_summary = Suppression.RuleDetails.RuleDetail.RuleSummary()
                        self.rule_summary.parent = self
                        self._children_name_map["rule_summary"] = "rule-summary"
                    return self.rule_summary

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "codes" or name == "rule-summary" or name == "rule-name" or name == "alarm-severity" or name == "all-alarms" or name == "apply-source"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rule-name"):
                    self.rule_name = value
                    self.rule_name.value_namespace = name_space
                    self.rule_name.value_namespace_prefix = name_space_prefix
                if(value_path == "alarm-severity"):
                    self.alarm_severity = value
                    self.alarm_severity.value_namespace = name_space
                    self.alarm_severity.value_namespace_prefix = name_space_prefix
                if(value_path == "all-alarms"):
                    self.all_alarms = value
                    self.all_alarms.value_namespace = name_space
                    self.all_alarms.value_namespace_prefix = name_space_prefix
                if(value_path == "apply-source"):
                    self.apply_source.append(value)

        def has_data(self):
            for c in self.rule_detail:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rule_detail:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rule-details" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-correlator-oper:suppression/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rule-detail"):
                for c in self.rule_detail:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Suppression.RuleDetails.RuleDetail()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rule_detail.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rule-detail"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.rule_details is not None and self.rule_details.has_data()) or
            (self.rule_summaries is not None and self.rule_summaries.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.rule_details is not None and self.rule_details.has_operation()) or
            (self.rule_summaries is not None and self.rule_summaries.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-correlator-oper:suppression" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "rule-details"):
            if (self.rule_details is None):
                self.rule_details = Suppression.RuleDetails()
                self.rule_details.parent = self
                self._children_name_map["rule_details"] = "rule-details"
            return self.rule_details

        if (child_yang_name == "rule-summaries"):
            if (self.rule_summaries is None):
                self.rule_summaries = Suppression.RuleSummaries()
                self.rule_summaries.parent = self
                self._children_name_map["rule_summaries"] = "rule-summaries"
            return self.rule_summaries

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "rule-details" or name == "rule-summaries"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Suppression()
        return self._top_entity

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
    _revision = '2015-11-09'

    def __init__(self):
        super(Correlator, self).__init__()
        self._top_entity = None

        self.yang_name = "correlator"
        self.yang_parent_name = "Cisco-IOS-XR-infra-correlator-oper"

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


    class Rules(Entity):
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
            super(Correlator.Rules, self).__init__()

            self.yang_name = "rules"
            self.yang_parent_name = "correlator"

            self.rule = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Correlator.Rules, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Correlator.Rules, self).__setattr__(name, value)


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
            _revision = '2015-11-09'

            def __init__(self):
                super(Correlator.Rules.Rule, self).__init__()

                self.yang_name = "rule"
                self.yang_parent_name = "rules"

                self.rule_name = YLeaf(YType.str, "rule-name")

                self.apply_context = YLeafList(YType.str, "apply-context")

                self.apply_location = YLeafList(YType.str, "apply-location")

                self.rule_name_xr = YLeaf(YType.str, "rule-name-xr")

                self.rule_state = YLeaf(YType.enumeration, "rule-state")

                self.timeout = YLeaf(YType.uint32, "timeout")

                self.codes = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rule_name",
                                "apply_context",
                                "apply_location",
                                "rule_name_xr",
                                "rule_state",
                                "timeout") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Correlator.Rules.Rule, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Correlator.Rules.Rule, self).__setattr__(name, value)


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(Correlator.Rules.Rule.Codes, self).__init__()

                    self.yang_name = "codes"
                    self.yang_parent_name = "rule"

                    self.category = YLeaf(YType.str, "category")

                    self.code = YLeaf(YType.str, "code")

                    self.group = YLeaf(YType.str, "group")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("category",
                                    "code",
                                    "group") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Correlator.Rules.Rule.Codes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Correlator.Rules.Rule.Codes, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.category.is_set or
                        self.code.is_set or
                        self.group.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.category.yfilter != YFilter.not_set or
                        self.code.yfilter != YFilter.not_set or
                        self.group.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "codes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.category.is_set or self.category.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.category.get_name_leafdata())
                    if (self.code.is_set or self.code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.code.get_name_leafdata())
                    if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "category" or name == "code" or name == "group"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "category"):
                        self.category = value
                        self.category.value_namespace = name_space
                        self.category.value_namespace_prefix = name_space_prefix
                    if(value_path == "code"):
                        self.code = value
                        self.code.value_namespace = name_space
                        self.code.value_namespace_prefix = name_space_prefix
                    if(value_path == "group"):
                        self.group = value
                        self.group.value_namespace = name_space
                        self.group.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.codes:
                    if (c.has_data()):
                        return True
                for leaf in self.apply_context.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.apply_location.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.rule_name.is_set or
                    self.rule_name_xr.is_set or
                    self.rule_state.is_set or
                    self.timeout.is_set)

            def has_operation(self):
                for c in self.codes:
                    if (c.has_operation()):
                        return True
                for leaf in self.apply_context.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.apply_location.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.rule_name.yfilter != YFilter.not_set or
                    self.apply_context.yfilter != YFilter.not_set or
                    self.apply_location.yfilter != YFilter.not_set or
                    self.rule_name_xr.yfilter != YFilter.not_set or
                    self.rule_state.yfilter != YFilter.not_set or
                    self.timeout.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rule" + "[rule-name='" + self.rule_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-correlator-oper:correlator/rules/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rule_name.is_set or self.rule_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_name.get_name_leafdata())
                if (self.rule_name_xr.is_set or self.rule_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_name_xr.get_name_leafdata())
                if (self.rule_state.is_set or self.rule_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_state.get_name_leafdata())
                if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout.get_name_leafdata())

                leaf_name_data.extend(self.apply_context.get_name_leafdata())

                leaf_name_data.extend(self.apply_location.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "codes"):
                    for c in self.codes:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Correlator.Rules.Rule.Codes()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.codes.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "codes" or name == "rule-name" or name == "apply-context" or name == "apply-location" or name == "rule-name-xr" or name == "rule-state" or name == "timeout"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rule-name"):
                    self.rule_name = value
                    self.rule_name.value_namespace = name_space
                    self.rule_name.value_namespace_prefix = name_space_prefix
                if(value_path == "apply-context"):
                    self.apply_context.append(value)
                if(value_path == "apply-location"):
                    self.apply_location.append(value)
                if(value_path == "rule-name-xr"):
                    self.rule_name_xr = value
                    self.rule_name_xr.value_namespace = name_space
                    self.rule_name_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "rule-state"):
                    self.rule_state = value
                    self.rule_state.value_namespace = name_space
                    self.rule_state.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout"):
                    self.timeout = value
                    self.timeout.value_namespace = name_space
                    self.timeout.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rule:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rule:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rules" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rule"):
                for c in self.rule:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Correlator.Rules.Rule()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rule.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rule"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        _revision = '2015-11-09'

        def __init__(self):
            super(Correlator.BufferStatus, self).__init__()

            self.yang_name = "buffer-status"
            self.yang_parent_name = "correlator"

            self.configured_size = YLeaf(YType.uint32, "configured-size")

            self.current_size = YLeaf(YType.uint32, "current-size")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("configured_size",
                            "current_size") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Correlator.BufferStatus, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Correlator.BufferStatus, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.configured_size.is_set or
                self.current_size.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.configured_size.yfilter != YFilter.not_set or
                self.current_size.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "buffer-status" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.configured_size.is_set or self.configured_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.configured_size.get_name_leafdata())
            if (self.current_size.is_set or self.current_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.current_size.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "configured-size" or name == "current-size"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "configured-size"):
                self.configured_size = value
                self.configured_size.value_namespace = name_space
                self.configured_size.value_namespace_prefix = name_space_prefix
            if(value_path == "current-size"):
                self.current_size = value
                self.current_size.value_namespace = name_space
                self.current_size.value_namespace_prefix = name_space_prefix


    class Alarms(Entity):
        """
        Correlated alarms Table
        
        .. attribute:: alarm
        
        	One of the correlated alarms
        	**type**\: list of    :py:class:`Alarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.Alarms.Alarm>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Correlator.Alarms, self).__init__()

            self.yang_name = "alarms"
            self.yang_parent_name = "correlator"

            self.alarm = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Correlator.Alarms, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Correlator.Alarms, self).__setattr__(name, value)


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
            _revision = '2015-11-09'

            def __init__(self):
                super(Correlator.Alarms.Alarm, self).__init__()

                self.yang_name = "alarm"
                self.yang_parent_name = "alarms"

                self.alarm_id = YLeaf(YType.int32, "alarm-id")

                self.context = YLeaf(YType.str, "context")

                self.rule_name = YLeaf(YType.str, "rule-name")

                self.alarm_info = Correlator.Alarms.Alarm.AlarmInfo()
                self.alarm_info.parent = self
                self._children_name_map["alarm_info"] = "alarm-info"
                self._children_yang_names.add("alarm-info")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("alarm_id",
                                "context",
                                "rule_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Correlator.Alarms.Alarm, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Correlator.Alarms.Alarm, self).__setattr__(name, value)


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(Correlator.Alarms.Alarm.AlarmInfo, self).__init__()

                    self.yang_name = "alarm-info"
                    self.yang_parent_name = "alarm"

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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("additional_text",
                                    "category",
                                    "code",
                                    "correlation_id",
                                    "group",
                                    "is_admin",
                                    "severity",
                                    "source_id",
                                    "state",
                                    "timestamp") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Correlator.Alarms.Alarm.AlarmInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Correlator.Alarms.Alarm.AlarmInfo, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.additional_text.is_set or
                        self.category.is_set or
                        self.code.is_set or
                        self.correlation_id.is_set or
                        self.group.is_set or
                        self.is_admin.is_set or
                        self.severity.is_set or
                        self.source_id.is_set or
                        self.state.is_set or
                        self.timestamp.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.additional_text.yfilter != YFilter.not_set or
                        self.category.yfilter != YFilter.not_set or
                        self.code.yfilter != YFilter.not_set or
                        self.correlation_id.yfilter != YFilter.not_set or
                        self.group.yfilter != YFilter.not_set or
                        self.is_admin.yfilter != YFilter.not_set or
                        self.severity.yfilter != YFilter.not_set or
                        self.source_id.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set or
                        self.timestamp.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "alarm-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.additional_text.is_set or self.additional_text.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.additional_text.get_name_leafdata())
                    if (self.category.is_set or self.category.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.category.get_name_leafdata())
                    if (self.code.is_set or self.code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.code.get_name_leafdata())
                    if (self.correlation_id.is_set or self.correlation_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.correlation_id.get_name_leafdata())
                    if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group.get_name_leafdata())
                    if (self.is_admin.is_set or self.is_admin.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_admin.get_name_leafdata())
                    if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.severity.get_name_leafdata())
                    if (self.source_id.is_set or self.source_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_id.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())
                    if (self.timestamp.is_set or self.timestamp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timestamp.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "additional-text" or name == "category" or name == "code" or name == "correlation-id" or name == "group" or name == "is-admin" or name == "severity" or name == "source-id" or name == "state" or name == "timestamp"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "additional-text"):
                        self.additional_text = value
                        self.additional_text.value_namespace = name_space
                        self.additional_text.value_namespace_prefix = name_space_prefix
                    if(value_path == "category"):
                        self.category = value
                        self.category.value_namespace = name_space
                        self.category.value_namespace_prefix = name_space_prefix
                    if(value_path == "code"):
                        self.code = value
                        self.code.value_namespace = name_space
                        self.code.value_namespace_prefix = name_space_prefix
                    if(value_path == "correlation-id"):
                        self.correlation_id = value
                        self.correlation_id.value_namespace = name_space
                        self.correlation_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "group"):
                        self.group = value
                        self.group.value_namespace = name_space
                        self.group.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-admin"):
                        self.is_admin = value
                        self.is_admin.value_namespace = name_space
                        self.is_admin.value_namespace_prefix = name_space_prefix
                    if(value_path == "severity"):
                        self.severity = value
                        self.severity.value_namespace = name_space
                        self.severity.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-id"):
                        self.source_id = value
                        self.source_id.value_namespace = name_space
                        self.source_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix
                    if(value_path == "timestamp"):
                        self.timestamp = value
                        self.timestamp.value_namespace = name_space
                        self.timestamp.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.alarm_id.is_set or
                    self.context.is_set or
                    self.rule_name.is_set or
                    (self.alarm_info is not None and self.alarm_info.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.alarm_id.yfilter != YFilter.not_set or
                    self.context.yfilter != YFilter.not_set or
                    self.rule_name.yfilter != YFilter.not_set or
                    (self.alarm_info is not None and self.alarm_info.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "alarm" + "[alarm-id='" + self.alarm_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-correlator-oper:correlator/alarms/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.alarm_id.is_set or self.alarm_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.alarm_id.get_name_leafdata())
                if (self.context.is_set or self.context.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.context.get_name_leafdata())
                if (self.rule_name.is_set or self.rule_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "alarm-info"):
                    if (self.alarm_info is None):
                        self.alarm_info = Correlator.Alarms.Alarm.AlarmInfo()
                        self.alarm_info.parent = self
                        self._children_name_map["alarm_info"] = "alarm-info"
                    return self.alarm_info

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "alarm-info" or name == "alarm-id" or name == "context" or name == "rule-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "alarm-id"):
                    self.alarm_id = value
                    self.alarm_id.value_namespace = name_space
                    self.alarm_id.value_namespace_prefix = name_space_prefix
                if(value_path == "context"):
                    self.context = value
                    self.context.value_namespace = name_space
                    self.context.value_namespace_prefix = name_space_prefix
                if(value_path == "rule-name"):
                    self.rule_name = value
                    self.rule_name.value_namespace = name_space
                    self.rule_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.alarm:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.alarm:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "alarms" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "alarm"):
                for c in self.alarm:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Correlator.Alarms.Alarm()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.alarm.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "alarm"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class RuleSetSummaries(Entity):
        """
        Table that contains the ruleset summary info
        
        .. attribute:: rule_set_summary
        
        	Summary of one of the correlation rulesets
        	**type**\: list of    :py:class:`RuleSetSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSetSummaries.RuleSetSummary>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Correlator.RuleSetSummaries, self).__init__()

            self.yang_name = "rule-set-summaries"
            self.yang_parent_name = "correlator"

            self.rule_set_summary = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Correlator.RuleSetSummaries, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Correlator.RuleSetSummaries, self).__setattr__(name, value)


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
            _revision = '2015-11-09'

            def __init__(self):
                super(Correlator.RuleSetSummaries.RuleSetSummary, self).__init__()

                self.yang_name = "rule-set-summary"
                self.yang_parent_name = "rule-set-summaries"

                self.rule_set_name = YLeaf(YType.str, "rule-set-name")

                self.rule_set_name_xr = YLeaf(YType.str, "rule-set-name-xr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rule_set_name",
                                "rule_set_name_xr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Correlator.RuleSetSummaries.RuleSetSummary, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Correlator.RuleSetSummaries.RuleSetSummary, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rule_set_name.is_set or
                    self.rule_set_name_xr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rule_set_name.yfilter != YFilter.not_set or
                    self.rule_set_name_xr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rule-set-summary" + "[rule-set-name='" + self.rule_set_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-correlator-oper:correlator/rule-set-summaries/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rule_set_name.is_set or self.rule_set_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_set_name.get_name_leafdata())
                if (self.rule_set_name_xr.is_set or self.rule_set_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_set_name_xr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rule-set-name" or name == "rule-set-name-xr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rule-set-name"):
                    self.rule_set_name = value
                    self.rule_set_name.value_namespace = name_space
                    self.rule_set_name.value_namespace_prefix = name_space_prefix
                if(value_path == "rule-set-name-xr"):
                    self.rule_set_name_xr = value
                    self.rule_set_name_xr.value_namespace = name_space
                    self.rule_set_name_xr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rule_set_summary:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rule_set_summary:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rule-set-summaries" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rule-set-summary"):
                for c in self.rule_set_summary:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Correlator.RuleSetSummaries.RuleSetSummary()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rule_set_summary.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rule-set-summary"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class RuleSetDetails(Entity):
        """
        Table that contains the ruleset detail info
        
        .. attribute:: rule_set_detail
        
        	Detail of one of the correlation rulesets
        	**type**\: list of    :py:class:`RuleSetDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper.Correlator.RuleSetDetails.RuleSetDetail>`
        
        

        """

        _prefix = 'infra-correlator-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Correlator.RuleSetDetails, self).__init__()

            self.yang_name = "rule-set-details"
            self.yang_parent_name = "correlator"

            self.rule_set_detail = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Correlator.RuleSetDetails, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Correlator.RuleSetDetails, self).__setattr__(name, value)


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
            _revision = '2015-11-09'

            def __init__(self):
                super(Correlator.RuleSetDetails.RuleSetDetail, self).__init__()

                self.yang_name = "rule-set-detail"
                self.yang_parent_name = "rule-set-details"

                self.rule_set_name = YLeaf(YType.str, "rule-set-name")

                self.rule_set_name_xr = YLeaf(YType.str, "rule-set-name-xr")

                self.rules = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rule_set_name",
                                "rule_set_name_xr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Correlator.RuleSetDetails.RuleSetDetail, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Correlator.RuleSetDetails.RuleSetDetail, self).__setattr__(name, value)


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(Correlator.RuleSetDetails.RuleSetDetail.Rules, self).__init__()

                    self.yang_name = "rules"
                    self.yang_parent_name = "rule-set-detail"

                    self.buffered_alarms_count = YLeaf(YType.uint32, "buffered-alarms-count")

                    self.rule_name_xr = YLeaf(YType.str, "rule-name-xr")

                    self.rule_state = YLeaf(YType.enumeration, "rule-state")

                    self.stateful = YLeaf(YType.boolean, "stateful")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("buffered_alarms_count",
                                    "rule_name_xr",
                                    "rule_state",
                                    "stateful") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Correlator.RuleSetDetails.RuleSetDetail.Rules, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Correlator.RuleSetDetails.RuleSetDetail.Rules, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.buffered_alarms_count.is_set or
                        self.rule_name_xr.is_set or
                        self.rule_state.is_set or
                        self.stateful.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.buffered_alarms_count.yfilter != YFilter.not_set or
                        self.rule_name_xr.yfilter != YFilter.not_set or
                        self.rule_state.yfilter != YFilter.not_set or
                        self.stateful.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rules" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.buffered_alarms_count.is_set or self.buffered_alarms_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.buffered_alarms_count.get_name_leafdata())
                    if (self.rule_name_xr.is_set or self.rule_name_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rule_name_xr.get_name_leafdata())
                    if (self.rule_state.is_set or self.rule_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rule_state.get_name_leafdata())
                    if (self.stateful.is_set or self.stateful.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.stateful.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "buffered-alarms-count" or name == "rule-name-xr" or name == "rule-state" or name == "stateful"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "buffered-alarms-count"):
                        self.buffered_alarms_count = value
                        self.buffered_alarms_count.value_namespace = name_space
                        self.buffered_alarms_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "rule-name-xr"):
                        self.rule_name_xr = value
                        self.rule_name_xr.value_namespace = name_space
                        self.rule_name_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "rule-state"):
                        self.rule_state = value
                        self.rule_state.value_namespace = name_space
                        self.rule_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "stateful"):
                        self.stateful = value
                        self.stateful.value_namespace = name_space
                        self.stateful.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.rules:
                    if (c.has_data()):
                        return True
                return (
                    self.rule_set_name.is_set or
                    self.rule_set_name_xr.is_set)

            def has_operation(self):
                for c in self.rules:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.rule_set_name.yfilter != YFilter.not_set or
                    self.rule_set_name_xr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rule-set-detail" + "[rule-set-name='" + self.rule_set_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-correlator-oper:correlator/rule-set-details/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rule_set_name.is_set or self.rule_set_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_set_name.get_name_leafdata())
                if (self.rule_set_name_xr.is_set or self.rule_set_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_set_name_xr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "rules"):
                    for c in self.rules:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Correlator.RuleSetDetails.RuleSetDetail.Rules()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.rules.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rules" or name == "rule-set-name" or name == "rule-set-name-xr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rule-set-name"):
                    self.rule_set_name = value
                    self.rule_set_name.value_namespace = name_space
                    self.rule_set_name.value_namespace_prefix = name_space_prefix
                if(value_path == "rule-set-name-xr"):
                    self.rule_set_name_xr = value
                    self.rule_set_name_xr.value_namespace = name_space
                    self.rule_set_name_xr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rule_set_detail:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rule_set_detail:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rule-set-details" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rule-set-detail"):
                for c in self.rule_set_detail:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Correlator.RuleSetDetails.RuleSetDetail()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rule_set_detail.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rule-set-detail"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class RuleDetails(Entity):
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
            super(Correlator.RuleDetails, self).__init__()

            self.yang_name = "rule-details"
            self.yang_parent_name = "correlator"

            self.rule_detail = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Correlator.RuleDetails, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Correlator.RuleDetails, self).__setattr__(name, value)


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
            _revision = '2015-11-09'

            def __init__(self):
                super(Correlator.RuleDetails.RuleDetail, self).__init__()

                self.yang_name = "rule-detail"
                self.yang_parent_name = "rule-details"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rule_name",
                                "apply_context",
                                "apply_location",
                                "context_correlation",
                                "internal",
                                "reissue_non_bistate",
                                "reparent",
                                "root_cause_timeout",
                                "timeout") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Correlator.RuleDetails.RuleDetail, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Correlator.RuleDetails.RuleDetail, self).__setattr__(name, value)


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(Correlator.RuleDetails.RuleDetail.RuleSummary, self).__init__()

                    self.yang_name = "rule-summary"
                    self.yang_parent_name = "rule-detail"

                    self.buffered_alarms_count = YLeaf(YType.uint32, "buffered-alarms-count")

                    self.rule_name_xr = YLeaf(YType.str, "rule-name-xr")

                    self.rule_state = YLeaf(YType.enumeration, "rule-state")

                    self.stateful = YLeaf(YType.boolean, "stateful")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("buffered_alarms_count",
                                    "rule_name_xr",
                                    "rule_state",
                                    "stateful") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Correlator.RuleDetails.RuleDetail.RuleSummary, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Correlator.RuleDetails.RuleDetail.RuleSummary, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.buffered_alarms_count.is_set or
                        self.rule_name_xr.is_set or
                        self.rule_state.is_set or
                        self.stateful.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.buffered_alarms_count.yfilter != YFilter.not_set or
                        self.rule_name_xr.yfilter != YFilter.not_set or
                        self.rule_state.yfilter != YFilter.not_set or
                        self.stateful.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rule-summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.buffered_alarms_count.is_set or self.buffered_alarms_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.buffered_alarms_count.get_name_leafdata())
                    if (self.rule_name_xr.is_set or self.rule_name_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rule_name_xr.get_name_leafdata())
                    if (self.rule_state.is_set or self.rule_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rule_state.get_name_leafdata())
                    if (self.stateful.is_set or self.stateful.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.stateful.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "buffered-alarms-count" or name == "rule-name-xr" or name == "rule-state" or name == "stateful"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "buffered-alarms-count"):
                        self.buffered_alarms_count = value
                        self.buffered_alarms_count.value_namespace = name_space
                        self.buffered_alarms_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "rule-name-xr"):
                        self.rule_name_xr = value
                        self.rule_name_xr.value_namespace = name_space
                        self.rule_name_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "rule-state"):
                        self.rule_state = value
                        self.rule_state.value_namespace = name_space
                        self.rule_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "stateful"):
                        self.stateful = value
                        self.stateful.value_namespace = name_space
                        self.stateful.value_namespace_prefix = name_space_prefix


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(Correlator.RuleDetails.RuleDetail.Codes, self).__init__()

                    self.yang_name = "codes"
                    self.yang_parent_name = "rule-detail"

                    self.category = YLeaf(YType.str, "category")

                    self.code = YLeaf(YType.str, "code")

                    self.group = YLeaf(YType.str, "group")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("category",
                                    "code",
                                    "group") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Correlator.RuleDetails.RuleDetail.Codes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Correlator.RuleDetails.RuleDetail.Codes, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.category.is_set or
                        self.code.is_set or
                        self.group.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.category.yfilter != YFilter.not_set or
                        self.code.yfilter != YFilter.not_set or
                        self.group.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "codes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.category.is_set or self.category.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.category.get_name_leafdata())
                    if (self.code.is_set or self.code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.code.get_name_leafdata())
                    if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "category" or name == "code" or name == "group"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "category"):
                        self.category = value
                        self.category.value_namespace = name_space
                        self.category.value_namespace_prefix = name_space_prefix
                    if(value_path == "code"):
                        self.code = value
                        self.code.value_namespace = name_space
                        self.code.value_namespace_prefix = name_space_prefix
                    if(value_path == "group"):
                        self.group = value
                        self.group.value_namespace = name_space
                        self.group.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.codes:
                    if (c.has_data()):
                        return True
                for leaf in self.apply_context.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                for leaf in self.apply_location.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.rule_name.is_set or
                    self.context_correlation.is_set or
                    self.internal.is_set or
                    self.reissue_non_bistate.is_set or
                    self.reparent.is_set or
                    self.root_cause_timeout.is_set or
                    self.timeout.is_set or
                    (self.rule_summary is not None and self.rule_summary.has_data()))

            def has_operation(self):
                for c in self.codes:
                    if (c.has_operation()):
                        return True
                for leaf in self.apply_context.getYLeafs():
                    if (leaf.is_set):
                        return True
                for leaf in self.apply_location.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.rule_name.yfilter != YFilter.not_set or
                    self.apply_context.yfilter != YFilter.not_set or
                    self.apply_location.yfilter != YFilter.not_set or
                    self.context_correlation.yfilter != YFilter.not_set or
                    self.internal.yfilter != YFilter.not_set or
                    self.reissue_non_bistate.yfilter != YFilter.not_set or
                    self.reparent.yfilter != YFilter.not_set or
                    self.root_cause_timeout.yfilter != YFilter.not_set or
                    self.timeout.yfilter != YFilter.not_set or
                    (self.rule_summary is not None and self.rule_summary.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rule-detail" + "[rule-name='" + self.rule_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-correlator-oper:correlator/rule-details/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rule_name.is_set or self.rule_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_name.get_name_leafdata())
                if (self.context_correlation.is_set or self.context_correlation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.context_correlation.get_name_leafdata())
                if (self.internal.is_set or self.internal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.internal.get_name_leafdata())
                if (self.reissue_non_bistate.is_set or self.reissue_non_bistate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.reissue_non_bistate.get_name_leafdata())
                if (self.reparent.is_set or self.reparent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.reparent.get_name_leafdata())
                if (self.root_cause_timeout.is_set or self.root_cause_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.root_cause_timeout.get_name_leafdata())
                if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout.get_name_leafdata())

                leaf_name_data.extend(self.apply_context.get_name_leafdata())

                leaf_name_data.extend(self.apply_location.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "codes"):
                    for c in self.codes:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Correlator.RuleDetails.RuleDetail.Codes()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.codes.append(c)
                    return c

                if (child_yang_name == "rule-summary"):
                    if (self.rule_summary is None):
                        self.rule_summary = Correlator.RuleDetails.RuleDetail.RuleSummary()
                        self.rule_summary.parent = self
                        self._children_name_map["rule_summary"] = "rule-summary"
                    return self.rule_summary

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "codes" or name == "rule-summary" or name == "rule-name" or name == "apply-context" or name == "apply-location" or name == "context-correlation" or name == "internal" or name == "reissue-non-bistate" or name == "reparent" or name == "root-cause-timeout" or name == "timeout"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rule-name"):
                    self.rule_name = value
                    self.rule_name.value_namespace = name_space
                    self.rule_name.value_namespace_prefix = name_space_prefix
                if(value_path == "apply-context"):
                    self.apply_context.append(value)
                if(value_path == "apply-location"):
                    self.apply_location.append(value)
                if(value_path == "context-correlation"):
                    self.context_correlation = value
                    self.context_correlation.value_namespace = name_space
                    self.context_correlation.value_namespace_prefix = name_space_prefix
                if(value_path == "internal"):
                    self.internal = value
                    self.internal.value_namespace = name_space
                    self.internal.value_namespace_prefix = name_space_prefix
                if(value_path == "reissue-non-bistate"):
                    self.reissue_non_bistate = value
                    self.reissue_non_bistate.value_namespace = name_space
                    self.reissue_non_bistate.value_namespace_prefix = name_space_prefix
                if(value_path == "reparent"):
                    self.reparent = value
                    self.reparent.value_namespace = name_space
                    self.reparent.value_namespace_prefix = name_space_prefix
                if(value_path == "root-cause-timeout"):
                    self.root_cause_timeout = value
                    self.root_cause_timeout.value_namespace = name_space
                    self.root_cause_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout"):
                    self.timeout = value
                    self.timeout.value_namespace = name_space
                    self.timeout.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rule_detail:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rule_detail:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rule-details" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rule-detail"):
                for c in self.rule_detail:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Correlator.RuleDetails.RuleDetail()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rule_detail.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rule-detail"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class RuleSummaries(Entity):
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
            super(Correlator.RuleSummaries, self).__init__()

            self.yang_name = "rule-summaries"
            self.yang_parent_name = "correlator"

            self.rule_summary = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Correlator.RuleSummaries, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Correlator.RuleSummaries, self).__setattr__(name, value)


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
            _revision = '2015-11-09'

            def __init__(self):
                super(Correlator.RuleSummaries.RuleSummary, self).__init__()

                self.yang_name = "rule-summary"
                self.yang_parent_name = "rule-summaries"

                self.rule_name = YLeaf(YType.str, "rule-name")

                self.buffered_alarms_count = YLeaf(YType.uint32, "buffered-alarms-count")

                self.rule_name_xr = YLeaf(YType.str, "rule-name-xr")

                self.rule_state = YLeaf(YType.enumeration, "rule-state")

                self.stateful = YLeaf(YType.boolean, "stateful")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rule_name",
                                "buffered_alarms_count",
                                "rule_name_xr",
                                "rule_state",
                                "stateful") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Correlator.RuleSummaries.RuleSummary, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Correlator.RuleSummaries.RuleSummary, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rule_name.is_set or
                    self.buffered_alarms_count.is_set or
                    self.rule_name_xr.is_set or
                    self.rule_state.is_set or
                    self.stateful.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rule_name.yfilter != YFilter.not_set or
                    self.buffered_alarms_count.yfilter != YFilter.not_set or
                    self.rule_name_xr.yfilter != YFilter.not_set or
                    self.rule_state.yfilter != YFilter.not_set or
                    self.stateful.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rule-summary" + "[rule-name='" + self.rule_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-correlator-oper:correlator/rule-summaries/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rule_name.is_set or self.rule_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_name.get_name_leafdata())
                if (self.buffered_alarms_count.is_set or self.buffered_alarms_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.buffered_alarms_count.get_name_leafdata())
                if (self.rule_name_xr.is_set or self.rule_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_name_xr.get_name_leafdata())
                if (self.rule_state.is_set or self.rule_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rule_state.get_name_leafdata())
                if (self.stateful.is_set or self.stateful.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stateful.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rule-name" or name == "buffered-alarms-count" or name == "rule-name-xr" or name == "rule-state" or name == "stateful"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rule-name"):
                    self.rule_name = value
                    self.rule_name.value_namespace = name_space
                    self.rule_name.value_namespace_prefix = name_space_prefix
                if(value_path == "buffered-alarms-count"):
                    self.buffered_alarms_count = value
                    self.buffered_alarms_count.value_namespace = name_space
                    self.buffered_alarms_count.value_namespace_prefix = name_space_prefix
                if(value_path == "rule-name-xr"):
                    self.rule_name_xr = value
                    self.rule_name_xr.value_namespace = name_space
                    self.rule_name_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "rule-state"):
                    self.rule_state = value
                    self.rule_state.value_namespace = name_space
                    self.rule_state.value_namespace_prefix = name_space_prefix
                if(value_path == "stateful"):
                    self.stateful = value
                    self.stateful.value_namespace = name_space
                    self.stateful.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rule_summary:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rule_summary:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rule-summaries" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-correlator-oper:correlator/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rule-summary"):
                for c in self.rule_summary:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Correlator.RuleSummaries.RuleSummary()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rule_summary.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rule-summary"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.alarms is not None and self.alarms.has_data()) or
            (self.buffer_status is not None and self.buffer_status.has_data()) or
            (self.rule_details is not None and self.rule_details.has_data()) or
            (self.rule_set_details is not None and self.rule_set_details.has_data()) or
            (self.rule_set_summaries is not None and self.rule_set_summaries.has_data()) or
            (self.rule_summaries is not None and self.rule_summaries.has_data()) or
            (self.rules is not None and self.rules.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.alarms is not None and self.alarms.has_operation()) or
            (self.buffer_status is not None and self.buffer_status.has_operation()) or
            (self.rule_details is not None and self.rule_details.has_operation()) or
            (self.rule_set_details is not None and self.rule_set_details.has_operation()) or
            (self.rule_set_summaries is not None and self.rule_set_summaries.has_operation()) or
            (self.rule_summaries is not None and self.rule_summaries.has_operation()) or
            (self.rules is not None and self.rules.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-correlator-oper:correlator" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "alarms"):
            if (self.alarms is None):
                self.alarms = Correlator.Alarms()
                self.alarms.parent = self
                self._children_name_map["alarms"] = "alarms"
            return self.alarms

        if (child_yang_name == "buffer-status"):
            if (self.buffer_status is None):
                self.buffer_status = Correlator.BufferStatus()
                self.buffer_status.parent = self
                self._children_name_map["buffer_status"] = "buffer-status"
            return self.buffer_status

        if (child_yang_name == "rule-details"):
            if (self.rule_details is None):
                self.rule_details = Correlator.RuleDetails()
                self.rule_details.parent = self
                self._children_name_map["rule_details"] = "rule-details"
            return self.rule_details

        if (child_yang_name == "rule-set-details"):
            if (self.rule_set_details is None):
                self.rule_set_details = Correlator.RuleSetDetails()
                self.rule_set_details.parent = self
                self._children_name_map["rule_set_details"] = "rule-set-details"
            return self.rule_set_details

        if (child_yang_name == "rule-set-summaries"):
            if (self.rule_set_summaries is None):
                self.rule_set_summaries = Correlator.RuleSetSummaries()
                self.rule_set_summaries.parent = self
                self._children_name_map["rule_set_summaries"] = "rule-set-summaries"
            return self.rule_set_summaries

        if (child_yang_name == "rule-summaries"):
            if (self.rule_summaries is None):
                self.rule_summaries = Correlator.RuleSummaries()
                self.rule_summaries.parent = self
                self._children_name_map["rule_summaries"] = "rule-summaries"
            return self.rule_summaries

        if (child_yang_name == "rules"):
            if (self.rules is None):
                self.rules = Correlator.Rules()
                self.rules.parent = self
                self._children_name_map["rules"] = "rules"
            return self.rules

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "alarms" or name == "buffer-status" or name == "rule-details" or name == "rule-set-details" or name == "rule-set-summaries" or name == "rule-summaries" or name == "rules"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Correlator()
        return self._top_entity

