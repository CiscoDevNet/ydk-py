


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Cdp' : {
        'meta_info' : _MetaInfoClass('Cdp',
            False, 
            [
            _MetaInfoClassMember('advertise-v1-only', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable CDPv1 only advertisements
                ''',
                'advertise_v1_only',
                'Cisco-IOS-XR-cdp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable CDP globally
                ''',
                'enable',
                'Cisco-IOS-XR-cdp-cfg', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('10', '255')], [], 
                '''                Length of time (in sec) that the receiver must
                keep a CDP packet
                ''',
                'hold_time',
                'Cisco-IOS-XR-cdp-cfg', False),
            _MetaInfoClassMember('log-adjacency', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging of adjacency changes
                ''',
                'log_adjacency',
                'Cisco-IOS-XR-cdp-cfg', False),
            _MetaInfoClassMember('timer', ATTRIBUTE, 'int' , None, None, 
                [('5', '255')], [], 
                '''                Specify the rate at which CDP packets are sent
                ''',
                'timer',
                'Cisco-IOS-XR-cdp-cfg', False),
            ],
            'Cisco-IOS-XR-cdp-cfg',
            'cdp',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_cfg'
        ),
    },
}
