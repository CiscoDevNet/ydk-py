


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'SubscriberManager.Accounting.SendStop' : {
        'meta_info' : _MetaInfoClass('SubscriberManager.Accounting.SendStop',
            False, 
            [
            _MetaInfoClassMember('setup-failure', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set up failure feature
                ''',
                'setup_failure',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'send-stop',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'SubscriberManager.Accounting' : {
        'meta_info' : _MetaInfoClass('SubscriberManager.Accounting',
            False, 
            [
            _MetaInfoClassMember('send-stop', REFERENCE_CLASS, 'SendStop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberManager.Accounting.SendStop', 
                [], [], 
                '''                Accounting send stop feature
                ''',
                'send_stop',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'SubscriberManager' : {
        'meta_info' : _MetaInfoClass('SubscriberManager',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberManager.Accounting', 
                [], [], 
                '''                iEdge accounting feature
                ''',
                'accounting',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'subscriber-manager',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'IedgeLicenseManager.Node' : {
        'meta_info' : _MetaInfoClass('IedgeLicenseManager.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The node id to filter on. For eg., 0/1/CPU0
                ''',
                'node_name',
                'Cisco-IOS-XR-iedge4710-cfg', True),
            _MetaInfoClassMember('session-limit', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Session limit configured on linecard
                ''',
                'session_limit',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            _MetaInfoClassMember('session-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Session threshold configured on linecard
                ''',
                'session_threshold',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'IedgeLicenseManager' : {
        'meta_info' : _MetaInfoClass('IedgeLicenseManager',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'IedgeLicenseManager.Node', 
                [], [], 
                '''                Location. For eg., 0/1/CPU0
                ''',
                'node',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'iedge-license-manager',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
}
_meta_table['SubscriberManager.Accounting.SendStop']['meta_info'].parent =_meta_table['SubscriberManager.Accounting']['meta_info']
_meta_table['SubscriberManager.Accounting']['meta_info'].parent =_meta_table['SubscriberManager']['meta_info']
_meta_table['IedgeLicenseManager.Node']['meta_info'].parent =_meta_table['IedgeLicenseManager']['meta_info']
