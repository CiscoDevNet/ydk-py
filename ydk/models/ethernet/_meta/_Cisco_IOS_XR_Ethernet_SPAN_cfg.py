


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SpanTrafficDirection_Enum' : _MetaInfoEnum('SpanTrafficDirection_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg',
        {
            'rx-only':'RX_ONLY',
            'tx-only':'TX_ONLY',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-cfg', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg']),
    'SpanMirrorInterval_Enum' : _MetaInfoEnum('SpanMirrorInterval_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg',
        {
            '512':'Y_512',
            '1k':'Y_1K',
            '2k':'Y_2K',
            '4k':'Y_4K',
            '8k':'Y_8K',
            '16k':'Y_16K',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-cfg', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg']),
    'SpanDestination_Enum' : _MetaInfoEnum('SpanDestination_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg',
        {
            'interface':'INTERFACE',
            'pseudowire':'PSEUDOWIRE',
            'ipv4-address':'IPV4_ADDRESS',
            'ipv6-address':'IPV6_ADDRESS',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-cfg', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg']),
    'SpanMonitorSession.Sessions.Session.Destination' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Sessions.Session.Destination',
            False, 
            [
            _MetaInfoClassMember('destination-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify the destination interface name
                ''',
                'destination_interface_name',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('destination-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Specify the destination next-hop IPv4 address
                ''',
                'destination_ipv4_address',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('destination-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Specify the destination next-hop IPv6 address
                ''',
                'destination_ipv6_address',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('destination-type', REFERENCE_ENUM_CLASS, 'SpanDestination_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanDestination_Enum', 
                [], [], 
                '''                Specify the type of destination
                ''',
                'destination_type',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg'
        ),
    },
    'SpanMonitorSession.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('session', ATTRIBUTE, 'str' , None, None, 
                [(0, 79)], [], 
                '''                Session Name
                ''',
                'session',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', True),
            _MetaInfoClassMember('class', REFERENCE_ENUM_CLASS, 'SpanSessionClass_Enum' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClass_Enum', 
                [], [], 
                '''                Enable a Monitor Session.  Setting this item
                causes the Monitor Session to be created.
                ''',
                'class_',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            _MetaInfoClassMember('destination', REFERENCE_CLASS, 'Destination' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanMonitorSession.Sessions.Session.Destination', 
                [], [], 
                '''                Specify a destination
                ''',
                'destination',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg'
        ),
    },
    'SpanMonitorSession.Sessions' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanMonitorSession.Sessions.Session', 
                [], [], 
                '''                Configuration for a particular Monitor Session
                ''',
                'session',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg'
        ),
    },
    'SpanMonitorSession' : {
        'meta_info' : _MetaInfoClass('SpanMonitorSession',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg', 'SpanMonitorSession.Sessions', 
                [], [], 
                '''                Monitor-session configuration commands
                ''',
                'sessions',
                'Cisco-IOS-XR-Ethernet-SPAN-cfg', False),
            ],
            'Cisco-IOS-XR-Ethernet-SPAN-cfg',
            'span-monitor-session',
            _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-cfg'],
        'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_cfg'
        ),
    },
}
_meta_table['SpanMonitorSession.Sessions.Session.Destination']['meta_info'].parent =_meta_table['SpanMonitorSession.Sessions.Session']['meta_info']
_meta_table['SpanMonitorSession.Sessions.Session']['meta_info'].parent =_meta_table['SpanMonitorSession.Sessions']['meta_info']
_meta_table['SpanMonitorSession.Sessions']['meta_info'].parent =_meta_table['SpanMonitorSession']['meta_info']
