


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature',
            False, 
            [
            _MetaInfoClassMember('service-accounting-enabled-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if service accounting is enabled
                ''',
                'service_accounting_enabled_flag',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('service-accounting-method-list', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Service accounting method list name
                ''',
                'service_accounting_method_list',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('service-accounting-periodic-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Service accounting periodic interval
                ''',
                'service_accounting_periodic_interval',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('service-accounting-service-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Service accounting service ID
                ''',
                'service_accounting_service_id',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-accounting-aaa-request-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Service Accounting AAA request
                failures for the service
                ''',
                'session_accounting_aaa_request_failed',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-accounting-aaa-trans-pending', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Service Accounting AAA transactions
                pending for the service
                ''',
                'session_accounting_aaa_trans_pending',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-accounting-started', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if Service accounting started  for the
                service
                ''',
                'session_accounting_started',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'service-accounting-feature',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
    'SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData',
            False, 
            [
            _MetaInfoClassMember('idle-timeout-direction', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Idle timeout direction
                ''',
                'idle_timeout_direction',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('idle-timeout-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Idle timeout threshold in minutes per packets
                ''',
                'idle_timeout_threshold',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('idle-timeout-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Idle timeout value in seconds
                ''',
                'idle_timeout_value',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Handle of interface associated with the session
                ''',
                'interface_handle',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('service-accounting-feature', REFERENCE_LIST, 'ServiceAccountingFeature' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper', 'SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature', 
                [], [], 
                '''                List of service accounting features
                ''',
                'service_accounting_feature',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-accounting-aaa-request-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Accounting AAA request
                failures
                ''',
                'session_accounting_aaa_request_failed',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-accounting-aaa-trans-pending', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Accounting AAA transactions
                pending
                ''',
                'session_accounting_aaa_trans_pending',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-accounting-enabled-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if session accounting is enabled
                ''',
                'session_accounting_enabled_flag',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-accounting-method-list', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Session accounting method list name
                ''',
                'session_accounting_method_list',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-accounting-periodic-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session accounting periodic interval
                ''',
                'session_accounting_periodic_interval',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-accounting-started', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if session accounting started
                ''',
                'session_accounting_started',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-disconnected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if session is disconnected
                ''',
                'session_disconnected',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-idle-timeout-enabled-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if session idle timeout is enabled
                ''',
                'session_idle_timeout_enabled_flag',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-idle-to-aaa-request-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Idle AAA request failures
                ''',
                'session_idle_to_aaa_request_failed',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-idle-to-aaa-trans-pending', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Idle AAA transactions pending
                ''',
                'session_idle_to_aaa_trans_pending',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-is-idle', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if session is idle
                ''',
                'session_is_idle',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-stats-changed-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last time session data was received
                ''',
                'session_stats_changed_time',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-timeout-enabled-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if session timeout is enabled
                ''',
                'session_timeout_enabled_flag',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-timeout-time-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number seconds remaining before session times
                out
                ''',
                'session_timeout_time_remaining',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-timeout-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session timeout value in seconds
                ''',
                'session_timeout_value',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-to-awake-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Awake AAA events
                ''',
                'session_to_awake_count',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-to-idle-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Idle AAA events
                ''',
                'session_to_idle_count',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-total-idle-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total time session has been idle
                ''',
                'session_total_idle_time',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('unique-subscriber-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unique subscriber label used to identify the
                session
                ''',
                'unique_subscriber_label',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'session-feature-data',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
    'SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature',
            False, 
            [
            _MetaInfoClassMember('sub-label', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Unique subscriber label
                ''',
                'sub_label',
                'Cisco-IOS-XR-subscriber-accounting-oper', True),
            _MetaInfoClassMember('session-feature-data', REFERENCE_CLASS, 'SessionFeatureData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper', 'SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData', 
                [], [], 
                '''                Accounting session feature display data
                ''',
                'session_feature_data',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'subscriber-accounting-session-feature',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
    'SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures',
            False, 
            [
            _MetaInfoClassMember('subscriber-accounting-session-feature', REFERENCE_LIST, 'SubscriberAccountingSessionFeature' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper', 'SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature', 
                [], [], 
                '''                Display accounting session features by unique
                subscriber label
                ''',
                'subscriber_accounting_session_feature',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'subscriber-accounting-session-features',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
    'SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters',
            False, 
            [
            _MetaInfoClassMember('accounting-callback', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Accounting Callbacks Received
                ''',
                'accounting_callback',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('flow-accounting-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Flow Accounting Start Requests Sent
                ''',
                'flow_accounting_start',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('flow-accounting-stop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Flow Accounting Stop Requests Sent
                ''',
                'flow_accounting_stop',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('flow-accounting-update', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Flow Accounting Update Requests Sent
                ''',
                'flow_accounting_update',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('flow-disconnect', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Flow Disconnect Requests Sent
                ''',
                'flow_disconnect',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('flow-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Flow Start Requests Sent
                ''',
                'flow_start',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('idle-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Idle Timeout Events Sent
                ''',
                'idle_timeout',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('idle-timeout-response-callback', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Idle Timeout Callbacks Received
                ''',
                'idle_timeout_response_callback',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('owned-resource-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Owned Resource Starts
                ''',
                'owned_resource_start',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-accounting-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Prepaid Accounting Start Requests Sent
                ''',
                'prepaid_accounting_start',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-accounting-stop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Prepaid Accounting Stop Requests Sent
                ''',
                'prepaid_accounting_stop',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-quota-depleted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Prepaid Quota Depleted Requests Sent
                ''',
                'prepaid_quota_depleted',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-reauthorization', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Prepaid Authorization Requests Sent
                ''',
                'prepaid_reauthorization',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Prepaid Start Requests Sent
                ''',
                'prepaid_start',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-stop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Prepaid Stop Requests Sent
                ''',
                'prepaid_stop',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-time-threshold-reached', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Prepaid Time Threshold Reached
                Requests Sent
                ''',
                'prepaid_time_threshold_reached',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-volume-threshold-reached', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Prepaid Volume Threshold Reached
                Requests Sent
                ''',
                'prepaid_volume_threshold_reached',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('service-accounting-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Service Accounting Start Requests Sent
                ''',
                'service_accounting_start',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('service-accounting-stop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Service Accounting Stop Requests Sent
                ''',
                'service_accounting_stop',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('service-accounting-update', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Service Accounting Update Requests
                Sent
                ''',
                'service_accounting_update',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('service-acct-out-of-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Service Accounting services out of
                sync
                ''',
                'service_acct_out_of_sync',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('service-acct-reqs-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Service Accounting requests that
                failed
                ''',
                'service_acct_reqs_failed',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('service-acct-trans-pending', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Service Accounting transactions
                pending
                ''',
                'service_acct_trans_pending',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('service-idle-to-out-of-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Service Idle Timeout services out of
                sync
                ''',
                'service_idle_to_out_of_sync',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('service-idle-to-reqs-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Service Idle Timeout requests that
                failed
                ''',
                'service_idle_to_reqs_failed',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('service-idle-to-trans-pending', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Service Idle Timeout transactions
                pending
                ''',
                'service_idle_to_trans_pending',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-accounting-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Accounting Start Requests Sent
                ''',
                'session_accounting_start',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-accounting-stop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Accounting Stop Requests Sent
                ''',
                'session_accounting_stop',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-accounting-update', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Accounting Update Requests
                Sent
                ''',
                'session_accounting_update',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-acct-out-of-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Accounting sessions out of
                sync
                ''',
                'session_acct_out_of_sync',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-acct-reqs-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Accounting requests that
                failed
                ''',
                'session_acct_reqs_failed',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-acct-trans-pending', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Accounting transactions
                pending
                ''',
                'session_acct_trans_pending',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-idle-to-out-of-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Idle Timeout sessions out of
                sync
                ''',
                'session_idle_to_out_of_sync',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-idle-to-reqs-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Idle Timeout requests that
                failed
                ''',
                'session_idle_to_reqs_failed',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-idle-to-trans-pending', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Session Idle Timeout transactions
                pending
                ''',
                'session_idle_to_trans_pending',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'aaa-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
    'SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters',
            False, 
            [
            _MetaInfoClassMember('active-flow-idle-timers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Active Flow Idle Timers
                ''',
                'active_flow_idle_timers',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('active-prepaid-idle-timers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Active Prepaid Idle Timers
                ''',
                'active_prepaid_idle_timers',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('active-session-idle-timers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Sessions with Idle Timeout Feature
                ''',
                'active_session_idle_timers',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('expired-flow-idle-timers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Flow Expired Idle Timers
                ''',
                'expired_flow_idle_timers',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('expired-prepaid-idle-timers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Expired Prepaid Idle Timers
                ''',
                'expired_prepaid_idle_timers',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Idle Sessions
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('transitions-to-awake', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Sessions Transitions to Awake State
                ''',
                'transitions_to_awake',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('transitions-to-idle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Sessions Transitions to Idle State
                ''',
                'transitions_to_idle',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'idle-timeout-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
    'SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters',
            False, 
            [
            _MetaInfoClassMember('active-session-timers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Active Session Timers
                ''',
                'active_session_timers',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('expired-session-timers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Expired Session Timers
                ''',
                'expired_session_timers',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'session-timeout-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
    'SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters',
            False, 
            [
            _MetaInfoClassMember('active-flows', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Active Flows
                ''',
                'active_flows',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('active-session-accounting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Active Sessions with Accounting
                ''',
                'active_session_accounting_sessions',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('active-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Active Sessions
                ''',
                'active_sessions',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('disconnected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Disconnected Sessions
                ''',
                'disconnected_sessions',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('quota-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of flows for which Quota is received
                ''',
                'quota_received',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'session-flow-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
    'SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary',
            False, 
            [
            _MetaInfoClassMember('aaa-counters', REFERENCE_CLASS, 'AaaCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper', 'SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters', 
                [], [], 
                '''                Accounting feature AAA summary counters
                ''',
                'aaa_counters',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('idle-timeout-counters', REFERENCE_CLASS, 'IdleTimeoutCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper', 'SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters', 
                [], [], 
                '''                Accounting feature idle timeout summary counters
                ''',
                'idle_timeout_counters',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-flow-counters', REFERENCE_CLASS, 'SessionFlowCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper', 'SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters', 
                [], [], 
                '''                Accounting feature session context summary
                counters
                ''',
                'session_flow_counters',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('session-timeout-counters', REFERENCE_CLASS, 'SessionTimeoutCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper', 'SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters', 
                [], [], 
                '''                Accounting feature session timeout summary
                counters
                ''',
                'session_timeout_counters',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'subscriber-accounting-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
    'SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData',
            False, 
            [
            _MetaInfoClassMember('flow-accounting-enabled-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if flow accounting is enabled
                ''',
                'flow_accounting_enabled_flag',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('flow-accounting-method-list-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Flow accounting method list name
                ''',
                'flow_accounting_method_list_name',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('flow-accounting-periodic-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flow accounting periodic interval
                ''',
                'flow_accounting_periodic_interval',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('flow-direction', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Direction of the flow. 0 = Ingress, 1 = Egress
                ''',
                'flow_direction',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('flow-idle-timeout-enabled-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if flow idle timeout is enabled
                ''',
                'flow_idle_timeout_enabled_flag',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('flow-idle-timeout-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flow idle timeout value in seconds
                ''',
                'flow_idle_timeout_value',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-ccfh', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prepaid CCFH flag
                ''',
                'prepaid_ccfh',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-cfg', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Prepaid Config
                ''',
                'prepaid_cfg',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-charging-rule', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Prepaid charging rule name string
                ''',
                'prepaid_charging_rule',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-enabled-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if prepaid is enabled
                ''',
                'prepaid_enabled_flag',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-final-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prepaid final unit indication flag
                ''',
                'prepaid_final_unit',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-idle-timeout-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to specify if idle timeout for service is
                enabled
                ''',
                'prepaid_idle_timeout_enabled',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-idle-timeout-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prepaid idle timeout value in seconds
                ''',
                'prepaid_idle_timeout_value',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-reauth-timeout-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time at which the re-authorization will
                occur
                ''',
                'prepaid_reauth_timeout_value',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-reauth-timer-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to specify if absolute timeout for ervice
                is enabled.
                ''',
                'prepaid_reauth_timer_enabled',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-remaining-qat', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time remaing for quota absolute timer to
                fire.
                ''',
                'prepaid_remaining_qat',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-remaining-qit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time remaing for quota holding timer to fire
                .
                ''',
                'prepaid_remaining_qit',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-remaining-qt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time remaing for QT timer to fire.
                ''',
                'prepaid_remaining_qt',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-remaining-qtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time remaining for tariff timer to fire.
                ''',
                'prepaid_remaining_qtt',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-remaining-wheel', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time remaining for idle timer wheel to fire.
                ''',
                'prepaid_remaining_wheel',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-result-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prepaid authorization operation result code
                ''',
                'prepaid_result_code',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-tariff-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The absolute time at which the traffic switch
                will occur expressed in UNIX time
                ''',
                'prepaid_tariff_time',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-tariff-volumeb-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total accumulated prepaid pre-tarrif total
                volume quota in bytes
                ''',
                'prepaid_tariff_volumeb_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-tariff-volumei-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total accumulated prepaid pre-tarrif input
                volume quota in bytes
                ''',
                'prepaid_tariff_volumei_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-tariff-volumeo-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total accumulated prepaid pre-tarrif output
                volume quota in bytes
                ''',
                'prepaid_tariff_volumeo_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-time-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current prepaid time quota in seconds
                ''',
                'prepaid_time_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-time-state', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Prepaid time state machine state
                ''',
                'prepaid_time_state',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-time-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current prepaid time threshold in seconds
                ''',
                'prepaid_time_threshold',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-total-time-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total accumulated prepaid time quota
                ''',
                'prepaid_total_time_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-total-volumeb-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total accumulated total volume quota in bytes
                ''',
                'prepaid_total_volumeb_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-total-volumei-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total accumulated input volume quota in bytes
                ''',
                'prepaid_total_volumei_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-total-volumeo-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total accumulated output volume quota in bytes
                ''',
                'prepaid_total_volumeo_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-volume-newb-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Newly arrvied bi-directional volume quota in
                bytes
                ''',
                'prepaid_volume_newb_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-volume-newi-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Newly arrvied input volume quota in bytes
                ''',
                'prepaid_volume_newi_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-volume-newo-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Newly arrvied output volume quota in bytes
                ''',
                'prepaid_volume_newo_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-volume-refb-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Accumulated bi-directional volume reference
                quota in bytes
                ''',
                'prepaid_volume_refb_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-volume-refi-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Accumulated input volume reference quota in
                bytes
                ''',
                'prepaid_volume_refi_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-volume-refo-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Accumulated output volume reference quota in
                bytes
                ''',
                'prepaid_volume_refo_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-volume-state', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Prepaid volume state machine state
                ''',
                'prepaid_volume_state',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-volume-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current prepaid volume threshold in bytes
                ''',
                'prepaid_volume_threshold',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-volume-usedi-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Accumulated input volume used quota in bytes
                ''',
                'prepaid_volume_usedi_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-volume-usedo-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Accumulated output volume used quota in bytes
                ''',
                'prepaid_volume_usedo_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-volumeb-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current prepaid total volume quota in bytes
                ''',
                'prepaid_volumeb_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-volumei-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current prepaid input volume quota in bytes
                ''',
                'prepaid_volumei_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('prepaid-volumeo-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current prepaid output volume quota in bytes
                ''',
                'prepaid_volumeo_quota',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('unique-class-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unique class label used to identify the flow
                ''',
                'unique_class_label',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'flow-feature-data',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
    'SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature',
            False, 
            [
            _MetaInfoClassMember('class-label', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Unique subscriber class label
                ''',
                'class_label',
                'Cisco-IOS-XR-subscriber-accounting-oper', True),
            _MetaInfoClassMember('flow-feature-data', REFERENCE_CLASS, 'FlowFeatureData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper', 'SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData', 
                [], [], 
                '''                Accouting flow feature display data
                ''',
                'flow_feature_data',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'subscriber-accounting-flow-feature',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
    'SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures',
            False, 
            [
            _MetaInfoClassMember('subscriber-accounting-flow-feature', REFERENCE_LIST, 'SubscriberAccountingFlowFeature' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper', 'SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature', 
                [], [], 
                '''                Display accounting flow features by unique
                subscriber label
                ''',
                'subscriber_accounting_flow_feature',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'subscriber-accounting-flow-features',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
    'SubscriberAccounting.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node id to filter on. For example,
                0/1/CPU0
                ''',
                'node_id',
                'Cisco-IOS-XR-subscriber-accounting-oper', True),
            _MetaInfoClassMember('subscriber-accounting-flow-features', REFERENCE_CLASS, 'SubscriberAccountingFlowFeatures' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper', 'SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures', 
                [], [], 
                '''                Subscriber accounting flow feature data
                ''',
                'subscriber_accounting_flow_features',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('subscriber-accounting-session-features', REFERENCE_CLASS, 'SubscriberAccountingSessionFeatures' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper', 'SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures', 
                [], [], 
                '''                Subscriber accounting session feature data
                ''',
                'subscriber_accounting_session_features',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            _MetaInfoClassMember('subscriber-accounting-summary', REFERENCE_CLASS, 'SubscriberAccountingSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper', 'SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary', 
                [], [], 
                '''                Display subscriber accounting summary data
                ''',
                'subscriber_accounting_summary',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
    'SubscriberAccounting.Nodes' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper', 'SubscriberAccounting.Nodes.Node', 
                [], [], 
                '''                Location. For example, 0/1/CPU0
                ''',
                'node',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
    'SubscriberAccounting' : {
        'meta_info' : _MetaInfoClass('SubscriberAccounting',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper', 'SubscriberAccounting.Nodes', 
                [], [], 
                '''                Subscriber accounting operational data for a
                particular location
                ''',
                'nodes',
                'Cisco-IOS-XR-subscriber-accounting-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-accounting-oper',
            'subscriber-accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-accounting-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_accounting_oper'
        ),
    },
}
_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData.ServiceAccountingFeature']['meta_info'].parent =_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData']['meta_info']
_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature.SessionFeatureData']['meta_info'].parent =_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature']['meta_info']
_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures.SubscriberAccountingSessionFeature']['meta_info'].parent =_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures']['meta_info']
_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.AaaCounters']['meta_info'].parent =_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary']['meta_info']
_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.IdleTimeoutCounters']['meta_info'].parent =_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary']['meta_info']
_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionTimeoutCounters']['meta_info'].parent =_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary']['meta_info']
_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary.SessionFlowCounters']['meta_info'].parent =_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary']['meta_info']
_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature.FlowFeatureData']['meta_info'].parent =_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature']['meta_info']
_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures.SubscriberAccountingFlowFeature']['meta_info'].parent =_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures']['meta_info']
_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSessionFeatures']['meta_info'].parent =_meta_table['SubscriberAccounting.Nodes.Node']['meta_info']
_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingSummary']['meta_info'].parent =_meta_table['SubscriberAccounting.Nodes.Node']['meta_info']
_meta_table['SubscriberAccounting.Nodes.Node.SubscriberAccountingFlowFeatures']['meta_info'].parent =_meta_table['SubscriberAccounting.Nodes.Node']['meta_info']
_meta_table['SubscriberAccounting.Nodes.Node']['meta_info'].parent =_meta_table['SubscriberAccounting.Nodes']['meta_info']
_meta_table['SubscriberAccounting.Nodes']['meta_info'].parent =_meta_table['SubscriberAccounting']['meta_info']
