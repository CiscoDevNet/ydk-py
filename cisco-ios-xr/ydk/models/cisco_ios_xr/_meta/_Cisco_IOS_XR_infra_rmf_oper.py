


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Redundancy.Nodes.Node.Redundancy_.Groupinfo' : {
        'meta_info' : _MetaInfoClass('Redundancy.Nodes.Node.Redundancy_.Groupinfo',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Active
                ''',
                'active',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('ha-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                HAState
                ''',
                'ha_state',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('nsr-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NSRState
                ''',
                'nsr_state',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('standby', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Standby
                ''',
                'standby',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            ],
            'Cisco-IOS-XR-infra-rmf-oper',
            'groupinfo',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rmf-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper'
        ),
    },
    'Redundancy.Nodes.Node.Redundancy_' : {
        'meta_info' : _MetaInfoClass('Redundancy.Nodes.Node.Redundancy_',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Active node name R/S/I
                ''',
                'active',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('groupinfo', REFERENCE_LIST, 'Groupinfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper', 'Redundancy.Nodes.Node.Redundancy_.Groupinfo', 
                [], [], 
                '''                groupinfo
                ''',
                'groupinfo',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('ha-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                High Availability state Ready/Not Ready
                ''',
                'ha_state',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('nsr-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NSR state Configured/Not Configured
                ''',
                'nsr_state',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('standby', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Standby node name R/S/I
                ''',
                'standby',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            ],
            'Cisco-IOS-XR-infra-rmf-oper',
            'redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rmf-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper'
        ),
    },
    'Redundancy.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Redundancy.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node Location
                ''',
                'node_id',
                'Cisco-IOS-XR-infra-rmf-oper', True),
            _MetaInfoClassMember('active-reboot-reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Active node reload
                ''',
                'active_reboot_reason',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('err-log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error Log
                ''',
                'err_log',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reload and boot logs
                ''',
                'log',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('redundancy', REFERENCE_CLASS, 'Redundancy_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper', 'Redundancy.Nodes.Node.Redundancy_', 
                [], [], 
                '''                Row information
                ''',
                'redundancy',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('standby-reboot-reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Standby node reload
                ''',
                'standby_reboot_reason',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            ],
            'Cisco-IOS-XR-infra-rmf-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rmf-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper'
        ),
    },
    'Redundancy.Nodes' : {
        'meta_info' : _MetaInfoClass('Redundancy.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper', 'Redundancy.Nodes.Node', 
                [], [], 
                '''                Redundancy Node Information
                ''',
                'node',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            ],
            'Cisco-IOS-XR-infra-rmf-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rmf-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper'
        ),
    },
    'Redundancy.Summary.RedPair.Groupinfo' : {
        'meta_info' : _MetaInfoClass('Redundancy.Summary.RedPair.Groupinfo',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Active
                ''',
                'active',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('ha-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                HAState
                ''',
                'ha_state',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('nsr-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NSRState
                ''',
                'nsr_state',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('standby', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Standby
                ''',
                'standby',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            ],
            'Cisco-IOS-XR-infra-rmf-oper',
            'groupinfo',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rmf-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper'
        ),
    },
    'Redundancy.Summary.RedPair' : {
        'meta_info' : _MetaInfoClass('Redundancy.Summary.RedPair',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Active node name R/S/I
                ''',
                'active',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('groupinfo', REFERENCE_LIST, 'Groupinfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper', 'Redundancy.Summary.RedPair.Groupinfo', 
                [], [], 
                '''                groupinfo
                ''',
                'groupinfo',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('ha-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                High Availability state Ready/Not Ready
                ''',
                'ha_state',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('nsr-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NSR state Configured/Not Configured
                ''',
                'nsr_state',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('standby', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Standby node name R/S/I
                ''',
                'standby',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            ],
            'Cisco-IOS-XR-infra-rmf-oper',
            'red-pair',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rmf-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper'
        ),
    },
    'Redundancy.Summary' : {
        'meta_info' : _MetaInfoClass('Redundancy.Summary',
            False, 
            [
            _MetaInfoClassMember('err-log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error Log
                ''',
                'err_log',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('red-pair', REFERENCE_LIST, 'RedPair' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper', 'Redundancy.Summary.RedPair', 
                [], [], 
                '''                Redundancy Pair
                ''',
                'red_pair',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            ],
            'Cisco-IOS-XR-infra-rmf-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rmf-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper'
        ),
    },
    'Redundancy' : {
        'meta_info' : _MetaInfoClass('Redundancy',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper', 'Redundancy.Nodes', 
                [], [], 
                '''                Location show information
                ''',
                'nodes',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper', 'Redundancy.Summary', 
                [], [], 
                '''                Redundancy Summary of Nodes
                ''',
                'summary',
                'Cisco-IOS-XR-infra-rmf-oper', False),
            ],
            'Cisco-IOS-XR-infra-rmf-oper',
            'redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rmf-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper'
        ),
    },
}
_meta_table['Redundancy.Nodes.Node.Redundancy_.Groupinfo']['meta_info'].parent =_meta_table['Redundancy.Nodes.Node.Redundancy_']['meta_info']
_meta_table['Redundancy.Nodes.Node.Redundancy_']['meta_info'].parent =_meta_table['Redundancy.Nodes.Node']['meta_info']
_meta_table['Redundancy.Nodes.Node']['meta_info'].parent =_meta_table['Redundancy.Nodes']['meta_info']
_meta_table['Redundancy.Summary.RedPair.Groupinfo']['meta_info'].parent =_meta_table['Redundancy.Summary.RedPair']['meta_info']
_meta_table['Redundancy.Summary.RedPair']['meta_info'].parent =_meta_table['Redundancy.Summary']['meta_info']
_meta_table['Redundancy.Nodes']['meta_info'].parent =_meta_table['Redundancy']['meta_info']
_meta_table['Redundancy.Summary']['meta_info'].parent =_meta_table['Redundancy']['meta_info']
