


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AaaTunnelProtoEnum' : _MetaInfoEnum('AaaTunnelProtoEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper',
        {
            'none':'none',
            'pptp':'pptp',
            'l2f':'l2f',
            'l2tp':'l2tp',
            'atmp':'atmp',
            'vtp':'vtp',
            'ah':'ah',
            'ip-over-ip':'ip_over_ip',
            'minimum-ip-over-ip':'minimum_ip_over_ip',
            'esp':'esp',
            'gre':'gre',
            'bay-dvs':'bay_dvs',
            'ip-in-ip':'ip_in_ip',
            'vlan':'vlan',
        }, 'Cisco-IOS-XR-iedge4710-oper', _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper']),
    'IedgeOperSessionAfStateEnum' : _MetaInfoEnum('IedgeOperSessionAfStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper',
        {
            'not-started':'not_started',
            'down':'down',
            'up-pending':'up_pending',
            'up':'up',
        }, 'Cisco-IOS-XR-iedge4710-oper', _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper']),
    'IedgeOperSessionStateEnum' : _MetaInfoEnum('IedgeOperSessionStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper',
        {
            'initialize':'initialize',
            'connecting':'connecting',
            'connected':'connected',
            'activated':'activated',
            'idle':'idle',
            'disconnecting':'disconnecting',
            'end':'end',
        }, 'Cisco-IOS-XR-iedge4710-oper', _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper']),
    'IedgePppSubEnum' : _MetaInfoEnum('IedgePppSubEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper',
        {
            'pta':'pta',
            'lac':'lac',
        }, 'Cisco-IOS-XR-iedge4710-oper', _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper']),
    'IedgeOperSessionEnum' : _MetaInfoEnum('IedgeOperSessionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper',
        {
            'unknown':'unknown',
            'pppoe':'pppoe',
            'ppp':'ppp',
            'ip-packet-trigger':'ip_packet_trigger',
            'ip-packet-dhcp-trigger':'ip_packet_dhcp_trigger',
        }, 'Cisco-IOS-XR-iedge4710-oper', _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper']),
    'AaaTerminateCauseEnum' : _MetaInfoEnum('AaaTerminateCauseEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper',
        {
            'none':'none',
            'user-request':'user_request',
            'lost-carrier':'lost_carrier',
            'lost-service':'lost_service',
            'idle-timeout':'idle_timeout',
            'session-timeout':'session_timeout',
            'admin-reset':'admin_reset',
            'admin-reboot':'admin_reboot',
            'port-error':'port_error',
            'nas-error':'nas_error',
            'nas-request':'nas_request',
            'nas-reboot':'nas_reboot',
            'port-unneeded':'port_unneeded',
            'port-preempted':'port_preempted',
            'port-suspended':'port_suspended',
            'service-unavailable':'service_unavailable',
            'callback':'callback',
            'user-error':'user_error',
            'host-request':'host_request',
            'supplicant-restart':'supplicant_restart',
            'reauthorization-failure':'reauthorization_failure',
            'port-reinitialized':'port_reinitialized',
            'admin-disabled':'admin_disabled',
        }, 'Cisco-IOS-XR-iedge4710-oper', _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper']),
    'AaaTunnelMediumEnum' : _MetaInfoEnum('AaaTunnelMediumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper',
        {
            'none':'none',
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'nsap':'nsap',
            'hdlc':'hdlc',
            'bbn':'bbn',
            'all802':'all802',
        }, 'Cisco-IOS-XR-iedge4710-oper', _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper']),
    'AaaInterfaceEnum' : _MetaInfoEnum('AaaInterfaceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper',
        {
            'none':'none',
            'primary-rate':'primary_rate',
            'basic-rate':'basic_rate',
            'serial':'serial',
            'asynchronous':'asynchronous',
            'vty':'vty',
            'atm':'atm',
            'ethernet':'ethernet',
            'ppp-over-atm':'ppp_over_atm',
            'pppoe-over-atm':'pppoe_over_atm',
            'pppoe-over-ethernet':'pppoe_over_ethernet',
            'ppp-over-vlan':'ppp_over_vlan',
            'ppp-over-qinq':'ppp_over_qinq',
            'v120':'v120',
            'v110':'v110',
            'piafs':'piafs',
            'x75':'x75',
            'ip-sec':'ip_sec',
            'other':'other',
            'virtual-pppoe-over-ethernet':'virtual_pppoe_over_ethernet',
            'virtual-pppoe-over-vlan':'virtual_pppoe_over_vlan',
            'virtual-pppoe-over-qinq':'virtual_pppoe_over_qinq',
            'ipo-e-over-ethernet':'ipo_e_over_ethernet',
            'ipo-e-over-vlan':'ipo_e_over_vlan',
            'ipo-e-over-qinq':'ipo_e_over_qinq',
            'virtual-i-po-e-over-ethernet':'virtual_i_po_e_over_ethernet',
            'virtual-i-po-e-over-vlan':'virtual_i_po_e_over_vlan',
            'virtual-i-po-e-over-qinq':'virtual_i_po_e_over_qinq',
        }, 'Cisco-IOS-XR-iedge4710-oper', _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper']),
    'SubscriberAddressFamilyFilterFlagEnum' : _MetaInfoEnum('SubscriberAddressFamilyFilterFlagEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper',
        {
            'ipv4-only':'ipv4_only',
            'ipv6-only':'ipv6_only',
            'ipv4-all':'ipv4_all',
            'ipv6-all':'ipv6_all',
            'dual-all':'dual_all',
            'dual-part-up':'dual_part_up',
            'dual-up':'dual_up',
            'lac':'lac',
        }, 'Cisco-IOS-XR-iedge4710-oper', _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper']),
    'AaaAuthServiceEnum' : _MetaInfoEnum('AaaAuthServiceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper',
        {
            'none':'none',
            'login':'login',
            'framed':'framed',
            'callback-login':'callback_login',
            'callback-framed':'callback_framed',
            'outbound':'outbound',
            'administrator':'administrator',
            'prompt':'prompt',
            'authentication-only':'authentication_only',
            'callback-nas-prompt':'callback_nas_prompt',
            'call-check':'call_check',
            'callback-administrator':'callback_administrator',
            'voice':'voice',
            'fax':'fax',
            'modem-relay':'modem_relay',
            'eap-over-udp':'eap_over_udp',
        }, 'Cisco-IOS-XR-iedge4710-oper', _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper']),
    'SubscriberAuthenStateFilterFlagEnum' : _MetaInfoEnum('SubscriberAuthenStateFilterFlagEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper',
        {
            'un-authenticated':'un_authenticated',
            'authenticated':'authenticated',
        }, 'Cisco-IOS-XR-iedge4710-oper', _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper']),
    'SubscriberAuthorStateFilterFlagEnum' : _MetaInfoEnum('SubscriberAuthorStateFilterFlagEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper',
        {
            'un-authorized':'un_authorized',
            'authorized':'authorized',
        }, 'Cisco-IOS-XR-iedge4710-oper', _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper']),
    'SubscriberStateFilterFlagEnum' : _MetaInfoEnum('SubscriberStateFilterFlagEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper',
        {
            'initializing':'initializing',
            'connecting':'connecting',
            'connected':'connected',
            'activated':'activated',
            'idle':'idle',
            'disconnecting':'disconnecting',
            'end':'end',
        }, 'Cisco-IOS-XR-iedge4710-oper', _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper']),
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'start',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'stop',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'interim',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pass-through',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'update',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight',
            False, 
            [
            _MetaInfoClassMember('accepted-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accepted requests
                ''',
                'accepted_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('denied-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Denied requests
                ''',
                'denied_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('low-water-mark-quota-of-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Low water mark quota of requests
                ''',
                'low_water_mark_quota_of_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('quota-exhausts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Quota exhausts
                ''',
                'quota_exhausts',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('remaining-quota-of-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining quota of requests
                ''',
                'remaining_quota_of_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('total-quota-of-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total quota of requests
                ''',
                'total_quota_of_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'interim-inflight',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting',
            False, 
            [
            _MetaInfoClassMember('active-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Active sessions
                ''',
                'active_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('interim', REFERENCE_CLASS, 'Interim' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim', 
                [], [], 
                '''                Interim statistics
                ''',
                'interim',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('interim-inflight', REFERENCE_CLASS, 'InterimInflight' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight', 
                [], [], 
                '''                Interim inflight details
                ''',
                'interim_inflight',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pass-through', REFERENCE_CLASS, 'PassThrough' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough', 
                [], [], 
                '''                Pass-through statistics
                ''',
                'pass_through',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('policy-plane-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Policy plane errored requests
                ''',
                'policy_plane_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('policy-plane-unknown-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Policy plane unknown requests
                ''',
                'policy_plane_unknown_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('start', REFERENCE_CLASS, 'Start' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start', 
                [], [], 
                '''                Start statistics
                ''',
                'start',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('started-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Started sessions
                ''',
                'started_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('stop', REFERENCE_CLASS, 'Stop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop', 
                [], [], 
                '''                Stop statistics
                ''',
                'stop',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('stopped-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Stopped sessions
                ''',
                'stopped_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('update', REFERENCE_CLASS, 'Update' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update', 
                [], [], 
                '''                Update statistics
                ''',
                'update',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'aggregate-accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication',
            False, 
            [
            _MetaInfoClassMember('accepted-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request accepted by Radius server
                ''',
                'accepted_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unexpected errors
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('incomplete-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Incomplete requests - missing attributes
                ''',
                'incomplete_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('rejected-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests rejected by radius server
                ''',
                'rejected_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests sent to radius server
                ''',
                'sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('successful-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests which are successful
                ''',
                'successful_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('terminated-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests terminated by disconnect
                ''',
                'terminated_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unreachable-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Radius server not available
                ''',
                'unreachable_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility',
            False, 
            [
            _MetaInfoClassMember('receive-response-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Response receive failures
                ''',
                'receive_response_failures',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('receive-response-successes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Response receive success
                ''',
                'receive_response_successes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('send-request-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request send failures
                ''',
                'send_request_failures',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('send-request-successes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request send success
                ''',
                'send_request_successes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'aggregate-mobility',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication',
            False, 
            [
            _MetaInfoClassMember('accepted-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request accepted by Radius server
                ''',
                'accepted_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unexpected errors
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('incomplete-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Incomplete requests - missing attributes
                ''',
                'incomplete_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('rejected-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests rejected by radius server
                ''',
                'rejected_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests sent to radius server
                ''',
                'sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('successful-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests which are successful
                ''',
                'successful_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('terminated-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests terminated by disconnect
                ''',
                'terminated_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unreachable-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Radius server not available
                ''',
                'unreachable_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'aggregate-authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Start' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Start',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'start',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Stop' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Stop',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'stop',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Interim' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Interim',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'interim',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.PassThrough' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.PassThrough',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pass-through',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Update' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Update',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'update',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.InterimInflight' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.InterimInflight',
            False, 
            [
            _MetaInfoClassMember('accepted-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accepted requests
                ''',
                'accepted_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('denied-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Denied requests
                ''',
                'denied_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('low-water-mark-quota-of-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Low water mark quota of requests
                ''',
                'low_water_mark_quota_of_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('quota-exhausts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Quota exhausts
                ''',
                'quota_exhausts',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('remaining-quota-of-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining quota of requests
                ''',
                'remaining_quota_of_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('total-quota-of-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total quota of requests
                ''',
                'total_quota_of_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'interim-inflight',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics',
            False, 
            [
            _MetaInfoClassMember('active-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Active sessions
                ''',
                'active_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('interim', REFERENCE_CLASS, 'Interim' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Interim', 
                [], [], 
                '''                Interim statistics
                ''',
                'interim',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('interim-inflight', REFERENCE_CLASS, 'InterimInflight' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.InterimInflight', 
                [], [], 
                '''                Interim inflight details
                ''',
                'interim_inflight',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pass-through', REFERENCE_CLASS, 'PassThrough' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.PassThrough', 
                [], [], 
                '''                Pass-through statistics
                ''',
                'pass_through',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('policy-plane-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Policy plane errored requests
                ''',
                'policy_plane_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('policy-plane-unknown-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Policy plane unknown requests
                ''',
                'policy_plane_unknown_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('start', REFERENCE_CLASS, 'Start' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Start', 
                [], [], 
                '''                Start statistics
                ''',
                'start',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('started-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Started sessions
                ''',
                'started_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('stop', REFERENCE_CLASS, 'Stop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Stop', 
                [], [], 
                '''                Stop statistics
                ''',
                'stop',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('stopped-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Stopped sessions
                ''',
                'stopped_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('update', REFERENCE_CLASS, 'Update' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Update', 
                [], [], 
                '''                Update statistics
                ''',
                'update',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'accounting-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthenticationStatistics' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthenticationStatistics',
            False, 
            [
            _MetaInfoClassMember('accepted-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request accepted by Radius server
                ''',
                'accepted_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unexpected errors
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('incomplete-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Incomplete requests - missing attributes
                ''',
                'incomplete_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('rejected-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests rejected by radius server
                ''',
                'rejected_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests sent to radius server
                ''',
                'sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('successful-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests which are successful
                ''',
                'successful_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('terminated-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests terminated by disconnect
                ''',
                'terminated_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unreachable-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Radius server not available
                ''',
                'unreachable_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'authentication-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthorizationStatistics' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthorizationStatistics',
            False, 
            [
            _MetaInfoClassMember('accepted-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request accepted by Radius server
                ''',
                'accepted_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unexpected errors
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('incomplete-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Incomplete requests - missing attributes
                ''',
                'incomplete_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('rejected-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests rejected by radius server
                ''',
                'rejected_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests sent to radius server
                ''',
                'sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('successful-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests which are successful
                ''',
                'successful_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('terminated-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests terminated by disconnect
                ''',
                'terminated_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unreachable-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Radius server not available
                ''',
                'unreachable_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'authorization-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'account-logon',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'account-logoff',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'account-update',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'session-disconnect',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'single-service-logon',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'single-service-logoff',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'single-service-modify',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'service-multi',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics',
            False, 
            [
            _MetaInfoClassMember('account-logoff', REFERENCE_CLASS, 'AccountLogoff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff', 
                [], [], 
                '''                Account logoff request statistics
                ''',
                'account_logoff',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('account-logon', REFERENCE_CLASS, 'AccountLogon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon', 
                [], [], 
                '''                Account logon request statistics
                ''',
                'account_logon',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('account-update', REFERENCE_CLASS, 'AccountUpdate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate', 
                [], [], 
                '''                Account update request statistics
                ''',
                'account_update',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('attr-list-retrieve-failure-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to attribute list failure errors
                ''',
                'attr_list_retrieve_failure_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('internal-err-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to internal error
                ''',
                'internal_err_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('no-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses empty (no command) COA request
                ''',
                'no_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('no-session-found-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to COA with unknown session identifier
                ''',
                'no_session_found_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('no-session-peer-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to session peer not found error
                ''',
                'no_session_peer_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('resp-send-failure', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Response send failures
                ''',
                'resp_send_failure',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('service-multi', REFERENCE_CLASS, 'ServiceMulti' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti', 
                [], [], 
                '''                MA-CoA Service request statistics
                ''',
                'service_multi',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('service-profile-push-failure-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to service profile push failures
                ''',
                'service_profile_push_failure_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-disconnect', REFERENCE_CLASS, 'SessionDisconnect' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect', 
                [], [], 
                '''                Session disconnect request statistics
                ''',
                'session_disconnect',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('single-service-logoff', REFERENCE_CLASS, 'SingleServiceLogoff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff', 
                [], [], 
                '''                Single Service logoff request statistics
                ''',
                'single_service_logoff',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('single-service-logon', REFERENCE_CLASS, 'SingleServiceLogon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon', 
                [], [], 
                '''                Service logon request statistics
                ''',
                'single_service_logon',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('single-service-modify', REFERENCE_CLASS, 'SingleServiceModify' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify', 
                [], [], 
                '''                Single Service Modify request statistics
                ''',
                'single_service_modify',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unknown-account-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to unknown account command
                ''',
                'unknown_account_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unknown-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to unknown command
                ''',
                'unknown_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unknown-service-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to unknown service command
                ''',
                'unknown_service_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'change-of-authorization-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.MobilityStatistics' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.MobilityStatistics',
            False, 
            [
            _MetaInfoClassMember('receive-response-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Response receive failures
                ''',
                'receive_response_failures',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('receive-response-successes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Response receive success
                ''',
                'receive_response_successes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('send-request-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request send failures
                ''',
                'send_request_failures',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('send-request-successes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request send success
                ''',
                'send_request_successes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'mobility-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll',
            False, 
            [
            _MetaInfoClassMember('accounting-statistics', REFERENCE_CLASS, 'AccountingStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics', 
                [], [], 
                '''                List of stats for accounting
                ''',
                'accounting_statistics',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('authentication-statistics', REFERENCE_CLASS, 'AuthenticationStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthenticationStatistics', 
                [], [], 
                '''                List of stats for authentication
                ''',
                'authentication_statistics',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('authorization-statistics', REFERENCE_CLASS, 'AuthorizationStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthorizationStatistics', 
                [], [], 
                '''                List of stats for authorization
                ''',
                'authorization_statistics',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('change-of-authorization-statistics', REFERENCE_CLASS, 'ChangeOfAuthorizationStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics', 
                [], [], 
                '''                List of stats for COA
                ''',
                'change_of_authorization_statistics',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('mobility-statistics', REFERENCE_CLASS, 'MobilityStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.MobilityStatistics', 
                [], [], 
                '''                List of stats for Mobility
                ''',
                'mobility_statistics',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'accounting-stats-all',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'account-logon',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'account-logoff',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'account-update',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'session-disconnect',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'single-service-logon',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'single-service-logoff',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'single-service-modify',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'service-multi',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization',
            False, 
            [
            _MetaInfoClassMember('account-logoff', REFERENCE_CLASS, 'AccountLogoff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff', 
                [], [], 
                '''                Account logoff request statistics
                ''',
                'account_logoff',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('account-logon', REFERENCE_CLASS, 'AccountLogon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon', 
                [], [], 
                '''                Account logon request statistics
                ''',
                'account_logon',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('account-update', REFERENCE_CLASS, 'AccountUpdate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate', 
                [], [], 
                '''                Account update request statistics
                ''',
                'account_update',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('attr-list-retrieve-failure-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to attribute list failure errors
                ''',
                'attr_list_retrieve_failure_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('internal-err-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to internal error
                ''',
                'internal_err_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('no-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses empty (no command) COA request
                ''',
                'no_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('no-session-found-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to COA with unknown session identifier
                ''',
                'no_session_found_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('no-session-peer-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to session peer not found error
                ''',
                'no_session_peer_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('resp-send-failure', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Response send failures
                ''',
                'resp_send_failure',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('service-multi', REFERENCE_CLASS, 'ServiceMulti' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti', 
                [], [], 
                '''                MA-CoA Service request statistics
                ''',
                'service_multi',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('service-profile-push-failure-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to service profile push failures
                ''',
                'service_profile_push_failure_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-disconnect', REFERENCE_CLASS, 'SessionDisconnect' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect', 
                [], [], 
                '''                Session disconnect request statistics
                ''',
                'session_disconnect',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('single-service-logoff', REFERENCE_CLASS, 'SingleServiceLogoff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff', 
                [], [], 
                '''                Single Service logoff request statistics
                ''',
                'single_service_logoff',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('single-service-logon', REFERENCE_CLASS, 'SingleServiceLogon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon', 
                [], [], 
                '''                Service logon request statistics
                ''',
                'single_service_logon',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('single-service-modify', REFERENCE_CLASS, 'SingleServiceModify' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify', 
                [], [], 
                '''                Single Service Modify request statistics
                ''',
                'single_service_modify',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unknown-account-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to unknown account command
                ''',
                'unknown_account_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unknown-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to unknown command
                ''',
                'unknown_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unknown-service-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to unknown service command
                ''',
                'unknown_service_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'change-of-authorization',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization',
            False, 
            [
            _MetaInfoClassMember('accepted-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request accepted by Radius server
                ''',
                'accepted_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unexpected errors
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('incomplete-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Incomplete requests - missing attributes
                ''',
                'incomplete_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('rejected-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests rejected by radius server
                ''',
                'rejected_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests sent to radius server
                ''',
                'sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('successful-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests which are successful
                ''',
                'successful_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('terminated-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests terminated by disconnect
                ''',
                'terminated_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unreachable-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Radius server not available
                ''',
                'unreachable_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'authorization',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization',
            False, 
            [
            _MetaInfoClassMember('accepted-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request accepted by Radius server
                ''',
                'accepted_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unexpected errors
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('incomplete-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Incomplete requests - missing attributes
                ''',
                'incomplete_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('rejected-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests rejected by radius server
                ''',
                'rejected_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests sent to radius server
                ''',
                'sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('successful-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests which are successful
                ''',
                'successful_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('terminated-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests terminated by disconnect
                ''',
                'terminated_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unreachable-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Radius server not available
                ''',
                'unreachable_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'aggregate-authorization',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Start' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Start',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'start',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Stop' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Stop',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'stop',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Interim' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Interim',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'interim',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.PassThrough' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.PassThrough',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pass-through',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Update' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Update',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'update',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.InterimInflight' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.InterimInflight',
            False, 
            [
            _MetaInfoClassMember('accepted-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accepted requests
                ''',
                'accepted_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('denied-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Denied requests
                ''',
                'denied_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('low-water-mark-quota-of-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Low water mark quota of requests
                ''',
                'low_water_mark_quota_of_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('quota-exhausts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Quota exhausts
                ''',
                'quota_exhausts',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('remaining-quota-of-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining quota of requests
                ''',
                'remaining_quota_of_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('total-quota-of-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total quota of requests
                ''',
                'total_quota_of_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'interim-inflight',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics',
            False, 
            [
            _MetaInfoClassMember('active-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Active sessions
                ''',
                'active_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('interim', REFERENCE_CLASS, 'Interim' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Interim', 
                [], [], 
                '''                Interim statistics
                ''',
                'interim',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('interim-inflight', REFERENCE_CLASS, 'InterimInflight' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.InterimInflight', 
                [], [], 
                '''                Interim inflight details
                ''',
                'interim_inflight',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pass-through', REFERENCE_CLASS, 'PassThrough' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.PassThrough', 
                [], [], 
                '''                Pass-through statistics
                ''',
                'pass_through',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('policy-plane-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Policy plane errored requests
                ''',
                'policy_plane_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('policy-plane-unknown-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Policy plane unknown requests
                ''',
                'policy_plane_unknown_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('start', REFERENCE_CLASS, 'Start' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Start', 
                [], [], 
                '''                Start statistics
                ''',
                'start',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('started-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Started sessions
                ''',
                'started_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('stop', REFERENCE_CLASS, 'Stop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Stop', 
                [], [], 
                '''                Stop statistics
                ''',
                'stop',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('stopped-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Stopped sessions
                ''',
                'stopped_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('update', REFERENCE_CLASS, 'Update' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Update', 
                [], [], 
                '''                Update statistics
                ''',
                'update',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'accounting-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthenticationStatistics' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthenticationStatistics',
            False, 
            [
            _MetaInfoClassMember('accepted-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request accepted by Radius server
                ''',
                'accepted_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unexpected errors
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('incomplete-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Incomplete requests - missing attributes
                ''',
                'incomplete_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('rejected-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests rejected by radius server
                ''',
                'rejected_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests sent to radius server
                ''',
                'sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('successful-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests which are successful
                ''',
                'successful_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('terminated-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests terminated by disconnect
                ''',
                'terminated_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unreachable-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Radius server not available
                ''',
                'unreachable_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'authentication-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthorizationStatistics' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthorizationStatistics',
            False, 
            [
            _MetaInfoClassMember('accepted-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request accepted by Radius server
                ''',
                'accepted_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unexpected errors
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('incomplete-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Incomplete requests - missing attributes
                ''',
                'incomplete_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('rejected-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests rejected by radius server
                ''',
                'rejected_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests sent to radius server
                ''',
                'sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('successful-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests which are successful
                ''',
                'successful_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('terminated-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Requests terminated by disconnect
                ''',
                'terminated_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unreachable-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Radius server not available
                ''',
                'unreachable_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'authorization-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'account-logon',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'account-logoff',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'account-update',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'session-disconnect',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'single-service-logon',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'single-service-logoff',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'single-service-modify',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'service-multi',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics',
            False, 
            [
            _MetaInfoClassMember('account-logoff', REFERENCE_CLASS, 'AccountLogoff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff', 
                [], [], 
                '''                Account logoff request statistics
                ''',
                'account_logoff',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('account-logon', REFERENCE_CLASS, 'AccountLogon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon', 
                [], [], 
                '''                Account logon request statistics
                ''',
                'account_logon',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('account-update', REFERENCE_CLASS, 'AccountUpdate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate', 
                [], [], 
                '''                Account update request statistics
                ''',
                'account_update',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('attr-list-retrieve-failure-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to attribute list failure errors
                ''',
                'attr_list_retrieve_failure_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('internal-err-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to internal error
                ''',
                'internal_err_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('no-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses empty (no command) COA request
                ''',
                'no_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('no-session-found-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to COA with unknown session identifier
                ''',
                'no_session_found_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('no-session-peer-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to session peer not found error
                ''',
                'no_session_peer_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('resp-send-failure', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Response send failures
                ''',
                'resp_send_failure',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('service-multi', REFERENCE_CLASS, 'ServiceMulti' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti', 
                [], [], 
                '''                MA-CoA Service request statistics
                ''',
                'service_multi',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('service-profile-push-failure-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to service profile push failures
                ''',
                'service_profile_push_failure_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-disconnect', REFERENCE_CLASS, 'SessionDisconnect' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect', 
                [], [], 
                '''                Session disconnect request statistics
                ''',
                'session_disconnect',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('single-service-logoff', REFERENCE_CLASS, 'SingleServiceLogoff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff', 
                [], [], 
                '''                Single Service logoff request statistics
                ''',
                'single_service_logoff',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('single-service-logon', REFERENCE_CLASS, 'SingleServiceLogon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon', 
                [], [], 
                '''                Service logon request statistics
                ''',
                'single_service_logon',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('single-service-modify', REFERENCE_CLASS, 'SingleServiceModify' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify', 
                [], [], 
                '''                Single Service Modify request statistics
                ''',
                'single_service_modify',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unknown-account-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to unknown account command
                ''',
                'unknown_account_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unknown-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to unknown command
                ''',
                'unknown_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unknown-service-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to unknown service command
                ''',
                'unknown_service_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'change-of-authorization-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.MobilityStatistics' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.MobilityStatistics',
            False, 
            [
            _MetaInfoClassMember('receive-response-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Response receive failures
                ''',
                'receive_response_failures',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('receive-response-successes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Response receive success
                ''',
                'receive_response_successes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('send-request-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request send failures
                ''',
                'send_request_failures',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('send-request-successes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request send success
                ''',
                'send_request_successes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'mobility-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll',
            False, 
            [
            _MetaInfoClassMember('accounting-statistics', REFERENCE_CLASS, 'AccountingStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics', 
                [], [], 
                '''                List of stats for accounting
                ''',
                'accounting_statistics',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('authentication-statistics', REFERENCE_CLASS, 'AuthenticationStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthenticationStatistics', 
                [], [], 
                '''                List of stats for authentication
                ''',
                'authentication_statistics',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('authorization-statistics', REFERENCE_CLASS, 'AuthorizationStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthorizationStatistics', 
                [], [], 
                '''                List of stats for authorization
                ''',
                'authorization_statistics',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('change-of-authorization-statistics', REFERENCE_CLASS, 'ChangeOfAuthorizationStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics', 
                [], [], 
                '''                List of stats for COA
                ''',
                'change_of_authorization_statistics',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('mobility-statistics', REFERENCE_CLASS, 'MobilityStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.MobilityStatistics', 
                [], [], 
                '''                List of stats for Mobility
                ''',
                'mobility_statistics',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'aggregate-accounting-stats-all',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'start',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'stop',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'interim',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pass-through',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update',
            False, 
            [
            _MetaInfoClassMember('aaa-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA errored requests
                ''',
                'aaa_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-failed-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA failed responses
                ''',
                'aaa_failed_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-sent-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA requests sent
                ''',
                'aaa_sent_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aaa-succeeded-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AAA succeeded responses
                ''',
                'aaa_succeeded_responses',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Errored requests
                ''',
                'errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'update',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight',
            False, 
            [
            _MetaInfoClassMember('accepted-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accepted requests
                ''',
                'accepted_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('denied-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Denied requests
                ''',
                'denied_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('low-water-mark-quota-of-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Low water mark quota of requests
                ''',
                'low_water_mark_quota_of_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('quota-exhausts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Quota exhausts
                ''',
                'quota_exhausts',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('remaining-quota-of-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining quota of requests
                ''',
                'remaining_quota_of_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('total-quota-of-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total quota of requests
                ''',
                'total_quota_of_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'interim-inflight',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting',
            False, 
            [
            _MetaInfoClassMember('active-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Active sessions
                ''',
                'active_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('interim', REFERENCE_CLASS, 'Interim' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim', 
                [], [], 
                '''                Interim statistics
                ''',
                'interim',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('interim-inflight', REFERENCE_CLASS, 'InterimInflight' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight', 
                [], [], 
                '''                Interim inflight details
                ''',
                'interim_inflight',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pass-through', REFERENCE_CLASS, 'PassThrough' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough', 
                [], [], 
                '''                Pass-through statistics
                ''',
                'pass_through',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('policy-plane-errored-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Policy plane errored requests
                ''',
                'policy_plane_errored_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('policy-plane-unknown-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Policy plane unknown requests
                ''',
                'policy_plane_unknown_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('start', REFERENCE_CLASS, 'Start' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start', 
                [], [], 
                '''                Start statistics
                ''',
                'start',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('started-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Started sessions
                ''',
                'started_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('stop', REFERENCE_CLASS, 'Stop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop', 
                [], [], 
                '''                Stop statistics
                ''',
                'stop',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('stopped-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Stopped sessions
                ''',
                'stopped_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('update', REFERENCE_CLASS, 'Update' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update', 
                [], [], 
                '''                Update statistics
                ''',
                'update',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility',
            False, 
            [
            _MetaInfoClassMember('receive-response-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Response receive failures
                ''',
                'receive_response_failures',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('receive-response-successes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Response receive success
                ''',
                'receive_response_successes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('send-request-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request send failures
                ''',
                'send_request_failures',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('send-request-successes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Request send success
                ''',
                'send_request_successes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'mobility',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'account-logon',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'account-logoff',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'account-update',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'session-disconnect',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'single-service-logon',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'single-service-logoff',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'single-service-modify',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti',
            False, 
            [
            _MetaInfoClassMember('acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Acknowledged requests
                ''',
                'acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('non-acknowledged-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Non acknowledged requests
                ''',
                'non_acknowledged_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('received-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received requests
                ''',
                'received_requests',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'service-multi',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization',
            False, 
            [
            _MetaInfoClassMember('account-logoff', REFERENCE_CLASS, 'AccountLogoff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff', 
                [], [], 
                '''                Account logoff request statistics
                ''',
                'account_logoff',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('account-logon', REFERENCE_CLASS, 'AccountLogon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon', 
                [], [], 
                '''                Account logon request statistics
                ''',
                'account_logon',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('account-update', REFERENCE_CLASS, 'AccountUpdate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate', 
                [], [], 
                '''                Account update request statistics
                ''',
                'account_update',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('attr-list-retrieve-failure-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to attribute list failure errors
                ''',
                'attr_list_retrieve_failure_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('internal-err-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to internal error
                ''',
                'internal_err_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('no-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses empty (no command) COA request
                ''',
                'no_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('no-session-found-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to COA with unknown session identifier
                ''',
                'no_session_found_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('no-session-peer-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to session peer not found error
                ''',
                'no_session_peer_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('resp-send-failure', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Response send failures
                ''',
                'resp_send_failure',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('service-multi', REFERENCE_CLASS, 'ServiceMulti' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti', 
                [], [], 
                '''                MA-CoA Service request statistics
                ''',
                'service_multi',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('service-profile-push-failure-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to service profile push failures
                ''',
                'service_profile_push_failure_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-disconnect', REFERENCE_CLASS, 'SessionDisconnect' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect', 
                [], [], 
                '''                Session disconnect request statistics
                ''',
                'session_disconnect',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('single-service-logoff', REFERENCE_CLASS, 'SingleServiceLogoff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff', 
                [], [], 
                '''                Single Service logoff request statistics
                ''',
                'single_service_logoff',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('single-service-logon', REFERENCE_CLASS, 'SingleServiceLogon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon', 
                [], [], 
                '''                Service logon request statistics
                ''',
                'single_service_logon',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('single-service-modify', REFERENCE_CLASS, 'SingleServiceModify' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify', 
                [], [], 
                '''                Single Service Modify request statistics
                ''',
                'single_service_modify',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unknown-account-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to unknown account command
                ''',
                'unknown_account_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unknown-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to unknown command
                ''',
                'unknown_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('unknown-service-cmd-resps', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Responses to unknown service command
                ''',
                'unknown_service_cmd_resps',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'aggregate-change-of-authorization',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Aaa' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Aaa',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting', 
                [], [], 
                '''                Accounting statistics
                ''',
                'accounting',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('accounting-stats-all', REFERENCE_CLASS, 'AccountingStatsAll' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll', 
                [], [], 
                '''                Display all subscriber management
                statistics
                ''',
                'accounting_stats_all',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aggregate-accounting', REFERENCE_CLASS, 'AggregateAccounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting', 
                [], [], 
                '''                Aggregate accounting statistics
                ''',
                'aggregate_accounting',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aggregate-accounting-stats-all', REFERENCE_CLASS, 'AggregateAccountingStatsAll' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll', 
                [], [], 
                '''                Display all subscriber management total
                statistics
                ''',
                'aggregate_accounting_stats_all',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aggregate-authentication', REFERENCE_CLASS, 'AggregateAuthentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication', 
                [], [], 
                '''                Aggregate authentication statistics
                ''',
                'aggregate_authentication',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aggregate-authorization', REFERENCE_CLASS, 'AggregateAuthorization' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization', 
                [], [], 
                '''                Aggregate authorization statistics
                ''',
                'aggregate_authorization',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aggregate-change-of-authorization', REFERENCE_CLASS, 'AggregateChangeOfAuthorization' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization', 
                [], [], 
                '''                Aggregate change of authorization (COA)
                statistics
                ''',
                'aggregate_change_of_authorization',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aggregate-mobility', REFERENCE_CLASS, 'AggregateMobility' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility', 
                [], [], 
                '''                Aggregate mobility statistics
                ''',
                'aggregate_mobility',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication', 
                [], [], 
                '''                Authentication statistics
                ''',
                'authentication',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('authorization', REFERENCE_CLASS, 'Authorization' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization', 
                [], [], 
                '''                Authorization statistics
                ''',
                'authorization',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('change-of-authorization', REFERENCE_CLASS, 'ChangeOfAuthorization' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization', 
                [], [], 
                '''                Change of authorization (COA) statistics
                ''',
                'change_of_authorization',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('mobility', REFERENCE_CLASS, 'Mobility' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility', 
                [], [], 
                '''                Mobility statistics
                ''',
                'mobility',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'aaa',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.AggregateSummary' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.AggregateSummary',
            False, 
            [
            _MetaInfoClassMember('calling-station-id-attribute-format-warnings', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Calling station ID attribute format warnings
                ''',
                'calling_station_id_attribute_format_warnings',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('destination-station-id-attribute-format-warnings', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Destination station ID attribute format warnings
                ''',
                'destination_station_id_attribute_format_warnings',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('install-user-profiles', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                User profiles installed
                ''',
                'install_user_profiles',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('nas-port-attribute-format-warnings', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                NAS port attribute format warnings
                ''',
                'nas_port_attribute_format_warnings',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('nas-port-id-attribute-format-warnings', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                NAS port ID attribute format warnings
                ''',
                'nas_port_id_attribute_format_warnings',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('no-class-match-in-start-request', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                No control policy class match during subscriber
                start
                ''',
                'no_class_match_in_start_request',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('no-subscriber-control-policy-on-interface', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Subscriber control policy not applied on
                interface
                ''',
                'no_subscriber_control_policy_on_interface',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sess-disc-no-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Session Disconnect Request Queued, no quota
                ''',
                'sess_disc_no_quota',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sess-disc-none-started', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Session Disconnect Requests not Dequeued, no
                quota
                ''',
                'sess_disc_none_started',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sess-disc-q-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Disconnect Requests Queued
                ''',
                'sess_disc_q_count',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sess-disc-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Disconnect Quota
                ''',
                'sess_disc_quota',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sess-disc-quota-avail', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Session Disconnect Request Accepted, quota
                available
                ''',
                'sess_disc_quota_avail',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sess-disc-quota-exhausts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Session Disconnect Quota Exhausts
                ''',
                'sess_disc_quota_exhausts',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sess-disc-quota-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Disconnect Quota Remaining
                ''',
                'sess_disc_quota_remaining',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sess-disc-recon-ip', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Session Disconnect Requests not Dequeued,
                reconciliation in progress
                ''',
                'sess_disc_recon_ip',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('user-profile-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                User profile errors
                ''',
                'user_profile_errors',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('user-profile-install-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                User profile install errors
                ''',
                'user_profile_install_errors',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('user-profile-removals', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                User profile removals
                ''',
                'user_profile_removals',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('username-attribute-format-warnings', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Username attribute format warnings
                ''',
                'username_attribute_format_warnings',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'aggregate-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics.Srg' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics.Srg',
            False, 
            [
            _MetaInfoClassMember('ack-to-srg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ACKs sent to Srg
                ''',
                'ack_to_srg',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('actual-txlist-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Txlist Send Success
                ''',
                'actual_txlist_sent',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('alreadyin-txlist', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Element already in Txlist
                ''',
                'alreadyin_txlist',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('create-upd-clean-callback', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Txlist Create/update clean callback
                ''',
                'create_upd_clean_callback',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('create-update-encode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Txlist Create Update Encode
                ''',
                'create_update_encode',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('delete-clean-callback', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Txlist Delete clean callback
                ''',
                'delete_clean_callback',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('delete-encode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Txlist Delete Encode
                ''',
                'delete_encode',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('eod-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of EODs Received
                ''',
                'eod_count',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('flow-control-resume-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold Limit to resume the flow control
                ''',
                'flow_control_resume_threshold',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('inflight-add-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No.of inflight sessions added
                ''',
                'inflight_add_count',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('inflight-alloc-fails', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Memory Alloc Failures for Inflight Entry
                ''',
                'inflight_alloc_fails',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('inflight-delete-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inflight Entry Delete Failures
                ''',
                'inflight_delete_failures',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('inflight-deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inflight Deletes Count
                ''',
                'inflight_deletes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('inflight-insert-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inflight Entry Insert Failures
                ''',
                'inflight_insert_failures',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('inflight-not-found', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inflight Entries not found during delete
                ''',
                'inflight_not_found',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('inflight-session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No.of Sessions inflight at given time
                ''',
                'inflight_session_count',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('inflight-under-run-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inflight Underrun Counter
                ''',
                'inflight_under_run_count',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('is-srg-flow-control-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag indicating SRG Flow control enabled or not
                ''',
                'is_srg_flow_control_enabled',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('last-pause-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Amount of time paused during last flow control
                window
                ''',
                'last_pause_period',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('last-pause-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of recent Pause Event
                ''',
                'last_pause_time',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('last-resume-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp of recent Resume Event
                ''',
                'last_resume_time',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('max-inflight-sessoin-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum no.of inflight sessions allowed
                ''',
                'max_inflight_sessoin_count',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('nack-to-srg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of NACKs sent to Srg
                ''',
                'nack_to_srg',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('nack-to-srg-fail-cnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of NACKs Failed to send to Srg
                ''',
                'nack_to_srg_fail_cnt',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('slave-create-update', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Create Update received on slave
                ''',
                'slave_create_update',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('slave-decode-fail', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Decode failed on Slave
                ''',
                'slave_decode_fail',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('slave-delete', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Delete received on slave
                ''',
                'slave_delete',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('slave-recv-entry', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Slave Recieved Sync
                ''',
                'slave_recv_entry',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sod-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of SODs Received
                ''',
                'sod_count',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sod-eod-dirty-delete-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Sessions Invalid Deletes Within SOD
                EOD Window
                ''',
                'sod_eod_dirty_delete_count',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sod-eod-dirty-mark-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Sessions Marked as Invalid Within SOD
                EOD Window
                ''',
                'sod_eod_dirty_mark_count',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sod-eod-replay-req-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Replay Requests Within SOD EOD Window
                ''',
                'sod_eod_replay_req_count',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('srg-context-free', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRG context freed
                ''',
                'srg_context_free',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('srg-context-malloc', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRG context allocated
                ''',
                'srg_context_malloc',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('total-dont-send-to-txlist', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total No of times Dont send to Txlist
                ''',
                'total_dont_send_to_txlist',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('total-master-eoms-pending', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total No of times Master EOMS Pending
                ''',
                'total_master_eoms_pending',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('total-pause-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total No.of times Pause is Enabled
                ''',
                'total_pause_count',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('total-pause-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total Amount of time paused during all flow
                control windows
                ''',
                'total_pause_time',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('total-resume-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total No.of times Resume is triggered
                ''',
                'total_resume_count',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('total-srg-not-master', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total No of times SRG Not Master
                ''',
                'total_srg_not_master',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('txlist-clean-invalid-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Txlist Cleanup called on Invalid
                subscriber srg state
                ''',
                'txlist_clean_invalid_state',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('txlist-del-app', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Txlist delete for App msg
                ''',
                'txlist_del_app',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('txlist-del-app-notlinked', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Txlist delete for App which are not
                linked
                ''',
                'txlist_del_app_notlinked',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('txlist-del-sync', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number for Txlist delete for sync msg
                ''',
                'txlist_del_sync',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('txlist-del-sync-notlinked', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Txlist delete for sync which are not
                linked
                ''',
                'txlist_del_sync_notlinked',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('txlist-encode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Txlist Encode
                ''',
                'txlist_encode',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('txlist-encode-fail', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Txlist encode Failed
                ''',
                'txlist_encode_fail',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('txlist-remove-all', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Txlist remove all calls
                ''',
                'txlist_remove_all',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('txlist-remove-all-internal-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Internal errors upon Master Txlist
                remove all call
                ''',
                'txlist_remove_all_internal_error',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('txlist-send-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Txlist Send Failed
                ''',
                'txlist_send_failed',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('txlist-send-failed-notactive', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Txlist send failed due to not active
                ''',
                'txlist_send_failed_notactive',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('txlist-send-triggered', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Txlist Send Triggered
                ''',
                'txlist_send_triggered',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'srg',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node.Statistics' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node.Statistics',
            False, 
            [
            _MetaInfoClassMember('aaa', REFERENCE_CLASS, 'Aaa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Aaa', 
                [], [], 
                '''                AAA statistics
                ''',
                'aaa',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('aggregate-summary', REFERENCE_CLASS, 'AggregateSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.AggregateSummary', 
                [], [], 
                '''                Aggregate summary of statistics
                ''',
                'aggregate_summary',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('srg', REFERENCE_CLASS, 'Srg' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics.Srg', 
                [], [], 
                '''                Geo Redundancy statistics
                ''',
                'srg',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-iedge4710-oper', True),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node.Statistics', 
                [], [], 
                '''                Subscriber manager statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager.Nodes' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes.Node', 
                [], [], 
                '''                Subscriber manager operational data for a
                particular node
                ''',
                'node',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Manager' : {
        'meta_info' : _MetaInfoClass('Subscriber.Manager',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager.Nodes', 
                [], [], 
                '''                Subscriber manager list of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'manager',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'state-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'address-family-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary',
            False, 
            [
            _MetaInfoClassMember('author-state', REFERENCE_ENUM_CLASS, 'SubscriberAuthorStateFilterFlagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'SubscriberAuthorStateFilterFlagEnum', 
                [], [], 
                '''                Authorization state
                ''',
                'author_state',
                'Cisco-IOS-XR-iedge4710-oper', True),
            _MetaInfoClassMember('address-family-xr', REFERENCE_CLASS, 'AddressFamilyXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr', 
                [], [], 
                '''                Address family summary
                ''',
                'address_family_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('state-xr', REFERENCE_CLASS, 'StateXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr', 
                [], [], 
                '''                State summary
                ''',
                'state_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'author-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthorSummaries' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthorSummaries',
            False, 
            [
            _MetaInfoClassMember('author-summary', REFERENCE_LIST, 'AuthorSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary', 
                [], [], 
                '''                authorization summary
                ''',
                'author_summary',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'author-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Summary.StateXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Summary.StateXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'state-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'address-family-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Summary' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Summary',
            False, 
            [
            _MetaInfoClassMember('address-family-xr', REFERENCE_CLASS, 'AddressFamilyXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr', 
                [], [], 
                '''                Address family summary
                ''',
                'address_family_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('state-xr', REFERENCE_CLASS, 'StateXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Summary.StateXr', 
                [], [], 
                '''                State summary
                ''',
                'state_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'state-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'address-family-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.MacSummaries.MacSummary',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Subscriber MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-iedge4710-oper', True),
            _MetaInfoClassMember('address-family-xr', REFERENCE_CLASS, 'AddressFamilyXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr', 
                [], [], 
                '''                Address family summary
                ''',
                'address_family_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('state-xr', REFERENCE_CLASS, 'StateXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr', 
                [], [], 
                '''                State summary
                ''',
                'state_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'mac-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.MacSummaries' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.MacSummaries',
            False, 
            [
            _MetaInfoClassMember('mac-summary', REFERENCE_LIST, 'MacSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.MacSummaries.MacSummary', 
                [], [], 
                '''                MAC address summary
                ''',
                'mac_summary',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'mac-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'state-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'address-family-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-iedge4710-oper', True),
            _MetaInfoClassMember('address-family-xr', REFERENCE_CLASS, 'AddressFamilyXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr', 
                [], [], 
                '''                Address family summary
                ''',
                'address_family_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('state-xr', REFERENCE_CLASS, 'StateXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr', 
                [], [], 
                '''                State summary
                ''',
                'state_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'interface-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.InterfaceSummaries' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.InterfaceSummaries',
            False, 
            [
            _MetaInfoClassMember('interface-summary', REFERENCE_LIST, 'InterfaceSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary', 
                [], [], 
                '''                Interface summary
                ''',
                'interface_summary',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'interface-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'state-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'address-family-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary',
            False, 
            [
            _MetaInfoClassMember('authentication-state', REFERENCE_ENUM_CLASS, 'SubscriberAuthenStateFilterFlagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'SubscriberAuthenStateFilterFlagEnum', 
                [], [], 
                '''                Authentication state
                ''',
                'authentication_state',
                'Cisco-IOS-XR-iedge4710-oper', True),
            _MetaInfoClassMember('address-family-xr', REFERENCE_CLASS, 'AddressFamilyXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr', 
                [], [], 
                '''                Address family summary
                ''',
                'address_family_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('state-xr', REFERENCE_CLASS, 'StateXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr', 
                [], [], 
                '''                State summary
                ''',
                'state_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'authentication-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AuthenticationSummaries' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AuthenticationSummaries',
            False, 
            [
            _MetaInfoClassMember('authentication-summary', REFERENCE_LIST, 'AuthenticationSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary', 
                [], [], 
                '''                authentication summary
                ''',
                'authentication_summary',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'authentication-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'state-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'address-family-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.StateSummaries.StateSummary',
            False, 
            [
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'SubscriberStateFilterFlagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'SubscriberStateFilterFlagEnum', 
                [], [], 
                '''                Subscriber state
                ''',
                'state',
                'Cisco-IOS-XR-iedge4710-oper', True),
            _MetaInfoClassMember('address-family-xr', REFERENCE_CLASS, 'AddressFamilyXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr', 
                [], [], 
                '''                Address family summary
                ''',
                'address_family_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('state-xr', REFERENCE_CLASS, 'StateXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr', 
                [], [], 
                '''                State summary
                ''',
                'state_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'state-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.StateSummaries' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.StateSummaries',
            False, 
            [
            _MetaInfoClassMember('state-summary', REFERENCE_LIST, 'StateSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.StateSummaries.StateSummary', 
                [], [], 
                '''                State summary
                ''',
                'state_summary',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'state-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'state-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'address-family-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subscriber IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('address-family-xr', REFERENCE_CLASS, 'AddressFamilyXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr', 
                [], [], 
                '''                Address family summary
                ''',
                'address_family_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('state-xr', REFERENCE_CLASS, 'StateXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr', 
                [], [], 
                '''                State summary
                ''',
                'state_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ipv4-address-vrf-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv4-address-vrf-summary', REFERENCE_LIST, 'Ipv4AddressVrfSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary', 
                [], [], 
                '''                IPv4 address and VRF summary
                ''',
                'ipv4_address_vrf_summary',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ipv4-address-vrf-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'state-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'address-family-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'SubscriberAddressFamilyFilterFlagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'SubscriberAddressFamilyFilterFlagEnum', 
                [], [], 
                '''                Address family
                ''',
                'address_family',
                'Cisco-IOS-XR-iedge4710-oper', True),
            _MetaInfoClassMember('address-family-xr', REFERENCE_CLASS, 'AddressFamilyXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr', 
                [], [], 
                '''                Address family summary
                ''',
                'address_family_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('state-xr', REFERENCE_CLASS, 'StateXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr', 
                [], [], 
                '''                State summary
                ''',
                'state_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'address-family-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AddressFamilySummaries' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AddressFamilySummaries',
            False, 
            [
            _MetaInfoClassMember('address-family-summary', REFERENCE_LIST, 'AddressFamilySummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary', 
                [], [], 
                '''                Address family summary
                ''',
                'address_family_summary',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'address-family-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'state-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'address-family-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary',
            False, 
            [
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Subscriber username
                ''',
                'username',
                'Cisco-IOS-XR-iedge4710-oper', True),
            _MetaInfoClassMember('address-family-xr', REFERENCE_CLASS, 'AddressFamilyXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr', 
                [], [], 
                '''                Address family summary
                ''',
                'address_family_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('state-xr', REFERENCE_CLASS, 'StateXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr', 
                [], [], 
                '''                State summary
                ''',
                'state_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'username-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.UsernameSummaries' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.UsernameSummaries',
            False, 
            [
            _MetaInfoClassMember('username-summary', REFERENCE_LIST, 'UsernameSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary', 
                [], [], 
                '''                Username summary
                ''',
                'username_summary',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'username-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'state-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'address-family-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-iedge4710-oper', True),
            _MetaInfoClassMember('address-family-xr', REFERENCE_CLASS, 'AddressFamilyXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr', 
                [], [], 
                '''                Address family summary
                ''',
                'address_family_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('state-xr', REFERENCE_CLASS, 'StateXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr', 
                [], [], 
                '''                State summary
                ''',
                'state_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'access-interface-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.AccessInterfaceSummaries',
            False, 
            [
            _MetaInfoClassMember('access-interface-summary', REFERENCE_LIST, 'AccessInterfaceSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary', 
                [], [], 
                '''                Access interface summary
                ''',
                'access_interface_summary',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'access-interface-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'state-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'address-family-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subscriber IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-iedge4710-oper', True),
            _MetaInfoClassMember('address-family-xr', REFERENCE_CLASS, 'AddressFamilyXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr', 
                [], [], 
                '''                Address family summary
                ''',
                'address_family_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('state-xr', REFERENCE_CLASS, 'StateXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr', 
                [], [], 
                '''                State summary
                ''',
                'state_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ipv4-address-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Ipv4AddressSummaries',
            False, 
            [
            _MetaInfoClassMember('ipv4-address-summary', REFERENCE_LIST, 'Ipv4AddressSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary', 
                [], [], 
                '''                IPv4 address summary
                ''',
                'ipv4_address_summary',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ipv4-address-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('activated-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in activated state
                ''',
                'activated_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connected state
                ''',
                'connected_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in connecting state
                ''',
                'connecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('disconnecting-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in disconnecting state
                ''',
                'disconnecting_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('end-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in end state
                ''',
                'end_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in idle state
                ''',
                'idle_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('initialized-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions in initialized state
                ''',
                'initialized_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'state-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket',
            False, 
            [
            _MetaInfoClassMember('dual-part-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack partially up sessions
                ''',
                'dual_part_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('dual-up-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dual stack up sessions
                ''',
                'dual_up_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('in-progress-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sessions with undecided address family
                ''',
                'in_progress_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 only sessions 
                ''',
                'ipv4_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-only-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 only sessions 
                ''',
                'ipv6_only_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAC sessions
                ''',
                'lac_sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'ip-subscriber-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr',
            False, 
            [
            _MetaInfoClassMember('ip-subscriber-dhcp', REFERENCE_CLASS, 'IpSubscriberDhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp', 
                [], [], 
                '''                IP subscriber DHCP summary
                ''',
                'ip_subscriber_dhcp',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-subscriber-packet', REFERENCE_CLASS, 'IpSubscriberPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket', 
                [], [], 
                '''                IP subscriber packet summary
                ''',
                'ip_subscriber_packet',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe', REFERENCE_CLASS, 'Pppoe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe', 
                [], [], 
                '''                PPPoE summary
                ''',
                'pppoe',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'address-family-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-iedge4710-oper', True),
            _MetaInfoClassMember('address-family-xr', REFERENCE_CLASS, 'AddressFamilyXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr', 
                [], [], 
                '''                Address family summary
                ''',
                'address_family_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('state-xr', REFERENCE_CLASS, 'StateXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr', 
                [], [], 
                '''                State summary
                ''',
                'state_xr',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'vrf-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.VrfSummaries' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.VrfSummaries',
            False, 
            [
            _MetaInfoClassMember('vrf-summary', REFERENCE_LIST, 'VrfSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary', 
                [], [], 
                '''                VRF summary
                ''',
                'vrf_summary',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'vrf-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Sessions.Session_.Accounting.AccountingSession' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Sessions.Session_.Accounting.AccountingSession',
            False, 
            [
            _MetaInfoClassMember('accepted-interim-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interim updates accepted
                ''',
                'accepted_interim_updates',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('account-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Accounting session ID
                ''',
                'account_session_id',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('accounting-start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Accounting start time in DDD MMM DD HH:MM:SS
                YYYY format eg: Tue Feb 15 15:12:49 2011
                ''',
                'accounting_start_time',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('accounting-state-rc', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting State Error Code for Accounting
                Session
                ''',
                'accounting_state_rc',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('accounting-stop-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting Stop State
                ''',
                'accounting_stop_state',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('interim-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interim accounting interval (in minutes)
                ''',
                'interim_interval',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('is-interim-accounting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if interim accounting is enabled
                ''',
                'is_interim_accounting_enabled',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('last-interim-update-attempt-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Time of last interim update attempt in DDD MMM
                DD HH:MM:SS YYYY format eg: Tue Apr 11 21:30:47
                2011
                ''',
                'last_interim_update_attempt_time',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('last-successful-interim-update-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Time of last successful interim update in DDD
                MMM DD HH:MM:SS YYYY format eg: Tue Apr 11 21:30
                :47 2011
                ''',
                'last_successful_interim_update_time',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('method-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AAA method list name used to perform accounting
                ''',
                'method_list_name',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('next-interim-update-attempt-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time of next interim update attempt (in seconds)
                ''',
                'next_interim_update_attempt_time',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('record-context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Accounting record context name
                ''',
                'record_context_name',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('rejected-interim-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interim updates rejected
                ''',
                'rejected_interim_updates',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sent-interim-update-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interim update send failures
                ''',
                'sent_interim_update_failures',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sent-interim-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interim updates sent
                ''',
                'sent_interim_updates',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'accounting-session',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Sessions.Session_.Accounting' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Sessions.Session_.Accounting',
            False, 
            [
            _MetaInfoClassMember('accounting-session', REFERENCE_LIST, 'AccountingSession' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Sessions.Session_.Accounting.AccountingSession', 
                [], [], 
                '''                Accounting information
                ''',
                'accounting_session',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Sessions.Session_.UserProfileAttributes' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Sessions.Session_.UserProfileAttributes',
            False, 
            [
            _MetaInfoClassMember('accounting-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Accounting session ID
                ''',
                'accounting_session_id',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('actual-data-rate-downstream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Actual data rate downstream (in Mbps)
                ''',
                'actual_data_rate_downstream',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('actual-data-rate-upstream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Actual data rate upstream (in Mbps)
                ''',
                'actual_data_rate_upstream',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('attainable-data-rate-downstream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Attainable data rate downstream (in Mbps)
                ''',
                'attainable_data_rate_downstream',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('attainable-data-rate-upstream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Attainable data rate upstream (in Mbps)
                ''',
                'attainable_data_rate_upstream',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('authorization-service-type', REFERENCE_ENUM_CLASS, 'AaaAuthServiceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'AaaAuthServiceEnum', 
                [], [], 
                '''                Authorization service type
                ''',
                'authorization_service_type',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('circuit-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Circuit ID
                ''',
                'circuit_id',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connection-receive-speed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Connection receive speed
                ''',
                'connection_receive_speed',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('connection-transmission-speed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Connection transmission speed
                ''',
                'connection_transmission_speed',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('destination-station-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination station ID
                ''',
                'destination_station_id',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('downstream-parameterized-qos-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Downstream parameterized QoS policy to be
                applied on the subscriber side
                ''',
                'downstream_parameterized_qos_policy',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('downstream-qos-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Downstream QoS policy to be applied on the
                subscriber side
                ''',
                'downstream_qos_policy',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('egress-access-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Egress access list
                ''',
                'egress_access_list',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('formatted-calling-station-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Formatted calling station id
                ''',
                'formatted_calling_station_id',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ingress-access-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ingress access list
                ''',
                'ingress_access_list',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('interface-type', REFERENCE_ENUM_CLASS, 'AaaInterfaceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'AaaInterfaceEnum', 
                [], [], 
                '''                Interface type
                ''',
                'interface_type',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('interim-accounting-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interim accounting interval
                ''',
                'interim_accounting_interval',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ip-netmask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP netmask for the user
                ''',
                'ip_netmask',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-unnumbered', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv4 unnumbered
                ''',
                'ipv4_unnumbered',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 maximum transmission unit
                ''',
                'ipv4mtu',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('is-interworking-functionality', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True, if interworking functionality
                ''',
                'is_interworking_functionality',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('max-data-rate-downstream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum data rate downstream (in Mbps)
                ''',
                'max_data_rate_downstream',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('max-data-rate-upstream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum data rate upstream (in Mbps)
                ''',
                'max_data_rate_upstream',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('max-interleaving-delay-downstream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum interleaving delay downstream (in Mbps)
                ''',
                'max_interleaving_delay_downstream',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('max-interleaving-delay-upstream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum interleaving delay upstream (in Mbps)
                ''',
                'max_interleaving_delay_upstream',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('min-data-rate-downstream', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum data rate downstream (in Mbps)
                ''',
                'min_data_rate_downstream',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('min-data-rate-downstream-low-power', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum data rate downstream low power (in Mbps)
                ''',
                'min_data_rate_downstream_low_power',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('min-data-rate-upstream-low-power', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum data rate upstream low power (in Mbps)
                ''',
                'min_data_rate_upstream_low_power',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('parent-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Parent interface name
                ''',
                'parent_interface_name',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pool-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address pool
                ''',
                'pool_address',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('primary-dns-server-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary DNS server address
                ''',
                'primary_dns_server_address',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('primary-net-bios-server-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary net bios server address
                ''',
                'primary_net_bios_server_address',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('remote-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote ID
                ''',
                'remote_id',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route information for a user session
                ''',
                'route',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('secondary-dns-server-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Secondary DNS server address
                ''',
                'secondary_dns_server_address',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('secondary-net-bios-server-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Secondary net bios server address
                ''',
                'secondary_net_bios_server_address',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-termination-cause', REFERENCE_ENUM_CLASS, 'AaaTerminateCauseEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'AaaTerminateCauseEnum', 
                [], [], 
                '''                Session termination cause
                ''',
                'session_termination_cause',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session timeout (in seconds)
                ''',
                'session_timeout',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('strict-rpf-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Strict RPF packets
                ''',
                'strict_rpf_packets',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('tunnel-client-authentication-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Tunnel client authentication ID
                ''',
                'tunnel_client_authentication_id',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('tunnel-client-endpoint', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Tunnel client endpoint
                ''',
                'tunnel_client_endpoint',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('tunnel-medium', REFERENCE_ENUM_CLASS, 'AaaTunnelMediumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'AaaTunnelMediumEnum', 
                [], [], 
                '''                Tunnel medium
                ''',
                'tunnel_medium',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('tunnel-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel preference
                ''',
                'tunnel_preference',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('tunnel-protocol', REFERENCE_ENUM_CLASS, 'AaaTunnelProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'AaaTunnelProtoEnum', 
                [], [], 
                '''                Tunnel protocol
                ''',
                'tunnel_protocol',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('tunnel-server-endpoint', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Tunnel server endpoint
                ''',
                'tunnel_server_endpoint',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('tunnel-tos-setting', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel TOS setting
                ''',
                'tunnel_tos_setting',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('upstream-parameterized-qos-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Upstream parameterized QoS policy to be applied
                on the subscriber side
                ''',
                'upstream_parameterized_qos_policy',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('upstream-qos-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Upstream QoS policy to be applied on the
                subscriber side
                ''',
                'upstream_qos_policy',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'user-profile-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Sessions.Session_.MobilityAttributes' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Sessions.Session_.MobilityAttributes',
            False, 
            [
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Domain Name
                ''',
                'domain_name',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('downlink-gre-key', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Downlink GRE Key
                ''',
                'downlink_gre_key',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lease-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of lease in seconds
                ''',
                'lease_time',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('mobility-default-ipv4-gateway', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Default Gateway IPv4 Address
                ''',
                'mobility_default_ipv4_gateway',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('mobility-dhcp-server', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DHCP Server
                ''',
                'mobility_dhcp_server',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('mobility-dns-server', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DNS Server Primary
                ''',
                'mobility_dns_server',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('mobility-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv4 address of Mobility Node
                ''',
                'mobility_ipv4_address',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('mobility-ipv4-netmask', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv4 Netmask
                ''',
                'mobility_ipv4_netmask',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('mpc-protocol', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Cisco MPC Protocol
                ''',
                'mpc_protocol',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('uplink-gre-key', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Uplink GRE Key
                ''',
                'uplink_gre_key',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'mobility-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Sessions.Session_.SessionChangeOfAuthorization' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Sessions.Session_.SessionChangeOfAuthorization',
            False, 
            [
            _MetaInfoClassMember('coa-reply-attributes', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                List of Reply Attributes collected in COA
                response
                ''',
                'coa_reply_attributes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('coa-request-attributes', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                List of Request Attributes collected in COA
                response
                ''',
                'coa_request_attributes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('reply-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reply time in DDD MMM DD HH:MM:SS YYYY format eg
                : Tue Apr 11 21:30:47 2011
                ''',
                'reply_time',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('request-acked', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Coa Request Acked
                ''',
                'request_acked',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('request-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Request time in DDD MMM DD HH:MM:SS YYYY format
                eg: Tue Apr 11 21:30:47 2011
                ''',
                'request_time',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'session-change-of-authorization',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Sessions.Session_' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Sessions.Session_',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-iedge4710-oper', True),
            _MetaInfoClassMember('access-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Access interface name associated with the
                session
                ''',
                'access_interface_name',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('account-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Accounting session ID
                ''',
                'account_session_id',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Sessions.Session_.Accounting', 
                [], [], 
                '''                Accounting information
                ''',
                'accounting',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('af-up-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AF status per Subscriber Session
                ''',
                'af_up_status',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('circuit-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Circuit ID
                ''',
                'circuit_id',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('clientname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Client Username
                ''',
                'clientname',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('delegated-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session delegated IPv6 prefix
                ''',
                'delegated_ipv6_prefix',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('formattedname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Formatted Username
                ''',
                'formattedname',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('idle-state-change-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Time when idle state change occurred in DDD MMM
                DD HH:MM:SS YYYY format eg: Tue Apr 11 21:30:47
                2011
                ''',
                'idle_state_change_time',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv6-interface-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                IPv6 Interface ID
                ''',
                'ipv6_interface_id',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('is-session-authentic', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, session is authentic
                ''',
                'is_session_authentic',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('is-session-author', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, session is authorized
                ''',
                'is_session_author',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                PPPoE LAC address
                ''',
                'lac_address',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('lns-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                PPPoE LNS address
                ''',
                'lns_address',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('mobility-attributes', REFERENCE_CLASS, 'MobilityAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Sessions.Session_.MobilityAttributes', 
                [], [], 
                '''                List of mobility attributes collected for
                subscriber session
                ''',
                'mobility_attributes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('nas-port', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NAS port
                ''',
                'nas_port',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pending-callbacks', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Active pending callbacks bitmask
                ''',
                'pending_callbacks',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('pppoe-sub-type', REFERENCE_ENUM_CLASS, 'IedgePppSubEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'IedgePppSubEnum', 
                [], [], 
                '''                PPPoE sub type
                ''',
                'pppoe_sub_type',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('remote-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote ID
                ''',
                'remote_id',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-change-of-authorization', REFERENCE_LIST, 'SessionChangeOfAuthorization' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Sessions.Session_.SessionChangeOfAuthorization', 
                [], [], 
                '''                Subscriber change of authorization information
                ''',
                'session_change_of_authorization',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-creation-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session creation time in DDD MMM DD HH:MM:SS
                YYYY format eg: Tue Apr 11 21:30:47 2011
                ''',
                'session_creation_time',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Session ip address
                ''',
                'session_ip_address',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-ipv4-state', REFERENCE_ENUM_CLASS, 'IedgeOperSessionAfStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'IedgeOperSessionAfStateEnum', 
                [], [], 
                '''                Session IPv4 state
                ''',
                'session_ipv4_state',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session IPv6 address
                ''',
                'session_ipv6_address',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session IPv6 prefix
                ''',
                'session_ipv6_prefix',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-ipv6-state', REFERENCE_ENUM_CLASS, 'IedgeOperSessionAfStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'IedgeOperSessionAfStateEnum', 
                [], [], 
                '''                Session IPv6 state
                ''',
                'session_ipv6_state',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-state', REFERENCE_ENUM_CLASS, 'IedgeOperSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'IedgeOperSessionStateEnum', 
                [], [], 
                '''                Session state
                ''',
                'session_state',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'IedgeOperSessionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'IedgeOperSessionEnum', 
                [], [], 
                '''                Subscriber session type
                ''',
                'session_type',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('total-session-idle-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total session idle time (in seconds)
                ''',
                'total_session_idle_time',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('tunnel-client-authentication-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                PPPoE LAC tunnel client authentication ID
                ''',
                'tunnel_client_authentication_id',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('tunnel-server-authentication-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                PPPoE LAC tunnel server authentication ID
                ''',
                'tunnel_server_authentication_id',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('user-profile-attributes', REFERENCE_CLASS, 'UserProfileAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Sessions.Session_.UserProfileAttributes', 
                [], [], 
                '''                List of user profile attributes collected for
                subscriber session
                ''',
                'user_profile_attributes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Username
                ''',
                'username',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node.Sessions' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Sessions.Session_', 
                [], [], 
                '''                Subscriber session information
                ''',
                'session',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-iedge4710-oper', True),
            _MetaInfoClassMember('access-interface-summaries', REFERENCE_CLASS, 'AccessInterfaceSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AccessInterfaceSummaries', 
                [], [], 
                '''                Summary information filtered by access
                interface
                ''',
                'access_interface_summaries',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('address-family-summaries', REFERENCE_CLASS, 'AddressFamilySummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AddressFamilySummaries', 
                [], [], 
                '''                Summary information filtered by address
                family
                ''',
                'address_family_summaries',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('authentication-summaries', REFERENCE_CLASS, 'AuthenticationSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthenticationSummaries', 
                [], [], 
                '''                Summary information filtered by
                authentication state
                ''',
                'authentication_summaries',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('author-summaries', REFERENCE_CLASS, 'AuthorSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.AuthorSummaries', 
                [], [], 
                '''                Summary information filtered by authorization
                state
                ''',
                'author_summaries',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('interface-summaries', REFERENCE_CLASS, 'InterfaceSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.InterfaceSummaries', 
                [], [], 
                '''                Summary information filtered by interface
                ''',
                'interface_summaries',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-address-summaries', REFERENCE_CLASS, 'Ipv4AddressSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressSummaries', 
                [], [], 
                '''                Summary information filtered by subscriber
                IPv4 address
                ''',
                'ipv4_address_summaries',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('ipv4-address-vrf-summaries', REFERENCE_CLASS, 'Ipv4AddressVrfSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries', 
                [], [], 
                '''                Summary information filtered by IPv4 address
                and VRF
                ''',
                'ipv4_address_vrf_summaries',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('mac-summaries', REFERENCE_CLASS, 'MacSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.MacSummaries', 
                [], [], 
                '''                Summary information filtered by MAC address
                ''',
                'mac_summaries',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Sessions', 
                [], [], 
                '''                IP subscriber sessions
                ''',
                'sessions',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('state-summaries', REFERENCE_CLASS, 'StateSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.StateSummaries', 
                [], [], 
                '''                Summary information filtered by session state
                ''',
                'state_summaries',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.Summary', 
                [], [], 
                '''                Subscriber session summary information
                ''',
                'summary',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('username-summaries', REFERENCE_CLASS, 'UsernameSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.UsernameSummaries', 
                [], [], 
                '''                Summary information filtered by username
                ''',
                'username_summaries',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('vrf-summaries', REFERENCE_CLASS, 'VrfSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node.VrfSummaries', 
                [], [], 
                '''                Summary information filtered by VRF
                ''',
                'vrf_summaries',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session.Nodes' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes.Node', 
                [], [], 
                '''                Subscriber session operational data for a
                particular node
                ''',
                'node',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber.Session' : {
        'meta_info' : _MetaInfoClass('Subscriber.Session',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session.Nodes', 
                [], [], 
                '''                List of subscriber session supported nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'Subscriber' : {
        'meta_info' : _MetaInfoClass('Subscriber',
            False, 
            [
            _MetaInfoClassMember('manager', REFERENCE_CLASS, 'Manager' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Manager', 
                [], [], 
                '''                Subscriber manager operational data
                ''',
                'manager',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'Subscriber.Session', 
                [], [], 
                '''                Subscriber session operational data
                ''',
                'session',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'subscriber',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'IedgeLicenseManager.Nodes.Node.IedgeLicenseManagerSummary' : {
        'meta_info' : _MetaInfoClass('IedgeLicenseManager.Nodes.Node.IedgeLicenseManagerSummary',
            False, 
            [
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of sessions
                ''',
                'session_count',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-license-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of license
                ''',
                'session_license_count',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                configured session limit
                ''',
                'session_limit',
                'Cisco-IOS-XR-iedge4710-oper', False),
            _MetaInfoClassMember('session-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                configured session threshold
                ''',
                'session_threshold',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'iedge-license-manager-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'IedgeLicenseManager.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('IedgeLicenseManager.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('nodeid', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node id to filter on. For example,
                0/1/CPU0
                ''',
                'nodeid',
                'Cisco-IOS-XR-iedge4710-oper', True),
            _MetaInfoClassMember('iedge-license-manager-summary', REFERENCE_CLASS, 'IedgeLicenseManagerSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'IedgeLicenseManager.Nodes.Node.IedgeLicenseManagerSummary', 
                [], [], 
                '''                Display Session License Manager summary data
                ''',
                'iedge_license_manager_summary',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'IedgeLicenseManager.Nodes' : {
        'meta_info' : _MetaInfoClass('IedgeLicenseManager.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'IedgeLicenseManager.Nodes.Node', 
                [], [], 
                '''                Location. For example, 0/1/CPU0
                ''',
                'node',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
    'IedgeLicenseManager' : {
        'meta_info' : _MetaInfoClass('IedgeLicenseManager',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper', 'IedgeLicenseManager.Nodes', 
                [], [], 
                '''                Session License Manager operational data for a
                location
                ''',
                'nodes',
                'Cisco-IOS-XR-iedge4710-oper', False),
            ],
            'Cisco-IOS-XR-iedge4710-oper',
            'iedge-license-manager',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper'
        ),
    },
}
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Start']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Stop']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Interim']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.PassThrough']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Update']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.InterimInflight']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthenticationStatistics']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthorizationStatistics']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.MobilityStatistics']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Start']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Stop']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Interim']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.PassThrough']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Update']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.InterimInflight']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthenticationStatistics']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthorizationStatistics']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.MobilityStatistics']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.AggregateSummary']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics.Srg']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node.Statistics']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node.Statistics']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes.Node']['meta_info']
_meta_table['Subscriber.Manager.Nodes.Node']['meta_info'].parent =_meta_table['Subscriber.Manager.Nodes']['meta_info']
_meta_table['Subscriber.Manager.Nodes']['meta_info'].parent =_meta_table['Subscriber.Manager']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Summary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Summary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Summary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Summary.StateXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Summary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Summary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.MacSummaries']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.StateSummaries']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_.Accounting.AccountingSession']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_.Accounting']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_.Accounting']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_.UserProfileAttributes']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_.MobilityAttributes']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_.SessionChangeOfAuthorization']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node.Sessions']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Summary']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.MacSummaries']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.StateSummaries']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.VrfSummaries']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node.Sessions']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes.Node']['meta_info']
_meta_table['Subscriber.Session.Nodes.Node']['meta_info'].parent =_meta_table['Subscriber.Session.Nodes']['meta_info']
_meta_table['Subscriber.Session.Nodes']['meta_info'].parent =_meta_table['Subscriber.Session']['meta_info']
_meta_table['Subscriber.Manager']['meta_info'].parent =_meta_table['Subscriber']['meta_info']
_meta_table['Subscriber.Session']['meta_info'].parent =_meta_table['Subscriber']['meta_info']
_meta_table['IedgeLicenseManager.Nodes.Node.IedgeLicenseManagerSummary']['meta_info'].parent =_meta_table['IedgeLicenseManager.Nodes.Node']['meta_info']
_meta_table['IedgeLicenseManager.Nodes.Node']['meta_info'].parent =_meta_table['IedgeLicenseManager.Nodes']['meta_info']
_meta_table['IedgeLicenseManager.Nodes']['meta_info'].parent =_meta_table['IedgeLicenseManager']['meta_info']
