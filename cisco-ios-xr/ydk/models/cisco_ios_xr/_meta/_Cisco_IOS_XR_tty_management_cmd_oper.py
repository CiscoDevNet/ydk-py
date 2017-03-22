


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ShowUsers.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('ShowUsers.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Session Id
                ''',
                'session_id',
                'Cisco-IOS-XR-tty-management-cmd-oper', True),
            _MetaInfoClassMember('conns', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                No. of Connections
                ''',
                'conns',
                'Cisco-IOS-XR-tty-management-cmd-oper', False),
            _MetaInfoClassMember('idle-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Idle Time
                ''',
                'idle_string',
                'Cisco-IOS-XR-tty-management-cmd-oper', False),
            _MetaInfoClassMember('line', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Line Number
                ''',
                'line',
                'Cisco-IOS-XR-tty-management-cmd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                location
                ''',
                'location',
                'Cisco-IOS-XR-tty-management-cmd-oper', False),
            _MetaInfoClassMember('service', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service Name
                ''',
                'service',
                'Cisco-IOS-XR-tty-management-cmd-oper', False),
            _MetaInfoClassMember('user', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                User Name
                ''',
                'user',
                'Cisco-IOS-XR-tty-management-cmd-oper', False),
            ],
            'Cisco-IOS-XR-tty-management-cmd-oper',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-cmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper'
        ),
    },
    'ShowUsers.Sessions' : {
        'meta_info' : _MetaInfoClass('ShowUsers.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper', 'ShowUsers.Sessions.Session', 
                [], [], 
                '''                Show users statistics
                ''',
                'session',
                'Cisco-IOS-XR-tty-management-cmd-oper', False),
            ],
            'Cisco-IOS-XR-tty-management-cmd-oper',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-cmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper'
        ),
    },
    'ShowUsers' : {
        'meta_info' : _MetaInfoClass('ShowUsers',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper', 'ShowUsers.Sessions', 
                [], [], 
                '''                Show users statistics
                ''',
                'sessions',
                'Cisco-IOS-XR-tty-management-cmd-oper', False),
            ],
            'Cisco-IOS-XR-tty-management-cmd-oper',
            'show-users',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-cmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper'
        ),
    },
}
_meta_table['ShowUsers.Sessions.Session']['meta_info'].parent =_meta_table['ShowUsers.Sessions']['meta_info']
_meta_table['ShowUsers.Sessions']['meta_info'].parent =_meta_table['ShowUsers']['meta_info']
