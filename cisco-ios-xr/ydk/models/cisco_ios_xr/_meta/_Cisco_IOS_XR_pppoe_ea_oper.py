


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac',
            False, 
            [
            _MetaInfoClassMember('macaddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                macaddr
                ''',
                'macaddr',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'srgv-mac',
            _yang_ns._namespaces['Cisco-IOS-XR-pppoe-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper'
        ),
    },
    'PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId',
            False, 
            [
            _MetaInfoClassMember('parent-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'parent_interface_name',
                'Cisco-IOS-XR-pppoe-ea-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            _MetaInfoClassMember('is-in-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is in sync
                ''',
                'is_in_sync',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            _MetaInfoClassMember('srgv-mac', REFERENCE_CLASS, 'SrgvMac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac', 
                [], [], 
                '''                SRG VMac-address
                ''',
                'srgv_mac',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'parent-interface-id',
            _yang_ns._namespaces['Cisco-IOS-XR-pppoe-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper'
        ),
    },
    'PppoeEa.Nodes.Node.ParentInterfaceIds' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.ParentInterfaceIds',
            False, 
            [
            _MetaInfoClassMember('parent-interface-id', REFERENCE_LIST, 'ParentInterfaceId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId', 
                [], [], 
                '''                PPPoE parent interface info
                ''',
                'parent_interface_id',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'parent-interface-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-pppoe-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper'
        ),
    },
    'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac',
            False, 
            [
            _MetaInfoClassMember('macaddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                macaddr
                ''',
                'macaddr',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'peer-mac',
            _yang_ns._namespaces['Cisco-IOS-XR-pppoe-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper'
        ),
    },
    'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac',
            False, 
            [
            _MetaInfoClassMember('macaddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                macaddr
                ''',
                'macaddr',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'local-mac',
            _yang_ns._namespaces['Cisco-IOS-XR-pppoe-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper'
        ),
    },
    'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac',
            False, 
            [
            _MetaInfoClassMember('macaddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                macaddr
                ''',
                'macaddr',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'srgv-mac',
            _yang_ns._namespaces['Cisco-IOS-XR-pppoe-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper'
        ),
    },
    'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.InterfaceIds.InterfaceId',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-pppoe-ea-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            _MetaInfoClassMember('is-in-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is in sync
                ''',
                'is_in_sync',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            _MetaInfoClassMember('is-platform-created', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Platform created
                ''',
                'is_platform_created',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            _MetaInfoClassMember('is-priority-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Priority Set
                ''',
                'is_priority_set',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            _MetaInfoClassMember('local-mac', REFERENCE_CLASS, 'LocalMac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac', 
                [], [], 
                '''                Local Mac-address
                ''',
                'local_mac',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            _MetaInfoClassMember('parent-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Parent Interface
                ''',
                'parent_interface',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            _MetaInfoClassMember('peer-mac', REFERENCE_CLASS, 'PeerMac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac', 
                [], [], 
                '''                Peer Mac-address
                ''',
                'peer_mac',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            _MetaInfoClassMember('srgv-mac', REFERENCE_CLASS, 'SrgvMac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac', 
                [], [], 
                '''                SRG VMac-address
                ''',
                'srgv_mac',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            _MetaInfoClassMember('vlanid', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN Ids
                ''',
                'vlanid',
                'Cisco-IOS-XR-pppoe-ea-oper', False, max_elements=2),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'interface-id',
            _yang_ns._namespaces['Cisco-IOS-XR-pppoe-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper'
        ),
    },
    'PppoeEa.Nodes.Node.InterfaceIds' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node.InterfaceIds',
            False, 
            [
            _MetaInfoClassMember('interface-id', REFERENCE_LIST, 'InterfaceId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.InterfaceIds.InterfaceId', 
                [], [], 
                '''                PPPoE interface info
                ''',
                'interface_id',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'interface-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-pppoe-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper'
        ),
    },
    'PppoeEa.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-pppoe-ea-oper', True),
            _MetaInfoClassMember('interface-ids', REFERENCE_CLASS, 'InterfaceIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.InterfaceIds', 
                [], [], 
                '''                PPPoE interface info
                ''',
                'interface_ids',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            _MetaInfoClassMember('parent-interface-ids', REFERENCE_CLASS, 'ParentInterfaceIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node.ParentInterfaceIds', 
                [], [], 
                '''                PPPoE parent interface info
                ''',
                'parent_interface_ids',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-pppoe-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper'
        ),
    },
    'PppoeEa.Nodes' : {
        'meta_info' : _MetaInfoClass('PppoeEa.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes.Node', 
                [], [], 
                '''                PPPOE-EA operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-pppoe-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper'
        ),
    },
    'PppoeEa' : {
        'meta_info' : _MetaInfoClass('PppoeEa',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper', 'PppoeEa.Nodes', 
                [], [], 
                '''                PPPOE_EA list of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-pppoe-ea-oper', False),
            ],
            'Cisco-IOS-XR-pppoe-ea-oper',
            'pppoe-ea',
            _yang_ns._namespaces['Cisco-IOS-XR-pppoe-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper'
        ),
    },
}
_meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId']['meta_info']
_meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds']['meta_info']
_meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId']['meta_info']
_meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId']['meta_info']
_meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId']['meta_info']
_meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node.InterfaceIds']['meta_info']
_meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node']['meta_info']
_meta_table['PppoeEa.Nodes.Node.InterfaceIds']['meta_info'].parent =_meta_table['PppoeEa.Nodes.Node']['meta_info']
_meta_table['PppoeEa.Nodes.Node']['meta_info'].parent =_meta_table['PppoeEa.Nodes']['meta_info']
_meta_table['PppoeEa.Nodes']['meta_info'].parent =_meta_table['PppoeEa']['meta_info']
