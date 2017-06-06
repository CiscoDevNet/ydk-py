


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ipv6Telnet.Client' : {
        'meta_info' : _MetaInfoClass('Ipv6Telnet.Client',
            False, 
            [
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source interface for telnet sessions
                ''',
                'source_interface',
                'Cisco-IOS-XR-ipv4-telnet-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-telnet-cfg',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-telnet-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_cfg'
        ),
    },
    'Ipv6Telnet' : {
        'meta_info' : _MetaInfoClass('Ipv6Telnet',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_CLASS, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_cfg', 'Ipv6Telnet.Client', 
                [], [], 
                '''                Telnet client configuration
                ''',
                'client',
                'Cisco-IOS-XR-ipv4-telnet-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-telnet-cfg',
            'ipv6-telnet',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-telnet-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_cfg'
        ),
    },
    'Ipv4Telnet.Client' : {
        'meta_info' : _MetaInfoClass('Ipv4Telnet.Client',
            False, 
            [
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source interface for telnet sessions
                ''',
                'source_interface',
                'Cisco-IOS-XR-ipv4-telnet-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-telnet-cfg',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-telnet-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_cfg'
        ),
    },
    'Ipv4Telnet' : {
        'meta_info' : _MetaInfoClass('Ipv4Telnet',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_CLASS, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_cfg', 'Ipv4Telnet.Client', 
                [], [], 
                '''                Telnet client configuration
                ''',
                'client',
                'Cisco-IOS-XR-ipv4-telnet-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-telnet-cfg',
            'ipv4-telnet',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-telnet-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_cfg'
        ),
    },
}
_meta_table['Ipv6Telnet.Client']['meta_info'].parent =_meta_table['Ipv6Telnet']['meta_info']
_meta_table['Ipv4Telnet.Client']['meta_info'].parent =_meta_table['Ipv4Telnet']['meta_info']
