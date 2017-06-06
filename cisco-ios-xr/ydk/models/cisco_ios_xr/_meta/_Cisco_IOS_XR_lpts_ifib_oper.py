


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'LptsIfib.Nodes.Node.SliceIds.SliceId.Entry' : {
        'meta_info' : _MetaInfoClass('LptsIfib.Nodes.Node.SliceIds.SliceId.Entry',
            False, 
            [
            _MetaInfoClassMember('entry', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Single Pre-ifib entry
                ''',
                'entry',
                'Cisco-IOS-XR-lpts-ifib-oper', True),
            _MetaInfoClassMember('accepts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets matched to accept
                ''',
                'accepts',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('deliver-list-long', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Deliver List Long Format
                ''',
                'deliver_list_long',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('deliver-list-short', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Deliver List Short Format
                ''',
                'deliver_list_short',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('destination-addr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination IP Address
                ''',
                'destination_addr',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('destination-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination Key Type
                ''',
                'destination_type',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('destination-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination Port/ICMP Type/IGMP Type
                ''',
                'destination_value',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets matched to drop
                ''',
                'drops',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('flow-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Flow type
                ''',
                'flow_type',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('ifib-program-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ifib program time in netio
                ''',
                'ifib_program_time',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('intf-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Handle
                ''',
                'intf_handle',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('intf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'intf_name',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('is-fgid', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Is FGID or not
                ''',
                'is_fgid',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('is-syn', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Is SYN
                ''',
                'is_syn',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('l3protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Layer 3 Protocol
                ''',
                'l3protocol',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('l4protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Layer 4 Protocol
                ''',
                'l4protocol',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('listener-tag', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Listener Tag
                ''',
                'listener_tag',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('local-flag', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Local Flag
                ''',
                'local_flag',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('min-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Minimum TTL
                ''',
                'min_ttl',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('opcode', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Opcode
                ''',
                'opcode',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('pending-ifibq-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pending ifib queue delay
                ''',
                'pending_ifibq_delay',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('sl-ifibq-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                sl_ifibq delay
                ''',
                'sl_ifibq_delay',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('source-addr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source IP Address
                ''',
                'source_addr',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('source-port', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source port
                ''',
                'source_port',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('vid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF ID
                ''',
                'vid',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            ],
            'Cisco-IOS-XR-lpts-ifib-oper',
            'entry',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-ifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper'
        ),
    },
    'LptsIfib.Nodes.Node.SliceIds.SliceId' : {
        'meta_info' : _MetaInfoClass('LptsIfib.Nodes.Node.SliceIds.SliceId',
            False, 
            [
            _MetaInfoClassMember('slice-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Type value
                ''',
                'slice_name',
                'Cisco-IOS-XR-lpts-ifib-oper', True),
            _MetaInfoClassMember('entry', REFERENCE_LIST, 'Entry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper', 'LptsIfib.Nodes.Node.SliceIds.SliceId.Entry', 
                [], [], 
                '''                Data for single pre-ifib entry
                ''',
                'entry',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            ],
            'Cisco-IOS-XR-lpts-ifib-oper',
            'slice-id',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-ifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper'
        ),
    },
    'LptsIfib.Nodes.Node.SliceIds' : {
        'meta_info' : _MetaInfoClass('LptsIfib.Nodes.Node.SliceIds',
            False, 
            [
            _MetaInfoClassMember('slice-id', REFERENCE_LIST, 'SliceId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper', 'LptsIfib.Nodes.Node.SliceIds.SliceId', 
                [], [], 
                '''                slice types
                ''',
                'slice_id',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            ],
            'Cisco-IOS-XR-lpts-ifib-oper',
            'slice-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-ifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper'
        ),
    },
    'LptsIfib.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('LptsIfib.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node name
                ''',
                'node_name',
                'Cisco-IOS-XR-lpts-ifib-oper', True),
            _MetaInfoClassMember('slice-ids', REFERENCE_CLASS, 'SliceIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper', 'LptsIfib.Nodes.Node.SliceIds', 
                [], [], 
                '''                Slice specific
                ''',
                'slice_ids',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            ],
            'Cisco-IOS-XR-lpts-ifib-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-ifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper'
        ),
    },
    'LptsIfib.Nodes' : {
        'meta_info' : _MetaInfoClass('LptsIfib.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper', 'LptsIfib.Nodes.Node', 
                [], [], 
                '''                Per node slice 
                ''',
                'node',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            ],
            'Cisco-IOS-XR-lpts-ifib-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-ifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper'
        ),
    },
    'LptsIfib' : {
        'meta_info' : _MetaInfoClass('LptsIfib',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper', 'LptsIfib.Nodes', 
                [], [], 
                '''                Node ifib database
                ''',
                'nodes',
                'Cisco-IOS-XR-lpts-ifib-oper', False),
            ],
            'Cisco-IOS-XR-lpts-ifib-oper',
            'lpts-ifib',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-ifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_ifib_oper'
        ),
    },
}
_meta_table['LptsIfib.Nodes.Node.SliceIds.SliceId.Entry']['meta_info'].parent =_meta_table['LptsIfib.Nodes.Node.SliceIds.SliceId']['meta_info']
_meta_table['LptsIfib.Nodes.Node.SliceIds.SliceId']['meta_info'].parent =_meta_table['LptsIfib.Nodes.Node.SliceIds']['meta_info']
_meta_table['LptsIfib.Nodes.Node.SliceIds']['meta_info'].parent =_meta_table['LptsIfib.Nodes.Node']['meta_info']
_meta_table['LptsIfib.Nodes.Node']['meta_info'].parent =_meta_table['LptsIfib.Nodes']['meta_info']
_meta_table['LptsIfib.Nodes']['meta_info'].parent =_meta_table['LptsIfib']['meta_info']
