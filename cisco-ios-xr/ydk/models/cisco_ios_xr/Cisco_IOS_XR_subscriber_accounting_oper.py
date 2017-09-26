""" Cisco_IOS_XR_subscriber_accounting_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-accounting package operational data.

This module contains definitions
for the following management objects\:
  subscriber\-accounting\: Subscriber accounting operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SubscriberAccounting(Entity):
    """
    Subscriber accounting operational data
    
    .. attribute:: nodes
    
    	Subscriber accounting operational data for a particular location
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes>`
    
    

    """

    _prefix = 'subscriber-accounting-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SubscriberAccounting, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-accounting"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-accounting-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", SubscriberAccounting.Nodes)}
        self._child_list_classes = {}

        self.nodes = SubscriberAccounting.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting"


    class Nodes(Entity):
        """
        Subscriber accounting operational data for a
        particular location
        
        .. attribute:: node
        
        	Location. For example, 0/1/CPU0
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node>`
        
        

        """

        _prefix = 'subscriber-accounting-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberAccounting.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "subscriber-accounting"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", SubscriberAccounting.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberAccounting.Nodes, [], name, value)


        class Node(Entity):
            """
            Location. For example, 0/1/CPU0
            
            .. attribute:: node_id  <key>
            
            	The node id to filter on. For example, 0/1/CPU0
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: subscriber_accounting_flow_features
            
            	Subscriber accounting flow feature data
            	**type**\:   :py:class:`SubscriberAccountingFlowFeatures <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures>`
            
            .. attribute:: subscriber_accounting_session_features
            
            	Subscriber accounting session feature data
            	**type**\:   :py:class:`SubscriberAccountingSessionFeatures <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures>`
            
            .. attribute:: subscriber_accounting_summary
            
            	Display subscriber accounting summary data
            	**type**\:   :py:class:`SubscriberAccountingSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary>`
            
            

            """

            _prefix = 'subscriber-accounting-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberAccounting.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"subscriber-accounting-flow-features" : ("subscriber_accounting_flow_features", SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures), "subscriber-accounting-session-features" : ("subscriber_accounting_session_features", SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures), "subscriber-accounting-summary" : ("subscriber_accounting_summary", SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary)}
                self._child_list_classes = {}

                self.node_id = YLeaf(YType.str, "node-id")

                self.subscriber_accounting_flow_features = SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures()
                self.subscriber_accounting_flow_features.parent = self
                self._children_name_map["subscriber_accounting_flow_features"] = "subscriber-accounting-flow-features"
                self._children_yang_names.add("subscriber-accounting-flow-features")

                self.subscriber_accounting_session_features = SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures()
                self.subscriber_accounting_session_features.parent = self
                self._children_name_map["subscriber_accounting_session_features"] = "subscriber-accounting-session-features"
                self._children_yang_names.add("subscriber-accounting-session-features")

                self.subscriber_accounting_summary = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary()
                self.subscriber_accounting_summary.parent = self
                self._children_name_map["subscriber_accounting_summary"] = "subscriber-accounting-summary"
                self._children_yang_names.add("subscriber-accounting-summary")
                self._segment_path = lambda: "node" + "[node-id='" + self.node_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SubscriberAccounting.Nodes.Node, ['node_id'], name, value)


            class SubscriberAccountingFlowFeatures(Entity):
                """
                Subscriber accounting flow feature data
                
                .. attribute:: subscriber_accounting_flow_feature
                
                	Display accounting flow features by unique subscriber label
                	**type**\: list of    :py:class:`SubscriberAccountingFlowFeature <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature>`
                
                

                """

                _prefix = 'subscriber-accounting-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures, self).__init__()

                    self.yang_name = "subscriber-accounting-flow-features"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"subscriber-accounting-flow-feature" : ("subscriber_accounting_flow_feature", SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature)}

                    self.subscriber_accounting_flow_feature = YList(self)
                    self._segment_path = lambda: "subscriber-accounting-flow-features"

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures, [], name, value)


                class SubscriberAccountingFlowFeature(Entity):
                    """
                    Display accounting flow features by unique
                    subscriber label
                    
                    .. attribute:: class_label  <key>
                    
                    	Unique subscriber class label
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: flow_feature_data
                    
                    	Accouting flow feature display data
                    	**type**\:   :py:class:`FlowFeatureData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData>`
                    
                    

                    """

                    _prefix = 'subscriber-accounting-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature, self).__init__()

                        self.yang_name = "subscriber-accounting-flow-feature"
                        self.yang_parent_name = "subscriber-accounting-flow-features"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"flow-feature-data" : ("flow_feature_data", SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData)}
                        self._child_list_classes = {}

                        self.class_label = YLeaf(YType.int32, "class-label")

                        self.flow_feature_data = SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData()
                        self.flow_feature_data.parent = self
                        self._children_name_map["flow_feature_data"] = "flow-feature-data"
                        self._children_yang_names.add("flow-feature-data")
                        self._segment_path = lambda: "subscriber-accounting-flow-feature" + "[class-label='" + self.class_label.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature, ['class_label'], name, value)


                    class FlowFeatureData(Entity):
                        """
                        Accouting flow feature display data
                        
                        .. attribute:: flow_accounting_enabled_flag
                        
                        	True if flow accounting is enabled
                        	**type**\:  bool
                        
                        .. attribute:: flow_accounting_method_list_name
                        
                        	Flow accounting method list name
                        	**type**\:  str
                        
                        	**length:** 0..256
                        
                        .. attribute:: flow_accounting_periodic_interval
                        
                        	Flow accounting periodic interval
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: flow_direction
                        
                        	Direction of the flow. 0 = Ingress, 1 = Egress
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: flow_idle_timeout_enabled_flag
                        
                        	True if flow idle timeout is enabled
                        	**type**\:  bool
                        
                        .. attribute:: flow_idle_timeout_value
                        
                        	Flow idle timeout value in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: prepaid_ccfh
                        
                        	Prepaid CCFH flag
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_cfg
                        
                        	Prepaid Config
                        	**type**\:  str
                        
                        	**length:** 0..256
                        
                        .. attribute:: prepaid_charging_rule
                        
                        	Prepaid charging rule name string
                        	**type**\:  str
                        
                        	**length:** 0..256
                        
                        .. attribute:: prepaid_enabled_flag
                        
                        	True if prepaid is enabled
                        	**type**\:  bool
                        
                        .. attribute:: prepaid_final_unit
                        
                        	Prepaid final unit indication flag
                        	**type**\:  bool
                        
                        .. attribute:: prepaid_idle_timeout_enabled
                        
                        	Flag to specify if idle timeout for service is enabled
                        	**type**\:  bool
                        
                        .. attribute:: prepaid_idle_timeout_value
                        
                        	Prepaid idle timeout value in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: prepaid_reauth_timeout_value
                        
                        	The time at which the re\-authorization will occur
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_reauth_timer_enabled
                        
                        	Flag to specify if absolute timeout for ervice is enabled
                        	**type**\:  bool
                        
                        .. attribute:: prepaid_remaining_qat
                        
                        	The time remaing for quota absolute timer to fire
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_remaining_qit
                        
                        	The time remaing for quota holding timer to fire 
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_remaining_qt
                        
                        	The time remaing for QT timer to fire
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_remaining_qtt
                        
                        	The time remaining for tariff timer to fire
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_remaining_wheel
                        
                        	The time remaining for idle timer wheel to fire
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_result_code
                        
                        	Prepaid authorization operation result code
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_tariff_time
                        
                        	The absolute time at which the traffic switch will occur expressed in UNIX time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_tariff_volumeb_quota
                        
                        	Total accumulated prepaid pre\-tarrif total volume quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_tariff_volumei_quota
                        
                        	Total accumulated prepaid pre\-tarrif input volume quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_tariff_volumeo_quota
                        
                        	Total accumulated prepaid pre\-tarrif output volume quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_time_quota
                        
                        	Current prepaid time quota in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: prepaid_time_state
                        
                        	Prepaid time state machine state
                        	**type**\:  str
                        
                        	**length:** 0..256
                        
                        .. attribute:: prepaid_time_threshold
                        
                        	Current prepaid time threshold in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: prepaid_total_time_quota
                        
                        	Total accumulated prepaid time quota
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_total_volumeb_quota
                        
                        	Total accumulated total volume quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_total_volumei_quota
                        
                        	Total accumulated input volume quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_total_volumeo_quota
                        
                        	Total accumulated output volume quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_newb_quota
                        
                        	Newly arrvied bi\-directional volume quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_newi_quota
                        
                        	Newly arrvied input volume quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_newo_quota
                        
                        	Newly arrvied output volume quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_refb_quota
                        
                        	Accumulated bi\-directional volume reference quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_refi_quota
                        
                        	Accumulated input volume reference quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_refo_quota
                        
                        	Accumulated output volume reference quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_state
                        
                        	Prepaid volume state machine state
                        	**type**\:  str
                        
                        	**length:** 0..256
                        
                        .. attribute:: prepaid_volume_threshold
                        
                        	Current prepaid volume threshold in bytes
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_usedi_quota
                        
                        	Accumulated input volume used quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_usedo_quota
                        
                        	Accumulated output volume used quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volumeb_quota
                        
                        	Current prepaid total volume quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volumei_quota
                        
                        	Current prepaid input volume quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volumeo_quota
                        
                        	Current prepaid output volume quota in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: unique_class_label
                        
                        	Unique class label used to identify the flow
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-accounting-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData, self).__init__()

                            self.yang_name = "flow-feature-data"
                            self.yang_parent_name = "subscriber-accounting-flow-feature"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.flow_accounting_enabled_flag = YLeaf(YType.boolean, "flow-accounting-enabled-flag")

                            self.flow_accounting_method_list_name = YLeaf(YType.str, "flow-accounting-method-list-name")

                            self.flow_accounting_periodic_interval = YLeaf(YType.uint32, "flow-accounting-periodic-interval")

                            self.flow_direction = YLeaf(YType.uint32, "flow-direction")

                            self.flow_idle_timeout_enabled_flag = YLeaf(YType.boolean, "flow-idle-timeout-enabled-flag")

                            self.flow_idle_timeout_value = YLeaf(YType.uint32, "flow-idle-timeout-value")

                            self.prepaid_ccfh = YLeaf(YType.uint32, "prepaid-ccfh")

                            self.prepaid_cfg = YLeaf(YType.str, "prepaid-cfg")

                            self.prepaid_charging_rule = YLeaf(YType.str, "prepaid-charging-rule")

                            self.prepaid_enabled_flag = YLeaf(YType.boolean, "prepaid-enabled-flag")

                            self.prepaid_final_unit = YLeaf(YType.boolean, "prepaid-final-unit")

                            self.prepaid_idle_timeout_enabled = YLeaf(YType.boolean, "prepaid-idle-timeout-enabled")

                            self.prepaid_idle_timeout_value = YLeaf(YType.uint32, "prepaid-idle-timeout-value")

                            self.prepaid_reauth_timeout_value = YLeaf(YType.uint32, "prepaid-reauth-timeout-value")

                            self.prepaid_reauth_timer_enabled = YLeaf(YType.boolean, "prepaid-reauth-timer-enabled")

                            self.prepaid_remaining_qat = YLeaf(YType.uint32, "prepaid-remaining-qat")

                            self.prepaid_remaining_qit = YLeaf(YType.uint32, "prepaid-remaining-qit")

                            self.prepaid_remaining_qt = YLeaf(YType.uint32, "prepaid-remaining-qt")

                            self.prepaid_remaining_qtt = YLeaf(YType.uint32, "prepaid-remaining-qtt")

                            self.prepaid_remaining_wheel = YLeaf(YType.uint32, "prepaid-remaining-wheel")

                            self.prepaid_result_code = YLeaf(YType.uint32, "prepaid-result-code")

                            self.prepaid_tariff_time = YLeaf(YType.uint32, "prepaid-tariff-time")

                            self.prepaid_tariff_volumeb_quota = YLeaf(YType.uint64, "prepaid-tariff-volumeb-quota")

                            self.prepaid_tariff_volumei_quota = YLeaf(YType.uint64, "prepaid-tariff-volumei-quota")

                            self.prepaid_tariff_volumeo_quota = YLeaf(YType.uint64, "prepaid-tariff-volumeo-quota")

                            self.prepaid_time_quota = YLeaf(YType.uint32, "prepaid-time-quota")

                            self.prepaid_time_state = YLeaf(YType.str, "prepaid-time-state")

                            self.prepaid_time_threshold = YLeaf(YType.uint32, "prepaid-time-threshold")

                            self.prepaid_total_time_quota = YLeaf(YType.uint32, "prepaid-total-time-quota")

                            self.prepaid_total_volumeb_quota = YLeaf(YType.uint64, "prepaid-total-volumeb-quota")

                            self.prepaid_total_volumei_quota = YLeaf(YType.uint64, "prepaid-total-volumei-quota")

                            self.prepaid_total_volumeo_quota = YLeaf(YType.uint64, "prepaid-total-volumeo-quota")

                            self.prepaid_volume_newb_quota = YLeaf(YType.uint64, "prepaid-volume-newb-quota")

                            self.prepaid_volume_newi_quota = YLeaf(YType.uint64, "prepaid-volume-newi-quota")

                            self.prepaid_volume_newo_quota = YLeaf(YType.uint64, "prepaid-volume-newo-quota")

                            self.prepaid_volume_refb_quota = YLeaf(YType.uint64, "prepaid-volume-refb-quota")

                            self.prepaid_volume_refi_quota = YLeaf(YType.uint64, "prepaid-volume-refi-quota")

                            self.prepaid_volume_refo_quota = YLeaf(YType.uint64, "prepaid-volume-refo-quota")

                            self.prepaid_volume_state = YLeaf(YType.str, "prepaid-volume-state")

                            self.prepaid_volume_threshold = YLeaf(YType.uint32, "prepaid-volume-threshold")

                            self.prepaid_volume_usedi_quota = YLeaf(YType.uint64, "prepaid-volume-usedi-quota")

                            self.prepaid_volume_usedo_quota = YLeaf(YType.uint64, "prepaid-volume-usedo-quota")

                            self.prepaid_volumeb_quota = YLeaf(YType.uint64, "prepaid-volumeb-quota")

                            self.prepaid_volumei_quota = YLeaf(YType.uint64, "prepaid-volumei-quota")

                            self.prepaid_volumeo_quota = YLeaf(YType.uint64, "prepaid-volumeo-quota")

                            self.unique_class_label = YLeaf(YType.uint32, "unique-class-label")
                            self._segment_path = lambda: "flow-feature-data"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData, ['flow_accounting_enabled_flag', 'flow_accounting_method_list_name', 'flow_accounting_periodic_interval', 'flow_direction', 'flow_idle_timeout_enabled_flag', 'flow_idle_timeout_value', 'prepaid_ccfh', 'prepaid_cfg', 'prepaid_charging_rule', 'prepaid_enabled_flag', 'prepaid_final_unit', 'prepaid_idle_timeout_enabled', 'prepaid_idle_timeout_value', 'prepaid_reauth_timeout_value', 'prepaid_reauth_timer_enabled', 'prepaid_remaining_qat', 'prepaid_remaining_qit', 'prepaid_remaining_qt', 'prepaid_remaining_qtt', 'prepaid_remaining_wheel', 'prepaid_result_code', 'prepaid_tariff_time', 'prepaid_tariff_volumeb_quota', 'prepaid_tariff_volumei_quota', 'prepaid_tariff_volumeo_quota', 'prepaid_time_quota', 'prepaid_time_state', 'prepaid_time_threshold', 'prepaid_total_time_quota', 'prepaid_total_volumeb_quota', 'prepaid_total_volumei_quota', 'prepaid_total_volumeo_quota', 'prepaid_volume_newb_quota', 'prepaid_volume_newi_quota', 'prepaid_volume_newo_quota', 'prepaid_volume_refb_quota', 'prepaid_volume_refi_quota', 'prepaid_volume_refo_quota', 'prepaid_volume_state', 'prepaid_volume_threshold', 'prepaid_volume_usedi_quota', 'prepaid_volume_usedo_quota', 'prepaid_volumeb_quota', 'prepaid_volumei_quota', 'prepaid_volumeo_quota', 'unique_class_label'], name, value)


            class SubscriberAccountingSessionFeatures(Entity):
                """
                Subscriber accounting session feature data
                
                .. attribute:: subscriber_accounting_session_feature
                
                	Display accounting session features by unique subscriber label
                	**type**\: list of    :py:class:`SubscriberAccountingSessionFeature <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature>`
                
                

                """

                _prefix = 'subscriber-accounting-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures, self).__init__()

                    self.yang_name = "subscriber-accounting-session-features"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"subscriber-accounting-session-feature" : ("subscriber_accounting_session_feature", SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature)}

                    self.subscriber_accounting_session_feature = YList(self)
                    self._segment_path = lambda: "subscriber-accounting-session-features"

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures, [], name, value)


                class SubscriberAccountingSessionFeature(Entity):
                    """
                    Display accounting session features by unique
                    subscriber label
                    
                    .. attribute:: sub_label  <key>
                    
                    	Unique subscriber label
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: session_feature_data
                    
                    	Accounting session feature display data
                    	**type**\:   :py:class:`SessionFeatureData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData>`
                    
                    

                    """

                    _prefix = 'subscriber-accounting-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature, self).__init__()

                        self.yang_name = "subscriber-accounting-session-feature"
                        self.yang_parent_name = "subscriber-accounting-session-features"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"session-feature-data" : ("session_feature_data", SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData)}
                        self._child_list_classes = {}

                        self.sub_label = YLeaf(YType.int32, "sub-label")

                        self.session_feature_data = SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData()
                        self.session_feature_data.parent = self
                        self._children_name_map["session_feature_data"] = "session-feature-data"
                        self._children_yang_names.add("session-feature-data")
                        self._segment_path = lambda: "subscriber-accounting-session-feature" + "[sub-label='" + self.sub_label.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature, ['sub_label'], name, value)


                    class SessionFeatureData(Entity):
                        """
                        Accounting session feature display data
                        
                        .. attribute:: idle_timeout_direction
                        
                        	Idle timeout direction
                        	**type**\:  str
                        
                        	**length:** 0..256
                        
                        .. attribute:: idle_timeout_threshold
                        
                        	Idle timeout threshold in minutes per packets
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: minute
                        
                        .. attribute:: idle_timeout_value
                        
                        	Idle timeout value in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: interface_handle
                        
                        	Handle of interface associated with the session
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: service_accounting_feature
                        
                        	List of service accounting features
                        	**type**\: list of    :py:class:`ServiceAccountingFeature <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature>`
                        
                        .. attribute:: session_accounting_aaa_request_failed
                        
                        	Number of Session Accounting AAA request failures
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_accounting_aaa_trans_pending
                        
                        	Number of Session Accounting AAA transactions pending
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_accounting_enabled_flag
                        
                        	True if session accounting is enabled
                        	**type**\:  bool
                        
                        .. attribute:: session_accounting_method_list
                        
                        	Session accounting method list name
                        	**type**\:  str
                        
                        	**length:** 0..256
                        
                        .. attribute:: session_accounting_periodic_interval
                        
                        	Session accounting periodic interval
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_accounting_started
                        
                        	True if session accounting started
                        	**type**\:  bool
                        
                        .. attribute:: session_disconnected
                        
                        	True if session is disconnected
                        	**type**\:  bool
                        
                        .. attribute:: session_idle_timeout_enabled_flag
                        
                        	True if session idle timeout is enabled
                        	**type**\:  bool
                        
                        .. attribute:: session_idle_to_aaa_request_failed
                        
                        	Number of Session Idle AAA request failures
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_idle_to_aaa_trans_pending
                        
                        	Number of Session Idle AAA transactions pending
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_is_idle
                        
                        	True if session is idle
                        	**type**\:  bool
                        
                        .. attribute:: session_stats_changed_time
                        
                        	Last time session data was received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_timeout_enabled_flag
                        
                        	True if session timeout is enabled
                        	**type**\:  bool
                        
                        .. attribute:: session_timeout_time_remaining
                        
                        	Number seconds remaining before session times out
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: session_timeout_value
                        
                        	Session timeout value in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: session_to_awake_count
                        
                        	Number of Session Awake AAA events
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_to_idle_count
                        
                        	Number of Session Idle AAA events
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_total_idle_time
                        
                        	Total time session has been idle
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unique_subscriber_label
                        
                        	Unique subscriber label used to identify the session
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-accounting-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData, self).__init__()

                            self.yang_name = "session-feature-data"
                            self.yang_parent_name = "subscriber-accounting-session-feature"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"service-accounting-feature" : ("service_accounting_feature", SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature)}

                            self.idle_timeout_direction = YLeaf(YType.str, "idle-timeout-direction")

                            self.idle_timeout_threshold = YLeaf(YType.uint32, "idle-timeout-threshold")

                            self.idle_timeout_value = YLeaf(YType.uint32, "idle-timeout-value")

                            self.interface_handle = YLeaf(YType.uint32, "interface-handle")

                            self.session_accounting_aaa_request_failed = YLeaf(YType.uint32, "session-accounting-aaa-request-failed")

                            self.session_accounting_aaa_trans_pending = YLeaf(YType.uint32, "session-accounting-aaa-trans-pending")

                            self.session_accounting_enabled_flag = YLeaf(YType.boolean, "session-accounting-enabled-flag")

                            self.session_accounting_method_list = YLeaf(YType.str, "session-accounting-method-list")

                            self.session_accounting_periodic_interval = YLeaf(YType.uint32, "session-accounting-periodic-interval")

                            self.session_accounting_started = YLeaf(YType.boolean, "session-accounting-started")

                            self.session_disconnected = YLeaf(YType.boolean, "session-disconnected")

                            self.session_idle_timeout_enabled_flag = YLeaf(YType.boolean, "session-idle-timeout-enabled-flag")

                            self.session_idle_to_aaa_request_failed = YLeaf(YType.uint32, "session-idle-to-aaa-request-failed")

                            self.session_idle_to_aaa_trans_pending = YLeaf(YType.uint32, "session-idle-to-aaa-trans-pending")

                            self.session_is_idle = YLeaf(YType.boolean, "session-is-idle")

                            self.session_stats_changed_time = YLeaf(YType.uint32, "session-stats-changed-time")

                            self.session_timeout_enabled_flag = YLeaf(YType.boolean, "session-timeout-enabled-flag")

                            self.session_timeout_time_remaining = YLeaf(YType.uint32, "session-timeout-time-remaining")

                            self.session_timeout_value = YLeaf(YType.uint32, "session-timeout-value")

                            self.session_to_awake_count = YLeaf(YType.uint32, "session-to-awake-count")

                            self.session_to_idle_count = YLeaf(YType.uint32, "session-to-idle-count")

                            self.session_total_idle_time = YLeaf(YType.uint32, "session-total-idle-time")

                            self.unique_subscriber_label = YLeaf(YType.uint32, "unique-subscriber-label")

                            self.service_accounting_feature = YList(self)
                            self._segment_path = lambda: "session-feature-data"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData, ['idle_timeout_direction', 'idle_timeout_threshold', 'idle_timeout_value', 'interface_handle', 'session_accounting_aaa_request_failed', 'session_accounting_aaa_trans_pending', 'session_accounting_enabled_flag', 'session_accounting_method_list', 'session_accounting_periodic_interval', 'session_accounting_started', 'session_disconnected', 'session_idle_timeout_enabled_flag', 'session_idle_to_aaa_request_failed', 'session_idle_to_aaa_trans_pending', 'session_is_idle', 'session_stats_changed_time', 'session_timeout_enabled_flag', 'session_timeout_time_remaining', 'session_timeout_value', 'session_to_awake_count', 'session_to_idle_count', 'session_total_idle_time', 'unique_subscriber_label'], name, value)


                        class ServiceAccountingFeature(Entity):
                            """
                            List of service accounting features
                            
                            .. attribute:: service_accounting_enabled_flag
                            
                            	True if service accounting is enabled
                            	**type**\:  bool
                            
                            .. attribute:: service_accounting_method_list
                            
                            	Service accounting method list name
                            	**type**\:  str
                            
                            	**length:** 0..256
                            
                            .. attribute:: service_accounting_periodic_interval
                            
                            	Service accounting periodic interval
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_accounting_service_id
                            
                            	Service accounting service ID
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_accounting_aaa_request_failed
                            
                            	Number of Service Accounting AAA request failures for the service
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_accounting_aaa_trans_pending
                            
                            	Number of Service Accounting AAA transactions pending for the service
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_accounting_started
                            
                            	True if Service accounting started  for the service
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'subscriber-accounting-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature, self).__init__()

                                self.yang_name = "service-accounting-feature"
                                self.yang_parent_name = "session-feature-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.service_accounting_enabled_flag = YLeaf(YType.boolean, "service-accounting-enabled-flag")

                                self.service_accounting_method_list = YLeaf(YType.str, "service-accounting-method-list")

                                self.service_accounting_periodic_interval = YLeaf(YType.uint32, "service-accounting-periodic-interval")

                                self.service_accounting_service_id = YLeaf(YType.uint32, "service-accounting-service-id")

                                self.session_accounting_aaa_request_failed = YLeaf(YType.uint32, "session-accounting-aaa-request-failed")

                                self.session_accounting_aaa_trans_pending = YLeaf(YType.uint32, "session-accounting-aaa-trans-pending")

                                self.session_accounting_started = YLeaf(YType.boolean, "session-accounting-started")
                                self._segment_path = lambda: "service-accounting-feature"

                            def __setattr__(self, name, value):
                                self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature, ['service_accounting_enabled_flag', 'service_accounting_method_list', 'service_accounting_periodic_interval', 'service_accounting_service_id', 'session_accounting_aaa_request_failed', 'session_accounting_aaa_trans_pending', 'session_accounting_started'], name, value)


            class SubscriberAccountingSummary(Entity):
                """
                Display subscriber accounting summary data
                
                .. attribute:: aaa_counters
                
                	Accounting feature AAA summary counters
                	**type**\:   :py:class:`AaaCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters>`
                
                .. attribute:: idle_timeout_counters
                
                	Accounting feature idle timeout summary counters
                	**type**\:   :py:class:`IdleTimeoutCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters>`
                
                .. attribute:: session_flow_counters
                
                	Accounting feature session context summary counters
                	**type**\:   :py:class:`SessionFlowCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters>`
                
                .. attribute:: session_timeout_counters
                
                	Accounting feature session timeout summary counters
                	**type**\:   :py:class:`SessionTimeoutCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters>`
                
                

                """

                _prefix = 'subscriber-accounting-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary, self).__init__()

                    self.yang_name = "subscriber-accounting-summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"aaa-counters" : ("aaa_counters", SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters), "idle-timeout-counters" : ("idle_timeout_counters", SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters), "session-flow-counters" : ("session_flow_counters", SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters), "session-timeout-counters" : ("session_timeout_counters", SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters)}
                    self._child_list_classes = {}

                    self.aaa_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters()
                    self.aaa_counters.parent = self
                    self._children_name_map["aaa_counters"] = "aaa-counters"
                    self._children_yang_names.add("aaa-counters")

                    self.idle_timeout_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters()
                    self.idle_timeout_counters.parent = self
                    self._children_name_map["idle_timeout_counters"] = "idle-timeout-counters"
                    self._children_yang_names.add("idle-timeout-counters")

                    self.session_flow_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters()
                    self.session_flow_counters.parent = self
                    self._children_name_map["session_flow_counters"] = "session-flow-counters"
                    self._children_yang_names.add("session-flow-counters")

                    self.session_timeout_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters()
                    self.session_timeout_counters.parent = self
                    self._children_name_map["session_timeout_counters"] = "session-timeout-counters"
                    self._children_yang_names.add("session-timeout-counters")
                    self._segment_path = lambda: "subscriber-accounting-summary"


                class AaaCounters(Entity):
                    """
                    Accounting feature AAA summary counters
                    
                    .. attribute:: accounting_callback
                    
                    	Number of Accounting Callbacks Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flow_accounting_start
                    
                    	Number of Flow Accounting Start Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flow_accounting_stop
                    
                    	Number of Flow Accounting Stop Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flow_accounting_update
                    
                    	Number of Flow Accounting Update Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flow_disconnect
                    
                    	Number of Flow Disconnect Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flow_start
                    
                    	Number of Flow Start Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: idle_timeout
                    
                    	Number of Idle Timeout Events Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: idle_timeout_response_callback
                    
                    	Number of Idle Timeout Callbacks Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: owned_resource_start
                    
                    	Number of Owned Resource Starts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_accounting_start
                    
                    	Number of Prepaid Accounting Start Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_accounting_stop
                    
                    	Number of Prepaid Accounting Stop Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_quota_depleted
                    
                    	Number of Prepaid Quota Depleted Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_reauthorization
                    
                    	Number of Prepaid Authorization Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_start
                    
                    	Number of Prepaid Start Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_stop
                    
                    	Number of Prepaid Stop Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_time_threshold_reached
                    
                    	Number of Prepaid Time Threshold Reached Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_volume_threshold_reached
                    
                    	Number of Prepaid Volume Threshold Reached Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_accounting_start
                    
                    	Number of Service Accounting Start Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_accounting_stop
                    
                    	Number of Service Accounting Stop Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_accounting_update
                    
                    	Number of Service Accounting Update Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_acct_out_of_sync
                    
                    	Number of Service Accounting services out of sync
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_acct_reqs_failed
                    
                    	Number of Service Accounting requests that failed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_acct_trans_pending
                    
                    	Number of Service Accounting transactions pending
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_idle_to_out_of_sync
                    
                    	Number of Service Idle Timeout services out of sync
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_idle_to_reqs_failed
                    
                    	Number of Service Idle Timeout requests that failed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_idle_to_trans_pending
                    
                    	Number of Service Idle Timeout transactions pending
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_accounting_start
                    
                    	Number of Session Accounting Start Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_accounting_stop
                    
                    	Number of Session Accounting Stop Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_accounting_update
                    
                    	Number of Session Accounting Update Requests Sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_acct_out_of_sync
                    
                    	Number of Session Accounting sessions out of sync
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_acct_reqs_failed
                    
                    	Number of Session Accounting requests that failed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_acct_trans_pending
                    
                    	Number of Session Accounting transactions pending
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_idle_to_out_of_sync
                    
                    	Number of Session Idle Timeout sessions out of sync
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_idle_to_reqs_failed
                    
                    	Number of Session Idle Timeout requests that failed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_idle_to_trans_pending
                    
                    	Number of Session Idle Timeout transactions pending
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-accounting-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters, self).__init__()

                        self.yang_name = "aaa-counters"
                        self.yang_parent_name = "subscriber-accounting-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.accounting_callback = YLeaf(YType.uint32, "accounting-callback")

                        self.flow_accounting_start = YLeaf(YType.uint32, "flow-accounting-start")

                        self.flow_accounting_stop = YLeaf(YType.uint32, "flow-accounting-stop")

                        self.flow_accounting_update = YLeaf(YType.uint32, "flow-accounting-update")

                        self.flow_disconnect = YLeaf(YType.uint32, "flow-disconnect")

                        self.flow_start = YLeaf(YType.uint32, "flow-start")

                        self.idle_timeout = YLeaf(YType.uint32, "idle-timeout")

                        self.idle_timeout_response_callback = YLeaf(YType.uint32, "idle-timeout-response-callback")

                        self.owned_resource_start = YLeaf(YType.uint32, "owned-resource-start")

                        self.prepaid_accounting_start = YLeaf(YType.uint32, "prepaid-accounting-start")

                        self.prepaid_accounting_stop = YLeaf(YType.uint32, "prepaid-accounting-stop")

                        self.prepaid_quota_depleted = YLeaf(YType.uint32, "prepaid-quota-depleted")

                        self.prepaid_reauthorization = YLeaf(YType.uint32, "prepaid-reauthorization")

                        self.prepaid_start = YLeaf(YType.uint32, "prepaid-start")

                        self.prepaid_stop = YLeaf(YType.uint32, "prepaid-stop")

                        self.prepaid_time_threshold_reached = YLeaf(YType.uint32, "prepaid-time-threshold-reached")

                        self.prepaid_volume_threshold_reached = YLeaf(YType.uint32, "prepaid-volume-threshold-reached")

                        self.service_accounting_start = YLeaf(YType.uint32, "service-accounting-start")

                        self.service_accounting_stop = YLeaf(YType.uint32, "service-accounting-stop")

                        self.service_accounting_update = YLeaf(YType.uint32, "service-accounting-update")

                        self.service_acct_out_of_sync = YLeaf(YType.uint32, "service-acct-out-of-sync")

                        self.service_acct_reqs_failed = YLeaf(YType.uint32, "service-acct-reqs-failed")

                        self.service_acct_trans_pending = YLeaf(YType.uint32, "service-acct-trans-pending")

                        self.service_idle_to_out_of_sync = YLeaf(YType.uint32, "service-idle-to-out-of-sync")

                        self.service_idle_to_reqs_failed = YLeaf(YType.uint32, "service-idle-to-reqs-failed")

                        self.service_idle_to_trans_pending = YLeaf(YType.uint32, "service-idle-to-trans-pending")

                        self.session_accounting_start = YLeaf(YType.uint32, "session-accounting-start")

                        self.session_accounting_stop = YLeaf(YType.uint32, "session-accounting-stop")

                        self.session_accounting_update = YLeaf(YType.uint32, "session-accounting-update")

                        self.session_acct_out_of_sync = YLeaf(YType.uint32, "session-acct-out-of-sync")

                        self.session_acct_reqs_failed = YLeaf(YType.uint32, "session-acct-reqs-failed")

                        self.session_acct_trans_pending = YLeaf(YType.uint32, "session-acct-trans-pending")

                        self.session_idle_to_out_of_sync = YLeaf(YType.uint32, "session-idle-to-out-of-sync")

                        self.session_idle_to_reqs_failed = YLeaf(YType.uint32, "session-idle-to-reqs-failed")

                        self.session_idle_to_trans_pending = YLeaf(YType.uint32, "session-idle-to-trans-pending")
                        self._segment_path = lambda: "aaa-counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters, ['accounting_callback', 'flow_accounting_start', 'flow_accounting_stop', 'flow_accounting_update', 'flow_disconnect', 'flow_start', 'idle_timeout', 'idle_timeout_response_callback', 'owned_resource_start', 'prepaid_accounting_start', 'prepaid_accounting_stop', 'prepaid_quota_depleted', 'prepaid_reauthorization', 'prepaid_start', 'prepaid_stop', 'prepaid_time_threshold_reached', 'prepaid_volume_threshold_reached', 'service_accounting_start', 'service_accounting_stop', 'service_accounting_update', 'service_acct_out_of_sync', 'service_acct_reqs_failed', 'service_acct_trans_pending', 'service_idle_to_out_of_sync', 'service_idle_to_reqs_failed', 'service_idle_to_trans_pending', 'session_accounting_start', 'session_accounting_stop', 'session_accounting_update', 'session_acct_out_of_sync', 'session_acct_reqs_failed', 'session_acct_trans_pending', 'session_idle_to_out_of_sync', 'session_idle_to_reqs_failed', 'session_idle_to_trans_pending'], name, value)


                class IdleTimeoutCounters(Entity):
                    """
                    Accounting feature idle timeout summary counters
                    
                    .. attribute:: active_flow_idle_timers
                    
                    	Number of Active Flow Idle Timers
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active_prepaid_idle_timers
                    
                    	Number of Active Prepaid Idle Timers
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active_session_idle_timers
                    
                    	Number of Sessions with Idle Timeout Feature
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: expired_flow_idle_timers
                    
                    	Number of Flow Expired Idle Timers
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: expired_prepaid_idle_timers
                    
                    	Number of Expired Prepaid Idle Timers
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: idle_sessions
                    
                    	Number of Idle Sessions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: transitions_to_awake
                    
                    	Number of Sessions Transitions to Awake State
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: transitions_to_idle
                    
                    	Number of Sessions Transitions to Idle State
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-accounting-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters, self).__init__()

                        self.yang_name = "idle-timeout-counters"
                        self.yang_parent_name = "subscriber-accounting-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.active_flow_idle_timers = YLeaf(YType.uint32, "active-flow-idle-timers")

                        self.active_prepaid_idle_timers = YLeaf(YType.uint32, "active-prepaid-idle-timers")

                        self.active_session_idle_timers = YLeaf(YType.uint32, "active-session-idle-timers")

                        self.expired_flow_idle_timers = YLeaf(YType.uint32, "expired-flow-idle-timers")

                        self.expired_prepaid_idle_timers = YLeaf(YType.uint32, "expired-prepaid-idle-timers")

                        self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                        self.transitions_to_awake = YLeaf(YType.uint32, "transitions-to-awake")

                        self.transitions_to_idle = YLeaf(YType.uint32, "transitions-to-idle")
                        self._segment_path = lambda: "idle-timeout-counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters, ['active_flow_idle_timers', 'active_prepaid_idle_timers', 'active_session_idle_timers', 'expired_flow_idle_timers', 'expired_prepaid_idle_timers', 'idle_sessions', 'transitions_to_awake', 'transitions_to_idle'], name, value)


                class SessionFlowCounters(Entity):
                    """
                    Accounting feature session context summary
                    counters
                    
                    .. attribute:: active_flows
                    
                    	Number of Active Flows
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active_session_accounting_sessions
                    
                    	Number of Active Sessions with Accounting
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active_sessions
                    
                    	Number of Active Sessions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: disconnected_sessions
                    
                    	Number of Disconnected Sessions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: quota_received
                    
                    	Number of flows for which Quota is received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-accounting-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters, self).__init__()

                        self.yang_name = "session-flow-counters"
                        self.yang_parent_name = "subscriber-accounting-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.active_flows = YLeaf(YType.uint32, "active-flows")

                        self.active_session_accounting_sessions = YLeaf(YType.uint32, "active-session-accounting-sessions")

                        self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                        self.disconnected_sessions = YLeaf(YType.uint32, "disconnected-sessions")

                        self.quota_received = YLeaf(YType.uint32, "quota-received")
                        self._segment_path = lambda: "session-flow-counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters, ['active_flows', 'active_session_accounting_sessions', 'active_sessions', 'disconnected_sessions', 'quota_received'], name, value)


                class SessionTimeoutCounters(Entity):
                    """
                    Accounting feature session timeout summary
                    counters
                    
                    .. attribute:: active_session_timers
                    
                    	Number of Active Session Timers
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: expired_session_timers
                    
                    	Number of Expired Session Timers
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-accounting-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters, self).__init__()

                        self.yang_name = "session-timeout-counters"
                        self.yang_parent_name = "subscriber-accounting-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.active_session_timers = YLeaf(YType.uint32, "active-session-timers")

                        self.expired_session_timers = YLeaf(YType.uint32, "expired-session-timers")
                        self._segment_path = lambda: "session-timeout-counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters, ['active_session_timers', 'expired_session_timers'], name, value)

    def clone_ptr(self):
        self._top_entity = SubscriberAccounting()
        return self._top_entity

