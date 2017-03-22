


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NetconfYang.Agent.Ssh' : {
        'meta_info' : _MetaInfoClass('NetconfYang.Agent.Ssh',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable NETCONF YANG agent over SSH connection
                ''',
                'enable',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            ],
            'Cisco-IOS-XR-man-netconf-cfg',
            'ssh',
            _yang_ns._namespaces['Cisco-IOS-XR-man-netconf-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg'
        ),
    },
    'NetconfYang.Agent.Session' : {
        'meta_info' : _MetaInfoClass('NetconfYang.Agent.Session',
            False, 
            [
            _MetaInfoClassMember('absolute-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '1440')], [], 
                '''                Absolute timeout in minutes
                ''',
                'absolute_timeout',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            _MetaInfoClassMember('idle-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '1440')], [], 
                '''                Non-active session lifetime
                ''',
                'idle_timeout',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '50')], [], 
                '''                Count of allowable concurrent netconf-yang
                sessions
                ''',
                'limit',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            ],
            'Cisco-IOS-XR-man-netconf-cfg',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-man-netconf-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg'
        ),
    },
    'NetconfYang.Agent' : {
        'meta_info' : _MetaInfoClass('NetconfYang.Agent',
            False, 
            [
            _MetaInfoClassMember('rate-limit', ATTRIBUTE, 'int' , None, None, 
                [('4096', '4294967295')], [], 
                '''                Number of bytes to process per sec
                ''',
                'rate_limit',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg', 'NetconfYang.Agent.Session', 
                [], [], 
                '''                Session settings
                ''',
                'session',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            _MetaInfoClassMember('ssh', REFERENCE_CLASS, 'Ssh' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg', 'NetconfYang.Agent.Ssh', 
                [], [], 
                '''                NETCONF YANG agent over SSH connection
                ''',
                'ssh',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            ],
            'Cisco-IOS-XR-man-netconf-cfg',
            'agent',
            _yang_ns._namespaces['Cisco-IOS-XR-man-netconf-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg'
        ),
    },
    'NetconfYang' : {
        'meta_info' : _MetaInfoClass('NetconfYang',
            False, 
            [
            _MetaInfoClassMember('agent', REFERENCE_CLASS, 'Agent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg', 'NetconfYang.Agent', 
                [], [], 
                '''                NETCONF YANG agent configuration commands
                ''',
                'agent',
                'Cisco-IOS-XR-man-netconf-cfg', False),
            ],
            'Cisco-IOS-XR-man-netconf-cfg',
            'netconf-yang',
            _yang_ns._namespaces['Cisco-IOS-XR-man-netconf-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg'
        ),
    },
}
_meta_table['NetconfYang.Agent.Ssh']['meta_info'].parent =_meta_table['NetconfYang.Agent']['meta_info']
_meta_table['NetconfYang.Agent.Session']['meta_info'].parent =_meta_table['NetconfYang.Agent']['meta_info']
_meta_table['NetconfYang.Agent']['meta_info'].parent =_meta_table['NetconfYang']['meta_info']
