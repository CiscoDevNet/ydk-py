


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'ImStateEnumEnum' : _MetaInfoEnum('ImStateEnumEnum', 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper',
        {
            'im-state-not-ready':'IM_STATE_NOT_READY',
            'im-state-admin-down':'IM_STATE_ADMIN_DOWN',
            'im-state-down':'IM_STATE_DOWN',
            'im-state-up':'IM_STATE_UP',
            'im-state-shutdown':'IM_STATE_SHUTDOWN',
            'im-state-err-disable':'IM_STATE_ERR_DISABLE',
            'im-state-down-immediate':'IM_STATE_DOWN_IMMEDIATE',
            'im-state-down-immediate-admin':'IM_STATE_DOWN_IMMEDIATE_ADMIN',
            'im-state-down-graceful':'IM_STATE_DOWN_GRACEFUL',
            'im-state-begin-shutdown':'IM_STATE_BEGIN_SHUTDOWN',
            'im-state-end-shutdown':'IM_STATE_END_SHUTDOWN',
            'im-state-begin-error-disable':'IM_STATE_BEGIN_ERROR_DISABLE',
            'im-state-end-error-disable':'IM_STATE_END_ERROR_DISABLE',
            'im-state-begin-down-graceful':'IM_STATE_BEGIN_DOWN_GRACEFUL',
            'im-state-reset':'IM_STATE_RESET',
            'im-state-operational':'IM_STATE_OPERATIONAL',
            'im-state-not-operational':'IM_STATE_NOT_OPERATIONAL',
            'im-state-unknown':'IM_STATE_UNKNOWN',
            'im-state-last':'IM_STATE_LAST',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-oper', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper']),
    'DestinationClassEnum' : _MetaInfoEnum('DestinationClassEnum', 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper',
        {
            'interface-class':'INTERFACE_CLASS',
            'pseudowire-class':'PSEUDOWIRE_CLASS',
            'next-hop-ipv4-class':'NEXT_HOP_IPV4_CLASS',
            'next-hop-ipv6-class':'NEXT_HOP_IPV6_CLASS',
            'invalid-class':'INVALID_CLASS',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-oper', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper']),
    'TrafficDirectionEnum' : _MetaInfoEnum('TrafficDirectionEnum', 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper',
        {
            'invalid':'INVALID',
            'rx-only':'RX_ONLY',
            'tx-only':'TX_ONLY',
            'both':'BOTH',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-oper', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper']),
    'SessionClassEnum' : _MetaInfoEnum('SessionClassEnum', 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper',
        {
            'ethernet-class':'ETHERNET_CLASS',
            'ipv4-class':'IPV4_CLASS',
            'ipv6-class':'IPV6_CLASS',
            'invalid-class':'INVALID_CLASS',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-oper', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper']),
    'MirrorIntervalEnum' : _MetaInfoEnum('MirrorIntervalEnum', 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper',
        {
            'mirror-interval-all':'MIRROR_INTERVAL_ALL',
            'mirror-interval512':'MIRROR_INTERVAL512',
            'mirror-interval1k':'MIRROR_INTERVAL1K',
            'mirror-interval2k':'MIRROR_INTERVAL2K',
            'mirror-interval4k':'MIRROR_INTERVAL4K',
            'mirror-interval8k':'MIRROR_INTERVAL8K',
            'mirror-interval16k':'MIRROR_INTERVAL16K',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-oper', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper']),
    'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.InterfaceData' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.InterfaceData',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface-state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Interface State
                ''',
                'interface_state',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'interface-data',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data',
            False, 
            [
            _MetaInfoClassMember('address-is-reachable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Address is reachable
                ''',
                'address_is_reachable',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'next-hop-ipv4-data',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data',
            False, 
            [
            _MetaInfoClassMember('address-is-reachable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Address is reachable
                ''',
                'address_is_reachable',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'next-hop-ipv6-data',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.PseudowireData' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.PseudowireData',
            False, 
            [
            _MetaInfoClassMember('pseudowire-is-up', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Pseudowire State
                ''',
                'pseudowire_is_up',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('pseudowire-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Pseudowire Name
                ''',
                'pseudowire_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'pseudowire-data',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData',
            False, 
            [
            _MetaInfoClassMember('destination-class', REFERENCE_ENUM_CLASS, 'DestinationClassEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClassEnum', 
                [], [], 
                '''                DestinationClass
                ''',
                'destination_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface-data', REFERENCE_CLASS, 'InterfaceData' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.InterfaceData', 
                [], [], 
                '''                Interface data
                ''',
                'interface_data',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('invalid-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Invalid Parameter
                ''',
                'invalid_value',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('next-hop-ipv4-data', REFERENCE_CLASS, 'NextHopIpv4Data' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data', 
                [], [], 
                '''                Next-hop IPv4 data
                ''',
                'next_hop_ipv4_data',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('next-hop-ipv6-data', REFERENCE_CLASS, 'NextHopIpv6Data' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data', 
                [], [], 
                '''                Next-hop IPv6 data
                ''',
                'next_hop_ipv6_data',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('pseudowire-data', REFERENCE_CLASS, 'PseudowireData' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.PseudowireData', 
                [], [], 
                '''                Pseudowire data
                ''',
                'pseudowire_data',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'destination-data',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'ipv4-address-and-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'ipv6-address-and-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId',
            False, 
            [
            _MetaInfoClassMember('destination-class', REFERENCE_ENUM_CLASS, 'DestinationClassEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClassEnum', 
                [], [], 
                '''                DestinationClass
                ''',
                'destination_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Handle
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('invalid-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Invalid Parameter
                ''',
                'invalid_value',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv4-address-and-vrf', REFERENCE_CLASS, 'Ipv4AddressAndVrf' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf', 
                [], [], 
                '''                IPv4 address
                ''',
                'ipv4_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv6-address-and-vrf', REFERENCE_CLASS, 'Ipv6AddressAndVrf' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf', 
                [], [], 
                '''                IPv6 address
                ''',
                'ipv6_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Pseudowire XCID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'destination-id',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global.GlobalSessions.GlobalSession' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global.GlobalSessions.GlobalSession',
            False, 
            [
            _MetaInfoClassMember('session', ATTRIBUTE, 'str' , None, None, 
                [(0, 79)], [], 
                '''                Session Name
                ''',
                'session',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', True),
            _MetaInfoClassMember('destination-data', REFERENCE_CLASS, 'DestinationData' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData', 
                [], [], 
                '''                Destination data
                ''',
                'destination_data',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Last error observed for the destination 
                ''',
                'destination_error',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-id', REFERENCE_CLASS, 'DestinationId' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId', 
                [], [], 
                '''                Destination ID
                ''',
                'destination_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Destination interface handle (deprecated by
                DestinationID, invalid for pseudowires)
                ''',
                'destination_interface_handle',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination interface name (deprecated by
                DestinationData, invalid for pseudowires)
                ''',
                'destination_interface_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Numerical ID assigned to session
                ''',
                'id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Last error observed for the destination
                interface (deprecated by DestinationError)
                ''',
                'interface_error',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session Name
                ''',
                'name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('session-class', REFERENCE_ENUM_CLASS, 'SessionClassEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClassEnum', 
                [], [], 
                '''                Session class
                ''',
                'session_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'global-session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global.GlobalSessions' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global.GlobalSessions',
            False, 
            [
            _MetaInfoClassMember('global-session', REFERENCE_LIST, 'GlobalSession' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global.GlobalSessions.GlobalSession', 
                [], [], 
                '''                Information about a globally-configured
                monitor session
                ''',
                'global_session',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'global-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global',
            False, 
            [
            _MetaInfoClassMember('global-sessions', REFERENCE_CLASS, 'GlobalSessions' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global.GlobalSessions', 
                [], [], 
                '''                Global Monitor Sessions table
                ''',
                'global_sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'ipv4-address-and-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'ipv6-address-and-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId',
            False, 
            [
            _MetaInfoClassMember('destination-class', REFERENCE_ENUM_CLASS, 'DestinationClassEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClassEnum', 
                [], [], 
                '''                DestinationClass
                ''',
                'destination_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Handle
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('invalid-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Invalid Parameter
                ''',
                'invalid_value',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv4-address-and-vrf', REFERENCE_CLASS, 'Ipv4AddressAndVrf' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf', 
                [], [], 
                '''                IPv4 address
                ''',
                'ipv4_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv6-address-and-vrf', REFERENCE_CLASS, 'Ipv6AddressAndVrf' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf', 
                [], [], 
                '''                IPv6 address
                ''',
                'ipv6_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Pseudowire XCID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'destination-id',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters',
            False, 
            [
            _MetaInfoClassMember('is-acl-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ACL enabled
                ''',
                'is_acl_enabled',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('mirror-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of bytes to mirror
                ''',
                'mirror_bytes',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('mirror-interval', REFERENCE_ENUM_CLASS, 'MirrorIntervalEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'MirrorIntervalEnum', 
                [], [], 
                '''                Interval between mirrored packets
                ''',
                'mirror_interval',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('port-level', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Port level mirroring
                ''',
                'port_level',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('traffic-direction', REFERENCE_ENUM_CLASS, 'TrafficDirectionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirectionEnum', 
                [], [], 
                '''                Direction
                ''',
                'traffic_direction',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'traffic-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Attachments.Attachment' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Attachments.Attachment',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', True),
            _MetaInfoClassMember('session', ATTRIBUTE, 'str' , None, None, 
                [(0, 79)], [], 
                '''                Session Name
                ''',
                'session',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', True),
            _MetaInfoClassMember('dest-pw-type-not-supported', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The destination PW type is not supported
                ''',
                'dest_pw_type_not_supported',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-id', REFERENCE_CLASS, 'DestinationId' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId', 
                [], [], 
                '''                Destination ID
                ''',
                'destination_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Destination interface (deprecated by
                DestinationID, invalid for pseudowires)
                ''',
                'destination_interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('global-class', REFERENCE_ENUM_CLASS, 'SessionClassEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClassEnum', 
                [], [], 
                '''                Global session class
                ''',
                'global_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Numerical ID assigned to session
                ''',
                'id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('local-class', REFERENCE_ENUM_CLASS, 'SessionClassEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClassEnum', 
                [], [], 
                '''                Local attachment class
                ''',
                'local_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session Name
                ''',
                'name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('pfi-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Last error returned from PFI for this interface
                ''',
                'pfi_error',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('session-is-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The Session is configured globally
                ''',
                'session_is_configured',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source interface
                ''',
                'source_interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('source-interface-state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Source interface state
                ''',
                'source_interface_state',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('traffic-direction', REFERENCE_ENUM_CLASS, 'TrafficDirectionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirectionEnum', 
                [], [], 
                '''                Traffic mirroring direction (deprecated by
                TrafficParameters)
                ''',
                'traffic_direction',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('traffic-parameters', REFERENCE_CLASS, 'TrafficParameters' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters', 
                [], [], 
                '''                Traffic mirroring parameters
                ''',
                'traffic_parameters',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'attachment',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Attachments' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Attachments',
            False, 
            [
            _MetaInfoClassMember('attachment', REFERENCE_LIST, 'Attachment' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Attachments.Attachment', 
                [], [], 
                '''                Information about a particular source
                interface configured as attached to monitor
                session
                ''',
                'attachment',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'attachments',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'ipv4-address-and-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'ipv6-address-and-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId',
            False, 
            [
            _MetaInfoClassMember('destination-class', REFERENCE_ENUM_CLASS, 'DestinationClassEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClassEnum', 
                [], [], 
                '''                DestinationClass
                ''',
                'destination_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Handle
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('invalid-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Invalid Parameter
                ''',
                'invalid_value',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv4-address-and-vrf', REFERENCE_CLASS, 'Ipv4AddressAndVrf' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf', 
                [], [], 
                '''                IPv4 address
                ''',
                'ipv4_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv6-address-and-vrf', REFERENCE_CLASS, 'Ipv6AddressAndVrf' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf', 
                [], [], 
                '''                IPv6 address
                ''',
                'ipv6_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Pseudowire XCID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'destination-id',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession',
            False, 
            [
            _MetaInfoClassMember('destination-id', REFERENCE_CLASS, 'DestinationId' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId', 
                [], [], 
                '''                Destination ID
                ''',
                'destination_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Destination interface (deprecated by
                DestinationID, invalid for pseudowires)
                ''',
                'destination_interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Assigned numerical ID for this session
                ''',
                'id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configured Session Name
                ''',
                'name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('platform-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Last error observed for this session while
                programming the hardware
                ''',
                'platform_error',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('session-class', REFERENCE_ENUM_CLASS, 'SpanSessionClassEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClassEnum', 
                [], [], 
                '''                Sesssion class
                ''',
                'session_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('session-class-xr', REFERENCE_ENUM_CLASS, 'SessionClassEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClassEnum', 
                [], [], 
                '''                Session class
                ''',
                'session_class_xr',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'hardware-session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.HardwareSessions' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.HardwareSessions',
            False, 
            [
            _MetaInfoClassMember('hardware-session', REFERENCE_LIST, 'HardwareSession' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession', 
                [], [], 
                '''                Information about a particular session that
                is set up in the hardware
                ''',
                'hardware_session',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'hardware-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'ipv4-address-and-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'ipv6-address-and-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId',
            False, 
            [
            _MetaInfoClassMember('destination-class', REFERENCE_ENUM_CLASS, 'DestinationClassEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClassEnum', 
                [], [], 
                '''                DestinationClass
                ''',
                'destination_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Handle
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('invalid-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Invalid Parameter
                ''',
                'invalid_value',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv4-address-and-vrf', REFERENCE_CLASS, 'Ipv4AddressAndVrf' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf', 
                [], [], 
                '''                IPv4 address
                ''',
                'ipv4_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv6-address-and-vrf', REFERENCE_CLASS, 'Ipv6AddressAndVrf' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf', 
                [], [], 
                '''                IPv6 address
                ''',
                'ipv6_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Pseudowire XCID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'destination-id',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters',
            False, 
            [
            _MetaInfoClassMember('is-acl-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ACL enabled
                ''',
                'is_acl_enabled',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('mirror-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of bytes to mirror
                ''',
                'mirror_bytes',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('mirror-interval', REFERENCE_ENUM_CLASS, 'MirrorIntervalEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'MirrorIntervalEnum', 
                [], [], 
                '''                Interval between mirrored packets
                ''',
                'mirror_interval',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('port-level', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Port level mirroring
                ''',
                'port_level',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('traffic-direction', REFERENCE_ENUM_CLASS, 'TrafficDirectionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirectionEnum', 
                [], [], 
                '''                Direction
                ''',
                'traffic_direction',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'traffic-mirroring-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_ENUM_CLASS, 'SessionClassEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClassEnum', 
                [], [], 
                '''                Attachment class
                ''',
                'class_',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-id', REFERENCE_CLASS, 'DestinationId' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId', 
                [], [], 
                '''                Destination ID
                ''',
                'destination_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('traffic-mirroring-parameters', REFERENCE_CLASS, 'TrafficMirroringParameters' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters', 
                [], [], 
                '''                Traffic mirroring parameters
                ''',
                'traffic_mirroring_parameters',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'attachment',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'ipv4-address-and-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'ipv6-address-and-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId',
            False, 
            [
            _MetaInfoClassMember('destination-class', REFERENCE_ENUM_CLASS, 'DestinationClassEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClassEnum', 
                [], [], 
                '''                DestinationClass
                ''',
                'destination_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Handle
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('invalid-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Invalid Parameter
                ''',
                'invalid_value',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv4-address-and-vrf', REFERENCE_CLASS, 'Ipv4AddressAndVrf' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf', 
                [], [], 
                '''                IPv4 address
                ''',
                'ipv4_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv6-address-and-vrf', REFERENCE_CLASS, 'Ipv6AddressAndVrf' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf', 
                [], [], 
                '''                IPv6 address
                ''',
                'ipv6_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Pseudowire XCID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'destination-id',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters',
            False, 
            [
            _MetaInfoClassMember('is-acl-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ACL enabled
                ''',
                'is_acl_enabled',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('mirror-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of bytes to mirror
                ''',
                'mirror_bytes',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('mirror-interval', REFERENCE_ENUM_CLASS, 'MirrorIntervalEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'MirrorIntervalEnum', 
                [], [], 
                '''                Interval between mirrored packets
                ''',
                'mirror_interval',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('port-level', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Port level mirroring
                ''',
                'port_level',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('traffic-direction', REFERENCE_ENUM_CLASS, 'TrafficDirectionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirectionEnum', 
                [], [], 
                '''                Direction
                ''',
                'traffic_direction',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'traffic-mirroring-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', True),
            _MetaInfoClassMember('attachment', REFERENCE_LIST, 'Attachment' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment', 
                [], [], 
                '''                Attachment information
                ''',
                'attachment',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-id', REFERENCE_CLASS, 'DestinationId' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId', 
                [], [], 
                '''                Destination ID (deprecated by Attachment)
                ''',
                'destination_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Destination interface (deprecated by Attachment)
                ''',
                'destination_interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('platform-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Last error observed for this interface while
                programming the hardware
                ''',
                'platform_error',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source interface
                ''',
                'source_interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('traffic-direction', REFERENCE_ENUM_CLASS, 'TrafficDirectionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirectionEnum', 
                [], [], 
                '''                Traffic mirroring direction (deprecated by
                Attachment)
                ''',
                'traffic_direction',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('traffic-mirroring-parameters', REFERENCE_CLASS, 'TrafficMirroringParameters' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters', 
                [], [], 
                '''                Traffic mirroring parameters (deprecated by
                Attachment)
                ''',
                'traffic_mirroring_parameters',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                Information about a particular interface that
                is set up in the hardware
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node
                ''',
                'node',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', True),
            _MetaInfoClassMember('attachments', REFERENCE_CLASS, 'Attachments' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Attachments', 
                [], [], 
                '''                Table of source interfaces configured as
                attached to a session
                ''',
                'attachments',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('hardware-sessions', REFERENCE_CLASS, 'HardwareSessions' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.HardwareSessions', 
                [], [], 
                '''                Table of sessions set up in the hardware. 
                When all sessions are operating correctly the
                entries in this table should match those
                entries in GlobalSessionTable that have a
                destination configured
                ''',
                'hardware_sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces', 
                [], [], 
                '''                Table of source interfaces set up in the
                hardware.  The entries in this table should
                match the entries in AttachmentTable when all
                sessions are operating correctly
                ''',
                'interfaces',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node', 
                [], [], 
                '''                Node-specific data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global', 
                [], [], 
                '''                Global operational data
                ''',
                'global_',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes', 
                [], [], 
                '''                Node table for node-specific operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'span-monitor-session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
}
_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.InterfaceData']['meta_info'].parent =_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData']['meta_info']
_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data']['meta_info'].parent =_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData']['meta_info']
_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data']['meta_info'].parent =_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData']['meta_info']
_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.PseudowireData']['meta_info'].parent =_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData']['meta_info']
_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData']['meta_info'].parent =_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession']['meta_info']
_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId']['meta_info'].parent =_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession']['meta_info']
_meta_table['SpanMonitorSession.Global.GlobalSessions.GlobalSession']['meta_info'].parent =_meta_table['SpanMonitorSession.Global.GlobalSessions']['meta_info']
_meta_table['SpanMonitorSession.Global.GlobalSessions']['meta_info'].parent =_meta_table['SpanMonitorSession.Global']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Attachments']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Attachments']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes']['meta_info']
_meta_table['SpanMonitorSession.Global']['meta_info'].parent =_meta_table['SpanMonitorSession']['meta_info']
_meta_table['SpanMonitorSession.Nodes']['meta_info'].parent =_meta_table['SpanMonitorSession']['meta_info']
