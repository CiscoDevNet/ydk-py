


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Clock.TimeZone' : {
        'meta_info' : _MetaInfoClass('Clock.TimeZone',
            False, 
            [
            _MetaInfoClassMember('area-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Area File in zoneinfo package
                ''',
                'area_name',
                'Cisco-IOS-XR-infra-infra-clock-linux-cfg', False),
            _MetaInfoClassMember('time-zone-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of time zone
                ''',
                'time_zone_name',
                'Cisco-IOS-XR-infra-infra-clock-linux-cfg', False),
            ],
            'Cisco-IOS-XR-infra-infra-clock-linux-cfg',
            'time-zone',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-infra-clock-linux-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_linux_cfg'
        ),
    },
    'Clock' : {
        'meta_info' : _MetaInfoClass('Clock',
            False, 
            [
            _MetaInfoClassMember('time-zone', REFERENCE_CLASS, 'TimeZone' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_linux_cfg', 'Clock.TimeZone', 
                [], [], 
                '''                Configure time zone
                ''',
                'time_zone',
                'Cisco-IOS-XR-infra-infra-clock-linux-cfg', False),
            ],
            'Cisco-IOS-XR-infra-infra-clock-linux-cfg',
            'clock',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-infra-clock-linux-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_linux_cfg'
        ),
    },
}
_meta_table['Clock.TimeZone']['meta_info'].parent =_meta_table['Clock']['meta_info']
