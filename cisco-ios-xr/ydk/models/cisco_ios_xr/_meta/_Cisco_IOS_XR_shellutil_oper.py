


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'TimeSourceEnum' : _MetaInfoEnum('TimeSourceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper',
        {
            'error':'error',
            'none':'none',
            'ntp':'ntp',
            'manual':'manual',
            'calendar':'calendar',
        }, 'Cisco-IOS-XR-shellutil-oper', _yang_ns._namespaces['Cisco-IOS-XR-shellutil-oper']),
    'SystemTime.Clock' : {
        'meta_info' : _MetaInfoClass('SystemTime.Clock',
            False, 
            [
            _MetaInfoClassMember('day', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Day [1..31]
                ''',
                'day',
                'Cisco-IOS-XR-shellutil-oper', False),
            _MetaInfoClassMember('hour', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Hour [0..23]
                ''',
                'hour',
                'Cisco-IOS-XR-shellutil-oper', False),
            _MetaInfoClassMember('millisecond', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Millisecond [0..999]
                ''',
                'millisecond',
                'Cisco-IOS-XR-shellutil-oper', False),
            _MetaInfoClassMember('minute', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Minute [0..59]
                ''',
                'minute',
                'Cisco-IOS-XR-shellutil-oper', False),
            _MetaInfoClassMember('month', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Month [1..12]
                ''',
                'month',
                'Cisco-IOS-XR-shellutil-oper', False),
            _MetaInfoClassMember('second', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Second [0..60], use 60 for leap-second
                ''',
                'second',
                'Cisco-IOS-XR-shellutil-oper', False),
            _MetaInfoClassMember('time-source', REFERENCE_ENUM_CLASS, 'TimeSourceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper', 'TimeSourceEnum', 
                [], [], 
                '''                Time source
                ''',
                'time_source',
                'Cisco-IOS-XR-shellutil-oper', False),
            _MetaInfoClassMember('time-zone', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Time zone
                ''',
                'time_zone',
                'Cisco-IOS-XR-shellutil-oper', False),
            _MetaInfoClassMember('wday', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Week Day [0..6]
                ''',
                'wday',
                'Cisco-IOS-XR-shellutil-oper', False),
            _MetaInfoClassMember('year', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Year [0..65535]
                ''',
                'year',
                'Cisco-IOS-XR-shellutil-oper', False),
            ],
            'Cisco-IOS-XR-shellutil-oper',
            'clock',
            _yang_ns._namespaces['Cisco-IOS-XR-shellutil-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper'
        ),
    },
    'SystemTime.Uptime' : {
        'meta_info' : _MetaInfoClass('SystemTime.Uptime',
            False, 
            [
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Host name
                ''',
                'host_name',
                'Cisco-IOS-XR-shellutil-oper', False),
            _MetaInfoClassMember('uptime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Amount of time in seconds since this system    
                was last initialized
                ''',
                'uptime',
                'Cisco-IOS-XR-shellutil-oper', False),
            ],
            'Cisco-IOS-XR-shellutil-oper',
            'uptime',
            _yang_ns._namespaces['Cisco-IOS-XR-shellutil-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper'
        ),
    },
    'SystemTime' : {
        'meta_info' : _MetaInfoClass('SystemTime',
            False, 
            [
            _MetaInfoClassMember('clock', REFERENCE_CLASS, 'Clock' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper', 'SystemTime.Clock', 
                [], [], 
                '''                System clock information
                ''',
                'clock',
                'Cisco-IOS-XR-shellutil-oper', False),
            _MetaInfoClassMember('uptime', REFERENCE_CLASS, 'Uptime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper', 'SystemTime.Uptime', 
                [], [], 
                '''                System uptime information
                ''',
                'uptime',
                'Cisco-IOS-XR-shellutil-oper', False),
            ],
            'Cisco-IOS-XR-shellutil-oper',
            'system-time',
            _yang_ns._namespaces['Cisco-IOS-XR-shellutil-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper'
        ),
    },
}
_meta_table['SystemTime.Clock']['meta_info'].parent =_meta_table['SystemTime']['meta_info']
_meta_table['SystemTime.Uptime']['meta_info'].parent =_meta_table['SystemTime']['meta_info']
