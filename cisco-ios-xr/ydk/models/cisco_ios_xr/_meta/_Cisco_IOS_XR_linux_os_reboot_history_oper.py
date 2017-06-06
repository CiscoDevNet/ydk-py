


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'RebootHistory.Node.RebootHistory_' : {
        'meta_info' : _MetaInfoClass('RebootHistory.Node.RebootHistory_',
            False, 
            [
            _MetaInfoClassMember('cause-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cause code for reboot
                ''',
                'cause_code',
                'Cisco-IOS-XR-linux-os-reboot-history-oper', False),
            _MetaInfoClassMember('no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number count
                ''',
                'no',
                'Cisco-IOS-XR-linux-os-reboot-history-oper', False),
            _MetaInfoClassMember('reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reason for reboot
                ''',
                'reason',
                'Cisco-IOS-XR-linux-os-reboot-history-oper', False),
            _MetaInfoClassMember('time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Time of reboot
                ''',
                'time',
                'Cisco-IOS-XR-linux-os-reboot-history-oper', False),
            ],
            'Cisco-IOS-XR-linux-os-reboot-history-oper',
            'reboot-history',
            _yang_ns._namespaces['Cisco-IOS-XR-linux-os-reboot-history-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper'
        ),
    },
    'RebootHistory.Node' : {
        'meta_info' : _MetaInfoClass('RebootHistory.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-linux-os-reboot-history-oper', True),
            _MetaInfoClassMember('reboot-history', REFERENCE_LIST, 'RebootHistory_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper', 'RebootHistory.Node.RebootHistory_', 
                [], [], 
                '''                Last Reboots
                ''',
                'reboot_history',
                'Cisco-IOS-XR-linux-os-reboot-history-oper', False),
            ],
            'Cisco-IOS-XR-linux-os-reboot-history-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-linux-os-reboot-history-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper'
        ),
    },
    'RebootHistory' : {
        'meta_info' : _MetaInfoClass('RebootHistory',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper', 'RebootHistory.Node', 
                [], [], 
                '''                Node ID
                ''',
                'node',
                'Cisco-IOS-XR-linux-os-reboot-history-oper', False),
            ],
            'Cisco-IOS-XR-linux-os-reboot-history-oper',
            'reboot-history',
            _yang_ns._namespaces['Cisco-IOS-XR-linux-os-reboot-history-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper'
        ),
    },
}
_meta_table['RebootHistory.Node.RebootHistory_']['meta_info'].parent =_meta_table['RebootHistory.Node']['meta_info']
_meta_table['RebootHistory.Node']['meta_info'].parent =_meta_table['RebootHistory']['meta_info']
