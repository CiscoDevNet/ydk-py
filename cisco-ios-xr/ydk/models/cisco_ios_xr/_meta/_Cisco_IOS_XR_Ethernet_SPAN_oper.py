


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SessionClassEnum' : _MetaInfoEnum('SessionClassEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper',
        {
            'ethernet-class':'ethernet_class',
            'ipv4-class':'ipv4_class',
            'ipv6-class':'ipv6_class',
            'invalid-class':'invalid_class',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-oper', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper']),
    'ImStateEnumEnum' : _MetaInfoEnum('ImStateEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper',
        {
            'im-state-not-ready':'im_state_not_ready',
            'im-state-admin-down':'im_state_admin_down',
            'im-state-down':'im_state_down',
            'im-state-up':'im_state_up',
            'im-state-shutdown':'im_state_shutdown',
            'im-state-err-disable':'im_state_err_disable',
            'im-state-down-immediate':'im_state_down_immediate',
            'im-state-down-immediate-admin':'im_state_down_immediate_admin',
            'im-state-down-graceful':'im_state_down_graceful',
            'im-state-begin-shutdown':'im_state_begin_shutdown',
            'im-state-end-shutdown':'im_state_end_shutdown',
            'im-state-begin-error-disable':'im_state_begin_error_disable',
            'im-state-end-error-disable':'im_state_end_error_disable',
            'im-state-begin-down-graceful':'im_state_begin_down_graceful',
            'im-state-reset':'im_state_reset',
            'im-state-operational':'im_state_operational',
            'im-state-not-operational':'im_state_not_operational',
            'im-state-unknown':'im_state_unknown',
            'im-state-last':'im_state_last',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-oper', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper']),
    'DestinationClassEnum' : _MetaInfoEnum('DestinationClassEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper',
        {
            'interface-class':'interface_class',
            'pseudowire-class':'pseudowire_class',
            'next-hop-ipv4-class':'next_hop_ipv4_class',
            'next-hop-ipv6-class':'next_hop_ipv6_class',
            'invalid-class':'invalid_class',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-oper', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper']),
    'TrafficDirectionEnum' : _MetaInfoEnum('TrafficDirectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper',
        {
            'invalid':'invalid',
            'rx-only':'rx_only',
            'tx-only':'tx_only',
            'both':'both',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-oper', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper']),
    'MirrorIntervalEnum' : _MetaInfoEnum('MirrorIntervalEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper',
        {
            'mirror-interval-all':'mirror_interval_all',
            'mirror-interval512':'mirror_interval512',
            'mirror-interval1k':'mirror_interval1k',
            'mirror-interval2k':'mirror_interval2k',
            'mirror-interval4k':'mirror_interval4k',
            'mirror-interval8k':'mirror_interval8k',
            'mirror-interval16k':'mirror_interval16k',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-oper', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper']),
    'SpanMonitorSession.Global_.Statistics.Statistic' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global_.Statistics.Statistic',
            False, 
            [
            _MetaInfoClassMember('session', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Session Name
                ''',
                'session',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', True),
            _MetaInfoClassMember('octets-not-mirrored', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Octets Not Mirrored
                ''',
                'octets_not_mirrored',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('packets-not-mirrored', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets Not Mirrored
                ''',
                'packets_not_mirrored',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('rx-octets-mirrored', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX Octets Mirrored
                ''',
                'rx_octets_mirrored',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('rx-packets-mirrored', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX Packets Mirrored
                ''',
                'rx_packets_mirrored',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('tx-octets-mirrored', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TX Octets Mirrored
                ''',
                'tx_octets_mirrored',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('tx-packets-mirrored', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TX Packets Mirrored
                ''',
                'tx_packets_mirrored',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global_.Statistics' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global_.Statistics',
            False, 
            [
            _MetaInfoClassMember('statistic', REFERENCE_LIST, 'Statistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global_.Statistics.Statistic', 
                [], [], 
                '''                Statistics for a particular source interface
                ''',
                'statistic',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface-state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Interface State
                ''',
                'interface_state',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'interface-data',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data',
            False, 
            [
            _MetaInfoClassMember('address-is-reachable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Address is reachable
                ''',
                'address_is_reachable',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data',
            False, 
            [
            _MetaInfoClassMember('address-is-reachable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Address is reachable
                ''',
                'address_is_reachable',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData',
            False, 
            [
            _MetaInfoClassMember('destination-class', REFERENCE_ENUM_CLASS, 'DestinationClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClassEnum', 
                [], [], 
                '''                DestinationClass
                ''',
                'destination_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface-data', REFERENCE_CLASS, 'InterfaceData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData', 
                [], [], 
                '''                Interface data
                ''',
                'interface_data',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('invalid-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid Parameter
                ''',
                'invalid_value',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('next-hop-ipv4-data', REFERENCE_CLASS, 'NextHopIpv4Data' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data', 
                [], [], 
                '''                Next-hop IPv4 data
                ''',
                'next_hop_ipv4_data',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('next-hop-ipv6-data', REFERENCE_CLASS, 'NextHopIpv6Data' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data', 
                [], [], 
                '''                Next-hop IPv6 data
                ''',
                'next_hop_ipv6_data',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('pseudowire-data', REFERENCE_CLASS, 'PseudowireData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData', 
                [], [], 
                '''                Pseudowire data
                ''',
                'pseudowire_data',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'destination-data',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId',
            False, 
            [
            _MetaInfoClassMember('destination-class', REFERENCE_ENUM_CLASS, 'DestinationClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClassEnum', 
                [], [], 
                '''                DestinationClass
                ''',
                'destination_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Handle
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('invalid-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid Parameter
                ''',
                'invalid_value',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv4-address-and-vrf', REFERENCE_CLASS, 'Ipv4AddressAndVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf', 
                [], [], 
                '''                IPv4 address
                ''',
                'ipv4_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv6-address-and-vrf', REFERENCE_CLASS, 'Ipv6AddressAndVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf', 
                [], [], 
                '''                IPv6 address
                ''',
                'ipv6_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pseudowire XCID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'destination-id',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global_.GlobalSessions.GlobalSession' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global_.GlobalSessions.GlobalSession',
            False, 
            [
            _MetaInfoClassMember('session', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Session Name
                ''',
                'session',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', True),
            _MetaInfoClassMember('destination-data', REFERENCE_CLASS, 'DestinationData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData', 
                [], [], 
                '''                Destination data
                ''',
                'destination_data',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last error observed for the destination 
                ''',
                'destination_error',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-id', REFERENCE_CLASS, 'DestinationId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId', 
                [], [], 
                '''                Destination ID
                ''',
                'destination_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
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
                [('0', '4294967295')], [], 
                '''                Numerical ID assigned to session
                ''',
                'id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            _MetaInfoClassMember('session-class', REFERENCE_ENUM_CLASS, 'SessionClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClassEnum', 
                [], [], 
                '''                Session class
                ''',
                'session_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'global-session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global_.GlobalSessions' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global_.GlobalSessions',
            False, 
            [
            _MetaInfoClassMember('global-session', REFERENCE_LIST, 'GlobalSession' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global_.GlobalSessions.GlobalSession', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Global_' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Global_',
            False, 
            [
            _MetaInfoClassMember('global-sessions', REFERENCE_CLASS, 'GlobalSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global_.GlobalSessions', 
                [], [], 
                '''                Global Monitor Sessions table
                ''',
                'global_sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global_.Statistics', 
                [], [], 
                '''                Table of statistics for source interfaces
                ''',
                'statistics',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
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
                [('0', '4294967295')], [], 
                '''                Number of bytes to mirror
                ''',
                'mirror_bytes',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('mirror-interval', REFERENCE_ENUM_CLASS, 'MirrorIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'MirrorIntervalEnum', 
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
            _MetaInfoClassMember('traffic-direction', REFERENCE_ENUM_CLASS, 'TrafficDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirectionEnum', 
                [], [], 
                '''                Direction
                ''',
                'traffic_direction',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'traffic-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId',
            False, 
            [
            _MetaInfoClassMember('destination-class', REFERENCE_ENUM_CLASS, 'DestinationClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClassEnum', 
                [], [], 
                '''                DestinationClass
                ''',
                'destination_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Handle
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('invalid-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid Parameter
                ''',
                'invalid_value',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv4-address-and-vrf', REFERENCE_CLASS, 'Ipv4AddressAndVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf', 
                [], [], 
                '''                IPv4 address
                ''',
                'ipv4_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv6-address-and-vrf', REFERENCE_CLASS, 'Ipv6AddressAndVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf', 
                [], [], 
                '''                IPv6 address
                ''',
                'ipv6_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pseudowire XCID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'destination-id',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Attachments.Attachment' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Attachments.Attachment',
            False, 
            [
            _MetaInfoClassMember('session', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Session Name
                ''',
                'session',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', True),
            _MetaInfoClassMember('dest-pw-type-not-supported', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The destination PW type is not supported
                ''',
                'dest_pw_type_not_supported',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-id', REFERENCE_CLASS, 'DestinationId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId', 
                [], [], 
                '''                Destination ID
                ''',
                'destination_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Destination interface (deprecated by
                DestinationID, invalid for pseudowires)
                ''',
                'destination_interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('global-class', REFERENCE_ENUM_CLASS, 'SessionClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClassEnum', 
                [], [], 
                '''                Global session class
                ''',
                'global_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Numerical ID assigned to session
                ''',
                'id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('local-class', REFERENCE_ENUM_CLASS, 'SessionClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClassEnum', 
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
                [('0', '4294967295')], [], 
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
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source interface
                ''',
                'source_interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('source-interface-is-a-destination', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This source interface is a destination for
                another monitor-session
                ''',
                'source_interface_is_a_destination',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('source-interface-state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Source interface state
                ''',
                'source_interface_state',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('traffic-direction', REFERENCE_ENUM_CLASS, 'TrafficDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirectionEnum', 
                [], [], 
                '''                Traffic mirroring direction (deprecated by
                TrafficParameters)
                ''',
                'traffic_direction',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('traffic-parameters', REFERENCE_CLASS, 'TrafficParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters', 
                [], [], 
                '''                Traffic mirroring parameters
                ''',
                'traffic_parameters',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'attachment',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Attachments' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Attachments',
            False, 
            [
            _MetaInfoClassMember('attachment', REFERENCE_LIST, 'Attachment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Attachments.Attachment', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId',
            False, 
            [
            _MetaInfoClassMember('destination-class', REFERENCE_ENUM_CLASS, 'DestinationClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClassEnum', 
                [], [], 
                '''                DestinationClass
                ''',
                'destination_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Handle
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('invalid-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid Parameter
                ''',
                'invalid_value',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv4-address-and-vrf', REFERENCE_CLASS, 'Ipv4AddressAndVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf', 
                [], [], 
                '''                IPv4 address
                ''',
                'ipv4_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv6-address-and-vrf', REFERENCE_CLASS, 'Ipv6AddressAndVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf', 
                [], [], 
                '''                IPv6 address
                ''',
                'ipv6_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pseudowire XCID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'destination-id',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession',
            False, 
            [
            _MetaInfoClassMember('destination-id', REFERENCE_CLASS, 'DestinationId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId', 
                [], [], 
                '''                Destination ID
                ''',
                'destination_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Destination interface (deprecated by
                DestinationID, invalid for pseudowires)
                ''',
                'destination_interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
                '''                Last error observed for this session while
                programming the hardware
                ''',
                'platform_error',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('session-class', REFERENCE_ENUM_CLASS, 'SpanSessionClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClassEnum', 
                [], [], 
                '''                Sesssion class
                ''',
                'session_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('session-class-xr', REFERENCE_ENUM_CLASS, 'SessionClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClassEnum', 
                [], [], 
                '''                Session class
                ''',
                'session_class_xr',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'hardware-session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.HardwareSessions' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.HardwareSessions',
            False, 
            [
            _MetaInfoClassMember('hardware-session', REFERENCE_LIST, 'HardwareSession' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId',
            False, 
            [
            _MetaInfoClassMember('destination-class', REFERENCE_ENUM_CLASS, 'DestinationClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClassEnum', 
                [], [], 
                '''                DestinationClass
                ''',
                'destination_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Handle
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('invalid-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid Parameter
                ''',
                'invalid_value',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv4-address-and-vrf', REFERENCE_CLASS, 'Ipv4AddressAndVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf', 
                [], [], 
                '''                IPv4 address
                ''',
                'ipv4_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv6-address-and-vrf', REFERENCE_CLASS, 'Ipv6AddressAndVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf', 
                [], [], 
                '''                IPv6 address
                ''',
                'ipv6_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pseudowire XCID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'destination-id',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
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
                [('0', '4294967295')], [], 
                '''                Number of bytes to mirror
                ''',
                'mirror_bytes',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('mirror-interval', REFERENCE_ENUM_CLASS, 'MirrorIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'MirrorIntervalEnum', 
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
            _MetaInfoClassMember('traffic-direction', REFERENCE_ENUM_CLASS, 'TrafficDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirectionEnum', 
                [], [], 
                '''                Direction
                ''',
                'traffic_direction',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'traffic-mirroring-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId',
            False, 
            [
            _MetaInfoClassMember('destination-class', REFERENCE_ENUM_CLASS, 'DestinationClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClassEnum', 
                [], [], 
                '''                DestinationClass
                ''',
                'destination_class',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Handle
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('invalid-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid Parameter
                ''',
                'invalid_value',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv4-address-and-vrf', REFERENCE_CLASS, 'Ipv4AddressAndVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf', 
                [], [], 
                '''                IPv4 address
                ''',
                'ipv4_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('ipv6-address-and-vrf', REFERENCE_CLASS, 'Ipv6AddressAndVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf', 
                [], [], 
                '''                IPv6 address
                ''',
                'ipv6_address_and_vrf',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('pseudowire-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pseudowire XCID
                ''',
                'pseudowire_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'destination-id',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
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
                [('0', '4294967295')], [], 
                '''                Number of bytes to mirror
                ''',
                'mirror_bytes',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('mirror-interval', REFERENCE_ENUM_CLASS, 'MirrorIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'MirrorIntervalEnum', 
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
            _MetaInfoClassMember('traffic-direction', REFERENCE_ENUM_CLASS, 'TrafficDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirectionEnum', 
                [], [], 
                '''                Direction
                ''',
                'traffic_direction',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'traffic-mirroring-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_ENUM_CLASS, 'SessionClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClassEnum', 
                [], [], 
                '''                Attachment class
                ''',
                'class_',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-id', REFERENCE_CLASS, 'DestinationId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId', 
                [], [], 
                '''                Destination ID
                ''',
                'destination_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('traffic-mirroring-parameters', REFERENCE_CLASS, 'TrafficMirroringParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters', 
                [], [], 
                '''                Traffic mirroring parameters
                ''',
                'traffic_mirroring_parameters',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'attachment',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', True),
            _MetaInfoClassMember('attachment', REFERENCE_LIST, 'Attachment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment', 
                [], [], 
                '''                Attachment information
                ''',
                'attachment',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-id', REFERENCE_CLASS, 'DestinationId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId', 
                [], [], 
                '''                Destination ID (deprecated by Attachment)
                ''',
                'destination_id',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('destination-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Destination interface (deprecated by Attachment)
                ''',
                'destination_interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('platform-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last error observed for this interface while
                programming the hardware
                ''',
                'platform_error',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source interface
                ''',
                'source_interface',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('traffic-direction', REFERENCE_ENUM_CLASS, 'TrafficDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirectionEnum', 
                [], [], 
                '''                Traffic mirroring direction (deprecated by
                Attachment)
                ''',
                'traffic_direction',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('traffic-mirroring-parameters', REFERENCE_CLASS, 'TrafficMirroringParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces.Interface', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node
                ''',
                'node',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', True),
            _MetaInfoClassMember('attachments', REFERENCE_CLASS, 'Attachments' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Attachments', 
                [], [], 
                '''                Table of source interfaces configured as
                attached to a session
                ''',
                'attachments',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('hardware-sessions', REFERENCE_CLASS, 'HardwareSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.HardwareSessions', 
                [], [], 
                '''                Table of sessions set up in the hardware. 
                When all sessions are operating correctly the
                entries in this table should match those
                entries in GlobalSessionTable that have a
                destination configured
                ''',
                'hardware_sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node.Interfaces', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession.Nodes' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes.Node', 
                [], [], 
                '''                Node-specific data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
    'SpanMonitorSession' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Global_', 
                [], [], 
                '''                Global operational data
                ''',
                'global_',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SpanMonitorSession.Nodes', 
                [], [], 
                '''                Node table for node-specific operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-Ethernet-SPAN-oper', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-oper',
            'span-monitor-session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper'
        ),
    },
}
_meta_table['SpanMonitorSession.Global_.Statistics.Statistic']['meta_info'].parent =_meta_table['SpanMonitorSession.Global_.Statistics']['meta_info']
_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData']['meta_info'].parent =_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData']['meta_info']
_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData']['meta_info'].parent =_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData']['meta_info']
_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data']['meta_info'].parent =_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData']['meta_info']
_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data']['meta_info'].parent =_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData']['meta_info']
_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData']['meta_info'].parent =_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession']['meta_info']
_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId']['meta_info'].parent =_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession']['meta_info']
_meta_table['SpanMonitorSession.Global_.GlobalSessions.GlobalSession']['meta_info'].parent =_meta_table['SpanMonitorSession.Global_.GlobalSessions']['meta_info']
_meta_table['SpanMonitorSession.Global_.Statistics']['meta_info'].parent =_meta_table['SpanMonitorSession.Global_']['meta_info']
_meta_table['SpanMonitorSession.Global_.GlobalSessions']['meta_info'].parent =_meta_table['SpanMonitorSession.Global_']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Attachments.Attachment']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Attachments']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node.Interfaces']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Attachments']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.HardwareSessions']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes.Node']['meta_info']
_meta_table['SpanMonitorSession.Nodes.Node']['meta_info'].parent =_meta_table['SpanMonitorSession.Nodes']['meta_info']
_meta_table['SpanMonitorSession.Global_']['meta_info'].parent =_meta_table['SpanMonitorSession']['meta_info']
_meta_table['SpanMonitorSession.Nodes']['meta_info'].parent =_meta_table['SpanMonitorSession']['meta_info']
