


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'Ipv6Assembler' : {
        'meta_info' : _MetaInfoClass('Ipv6Assembler',
            False, 
            [
            _MetaInfoClassMember('max-packets', ATTRIBUTE, 'int' , None, None, 
                [(1, 50)], [], 
                '''                Maxinum packets allowed in assembly queues (in
                percent)
                ''',
                'max_packets',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [(1, 120)], [], 
                '''                Number of seconds an assembly queue will hold
                before timeout
                ''',
                'timeout',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-io-cfg',
            'ipv6-assembler',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-io-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_io_cfg'
        ),
    },
    'Ipv6icmp' : {
        'meta_info' : _MetaInfoClass('Ipv6icmp',
            False, 
            [
            _MetaInfoClassMember('bucket-size', ATTRIBUTE, 'int' , None, None, 
                [(1, 200)], [], 
                '''                Bucket size
                ''',
                'bucket_size',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            _MetaInfoClassMember('error-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                Interval between tokens in milliseconds
                ''',
                'error_interval',
                'Cisco-IOS-XR-ipv6-io-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-io-cfg',
            'ipv6icmp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-io-cfg'],
        'ydk.models.ipv6.Cisco_IOS_XR_ipv6_io_cfg'
        ),
    },
}
