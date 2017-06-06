


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'TtyPagerEnum' : _MetaInfoEnum('TtyPagerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes',
        {
            'more':'more',
            'less':'less',
            'none':'none',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
    'TtyEscapeCharEnum' : _MetaInfoEnum('TtyEscapeCharEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes',
        {
            'break':'break_',
            'default':'default',
            'none':'none',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
    'TtyTransportProtocolSelectEnum' : _MetaInfoEnum('TtyTransportProtocolSelectEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes',
        {
            'none':'none',
            'all':'all',
            'some':'some',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
    'TtyTransportProtocolEnum' : _MetaInfoEnum('TtyTransportProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes',
        {
            'none':'none',
            'telnet':'telnet',
            'ssh':'ssh',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
    'TtySessionTimeoutDirectionEnum' : _MetaInfoEnum('TtySessionTimeoutDirectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes',
        {
            'in':'in_',
            'in-out':'in_out',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
}
