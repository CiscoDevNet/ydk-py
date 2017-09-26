""" ietf_diffserv_policy 

This module contains a collection of YANG definitions for
configuring diffserv specification implementations.

Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC XXXX; see
the RFC itself for full legal notices.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ActionType(Identity):
    """
    This base identity type defines action\-types
    
    

    """

    _prefix = 'policy'
    _revision = '2015-04-07'

    def __init__(self):
        super(ActionType, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-policy", "ietf-diffserv-policy", "ietf-diffserv-policy:action-type")


class Policies(Entity):
    """
    list of policy templates
    
    .. attribute:: policy_entry
    
    	policy template
    	**type**\: list of    :py:class:`PolicyEntry <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry>`
    
    

    """

    _prefix = 'policy'
    _revision = '2015-04-07'

    def __init__(self):
        super(Policies, self).__init__()
        self._top_entity = None

        self.yang_name = "policies"
        self.yang_parent_name = "ietf-diffserv-policy"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"policy-entry" : ("policy_entry", Policies.PolicyEntry)}

        self.policy_entry = YList(self)
        self._segment_path = lambda: "ietf-diffserv-policy:policies"

    def __setattr__(self, name, value):
        self._perform_setattr(Policies, [], name, value)


    class PolicyEntry(Entity):
        """
        policy template
        
        .. attribute:: policy_name  <key>
        
        	Diffserv policy name
        	**type**\:  str
        
        .. attribute:: classifier_entry
        
        	Classifier entry configuration in a policy
        	**type**\: list of    :py:class:`ClassifierEntry <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry>`
        
        .. attribute:: policy_descr
        
        	Diffserv policy description
        	**type**\:  str
        
        

        """

        _prefix = 'policy'
        _revision = '2015-04-07'

        def __init__(self):
            super(Policies.PolicyEntry, self).__init__()

            self.yang_name = "policy-entry"
            self.yang_parent_name = "policies"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"classifier-entry" : ("classifier_entry", Policies.PolicyEntry.ClassifierEntry)}

            self.policy_name = YLeaf(YType.str, "policy-name")

            self.policy_descr = YLeaf(YType.str, "policy-descr")

            self.classifier_entry = YList(self)
            self._segment_path = lambda: "policy-entry" + "[policy-name='" + self.policy_name.get() + "']"
            self._absolute_path = lambda: "ietf-diffserv-policy:policies/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Policies.PolicyEntry, ['policy_name', 'policy_descr'], name, value)


        class ClassifierEntry(Entity):
            """
            Classifier entry configuration in a policy
            
            .. attribute:: classifier_entry_name  <key>
            
            	Diffserv classifier entry name
            	**type**\:  str
            
            .. attribute:: classifier_action_entry_cfg
            
            	Configuration of classifier & associated actions
            	**type**\: list of    :py:class:`ClassifierActionEntryCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg>`
            
            .. attribute:: classifier_entry_filter_oper
            
            	Filters are applicable as any or all filters
            	**type**\:   :py:class:`ClassifierEntryFilterOperationType <ydk.models.ietf.ietf_diffserv_classifier.ClassifierEntryFilterOperationType>`
            
            	**default value**\: match-any-filter
            
            .. attribute:: classifier_entry_inline
            
            	Indication of inline classifier entry
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: filter_entry
            
            	Filters configured inline in a policy
            	**type**\: list of    :py:class:`FilterEntry <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry>`
            
            

            """

            _prefix = 'policy'
            _revision = '2015-04-07'

            def __init__(self):
                super(Policies.PolicyEntry.ClassifierEntry, self).__init__()

                self.yang_name = "classifier-entry"
                self.yang_parent_name = "policy-entry"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"classifier-action-entry-cfg" : ("classifier_action_entry_cfg", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg), "filter-entry" : ("filter_entry", Policies.PolicyEntry.ClassifierEntry.FilterEntry)}

                self.classifier_entry_name = YLeaf(YType.str, "classifier-entry-name")

                self.classifier_entry_filter_oper = YLeaf(YType.identityref, "classifier-entry-filter-oper")

                self.classifier_entry_inline = YLeaf(YType.boolean, "classifier-entry-inline")

                self.classifier_action_entry_cfg = YList(self)
                self.filter_entry = YList(self)
                self._segment_path = lambda: "classifier-entry" + "[classifier-entry-name='" + self.classifier_entry_name.get() + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(Policies.PolicyEntry.ClassifierEntry, ['classifier_entry_name', 'classifier_entry_filter_oper', 'classifier_entry_inline'], name, value)


            class ClassifierActionEntryCfg(Entity):
                """
                Configuration of classifier & associated actions
                
                .. attribute:: action_type  <key>
                
                	This defines action type 
                	**type**\:   :py:class:`ActionType <ydk.models.ietf.ietf_diffserv_policy.ActionType>`
                
                .. attribute:: drop_cfg
                
                	Always Drop configuration container
                	**type**\:   :py:class:`DropCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.DropCfg>`
                
                .. attribute:: marking_cfg
                
                	Marking configuration container
                	**type**\:   :py:class:`MarkingCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MarkingCfg>`
                
                .. attribute:: max_rate_cfg
                
                	maximum rate attributes
                	**type**\:   :py:class:`MaxRateCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MaxRateCfg>`
                
                .. attribute:: meter_cfg
                
                	Meter list configuration container
                	**type**\:   :py:class:`MeterCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg>`
                
                .. attribute:: min_rate_cfg
                
                	min guaranteed bandwidth
                	**type**\:   :py:class:`MinRateCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg>`
                
                .. attribute:: priority_cfg
                
                	priority attributes container
                	**type**\:   :py:class:`PriorityCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg>`
                
                .. attribute:: random_detect_cfg
                
                	Random Detect configuration container
                	**type**\:   :py:class:`RandomDetectCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg>`
                
                .. attribute:: tail_drop_cfg
                
                	Tail Drop configuration container
                	**type**\:   :py:class:`TailDropCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg>`
                
                

                """

                _prefix = 'policy'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg, self).__init__()

                    self.yang_name = "classifier-action-entry-cfg"
                    self.yang_parent_name = "classifier-entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"drop-cfg" : ("drop_cfg", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.DropCfg), "marking-cfg" : ("marking_cfg", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MarkingCfg), "max-rate-cfg" : ("max_rate_cfg", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MaxRateCfg), "meter-cfg" : ("meter_cfg", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg), "min-rate-cfg" : ("min_rate_cfg", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg), "priority-cfg" : ("priority_cfg", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg), "random-detect-cfg" : ("random_detect_cfg", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg), "tail-drop-cfg" : ("tail_drop_cfg", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg)}
                    self._child_list_classes = {}

                    self.action_type = YLeaf(YType.identityref, "action-type")

                    self.drop_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.DropCfg()
                    self.drop_cfg.parent = self
                    self._children_name_map["drop_cfg"] = "drop-cfg"
                    self._children_yang_names.add("drop-cfg")

                    self.marking_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MarkingCfg()
                    self.marking_cfg.parent = self
                    self._children_name_map["marking_cfg"] = "marking-cfg"
                    self._children_yang_names.add("marking-cfg")

                    self.max_rate_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MaxRateCfg()
                    self.max_rate_cfg.parent = self
                    self._children_name_map["max_rate_cfg"] = "max-rate-cfg"
                    self._children_yang_names.add("max-rate-cfg")

                    self.meter_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg()
                    self.meter_cfg.parent = self
                    self._children_name_map["meter_cfg"] = "meter-cfg"
                    self._children_yang_names.add("meter-cfg")

                    self.min_rate_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg()
                    self.min_rate_cfg.parent = self
                    self._children_name_map["min_rate_cfg"] = "min-rate-cfg"
                    self._children_yang_names.add("min-rate-cfg")

                    self.priority_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg()
                    self.priority_cfg.parent = self
                    self._children_name_map["priority_cfg"] = "priority-cfg"
                    self._children_yang_names.add("priority-cfg")

                    self.random_detect_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg()
                    self.random_detect_cfg.parent = self
                    self._children_name_map["random_detect_cfg"] = "random-detect-cfg"
                    self._children_yang_names.add("random-detect-cfg")

                    self.tail_drop_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg()
                    self.tail_drop_cfg.parent = self
                    self._children_name_map["tail_drop_cfg"] = "tail-drop-cfg"
                    self._children_yang_names.add("tail-drop-cfg")
                    self._segment_path = lambda: "classifier-action-entry-cfg" + "[action-type='" + self.action_type.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg, ['action_type'], name, value)


                class DropCfg(Entity):
                    """
                    Always Drop configuration container
                    
                    .. attribute:: drop_action
                    
                    	always drop algorithm
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.DropCfg, self).__init__()

                        self.yang_name = "drop-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.drop_action = YLeaf(YType.empty, "drop-action")
                        self._segment_path = lambda: "ietf-diffserv-action:drop-cfg"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.DropCfg, ['drop_action'], name, value)


                class MarkingCfg(Entity):
                    """
                    Marking configuration container
                    
                    .. attribute:: dscp
                    
                    	dscp marking
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MarkingCfg, self).__init__()

                        self.yang_name = "marking-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.dscp = YLeaf(YType.uint8, "dscp")
                        self._segment_path = lambda: "ietf-diffserv-action:marking-cfg"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MarkingCfg, ['dscp'], name, value)


                class MaxRateCfg(Entity):
                    """
                    maximum rate attributes
                    
                    .. attribute:: absolute_rate
                    
                    	rate in bits per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bits-per-second
                    
                    .. attribute:: absolute_rate_metric
                    
                    	Metric
                    	**type**\:   :py:class:`Metric <ydk.models.ietf.policy_types.Metric>`
                    
                    	**default value**\: none
                    
                    .. attribute:: absolute_rate_units
                    
                    	Rate basic units
                    	**type**\:   :py:class:`RateUnit <ydk.models.ietf.policy_types.RateUnit>`
                    
                    .. attribute:: burst_interval
                    
                    	burst interval
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: microsecond
                    
                    .. attribute:: burst_size
                    
                    	burst size
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bytes
                    
                    .. attribute:: rate_percent
                    
                    	percent
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    .. attribute:: rate_ratio
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 1..65532
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MaxRateCfg, self).__init__()

                        self.yang_name = "max-rate-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.absolute_rate = YLeaf(YType.uint64, "absolute-rate")

                        self.absolute_rate_metric = YLeaf(YType.enumeration, "absolute-rate-metric")

                        self.absolute_rate_units = YLeaf(YType.enumeration, "absolute-rate-units")

                        self.burst_interval = YLeaf(YType.uint64, "burst-interval")

                        self.burst_size = YLeaf(YType.uint64, "burst-size")

                        self.rate_percent = YLeaf(YType.uint8, "rate-percent")

                        self.rate_ratio = YLeaf(YType.uint32, "rate-ratio")
                        self._segment_path = lambda: "ietf-diffserv-action:max-rate-cfg"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MaxRateCfg, ['absolute_rate', 'absolute_rate_metric', 'absolute_rate_units', 'burst_interval', 'burst_size', 'rate_percent', 'rate_ratio'], name, value)


                class MeterCfg(Entity):
                    """
                    Meter list configuration container
                    
                    .. attribute:: meter_list
                    
                    	Meter configuration
                    	**type**\: list of    :py:class:`MeterList <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg, self).__init__()

                        self.yang_name = "meter-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"meter-list" : ("meter_list", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList)}

                        self.meter_list = YList(self)
                        self._segment_path = lambda: "ietf-diffserv-action:meter-cfg"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg, [], name, value)


                    class MeterList(Entity):
                        """
                        Meter configuration
                        
                        .. attribute:: meter_id  <key>
                        
                        	meter identifier
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: burst_interval
                        
                        	burst interval
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: microsecond
                        
                        .. attribute:: burst_size
                        
                        	burst size
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bytes
                        
                        .. attribute:: color
                        
                        	color aware & color blind attributes container
                        	**type**\:   :py:class:`Color <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.Color>`
                        
                        .. attribute:: fail_action
                        
                        	exceed action
                        	**type**\:   :py:class:`FailAction <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.FailAction>`
                        
                        .. attribute:: meter_rate
                        
                        	meter rate
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bits-per-second
                        
                        .. attribute:: succeed_action
                        
                        	confirm action
                        	**type**\:   :py:class:`SucceedAction <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.SucceedAction>`
                        
                        

                        """

                        _prefix = 'action'
                        _revision = '2015-04-07'

                        def __init__(self):
                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList, self).__init__()

                            self.yang_name = "meter-list"
                            self.yang_parent_name = "meter-cfg"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"color" : ("color", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.Color), "fail-action" : ("fail_action", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.FailAction), "succeed-action" : ("succeed_action", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.SucceedAction)}
                            self._child_list_classes = {}

                            self.meter_id = YLeaf(YType.uint16, "meter-id")

                            self.burst_interval = YLeaf(YType.uint64, "burst-interval")

                            self.burst_size = YLeaf(YType.uint64, "burst-size")

                            self.meter_rate = YLeaf(YType.uint64, "meter-rate")

                            self.color = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.Color()
                            self.color.parent = self
                            self._children_name_map["color"] = "color"
                            self._children_yang_names.add("color")

                            self.fail_action = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.FailAction()
                            self.fail_action.parent = self
                            self._children_name_map["fail_action"] = "fail-action"
                            self._children_yang_names.add("fail-action")

                            self.succeed_action = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.SucceedAction()
                            self.succeed_action.parent = self
                            self._children_name_map["succeed_action"] = "succeed-action"
                            self._children_yang_names.add("succeed-action")
                            self._segment_path = lambda: "meter-list" + "[meter-id='" + self.meter_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList, ['meter_id', 'burst_interval', 'burst_size', 'meter_rate'], name, value)


                        class Color(Entity):
                            """
                            color aware & color blind attributes container
                            
                            .. attribute:: classifier_entry_descr
                            
                            	Description of the class template
                            	**type**\:  str
                            
                            .. attribute:: classifier_entry_filter_operation
                            
                            	Filters are applicable as any or all filters
                            	**type**\:   :py:class:`ClassifierEntryFilterOperationType <ydk.models.ietf.ietf_diffserv_classifier.ClassifierEntryFilterOperationType>`
                            
                            	**default value**\: match-any-filter
                            
                            .. attribute:: classifier_entry_name
                            
                            	Diffserv classifier name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'action'
                            _revision = '2015-04-07'

                            def __init__(self):
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.Color, self).__init__()

                                self.yang_name = "color"
                                self.yang_parent_name = "meter-list"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.classifier_entry_descr = YLeaf(YType.str, "classifier-entry-descr")

                                self.classifier_entry_filter_operation = YLeaf(YType.identityref, "classifier-entry-filter-operation")

                                self.classifier_entry_name = YLeaf(YType.str, "classifier-entry-name")
                                self._segment_path = lambda: "color"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.Color, ['classifier_entry_descr', 'classifier_entry_filter_operation', 'classifier_entry_name'], name, value)


                        class FailAction(Entity):
                            """
                            exceed action
                            
                            .. attribute:: drop_action
                            
                            	always drop algorithm
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: dscp
                            
                            	dscp marking
                            	**type**\:  int
                            
                            	**range:** 0..63
                            
                            .. attribute:: meter_action_type
                            
                            	meter action type
                            	**type**\:   :py:class:`MeterActionType <ydk.models.ietf.ietf_diffserv_action.MeterActionType>`
                            
                            .. attribute:: next_meter_id
                            
                            	next meter identifier
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'action'
                            _revision = '2015-04-07'

                            def __init__(self):
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.FailAction, self).__init__()

                                self.yang_name = "fail-action"
                                self.yang_parent_name = "meter-list"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.drop_action = YLeaf(YType.empty, "drop-action")

                                self.dscp = YLeaf(YType.uint8, "dscp")

                                self.meter_action_type = YLeaf(YType.identityref, "meter-action-type")

                                self.next_meter_id = YLeaf(YType.uint16, "next-meter-id")
                                self._segment_path = lambda: "fail-action"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.FailAction, ['drop_action', 'dscp', 'meter_action_type', 'next_meter_id'], name, value)


                        class SucceedAction(Entity):
                            """
                            confirm action
                            
                            .. attribute:: drop_action
                            
                            	always drop algorithm
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: dscp
                            
                            	dscp marking
                            	**type**\:  int
                            
                            	**range:** 0..63
                            
                            .. attribute:: meter_action_type
                            
                            	meter action type
                            	**type**\:   :py:class:`MeterActionType <ydk.models.ietf.ietf_diffserv_action.MeterActionType>`
                            
                            .. attribute:: next_meter_id
                            
                            	next meter identifier
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'action'
                            _revision = '2015-04-07'

                            def __init__(self):
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.SucceedAction, self).__init__()

                                self.yang_name = "succeed-action"
                                self.yang_parent_name = "meter-list"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.drop_action = YLeaf(YType.empty, "drop-action")

                                self.dscp = YLeaf(YType.uint8, "dscp")

                                self.meter_action_type = YLeaf(YType.identityref, "meter-action-type")

                                self.next_meter_id = YLeaf(YType.uint16, "next-meter-id")
                                self._segment_path = lambda: "succeed-action"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MeterCfg.MeterList.SucceedAction, ['drop_action', 'dscp', 'meter_action_type', 'next_meter_id'], name, value)


                class MinRateCfg(Entity):
                    """
                    min guaranteed bandwidth
                    
                    .. attribute:: absolute_rate_metric
                    
                    	Metric
                    	**type**\:   :py:class:`Metric <ydk.models.ietf.policy_types.Metric>`
                    
                    	**default value**\: none
                    
                    .. attribute:: absolute_rate_units
                    
                    	Rate basic units
                    	**type**\:   :py:class:`RateUnit <ydk.models.ietf.policy_types.RateUnit>`
                    
                    .. attribute:: bw_excess_share_cfg
                    
                    	share the bandwidth remaming
                    	**type**\:   :py:class:`BwExcessShareCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg.BwExcessShareCfg>`
                    
                    .. attribute:: min_rate
                    
                    	minimum rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bits-per-second
                    
                    .. attribute:: rate_percent
                    
                    	percent
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    .. attribute:: rate_ratio
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 1..65532
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg, self).__init__()

                        self.yang_name = "min-rate-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"bw-excess-share-cfg" : ("bw_excess_share_cfg", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg.BwExcessShareCfg)}
                        self._child_list_classes = {}

                        self.absolute_rate_metric = YLeaf(YType.enumeration, "absolute-rate-metric")

                        self.absolute_rate_units = YLeaf(YType.enumeration, "absolute-rate-units")

                        self.min_rate = YLeaf(YType.uint64, "min-rate")

                        self.rate_percent = YLeaf(YType.uint8, "rate-percent")

                        self.rate_ratio = YLeaf(YType.uint32, "rate-ratio")

                        self.bw_excess_share_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg.BwExcessShareCfg()
                        self.bw_excess_share_cfg.parent = self
                        self._children_name_map["bw_excess_share_cfg"] = "bw-excess-share-cfg"
                        self._children_yang_names.add("bw-excess-share-cfg")
                        self._segment_path = lambda: "ietf-diffserv-action:min-rate-cfg"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg, ['absolute_rate_metric', 'absolute_rate_units', 'min_rate', 'rate_percent', 'rate_ratio'], name, value)


                    class BwExcessShareCfg(Entity):
                        """
                        share the bandwidth remaming
                        
                        .. attribute:: absolute_rate_metric
                        
                        	Metric
                        	**type**\:   :py:class:`Metric <ydk.models.ietf.policy_types.Metric>`
                        
                        	**default value**\: none
                        
                        .. attribute:: absolute_rate_units
                        
                        	Rate basic units
                        	**type**\:   :py:class:`RateUnit <ydk.models.ietf.policy_types.RateUnit>`
                        
                        .. attribute:: rate_percent
                        
                        	percent
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: rate_ratio
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 1..65532
                        
                        .. attribute:: value
                        
                        	percentage or ratio value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'action'
                        _revision = '2015-04-07'

                        def __init__(self):
                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg.BwExcessShareCfg, self).__init__()

                            self.yang_name = "bw-excess-share-cfg"
                            self.yang_parent_name = "min-rate-cfg"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.absolute_rate_metric = YLeaf(YType.enumeration, "absolute-rate-metric")

                            self.absolute_rate_units = YLeaf(YType.enumeration, "absolute-rate-units")

                            self.rate_percent = YLeaf(YType.uint8, "rate-percent")

                            self.rate_ratio = YLeaf(YType.uint32, "rate-ratio")

                            self.value = YLeaf(YType.uint32, "value")
                            self._segment_path = lambda: "bw-excess-share-cfg"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.MinRateCfg.BwExcessShareCfg, ['absolute_rate_metric', 'absolute_rate_units', 'rate_percent', 'rate_ratio', 'value'], name, value)


                class PriorityCfg(Entity):
                    """
                    priority attributes container
                    
                    .. attribute:: priority_level
                    
                    	priority level
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rate_burst
                    
                    	absolute priority rate with/without burst rateand absolute percent
                    	**type**\:   :py:class:`RateBurst <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg.RateBurst>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg, self).__init__()

                        self.yang_name = "priority-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"rate-burst" : ("rate_burst", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg.RateBurst)}
                        self._child_list_classes = {}

                        self.priority_level = YLeaf(YType.uint8, "priority-level")

                        self.rate_burst = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg.RateBurst()
                        self.rate_burst.parent = self
                        self._children_name_map["rate_burst"] = "rate-burst"
                        self._children_yang_names.add("rate-burst")
                        self._segment_path = lambda: "ietf-diffserv-action:priority-cfg"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg, ['priority_level'], name, value)


                    class RateBurst(Entity):
                        """
                        absolute priority rate with/without burst rateand absolute percent
                        
                        .. attribute:: absolute_rate_metric
                        
                        	Metric
                        	**type**\:   :py:class:`Metric <ydk.models.ietf.policy_types.Metric>`
                        
                        	**default value**\: none
                        
                        .. attribute:: absolute_rate_units
                        
                        	Rate basic units
                        	**type**\:   :py:class:`RateUnit <ydk.models.ietf.policy_types.RateUnit>`
                        
                        .. attribute:: burst_interval
                        
                        	burst interval
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: microsecond
                        
                        .. attribute:: burst_size
                        
                        	burst size
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bytes
                        
                        .. attribute:: rate
                        
                        	Rate value
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bits-per-second
                        
                        .. attribute:: rate_percent
                        
                        	percent
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: rate_ratio
                        
                        	
                        	**type**\:  int
                        
                        	**range:** 1..65532
                        
                        

                        """

                        _prefix = 'action'
                        _revision = '2015-04-07'

                        def __init__(self):
                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg.RateBurst, self).__init__()

                            self.yang_name = "rate-burst"
                            self.yang_parent_name = "priority-cfg"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.absolute_rate_metric = YLeaf(YType.enumeration, "absolute-rate-metric")

                            self.absolute_rate_units = YLeaf(YType.enumeration, "absolute-rate-units")

                            self.burst_interval = YLeaf(YType.uint64, "burst-interval")

                            self.burst_size = YLeaf(YType.uint64, "burst-size")

                            self.rate = YLeaf(YType.uint64, "rate")

                            self.rate_percent = YLeaf(YType.uint8, "rate-percent")

                            self.rate_ratio = YLeaf(YType.uint32, "rate-ratio")
                            self._segment_path = lambda: "rate-burst"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.PriorityCfg.RateBurst, ['absolute_rate_metric', 'absolute_rate_units', 'burst_interval', 'burst_size', 'rate', 'rate_percent', 'rate_ratio'], name, value)


                class RandomDetectCfg(Entity):
                    """
                    Random Detect configuration container
                    
                    .. attribute:: exp_weighting_const
                    
                    	Exponential weighting constant factor for red profile 
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mark_probability
                    
                    	Mark probability
                    	**type**\:  int
                    
                    	**range:** 1..1000
                    
                    .. attribute:: red_max_thresh
                    
                    	Maximum threshold
                    	**type**\:   :py:class:`RedMaxThresh <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh>`
                    
                    .. attribute:: red_min_thresh
                    
                    	Minimum threshold
                    	**type**\:   :py:class:`RedMinThresh <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg, self).__init__()

                        self.yang_name = "random-detect-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"red-max-thresh" : ("red_max_thresh", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh), "red-min-thresh" : ("red_min_thresh", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh)}
                        self._child_list_classes = {}

                        self.exp_weighting_const = YLeaf(YType.uint32, "exp-weighting-const")

                        self.mark_probability = YLeaf(YType.uint32, "mark-probability")

                        self.red_max_thresh = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh()
                        self.red_max_thresh.parent = self
                        self._children_name_map["red_max_thresh"] = "red-max-thresh"
                        self._children_yang_names.add("red-max-thresh")

                        self.red_min_thresh = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh()
                        self.red_min_thresh.parent = self
                        self._children_name_map["red_min_thresh"] = "red-min-thresh"
                        self._children_yang_names.add("red-min-thresh")
                        self._segment_path = lambda: "ietf-diffserv-action:random-detect-cfg"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg, ['exp_weighting_const', 'mark_probability'], name, value)


                    class RedMaxThresh(Entity):
                        """
                        Maximum threshold
                        
                        .. attribute:: threshold
                        
                        	threshold
                        	**type**\:   :py:class:`Threshold <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh.Threshold>`
                        
                        

                        """

                        _prefix = 'action'
                        _revision = '2015-04-07'

                        def __init__(self):
                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh, self).__init__()

                            self.yang_name = "red-max-thresh"
                            self.yang_parent_name = "random-detect-cfg"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"threshold" : ("threshold", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh.Threshold)}
                            self._child_list_classes = {}

                            self.threshold = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh.Threshold()
                            self.threshold.parent = self
                            self._children_name_map["threshold"] = "threshold"
                            self._children_yang_names.add("threshold")
                            self._segment_path = lambda: "red-max-thresh"


                        class Threshold(Entity):
                            """
                            threshold
                            
                            .. attribute:: threshold_interval
                            
                            	Threshold interval
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: microsecond
                            
                            .. attribute:: threshold_size
                            
                            	Threshold size
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: bytes
                            
                            

                            """

                            _prefix = 'action'
                            _revision = '2015-04-07'

                            def __init__(self):
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh.Threshold, self).__init__()

                                self.yang_name = "threshold"
                                self.yang_parent_name = "red-max-thresh"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.threshold_interval = YLeaf(YType.uint64, "threshold-interval")

                                self.threshold_size = YLeaf(YType.uint64, "threshold-size")
                                self._segment_path = lambda: "threshold"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMaxThresh.Threshold, ['threshold_interval', 'threshold_size'], name, value)


                    class RedMinThresh(Entity):
                        """
                        Minimum threshold
                        
                        .. attribute:: threshold
                        
                        	threshold
                        	**type**\:   :py:class:`Threshold <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh.Threshold>`
                        
                        

                        """

                        _prefix = 'action'
                        _revision = '2015-04-07'

                        def __init__(self):
                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh, self).__init__()

                            self.yang_name = "red-min-thresh"
                            self.yang_parent_name = "random-detect-cfg"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"threshold" : ("threshold", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh.Threshold)}
                            self._child_list_classes = {}

                            self.threshold = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh.Threshold()
                            self.threshold.parent = self
                            self._children_name_map["threshold"] = "threshold"
                            self._children_yang_names.add("threshold")
                            self._segment_path = lambda: "red-min-thresh"


                        class Threshold(Entity):
                            """
                            threshold
                            
                            .. attribute:: threshold_interval
                            
                            	Threshold interval
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: microsecond
                            
                            .. attribute:: threshold_size
                            
                            	Threshold size
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: bytes
                            
                            

                            """

                            _prefix = 'action'
                            _revision = '2015-04-07'

                            def __init__(self):
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh.Threshold, self).__init__()

                                self.yang_name = "threshold"
                                self.yang_parent_name = "red-min-thresh"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.threshold_interval = YLeaf(YType.uint64, "threshold-interval")

                                self.threshold_size = YLeaf(YType.uint64, "threshold-size")
                                self._segment_path = lambda: "threshold"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.RandomDetectCfg.RedMinThresh.Threshold, ['threshold_interval', 'threshold_size'], name, value)


                class TailDropCfg(Entity):
                    """
                    Tail Drop configuration container
                    
                    .. attribute:: qlimit_dscp_thresh
                    
                    	the queue limit per dscp range
                    	**type**\: list of    :py:class:`QlimitDscpThresh <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh>`
                    
                    

                    """

                    _prefix = 'action'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg, self).__init__()

                        self.yang_name = "tail-drop-cfg"
                        self.yang_parent_name = "classifier-action-entry-cfg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"qlimit-dscp-thresh" : ("qlimit_dscp_thresh", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh)}

                        self.qlimit_dscp_thresh = YList(self)
                        self._segment_path = lambda: "ietf-diffserv-action:tail-drop-cfg"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg, [], name, value)


                    class QlimitDscpThresh(Entity):
                        """
                        the queue limit per dscp range
                        
                        .. attribute:: dscp_min  <key>
                        
                        	Minimum of dscp range
                        	**type**\:  int
                        
                        	**range:** 0..63
                        
                        .. attribute:: dscp_max  <key>
                        
                        	Maximum of dscp range
                        	**type**\:  int
                        
                        	**range:** 0..63
                        
                        .. attribute:: threshold
                        
                        	threshold
                        	**type**\:   :py:class:`Threshold <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh.Threshold>`
                        
                        

                        """

                        _prefix = 'action'
                        _revision = '2015-04-07'

                        def __init__(self):
                            super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh, self).__init__()

                            self.yang_name = "qlimit-dscp-thresh"
                            self.yang_parent_name = "tail-drop-cfg"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"threshold" : ("threshold", Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh.Threshold)}
                            self._child_list_classes = {}

                            self.dscp_min = YLeaf(YType.uint8, "dscp-min")

                            self.dscp_max = YLeaf(YType.uint8, "dscp-max")

                            self.threshold = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh.Threshold()
                            self.threshold.parent = self
                            self._children_name_map["threshold"] = "threshold"
                            self._children_yang_names.add("threshold")
                            self._segment_path = lambda: "qlimit-dscp-thresh" + "[dscp-min='" + self.dscp_min.get() + "']" + "[dscp-max='" + self.dscp_max.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh, ['dscp_min', 'dscp_max'], name, value)


                        class Threshold(Entity):
                            """
                            threshold
                            
                            .. attribute:: threshold_interval
                            
                            	Threshold interval
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: microsecond
                            
                            .. attribute:: threshold_size
                            
                            	Threshold size
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: bytes
                            
                            

                            """

                            _prefix = 'action'
                            _revision = '2015-04-07'

                            def __init__(self):
                                super(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh.Threshold, self).__init__()

                                self.yang_name = "threshold"
                                self.yang_parent_name = "qlimit-dscp-thresh"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.threshold_interval = YLeaf(YType.uint64, "threshold-interval")

                                self.threshold_size = YLeaf(YType.uint64, "threshold-size")
                                self._segment_path = lambda: "threshold"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.TailDropCfg.QlimitDscpThresh.Threshold, ['threshold_interval', 'threshold_size'], name, value)


            class FilterEntry(Entity):
                """
                Filters configured inline in a policy
                
                .. attribute:: filter_type  <key>
                
                	This leaf defines type of the filter
                	**type**\:   :py:class:`FilterType <ydk.models.ietf.ietf_diffserv_classifier.FilterType>`
                
                .. attribute:: filter_logical_not  <key>
                
                	 This is logical\-not operator for a filter. When true, it  indicates filter looks for absence of a pattern defined  by the filter 
                	**type**\:  bool
                
                .. attribute:: destination_ip_address_cfg
                
                	list of destination ip address
                	**type**\: list of    :py:class:`DestinationIpAddressCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg>`
                
                .. attribute:: destination_port_cfg
                
                	list of ranges of destination port
                	**type**\: list of    :py:class:`DestinationPortCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg>`
                
                .. attribute:: dscp_cfg
                
                	list of dscp ranges
                	**type**\: list of    :py:class:`DscpCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg>`
                
                .. attribute:: protocol_cfg
                
                	list of ranges of protocol values
                	**type**\: list of    :py:class:`ProtocolCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg>`
                
                .. attribute:: source_ip_address_cfg
                
                	list of source ip address
                	**type**\: list of    :py:class:`SourceIpAddressCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg>`
                
                .. attribute:: source_port_cfg
                
                	list of ranges of source port
                	**type**\: list of    :py:class:`SourcePortCfg <ydk.models.ietf.ietf_diffserv_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg>`
                
                

                """

                _prefix = 'policy'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Policies.PolicyEntry.ClassifierEntry.FilterEntry, self).__init__()

                    self.yang_name = "filter-entry"
                    self.yang_parent_name = "classifier-entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"destination-ip-address-cfg" : ("destination_ip_address_cfg", Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg), "destination-port-cfg" : ("destination_port_cfg", Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg), "dscp-cfg" : ("dscp_cfg", Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg), "protocol-cfg" : ("protocol_cfg", Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg), "source-ip-address-cfg" : ("source_ip_address_cfg", Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg), "source-port-cfg" : ("source_port_cfg", Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg)}

                    self.filter_type = YLeaf(YType.identityref, "filter-type")

                    self.filter_logical_not = YLeaf(YType.boolean, "filter-logical-not")

                    self.destination_ip_address_cfg = YList(self)
                    self.destination_port_cfg = YList(self)
                    self.dscp_cfg = YList(self)
                    self.protocol_cfg = YList(self)
                    self.source_ip_address_cfg = YList(self)
                    self.source_port_cfg = YList(self)
                    self._segment_path = lambda: "filter-entry" + "[filter-type='" + self.filter_type.get() + "']" + "[filter-logical-not='" + self.filter_logical_not.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.FilterEntry, ['filter_type', 'filter_logical_not'], name, value)


                class DestinationIpAddressCfg(Entity):
                    """
                    list of destination ip address
                    
                    .. attribute:: destination_ip_addr  <key>
                    
                    	destination ip prefix
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    
                    ----
                    

                    """

                    _prefix = 'policy'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg, self).__init__()

                        self.yang_name = "destination-ip-address-cfg"
                        self.yang_parent_name = "filter-entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.destination_ip_addr = YLeaf(YType.str, "destination-ip-addr")
                        self._segment_path = lambda: "destination-ip-address-cfg" + "[destination-ip-addr='" + self.destination_ip_addr.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg, ['destination_ip_addr'], name, value)


                class DestinationPortCfg(Entity):
                    """
                    list of ranges of destination port
                    
                    .. attribute:: destination_port_min  <key>
                    
                    	minimum value of destination port range
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: destination_port_max  <key>
                    
                    	maximum value of destination port range
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'policy'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg, self).__init__()

                        self.yang_name = "destination-port-cfg"
                        self.yang_parent_name = "filter-entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.destination_port_min = YLeaf(YType.uint16, "destination-port-min")

                        self.destination_port_max = YLeaf(YType.uint16, "destination-port-max")
                        self._segment_path = lambda: "destination-port-cfg" + "[destination-port-min='" + self.destination_port_min.get() + "']" + "[destination-port-max='" + self.destination_port_max.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg, ['destination_port_min', 'destination_port_max'], name, value)


                class DscpCfg(Entity):
                    """
                    list of dscp ranges
                    
                    .. attribute:: dscp_min  <key>
                    
                    	Minimum value of dscp range
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    .. attribute:: dscp_max  <key>
                    
                    	maximum value of dscp range
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    

                    """

                    _prefix = 'policy'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg, self).__init__()

                        self.yang_name = "dscp-cfg"
                        self.yang_parent_name = "filter-entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.dscp_min = YLeaf(YType.uint8, "dscp-min")

                        self.dscp_max = YLeaf(YType.uint8, "dscp-max")
                        self._segment_path = lambda: "dscp-cfg" + "[dscp-min='" + self.dscp_min.get() + "']" + "[dscp-max='" + self.dscp_max.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg, ['dscp_min', 'dscp_max'], name, value)


                class ProtocolCfg(Entity):
                    """
                    list of ranges of protocol values
                    
                    .. attribute:: protocol_min  <key>
                    
                    	minimum value of protocol range
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: protocol_max  <key>
                    
                    	maximum value of protocol range
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'policy'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg, self).__init__()

                        self.yang_name = "protocol-cfg"
                        self.yang_parent_name = "filter-entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.protocol_min = YLeaf(YType.uint8, "protocol-min")

                        self.protocol_max = YLeaf(YType.uint8, "protocol-max")
                        self._segment_path = lambda: "protocol-cfg" + "[protocol-min='" + self.protocol_min.get() + "']" + "[protocol-max='" + self.protocol_max.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg, ['protocol_min', 'protocol_max'], name, value)


                class SourceIpAddressCfg(Entity):
                    """
                    list of source ip address
                    
                    .. attribute:: source_ip_addr  <key>
                    
                    	source ip prefix
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    
                    ----
                    

                    """

                    _prefix = 'policy'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg, self).__init__()

                        self.yang_name = "source-ip-address-cfg"
                        self.yang_parent_name = "filter-entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.source_ip_addr = YLeaf(YType.str, "source-ip-addr")
                        self._segment_path = lambda: "source-ip-address-cfg" + "[source-ip-addr='" + self.source_ip_addr.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg, ['source_ip_addr'], name, value)


                class SourcePortCfg(Entity):
                    """
                    list of ranges of source port
                    
                    .. attribute:: source_port_min  <key>
                    
                    	minimum value of source port range
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: source_port_max  <key>
                    
                    	maximum value of source port range
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'policy'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg, self).__init__()

                        self.yang_name = "source-port-cfg"
                        self.yang_parent_name = "filter-entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.source_port_min = YLeaf(YType.uint16, "source-port-min")

                        self.source_port_max = YLeaf(YType.uint16, "source-port-max")
                        self._segment_path = lambda: "source-port-cfg" + "[source-port-min='" + self.source_port_min.get() + "']" + "[source-port-max='" + self.source_port_max.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg, ['source_port_min', 'source_port_max'], name, value)

    def clone_ptr(self):
        self._top_entity = Policies()
        return self._top_entity

