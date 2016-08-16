


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'TtySessionTimeoutDirectionEnum' : _MetaInfoEnum('TtySessionTimeoutDirectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes',
        {
            'in':'IN',
            'in-out':'IN_OUT',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
    'TtyPagerEnum' : _MetaInfoEnum('TtyPagerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes',
        {
            'more':'MORE',
            'less':'LESS',
            'none':'NONE',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
    'TtyEscapeCharEnum' : _MetaInfoEnum('TtyEscapeCharEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes',
        {
            'break':'BREAK',
            'default':'DEFAULT',
            'none':'NONE',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
    'TtyTransportProtocolEnum' : _MetaInfoEnum('TtyTransportProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes',
        {
            'none':'NONE',
            'telnet':'TELNET',
            'ssh':'SSH',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
    'TtyTransportProtocolSelectEnum' : _MetaInfoEnum('TtyTransportProtocolSelectEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes',
        {
            'none':'NONE',
            'all':'ALL',
            'some':'SOME',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
}
