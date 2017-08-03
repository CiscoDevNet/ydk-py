""" Cisco_IOS_XR_subscriber_accounting_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-accounting package operational data.

This module contains definitions
for the following management objects\:
  subscriber\-accounting\: Subscriber accounting operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.nodes = SubscriberAccounting.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


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

            self.node = YList(self)

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
                        super(SubscriberAccounting.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SubscriberAccounting.Nodes, self).__setattr__(name, value)


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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SubscriberAccounting.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SubscriberAccounting.Nodes.Node, self).__setattr__(name, value)


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

                    self.subscriber_accounting_session_feature = YList(self)

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
                                super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures, self).__setattr__(name, value)


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

                        self.sub_label = YLeaf(YType.int32, "sub-label")

                        self.session_feature_data = SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData()
                        self.session_feature_data.parent = self
                        self._children_name_map["session_feature_data"] = "session-feature-data"
                        self._children_yang_names.add("session-feature-data")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("sub_label") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature, self).__setattr__(name, value)


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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("idle_timeout_direction",
                                            "idle_timeout_threshold",
                                            "idle_timeout_value",
                                            "interface_handle",
                                            "session_accounting_aaa_request_failed",
                                            "session_accounting_aaa_trans_pending",
                                            "session_accounting_enabled_flag",
                                            "session_accounting_method_list",
                                            "session_accounting_periodic_interval",
                                            "session_accounting_started",
                                            "session_disconnected",
                                            "session_idle_timeout_enabled_flag",
                                            "session_idle_to_aaa_request_failed",
                                            "session_idle_to_aaa_trans_pending",
                                            "session_is_idle",
                                            "session_stats_changed_time",
                                            "session_timeout_enabled_flag",
                                            "session_timeout_time_remaining",
                                            "session_timeout_value",
                                            "session_to_awake_count",
                                            "session_to_idle_count",
                                            "session_total_idle_time",
                                            "unique_subscriber_label") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData, self).__setattr__(name, value)


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

                                self.service_accounting_enabled_flag = YLeaf(YType.boolean, "service-accounting-enabled-flag")

                                self.service_accounting_method_list = YLeaf(YType.str, "service-accounting-method-list")

                                self.service_accounting_periodic_interval = YLeaf(YType.uint32, "service-accounting-periodic-interval")

                                self.service_accounting_service_id = YLeaf(YType.uint32, "service-accounting-service-id")

                                self.session_accounting_aaa_request_failed = YLeaf(YType.uint32, "session-accounting-aaa-request-failed")

                                self.session_accounting_aaa_trans_pending = YLeaf(YType.uint32, "session-accounting-aaa-trans-pending")

                                self.session_accounting_started = YLeaf(YType.boolean, "session-accounting-started")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("service_accounting_enabled_flag",
                                                "service_accounting_method_list",
                                                "service_accounting_periodic_interval",
                                                "service_accounting_service_id",
                                                "session_accounting_aaa_request_failed",
                                                "session_accounting_aaa_trans_pending",
                                                "session_accounting_started") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.service_accounting_enabled_flag.is_set or
                                    self.service_accounting_method_list.is_set or
                                    self.service_accounting_periodic_interval.is_set or
                                    self.service_accounting_service_id.is_set or
                                    self.session_accounting_aaa_request_failed.is_set or
                                    self.session_accounting_aaa_trans_pending.is_set or
                                    self.session_accounting_started.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.service_accounting_enabled_flag.yfilter != YFilter.not_set or
                                    self.service_accounting_method_list.yfilter != YFilter.not_set or
                                    self.service_accounting_periodic_interval.yfilter != YFilter.not_set or
                                    self.service_accounting_service_id.yfilter != YFilter.not_set or
                                    self.session_accounting_aaa_request_failed.yfilter != YFilter.not_set or
                                    self.session_accounting_aaa_trans_pending.yfilter != YFilter.not_set or
                                    self.session_accounting_started.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "service-accounting-feature" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.service_accounting_enabled_flag.is_set or self.service_accounting_enabled_flag.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.service_accounting_enabled_flag.get_name_leafdata())
                                if (self.service_accounting_method_list.is_set or self.service_accounting_method_list.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.service_accounting_method_list.get_name_leafdata())
                                if (self.service_accounting_periodic_interval.is_set or self.service_accounting_periodic_interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.service_accounting_periodic_interval.get_name_leafdata())
                                if (self.service_accounting_service_id.is_set or self.service_accounting_service_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.service_accounting_service_id.get_name_leafdata())
                                if (self.session_accounting_aaa_request_failed.is_set or self.session_accounting_aaa_request_failed.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_accounting_aaa_request_failed.get_name_leafdata())
                                if (self.session_accounting_aaa_trans_pending.is_set or self.session_accounting_aaa_trans_pending.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_accounting_aaa_trans_pending.get_name_leafdata())
                                if (self.session_accounting_started.is_set or self.session_accounting_started.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_accounting_started.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "service-accounting-enabled-flag" or name == "service-accounting-method-list" or name == "service-accounting-periodic-interval" or name == "service-accounting-service-id" or name == "session-accounting-aaa-request-failed" or name == "session-accounting-aaa-trans-pending" or name == "session-accounting-started"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "service-accounting-enabled-flag"):
                                    self.service_accounting_enabled_flag = value
                                    self.service_accounting_enabled_flag.value_namespace = name_space
                                    self.service_accounting_enabled_flag.value_namespace_prefix = name_space_prefix
                                if(value_path == "service-accounting-method-list"):
                                    self.service_accounting_method_list = value
                                    self.service_accounting_method_list.value_namespace = name_space
                                    self.service_accounting_method_list.value_namespace_prefix = name_space_prefix
                                if(value_path == "service-accounting-periodic-interval"):
                                    self.service_accounting_periodic_interval = value
                                    self.service_accounting_periodic_interval.value_namespace = name_space
                                    self.service_accounting_periodic_interval.value_namespace_prefix = name_space_prefix
                                if(value_path == "service-accounting-service-id"):
                                    self.service_accounting_service_id = value
                                    self.service_accounting_service_id.value_namespace = name_space
                                    self.service_accounting_service_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-accounting-aaa-request-failed"):
                                    self.session_accounting_aaa_request_failed = value
                                    self.session_accounting_aaa_request_failed.value_namespace = name_space
                                    self.session_accounting_aaa_request_failed.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-accounting-aaa-trans-pending"):
                                    self.session_accounting_aaa_trans_pending = value
                                    self.session_accounting_aaa_trans_pending.value_namespace = name_space
                                    self.session_accounting_aaa_trans_pending.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-accounting-started"):
                                    self.session_accounting_started = value
                                    self.session_accounting_started.value_namespace = name_space
                                    self.session_accounting_started.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.service_accounting_feature:
                                if (c.has_data()):
                                    return True
                            return (
                                self.idle_timeout_direction.is_set or
                                self.idle_timeout_threshold.is_set or
                                self.idle_timeout_value.is_set or
                                self.interface_handle.is_set or
                                self.session_accounting_aaa_request_failed.is_set or
                                self.session_accounting_aaa_trans_pending.is_set or
                                self.session_accounting_enabled_flag.is_set or
                                self.session_accounting_method_list.is_set or
                                self.session_accounting_periodic_interval.is_set or
                                self.session_accounting_started.is_set or
                                self.session_disconnected.is_set or
                                self.session_idle_timeout_enabled_flag.is_set or
                                self.session_idle_to_aaa_request_failed.is_set or
                                self.session_idle_to_aaa_trans_pending.is_set or
                                self.session_is_idle.is_set or
                                self.session_stats_changed_time.is_set or
                                self.session_timeout_enabled_flag.is_set or
                                self.session_timeout_time_remaining.is_set or
                                self.session_timeout_value.is_set or
                                self.session_to_awake_count.is_set or
                                self.session_to_idle_count.is_set or
                                self.session_total_idle_time.is_set or
                                self.unique_subscriber_label.is_set)

                        def has_operation(self):
                            for c in self.service_accounting_feature:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.idle_timeout_direction.yfilter != YFilter.not_set or
                                self.idle_timeout_threshold.yfilter != YFilter.not_set or
                                self.idle_timeout_value.yfilter != YFilter.not_set or
                                self.interface_handle.yfilter != YFilter.not_set or
                                self.session_accounting_aaa_request_failed.yfilter != YFilter.not_set or
                                self.session_accounting_aaa_trans_pending.yfilter != YFilter.not_set or
                                self.session_accounting_enabled_flag.yfilter != YFilter.not_set or
                                self.session_accounting_method_list.yfilter != YFilter.not_set or
                                self.session_accounting_periodic_interval.yfilter != YFilter.not_set or
                                self.session_accounting_started.yfilter != YFilter.not_set or
                                self.session_disconnected.yfilter != YFilter.not_set or
                                self.session_idle_timeout_enabled_flag.yfilter != YFilter.not_set or
                                self.session_idle_to_aaa_request_failed.yfilter != YFilter.not_set or
                                self.session_idle_to_aaa_trans_pending.yfilter != YFilter.not_set or
                                self.session_is_idle.yfilter != YFilter.not_set or
                                self.session_stats_changed_time.yfilter != YFilter.not_set or
                                self.session_timeout_enabled_flag.yfilter != YFilter.not_set or
                                self.session_timeout_time_remaining.yfilter != YFilter.not_set or
                                self.session_timeout_value.yfilter != YFilter.not_set or
                                self.session_to_awake_count.yfilter != YFilter.not_set or
                                self.session_to_idle_count.yfilter != YFilter.not_set or
                                self.session_total_idle_time.yfilter != YFilter.not_set or
                                self.unique_subscriber_label.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "session-feature-data" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.idle_timeout_direction.is_set or self.idle_timeout_direction.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idle_timeout_direction.get_name_leafdata())
                            if (self.idle_timeout_threshold.is_set or self.idle_timeout_threshold.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idle_timeout_threshold.get_name_leafdata())
                            if (self.idle_timeout_value.is_set or self.idle_timeout_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idle_timeout_value.get_name_leafdata())
                            if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_handle.get_name_leafdata())
                            if (self.session_accounting_aaa_request_failed.is_set or self.session_accounting_aaa_request_failed.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_accounting_aaa_request_failed.get_name_leafdata())
                            if (self.session_accounting_aaa_trans_pending.is_set or self.session_accounting_aaa_trans_pending.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_accounting_aaa_trans_pending.get_name_leafdata())
                            if (self.session_accounting_enabled_flag.is_set or self.session_accounting_enabled_flag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_accounting_enabled_flag.get_name_leafdata())
                            if (self.session_accounting_method_list.is_set or self.session_accounting_method_list.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_accounting_method_list.get_name_leafdata())
                            if (self.session_accounting_periodic_interval.is_set or self.session_accounting_periodic_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_accounting_periodic_interval.get_name_leafdata())
                            if (self.session_accounting_started.is_set or self.session_accounting_started.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_accounting_started.get_name_leafdata())
                            if (self.session_disconnected.is_set or self.session_disconnected.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_disconnected.get_name_leafdata())
                            if (self.session_idle_timeout_enabled_flag.is_set or self.session_idle_timeout_enabled_flag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_idle_timeout_enabled_flag.get_name_leafdata())
                            if (self.session_idle_to_aaa_request_failed.is_set or self.session_idle_to_aaa_request_failed.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_idle_to_aaa_request_failed.get_name_leafdata())
                            if (self.session_idle_to_aaa_trans_pending.is_set or self.session_idle_to_aaa_trans_pending.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_idle_to_aaa_trans_pending.get_name_leafdata())
                            if (self.session_is_idle.is_set or self.session_is_idle.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_is_idle.get_name_leafdata())
                            if (self.session_stats_changed_time.is_set or self.session_stats_changed_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_stats_changed_time.get_name_leafdata())
                            if (self.session_timeout_enabled_flag.is_set or self.session_timeout_enabled_flag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_timeout_enabled_flag.get_name_leafdata())
                            if (self.session_timeout_time_remaining.is_set or self.session_timeout_time_remaining.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_timeout_time_remaining.get_name_leafdata())
                            if (self.session_timeout_value.is_set or self.session_timeout_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_timeout_value.get_name_leafdata())
                            if (self.session_to_awake_count.is_set or self.session_to_awake_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_to_awake_count.get_name_leafdata())
                            if (self.session_to_idle_count.is_set or self.session_to_idle_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_to_idle_count.get_name_leafdata())
                            if (self.session_total_idle_time.is_set or self.session_total_idle_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.session_total_idle_time.get_name_leafdata())
                            if (self.unique_subscriber_label.is_set or self.unique_subscriber_label.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unique_subscriber_label.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "service-accounting-feature"):
                                for c in self.service_accounting_feature:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.service_accounting_feature.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "service-accounting-feature" or name == "idle-timeout-direction" or name == "idle-timeout-threshold" or name == "idle-timeout-value" or name == "interface-handle" or name == "session-accounting-aaa-request-failed" or name == "session-accounting-aaa-trans-pending" or name == "session-accounting-enabled-flag" or name == "session-accounting-method-list" or name == "session-accounting-periodic-interval" or name == "session-accounting-started" or name == "session-disconnected" or name == "session-idle-timeout-enabled-flag" or name == "session-idle-to-aaa-request-failed" or name == "session-idle-to-aaa-trans-pending" or name == "session-is-idle" or name == "session-stats-changed-time" or name == "session-timeout-enabled-flag" or name == "session-timeout-time-remaining" or name == "session-timeout-value" or name == "session-to-awake-count" or name == "session-to-idle-count" or name == "session-total-idle-time" or name == "unique-subscriber-label"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "idle-timeout-direction"):
                                self.idle_timeout_direction = value
                                self.idle_timeout_direction.value_namespace = name_space
                                self.idle_timeout_direction.value_namespace_prefix = name_space_prefix
                            if(value_path == "idle-timeout-threshold"):
                                self.idle_timeout_threshold = value
                                self.idle_timeout_threshold.value_namespace = name_space
                                self.idle_timeout_threshold.value_namespace_prefix = name_space_prefix
                            if(value_path == "idle-timeout-value"):
                                self.idle_timeout_value = value
                                self.idle_timeout_value.value_namespace = name_space
                                self.idle_timeout_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-handle"):
                                self.interface_handle = value
                                self.interface_handle.value_namespace = name_space
                                self.interface_handle.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-accounting-aaa-request-failed"):
                                self.session_accounting_aaa_request_failed = value
                                self.session_accounting_aaa_request_failed.value_namespace = name_space
                                self.session_accounting_aaa_request_failed.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-accounting-aaa-trans-pending"):
                                self.session_accounting_aaa_trans_pending = value
                                self.session_accounting_aaa_trans_pending.value_namespace = name_space
                                self.session_accounting_aaa_trans_pending.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-accounting-enabled-flag"):
                                self.session_accounting_enabled_flag = value
                                self.session_accounting_enabled_flag.value_namespace = name_space
                                self.session_accounting_enabled_flag.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-accounting-method-list"):
                                self.session_accounting_method_list = value
                                self.session_accounting_method_list.value_namespace = name_space
                                self.session_accounting_method_list.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-accounting-periodic-interval"):
                                self.session_accounting_periodic_interval = value
                                self.session_accounting_periodic_interval.value_namespace = name_space
                                self.session_accounting_periodic_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-accounting-started"):
                                self.session_accounting_started = value
                                self.session_accounting_started.value_namespace = name_space
                                self.session_accounting_started.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-disconnected"):
                                self.session_disconnected = value
                                self.session_disconnected.value_namespace = name_space
                                self.session_disconnected.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-idle-timeout-enabled-flag"):
                                self.session_idle_timeout_enabled_flag = value
                                self.session_idle_timeout_enabled_flag.value_namespace = name_space
                                self.session_idle_timeout_enabled_flag.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-idle-to-aaa-request-failed"):
                                self.session_idle_to_aaa_request_failed = value
                                self.session_idle_to_aaa_request_failed.value_namespace = name_space
                                self.session_idle_to_aaa_request_failed.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-idle-to-aaa-trans-pending"):
                                self.session_idle_to_aaa_trans_pending = value
                                self.session_idle_to_aaa_trans_pending.value_namespace = name_space
                                self.session_idle_to_aaa_trans_pending.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-is-idle"):
                                self.session_is_idle = value
                                self.session_is_idle.value_namespace = name_space
                                self.session_is_idle.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-stats-changed-time"):
                                self.session_stats_changed_time = value
                                self.session_stats_changed_time.value_namespace = name_space
                                self.session_stats_changed_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-timeout-enabled-flag"):
                                self.session_timeout_enabled_flag = value
                                self.session_timeout_enabled_flag.value_namespace = name_space
                                self.session_timeout_enabled_flag.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-timeout-time-remaining"):
                                self.session_timeout_time_remaining = value
                                self.session_timeout_time_remaining.value_namespace = name_space
                                self.session_timeout_time_remaining.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-timeout-value"):
                                self.session_timeout_value = value
                                self.session_timeout_value.value_namespace = name_space
                                self.session_timeout_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-to-awake-count"):
                                self.session_to_awake_count = value
                                self.session_to_awake_count.value_namespace = name_space
                                self.session_to_awake_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-to-idle-count"):
                                self.session_to_idle_count = value
                                self.session_to_idle_count.value_namespace = name_space
                                self.session_to_idle_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "session-total-idle-time"):
                                self.session_total_idle_time = value
                                self.session_total_idle_time.value_namespace = name_space
                                self.session_total_idle_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "unique-subscriber-label"):
                                self.unique_subscriber_label = value
                                self.unique_subscriber_label.value_namespace = name_space
                                self.unique_subscriber_label.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.sub_label.is_set or
                            (self.session_feature_data is not None and self.session_feature_data.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.sub_label.yfilter != YFilter.not_set or
                            (self.session_feature_data is not None and self.session_feature_data.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "subscriber-accounting-session-feature" + "[sub-label='" + self.sub_label.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.sub_label.is_set or self.sub_label.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sub_label.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "session-feature-data"):
                            if (self.session_feature_data is None):
                                self.session_feature_data = SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData()
                                self.session_feature_data.parent = self
                                self._children_name_map["session_feature_data"] = "session-feature-data"
                            return self.session_feature_data

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "session-feature-data" or name == "sub-label"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "sub-label"):
                            self.sub_label = value
                            self.sub_label.value_namespace = name_space
                            self.sub_label.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.subscriber_accounting_session_feature:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.subscriber_accounting_session_feature:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "subscriber-accounting-session-features" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "subscriber-accounting-session-feature"):
                        for c in self.subscriber_accounting_session_feature:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.subscriber_accounting_session_feature.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "subscriber-accounting-session-feature"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("accounting_callback",
                                        "flow_accounting_start",
                                        "flow_accounting_stop",
                                        "flow_accounting_update",
                                        "flow_disconnect",
                                        "flow_start",
                                        "idle_timeout",
                                        "idle_timeout_response_callback",
                                        "owned_resource_start",
                                        "prepaid_accounting_start",
                                        "prepaid_accounting_stop",
                                        "prepaid_quota_depleted",
                                        "prepaid_reauthorization",
                                        "prepaid_start",
                                        "prepaid_stop",
                                        "prepaid_time_threshold_reached",
                                        "prepaid_volume_threshold_reached",
                                        "service_accounting_start",
                                        "service_accounting_stop",
                                        "service_accounting_update",
                                        "service_acct_out_of_sync",
                                        "service_acct_reqs_failed",
                                        "service_acct_trans_pending",
                                        "service_idle_to_out_of_sync",
                                        "service_idle_to_reqs_failed",
                                        "service_idle_to_trans_pending",
                                        "session_accounting_start",
                                        "session_accounting_stop",
                                        "session_accounting_update",
                                        "session_acct_out_of_sync",
                                        "session_acct_reqs_failed",
                                        "session_acct_trans_pending",
                                        "session_idle_to_out_of_sync",
                                        "session_idle_to_reqs_failed",
                                        "session_idle_to_trans_pending") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.accounting_callback.is_set or
                            self.flow_accounting_start.is_set or
                            self.flow_accounting_stop.is_set or
                            self.flow_accounting_update.is_set or
                            self.flow_disconnect.is_set or
                            self.flow_start.is_set or
                            self.idle_timeout.is_set or
                            self.idle_timeout_response_callback.is_set or
                            self.owned_resource_start.is_set or
                            self.prepaid_accounting_start.is_set or
                            self.prepaid_accounting_stop.is_set or
                            self.prepaid_quota_depleted.is_set or
                            self.prepaid_reauthorization.is_set or
                            self.prepaid_start.is_set or
                            self.prepaid_stop.is_set or
                            self.prepaid_time_threshold_reached.is_set or
                            self.prepaid_volume_threshold_reached.is_set or
                            self.service_accounting_start.is_set or
                            self.service_accounting_stop.is_set or
                            self.service_accounting_update.is_set or
                            self.service_acct_out_of_sync.is_set or
                            self.service_acct_reqs_failed.is_set or
                            self.service_acct_trans_pending.is_set or
                            self.service_idle_to_out_of_sync.is_set or
                            self.service_idle_to_reqs_failed.is_set or
                            self.service_idle_to_trans_pending.is_set or
                            self.session_accounting_start.is_set or
                            self.session_accounting_stop.is_set or
                            self.session_accounting_update.is_set or
                            self.session_acct_out_of_sync.is_set or
                            self.session_acct_reqs_failed.is_set or
                            self.session_acct_trans_pending.is_set or
                            self.session_idle_to_out_of_sync.is_set or
                            self.session_idle_to_reqs_failed.is_set or
                            self.session_idle_to_trans_pending.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.accounting_callback.yfilter != YFilter.not_set or
                            self.flow_accounting_start.yfilter != YFilter.not_set or
                            self.flow_accounting_stop.yfilter != YFilter.not_set or
                            self.flow_accounting_update.yfilter != YFilter.not_set or
                            self.flow_disconnect.yfilter != YFilter.not_set or
                            self.flow_start.yfilter != YFilter.not_set or
                            self.idle_timeout.yfilter != YFilter.not_set or
                            self.idle_timeout_response_callback.yfilter != YFilter.not_set or
                            self.owned_resource_start.yfilter != YFilter.not_set or
                            self.prepaid_accounting_start.yfilter != YFilter.not_set or
                            self.prepaid_accounting_stop.yfilter != YFilter.not_set or
                            self.prepaid_quota_depleted.yfilter != YFilter.not_set or
                            self.prepaid_reauthorization.yfilter != YFilter.not_set or
                            self.prepaid_start.yfilter != YFilter.not_set or
                            self.prepaid_stop.yfilter != YFilter.not_set or
                            self.prepaid_time_threshold_reached.yfilter != YFilter.not_set or
                            self.prepaid_volume_threshold_reached.yfilter != YFilter.not_set or
                            self.service_accounting_start.yfilter != YFilter.not_set or
                            self.service_accounting_stop.yfilter != YFilter.not_set or
                            self.service_accounting_update.yfilter != YFilter.not_set or
                            self.service_acct_out_of_sync.yfilter != YFilter.not_set or
                            self.service_acct_reqs_failed.yfilter != YFilter.not_set or
                            self.service_acct_trans_pending.yfilter != YFilter.not_set or
                            self.service_idle_to_out_of_sync.yfilter != YFilter.not_set or
                            self.service_idle_to_reqs_failed.yfilter != YFilter.not_set or
                            self.service_idle_to_trans_pending.yfilter != YFilter.not_set or
                            self.session_accounting_start.yfilter != YFilter.not_set or
                            self.session_accounting_stop.yfilter != YFilter.not_set or
                            self.session_accounting_update.yfilter != YFilter.not_set or
                            self.session_acct_out_of_sync.yfilter != YFilter.not_set or
                            self.session_acct_reqs_failed.yfilter != YFilter.not_set or
                            self.session_acct_trans_pending.yfilter != YFilter.not_set or
                            self.session_idle_to_out_of_sync.yfilter != YFilter.not_set or
                            self.session_idle_to_reqs_failed.yfilter != YFilter.not_set or
                            self.session_idle_to_trans_pending.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "aaa-counters" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.accounting_callback.is_set or self.accounting_callback.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accounting_callback.get_name_leafdata())
                        if (self.flow_accounting_start.is_set or self.flow_accounting_start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flow_accounting_start.get_name_leafdata())
                        if (self.flow_accounting_stop.is_set or self.flow_accounting_stop.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flow_accounting_stop.get_name_leafdata())
                        if (self.flow_accounting_update.is_set or self.flow_accounting_update.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flow_accounting_update.get_name_leafdata())
                        if (self.flow_disconnect.is_set or self.flow_disconnect.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flow_disconnect.get_name_leafdata())
                        if (self.flow_start.is_set or self.flow_start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flow_start.get_name_leafdata())
                        if (self.idle_timeout.is_set or self.idle_timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.idle_timeout.get_name_leafdata())
                        if (self.idle_timeout_response_callback.is_set or self.idle_timeout_response_callback.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.idle_timeout_response_callback.get_name_leafdata())
                        if (self.owned_resource_start.is_set or self.owned_resource_start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.owned_resource_start.get_name_leafdata())
                        if (self.prepaid_accounting_start.is_set or self.prepaid_accounting_start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prepaid_accounting_start.get_name_leafdata())
                        if (self.prepaid_accounting_stop.is_set or self.prepaid_accounting_stop.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prepaid_accounting_stop.get_name_leafdata())
                        if (self.prepaid_quota_depleted.is_set or self.prepaid_quota_depleted.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prepaid_quota_depleted.get_name_leafdata())
                        if (self.prepaid_reauthorization.is_set or self.prepaid_reauthorization.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prepaid_reauthorization.get_name_leafdata())
                        if (self.prepaid_start.is_set or self.prepaid_start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prepaid_start.get_name_leafdata())
                        if (self.prepaid_stop.is_set or self.prepaid_stop.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prepaid_stop.get_name_leafdata())
                        if (self.prepaid_time_threshold_reached.is_set or self.prepaid_time_threshold_reached.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prepaid_time_threshold_reached.get_name_leafdata())
                        if (self.prepaid_volume_threshold_reached.is_set or self.prepaid_volume_threshold_reached.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prepaid_volume_threshold_reached.get_name_leafdata())
                        if (self.service_accounting_start.is_set or self.service_accounting_start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service_accounting_start.get_name_leafdata())
                        if (self.service_accounting_stop.is_set or self.service_accounting_stop.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service_accounting_stop.get_name_leafdata())
                        if (self.service_accounting_update.is_set or self.service_accounting_update.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service_accounting_update.get_name_leafdata())
                        if (self.service_acct_out_of_sync.is_set or self.service_acct_out_of_sync.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service_acct_out_of_sync.get_name_leafdata())
                        if (self.service_acct_reqs_failed.is_set or self.service_acct_reqs_failed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service_acct_reqs_failed.get_name_leafdata())
                        if (self.service_acct_trans_pending.is_set or self.service_acct_trans_pending.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service_acct_trans_pending.get_name_leafdata())
                        if (self.service_idle_to_out_of_sync.is_set or self.service_idle_to_out_of_sync.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service_idle_to_out_of_sync.get_name_leafdata())
                        if (self.service_idle_to_reqs_failed.is_set or self.service_idle_to_reqs_failed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service_idle_to_reqs_failed.get_name_leafdata())
                        if (self.service_idle_to_trans_pending.is_set or self.service_idle_to_trans_pending.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service_idle_to_trans_pending.get_name_leafdata())
                        if (self.session_accounting_start.is_set or self.session_accounting_start.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_accounting_start.get_name_leafdata())
                        if (self.session_accounting_stop.is_set or self.session_accounting_stop.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_accounting_stop.get_name_leafdata())
                        if (self.session_accounting_update.is_set or self.session_accounting_update.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_accounting_update.get_name_leafdata())
                        if (self.session_acct_out_of_sync.is_set or self.session_acct_out_of_sync.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_acct_out_of_sync.get_name_leafdata())
                        if (self.session_acct_reqs_failed.is_set or self.session_acct_reqs_failed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_acct_reqs_failed.get_name_leafdata())
                        if (self.session_acct_trans_pending.is_set or self.session_acct_trans_pending.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_acct_trans_pending.get_name_leafdata())
                        if (self.session_idle_to_out_of_sync.is_set or self.session_idle_to_out_of_sync.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_idle_to_out_of_sync.get_name_leafdata())
                        if (self.session_idle_to_reqs_failed.is_set or self.session_idle_to_reqs_failed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_idle_to_reqs_failed.get_name_leafdata())
                        if (self.session_idle_to_trans_pending.is_set or self.session_idle_to_trans_pending.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_idle_to_trans_pending.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accounting-callback" or name == "flow-accounting-start" or name == "flow-accounting-stop" or name == "flow-accounting-update" or name == "flow-disconnect" or name == "flow-start" or name == "idle-timeout" or name == "idle-timeout-response-callback" or name == "owned-resource-start" or name == "prepaid-accounting-start" or name == "prepaid-accounting-stop" or name == "prepaid-quota-depleted" or name == "prepaid-reauthorization" or name == "prepaid-start" or name == "prepaid-stop" or name == "prepaid-time-threshold-reached" or name == "prepaid-volume-threshold-reached" or name == "service-accounting-start" or name == "service-accounting-stop" or name == "service-accounting-update" or name == "service-acct-out-of-sync" or name == "service-acct-reqs-failed" or name == "service-acct-trans-pending" or name == "service-idle-to-out-of-sync" or name == "service-idle-to-reqs-failed" or name == "service-idle-to-trans-pending" or name == "session-accounting-start" or name == "session-accounting-stop" or name == "session-accounting-update" or name == "session-acct-out-of-sync" or name == "session-acct-reqs-failed" or name == "session-acct-trans-pending" or name == "session-idle-to-out-of-sync" or name == "session-idle-to-reqs-failed" or name == "session-idle-to-trans-pending"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "accounting-callback"):
                            self.accounting_callback = value
                            self.accounting_callback.value_namespace = name_space
                            self.accounting_callback.value_namespace_prefix = name_space_prefix
                        if(value_path == "flow-accounting-start"):
                            self.flow_accounting_start = value
                            self.flow_accounting_start.value_namespace = name_space
                            self.flow_accounting_start.value_namespace_prefix = name_space_prefix
                        if(value_path == "flow-accounting-stop"):
                            self.flow_accounting_stop = value
                            self.flow_accounting_stop.value_namespace = name_space
                            self.flow_accounting_stop.value_namespace_prefix = name_space_prefix
                        if(value_path == "flow-accounting-update"):
                            self.flow_accounting_update = value
                            self.flow_accounting_update.value_namespace = name_space
                            self.flow_accounting_update.value_namespace_prefix = name_space_prefix
                        if(value_path == "flow-disconnect"):
                            self.flow_disconnect = value
                            self.flow_disconnect.value_namespace = name_space
                            self.flow_disconnect.value_namespace_prefix = name_space_prefix
                        if(value_path == "flow-start"):
                            self.flow_start = value
                            self.flow_start.value_namespace = name_space
                            self.flow_start.value_namespace_prefix = name_space_prefix
                        if(value_path == "idle-timeout"):
                            self.idle_timeout = value
                            self.idle_timeout.value_namespace = name_space
                            self.idle_timeout.value_namespace_prefix = name_space_prefix
                        if(value_path == "idle-timeout-response-callback"):
                            self.idle_timeout_response_callback = value
                            self.idle_timeout_response_callback.value_namespace = name_space
                            self.idle_timeout_response_callback.value_namespace_prefix = name_space_prefix
                        if(value_path == "owned-resource-start"):
                            self.owned_resource_start = value
                            self.owned_resource_start.value_namespace = name_space
                            self.owned_resource_start.value_namespace_prefix = name_space_prefix
                        if(value_path == "prepaid-accounting-start"):
                            self.prepaid_accounting_start = value
                            self.prepaid_accounting_start.value_namespace = name_space
                            self.prepaid_accounting_start.value_namespace_prefix = name_space_prefix
                        if(value_path == "prepaid-accounting-stop"):
                            self.prepaid_accounting_stop = value
                            self.prepaid_accounting_stop.value_namespace = name_space
                            self.prepaid_accounting_stop.value_namespace_prefix = name_space_prefix
                        if(value_path == "prepaid-quota-depleted"):
                            self.prepaid_quota_depleted = value
                            self.prepaid_quota_depleted.value_namespace = name_space
                            self.prepaid_quota_depleted.value_namespace_prefix = name_space_prefix
                        if(value_path == "prepaid-reauthorization"):
                            self.prepaid_reauthorization = value
                            self.prepaid_reauthorization.value_namespace = name_space
                            self.prepaid_reauthorization.value_namespace_prefix = name_space_prefix
                        if(value_path == "prepaid-start"):
                            self.prepaid_start = value
                            self.prepaid_start.value_namespace = name_space
                            self.prepaid_start.value_namespace_prefix = name_space_prefix
                        if(value_path == "prepaid-stop"):
                            self.prepaid_stop = value
                            self.prepaid_stop.value_namespace = name_space
                            self.prepaid_stop.value_namespace_prefix = name_space_prefix
                        if(value_path == "prepaid-time-threshold-reached"):
                            self.prepaid_time_threshold_reached = value
                            self.prepaid_time_threshold_reached.value_namespace = name_space
                            self.prepaid_time_threshold_reached.value_namespace_prefix = name_space_prefix
                        if(value_path == "prepaid-volume-threshold-reached"):
                            self.prepaid_volume_threshold_reached = value
                            self.prepaid_volume_threshold_reached.value_namespace = name_space
                            self.prepaid_volume_threshold_reached.value_namespace_prefix = name_space_prefix
                        if(value_path == "service-accounting-start"):
                            self.service_accounting_start = value
                            self.service_accounting_start.value_namespace = name_space
                            self.service_accounting_start.value_namespace_prefix = name_space_prefix
                        if(value_path == "service-accounting-stop"):
                            self.service_accounting_stop = value
                            self.service_accounting_stop.value_namespace = name_space
                            self.service_accounting_stop.value_namespace_prefix = name_space_prefix
                        if(value_path == "service-accounting-update"):
                            self.service_accounting_update = value
                            self.service_accounting_update.value_namespace = name_space
                            self.service_accounting_update.value_namespace_prefix = name_space_prefix
                        if(value_path == "service-acct-out-of-sync"):
                            self.service_acct_out_of_sync = value
                            self.service_acct_out_of_sync.value_namespace = name_space
                            self.service_acct_out_of_sync.value_namespace_prefix = name_space_prefix
                        if(value_path == "service-acct-reqs-failed"):
                            self.service_acct_reqs_failed = value
                            self.service_acct_reqs_failed.value_namespace = name_space
                            self.service_acct_reqs_failed.value_namespace_prefix = name_space_prefix
                        if(value_path == "service-acct-trans-pending"):
                            self.service_acct_trans_pending = value
                            self.service_acct_trans_pending.value_namespace = name_space
                            self.service_acct_trans_pending.value_namespace_prefix = name_space_prefix
                        if(value_path == "service-idle-to-out-of-sync"):
                            self.service_idle_to_out_of_sync = value
                            self.service_idle_to_out_of_sync.value_namespace = name_space
                            self.service_idle_to_out_of_sync.value_namespace_prefix = name_space_prefix
                        if(value_path == "service-idle-to-reqs-failed"):
                            self.service_idle_to_reqs_failed = value
                            self.service_idle_to_reqs_failed.value_namespace = name_space
                            self.service_idle_to_reqs_failed.value_namespace_prefix = name_space_prefix
                        if(value_path == "service-idle-to-trans-pending"):
                            self.service_idle_to_trans_pending = value
                            self.service_idle_to_trans_pending.value_namespace = name_space
                            self.service_idle_to_trans_pending.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-accounting-start"):
                            self.session_accounting_start = value
                            self.session_accounting_start.value_namespace = name_space
                            self.session_accounting_start.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-accounting-stop"):
                            self.session_accounting_stop = value
                            self.session_accounting_stop.value_namespace = name_space
                            self.session_accounting_stop.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-accounting-update"):
                            self.session_accounting_update = value
                            self.session_accounting_update.value_namespace = name_space
                            self.session_accounting_update.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-acct-out-of-sync"):
                            self.session_acct_out_of_sync = value
                            self.session_acct_out_of_sync.value_namespace = name_space
                            self.session_acct_out_of_sync.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-acct-reqs-failed"):
                            self.session_acct_reqs_failed = value
                            self.session_acct_reqs_failed.value_namespace = name_space
                            self.session_acct_reqs_failed.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-acct-trans-pending"):
                            self.session_acct_trans_pending = value
                            self.session_acct_trans_pending.value_namespace = name_space
                            self.session_acct_trans_pending.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-idle-to-out-of-sync"):
                            self.session_idle_to_out_of_sync = value
                            self.session_idle_to_out_of_sync.value_namespace = name_space
                            self.session_idle_to_out_of_sync.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-idle-to-reqs-failed"):
                            self.session_idle_to_reqs_failed = value
                            self.session_idle_to_reqs_failed.value_namespace = name_space
                            self.session_idle_to_reqs_failed.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-idle-to-trans-pending"):
                            self.session_idle_to_trans_pending = value
                            self.session_idle_to_trans_pending.value_namespace = name_space
                            self.session_idle_to_trans_pending.value_namespace_prefix = name_space_prefix


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

                        self.active_flow_idle_timers = YLeaf(YType.uint32, "active-flow-idle-timers")

                        self.active_prepaid_idle_timers = YLeaf(YType.uint32, "active-prepaid-idle-timers")

                        self.active_session_idle_timers = YLeaf(YType.uint32, "active-session-idle-timers")

                        self.expired_flow_idle_timers = YLeaf(YType.uint32, "expired-flow-idle-timers")

                        self.expired_prepaid_idle_timers = YLeaf(YType.uint32, "expired-prepaid-idle-timers")

                        self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                        self.transitions_to_awake = YLeaf(YType.uint32, "transitions-to-awake")

                        self.transitions_to_idle = YLeaf(YType.uint32, "transitions-to-idle")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("active_flow_idle_timers",
                                        "active_prepaid_idle_timers",
                                        "active_session_idle_timers",
                                        "expired_flow_idle_timers",
                                        "expired_prepaid_idle_timers",
                                        "idle_sessions",
                                        "transitions_to_awake",
                                        "transitions_to_idle") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.active_flow_idle_timers.is_set or
                            self.active_prepaid_idle_timers.is_set or
                            self.active_session_idle_timers.is_set or
                            self.expired_flow_idle_timers.is_set or
                            self.expired_prepaid_idle_timers.is_set or
                            self.idle_sessions.is_set or
                            self.transitions_to_awake.is_set or
                            self.transitions_to_idle.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.active_flow_idle_timers.yfilter != YFilter.not_set or
                            self.active_prepaid_idle_timers.yfilter != YFilter.not_set or
                            self.active_session_idle_timers.yfilter != YFilter.not_set or
                            self.expired_flow_idle_timers.yfilter != YFilter.not_set or
                            self.expired_prepaid_idle_timers.yfilter != YFilter.not_set or
                            self.idle_sessions.yfilter != YFilter.not_set or
                            self.transitions_to_awake.yfilter != YFilter.not_set or
                            self.transitions_to_idle.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "idle-timeout-counters" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.active_flow_idle_timers.is_set or self.active_flow_idle_timers.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active_flow_idle_timers.get_name_leafdata())
                        if (self.active_prepaid_idle_timers.is_set or self.active_prepaid_idle_timers.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active_prepaid_idle_timers.get_name_leafdata())
                        if (self.active_session_idle_timers.is_set or self.active_session_idle_timers.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active_session_idle_timers.get_name_leafdata())
                        if (self.expired_flow_idle_timers.is_set or self.expired_flow_idle_timers.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.expired_flow_idle_timers.get_name_leafdata())
                        if (self.expired_prepaid_idle_timers.is_set or self.expired_prepaid_idle_timers.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.expired_prepaid_idle_timers.get_name_leafdata())
                        if (self.idle_sessions.is_set or self.idle_sessions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.idle_sessions.get_name_leafdata())
                        if (self.transitions_to_awake.is_set or self.transitions_to_awake.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transitions_to_awake.get_name_leafdata())
                        if (self.transitions_to_idle.is_set or self.transitions_to_idle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transitions_to_idle.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "active-flow-idle-timers" or name == "active-prepaid-idle-timers" or name == "active-session-idle-timers" or name == "expired-flow-idle-timers" or name == "expired-prepaid-idle-timers" or name == "idle-sessions" or name == "transitions-to-awake" or name == "transitions-to-idle"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "active-flow-idle-timers"):
                            self.active_flow_idle_timers = value
                            self.active_flow_idle_timers.value_namespace = name_space
                            self.active_flow_idle_timers.value_namespace_prefix = name_space_prefix
                        if(value_path == "active-prepaid-idle-timers"):
                            self.active_prepaid_idle_timers = value
                            self.active_prepaid_idle_timers.value_namespace = name_space
                            self.active_prepaid_idle_timers.value_namespace_prefix = name_space_prefix
                        if(value_path == "active-session-idle-timers"):
                            self.active_session_idle_timers = value
                            self.active_session_idle_timers.value_namespace = name_space
                            self.active_session_idle_timers.value_namespace_prefix = name_space_prefix
                        if(value_path == "expired-flow-idle-timers"):
                            self.expired_flow_idle_timers = value
                            self.expired_flow_idle_timers.value_namespace = name_space
                            self.expired_flow_idle_timers.value_namespace_prefix = name_space_prefix
                        if(value_path == "expired-prepaid-idle-timers"):
                            self.expired_prepaid_idle_timers = value
                            self.expired_prepaid_idle_timers.value_namespace = name_space
                            self.expired_prepaid_idle_timers.value_namespace_prefix = name_space_prefix
                        if(value_path == "idle-sessions"):
                            self.idle_sessions = value
                            self.idle_sessions.value_namespace = name_space
                            self.idle_sessions.value_namespace_prefix = name_space_prefix
                        if(value_path == "transitions-to-awake"):
                            self.transitions_to_awake = value
                            self.transitions_to_awake.value_namespace = name_space
                            self.transitions_to_awake.value_namespace_prefix = name_space_prefix
                        if(value_path == "transitions-to-idle"):
                            self.transitions_to_idle = value
                            self.transitions_to_idle.value_namespace = name_space
                            self.transitions_to_idle.value_namespace_prefix = name_space_prefix


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

                        self.active_session_timers = YLeaf(YType.uint32, "active-session-timers")

                        self.expired_session_timers = YLeaf(YType.uint32, "expired-session-timers")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("active_session_timers",
                                        "expired_session_timers") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.active_session_timers.is_set or
                            self.expired_session_timers.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.active_session_timers.yfilter != YFilter.not_set or
                            self.expired_session_timers.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session-timeout-counters" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.active_session_timers.is_set or self.active_session_timers.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active_session_timers.get_name_leafdata())
                        if (self.expired_session_timers.is_set or self.expired_session_timers.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.expired_session_timers.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "active-session-timers" or name == "expired-session-timers"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "active-session-timers"):
                            self.active_session_timers = value
                            self.active_session_timers.value_namespace = name_space
                            self.active_session_timers.value_namespace_prefix = name_space_prefix
                        if(value_path == "expired-session-timers"):
                            self.expired_session_timers = value
                            self.expired_session_timers.value_namespace = name_space
                            self.expired_session_timers.value_namespace_prefix = name_space_prefix


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

                        self.active_flows = YLeaf(YType.uint32, "active-flows")

                        self.active_session_accounting_sessions = YLeaf(YType.uint32, "active-session-accounting-sessions")

                        self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                        self.disconnected_sessions = YLeaf(YType.uint32, "disconnected-sessions")

                        self.quota_received = YLeaf(YType.uint32, "quota-received")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("active_flows",
                                        "active_session_accounting_sessions",
                                        "active_sessions",
                                        "disconnected_sessions",
                                        "quota_received") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.active_flows.is_set or
                            self.active_session_accounting_sessions.is_set or
                            self.active_sessions.is_set or
                            self.disconnected_sessions.is_set or
                            self.quota_received.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.active_flows.yfilter != YFilter.not_set or
                            self.active_session_accounting_sessions.yfilter != YFilter.not_set or
                            self.active_sessions.yfilter != YFilter.not_set or
                            self.disconnected_sessions.yfilter != YFilter.not_set or
                            self.quota_received.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session-flow-counters" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.active_flows.is_set or self.active_flows.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active_flows.get_name_leafdata())
                        if (self.active_session_accounting_sessions.is_set or self.active_session_accounting_sessions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active_session_accounting_sessions.get_name_leafdata())
                        if (self.active_sessions.is_set or self.active_sessions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active_sessions.get_name_leafdata())
                        if (self.disconnected_sessions.is_set or self.disconnected_sessions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.disconnected_sessions.get_name_leafdata())
                        if (self.quota_received.is_set or self.quota_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.quota_received.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "active-flows" or name == "active-session-accounting-sessions" or name == "active-sessions" or name == "disconnected-sessions" or name == "quota-received"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "active-flows"):
                            self.active_flows = value
                            self.active_flows.value_namespace = name_space
                            self.active_flows.value_namespace_prefix = name_space_prefix
                        if(value_path == "active-session-accounting-sessions"):
                            self.active_session_accounting_sessions = value
                            self.active_session_accounting_sessions.value_namespace = name_space
                            self.active_session_accounting_sessions.value_namespace_prefix = name_space_prefix
                        if(value_path == "active-sessions"):
                            self.active_sessions = value
                            self.active_sessions.value_namespace = name_space
                            self.active_sessions.value_namespace_prefix = name_space_prefix
                        if(value_path == "disconnected-sessions"):
                            self.disconnected_sessions = value
                            self.disconnected_sessions.value_namespace = name_space
                            self.disconnected_sessions.value_namespace_prefix = name_space_prefix
                        if(value_path == "quota-received"):
                            self.quota_received = value
                            self.quota_received.value_namespace = name_space
                            self.quota_received.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.aaa_counters is not None and self.aaa_counters.has_data()) or
                        (self.idle_timeout_counters is not None and self.idle_timeout_counters.has_data()) or
                        (self.session_flow_counters is not None and self.session_flow_counters.has_data()) or
                        (self.session_timeout_counters is not None and self.session_timeout_counters.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.aaa_counters is not None and self.aaa_counters.has_operation()) or
                        (self.idle_timeout_counters is not None and self.idle_timeout_counters.has_operation()) or
                        (self.session_flow_counters is not None and self.session_flow_counters.has_operation()) or
                        (self.session_timeout_counters is not None and self.session_timeout_counters.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "subscriber-accounting-summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "aaa-counters"):
                        if (self.aaa_counters is None):
                            self.aaa_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters()
                            self.aaa_counters.parent = self
                            self._children_name_map["aaa_counters"] = "aaa-counters"
                        return self.aaa_counters

                    if (child_yang_name == "idle-timeout-counters"):
                        if (self.idle_timeout_counters is None):
                            self.idle_timeout_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters()
                            self.idle_timeout_counters.parent = self
                            self._children_name_map["idle_timeout_counters"] = "idle-timeout-counters"
                        return self.idle_timeout_counters

                    if (child_yang_name == "session-flow-counters"):
                        if (self.session_flow_counters is None):
                            self.session_flow_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters()
                            self.session_flow_counters.parent = self
                            self._children_name_map["session_flow_counters"] = "session-flow-counters"
                        return self.session_flow_counters

                    if (child_yang_name == "session-timeout-counters"):
                        if (self.session_timeout_counters is None):
                            self.session_timeout_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters()
                            self.session_timeout_counters.parent = self
                            self._children_name_map["session_timeout_counters"] = "session-timeout-counters"
                        return self.session_timeout_counters

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "aaa-counters" or name == "idle-timeout-counters" or name == "session-flow-counters" or name == "session-timeout-counters"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.subscriber_accounting_flow_feature = YList(self)

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
                                super(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures, self).__setattr__(name, value)


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

                        self.class_label = YLeaf(YType.int32, "class-label")

                        self.flow_feature_data = SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData()
                        self.flow_feature_data.parent = self
                        self._children_name_map["flow_feature_data"] = "flow-feature-data"
                        self._children_yang_names.add("flow-feature-data")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("class_label") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature, self).__setattr__(name, value)


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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("flow_accounting_enabled_flag",
                                            "flow_accounting_method_list_name",
                                            "flow_accounting_periodic_interval",
                                            "flow_direction",
                                            "flow_idle_timeout_enabled_flag",
                                            "flow_idle_timeout_value",
                                            "prepaid_ccfh",
                                            "prepaid_cfg",
                                            "prepaid_charging_rule",
                                            "prepaid_enabled_flag",
                                            "prepaid_final_unit",
                                            "prepaid_idle_timeout_enabled",
                                            "prepaid_idle_timeout_value",
                                            "prepaid_reauth_timeout_value",
                                            "prepaid_reauth_timer_enabled",
                                            "prepaid_remaining_qat",
                                            "prepaid_remaining_qit",
                                            "prepaid_remaining_qt",
                                            "prepaid_remaining_qtt",
                                            "prepaid_remaining_wheel",
                                            "prepaid_result_code",
                                            "prepaid_tariff_time",
                                            "prepaid_tariff_volumeb_quota",
                                            "prepaid_tariff_volumei_quota",
                                            "prepaid_tariff_volumeo_quota",
                                            "prepaid_time_quota",
                                            "prepaid_time_state",
                                            "prepaid_time_threshold",
                                            "prepaid_total_time_quota",
                                            "prepaid_total_volumeb_quota",
                                            "prepaid_total_volumei_quota",
                                            "prepaid_total_volumeo_quota",
                                            "prepaid_volume_newb_quota",
                                            "prepaid_volume_newi_quota",
                                            "prepaid_volume_newo_quota",
                                            "prepaid_volume_refb_quota",
                                            "prepaid_volume_refi_quota",
                                            "prepaid_volume_refo_quota",
                                            "prepaid_volume_state",
                                            "prepaid_volume_threshold",
                                            "prepaid_volume_usedi_quota",
                                            "prepaid_volume_usedo_quota",
                                            "prepaid_volumeb_quota",
                                            "prepaid_volumei_quota",
                                            "prepaid_volumeo_quota",
                                            "unique_class_label") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.flow_accounting_enabled_flag.is_set or
                                self.flow_accounting_method_list_name.is_set or
                                self.flow_accounting_periodic_interval.is_set or
                                self.flow_direction.is_set or
                                self.flow_idle_timeout_enabled_flag.is_set or
                                self.flow_idle_timeout_value.is_set or
                                self.prepaid_ccfh.is_set or
                                self.prepaid_cfg.is_set or
                                self.prepaid_charging_rule.is_set or
                                self.prepaid_enabled_flag.is_set or
                                self.prepaid_final_unit.is_set or
                                self.prepaid_idle_timeout_enabled.is_set or
                                self.prepaid_idle_timeout_value.is_set or
                                self.prepaid_reauth_timeout_value.is_set or
                                self.prepaid_reauth_timer_enabled.is_set or
                                self.prepaid_remaining_qat.is_set or
                                self.prepaid_remaining_qit.is_set or
                                self.prepaid_remaining_qt.is_set or
                                self.prepaid_remaining_qtt.is_set or
                                self.prepaid_remaining_wheel.is_set or
                                self.prepaid_result_code.is_set or
                                self.prepaid_tariff_time.is_set or
                                self.prepaid_tariff_volumeb_quota.is_set or
                                self.prepaid_tariff_volumei_quota.is_set or
                                self.prepaid_tariff_volumeo_quota.is_set or
                                self.prepaid_time_quota.is_set or
                                self.prepaid_time_state.is_set or
                                self.prepaid_time_threshold.is_set or
                                self.prepaid_total_time_quota.is_set or
                                self.prepaid_total_volumeb_quota.is_set or
                                self.prepaid_total_volumei_quota.is_set or
                                self.prepaid_total_volumeo_quota.is_set or
                                self.prepaid_volume_newb_quota.is_set or
                                self.prepaid_volume_newi_quota.is_set or
                                self.prepaid_volume_newo_quota.is_set or
                                self.prepaid_volume_refb_quota.is_set or
                                self.prepaid_volume_refi_quota.is_set or
                                self.prepaid_volume_refo_quota.is_set or
                                self.prepaid_volume_state.is_set or
                                self.prepaid_volume_threshold.is_set or
                                self.prepaid_volume_usedi_quota.is_set or
                                self.prepaid_volume_usedo_quota.is_set or
                                self.prepaid_volumeb_quota.is_set or
                                self.prepaid_volumei_quota.is_set or
                                self.prepaid_volumeo_quota.is_set or
                                self.unique_class_label.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.flow_accounting_enabled_flag.yfilter != YFilter.not_set or
                                self.flow_accounting_method_list_name.yfilter != YFilter.not_set or
                                self.flow_accounting_periodic_interval.yfilter != YFilter.not_set or
                                self.flow_direction.yfilter != YFilter.not_set or
                                self.flow_idle_timeout_enabled_flag.yfilter != YFilter.not_set or
                                self.flow_idle_timeout_value.yfilter != YFilter.not_set or
                                self.prepaid_ccfh.yfilter != YFilter.not_set or
                                self.prepaid_cfg.yfilter != YFilter.not_set or
                                self.prepaid_charging_rule.yfilter != YFilter.not_set or
                                self.prepaid_enabled_flag.yfilter != YFilter.not_set or
                                self.prepaid_final_unit.yfilter != YFilter.not_set or
                                self.prepaid_idle_timeout_enabled.yfilter != YFilter.not_set or
                                self.prepaid_idle_timeout_value.yfilter != YFilter.not_set or
                                self.prepaid_reauth_timeout_value.yfilter != YFilter.not_set or
                                self.prepaid_reauth_timer_enabled.yfilter != YFilter.not_set or
                                self.prepaid_remaining_qat.yfilter != YFilter.not_set or
                                self.prepaid_remaining_qit.yfilter != YFilter.not_set or
                                self.prepaid_remaining_qt.yfilter != YFilter.not_set or
                                self.prepaid_remaining_qtt.yfilter != YFilter.not_set or
                                self.prepaid_remaining_wheel.yfilter != YFilter.not_set or
                                self.prepaid_result_code.yfilter != YFilter.not_set or
                                self.prepaid_tariff_time.yfilter != YFilter.not_set or
                                self.prepaid_tariff_volumeb_quota.yfilter != YFilter.not_set or
                                self.prepaid_tariff_volumei_quota.yfilter != YFilter.not_set or
                                self.prepaid_tariff_volumeo_quota.yfilter != YFilter.not_set or
                                self.prepaid_time_quota.yfilter != YFilter.not_set or
                                self.prepaid_time_state.yfilter != YFilter.not_set or
                                self.prepaid_time_threshold.yfilter != YFilter.not_set or
                                self.prepaid_total_time_quota.yfilter != YFilter.not_set or
                                self.prepaid_total_volumeb_quota.yfilter != YFilter.not_set or
                                self.prepaid_total_volumei_quota.yfilter != YFilter.not_set or
                                self.prepaid_total_volumeo_quota.yfilter != YFilter.not_set or
                                self.prepaid_volume_newb_quota.yfilter != YFilter.not_set or
                                self.prepaid_volume_newi_quota.yfilter != YFilter.not_set or
                                self.prepaid_volume_newo_quota.yfilter != YFilter.not_set or
                                self.prepaid_volume_refb_quota.yfilter != YFilter.not_set or
                                self.prepaid_volume_refi_quota.yfilter != YFilter.not_set or
                                self.prepaid_volume_refo_quota.yfilter != YFilter.not_set or
                                self.prepaid_volume_state.yfilter != YFilter.not_set or
                                self.prepaid_volume_threshold.yfilter != YFilter.not_set or
                                self.prepaid_volume_usedi_quota.yfilter != YFilter.not_set or
                                self.prepaid_volume_usedo_quota.yfilter != YFilter.not_set or
                                self.prepaid_volumeb_quota.yfilter != YFilter.not_set or
                                self.prepaid_volumei_quota.yfilter != YFilter.not_set or
                                self.prepaid_volumeo_quota.yfilter != YFilter.not_set or
                                self.unique_class_label.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "flow-feature-data" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.flow_accounting_enabled_flag.is_set or self.flow_accounting_enabled_flag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_accounting_enabled_flag.get_name_leafdata())
                            if (self.flow_accounting_method_list_name.is_set or self.flow_accounting_method_list_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_accounting_method_list_name.get_name_leafdata())
                            if (self.flow_accounting_periodic_interval.is_set or self.flow_accounting_periodic_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_accounting_periodic_interval.get_name_leafdata())
                            if (self.flow_direction.is_set or self.flow_direction.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_direction.get_name_leafdata())
                            if (self.flow_idle_timeout_enabled_flag.is_set or self.flow_idle_timeout_enabled_flag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_idle_timeout_enabled_flag.get_name_leafdata())
                            if (self.flow_idle_timeout_value.is_set or self.flow_idle_timeout_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.flow_idle_timeout_value.get_name_leafdata())
                            if (self.prepaid_ccfh.is_set or self.prepaid_ccfh.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_ccfh.get_name_leafdata())
                            if (self.prepaid_cfg.is_set or self.prepaid_cfg.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_cfg.get_name_leafdata())
                            if (self.prepaid_charging_rule.is_set or self.prepaid_charging_rule.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_charging_rule.get_name_leafdata())
                            if (self.prepaid_enabled_flag.is_set or self.prepaid_enabled_flag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_enabled_flag.get_name_leafdata())
                            if (self.prepaid_final_unit.is_set or self.prepaid_final_unit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_final_unit.get_name_leafdata())
                            if (self.prepaid_idle_timeout_enabled.is_set or self.prepaid_idle_timeout_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_idle_timeout_enabled.get_name_leafdata())
                            if (self.prepaid_idle_timeout_value.is_set or self.prepaid_idle_timeout_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_idle_timeout_value.get_name_leafdata())
                            if (self.prepaid_reauth_timeout_value.is_set or self.prepaid_reauth_timeout_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_reauth_timeout_value.get_name_leafdata())
                            if (self.prepaid_reauth_timer_enabled.is_set or self.prepaid_reauth_timer_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_reauth_timer_enabled.get_name_leafdata())
                            if (self.prepaid_remaining_qat.is_set or self.prepaid_remaining_qat.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_remaining_qat.get_name_leafdata())
                            if (self.prepaid_remaining_qit.is_set or self.prepaid_remaining_qit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_remaining_qit.get_name_leafdata())
                            if (self.prepaid_remaining_qt.is_set or self.prepaid_remaining_qt.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_remaining_qt.get_name_leafdata())
                            if (self.prepaid_remaining_qtt.is_set or self.prepaid_remaining_qtt.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_remaining_qtt.get_name_leafdata())
                            if (self.prepaid_remaining_wheel.is_set or self.prepaid_remaining_wheel.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_remaining_wheel.get_name_leafdata())
                            if (self.prepaid_result_code.is_set or self.prepaid_result_code.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_result_code.get_name_leafdata())
                            if (self.prepaid_tariff_time.is_set or self.prepaid_tariff_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_tariff_time.get_name_leafdata())
                            if (self.prepaid_tariff_volumeb_quota.is_set or self.prepaid_tariff_volumeb_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_tariff_volumeb_quota.get_name_leafdata())
                            if (self.prepaid_tariff_volumei_quota.is_set or self.prepaid_tariff_volumei_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_tariff_volumei_quota.get_name_leafdata())
                            if (self.prepaid_tariff_volumeo_quota.is_set or self.prepaid_tariff_volumeo_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_tariff_volumeo_quota.get_name_leafdata())
                            if (self.prepaid_time_quota.is_set or self.prepaid_time_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_time_quota.get_name_leafdata())
                            if (self.prepaid_time_state.is_set or self.prepaid_time_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_time_state.get_name_leafdata())
                            if (self.prepaid_time_threshold.is_set or self.prepaid_time_threshold.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_time_threshold.get_name_leafdata())
                            if (self.prepaid_total_time_quota.is_set or self.prepaid_total_time_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_total_time_quota.get_name_leafdata())
                            if (self.prepaid_total_volumeb_quota.is_set or self.prepaid_total_volumeb_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_total_volumeb_quota.get_name_leafdata())
                            if (self.prepaid_total_volumei_quota.is_set or self.prepaid_total_volumei_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_total_volumei_quota.get_name_leafdata())
                            if (self.prepaid_total_volumeo_quota.is_set or self.prepaid_total_volumeo_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_total_volumeo_quota.get_name_leafdata())
                            if (self.prepaid_volume_newb_quota.is_set or self.prepaid_volume_newb_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_volume_newb_quota.get_name_leafdata())
                            if (self.prepaid_volume_newi_quota.is_set or self.prepaid_volume_newi_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_volume_newi_quota.get_name_leafdata())
                            if (self.prepaid_volume_newo_quota.is_set or self.prepaid_volume_newo_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_volume_newo_quota.get_name_leafdata())
                            if (self.prepaid_volume_refb_quota.is_set or self.prepaid_volume_refb_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_volume_refb_quota.get_name_leafdata())
                            if (self.prepaid_volume_refi_quota.is_set or self.prepaid_volume_refi_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_volume_refi_quota.get_name_leafdata())
                            if (self.prepaid_volume_refo_quota.is_set or self.prepaid_volume_refo_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_volume_refo_quota.get_name_leafdata())
                            if (self.prepaid_volume_state.is_set or self.prepaid_volume_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_volume_state.get_name_leafdata())
                            if (self.prepaid_volume_threshold.is_set or self.prepaid_volume_threshold.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_volume_threshold.get_name_leafdata())
                            if (self.prepaid_volume_usedi_quota.is_set or self.prepaid_volume_usedi_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_volume_usedi_quota.get_name_leafdata())
                            if (self.prepaid_volume_usedo_quota.is_set or self.prepaid_volume_usedo_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_volume_usedo_quota.get_name_leafdata())
                            if (self.prepaid_volumeb_quota.is_set or self.prepaid_volumeb_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_volumeb_quota.get_name_leafdata())
                            if (self.prepaid_volumei_quota.is_set or self.prepaid_volumei_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_volumei_quota.get_name_leafdata())
                            if (self.prepaid_volumeo_quota.is_set or self.prepaid_volumeo_quota.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prepaid_volumeo_quota.get_name_leafdata())
                            if (self.unique_class_label.is_set or self.unique_class_label.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.unique_class_label.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "flow-accounting-enabled-flag" or name == "flow-accounting-method-list-name" or name == "flow-accounting-periodic-interval" or name == "flow-direction" or name == "flow-idle-timeout-enabled-flag" or name == "flow-idle-timeout-value" or name == "prepaid-ccfh" or name == "prepaid-cfg" or name == "prepaid-charging-rule" or name == "prepaid-enabled-flag" or name == "prepaid-final-unit" or name == "prepaid-idle-timeout-enabled" or name == "prepaid-idle-timeout-value" or name == "prepaid-reauth-timeout-value" or name == "prepaid-reauth-timer-enabled" or name == "prepaid-remaining-qat" or name == "prepaid-remaining-qit" or name == "prepaid-remaining-qt" or name == "prepaid-remaining-qtt" or name == "prepaid-remaining-wheel" or name == "prepaid-result-code" or name == "prepaid-tariff-time" or name == "prepaid-tariff-volumeb-quota" or name == "prepaid-tariff-volumei-quota" or name == "prepaid-tariff-volumeo-quota" or name == "prepaid-time-quota" or name == "prepaid-time-state" or name == "prepaid-time-threshold" or name == "prepaid-total-time-quota" or name == "prepaid-total-volumeb-quota" or name == "prepaid-total-volumei-quota" or name == "prepaid-total-volumeo-quota" or name == "prepaid-volume-newb-quota" or name == "prepaid-volume-newi-quota" or name == "prepaid-volume-newo-quota" or name == "prepaid-volume-refb-quota" or name == "prepaid-volume-refi-quota" or name == "prepaid-volume-refo-quota" or name == "prepaid-volume-state" or name == "prepaid-volume-threshold" or name == "prepaid-volume-usedi-quota" or name == "prepaid-volume-usedo-quota" or name == "prepaid-volumeb-quota" or name == "prepaid-volumei-quota" or name == "prepaid-volumeo-quota" or name == "unique-class-label"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "flow-accounting-enabled-flag"):
                                self.flow_accounting_enabled_flag = value
                                self.flow_accounting_enabled_flag.value_namespace = name_space
                                self.flow_accounting_enabled_flag.value_namespace_prefix = name_space_prefix
                            if(value_path == "flow-accounting-method-list-name"):
                                self.flow_accounting_method_list_name = value
                                self.flow_accounting_method_list_name.value_namespace = name_space
                                self.flow_accounting_method_list_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "flow-accounting-periodic-interval"):
                                self.flow_accounting_periodic_interval = value
                                self.flow_accounting_periodic_interval.value_namespace = name_space
                                self.flow_accounting_periodic_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "flow-direction"):
                                self.flow_direction = value
                                self.flow_direction.value_namespace = name_space
                                self.flow_direction.value_namespace_prefix = name_space_prefix
                            if(value_path == "flow-idle-timeout-enabled-flag"):
                                self.flow_idle_timeout_enabled_flag = value
                                self.flow_idle_timeout_enabled_flag.value_namespace = name_space
                                self.flow_idle_timeout_enabled_flag.value_namespace_prefix = name_space_prefix
                            if(value_path == "flow-idle-timeout-value"):
                                self.flow_idle_timeout_value = value
                                self.flow_idle_timeout_value.value_namespace = name_space
                                self.flow_idle_timeout_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-ccfh"):
                                self.prepaid_ccfh = value
                                self.prepaid_ccfh.value_namespace = name_space
                                self.prepaid_ccfh.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-cfg"):
                                self.prepaid_cfg = value
                                self.prepaid_cfg.value_namespace = name_space
                                self.prepaid_cfg.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-charging-rule"):
                                self.prepaid_charging_rule = value
                                self.prepaid_charging_rule.value_namespace = name_space
                                self.prepaid_charging_rule.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-enabled-flag"):
                                self.prepaid_enabled_flag = value
                                self.prepaid_enabled_flag.value_namespace = name_space
                                self.prepaid_enabled_flag.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-final-unit"):
                                self.prepaid_final_unit = value
                                self.prepaid_final_unit.value_namespace = name_space
                                self.prepaid_final_unit.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-idle-timeout-enabled"):
                                self.prepaid_idle_timeout_enabled = value
                                self.prepaid_idle_timeout_enabled.value_namespace = name_space
                                self.prepaid_idle_timeout_enabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-idle-timeout-value"):
                                self.prepaid_idle_timeout_value = value
                                self.prepaid_idle_timeout_value.value_namespace = name_space
                                self.prepaid_idle_timeout_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-reauth-timeout-value"):
                                self.prepaid_reauth_timeout_value = value
                                self.prepaid_reauth_timeout_value.value_namespace = name_space
                                self.prepaid_reauth_timeout_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-reauth-timer-enabled"):
                                self.prepaid_reauth_timer_enabled = value
                                self.prepaid_reauth_timer_enabled.value_namespace = name_space
                                self.prepaid_reauth_timer_enabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-remaining-qat"):
                                self.prepaid_remaining_qat = value
                                self.prepaid_remaining_qat.value_namespace = name_space
                                self.prepaid_remaining_qat.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-remaining-qit"):
                                self.prepaid_remaining_qit = value
                                self.prepaid_remaining_qit.value_namespace = name_space
                                self.prepaid_remaining_qit.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-remaining-qt"):
                                self.prepaid_remaining_qt = value
                                self.prepaid_remaining_qt.value_namespace = name_space
                                self.prepaid_remaining_qt.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-remaining-qtt"):
                                self.prepaid_remaining_qtt = value
                                self.prepaid_remaining_qtt.value_namespace = name_space
                                self.prepaid_remaining_qtt.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-remaining-wheel"):
                                self.prepaid_remaining_wheel = value
                                self.prepaid_remaining_wheel.value_namespace = name_space
                                self.prepaid_remaining_wheel.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-result-code"):
                                self.prepaid_result_code = value
                                self.prepaid_result_code.value_namespace = name_space
                                self.prepaid_result_code.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-tariff-time"):
                                self.prepaid_tariff_time = value
                                self.prepaid_tariff_time.value_namespace = name_space
                                self.prepaid_tariff_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-tariff-volumeb-quota"):
                                self.prepaid_tariff_volumeb_quota = value
                                self.prepaid_tariff_volumeb_quota.value_namespace = name_space
                                self.prepaid_tariff_volumeb_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-tariff-volumei-quota"):
                                self.prepaid_tariff_volumei_quota = value
                                self.prepaid_tariff_volumei_quota.value_namespace = name_space
                                self.prepaid_tariff_volumei_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-tariff-volumeo-quota"):
                                self.prepaid_tariff_volumeo_quota = value
                                self.prepaid_tariff_volumeo_quota.value_namespace = name_space
                                self.prepaid_tariff_volumeo_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-time-quota"):
                                self.prepaid_time_quota = value
                                self.prepaid_time_quota.value_namespace = name_space
                                self.prepaid_time_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-time-state"):
                                self.prepaid_time_state = value
                                self.prepaid_time_state.value_namespace = name_space
                                self.prepaid_time_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-time-threshold"):
                                self.prepaid_time_threshold = value
                                self.prepaid_time_threshold.value_namespace = name_space
                                self.prepaid_time_threshold.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-total-time-quota"):
                                self.prepaid_total_time_quota = value
                                self.prepaid_total_time_quota.value_namespace = name_space
                                self.prepaid_total_time_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-total-volumeb-quota"):
                                self.prepaid_total_volumeb_quota = value
                                self.prepaid_total_volumeb_quota.value_namespace = name_space
                                self.prepaid_total_volumeb_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-total-volumei-quota"):
                                self.prepaid_total_volumei_quota = value
                                self.prepaid_total_volumei_quota.value_namespace = name_space
                                self.prepaid_total_volumei_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-total-volumeo-quota"):
                                self.prepaid_total_volumeo_quota = value
                                self.prepaid_total_volumeo_quota.value_namespace = name_space
                                self.prepaid_total_volumeo_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-volume-newb-quota"):
                                self.prepaid_volume_newb_quota = value
                                self.prepaid_volume_newb_quota.value_namespace = name_space
                                self.prepaid_volume_newb_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-volume-newi-quota"):
                                self.prepaid_volume_newi_quota = value
                                self.prepaid_volume_newi_quota.value_namespace = name_space
                                self.prepaid_volume_newi_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-volume-newo-quota"):
                                self.prepaid_volume_newo_quota = value
                                self.prepaid_volume_newo_quota.value_namespace = name_space
                                self.prepaid_volume_newo_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-volume-refb-quota"):
                                self.prepaid_volume_refb_quota = value
                                self.prepaid_volume_refb_quota.value_namespace = name_space
                                self.prepaid_volume_refb_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-volume-refi-quota"):
                                self.prepaid_volume_refi_quota = value
                                self.prepaid_volume_refi_quota.value_namespace = name_space
                                self.prepaid_volume_refi_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-volume-refo-quota"):
                                self.prepaid_volume_refo_quota = value
                                self.prepaid_volume_refo_quota.value_namespace = name_space
                                self.prepaid_volume_refo_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-volume-state"):
                                self.prepaid_volume_state = value
                                self.prepaid_volume_state.value_namespace = name_space
                                self.prepaid_volume_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-volume-threshold"):
                                self.prepaid_volume_threshold = value
                                self.prepaid_volume_threshold.value_namespace = name_space
                                self.prepaid_volume_threshold.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-volume-usedi-quota"):
                                self.prepaid_volume_usedi_quota = value
                                self.prepaid_volume_usedi_quota.value_namespace = name_space
                                self.prepaid_volume_usedi_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-volume-usedo-quota"):
                                self.prepaid_volume_usedo_quota = value
                                self.prepaid_volume_usedo_quota.value_namespace = name_space
                                self.prepaid_volume_usedo_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-volumeb-quota"):
                                self.prepaid_volumeb_quota = value
                                self.prepaid_volumeb_quota.value_namespace = name_space
                                self.prepaid_volumeb_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-volumei-quota"):
                                self.prepaid_volumei_quota = value
                                self.prepaid_volumei_quota.value_namespace = name_space
                                self.prepaid_volumei_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "prepaid-volumeo-quota"):
                                self.prepaid_volumeo_quota = value
                                self.prepaid_volumeo_quota.value_namespace = name_space
                                self.prepaid_volumeo_quota.value_namespace_prefix = name_space_prefix
                            if(value_path == "unique-class-label"):
                                self.unique_class_label = value
                                self.unique_class_label.value_namespace = name_space
                                self.unique_class_label.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.class_label.is_set or
                            (self.flow_feature_data is not None and self.flow_feature_data.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.class_label.yfilter != YFilter.not_set or
                            (self.flow_feature_data is not None and self.flow_feature_data.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "subscriber-accounting-flow-feature" + "[class-label='" + self.class_label.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.class_label.is_set or self.class_label.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.class_label.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "flow-feature-data"):
                            if (self.flow_feature_data is None):
                                self.flow_feature_data = SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData()
                                self.flow_feature_data.parent = self
                                self._children_name_map["flow_feature_data"] = "flow-feature-data"
                            return self.flow_feature_data

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "flow-feature-data" or name == "class-label"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "class-label"):
                            self.class_label = value
                            self.class_label.value_namespace = name_space
                            self.class_label.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.subscriber_accounting_flow_feature:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.subscriber_accounting_flow_feature:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "subscriber-accounting-flow-features" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "subscriber-accounting-flow-feature"):
                        for c in self.subscriber_accounting_flow_feature:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.subscriber_accounting_flow_feature.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "subscriber-accounting-flow-feature"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_id.is_set or
                    (self.subscriber_accounting_flow_features is not None and self.subscriber_accounting_flow_features.has_data()) or
                    (self.subscriber_accounting_session_features is not None and self.subscriber_accounting_session_features.has_data()) or
                    (self.subscriber_accounting_summary is not None and self.subscriber_accounting_summary.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_id.yfilter != YFilter.not_set or
                    (self.subscriber_accounting_flow_features is not None and self.subscriber_accounting_flow_features.has_operation()) or
                    (self.subscriber_accounting_session_features is not None and self.subscriber_accounting_session_features.has_operation()) or
                    (self.subscriber_accounting_summary is not None and self.subscriber_accounting_summary.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-id='" + self.node_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_id.is_set or self.node_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "subscriber-accounting-flow-features"):
                    if (self.subscriber_accounting_flow_features is None):
                        self.subscriber_accounting_flow_features = SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures()
                        self.subscriber_accounting_flow_features.parent = self
                        self._children_name_map["subscriber_accounting_flow_features"] = "subscriber-accounting-flow-features"
                    return self.subscriber_accounting_flow_features

                if (child_yang_name == "subscriber-accounting-session-features"):
                    if (self.subscriber_accounting_session_features is None):
                        self.subscriber_accounting_session_features = SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures()
                        self.subscriber_accounting_session_features.parent = self
                        self._children_name_map["subscriber_accounting_session_features"] = "subscriber-accounting-session-features"
                    return self.subscriber_accounting_session_features

                if (child_yang_name == "subscriber-accounting-summary"):
                    if (self.subscriber_accounting_summary is None):
                        self.subscriber_accounting_summary = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary()
                        self.subscriber_accounting_summary.parent = self
                        self._children_name_map["subscriber_accounting_summary"] = "subscriber-accounting-summary"
                    return self.subscriber_accounting_summary

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "subscriber-accounting-flow-features" or name == "subscriber-accounting-session-features" or name == "subscriber-accounting-summary" or name == "node-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-id"):
                    self.node_id = value
                    self.node_id.value_namespace = name_space
                    self.node_id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SubscriberAccounting.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting" + path_buffer

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

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = SubscriberAccounting.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SubscriberAccounting()
        return self._top_entity

