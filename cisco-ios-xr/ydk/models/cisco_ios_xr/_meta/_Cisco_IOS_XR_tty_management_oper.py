


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'TransportServiceEnum' : _MetaInfoEnum('TransportServiceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper',
        {
            'unknown':'unknown',
            'telnet':'telnet',
            'rlogin':'rlogin',
            'ssh':'ssh',
        }, 'Cisco-IOS-XR-tty-management-oper', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-oper']),
    'HostAfIdBaseIdentity' : {
        'meta_info' : _MetaInfoClass('HostAfIdBaseIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XR-tty-management-oper',
            'Host-af-id-base',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper'
        ),
    },
    'Ipv4Identity' : {
        'meta_info' : _MetaInfoClass('Ipv4Identity',
            False, 
            [
            ],
            'Cisco-IOS-XR-tty-management-oper',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper'
        ),
    },
    'Ipv6Identity' : {
        'meta_info' : _MetaInfoClass('Ipv6Identity',
            False, 
            [
            ],
            'Cisco-IOS-XR-tty-management-oper',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper'
        ),
    },
}
