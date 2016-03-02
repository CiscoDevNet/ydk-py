


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'TtySessionTimeoutDirection_Enum' : _MetaInfoEnum('TtySessionTimeoutDirection_Enum', 'ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes',
        {
            'in':'IN',
            'in-out':'IN_OUT',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
    'TtyPager_Enum' : _MetaInfoEnum('TtyPager_Enum', 'ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes',
        {
            'more':'MORE',
            'less':'LESS',
            'none':'NONE',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
    'TtyEscapeChar_Enum' : _MetaInfoEnum('TtyEscapeChar_Enum', 'ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes',
        {
            'break':'BREAK',
            'default':'DEFAULT',
            'none':'NONE',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
    'TtyTransportProtocol_Enum' : _MetaInfoEnum('TtyTransportProtocol_Enum', 'ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes',
        {
            'none':'NONE',
            'telnet':'TELNET',
            'ssh':'SSH',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
    'TtyTransportProtocolSelect_Enum' : _MetaInfoEnum('TtyTransportProtocolSelect_Enum', 'ydk.models.tty.Cisco_IOS_XR_tty_management_datatypes',
        {
            'none':'NONE',
            'all':'ALL',
            'some':'SOME',
        }, 'Cisco-IOS-XR-tty-management-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-tty-management-datatypes']),
}
