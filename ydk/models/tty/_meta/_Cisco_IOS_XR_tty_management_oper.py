


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'TransportServiceEnum' : _MetaInfoEnum('TransportServiceEnum', 'ydk.models.tty.Cisco_IOS_XR_tty_management_oper',
        {
            'unknown':'UNKNOWN',
            'telnet':'TELNET',
            'rlogin':'RLOGIN',
            'ssh':'SSH',
        }, 'Cisco-IOS-XR-tty-management-oper', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-oper']),
    'HostAfIdBase_Identity' : {
        'meta_info' : _MetaInfoClass('HostAfIdBase_Identity',
            False, 
            [
            ],
            'Cisco-IOS-XR-tty-management-oper',
            'Host-af-id-base',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-oper'],
        'ydk.models.tty.Cisco_IOS_XR_tty_management_oper'
        ),
    },
    'Ipv6_Identity' : {
        'meta_info' : _MetaInfoClass('Ipv6_Identity',
            False, 
            [
            ],
            'Cisco-IOS-XR-tty-management-oper',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-oper'],
        'ydk.models.tty.Cisco_IOS_XR_tty_management_oper'
        ),
    },
    'Ipv4_Identity' : {
        'meta_info' : _MetaInfoClass('Ipv4_Identity',
            False, 
            [
            ],
            'Cisco-IOS-XR-tty-management-oper',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-oper'],
        'ydk.models.tty.Cisco_IOS_XR_tty_management_oper'
        ),
    },
}
