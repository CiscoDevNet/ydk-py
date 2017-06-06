""" Cisco_IOS_XR_subscriber_accounting_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-accounting package operational data.

This module contains definitions
for the following management objects\:
  subscriber\-accounting\: Subscriber accounting operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class SubscriberAccounting(object):
    """
    Subscriber accounting operational data
    
    .. attribute:: nodes
    
    	Subscriber accounting operational data for a particular location
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes>`
    
    

    """

    _prefix = 'subscriber-accounting-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = SubscriberAccounting.Nodes()
        self.nodes.parent = self


    class Nodes(object):
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
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
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
                self.parent = None
                self.node_id = None
                self.subscriber_accounting_flow_features = SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures()
                self.subscriber_accounting_flow_features.parent = self
                self.subscriber_accounting_session_features = SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures()
                self.subscriber_accounting_session_features.parent = self
                self.subscriber_accounting_summary = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary()
                self.subscriber_accounting_summary.parent = self


            class SubscriberAccountingSessionFeatures(object):
                """
                Subscriber accounting session feature data
                
                .. attribute:: subscriber_accounting_session_feature
                
                	Display accounting session features by unique subscriber label
                	**type**\: list of    :py:class:`SubscriberAccountingSessionFeature <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature>`
                
                

                """

                _prefix = 'subscriber-accounting-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.subscriber_accounting_session_feature = YList()
                    self.subscriber_accounting_session_feature.parent = self
                    self.subscriber_accounting_session_feature.name = 'subscriber_accounting_session_feature'


                class SubscriberAccountingSessionFeature(object):
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
                        self.parent = None
                        self.sub_label = None
                        self.session_feature_data = SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData()
                        self.session_feature_data.parent = self


                    class SessionFeatureData(object):
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
                            self.parent = None
                            self.idle_timeout_direction = None
                            self.idle_timeout_threshold = None
                            self.idle_timeout_value = None
                            self.interface_handle = None
                            self.service_accounting_feature = YList()
                            self.service_accounting_feature.parent = self
                            self.service_accounting_feature.name = 'service_accounting_feature'
                            self.session_accounting_aaa_request_failed = None
                            self.session_accounting_aaa_trans_pending = None
                            self.session_accounting_enabled_flag = None
                            self.session_accounting_method_list = None
                            self.session_accounting_periodic_interval = None
                            self.session_accounting_started = None
                            self.session_disconnected = None
                            self.session_idle_timeout_enabled_flag = None
                            self.session_idle_to_aaa_request_failed = None
                            self.session_idle_to_aaa_trans_pending = None
                            self.session_is_idle = None
                            self.session_stats_changed_time = None
                            self.session_timeout_enabled_flag = None
                            self.session_timeout_time_remaining = None
                            self.session_timeout_value = None
                            self.session_to_awake_count = None
                            self.session_to_idle_count = None
                            self.session_total_idle_time = None
                            self.unique_subscriber_label = None


                        class ServiceAccountingFeature(object):
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
                                self.parent = None
                                self.service_accounting_enabled_flag = None
                                self.service_accounting_method_list = None
                                self.service_accounting_periodic_interval = None
                                self.service_accounting_service_id = None
                                self.session_accounting_aaa_request_failed = None
                                self.session_accounting_aaa_trans_pending = None
                                self.session_accounting_started = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-subscriber-accounting-oper:service-accounting-feature'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.service_accounting_enabled_flag is not None:
                                    return True

                                if self.service_accounting_method_list is not None:
                                    return True

                                if self.service_accounting_periodic_interval is not None:
                                    return True

                                if self.service_accounting_service_id is not None:
                                    return True

                                if self.session_accounting_aaa_request_failed is not None:
                                    return True

                                if self.session_accounting_aaa_trans_pending is not None:
                                    return True

                                if self.session_accounting_started is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
                                return meta._meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-accounting-oper:session-feature-data'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.idle_timeout_direction is not None:
                                return True

                            if self.idle_timeout_threshold is not None:
                                return True

                            if self.idle_timeout_value is not None:
                                return True

                            if self.interface_handle is not None:
                                return True

                            if self.service_accounting_feature is not None:
                                for child_ref in self.service_accounting_feature:
                                    if child_ref._has_data():
                                        return True

                            if self.session_accounting_aaa_request_failed is not None:
                                return True

                            if self.session_accounting_aaa_trans_pending is not None:
                                return True

                            if self.session_accounting_enabled_flag is not None:
                                return True

                            if self.session_accounting_method_list is not None:
                                return True

                            if self.session_accounting_periodic_interval is not None:
                                return True

                            if self.session_accounting_started is not None:
                                return True

                            if self.session_disconnected is not None:
                                return True

                            if self.session_idle_timeout_enabled_flag is not None:
                                return True

                            if self.session_idle_to_aaa_request_failed is not None:
                                return True

                            if self.session_idle_to_aaa_trans_pending is not None:
                                return True

                            if self.session_is_idle is not None:
                                return True

                            if self.session_stats_changed_time is not None:
                                return True

                            if self.session_timeout_enabled_flag is not None:
                                return True

                            if self.session_timeout_time_remaining is not None:
                                return True

                            if self.session_timeout_value is not None:
                                return True

                            if self.session_to_awake_count is not None:
                                return True

                            if self.session_to_idle_count is not None:
                                return True

                            if self.session_total_idle_time is not None:
                                return True

                            if self.unique_subscriber_label is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
                            return meta._meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.sub_label is None:
                            raise YPYModelError('Key property sub_label is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting-session-feature[Cisco-IOS-XR-subscriber-accounting-oper:sub-label = ' + str(self.sub_label) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.sub_label is not None:
                            return True

                        if self.session_feature_data is not None and self.session_feature_data._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
                        return meta._meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting-session-features'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.subscriber_accounting_session_feature is not None:
                        for child_ref in self.subscriber_accounting_session_feature:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
                    return meta._meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures']['meta_info']


            class SubscriberAccountingSummary(object):
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
                    self.parent = None
                    self.aaa_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters()
                    self.aaa_counters.parent = self
                    self.idle_timeout_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters()
                    self.idle_timeout_counters.parent = self
                    self.session_flow_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters()
                    self.session_flow_counters.parent = self
                    self.session_timeout_counters = SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters()
                    self.session_timeout_counters.parent = self


                class AaaCounters(object):
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
                        self.parent = None
                        self.accounting_callback = None
                        self.flow_accounting_start = None
                        self.flow_accounting_stop = None
                        self.flow_accounting_update = None
                        self.flow_disconnect = None
                        self.flow_start = None
                        self.idle_timeout = None
                        self.idle_timeout_response_callback = None
                        self.owned_resource_start = None
                        self.prepaid_accounting_start = None
                        self.prepaid_accounting_stop = None
                        self.prepaid_quota_depleted = None
                        self.prepaid_reauthorization = None
                        self.prepaid_start = None
                        self.prepaid_stop = None
                        self.prepaid_time_threshold_reached = None
                        self.prepaid_volume_threshold_reached = None
                        self.service_accounting_start = None
                        self.service_accounting_stop = None
                        self.service_accounting_update = None
                        self.service_acct_out_of_sync = None
                        self.service_acct_reqs_failed = None
                        self.service_acct_trans_pending = None
                        self.service_idle_to_out_of_sync = None
                        self.service_idle_to_reqs_failed = None
                        self.service_idle_to_trans_pending = None
                        self.session_accounting_start = None
                        self.session_accounting_stop = None
                        self.session_accounting_update = None
                        self.session_acct_out_of_sync = None
                        self.session_acct_reqs_failed = None
                        self.session_acct_trans_pending = None
                        self.session_idle_to_out_of_sync = None
                        self.session_idle_to_reqs_failed = None
                        self.session_idle_to_trans_pending = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-accounting-oper:aaa-counters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.accounting_callback is not None:
                            return True

                        if self.flow_accounting_start is not None:
                            return True

                        if self.flow_accounting_stop is not None:
                            return True

                        if self.flow_accounting_update is not None:
                            return True

                        if self.flow_disconnect is not None:
                            return True

                        if self.flow_start is not None:
                            return True

                        if self.idle_timeout is not None:
                            return True

                        if self.idle_timeout_response_callback is not None:
                            return True

                        if self.owned_resource_start is not None:
                            return True

                        if self.prepaid_accounting_start is not None:
                            return True

                        if self.prepaid_accounting_stop is not None:
                            return True

                        if self.prepaid_quota_depleted is not None:
                            return True

                        if self.prepaid_reauthorization is not None:
                            return True

                        if self.prepaid_start is not None:
                            return True

                        if self.prepaid_stop is not None:
                            return True

                        if self.prepaid_time_threshold_reached is not None:
                            return True

                        if self.prepaid_volume_threshold_reached is not None:
                            return True

                        if self.service_accounting_start is not None:
                            return True

                        if self.service_accounting_stop is not None:
                            return True

                        if self.service_accounting_update is not None:
                            return True

                        if self.service_acct_out_of_sync is not None:
                            return True

                        if self.service_acct_reqs_failed is not None:
                            return True

                        if self.service_acct_trans_pending is not None:
                            return True

                        if self.service_idle_to_out_of_sync is not None:
                            return True

                        if self.service_idle_to_reqs_failed is not None:
                            return True

                        if self.service_idle_to_trans_pending is not None:
                            return True

                        if self.session_accounting_start is not None:
                            return True

                        if self.session_accounting_stop is not None:
                            return True

                        if self.session_accounting_update is not None:
                            return True

                        if self.session_acct_out_of_sync is not None:
                            return True

                        if self.session_acct_reqs_failed is not None:
                            return True

                        if self.session_acct_trans_pending is not None:
                            return True

                        if self.session_idle_to_out_of_sync is not None:
                            return True

                        if self.session_idle_to_reqs_failed is not None:
                            return True

                        if self.session_idle_to_trans_pending is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
                        return meta._meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters']['meta_info']


                class IdleTimeoutCounters(object):
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
                        self.parent = None
                        self.active_flow_idle_timers = None
                        self.active_prepaid_idle_timers = None
                        self.active_session_idle_timers = None
                        self.expired_flow_idle_timers = None
                        self.expired_prepaid_idle_timers = None
                        self.idle_sessions = None
                        self.transitions_to_awake = None
                        self.transitions_to_idle = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-accounting-oper:idle-timeout-counters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.active_flow_idle_timers is not None:
                            return True

                        if self.active_prepaid_idle_timers is not None:
                            return True

                        if self.active_session_idle_timers is not None:
                            return True

                        if self.expired_flow_idle_timers is not None:
                            return True

                        if self.expired_prepaid_idle_timers is not None:
                            return True

                        if self.idle_sessions is not None:
                            return True

                        if self.transitions_to_awake is not None:
                            return True

                        if self.transitions_to_idle is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
                        return meta._meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters']['meta_info']


                class SessionTimeoutCounters(object):
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
                        self.parent = None
                        self.active_session_timers = None
                        self.expired_session_timers = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-accounting-oper:session-timeout-counters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.active_session_timers is not None:
                            return True

                        if self.expired_session_timers is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
                        return meta._meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters']['meta_info']


                class SessionFlowCounters(object):
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
                        self.parent = None
                        self.active_flows = None
                        self.active_session_accounting_sessions = None
                        self.active_sessions = None
                        self.disconnected_sessions = None
                        self.quota_received = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-accounting-oper:session-flow-counters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.active_flows is not None:
                            return True

                        if self.active_session_accounting_sessions is not None:
                            return True

                        if self.active_sessions is not None:
                            return True

                        if self.disconnected_sessions is not None:
                            return True

                        if self.quota_received is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
                        return meta._meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.aaa_counters is not None and self.aaa_counters._has_data():
                        return True

                    if self.idle_timeout_counters is not None and self.idle_timeout_counters._has_data():
                        return True

                    if self.session_flow_counters is not None and self.session_flow_counters._has_data():
                        return True

                    if self.session_timeout_counters is not None and self.session_timeout_counters._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
                    return meta._meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary']['meta_info']


            class SubscriberAccountingFlowFeatures(object):
                """
                Subscriber accounting flow feature data
                
                .. attribute:: subscriber_accounting_flow_feature
                
                	Display accounting flow features by unique subscriber label
                	**type**\: list of    :py:class:`SubscriberAccountingFlowFeature <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper.SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature>`
                
                

                """

                _prefix = 'subscriber-accounting-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.subscriber_accounting_flow_feature = YList()
                    self.subscriber_accounting_flow_feature.parent = self
                    self.subscriber_accounting_flow_feature.name = 'subscriber_accounting_flow_feature'


                class SubscriberAccountingFlowFeature(object):
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
                        self.parent = None
                        self.class_label = None
                        self.flow_feature_data = SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData()
                        self.flow_feature_data.parent = self


                    class FlowFeatureData(object):
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
                            self.parent = None
                            self.flow_accounting_enabled_flag = None
                            self.flow_accounting_method_list_name = None
                            self.flow_accounting_periodic_interval = None
                            self.flow_direction = None
                            self.flow_idle_timeout_enabled_flag = None
                            self.flow_idle_timeout_value = None
                            self.prepaid_ccfh = None
                            self.prepaid_cfg = None
                            self.prepaid_charging_rule = None
                            self.prepaid_enabled_flag = None
                            self.prepaid_final_unit = None
                            self.prepaid_idle_timeout_enabled = None
                            self.prepaid_idle_timeout_value = None
                            self.prepaid_reauth_timeout_value = None
                            self.prepaid_reauth_timer_enabled = None
                            self.prepaid_remaining_qat = None
                            self.prepaid_remaining_qit = None
                            self.prepaid_remaining_qt = None
                            self.prepaid_remaining_qtt = None
                            self.prepaid_remaining_wheel = None
                            self.prepaid_result_code = None
                            self.prepaid_tariff_time = None
                            self.prepaid_tariff_volumeb_quota = None
                            self.prepaid_tariff_volumei_quota = None
                            self.prepaid_tariff_volumeo_quota = None
                            self.prepaid_time_quota = None
                            self.prepaid_time_state = None
                            self.prepaid_time_threshold = None
                            self.prepaid_total_time_quota = None
                            self.prepaid_total_volumeb_quota = None
                            self.prepaid_total_volumei_quota = None
                            self.prepaid_total_volumeo_quota = None
                            self.prepaid_volume_newb_quota = None
                            self.prepaid_volume_newi_quota = None
                            self.prepaid_volume_newo_quota = None
                            self.prepaid_volume_refb_quota = None
                            self.prepaid_volume_refi_quota = None
                            self.prepaid_volume_refo_quota = None
                            self.prepaid_volume_state = None
                            self.prepaid_volume_threshold = None
                            self.prepaid_volume_usedi_quota = None
                            self.prepaid_volume_usedo_quota = None
                            self.prepaid_volumeb_quota = None
                            self.prepaid_volumei_quota = None
                            self.prepaid_volumeo_quota = None
                            self.unique_class_label = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-accounting-oper:flow-feature-data'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.flow_accounting_enabled_flag is not None:
                                return True

                            if self.flow_accounting_method_list_name is not None:
                                return True

                            if self.flow_accounting_periodic_interval is not None:
                                return True

                            if self.flow_direction is not None:
                                return True

                            if self.flow_idle_timeout_enabled_flag is not None:
                                return True

                            if self.flow_idle_timeout_value is not None:
                                return True

                            if self.prepaid_ccfh is not None:
                                return True

                            if self.prepaid_cfg is not None:
                                return True

                            if self.prepaid_charging_rule is not None:
                                return True

                            if self.prepaid_enabled_flag is not None:
                                return True

                            if self.prepaid_final_unit is not None:
                                return True

                            if self.prepaid_idle_timeout_enabled is not None:
                                return True

                            if self.prepaid_idle_timeout_value is not None:
                                return True

                            if self.prepaid_reauth_timeout_value is not None:
                                return True

                            if self.prepaid_reauth_timer_enabled is not None:
                                return True

                            if self.prepaid_remaining_qat is not None:
                                return True

                            if self.prepaid_remaining_qit is not None:
                                return True

                            if self.prepaid_remaining_qt is not None:
                                return True

                            if self.prepaid_remaining_qtt is not None:
                                return True

                            if self.prepaid_remaining_wheel is not None:
                                return True

                            if self.prepaid_result_code is not None:
                                return True

                            if self.prepaid_tariff_time is not None:
                                return True

                            if self.prepaid_tariff_volumeb_quota is not None:
                                return True

                            if self.prepaid_tariff_volumei_quota is not None:
                                return True

                            if self.prepaid_tariff_volumeo_quota is not None:
                                return True

                            if self.prepaid_time_quota is not None:
                                return True

                            if self.prepaid_time_state is not None:
                                return True

                            if self.prepaid_time_threshold is not None:
                                return True

                            if self.prepaid_total_time_quota is not None:
                                return True

                            if self.prepaid_total_volumeb_quota is not None:
                                return True

                            if self.prepaid_total_volumei_quota is not None:
                                return True

                            if self.prepaid_total_volumeo_quota is not None:
                                return True

                            if self.prepaid_volume_newb_quota is not None:
                                return True

                            if self.prepaid_volume_newi_quota is not None:
                                return True

                            if self.prepaid_volume_newo_quota is not None:
                                return True

                            if self.prepaid_volume_refb_quota is not None:
                                return True

                            if self.prepaid_volume_refi_quota is not None:
                                return True

                            if self.prepaid_volume_refo_quota is not None:
                                return True

                            if self.prepaid_volume_state is not None:
                                return True

                            if self.prepaid_volume_threshold is not None:
                                return True

                            if self.prepaid_volume_usedi_quota is not None:
                                return True

                            if self.prepaid_volume_usedo_quota is not None:
                                return True

                            if self.prepaid_volumeb_quota is not None:
                                return True

                            if self.prepaid_volumei_quota is not None:
                                return True

                            if self.prepaid_volumeo_quota is not None:
                                return True

                            if self.unique_class_label is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
                            return meta._meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.class_label is None:
                            raise YPYModelError('Key property class_label is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting-flow-feature[Cisco-IOS-XR-subscriber-accounting-oper:class-label = ' + str(self.class_label) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.class_label is not None:
                            return True

                        if self.flow_feature_data is not None and self.flow_feature_data._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
                        return meta._meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting-flow-features'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.subscriber_accounting_flow_feature is not None:
                        for child_ref in self.subscriber_accounting_flow_feature:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
                    return meta._meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures']['meta_info']

            @property
            def _common_path(self):
                if self.node_id is None:
                    raise YPYModelError('Key property node_id is None')

                return '/Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting/Cisco-IOS-XR-subscriber-accounting-oper:nodes/Cisco-IOS-XR-subscriber-accounting-oper:node[Cisco-IOS-XR-subscriber-accounting-oper:node-id = ' + str(self.node_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_id is not None:
                    return True

                if self.subscriber_accounting_flow_features is not None and self.subscriber_accounting_flow_features._has_data():
                    return True

                if self.subscriber_accounting_session_features is not None and self.subscriber_accounting_session_features._has_data():
                    return True

                if self.subscriber_accounting_summary is not None and self.subscriber_accounting_summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
                return meta._meta_table['SubscriberAccounting.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting/Cisco-IOS-XR-subscriber-accounting-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
            return meta._meta_table['SubscriberAccounting.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-subscriber-accounting-oper:subscriber-accounting'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_accounting_oper as meta
        return meta._meta_table['SubscriberAccounting']['meta_info']


