


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ipv6Configuration.Ipv6Assembler' : {
        'meta_info' : _MetaInfoClass('Ipv6Configuration.Ipv6Assembler',
            False, 
            [
            _MetaInfoClassMember('max-packets', ATTRIBUTE, 'int' , None, None, 
                [('1', '50')], [], 
                '''                Maxinum packets allowed in assembly queues (in
                percent)
                ''',
                'max_packets',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '120')], [], 
                '''                Number of seconds an assembly queue will hold
                before timeout
                ''',
                'timeout',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-io-cfg',
            'ipv6-assembler',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-io-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg'
        ),
    },
    'Ipv6Configuration.Ipv6Icmp' : {
        'meta_info' : _MetaInfoClass('Ipv6Configuration.Ipv6Icmp',
            False, 
            [
            _MetaInfoClassMember('bucket-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '200')], [], 
                '''                Bucket size
                ''',
                'bucket_size',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            _MetaInfoClassMember('error-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Interval between tokens in milliseconds
                ''',
                'error_interval',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-io-cfg',
            'ipv6icmp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-io-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg'
        ),
    },
    'Ipv6Configuration' : {
        'meta_info' : _MetaInfoClass('Ipv6Configuration',
            False, 
            [
            _MetaInfoClassMember('ipv6-assembler', REFERENCE_CLASS, 'Ipv6Assembler' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg', 'Ipv6Configuration.Ipv6Assembler', 
                [], [], 
                '''                IPv6 fragmented packet assembler
                ''',
                'ipv6_assembler',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            _MetaInfoClassMember('ipv6-hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Configure IPv6 hop count limit
                ''',
                'ipv6_hop_limit',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            _MetaInfoClassMember('ipv6-pmtu-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'ipv6_pmtu_enable',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            _MetaInfoClassMember('ipv6-pmtu-time-out', ATTRIBUTE, 'int' , None, None, 
                [('1', '15')], [], 
                '''                Configure IPv6 Path MTU timeout value in minutes
                ''',
                'ipv6_pmtu_time_out',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            _MetaInfoClassMember('ipv6-source-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if enabled, FALSE if disabled
                ''',
                'ipv6_source_route',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            _MetaInfoClassMember('ipv6icmp', REFERENCE_CLASS, 'Ipv6Icmp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg', 'Ipv6Configuration.Ipv6Icmp', 
                [], [], 
                '''                Configure IPv6 ICMP parameters
                ''',
                'ipv6icmp',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-io-cfg',
            'ipv6-configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-io-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_io_cfg'
        ),
    },
}
_meta_table['Ipv6Configuration.Ipv6Assembler']['meta_info'].parent =_meta_table['Ipv6Configuration']['meta_info']
_meta_table['Ipv6Configuration.Ipv6Icmp']['meta_info'].parent =_meta_table['Ipv6Configuration']['meta_info']
