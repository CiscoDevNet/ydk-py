


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AaaActionEnum' : _MetaInfoEnum('AaaActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg',
        {
            'accept':'accept',
            'reject':'reject',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
    'AaaConfigEnum' : _MetaInfoEnum('AaaConfigEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
    'AaaDscpValueEnum' : _MetaInfoEnum('AaaDscpValueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg',
        {
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
            'default':'default',
            'ef':'ef',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
    'AaaSelectKeyEnum' : _MetaInfoEnum('AaaSelectKeyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg',
        {
            'server-key':'server_key',
            'session-key':'session_key',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
    'AaaAuthenticationEnum' : _MetaInfoEnum('AaaAuthenticationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg',
        {
            'all':'all',
            'any':'any',
            'session-key':'session_key',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
    'AaaDirectionEnum' : _MetaInfoEnum('AaaDirectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg',
        {
            'inbound':'inbound',
            'outbound':'outbound',
        }, 'Cisco-IOS-XR-aaa-protocol-radius-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg']),
}
