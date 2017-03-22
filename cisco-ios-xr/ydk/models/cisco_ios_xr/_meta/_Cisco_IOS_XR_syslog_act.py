


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'LogmsgRpc.Input' : {
        'meta_info' : _MetaInfoClass('LogmsgRpc.Input',
            False, 
            [
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'SeverityEnum' , 'ydk.models.ietf.ietf_syslog_types', 'SeverityEnum', 
                [], [], 
                '''                Set serverity level
                ''',
                'severity',
                'Cisco-IOS-XR-syslog-act', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Message body.
                ''',
                'message',
                'Cisco-IOS-XR-syslog-act', False),
            ],
            'Cisco-IOS-XR-syslog-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-syslog-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_syslog_act'
        ),
    },
    'LogmsgRpc' : {
        'meta_info' : _MetaInfoClass('LogmsgRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_syslog_act', 'LogmsgRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-syslog-act', False),
            ],
            'Cisco-IOS-XR-syslog-act',
            'logmsg',
            _yang_ns._namespaces['Cisco-IOS-XR-syslog-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_syslog_act'
        ),
    },
}
_meta_table['LogmsgRpc.Input']['meta_info'].parent =_meta_table['LogmsgRpc']['meta_info']
