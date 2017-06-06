


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PrmTcamProfileEnum' : _MetaInfoEnum('PrmTcamProfileEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg',
        {
            'profile0':'profile0',
            'profile1':'profile1',
            'profile2':'profile2',
        }, 'Cisco-IOS-XR-asr9k-prm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg']),
    'Asr9KEfdModeEnum' : _MetaInfoEnum('Asr9KEfdModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg',
        {
            'only-outer-encap':'only_outer_encap',
            'include-inner-encap':'include_inner_encap',
        }, 'Cisco-IOS-XR-asr9k-prm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg']),
    'Asr9KEfdOperationEnum' : _MetaInfoEnum('Asr9KEfdOperationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg',
        {
            'less-than':'less_than',
            'greater-than-or-equal':'greater_than_or_equal',
        }, 'Cisco-IOS-XR-asr9k-prm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg']),
    'HardwareModuleQosMode.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('HardwareModuleQosMode.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-asr9k-prm-cfg', True),
            _MetaInfoClassMember('child-shaping-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable child level/flat policy shaping
                ''',
                'child_shaping_disable',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('lowburst-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable low burst mode for TM entity
                ''',
                'lowburst_enable',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleQosMode.Nodes' : {
        'meta_info' : _MetaInfoClass('HardwareModuleQosMode.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleQosMode.Nodes.Node', 
                [], [], 
                '''                A node
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleQosMode' : {
        'meta_info' : _MetaInfoClass('HardwareModuleQosMode',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleQosMode.Nodes', 
                [], [], 
                '''                QoS applicable nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'hardware-module-qos-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np' : {
        'meta_info' : _MetaInfoClass('HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np',
            False, 
            [
            _MetaInfoClassMember('np-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Number between 0-7
                ''',
                'np_id',
                'Cisco-IOS-XR-asr9k-prm-cfg', True),
            _MetaInfoClassMember('adjust-value', ATTRIBUTE, 'int' , None, None, 
                [('1280', '1535')], [], 
                '''                TCP MSS Adjust value
                ''',
                'adjust_value',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'np',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleTcpMssAdjust.Nodes.Node.Nps' : {
        'meta_info' : _MetaInfoClass('HardwareModuleTcpMssAdjust.Nodes.Node.Nps',
            False, 
            [
            _MetaInfoClassMember('np', REFERENCE_LIST, 'Np' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np', 
                [], [], 
                '''                NP number
                ''',
                'np',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'nps',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleTcpMssAdjust.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('HardwareModuleTcpMssAdjust.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-asr9k-prm-cfg', True),
            _MetaInfoClassMember('nps', REFERENCE_CLASS, 'Nps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleTcpMssAdjust.Nodes.Node.Nps', 
                [], [], 
                '''                TCP MSS Adjust NPs
                ''',
                'nps',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleTcpMssAdjust.Nodes' : {
        'meta_info' : _MetaInfoClass('HardwareModuleTcpMssAdjust.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleTcpMssAdjust.Nodes.Node', 
                [], [], 
                '''                A node
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleTcpMssAdjust' : {
        'meta_info' : _MetaInfoClass('HardwareModuleTcpMssAdjust',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleTcpMssAdjust.Nodes', 
                [], [], 
                '''                TCP MSS Adjust applicable nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'hardware-module-tcp-mss-adjust',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleLoadBalance.Bundle.L2Service' : {
        'meta_info' : _MetaInfoClass('HardwareModuleLoadBalance.Bundle.L2Service',
            False, 
            [
            _MetaInfoClassMember('l3-parameters', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Load balance L2 services over bundle with L3
                parameters
                ''',
                'l3_parameters',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'l2-service',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleLoadBalance.Bundle' : {
        'meta_info' : _MetaInfoClass('HardwareModuleLoadBalance.Bundle',
            False, 
            [
            _MetaInfoClassMember('l2-service', REFERENCE_CLASS, 'L2Service' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleLoadBalance.Bundle.L2Service', 
                [], [], 
                '''                Load balance for L2 services
                ''',
                'l2_service',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'bundle',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleLoadBalance' : {
        'meta_info' : _MetaInfoClass('HardwareModuleLoadBalance',
            False, 
            [
            _MetaInfoClassMember('bundle', REFERENCE_CLASS, 'Bundle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleLoadBalance.Bundle', 
                [], [], 
                '''                Bundle load balance options
                ''',
                'bundle',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'hardware-module-load-balance',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleTcam.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('HardwareModuleTcam.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-asr9k-prm-cfg', True),
            _MetaInfoClassMember('profile', REFERENCE_ENUM_CLASS, 'PrmTcamProfileEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'PrmTcamProfileEnum', 
                [], [], 
                '''                A TCAM partition profile
                ''',
                'profile',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleTcam.Nodes' : {
        'meta_info' : _MetaInfoClass('HardwareModuleTcam.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleTcam.Nodes.Node', 
                [], [], 
                '''                A TCAM applicable node
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleTcam' : {
        'meta_info' : _MetaInfoClass('HardwareModuleTcam',
            False, 
            [
            _MetaInfoClassMember('global-profile', REFERENCE_ENUM_CLASS, 'PrmTcamProfileEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'PrmTcamProfileEnum', 
                [], [], 
                '''                Global TCAM partition profile for all TCAM
                applicable nodes
                ''',
                'global_profile',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleTcam.Nodes', 
                [], [], 
                '''                TCAM applicable nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'hardware-module-tcam',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleEfd.NodeAll.IpPrecedence' : {
        'meta_info' : _MetaInfoClass('HardwareModuleEfd.NodeAll.IpPrecedence',
            False, 
            [
            _MetaInfoClassMember('operation', REFERENCE_ENUM_CLASS, 'Asr9KEfdOperationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'Asr9KEfdOperationEnum', 
                [], [], 
                '''                IP operation
                ''',
                'operation',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                IP TOS precedence threshold
                ''',
                'precedence',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'ip-precedence',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleEfd.NodeAll.VlanCos' : {
        'meta_info' : _MetaInfoClass('HardwareModuleEfd.NodeAll.VlanCos',
            False, 
            [
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                VLAN COS threshold
                ''',
                'cos',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('operation', REFERENCE_ENUM_CLASS, 'Asr9KEfdOperationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'Asr9KEfdOperationEnum', 
                [], [], 
                '''                VLAN operation
                ''',
                'operation',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'vlan-cos',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleEfd.NodeAll.MplsExp' : {
        'meta_info' : _MetaInfoClass('HardwareModuleEfd.NodeAll.MplsExp',
            False, 
            [
            _MetaInfoClassMember('exp', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                MPLS EXP threshold
                ''',
                'exp',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('operation', REFERENCE_ENUM_CLASS, 'Asr9KEfdOperationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'Asr9KEfdOperationEnum', 
                [], [], 
                '''                MPLS operation
                ''',
                'operation',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'mpls-exp',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleEfd.NodeAll' : {
        'meta_info' : _MetaInfoClass('HardwareModuleEfd.NodeAll',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable EFD for this node
                ''',
                'enable',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('ip-precedence', REFERENCE_CLASS, 'IpPrecedence' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleEfd.NodeAll.IpPrecedence', 
                [], [], 
                '''                EFD IP parameters
                ''',
                'ip_precedence',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'Asr9KEfdModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'Asr9KEfdModeEnum', 
                [], [], 
                '''                EFD mode parameter.
                ''',
                'mode',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('mpls-exp', REFERENCE_CLASS, 'MplsExp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleEfd.NodeAll.MplsExp', 
                [], [], 
                '''                EFD MPLS parameters
                ''',
                'mpls_exp',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('vlan-cos', REFERENCE_CLASS, 'VlanCos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleEfd.NodeAll.VlanCos', 
                [], [], 
                '''                EFD VLAN parameters
                ''',
                'vlan_cos',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'node-all',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleEfd.Nodes.Node.IpPrecedence' : {
        'meta_info' : _MetaInfoClass('HardwareModuleEfd.Nodes.Node.IpPrecedence',
            False, 
            [
            _MetaInfoClassMember('operation', REFERENCE_ENUM_CLASS, 'Asr9KEfdOperationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'Asr9KEfdOperationEnum', 
                [], [], 
                '''                IP operation
                ''',
                'operation',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                IP TOS precedence threshold
                ''',
                'precedence',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'ip-precedence',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleEfd.Nodes.Node.VlanCos' : {
        'meta_info' : _MetaInfoClass('HardwareModuleEfd.Nodes.Node.VlanCos',
            False, 
            [
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                VLAN COS threshold
                ''',
                'cos',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('operation', REFERENCE_ENUM_CLASS, 'Asr9KEfdOperationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'Asr9KEfdOperationEnum', 
                [], [], 
                '''                VLAN operation
                ''',
                'operation',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'vlan-cos',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleEfd.Nodes.Node.MplsExp' : {
        'meta_info' : _MetaInfoClass('HardwareModuleEfd.Nodes.Node.MplsExp',
            False, 
            [
            _MetaInfoClassMember('exp', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                MPLS EXP threshold
                ''',
                'exp',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('operation', REFERENCE_ENUM_CLASS, 'Asr9KEfdOperationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'Asr9KEfdOperationEnum', 
                [], [], 
                '''                MPLS operation
                ''',
                'operation',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'mpls-exp',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleEfd.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('HardwareModuleEfd.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node Name
                ''',
                'node_name',
                'Cisco-IOS-XR-asr9k-prm-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable EFD for this node
                ''',
                'enable',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('ip-precedence', REFERENCE_CLASS, 'IpPrecedence' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleEfd.Nodes.Node.IpPrecedence', 
                [], [], 
                '''                EFD IP parameters
                ''',
                'ip_precedence',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'Asr9KEfdModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'Asr9KEfdModeEnum', 
                [], [], 
                '''                EFD mode parameter.
                ''',
                'mode',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('mpls-exp', REFERENCE_CLASS, 'MplsExp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleEfd.Nodes.Node.MplsExp', 
                [], [], 
                '''                EFD MPLS parameters
                ''',
                'mpls_exp',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('vlan-cos', REFERENCE_CLASS, 'VlanCos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleEfd.Nodes.Node.VlanCos', 
                [], [], 
                '''                EFD VLAN parameters
                ''',
                'vlan_cos',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleEfd.Nodes' : {
        'meta_info' : _MetaInfoClass('HardwareModuleEfd.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleEfd.Nodes.Node', 
                [], [], 
                '''                A node
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
    'HardwareModuleEfd' : {
        'meta_info' : _MetaInfoClass('HardwareModuleEfd',
            False, 
            [
            _MetaInfoClassMember('node-all', REFERENCE_CLASS, 'NodeAll' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleEfd.NodeAll', 
                [], [], 
                '''                All nodes
                ''',
                'node_all',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg', 'HardwareModuleEfd.Nodes', 
                [], [], 
                '''                EFD applicable nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-asr9k-prm-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-prm-cfg',
            'hardware-module-efd',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-prm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg'
        ),
    },
}
_meta_table['HardwareModuleQosMode.Nodes.Node']['meta_info'].parent =_meta_table['HardwareModuleQosMode.Nodes']['meta_info']
_meta_table['HardwareModuleQosMode.Nodes']['meta_info'].parent =_meta_table['HardwareModuleQosMode']['meta_info']
_meta_table['HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np']['meta_info'].parent =_meta_table['HardwareModuleTcpMssAdjust.Nodes.Node.Nps']['meta_info']
_meta_table['HardwareModuleTcpMssAdjust.Nodes.Node.Nps']['meta_info'].parent =_meta_table['HardwareModuleTcpMssAdjust.Nodes.Node']['meta_info']
_meta_table['HardwareModuleTcpMssAdjust.Nodes.Node']['meta_info'].parent =_meta_table['HardwareModuleTcpMssAdjust.Nodes']['meta_info']
_meta_table['HardwareModuleTcpMssAdjust.Nodes']['meta_info'].parent =_meta_table['HardwareModuleTcpMssAdjust']['meta_info']
_meta_table['HardwareModuleLoadBalance.Bundle.L2Service']['meta_info'].parent =_meta_table['HardwareModuleLoadBalance.Bundle']['meta_info']
_meta_table['HardwareModuleLoadBalance.Bundle']['meta_info'].parent =_meta_table['HardwareModuleLoadBalance']['meta_info']
_meta_table['HardwareModuleTcam.Nodes.Node']['meta_info'].parent =_meta_table['HardwareModuleTcam.Nodes']['meta_info']
_meta_table['HardwareModuleTcam.Nodes']['meta_info'].parent =_meta_table['HardwareModuleTcam']['meta_info']
_meta_table['HardwareModuleEfd.NodeAll.IpPrecedence']['meta_info'].parent =_meta_table['HardwareModuleEfd.NodeAll']['meta_info']
_meta_table['HardwareModuleEfd.NodeAll.VlanCos']['meta_info'].parent =_meta_table['HardwareModuleEfd.NodeAll']['meta_info']
_meta_table['HardwareModuleEfd.NodeAll.MplsExp']['meta_info'].parent =_meta_table['HardwareModuleEfd.NodeAll']['meta_info']
_meta_table['HardwareModuleEfd.Nodes.Node.IpPrecedence']['meta_info'].parent =_meta_table['HardwareModuleEfd.Nodes.Node']['meta_info']
_meta_table['HardwareModuleEfd.Nodes.Node.VlanCos']['meta_info'].parent =_meta_table['HardwareModuleEfd.Nodes.Node']['meta_info']
_meta_table['HardwareModuleEfd.Nodes.Node.MplsExp']['meta_info'].parent =_meta_table['HardwareModuleEfd.Nodes.Node']['meta_info']
_meta_table['HardwareModuleEfd.Nodes.Node']['meta_info'].parent =_meta_table['HardwareModuleEfd.Nodes']['meta_info']
_meta_table['HardwareModuleEfd.NodeAll']['meta_info'].parent =_meta_table['HardwareModuleEfd']['meta_info']
_meta_table['HardwareModuleEfd.Nodes']['meta_info'].parent =_meta_table['HardwareModuleEfd']['meta_info']
