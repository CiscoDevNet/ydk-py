""" Cisco_IOS_XR_subscriber_accounting_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-accounting package operational data.

This module contains definitions
for the following management objects\:
  subscriber\-accounting\: Subscriber accounting operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class SubscriberAccounting(Entity):
    """
    Subscriber accounting operational data
    
    .. attribute:: nodes
    
    	Subscriber accounting operational data for a particular location
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes>`
    
    

    """

    _prefix = 'subscriber-accounting-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(SubscriberAccounting, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-accounting"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-accounting-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", SubscriberAccounting.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = SubscriberAccounting.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SubscriberAccounting, [], name, value)


    class Nodes(Entity):
        """
        Subscriber accounting operational data for a
        particular location
        
        .. attribute:: node
        
        	Location. For example, 0/1/CPU0
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node>`
        
        

        """

        _prefix = 'subscriber-accounting-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(SubscriberAccounting.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "subscriber-accounting"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", SubscriberAccounting.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberAccounting.Nodes, [], name, value)


        class Node(Entity):
            """
            Location. For example, 0/1/CPU0
            
            .. attribute:: node_id  (key)
            
            	The node id to filter on. For example, 0/1/CPU0
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: subscriber_accounting_session_features
            
            	Subscriber accounting session feature data
            	**type**\:  :py:class:`SubscriberAccountingSessionFeatures <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures>`
            
            .. attribute:: subscriber_accounting_summary
            
            	Display subscriber accounting summary data
            	**type**\:  :py:class:`SubscriberAccountingSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary>`
            
            .. attribute:: subscriber_accounting_flow_features
            
            	Subscriber accounting flow feature data
            	**type**\:  :py:class:`SubscriberAccountingFlowFeatures <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures>`
            
            

            """

            _prefix = 'subscriber-accounting-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(SubscriberAccounting.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_id']
                self._child_classes = OrderedDict([("subscriber-accounting-session-features", ("subscriber_accounting_session_features", SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures)), ("subscriber-accounting-summary", ("subscriber_accounting_summary", SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary)), ("subscriber-accounting-flow-features", ("subscriber_accounting_flow_features", SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures))])
                self._leafs = OrderedDict([
                    ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                ])
                self.node_id = None

                self.subscriber_accounting_session_features = SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures()
                self.subscriber_accounting_session_features.parent = self
                self._children_name_map["subscriber_accounting_session_features"] = "subscriber-accounting-session-features"

                self.subscriber_accounting_summary = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary()
                self.subscriber_accounting_summary.parent = self
                self._children_name_map["subscriber_accounting_summary"] = "subscriber-accounting-summary"

                self.subscriber_accounting_flow_features = SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures()
                self.subscriber_accounting_flow_features.parent = self
                self._children_name_map["subscriber_accounting_flow_features"] = "subscriber-accounting-flow-features"
                self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SubscriberAccounting.Nodes.Node, ['node_id'], name, value)


            class SubscriberAccountingSessionFeatures(Entity):
                """
                Subscriber accounting session feature data
                
                .. attribute:: subscriber_accounting_session_feature
                
                	Display accounting session features by unique subscriber label
                	**type**\: list of  		 :py:class:`SubscriberAccountingSessionFeature <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature>`
                
                

                """

                _prefix = 'subscriber-accounting-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures, self).__init__()

                    self.yang_name = "subscriber-accounting-session-features"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("subscriber-accounting-session-feature", ("subscriber_accounting_session_feature", SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature))])
                    self._leafs = OrderedDict()

                    self.subscriber_accounting_session_feature = YList(self)
                    self._segment_path = lambda: "subscriber-accounting-session-features"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures, [], name, value)


                class SubscriberAccountingSessionFeature(Entity):
                    """
                    Display accounting session features by unique
                    subscriber label
                    
                    .. attribute:: sub_label  (key)
                    
                    	Unique subscriber label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_feature_data
                    
                    	Accounting session feature display data
                    	**type**\:  :py:class:`SessionFeatureData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData>`
                    
                    

                    """

                    _prefix = 'subscriber-accounting-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature, self).__init__()

                        self.yang_name = "subscriber-accounting-session-feature"
                        self.yang_parent_name = "subscriber-accounting-session-features"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sub_label']
                        self._child_classes = OrderedDict([("session-feature-data", ("session_feature_data", SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData))])
                        self._leafs = OrderedDict([
                            ('sub_label', (YLeaf(YType.uint32, 'sub-label'), ['int'])),
                        ])
                        self.sub_label = None

                        self.session_feature_data = SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData()
                        self.session_feature_data.parent = self
                        self._children_name_map["session_feature_data"] = "session-feature-data"
                        self._segment_path = lambda: "subscriber-accounting-session-feature" + "[sub-label='" + str(self.sub_label) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature, ['sub_label'], name, value)


                    class SessionFeatureData(Entity):
                        """
                        Accounting session feature display data
                        
                        .. attribute:: unique_subscriber_label
                        
                        	Unique subscriber label used to identify the session
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_handle
                        
                        	Handle of interface associated with the session
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_disconnected
                        
                        	True if session is disconnected
                        	**type**\: bool
                        
                        .. attribute:: session_accounting_enabled_flag
                        
                        	True if session accounting is enabled
                        	**type**\: bool
                        
                        .. attribute:: session_accounting_method_list
                        
                        	Session accounting method list name
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        .. attribute:: session_accounting_periodic_interval
                        
                        	Session accounting periodic interval
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_accounting_aaa_trans_pending
                        
                        	Number of Session Accounting AAA transactions pending
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_accounting_aaa_request_failed
                        
                        	Number of Session Accounting AAA request failures
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_accounting_started
                        
                        	True if session accounting started
                        	**type**\: bool
                        
                        .. attribute:: session_idle_timeout_enabled_flag
                        
                        	True if session idle timeout is enabled
                        	**type**\: bool
                        
                        .. attribute:: idle_timeout_value
                        
                        	Idle timeout value in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: idle_timeout_threshold
                        
                        	Idle timeout threshold in minutes per packets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: minute
                        
                        .. attribute:: idle_timeout_direction
                        
                        	Idle timeout direction
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        .. attribute:: session_is_idle
                        
                        	True if session is idle
                        	**type**\: bool
                        
                        .. attribute:: session_stats_changed_time
                        
                        	Last time session data was received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_total_idle_time
                        
                        	Total time session has been idle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_to_idle_count
                        
                        	Number of Session Idle AAA events
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_to_awake_count
                        
                        	Number of Session Awake AAA events
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_idle_to_aaa_trans_pending
                        
                        	Number of Session Idle AAA transactions pending
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_idle_to_aaa_request_failed
                        
                        	Number of Session Idle AAA request failures
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_timeout_enabled_flag
                        
                        	True if session timeout is enabled
                        	**type**\: bool
                        
                        .. attribute:: session_timeout_value
                        
                        	Session timeout value in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: session_timeout_time_remaining
                        
                        	Number seconds remaining before session times out
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: service_accounting_feature
                        
                        	List of service accounting features
                        	**type**\: list of  		 :py:class:`ServiceAccountingFeature <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature>`
                        
                        

                        """

                        _prefix = 'subscriber-accounting-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData, self).__init__()

                            self.yang_name = "session-feature-data"
                            self.yang_parent_name = "subscriber-accounting-session-feature"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("service-accounting-feature", ("service_accounting_feature", SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature))])
                            self._leafs = OrderedDict([
                                ('unique_subscriber_label', (YLeaf(YType.uint32, 'unique-subscriber-label'), ['int'])),
                                ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                ('session_disconnected', (YLeaf(YType.boolean, 'session-disconnected'), ['bool'])),
                                ('session_accounting_enabled_flag', (YLeaf(YType.boolean, 'session-accounting-enabled-flag'), ['bool'])),
                                ('session_accounting_method_list', (YLeaf(YType.str, 'session-accounting-method-list'), ['str'])),
                                ('session_accounting_periodic_interval', (YLeaf(YType.uint32, 'session-accounting-periodic-interval'), ['int'])),
                                ('session_accounting_aaa_trans_pending', (YLeaf(YType.uint32, 'session-accounting-aaa-trans-pending'), ['int'])),
                                ('session_accounting_aaa_request_failed', (YLeaf(YType.uint32, 'session-accounting-aaa-request-failed'), ['int'])),
                                ('session_accounting_started', (YLeaf(YType.boolean, 'session-accounting-started'), ['bool'])),
                                ('session_idle_timeout_enabled_flag', (YLeaf(YType.boolean, 'session-idle-timeout-enabled-flag'), ['bool'])),
                                ('idle_timeout_value', (YLeaf(YType.uint32, 'idle-timeout-value'), ['int'])),
                                ('idle_timeout_threshold', (YLeaf(YType.uint32, 'idle-timeout-threshold'), ['int'])),
                                ('idle_timeout_direction', (YLeaf(YType.str, 'idle-timeout-direction'), ['str'])),
                                ('session_is_idle', (YLeaf(YType.boolean, 'session-is-idle'), ['bool'])),
                                ('session_stats_changed_time', (YLeaf(YType.uint32, 'session-stats-changed-time'), ['int'])),
                                ('session_total_idle_time', (YLeaf(YType.uint32, 'session-total-idle-time'), ['int'])),
                                ('session_to_idle_count', (YLeaf(YType.uint32, 'session-to-idle-count'), ['int'])),
                                ('session_to_awake_count', (YLeaf(YType.uint32, 'session-to-awake-count'), ['int'])),
                                ('session_idle_to_aaa_trans_pending', (YLeaf(YType.uint32, 'session-idle-to-aaa-trans-pending'), ['int'])),
                                ('session_idle_to_aaa_request_failed', (YLeaf(YType.uint32, 'session-idle-to-aaa-request-failed'), ['int'])),
                                ('session_timeout_enabled_flag', (YLeaf(YType.boolean, 'session-timeout-enabled-flag'), ['bool'])),
                                ('session_timeout_value', (YLeaf(YType.uint32, 'session-timeout-value'), ['int'])),
                                ('session_timeout_time_remaining', (YLeaf(YType.uint32, 'session-timeout-time-remaining'), ['int'])),
                            ])
                            self.unique_subscriber_label = None
                            self.interface_handle = None
                            self.session_disconnected = None
                            self.session_accounting_enabled_flag = None
                            self.session_accounting_method_list = None
                            self.session_accounting_periodic_interval = None
                            self.session_accounting_aaa_trans_pending = None
                            self.session_accounting_aaa_request_failed = None
                            self.session_accounting_started = None
                            self.session_idle_timeout_enabled_flag = None
                            self.idle_timeout_value = None
                            self.idle_timeout_threshold = None
                            self.idle_timeout_direction = None
                            self.session_is_idle = None
                            self.session_stats_changed_time = None
                            self.session_total_idle_time = None
                            self.session_to_idle_count = None
                            self.session_to_awake_count = None
                            self.session_idle_to_aaa_trans_pending = None
                            self.session_idle_to_aaa_request_failed = None
                            self.session_timeout_enabled_flag = None
                            self.session_timeout_value = None
                            self.session_timeout_time_remaining = None

                            self.service_accounting_feature = YList(self)
                            self._segment_path = lambda: "session-feature-data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData, [u'unique_subscriber_label', u'interface_handle', u'session_disconnected', u'session_accounting_enabled_flag', u'session_accounting_method_list', u'session_accounting_periodic_interval', u'session_accounting_aaa_trans_pending', u'session_accounting_aaa_request_failed', u'session_accounting_started', u'session_idle_timeout_enabled_flag', u'idle_timeout_value', u'idle_timeout_threshold', u'idle_timeout_direction', u'session_is_idle', u'session_stats_changed_time', u'session_total_idle_time', u'session_to_idle_count', u'session_to_awake_count', u'session_idle_to_aaa_trans_pending', u'session_idle_to_aaa_request_failed', u'session_timeout_enabled_flag', u'session_timeout_value', u'session_timeout_time_remaining'], name, value)


                        class ServiceAccountingFeature(Entity):
                            """
                            List of service accounting features
                            
                            .. attribute:: service_accounting_enabled_flag
                            
                            	True if service accounting is enabled
                            	**type**\: bool
                            
                            .. attribute:: service_accounting_service_id
                            
                            	Service accounting service ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: service_accounting_method_list
                            
                            	Service accounting method list name
                            	**type**\: str
                            
                            	**length:** 0..256
                            
                            .. attribute:: service_accounting_periodic_interval
                            
                            	Service accounting periodic interval
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_accounting_aaa_trans_pending
                            
                            	Number of Service Accounting AAA transactions pending for the service
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_accounting_aaa_request_failed
                            
                            	Number of Service Accounting AAA request failures for the service
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_accounting_started
                            
                            	True if Service accounting started  for the service
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'subscriber-accounting-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature, self).__init__()

                                self.yang_name = "service-accounting-feature"
                                self.yang_parent_name = "session-feature-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('service_accounting_enabled_flag', (YLeaf(YType.boolean, 'service-accounting-enabled-flag'), ['bool'])),
                                    ('service_accounting_service_id', (YLeaf(YType.uint32, 'service-accounting-service-id'), ['int'])),
                                    ('service_accounting_method_list', (YLeaf(YType.str, 'service-accounting-method-list'), ['str'])),
                                    ('service_accounting_periodic_interval', (YLeaf(YType.uint32, 'service-accounting-periodic-interval'), ['int'])),
                                    ('session_accounting_aaa_trans_pending', (YLeaf(YType.uint32, 'session-accounting-aaa-trans-pending'), ['int'])),
                                    ('session_accounting_aaa_request_failed', (YLeaf(YType.uint32, 'session-accounting-aaa-request-failed'), ['int'])),
                                    ('session_accounting_started', (YLeaf(YType.boolean, 'session-accounting-started'), ['bool'])),
                                ])
                                self.service_accounting_enabled_flag = None
                                self.service_accounting_service_id = None
                                self.service_accounting_method_list = None
                                self.service_accounting_periodic_interval = None
                                self.session_accounting_aaa_trans_pending = None
                                self.session_accounting_aaa_request_failed = None
                                self.session_accounting_started = None
                                self._segment_path = lambda: "service-accounting-feature"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature, [u'service_accounting_enabled_flag', u'service_accounting_service_id', u'service_accounting_method_list', u'service_accounting_periodic_interval', u'session_accounting_aaa_trans_pending', u'session_accounting_aaa_request_failed', u'session_accounting_started'], name, value)


            class SubscriberAccountingSummary(Entity):
                """
                Display subscriber accounting summary data
                
                .. attribute:: aaa_counters
                
                	Accounting feature AAA summary counters
                	**type**\:  :py:class:`AaaCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters>`
                
                .. attribute:: idle_timeout_counters
                
                	Accounting feature idle timeout summary counters
                	**type**\:  :py:class:`IdleTimeoutCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters>`
                
                .. attribute:: session_timeout_counters
                
                	Accounting feature session timeout summary counters
                	**type**\:  :py:class:`SessionTimeoutCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters>`
                
                .. attribute:: session_flow_counters
                
                	Accounting feature session context summary counters
                	**type**\:  :py:class:`SessionFlowCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters>`
                
                

                """

                _prefix = 'subscriber-accounting-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary, self).__init__()

                    self.yang_name = "subscriber-accounting-summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("aaa-counters", ("aaa_counters", SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters)), ("idle-timeout-counters", ("idle_timeout_counters", SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters)), ("session-timeout-counters", ("session_timeout_counters", SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters)), ("session-flow-counters", ("session_flow_counters", SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters))])
                    self._leafs = OrderedDict()

                    self.aaa_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters()
                    self.aaa_counters.parent = self
                    self._children_name_map["aaa_counters"] = "aaa-counters"

                    self.idle_timeout_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters()
                    self.idle_timeout_counters.parent = self
                    self._children_name_map["idle_timeout_counters"] = "idle-timeout-counters"

                    self.session_timeout_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters()
                    self.session_timeout_counters.parent = self
                    self._children_name_map["session_timeout_counters"] = "session-timeout-counters"

                    self.session_flow_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters()
                    self.session_flow_counters.parent = self
                    self._children_name_map["session_flow_counters"] = "session-flow-counters"
                    self._segment_path = lambda: "subscriber-accounting-summary"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary, [], name, value)


                class AaaCounters(Entity):
                    """
                    Accounting feature AAA summary counters
                    
                    .. attribute:: flow_start
                    
                    	Number of Flow Start Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flow_disconnect
                    
                    	Number of Flow Disconnect Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_accounting_start
                    
                    	Number of Session Accounting Start Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_accounting_stop
                    
                    	Number of Session Accounting Stop Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_accounting_update
                    
                    	Number of Session Accounting Update Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_accounting_start
                    
                    	Number of Service Accounting Start Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_accounting_stop
                    
                    	Number of Service Accounting Stop Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_accounting_update
                    
                    	Number of Service Accounting Update Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flow_accounting_start
                    
                    	Number of Flow Accounting Start Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flow_accounting_stop
                    
                    	Number of Flow Accounting Stop Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flow_accounting_update
                    
                    	Number of Flow Accounting Update Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: accounting_callback
                    
                    	Number of Accounting Callbacks Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_acct_trans_pending
                    
                    	Number of Session Accounting transactions pending
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_acct_reqs_failed
                    
                    	Number of Session Accounting requests that failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_acct_out_of_sync
                    
                    	Number of Session Accounting sessions out of sync
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_idle_to_trans_pending
                    
                    	Number of Session Idle Timeout transactions pending
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_idle_to_reqs_failed
                    
                    	Number of Session Idle Timeout requests that failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_idle_to_out_of_sync
                    
                    	Number of Session Idle Timeout sessions out of sync
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_acct_trans_pending
                    
                    	Number of Service Accounting transactions pending
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_acct_reqs_failed
                    
                    	Number of Service Accounting requests that failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_acct_out_of_sync
                    
                    	Number of Service Accounting services out of sync
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_idle_to_trans_pending
                    
                    	Number of Service Idle Timeout transactions pending
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_idle_to_reqs_failed
                    
                    	Number of Service Idle Timeout requests that failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: service_idle_to_out_of_sync
                    
                    	Number of Service Idle Timeout services out of sync
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_start
                    
                    	Number of Prepaid Start Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_stop
                    
                    	Number of Prepaid Stop Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_accounting_start
                    
                    	Number of Prepaid Accounting Start Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_accounting_stop
                    
                    	Number of Prepaid Accounting Stop Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_volume_threshold_reached
                    
                    	Number of Prepaid Volume Threshold Reached Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_time_threshold_reached
                    
                    	Number of Prepaid Time Threshold Reached Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_quota_depleted
                    
                    	Number of Prepaid Quota Depleted Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prepaid_reauthorization
                    
                    	Number of Prepaid Authorization Requests Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: idle_timeout
                    
                    	Number of Idle Timeout Events Sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: idle_timeout_response_callback
                    
                    	Number of Idle Timeout Callbacks Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: owned_resource_start
                    
                    	Number of Owned Resource Starts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-accounting-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters, self).__init__()

                        self.yang_name = "aaa-counters"
                        self.yang_parent_name = "subscriber-accounting-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('flow_start', (YLeaf(YType.uint32, 'flow-start'), ['int'])),
                            ('flow_disconnect', (YLeaf(YType.uint32, 'flow-disconnect'), ['int'])),
                            ('session_accounting_start', (YLeaf(YType.uint32, 'session-accounting-start'), ['int'])),
                            ('session_accounting_stop', (YLeaf(YType.uint32, 'session-accounting-stop'), ['int'])),
                            ('session_accounting_update', (YLeaf(YType.uint32, 'session-accounting-update'), ['int'])),
                            ('service_accounting_start', (YLeaf(YType.uint32, 'service-accounting-start'), ['int'])),
                            ('service_accounting_stop', (YLeaf(YType.uint32, 'service-accounting-stop'), ['int'])),
                            ('service_accounting_update', (YLeaf(YType.uint32, 'service-accounting-update'), ['int'])),
                            ('flow_accounting_start', (YLeaf(YType.uint32, 'flow-accounting-start'), ['int'])),
                            ('flow_accounting_stop', (YLeaf(YType.uint32, 'flow-accounting-stop'), ['int'])),
                            ('flow_accounting_update', (YLeaf(YType.uint32, 'flow-accounting-update'), ['int'])),
                            ('accounting_callback', (YLeaf(YType.uint32, 'accounting-callback'), ['int'])),
                            ('session_acct_trans_pending', (YLeaf(YType.uint32, 'session-acct-trans-pending'), ['int'])),
                            ('session_acct_reqs_failed', (YLeaf(YType.uint32, 'session-acct-reqs-failed'), ['int'])),
                            ('session_acct_out_of_sync', (YLeaf(YType.uint32, 'session-acct-out-of-sync'), ['int'])),
                            ('session_idle_to_trans_pending', (YLeaf(YType.uint32, 'session-idle-to-trans-pending'), ['int'])),
                            ('session_idle_to_reqs_failed', (YLeaf(YType.uint32, 'session-idle-to-reqs-failed'), ['int'])),
                            ('session_idle_to_out_of_sync', (YLeaf(YType.uint32, 'session-idle-to-out-of-sync'), ['int'])),
                            ('service_acct_trans_pending', (YLeaf(YType.uint32, 'service-acct-trans-pending'), ['int'])),
                            ('service_acct_reqs_failed', (YLeaf(YType.uint32, 'service-acct-reqs-failed'), ['int'])),
                            ('service_acct_out_of_sync', (YLeaf(YType.uint32, 'service-acct-out-of-sync'), ['int'])),
                            ('service_idle_to_trans_pending', (YLeaf(YType.uint32, 'service-idle-to-trans-pending'), ['int'])),
                            ('service_idle_to_reqs_failed', (YLeaf(YType.uint32, 'service-idle-to-reqs-failed'), ['int'])),
                            ('service_idle_to_out_of_sync', (YLeaf(YType.uint32, 'service-idle-to-out-of-sync'), ['int'])),
                            ('prepaid_start', (YLeaf(YType.uint32, 'prepaid-start'), ['int'])),
                            ('prepaid_stop', (YLeaf(YType.uint32, 'prepaid-stop'), ['int'])),
                            ('prepaid_accounting_start', (YLeaf(YType.uint32, 'prepaid-accounting-start'), ['int'])),
                            ('prepaid_accounting_stop', (YLeaf(YType.uint32, 'prepaid-accounting-stop'), ['int'])),
                            ('prepaid_volume_threshold_reached', (YLeaf(YType.uint32, 'prepaid-volume-threshold-reached'), ['int'])),
                            ('prepaid_time_threshold_reached', (YLeaf(YType.uint32, 'prepaid-time-threshold-reached'), ['int'])),
                            ('prepaid_quota_depleted', (YLeaf(YType.uint32, 'prepaid-quota-depleted'), ['int'])),
                            ('prepaid_reauthorization', (YLeaf(YType.uint32, 'prepaid-reauthorization'), ['int'])),
                            ('idle_timeout', (YLeaf(YType.uint32, 'idle-timeout'), ['int'])),
                            ('idle_timeout_response_callback', (YLeaf(YType.uint32, 'idle-timeout-response-callback'), ['int'])),
                            ('owned_resource_start', (YLeaf(YType.uint32, 'owned-resource-start'), ['int'])),
                        ])
                        self.flow_start = None
                        self.flow_disconnect = None
                        self.session_accounting_start = None
                        self.session_accounting_stop = None
                        self.session_accounting_update = None
                        self.service_accounting_start = None
                        self.service_accounting_stop = None
                        self.service_accounting_update = None
                        self.flow_accounting_start = None
                        self.flow_accounting_stop = None
                        self.flow_accounting_update = None
                        self.accounting_callback = None
                        self.session_acct_trans_pending = None
                        self.session_acct_reqs_failed = None
                        self.session_acct_out_of_sync = None
                        self.session_idle_to_trans_pending = None
                        self.session_idle_to_reqs_failed = None
                        self.session_idle_to_out_of_sync = None
                        self.service_acct_trans_pending = None
                        self.service_acct_reqs_failed = None
                        self.service_acct_out_of_sync = None
                        self.service_idle_to_trans_pending = None
                        self.service_idle_to_reqs_failed = None
                        self.service_idle_to_out_of_sync = None
                        self.prepaid_start = None
                        self.prepaid_stop = None
                        self.prepaid_accounting_start = None
                        self.prepaid_accounting_stop = None
                        self.prepaid_volume_threshold_reached = None
                        self.prepaid_time_threshold_reached = None
                        self.prepaid_quota_depleted = None
                        self.prepaid_reauthorization = None
                        self.idle_timeout = None
                        self.idle_timeout_response_callback = None
                        self.owned_resource_start = None
                        self._segment_path = lambda: "aaa-counters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters, [u'flow_start', u'flow_disconnect', u'session_accounting_start', u'session_accounting_stop', u'session_accounting_update', u'service_accounting_start', u'service_accounting_stop', u'service_accounting_update', u'flow_accounting_start', u'flow_accounting_stop', u'flow_accounting_update', u'accounting_callback', u'session_acct_trans_pending', u'session_acct_reqs_failed', u'session_acct_out_of_sync', u'session_idle_to_trans_pending', u'session_idle_to_reqs_failed', u'session_idle_to_out_of_sync', u'service_acct_trans_pending', u'service_acct_reqs_failed', u'service_acct_out_of_sync', u'service_idle_to_trans_pending', u'service_idle_to_reqs_failed', u'service_idle_to_out_of_sync', u'prepaid_start', u'prepaid_stop', u'prepaid_accounting_start', u'prepaid_accounting_stop', u'prepaid_volume_threshold_reached', u'prepaid_time_threshold_reached', u'prepaid_quota_depleted', u'prepaid_reauthorization', u'idle_timeout', u'idle_timeout_response_callback', u'owned_resource_start'], name, value)


                class IdleTimeoutCounters(Entity):
                    """
                    Accounting feature idle timeout summary counters
                    
                    .. attribute:: active_session_idle_timers
                    
                    	Number of Sessions with Idle Timeout Feature
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: idle_sessions
                    
                    	Number of Idle Sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: transitions_to_idle
                    
                    	Number of Sessions Transitions to Idle State
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: transitions_to_awake
                    
                    	Number of Sessions Transitions to Awake State
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active_flow_idle_timers
                    
                    	Number of Active Flow Idle Timers
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: expired_flow_idle_timers
                    
                    	Number of Flow Expired Idle Timers
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active_prepaid_idle_timers
                    
                    	Number of Active Prepaid Idle Timers
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: expired_prepaid_idle_timers
                    
                    	Number of Expired Prepaid Idle Timers
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-accounting-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters, self).__init__()

                        self.yang_name = "idle-timeout-counters"
                        self.yang_parent_name = "subscriber-accounting-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('active_session_idle_timers', (YLeaf(YType.uint32, 'active-session-idle-timers'), ['int'])),
                            ('idle_sessions', (YLeaf(YType.uint32, 'idle-sessions'), ['int'])),
                            ('transitions_to_idle', (YLeaf(YType.uint32, 'transitions-to-idle'), ['int'])),
                            ('transitions_to_awake', (YLeaf(YType.uint32, 'transitions-to-awake'), ['int'])),
                            ('active_flow_idle_timers', (YLeaf(YType.uint32, 'active-flow-idle-timers'), ['int'])),
                            ('expired_flow_idle_timers', (YLeaf(YType.uint32, 'expired-flow-idle-timers'), ['int'])),
                            ('active_prepaid_idle_timers', (YLeaf(YType.uint32, 'active-prepaid-idle-timers'), ['int'])),
                            ('expired_prepaid_idle_timers', (YLeaf(YType.uint32, 'expired-prepaid-idle-timers'), ['int'])),
                        ])
                        self.active_session_idle_timers = None
                        self.idle_sessions = None
                        self.transitions_to_idle = None
                        self.transitions_to_awake = None
                        self.active_flow_idle_timers = None
                        self.expired_flow_idle_timers = None
                        self.active_prepaid_idle_timers = None
                        self.expired_prepaid_idle_timers = None
                        self._segment_path = lambda: "idle-timeout-counters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters, [u'active_session_idle_timers', u'idle_sessions', u'transitions_to_idle', u'transitions_to_awake', u'active_flow_idle_timers', u'expired_flow_idle_timers', u'active_prepaid_idle_timers', u'expired_prepaid_idle_timers'], name, value)


                class SessionTimeoutCounters(Entity):
                    """
                    Accounting feature session timeout summary
                    counters
                    
                    .. attribute:: active_session_timers
                    
                    	Number of Active Session Timers
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: expired_session_timers
                    
                    	Number of Expired Session Timers
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-accounting-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters, self).__init__()

                        self.yang_name = "session-timeout-counters"
                        self.yang_parent_name = "subscriber-accounting-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('active_session_timers', (YLeaf(YType.uint32, 'active-session-timers'), ['int'])),
                            ('expired_session_timers', (YLeaf(YType.uint32, 'expired-session-timers'), ['int'])),
                        ])
                        self.active_session_timers = None
                        self.expired_session_timers = None
                        self._segment_path = lambda: "session-timeout-counters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters, [u'active_session_timers', u'expired_session_timers'], name, value)


                class SessionFlowCounters(Entity):
                    """
                    Accounting feature session context summary
                    counters
                    
                    .. attribute:: active_sessions
                    
                    	Number of Active Sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: disconnected_sessions
                    
                    	Number of Disconnected Sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active_session_accounting_sessions
                    
                    	Number of Active Sessions with Accounting
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active_flows
                    
                    	Number of Active Flows
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: quota_received
                    
                    	Number of flows for which Quota is received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-accounting-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters, self).__init__()

                        self.yang_name = "session-flow-counters"
                        self.yang_parent_name = "subscriber-accounting-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('active_sessions', (YLeaf(YType.uint32, 'active-sessions'), ['int'])),
                            ('disconnected_sessions', (YLeaf(YType.uint32, 'disconnected-sessions'), ['int'])),
                            ('active_session_accounting_sessions', (YLeaf(YType.uint32, 'active-session-accounting-sessions'), ['int'])),
                            ('active_flows', (YLeaf(YType.uint32, 'active-flows'), ['int'])),
                            ('quota_received', (YLeaf(YType.uint32, 'quota-received'), ['int'])),
                        ])
                        self.active_sessions = None
                        self.disconnected_sessions = None
                        self.active_session_accounting_sessions = None
                        self.active_flows = None
                        self.quota_received = None
                        self._segment_path = lambda: "session-flow-counters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters, [u'active_sessions', u'disconnected_sessions', u'active_session_accounting_sessions', u'active_flows', u'quota_received'], name, value)


            class SubscriberAccountingFlowFeatures(Entity):
                """
                Subscriber accounting flow feature data
                
                .. attribute:: subscriber_accounting_flow_feature
                
                	Display accounting flow features by unique subscriber label
                	**type**\: list of  		 :py:class:`SubscriberAccountingFlowFeature <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature>`
                
                

                """

                _prefix = 'subscriber-accounting-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures, self).__init__()

                    self.yang_name = "subscriber-accounting-flow-features"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("subscriber-accounting-flow-feature", ("subscriber_accounting_flow_feature", SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature))])
                    self._leafs = OrderedDict()

                    self.subscriber_accounting_flow_feature = YList(self)
                    self._segment_path = lambda: "subscriber-accounting-flow-features"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures, [], name, value)


                class SubscriberAccountingFlowFeature(Entity):
                    """
                    Display accounting flow features by unique
                    subscriber label
                    
                    .. attribute:: class_label  (key)
                    
                    	Unique subscriber class label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flow_feature_data
                    
                    	Accouting flow feature display data
                    	**type**\:  :py:class:`FlowFeatureData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData>`
                    
                    

                    """

                    _prefix = 'subscriber-accounting-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature, self).__init__()

                        self.yang_name = "subscriber-accounting-flow-feature"
                        self.yang_parent_name = "subscriber-accounting-flow-features"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['class_label']
                        self._child_classes = OrderedDict([("flow-feature-data", ("flow_feature_data", SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData))])
                        self._leafs = OrderedDict([
                            ('class_label', (YLeaf(YType.uint32, 'class-label'), ['int'])),
                        ])
                        self.class_label = None

                        self.flow_feature_data = SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData()
                        self.flow_feature_data.parent = self
                        self._children_name_map["flow_feature_data"] = "flow-feature-data"
                        self._segment_path = lambda: "subscriber-accounting-flow-feature" + "[class-label='" + str(self.class_label) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature, ['class_label'], name, value)


                    class FlowFeatureData(Entity):
                        """
                        Accouting flow feature display data
                        
                        .. attribute:: flow_accounting_enabled_flag
                        
                        	True if flow accounting is enabled
                        	**type**\: bool
                        
                        .. attribute:: flow_idle_timeout_enabled_flag
                        
                        	True if flow idle timeout is enabled
                        	**type**\: bool
                        
                        .. attribute:: prepaid_enabled_flag
                        
                        	True if prepaid is enabled
                        	**type**\: bool
                        
                        .. attribute:: prepaid_reauth_timer_enabled
                        
                        	Flag to specify if absolute timeout for ervice is enabled
                        	**type**\: bool
                        
                        .. attribute:: prepaid_idle_timeout_enabled
                        
                        	Flag to specify if idle timeout for service is enabled
                        	**type**\: bool
                        
                        .. attribute:: prepaid_final_unit
                        
                        	Prepaid final unit indication flag
                        	**type**\: bool
                        
                        .. attribute:: unique_class_label
                        
                        	Unique class label used to identify the flow
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: flow_direction
                        
                        	Direction of the flow. 0 = Ingress, 1 = Egress
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: flow_accounting_periodic_interval
                        
                        	Flow accounting periodic interval
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: flow_idle_timeout_value
                        
                        	Flow idle timeout value in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: prepaid_time_quota
                        
                        	Current prepaid time quota in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: prepaid_time_threshold
                        
                        	Current prepaid time threshold in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: prepaid_total_time_quota
                        
                        	Total accumulated prepaid time quota
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_volume_threshold
                        
                        	Current prepaid volume threshold in bytes
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_remaining_qt
                        
                        	The time remaing for QT timer to fire
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_remaining_qat
                        
                        	The time remaing for quota absolute timer to fire
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_remaining_qit
                        
                        	The time remaing for quota holding timer to fire 
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_remaining_qtt
                        
                        	The time remaining for tariff timer to fire
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_remaining_wheel
                        
                        	The time remaining for idle timer wheel to fire
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_tariff_time
                        
                        	The absolute time at which the traffic switch will occur expressed in UNIX time
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_idle_timeout_value
                        
                        	Prepaid idle timeout value in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: prepaid_reauth_timeout_value
                        
                        	The time at which the re\-authorization will occur
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_ccfh
                        
                        	Prepaid CCFH flag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_result_code
                        
                        	Prepaid authorization operation result code
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prepaid_volumei_quota
                        
                        	Current prepaid input volume quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volumeo_quota
                        
                        	Current prepaid output volume quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volumeb_quota
                        
                        	Current prepaid total volume quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_total_volumei_quota
                        
                        	Total accumulated input volume quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_total_volumeo_quota
                        
                        	Total accumulated output volume quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_total_volumeb_quota
                        
                        	Total accumulated total volume quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_usedi_quota
                        
                        	Accumulated input volume used quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_usedo_quota
                        
                        	Accumulated output volume used quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_refi_quota
                        
                        	Accumulated input volume reference quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_refo_quota
                        
                        	Accumulated output volume reference quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_refb_quota
                        
                        	Accumulated bi\-directional volume reference quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_agg_refi_quota
                        
                        	Total Accumulated input volume reference quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_agg_refo_quota
                        
                        	Total Accumulated output volume reference quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_agg_refb_quota
                        
                        	Total Accumulated bi\-directional volume reference quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_newi_quota
                        
                        	Newly arrvied input volume quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_newo_quota
                        
                        	Newly arrvied output volume quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_volume_newb_quota
                        
                        	Newly arrvied bi\-directional volume quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_tariff_volumei_quota
                        
                        	Total accumulated prepaid pre\-tarrif input volume quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_tariff_volumeo_quota
                        
                        	Total accumulated prepaid pre\-tarrif output volume quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: prepaid_tariff_volumeb_quota
                        
                        	Total accumulated prepaid pre\-tarrif total volume quota in bytes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: flow_accounting_method_list_name
                        
                        	Flow accounting method list name
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        .. attribute:: prepaid_cfg
                        
                        	Prepaid Config
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        .. attribute:: prepaid_time_state
                        
                        	Prepaid time state machine state
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        .. attribute:: prepaid_volume_state
                        
                        	Prepaid volume state machine state
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        .. attribute:: prepaid_charging_rule
                        
                        	Prepaid charging rule name string
                        	**type**\: str
                        
                        	**length:** 0..256
                        
                        

                        """

                        _prefix = 'subscriber-accounting-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData, self).__init__()

                            self.yang_name = "flow-feature-data"
                            self.yang_parent_name = "subscriber-accounting-flow-feature"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('flow_accounting_enabled_flag', (YLeaf(YType.boolean, 'flow-accounting-enabled-flag'), ['bool'])),
                                ('flow_idle_timeout_enabled_flag', (YLeaf(YType.boolean, 'flow-idle-timeout-enabled-flag'), ['bool'])),
                                ('prepaid_enabled_flag', (YLeaf(YType.boolean, 'prepaid-enabled-flag'), ['bool'])),
                                ('prepaid_reauth_timer_enabled', (YLeaf(YType.boolean, 'prepaid-reauth-timer-enabled'), ['bool'])),
                                ('prepaid_idle_timeout_enabled', (YLeaf(YType.boolean, 'prepaid-idle-timeout-enabled'), ['bool'])),
                                ('prepaid_final_unit', (YLeaf(YType.boolean, 'prepaid-final-unit'), ['bool'])),
                                ('unique_class_label', (YLeaf(YType.uint32, 'unique-class-label'), ['int'])),
                                ('flow_direction', (YLeaf(YType.uint32, 'flow-direction'), ['int'])),
                                ('flow_accounting_periodic_interval', (YLeaf(YType.uint32, 'flow-accounting-periodic-interval'), ['int'])),
                                ('flow_idle_timeout_value', (YLeaf(YType.uint32, 'flow-idle-timeout-value'), ['int'])),
                                ('prepaid_time_quota', (YLeaf(YType.uint32, 'prepaid-time-quota'), ['int'])),
                                ('prepaid_time_threshold', (YLeaf(YType.uint32, 'prepaid-time-threshold'), ['int'])),
                                ('prepaid_total_time_quota', (YLeaf(YType.uint32, 'prepaid-total-time-quota'), ['int'])),
                                ('prepaid_volume_threshold', (YLeaf(YType.uint32, 'prepaid-volume-threshold'), ['int'])),
                                ('prepaid_remaining_qt', (YLeaf(YType.uint32, 'prepaid-remaining-qt'), ['int'])),
                                ('prepaid_remaining_qat', (YLeaf(YType.uint32, 'prepaid-remaining-qat'), ['int'])),
                                ('prepaid_remaining_qit', (YLeaf(YType.uint32, 'prepaid-remaining-qit'), ['int'])),
                                ('prepaid_remaining_qtt', (YLeaf(YType.uint32, 'prepaid-remaining-qtt'), ['int'])),
                                ('prepaid_remaining_wheel', (YLeaf(YType.uint32, 'prepaid-remaining-wheel'), ['int'])),
                                ('prepaid_tariff_time', (YLeaf(YType.uint32, 'prepaid-tariff-time'), ['int'])),
                                ('prepaid_idle_timeout_value', (YLeaf(YType.uint32, 'prepaid-idle-timeout-value'), ['int'])),
                                ('prepaid_reauth_timeout_value', (YLeaf(YType.uint32, 'prepaid-reauth-timeout-value'), ['int'])),
                                ('prepaid_ccfh', (YLeaf(YType.uint32, 'prepaid-ccfh'), ['int'])),
                                ('prepaid_result_code', (YLeaf(YType.uint32, 'prepaid-result-code'), ['int'])),
                                ('prepaid_volumei_quota', (YLeaf(YType.uint64, 'prepaid-volumei-quota'), ['int'])),
                                ('prepaid_volumeo_quota', (YLeaf(YType.uint64, 'prepaid-volumeo-quota'), ['int'])),
                                ('prepaid_volumeb_quota', (YLeaf(YType.uint64, 'prepaid-volumeb-quota'), ['int'])),
                                ('prepaid_total_volumei_quota', (YLeaf(YType.uint64, 'prepaid-total-volumei-quota'), ['int'])),
                                ('prepaid_total_volumeo_quota', (YLeaf(YType.uint64, 'prepaid-total-volumeo-quota'), ['int'])),
                                ('prepaid_total_volumeb_quota', (YLeaf(YType.uint64, 'prepaid-total-volumeb-quota'), ['int'])),
                                ('prepaid_volume_usedi_quota', (YLeaf(YType.uint64, 'prepaid-volume-usedi-quota'), ['int'])),
                                ('prepaid_volume_usedo_quota', (YLeaf(YType.uint64, 'prepaid-volume-usedo-quota'), ['int'])),
                                ('prepaid_volume_refi_quota', (YLeaf(YType.uint64, 'prepaid-volume-refi-quota'), ['int'])),
                                ('prepaid_volume_refo_quota', (YLeaf(YType.uint64, 'prepaid-volume-refo-quota'), ['int'])),
                                ('prepaid_volume_refb_quota', (YLeaf(YType.uint64, 'prepaid-volume-refb-quota'), ['int'])),
                                ('prepaid_volume_agg_refi_quota', (YLeaf(YType.uint64, 'prepaid-volume-agg-refi-quota'), ['int'])),
                                ('prepaid_volume_agg_refo_quota', (YLeaf(YType.uint64, 'prepaid-volume-agg-refo-quota'), ['int'])),
                                ('prepaid_volume_agg_refb_quota', (YLeaf(YType.uint64, 'prepaid-volume-agg-refb-quota'), ['int'])),
                                ('prepaid_volume_newi_quota', (YLeaf(YType.uint64, 'prepaid-volume-newi-quota'), ['int'])),
                                ('prepaid_volume_newo_quota', (YLeaf(YType.uint64, 'prepaid-volume-newo-quota'), ['int'])),
                                ('prepaid_volume_newb_quota', (YLeaf(YType.uint64, 'prepaid-volume-newb-quota'), ['int'])),
                                ('prepaid_tariff_volumei_quota', (YLeaf(YType.uint64, 'prepaid-tariff-volumei-quota'), ['int'])),
                                ('prepaid_tariff_volumeo_quota', (YLeaf(YType.uint64, 'prepaid-tariff-volumeo-quota'), ['int'])),
                                ('prepaid_tariff_volumeb_quota', (YLeaf(YType.uint64, 'prepaid-tariff-volumeb-quota'), ['int'])),
                                ('flow_accounting_method_list_name', (YLeaf(YType.str, 'flow-accounting-method-list-name'), ['str'])),
                                ('prepaid_cfg', (YLeaf(YType.str, 'prepaid-cfg'), ['str'])),
                                ('prepaid_time_state', (YLeaf(YType.str, 'prepaid-time-state'), ['str'])),
                                ('prepaid_volume_state', (YLeaf(YType.str, 'prepaid-volume-state'), ['str'])),
                                ('prepaid_charging_rule', (YLeaf(YType.str, 'prepaid-charging-rule'), ['str'])),
                            ])
                            self.flow_accounting_enabled_flag = None
                            self.flow_idle_timeout_enabled_flag = None
                            self.prepaid_enabled_flag = None
                            self.prepaid_reauth_timer_enabled = None
                            self.prepaid_idle_timeout_enabled = None
                            self.prepaid_final_unit = None
                            self.unique_class_label = None
                            self.flow_direction = None
                            self.flow_accounting_periodic_interval = None
                            self.flow_idle_timeout_value = None
                            self.prepaid_time_quota = None
                            self.prepaid_time_threshold = None
                            self.prepaid_total_time_quota = None
                            self.prepaid_volume_threshold = None
                            self.prepaid_remaining_qt = None
                            self.prepaid_remaining_qat = None
                            self.prepaid_remaining_qit = None
                            self.prepaid_remaining_qtt = None
                            self.prepaid_remaining_wheel = None
                            self.prepaid_tariff_time = None
                            self.prepaid_idle_timeout_value = None
                            self.prepaid_reauth_timeout_value = None
                            self.prepaid_ccfh = None
                            self.prepaid_result_code = None
                            self.prepaid_volumei_quota = None
                            self.prepaid_volumeo_quota = None
                            self.prepaid_volumeb_quota = None
                            self.prepaid_total_volumei_quota = None
                            self.prepaid_total_volumeo_quota = None
                            self.prepaid_total_volumeb_quota = None
                            self.prepaid_volume_usedi_quota = None
                            self.prepaid_volume_usedo_quota = None
                            self.prepaid_volume_refi_quota = None
                            self.prepaid_volume_refo_quota = None
                            self.prepaid_volume_refb_quota = None
                            self.prepaid_volume_agg_refi_quota = None
                            self.prepaid_volume_agg_refo_quota = None
                            self.prepaid_volume_agg_refb_quota = None
                            self.prepaid_volume_newi_quota = None
                            self.prepaid_volume_newo_quota = None
                            self.prepaid_volume_newb_quota = None
                            self.prepaid_tariff_volumei_quota = None
                            self.prepaid_tariff_volumeo_quota = None
                            self.prepaid_tariff_volumeb_quota = None
                            self.flow_accounting_method_list_name = None
                            self.prepaid_cfg = None
                            self.prepaid_time_state = None
                            self.prepaid_volume_state = None
                            self.prepaid_charging_rule = None
                            self._segment_path = lambda: "flow-feature-data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData, [u'flow_accounting_enabled_flag', u'flow_idle_timeout_enabled_flag', u'prepaid_enabled_flag', u'prepaid_reauth_timer_enabled', u'prepaid_idle_timeout_enabled', u'prepaid_final_unit', u'unique_class_label', u'flow_direction', u'flow_accounting_periodic_interval', u'flow_idle_timeout_value', u'prepaid_time_quota', u'prepaid_time_threshold', u'prepaid_total_time_quota', u'prepaid_volume_threshold', u'prepaid_remaining_qt', u'prepaid_remaining_qat', u'prepaid_remaining_qit', u'prepaid_remaining_qtt', u'prepaid_remaining_wheel', u'prepaid_tariff_time', u'prepaid_idle_timeout_value', u'prepaid_reauth_timeout_value', u'prepaid_ccfh', u'prepaid_result_code', u'prepaid_volumei_quota', u'prepaid_volumeo_quota', u'prepaid_volumeb_quota', u'prepaid_total_volumei_quota', u'prepaid_total_volumeo_quota', u'prepaid_total_volumeb_quota', u'prepaid_volume_usedi_quota', u'prepaid_volume_usedo_quota', u'prepaid_volume_refi_quota', u'prepaid_volume_refo_quota', u'prepaid_volume_refb_quota', u'prepaid_volume_agg_refi_quota', u'prepaid_volume_agg_refo_quota', u'prepaid_volume_agg_refb_quota', u'prepaid_volume_newi_quota', u'prepaid_volume_newo_quota', u'prepaid_volume_newb_quota', u'prepaid_tariff_volumei_quota', u'prepaid_tariff_volumeo_quota', u'prepaid_tariff_volumeb_quota', u'flow_accounting_method_list_name', u'prepaid_cfg', u'prepaid_time_state', u'prepaid_volume_state', u'prepaid_charging_rule'], name, value)

    def clone_ptr(self):
        self._top_entity = SubscriberAccounting()
        return self._top_entity

