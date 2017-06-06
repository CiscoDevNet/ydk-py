


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PriorityEnum' : _MetaInfoEnum('PriorityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper',
        {
            'critical':'critical',
            'high':'high',
            'medium':'medium',
            'low':'low',
            'very-low':'very_low',
        }, 'Cisco-IOS-XR-infra-rsi-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper']),
    'SourceEnum' : _MetaInfoEnum('SourceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper',
        {
            'configured':'configured',
            'from-group':'from_group',
            'inherited':'inherited',
            'from-optical':'from_optical',
            'configured-and-notified':'configured_and_notified',
            'from-group-and-notified':'from_group_and_notified',
            'inherited-and-notified':'inherited_and_notified',
            'from-optical-and-notified':'from_optical_and_notified',
        }, 'Cisco-IOS-XR-infra-rsi-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper']),
    'VrfGroup.Nodes.Node.Groups.Group.Vrf' : {
        'meta_info' : _MetaInfoClass('VrfGroup.Nodes.Node.Groups.Group.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'VrfGroup.Nodes.Node.Groups.Group' : {
        'meta_info' : _MetaInfoClass('VrfGroup.Nodes.Node.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Group name
                ''',
                'group_name',
                'Cisco-IOS-XR-infra-rsi-oper', True),
            _MetaInfoClassMember('forward-reference', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VRF group not present but used
                ''',
                'forward_reference',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('vr-fs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of VRFs in this VRF group
                ''',
                'vr_fs',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'VrfGroup.Nodes.Node.Groups.Group.Vrf', 
                [], [], 
                '''                VRF group's VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'VrfGroup.Nodes.Node.Groups' : {
        'meta_info' : _MetaInfoClass('VrfGroup.Nodes.Node.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'VrfGroup.Nodes.Node.Groups.Group', 
                [], [], 
                '''                Group details
                ''',
                'group',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'VrfGroup.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('VrfGroup.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rsi-oper', True),
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'VrfGroup.Nodes.Node.Groups', 
                [], [], 
                '''                Group operational data
                ''',
                'groups',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'VrfGroup.Nodes' : {
        'meta_info' : _MetaInfoClass('VrfGroup.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'VrfGroup.Nodes.Node', 
                [], [], 
                '''                Node details
                ''',
                'node',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'VrfGroup' : {
        'meta_info' : _MetaInfoClass('VrfGroup',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'VrfGroup.Nodes', 
                [], [], 
                '''                Node operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'vrf-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.SrlgMaps.SrlgMap' : {
        'meta_info' : _MetaInfoClass('Srlg.SrlgMaps.SrlgMap',
            False, 
            [
            _MetaInfoClassMember('srlg-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                SRLG name
                ''',
                'srlg_name',
                'Cisco-IOS-XR-infra-rsi-oper', True),
            _MetaInfoClassMember('srlg-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SRLG name
                ''',
                'srlg_name_xr',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG value
                ''',
                'srlg_value',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'srlg-map',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.SrlgMaps' : {
        'meta_info' : _MetaInfoClass('Srlg.SrlgMaps',
            False, 
            [
            _MetaInfoClassMember('srlg-map', REFERENCE_LIST, 'SrlgMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.SrlgMaps.SrlgMap', 
                [], [], 
                '''                Configured SRLG name details 
                ''',
                'srlg_map',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'srlg-maps',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.SrlgMaps.SrlgMap' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.SrlgMaps.SrlgMap',
            False, 
            [
            _MetaInfoClassMember('srlg-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                SRLG name
                ''',
                'srlg_name',
                'Cisco-IOS-XR-infra-rsi-oper', True),
            _MetaInfoClassMember('srlg-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SRLG name
                ''',
                'srlg_name_xr',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG value
                ''',
                'srlg_value',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'srlg-map',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.SrlgMaps' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.SrlgMaps',
            False, 
            [
            _MetaInfoClassMember('srlg-map', REFERENCE_LIST, 'SrlgMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.SrlgMaps.SrlgMap', 
                [], [], 
                '''                Configured SRLG name details 
                ''',
                'srlg_map',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'srlg-maps',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.Groups.Group.SrlgAttribute' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.Groups.Group.SrlgAttribute',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'PriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'PriorityEnum', 
                [], [], 
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Index
                ''',
                'srlg_index',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG value
                ''',
                'srlg_value',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'srlg-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Group name
                ''',
                'group_name',
                'Cisco-IOS-XR-infra-rsi-oper', True),
            _MetaInfoClassMember('group-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Group name
                ''',
                'group_name_xr',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('group-values', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group values
                ''',
                'group_values',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-attribute', REFERENCE_LIST, 'SrlgAttribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.Groups.Group.SrlgAttribute', 
                [], [], 
                '''                SRLG attribute
                ''',
                'srlg_attribute',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.Groups' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.Groups.Group', 
                [], [], 
                '''                SRLG group details
                ''',
                'group',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'PriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'PriorityEnum', 
                [], [], 
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Index
                ''',
                'srlg_index',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG value
                ''',
                'srlg_value',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'srlg-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.InheritNodes.InheritNode' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.InheritNodes.InheritNode',
            False, 
            [
            _MetaInfoClassMember('inherit-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'((([a-zA-Z0-9_]*\\d+)|(\\*))/){2}(([a-zA-Z0-9_]*\\d+)|(\\*))'], 
                '''                Inherit node
                ''',
                'inherit_node_name',
                'Cisco-IOS-XR-infra-rsi-oper', True),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('node-values', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Node values
                ''',
                'node_values',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-attribute', REFERENCE_LIST, 'SrlgAttribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute', 
                [], [], 
                '''                SRLG attribute
                ''',
                'srlg_attribute',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'inherit-node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.InheritNodes' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.InheritNodes',
            False, 
            [
            _MetaInfoClassMember('inherit-node', REFERENCE_LIST, 'InheritNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.InheritNodes.InheritNode', 
                [], [], 
                '''                SRLG inherit location details
                ''',
                'inherit_node',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'inherit-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rsi-oper', True),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('registrations', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Registrations
                ''',
                'registrations',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-value', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG values
                ''',
                'srlg_value',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('value-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Values
                ''',
                'value_count',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                SRLG interface summary
                ''',
                'interface',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'PriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'PriorityEnum', 
                [], [], 
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('source', REFERENCE_ENUM_CLASS, 'SourceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'SourceEnum', 
                [], [], 
                '''                Source
                ''',
                'source',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('source-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source name
                ''',
                'source_name',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Index
                ''',
                'srlg_index',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG value
                ''',
                'srlg_value',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'srlg-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rsi-oper', True),
            _MetaInfoClassMember('groups', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Groups
                ''',
                'groups',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('nodes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-attribute', REFERENCE_LIST, 'SrlgAttribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute', 
                [], [], 
                '''                SRLG attributes
                ''',
                'srlg_attribute',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'interface-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.InterfaceDetails' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.InterfaceDetails',
            False, 
            [
            _MetaInfoClassMember('interface-detail', REFERENCE_LIST, 'InterfaceDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail', 
                [], [], 
                '''                SRLG interface details
                ''',
                'interface_detail',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'interface-details',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.SrlgValues.SrlgValue' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.SrlgValues.SrlgValue',
            False, 
            [
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                SRLG value
                ''',
                'value',
                'Cisco-IOS-XR-infra-rsi-oper', True),
            _MetaInfoClassMember('interface-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'srlg-value',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.SrlgValues' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.SrlgValues',
            False, 
            [
            _MetaInfoClassMember('srlg-value', REFERENCE_LIST, 'SrlgValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.SrlgValues.SrlgValue', 
                [], [], 
                '''                Configured SRLG value details 
                ''',
                'srlg_value',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'srlg-values',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName',
            False, 
            [
            _MetaInfoClassMember('srlg-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                SRLG name
                ''',
                'srlg_name',
                'Cisco-IOS-XR-infra-rsi-oper', True),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces', 
                [], [], 
                '''                Interfaces information
                ''',
                'interfaces',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SRLG name
                ''',
                'srlg_name_xr',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG value
                ''',
                'srlg_value',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'interface-srlg-name',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node.InterfaceSrlgNames' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node.InterfaceSrlgNames',
            False, 
            [
            _MetaInfoClassMember('interface-srlg-name', REFERENCE_LIST, 'InterfaceSrlgName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName', 
                [], [], 
                '''                Configured SRLG name details 
                ''',
                'interface_srlg_name',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'interface-srlg-names',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rsi-oper', True),
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.Groups', 
                [], [], 
                '''                Set of Groups configured for SRLG
                ''',
                'groups',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('inherit-nodes', REFERENCE_CLASS, 'InheritNodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.InheritNodes', 
                [], [], 
                '''                Set of inherit locations configured for SRLG
                ''',
                'inherit_nodes',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('interface-details', REFERENCE_CLASS, 'InterfaceDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.InterfaceDetails', 
                [], [], 
                '''                Set of interfaces configured for SRLG
                ''',
                'interface_details',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('interface-srlg-names', REFERENCE_CLASS, 'InterfaceSrlgNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.InterfaceSrlgNames', 
                [], [], 
                '''                Set of SRLG names configured
                ''',
                'interface_srlg_names',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.Interfaces', 
                [], [], 
                '''                Set of interfaces configured for SRLG
                ''',
                'interfaces',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-maps', REFERENCE_CLASS, 'SrlgMaps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.SrlgMaps', 
                [], [], 
                '''                Set of SRLG name, value maps configured
                ''',
                'srlg_maps',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-values', REFERENCE_CLASS, 'SrlgValues' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node.SrlgValues', 
                [], [], 
                '''                Set of SRLG values configured
                ''',
                'srlg_values',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.Nodes' : {
        'meta_info' : _MetaInfoClass('Srlg.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes.Node', 
                [], [], 
                '''                RSI SRLG operational data
                ''',
                'node',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces' : {
        'meta_info' : _MetaInfoClass('Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.InterfaceSrlgNames.InterfaceSrlgName' : {
        'meta_info' : _MetaInfoClass('Srlg.InterfaceSrlgNames.InterfaceSrlgName',
            False, 
            [
            _MetaInfoClassMember('srlg-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                SRLG name
                ''',
                'srlg_name',
                'Cisco-IOS-XR-infra-rsi-oper', True),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces', 
                [], [], 
                '''                Interfaces information
                ''',
                'interfaces',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SRLG name
                ''',
                'srlg_name_xr',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG value
                ''',
                'srlg_value',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'interface-srlg-name',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg.InterfaceSrlgNames' : {
        'meta_info' : _MetaInfoClass('Srlg.InterfaceSrlgNames',
            False, 
            [
            _MetaInfoClassMember('interface-srlg-name', REFERENCE_LIST, 'InterfaceSrlgName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.InterfaceSrlgNames.InterfaceSrlgName', 
                [], [], 
                '''                Configured SRLG name details 
                ''',
                'interface_srlg_name',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'interface-srlg-names',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'Srlg' : {
        'meta_info' : _MetaInfoClass('Srlg',
            False, 
            [
            _MetaInfoClassMember('interface-srlg-names', REFERENCE_CLASS, 'InterfaceSrlgNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.InterfaceSrlgNames', 
                [], [], 
                '''                Set of SRLG names configured
                ''',
                'interface_srlg_names',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.Nodes', 
                [], [], 
                '''                RSI SRLG operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('srlg-maps', REFERENCE_CLASS, 'SrlgMaps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Srlg.SrlgMaps', 
                [], [], 
                '''                Set of SRLG name, value maps configured
                ''',
                'srlg_maps',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'srlg',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'SelectiveVrfDownload.State' : {
        'meta_info' : _MetaInfoClass('SelectiveVrfDownload.State',
            False, 
            [
            _MetaInfoClassMember('is-svd-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is SVD Enabled Operational
                ''',
                'is_svd_enabled',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            _MetaInfoClassMember('is-svd-enabled-cfg', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is SVD Enabled Config
                ''',
                'is_svd_enabled_cfg',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'state',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
    'SelectiveVrfDownload' : {
        'meta_info' : _MetaInfoClass('SelectiveVrfDownload',
            False, 
            [
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'SelectiveVrfDownload.State', 
                [], [], 
                '''                Selective VRF Download feature state details
                ''',
                'state',
                'Cisco-IOS-XR-infra-rsi-oper', False),
            ],
            'Cisco-IOS-XR-infra-rsi-oper',
            'selective-vrf-download',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper'
        ),
    },
}
_meta_table['VrfGroup.Nodes.Node.Groups.Group.Vrf']['meta_info'].parent =_meta_table['VrfGroup.Nodes.Node.Groups.Group']['meta_info']
_meta_table['VrfGroup.Nodes.Node.Groups.Group']['meta_info'].parent =_meta_table['VrfGroup.Nodes.Node.Groups']['meta_info']
_meta_table['VrfGroup.Nodes.Node.Groups']['meta_info'].parent =_meta_table['VrfGroup.Nodes.Node']['meta_info']
_meta_table['VrfGroup.Nodes.Node']['meta_info'].parent =_meta_table['VrfGroup.Nodes']['meta_info']
_meta_table['VrfGroup.Nodes']['meta_info'].parent =_meta_table['VrfGroup']['meta_info']
_meta_table['Srlg.SrlgMaps.SrlgMap']['meta_info'].parent =_meta_table['Srlg.SrlgMaps']['meta_info']
_meta_table['Srlg.Nodes.Node.SrlgMaps.SrlgMap']['meta_info'].parent =_meta_table['Srlg.Nodes.Node.SrlgMaps']['meta_info']
_meta_table['Srlg.Nodes.Node.Groups.Group.SrlgAttribute']['meta_info'].parent =_meta_table['Srlg.Nodes.Node.Groups.Group']['meta_info']
_meta_table['Srlg.Nodes.Node.Groups.Group']['meta_info'].parent =_meta_table['Srlg.Nodes.Node.Groups']['meta_info']
_meta_table['Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute']['meta_info'].parent =_meta_table['Srlg.Nodes.Node.InheritNodes.InheritNode']['meta_info']
_meta_table['Srlg.Nodes.Node.InheritNodes.InheritNode']['meta_info'].parent =_meta_table['Srlg.Nodes.Node.InheritNodes']['meta_info']
_meta_table['Srlg.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['Srlg.Nodes.Node.Interfaces']['meta_info']
_meta_table['Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute']['meta_info'].parent =_meta_table['Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail']['meta_info']
_meta_table['Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail']['meta_info'].parent =_meta_table['Srlg.Nodes.Node.InterfaceDetails']['meta_info']
_meta_table['Srlg.Nodes.Node.SrlgValues.SrlgValue']['meta_info'].parent =_meta_table['Srlg.Nodes.Node.SrlgValues']['meta_info']
_meta_table['Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces']['meta_info'].parent =_meta_table['Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName']['meta_info']
_meta_table['Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName']['meta_info'].parent =_meta_table['Srlg.Nodes.Node.InterfaceSrlgNames']['meta_info']
_meta_table['Srlg.Nodes.Node.SrlgMaps']['meta_info'].parent =_meta_table['Srlg.Nodes.Node']['meta_info']
_meta_table['Srlg.Nodes.Node.Groups']['meta_info'].parent =_meta_table['Srlg.Nodes.Node']['meta_info']
_meta_table['Srlg.Nodes.Node.InheritNodes']['meta_info'].parent =_meta_table['Srlg.Nodes.Node']['meta_info']
_meta_table['Srlg.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['Srlg.Nodes.Node']['meta_info']
_meta_table['Srlg.Nodes.Node.InterfaceDetails']['meta_info'].parent =_meta_table['Srlg.Nodes.Node']['meta_info']
_meta_table['Srlg.Nodes.Node.SrlgValues']['meta_info'].parent =_meta_table['Srlg.Nodes.Node']['meta_info']
_meta_table['Srlg.Nodes.Node.InterfaceSrlgNames']['meta_info'].parent =_meta_table['Srlg.Nodes.Node']['meta_info']
_meta_table['Srlg.Nodes.Node']['meta_info'].parent =_meta_table['Srlg.Nodes']['meta_info']
_meta_table['Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces']['meta_info'].parent =_meta_table['Srlg.InterfaceSrlgNames.InterfaceSrlgName']['meta_info']
_meta_table['Srlg.InterfaceSrlgNames.InterfaceSrlgName']['meta_info'].parent =_meta_table['Srlg.InterfaceSrlgNames']['meta_info']
_meta_table['Srlg.SrlgMaps']['meta_info'].parent =_meta_table['Srlg']['meta_info']
_meta_table['Srlg.Nodes']['meta_info'].parent =_meta_table['Srlg']['meta_info']
_meta_table['Srlg.InterfaceSrlgNames']['meta_info'].parent =_meta_table['Srlg']['meta_info']
_meta_table['SelectiveVrfDownload.State']['meta_info'].parent =_meta_table['SelectiveVrfDownload']['meta_info']
