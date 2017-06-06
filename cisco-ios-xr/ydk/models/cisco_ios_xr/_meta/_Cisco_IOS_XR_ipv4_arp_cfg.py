


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ArpEncapEnum' : _MetaInfoEnum('ArpEncapEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        {
            'arpa':'arpa',
            'srp':'srp',
            'srpa':'srpa',
            'srpb':'srpb',
        }, 'Cisco-IOS-XR-ipv4-arp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg']),
    'ArpEntryEnum' : _MetaInfoEnum('ArpEntryEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg',
        {
            'static':'static',
            'alias':'alias',
        }, 'Cisco-IOS-XR-ipv4-arp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg']),
    'Arp' : {
        'meta_info' : _MetaInfoClass('Arp',
            False, 
            [
            _MetaInfoClassMember('inner-cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Configure inner cos values for arp packets
                ''',
                'inner_cos',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('max-entries', ATTRIBUTE, 'int' , None, None, 
                [('1', '256000')], [], 
                '''                Configure maximum number of safe ARP entries per
                line card
                ''',
                'max_entries',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('outer-cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Configure outer cos values for arp packets
                ''',
                'outer_cos',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'arp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg'
        ),
    },
    'Arpgmp.Vrf.Entries.Entry' : {
        'meta_info' : _MetaInfoClass('Arpgmp.Vrf.Entries.Entry',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP Address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-arp-cfg', True),
            _MetaInfoClassMember('encapsulation', REFERENCE_ENUM_CLASS, 'ArpEncapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpEncapEnum', 
                [], [], 
                '''                Encapsulation type
                ''',
                'encapsulation',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('entry-type', REFERENCE_ENUM_CLASS, 'ArpEntryEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpEntryEnum', 
                [], [], 
                '''                Entry type
                ''',
                'entry_type',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC Address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg'
        ),
    },
    'Arpgmp.Vrf.Entries' : {
        'meta_info' : _MetaInfoClass('Arpgmp.Vrf.Entries',
            False, 
            [
            _MetaInfoClassMember('entry', REFERENCE_LIST, 'Entry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'Arpgmp.Vrf.Entries.Entry', 
                [], [], 
                '''                ARP static and alias entry configuration item
                ''',
                'entry',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'entries',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg'
        ),
    },
    'Arpgmp.Vrf' : {
        'meta_info' : _MetaInfoClass('Arpgmp.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-arp-cfg', True),
            _MetaInfoClassMember('entries', REFERENCE_CLASS, 'Entries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'Arpgmp.Vrf.Entries', 
                [], [], 
                '''                ARP static and alias entry configuration
                ''',
                'entries',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg'
        ),
    },
    'Arpgmp' : {
        'meta_info' : _MetaInfoClass('Arpgmp',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'Arpgmp.Vrf', 
                [], [], 
                '''                Per VRF configuration, for the default VRF use
                'default'
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'arpgmp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg'
        ),
    },
    'ArpRedundancy.Redundancy.Groups.Group.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy.Groups.Group.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('prefix-string', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor IPv4 address
                ''',
                'prefix_string',
                'Cisco-IOS-XR-ipv4-arp-cfg', True, [
                    _MetaInfoClassMember('prefix-string', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor IPv4 address
                        ''',
                        'prefix_string',
                        'Cisco-IOS-XR-ipv4-arp-cfg', True),
                    _MetaInfoClassMember('prefix-string', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor IPv4 address
                        ''',
                        'prefix_string',
                        'Cisco-IOS-XR-ipv4-arp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg'
        ),
    },
    'ArpRedundancy.Redundancy.Groups.Group.Peers' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy.Groups.Group.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy.Groups.Group.Peers.Peer', 
                [], [], 
                '''                None
                ''',
                'peer',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg'
        ),
    },
    'ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-arp-cfg', True),
            _MetaInfoClassMember('interface-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface Id for the interface
                ''',
                'interface_id',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg'
        ),
    },
    'ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface', 
                [], [], 
                '''                Interface for this Group
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg'
        ),
    },
    'ArpRedundancy.Redundancy.Groups.Group.InterfaceList' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy.Groups.Group.InterfaceList',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable List of Interfaces for this Group.
                Deletion of this object also causes deletion
                of all associated objects under
                InterfaceList.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces', 
                [], [], 
                '''                Table of Interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'interface-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg'
        ),
    },
    'ArpRedundancy.Redundancy.Groups.Group' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '32')], [], 
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-ipv4-arp-cfg', True),
            _MetaInfoClassMember('interface-list', REFERENCE_CLASS, 'InterfaceList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy.Groups.Group.InterfaceList', 
                [], [], 
                '''                List of Interfaces for this Group
                ''',
                'interface_list',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy.Groups.Group.Peers', 
                [], [], 
                '''                Table of Peer
                ''',
                'peers',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'source_interface',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg'
        ),
    },
    'ArpRedundancy.Redundancy.Groups' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy.Groups.Group', 
                [], [], 
                '''                None
                ''',
                'group',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg'
        ),
    },
    'ArpRedundancy.Redundancy' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy.Redundancy',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Configure parameter for ARP Geo
                redundancy. Deletion of this object also causes
                deletion of all associated objects under
                ArpRedundancy.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy.Groups', 
                [], [], 
                '''                Table of Group
                ''',
                'groups',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg'
        ),
    },
    'ArpRedundancy' : {
        'meta_info' : _MetaInfoClass('ArpRedundancy',
            False, 
            [
            _MetaInfoClassMember('redundancy', REFERENCE_CLASS, 'Redundancy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpRedundancy.Redundancy', 
                [], [], 
                '''                Configure parameter for ARP Geo redundancy
                ''',
                'redundancy',
                'Cisco-IOS-XR-ipv4-arp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-cfg',
            'arp-redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg'
        ),
    },
}
_meta_table['Arpgmp.Vrf.Entries.Entry']['meta_info'].parent =_meta_table['Arpgmp.Vrf.Entries']['meta_info']
_meta_table['Arpgmp.Vrf.Entries']['meta_info'].parent =_meta_table['Arpgmp.Vrf']['meta_info']
_meta_table['Arpgmp.Vrf']['meta_info'].parent =_meta_table['Arpgmp']['meta_info']
_meta_table['ArpRedundancy.Redundancy.Groups.Group.Peers.Peer']['meta_info'].parent =_meta_table['ArpRedundancy.Redundancy.Groups.Group.Peers']['meta_info']
_meta_table['ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface']['meta_info'].parent =_meta_table['ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces']['meta_info']
_meta_table['ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces']['meta_info'].parent =_meta_table['ArpRedundancy.Redundancy.Groups.Group.InterfaceList']['meta_info']
_meta_table['ArpRedundancy.Redundancy.Groups.Group.Peers']['meta_info'].parent =_meta_table['ArpRedundancy.Redundancy.Groups.Group']['meta_info']
_meta_table['ArpRedundancy.Redundancy.Groups.Group.InterfaceList']['meta_info'].parent =_meta_table['ArpRedundancy.Redundancy.Groups.Group']['meta_info']
_meta_table['ArpRedundancy.Redundancy.Groups.Group']['meta_info'].parent =_meta_table['ArpRedundancy.Redundancy.Groups']['meta_info']
_meta_table['ArpRedundancy.Redundancy.Groups']['meta_info'].parent =_meta_table['ArpRedundancy.Redundancy']['meta_info']
_meta_table['ArpRedundancy.Redundancy']['meta_info'].parent =_meta_table['ArpRedundancy']['meta_info']
