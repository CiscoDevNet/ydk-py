


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ipv6SrpEncapsulationEnum' : _MetaInfoEnum('Ipv6SrpEncapsulationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg',
        {
            'srpa':'srpa',
            'srpb':'srpb',
        }, 'Cisco-IOS-XR-ipv6-nd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-cfg']),
    'Ipv6NdMonthEnum' : _MetaInfoEnum('Ipv6NdMonthEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg',
        {
            'january':'january',
            'february':'february',
            'march':'march',
            'april':'april',
            'may':'may',
            'june':'june',
            'july':'july',
            'august':'august',
            'september':'september',
            'october':'october',
            'november':'november',
            'december':'december',
        }, 'Cisco-IOS-XR-ipv6-nd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-cfg']),
    'Ipv6NdRouterPrefEnum' : _MetaInfoEnum('Ipv6NdRouterPrefEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg',
        {
            'high':'high',
            'medium':'medium',
            'low':'low',
        }, 'Cisco-IOS-XR-ipv6-nd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-cfg']),
    'Ipv6Neighbor.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Ipv6Neighbor.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv6-nd-cfg', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-nd-cfg', True),
            _MetaInfoClassMember('encapsulation', REFERENCE_ENUM_CLASS, 'Ipv6SrpEncapsulationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6SrpEncapsulationEnum', 
                [], [], 
                '''                Encapsulation type only if interface type is
                SRP
                ''',
                'encapsulation',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                48-bit hardware address H.H.H
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('zone', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv6 address zone
                ''',
                'zone',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg'
        ),
    },
    'Ipv6Neighbor.Neighbors' : {
        'meta_info' : _MetaInfoClass('Ipv6Neighbor.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6Neighbor.Neighbors.Neighbor', 
                [], [], 
                '''                IPv6 neighbor configuration
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg'
        ),
    },
    'Ipv6Neighbor' : {
        'meta_info' : _MetaInfoClass('Ipv6Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg', 'Ipv6Neighbor.Neighbors', 
                [], [], 
                '''                IPv6 neighbors
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            _MetaInfoClassMember('scavenge-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '43200')], [], 
                '''                Set lifetime for stale neighbor
                ''',
                'scavenge_timeout',
                'Cisco-IOS-XR-ipv6-nd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-cfg',
            'ipv6-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg'
        ),
    },
}
_meta_table['Ipv6Neighbor.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Ipv6Neighbor.Neighbors']['meta_info']
_meta_table['Ipv6Neighbor.Neighbors']['meta_info'].parent =_meta_table['Ipv6Neighbor']['meta_info']
