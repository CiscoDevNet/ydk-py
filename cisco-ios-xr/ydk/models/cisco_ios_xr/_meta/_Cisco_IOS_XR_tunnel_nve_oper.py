


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Nve.Vnis.Vni' : {
        'meta_info' : _MetaInfoClass('Nve.Vnis.Vni',
            False, 
            [
            _MetaInfoClassMember('vni', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VNI ID
                ''',
                'vni',
                'Cisco-IOS-XR-tunnel-nve-oper', True),
            _MetaInfoClassMember('bvi-ifh', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BVI Interface Handle
                ''',
                'bvi_ifh',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('bvi-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                BVI MAC address
                ''',
                'bvi_mac',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('bvi-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                BVI Interface Oper State
                ''',
                'bvi_state',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flags
                ''',
                'flags',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NVE Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('ipv4-tbl-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv4 Table ID
                ''',
                'ipv4_tbl_id',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('ipv6-tbl-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 Table ID
                ''',
                'ipv6_tbl_id',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('mcast-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                McastFlags
                ''',
                'mcast_flags',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('mcast-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                MCAST IPv4 Address
                ''',
                'mcast_ipv4_address',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('topo-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                L2RIB Topology ID
                ''',
                'topo_id',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('topo-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 50)], [], 
                '''                L2RIB Topology Name
                ''',
                'topo_name',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('topo-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TOPO ID valid flag
                ''',
                'topo_valid',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('udp-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDP Port
                ''',
                'udp_port',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('vni-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VNI Max in Range
                ''',
                'vni_max',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('vni-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VNI Min in Range
                ''',
                'vni_min',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('vni-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VNI Number
                ''',
                'vni_xr',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                L3 VRF ID
                ''',
                'vrf_id',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                L3 VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('vrf-vni', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF VNI
                ''',
                'vrf_vni',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-nve-oper',
            'vni',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-nve-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper'
        ),
    },
    'Nve.Vnis' : {
        'meta_info' : _MetaInfoClass('Nve.Vnis',
            False, 
            [
            _MetaInfoClassMember('vni', REFERENCE_LIST, 'Vni' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper', 'Nve.Vnis.Vni', 
                [], [], 
                '''                The attributes for a particular VNI
                ''',
                'vni',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-nve-oper',
            'vnis',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-nve-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper'
        ),
    },
    'Nve.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Nve.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-tunnel-nve-oper', True),
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                Admin State
                ''',
                'admin_state',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('any-cast-source-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Anycast Source Interface name
                ''',
                'any_cast_source_interface_name',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('any-cast-source-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Anycast Source IPv4 Address
                ''',
                'any_cast_source_ipv4_address',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('any-cast-source-state', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                Anycast Source Interface State
                ''',
                'any_cast_source_state',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('encap', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                Encap
                ''',
                'encap',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flags
                ''',
                'flags',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('if-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                NVE IfHandle
                ''',
                'if_handle',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('source-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Interface name
                ''',
                'source_interface_name',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('source-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source IPv4 Address
                ''',
                'source_ipv4_address',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('source-state', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                Source Intf State
                ''',
                'source_state',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('sync-mcast-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sync McastFlags
                ''',
                'sync_mcast_flags',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('sync-mcast-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                MCAST sync group IPv4 Address
                ''',
                'sync_mcast_ipv4_address',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('udp-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDP Port
                ''',
                'udp_port',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-nve-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-nve-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper'
        ),
    },
    'Nve.Interfaces' : {
        'meta_info' : _MetaInfoClass('Nve.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper', 'Nve.Interfaces.Interface', 
                [], [], 
                '''                The attributes for a particular interface
                ''',
                'interface',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-nve-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-nve-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper'
        ),
    },
    'Nve' : {
        'meta_info' : _MetaInfoClass('Nve',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper', 'Nve.Interfaces', 
                [], [], 
                '''                Table for NVE interface attributes
                ''',
                'interfaces',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            _MetaInfoClassMember('vnis', REFERENCE_CLASS, 'Vnis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper', 'Nve.Vnis', 
                [], [], 
                '''                Table for VNIs
                ''',
                'vnis',
                'Cisco-IOS-XR-tunnel-nve-oper', False),
            ],
            'Cisco-IOS-XR-tunnel-nve-oper',
            'nve',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-nve-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_nve_oper'
        ),
    },
}
_meta_table['Nve.Vnis.Vni']['meta_info'].parent =_meta_table['Nve.Vnis']['meta_info']
_meta_table['Nve.Interfaces.Interface']['meta_info'].parent =_meta_table['Nve.Interfaces']['meta_info']
_meta_table['Nve.Vnis']['meta_info'].parent =_meta_table['Nve']['meta_info']
_meta_table['Nve.Interfaces']['meta_info'].parent =_meta_table['Nve']['meta_info']
