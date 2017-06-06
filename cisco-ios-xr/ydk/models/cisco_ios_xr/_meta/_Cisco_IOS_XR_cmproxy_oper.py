


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry' : {
        'meta_info' : _MetaInfoClass('SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Node name
                ''',
                'name',
                'Cisco-IOS-XR-cmproxy-oper', True),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                card type
                ''',
                'card_type',
                'Cisco-IOS-XR-cmproxy-oper', False),
            _MetaInfoClassMember('card-type-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                card type string
                ''',
                'card_type_string',
                'Cisco-IOS-XR-cmproxy-oper', False),
            _MetaInfoClassMember('node-ip', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                node IP address
                ''',
                'node_ip',
                'Cisco-IOS-XR-cmproxy-oper', False),
            _MetaInfoClassMember('node-ipv4-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                node IPv4 address string
                ''',
                'node_ipv4_string',
                'Cisco-IOS-XR-cmproxy-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                node name string
                ''',
                'node_name',
                'Cisco-IOS-XR-cmproxy-oper', False),
            _MetaInfoClassMember('node-sw-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                current software state
                ''',
                'node_sw_state',
                'Cisco-IOS-XR-cmproxy-oper', False),
            _MetaInfoClassMember('node-sw-state-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                current software state string
                ''',
                'node_sw_state_string',
                'Cisco-IOS-XR-cmproxy-oper', False),
            _MetaInfoClassMember('nodeid', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                node ID
                ''',
                'nodeid',
                'Cisco-IOS-XR-cmproxy-oper', False),
            _MetaInfoClassMember('partner-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                partner node id
                ''',
                'partner_id',
                'Cisco-IOS-XR-cmproxy-oper', False),
            _MetaInfoClassMember('partner-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                partner name string
                ''',
                'partner_name',
                'Cisco-IOS-XR-cmproxy-oper', False),
            _MetaInfoClassMember('prev-sw-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                previous software state
                ''',
                'prev_sw_state',
                'Cisco-IOS-XR-cmproxy-oper', False),
            _MetaInfoClassMember('prev-sw-state-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                previous software state string
                ''',
                'prev_sw_state_string',
                'Cisco-IOS-XR-cmproxy-oper', False),
            _MetaInfoClassMember('red-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                redundancy state
                ''',
                'red_state',
                'Cisco-IOS-XR-cmproxy-oper', False),
            _MetaInfoClassMember('red-state-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                redundancy state string
                ''',
                'red_state_string',
                'Cisco-IOS-XR-cmproxy-oper', False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                valid flag
                ''',
                'valid',
                'Cisco-IOS-XR-cmproxy-oper', False),
            ],
            'Cisco-IOS-XR-cmproxy-oper',
            'node-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-cmproxy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper'
        ),
    },
    'SdrInventoryVm.Nodes.Node.NodeEntries' : {
        'meta_info' : _MetaInfoClass('SdrInventoryVm.Nodes.Node.NodeEntries',
            False, 
            [
            _MetaInfoClassMember('node-entry', REFERENCE_LIST, 'NodeEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper', 'SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry', 
                [], [], 
                '''                VM information for a node
                ''',
                'node_entry',
                'Cisco-IOS-XR-cmproxy-oper', False),
            ],
            'Cisco-IOS-XR-cmproxy-oper',
            'node-entries',
            _yang_ns._namespaces['Cisco-IOS-XR-cmproxy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper'
        ),
    },
    'SdrInventoryVm.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('SdrInventoryVm.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Node name
                ''',
                'name',
                'Cisco-IOS-XR-cmproxy-oper', True),
            _MetaInfoClassMember('node-entries', REFERENCE_CLASS, 'NodeEntries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper', 'SdrInventoryVm.Nodes.Node.NodeEntries', 
                [], [], 
                '''                VM Information
                ''',
                'node_entries',
                'Cisco-IOS-XR-cmproxy-oper', False),
            ],
            'Cisco-IOS-XR-cmproxy-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-cmproxy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper'
        ),
    },
    'SdrInventoryVm.Nodes' : {
        'meta_info' : _MetaInfoClass('SdrInventoryVm.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper', 'SdrInventoryVm.Nodes.Node', 
                [], [], 
                '''                Node name
                ''',
                'node',
                'Cisco-IOS-XR-cmproxy-oper', False),
            ],
            'Cisco-IOS-XR-cmproxy-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-cmproxy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper'
        ),
    },
    'SdrInventoryVm' : {
        'meta_info' : _MetaInfoClass('SdrInventoryVm',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper', 'SdrInventoryVm.Nodes', 
                [], [], 
                '''                Node directory
                ''',
                'nodes',
                'Cisco-IOS-XR-cmproxy-oper', False),
            ],
            'Cisco-IOS-XR-cmproxy-oper',
            'sdr-inventory-vm',
            _yang_ns._namespaces['Cisco-IOS-XR-cmproxy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper'
        ),
    },
}
_meta_table['SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry']['meta_info'].parent =_meta_table['SdrInventoryVm.Nodes.Node.NodeEntries']['meta_info']
_meta_table['SdrInventoryVm.Nodes.Node.NodeEntries']['meta_info'].parent =_meta_table['SdrInventoryVm.Nodes.Node']['meta_info']
_meta_table['SdrInventoryVm.Nodes.Node']['meta_info'].parent =_meta_table['SdrInventoryVm.Nodes']['meta_info']
_meta_table['SdrInventoryVm.Nodes']['meta_info'].parent =_meta_table['SdrInventoryVm']['meta_info']
