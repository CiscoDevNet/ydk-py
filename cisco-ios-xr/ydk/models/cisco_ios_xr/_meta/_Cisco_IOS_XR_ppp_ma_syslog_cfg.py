


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ppp.Syslog' : {
        'meta_info' : _MetaInfoClass('Ppp.Syslog',
            False, 
            [
            _MetaInfoClassMember('enable-session-status', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable syslog for ppp session status
                ''',
                'enable_session_status',
                'Cisco-IOS-XR-ppp-ma-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-syslog-cfg',
            'syslog',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_syslog_cfg'
        ),
    },
    'Ppp' : {
        'meta_info' : _MetaInfoClass('Ppp',
            False, 
            [
            _MetaInfoClassMember('syslog', REFERENCE_CLASS, 'Syslog' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_syslog_cfg', 'Ppp.Syslog', 
                [], [], 
                '''                syslog option for session status
                ''',
                'syslog',
                'Cisco-IOS-XR-ppp-ma-syslog-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-syslog-cfg',
            'ppp',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-syslog-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_syslog_cfg'
        ),
    },
}
_meta_table['Ppp.Syslog']['meta_info'].parent =_meta_table['Ppp']['meta_info']
