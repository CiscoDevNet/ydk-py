


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SpanDestinationEnum' : _MetaInfoEnum('SpanDestinationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg',
        {
            'interface':'interface',
            'pseudowire':'pseudowire',
            'ipv4-address':'ipv4_address',
            'ipv6-address':'ipv6_address',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-cfg', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg']),
    'SpanMirrorIntervalEnum' : _MetaInfoEnum('SpanMirrorIntervalEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg',
        {
            '512':'Y_512',
            '1k':'Y_1k',
            '2k':'Y_2k',
            '4k':'Y_4k',
            '8k':'Y_8k',
            '16k':'Y_16k',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-cfg', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg']),
    'SpanTrafficDirectionEnum' : _MetaInfoEnum('SpanTrafficDirectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg',
        {
            'rx-only':'rx_only',
            'tx-only':'tx_only',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-cfg', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg']),
    'SpanMonitorSession.Sessions.Session.Destination' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Sessions.Session.Destination',
            False, 
            [
            _MetaInfoClassMember('destination-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify the destination interface name
                ''',
                'destination_interface_name',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('destination-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Specify the destination next-hop IPv4 address
                ''',
                'destination_ipv4_address',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('destination-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Specify the destination next-hop IPv6 address
                ''',
                'destination_ipv6_address',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('destination-type', REFERENCE_ENUM_CLASS, 'SpanDestinationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanDestinationEnum', 
                [], [], 
                '''                Specify the type of destination
                ''',
                'destination_type',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg'
        ),
    },
    'SpanMonitorSession.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('session', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                Session Name
                ''',
                'session',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', True),
            _MetaInfoClassMember('class', REFERENCE_ENUM_CLASS, 'SpanSessionClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClassEnum', 
                [], [], 
                '''                Enable a Monitor Session.  Setting this item
                causes the Monitor Session to be created.
                ''',
                'class_',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('destination', REFERENCE_CLASS, 'Destination' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanMonitorSession.Sessions.Session.Destination', 
                [], [], 
                '''                Specify a destination
                ''',
                'destination',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg'
        ),
    },
    'SpanMonitorSession.Sessions' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanMonitorSession.Sessions.Session', 
                [], [], 
                '''                Configuration for a particular Monitor Session
                ''',
                'session',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg'
        ),
    },
    'SpanMonitorSession' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanMonitorSession.Sessions', 
                [], [], 
                '''                Monitor-session configuration commands
                ''',
                'sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'span-monitor-session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg'
        ),
    },
}
_meta_table['SpanMonitorSession.Sessions.Session.Destination']['meta_info'].parent =_meta_table['SpanMonitorSession.Sessions.Session']['meta_info']
_meta_table['SpanMonitorSession.Sessions.Session']['meta_info'].parent =_meta_table['SpanMonitorSession.Sessions']['meta_info']
_meta_table['SpanMonitorSession.Sessions']['meta_info'].parent =_meta_table['SpanMonitorSession']['meta_info']
