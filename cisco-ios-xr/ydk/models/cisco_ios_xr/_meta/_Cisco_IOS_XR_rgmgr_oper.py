


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'RedundancyGroupManager.Controllers.Controller' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Controllers.Controller',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Controller name
                ''',
                'controller_name',
                'Cisco-IOS-XR-rgmgr-oper', True),
            _MetaInfoClassMember('backup-interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Backup interface handle
                ''',
                'backup_interface_handle',
                'Cisco-IOS-XR-rgmgr-oper', False),
            _MetaInfoClassMember('backup-interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Backup interface name
                ''',
                'backup_interface_name',
                'Cisco-IOS-XR-rgmgr-oper', False),
            _MetaInfoClassMember('backup-interface-next-hop-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Backup interface next hop IP address
                ''',
                'backup_interface_next_hop_ip_address',
                'Cisco-IOS-XR-rgmgr-oper', False),
            _MetaInfoClassMember('controller-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Handle of controller being backed up
                ''',
                'controller_handle',
                'Cisco-IOS-XR-rgmgr-oper', False),
            _MetaInfoClassMember('controller-name-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Name of controller being backed up
                ''',
                'controller_name_xr',
                'Cisco-IOS-XR-rgmgr-oper', False),
            _MetaInfoClassMember('inter-chassis-group-state', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Configured interchassis redundancy group state
                ''',
                'inter_chassis_group_state',
                'Cisco-IOS-XR-rgmgr-oper', False),
            _MetaInfoClassMember('multi-router-aps-group-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Configured interchassis redundancy group number
                ''',
                'multi_router_aps_group_number',
                'Cisco-IOS-XR-rgmgr-oper', False),
            ],
            'Cisco-IOS-XR-rgmgr-oper',
            'controller',
            _yang_ns._namespaces['Cisco-IOS-XR-rgmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper'
        ),
    },
    'RedundancyGroupManager.Controllers' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager.Controllers',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper', 'RedundancyGroupManager.Controllers.Controller', 
                [], [], 
                '''                Display redundancy group by controller name
                ''',
                'controller',
                'Cisco-IOS-XR-rgmgr-oper', False),
            ],
            'Cisco-IOS-XR-rgmgr-oper',
            'controllers',
            _yang_ns._namespaces['Cisco-IOS-XR-rgmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper'
        ),
    },
    'RedundancyGroupManager' : {
        'meta_info' : _MetaInfoClass('RedundancyGroupManager',
            False, 
            [
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper', 'RedundancyGroupManager.Controllers', 
                [], [], 
                '''                Redundancy group manager data
                ''',
                'controllers',
                'Cisco-IOS-XR-rgmgr-oper', False),
            ],
            'Cisco-IOS-XR-rgmgr-oper',
            'redundancy-group-manager',
            _yang_ns._namespaces['Cisco-IOS-XR-rgmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper'
        ),
    },
}
_meta_table['RedundancyGroupManager.Controllers.Controller']['meta_info'].parent =_meta_table['RedundancyGroupManager.Controllers']['meta_info']
_meta_table['RedundancyGroupManager.Controllers']['meta_info'].parent =_meta_table['RedundancyGroupManager']['meta_info']
