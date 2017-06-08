


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTableVersion' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTableVersion',
            False, 
            [
            _MetaInfoClassMember('binding-table-date', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp to the binding
                table
                ''',
                'binding_table_date',
                'ietf-softwire', False),
            _MetaInfoClassMember('binding-table-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Incremental version number
                to the binding table
                ''',
                'binding_table_version',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'binding-table-version',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry.PortSet' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry.PortSet',
            False, 
            [
            _MetaInfoClassMember('psid', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port Set Identifier (PSID) value, which identifies a set
                of ports algorithmically.
                ''',
                'psid',
                'ietf-softwire', False),
            _MetaInfoClassMember('psid-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '15')], [], 
                '''                The length of PSID, representing the sharing ratio for an
                IPv4 address.
                ''',
                'psid_len',
                'ietf-softwire', False),
            _MetaInfoClassMember('psid-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '16')], [], 
                '''                The number of offset bits. In Lightweight 4over6, the default
                value is 0 for assigning one contiguous port range. In MAP-E/T,
                the default value is 6, which excludes system ports by default
                and assigns port ranges distribute across the entire port space.
                If the this parameter is larger than 0, the value of offset
                MUST be greater than 0.
                ''',
                'psid_offset',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'port-set',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry',
            False, 
            [
            _MetaInfoClassMember('binding-ipv6info', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IPv6 information for a binding entry.
                If this is an IPv6 prefix, it indicates that
                the IPv6 source address of the lwB4 is constructed
                according to the description in RFC7596;
                if it is an IPv6 address, it means the lwB4 uses
                any /128 address from the assigned IPv6 prefix.
                
                ''',
                'binding_ipv6info',
                'ietf-softwire', True, [
                    _MetaInfoClassMember('binding-ipv6info', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IPv6 information for a binding entry.
                        If this is an IPv6 prefix, it indicates that
                        the IPv6 source address of the lwB4 is constructed
                        according to the description in RFC7596;
                        if it is an IPv6 address, it means the lwB4 uses
                        any /128 address from the assigned IPv6 prefix.
                        
                        ''',
                        'binding_ipv6info',
                        'ietf-softwire', True),
                    _MetaInfoClassMember('binding-ipv6info', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        The IPv6 information for a binding entry.
                        If this is an IPv6 prefix, it indicates that
                        the IPv6 source address of the lwB4 is constructed
                        according to the description in RFC7596;
                        if it is an IPv6 address, it means the lwB4 uses
                        any /128 address from the assigned IPv6 prefix.
                        
                        ''',
                        'binding_ipv6info',
                        'ietf-softwire', True),
                ]),
            _MetaInfoClassMember('binding-ipv4-addr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv4 address assigned to the lwB4, which is
                used as the IPv4 external address
                for lwB4 local NAPT44.
                ''',
                'binding_ipv4_addr',
                'ietf-softwire', False),
            _MetaInfoClassMember('br-ipv6-addr', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv6 address for lwaftr.
                ''',
                'br_ipv6_addr',
                'ietf-softwire', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The lifetime for the binding entry
                ''',
                'lifetime',
                'ietf-softwire', False),
            _MetaInfoClassMember('port-set', REFERENCE_CLASS, 'PortSet' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry.PortSet', 
                [], [], 
                '''                For Lightweight 4over6, the default value
                of offset should be 0, to configure one contiguous
                port range.
                ''',
                'port_set',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'binding-entry',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable',
            False, 
            [
            _MetaInfoClassMember('binding-entry', REFERENCE_LIST, 'BindingEntry' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry', 
                [], [], 
                '''                binding entry
                ''',
                'binding_entry',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'binding-table',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Binding.Br.BrInstances.BrInstance' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Binding.Br.BrInstances.BrInstance',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An instance identifier.
                ''',
                'id',
                'ietf-softwire', True),
            _MetaInfoClassMember('binding-table', REFERENCE_CLASS, 'BindingTable' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable', 
                [], [], 
                '''                binding table
                ''',
                'binding_table',
                'ietf-softwire', False),
            _MetaInfoClassMember('binding-table-version', REFERENCE_CLASS, 'BindingTableVersion' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTableVersion', 
                [], [], 
                '''                binding table's version
                ''',
                'binding_table_version',
                'ietf-softwire', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name for the lwaftr.
                ''',
                'name',
                'ietf-softwire', False),
            _MetaInfoClassMember('softwire-num-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum number of tunnels that can be created on
                the lwAFTR.
                ''',
                'softwire_num_threshold',
                'ietf-softwire', False),
            _MetaInfoClassMember('tunnel-path-mru', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The path MRU for Lightweight 4over6 tunnel.
                ''',
                'tunnel_path_mru',
                'ietf-softwire', False),
            _MetaInfoClassMember('tunnel-payload-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The payload MTU for Lightweight 4over6 tunnel.
                ''',
                'tunnel_payload_mtu',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'br-instance',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Binding.Br.BrInstances' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Binding.Br.BrInstances',
            False, 
            [
            _MetaInfoClassMember('br-instance', REFERENCE_LIST, 'BrInstance' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Binding.Br.BrInstances.BrInstance', 
                [], [], 
                '''                A set of lwAFTRs to be configured.
                ''',
                'br_instance',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'br-instances',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Binding.Br' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Binding.Br',
            False, 
            [
            _MetaInfoClassMember('br-instances', REFERENCE_CLASS, 'BrInstances' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Binding.Br.BrInstances', 
                [], [], 
                '''                A set of BRs to be configured.
                ''',
                'br_instances',
                'ietf-softwire', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable the lwAFTR (BR) function.
                ''',
                'enable',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'br',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Binding.Ce.CeInstances.CeInstance.PortSet' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Binding.Ce.CeInstances.CeInstance.PortSet',
            False, 
            [
            _MetaInfoClassMember('psid', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port Set Identifier (PSID) value, which identifies a set
                of ports algorithmically.
                ''',
                'psid',
                'ietf-softwire', False),
            _MetaInfoClassMember('psid-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '15')], [], 
                '''                The length of PSID, representing the sharing ratio for an
                IPv4 address.
                ''',
                'psid_len',
                'ietf-softwire', False),
            _MetaInfoClassMember('psid-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '16')], [], 
                '''                The number of offset bits. In Lightweight 4over6, the default
                value is 0 for assigning one contiguous port range. In MAP-E/T,
                the default value is 6, which excludes system ports by default
                and assigns port ranges distribute across the entire port space.
                If the this parameter is larger than 0, the value of offset
                MUST be greater than 0.
                ''',
                'psid_offset',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'port-set',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Binding.Ce.CeInstances.CeInstance' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Binding.Ce.CeInstances.CeInstance',
            False, 
            [
            _MetaInfoClassMember('binding-ipv6info', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IPv6 information for a binding entry.
                If this is an IPv6 prefix, it indicates that
                the IPv6 source address of the lwB4 is constructed
                according to the description in RFC7596;
                if it is an IPv6 address, it means the lwB4 uses
                any /128 address from the assigned IPv6 prefix.
                
                ''',
                'binding_ipv6info',
                'ietf-softwire', True, [
                    _MetaInfoClassMember('binding-ipv6info', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IPv6 information for a binding entry.
                        If this is an IPv6 prefix, it indicates that
                        the IPv6 source address of the lwB4 is constructed
                        according to the description in RFC7596;
                        if it is an IPv6 address, it means the lwB4 uses
                        any /128 address from the assigned IPv6 prefix.
                        
                        ''',
                        'binding_ipv6info',
                        'ietf-softwire', True),
                    _MetaInfoClassMember('binding-ipv6info', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        The IPv6 information for a binding entry.
                        If this is an IPv6 prefix, it indicates that
                        the IPv6 source address of the lwB4 is constructed
                        according to the description in RFC7596;
                        if it is an IPv6 address, it means the lwB4 uses
                        any /128 address from the assigned IPv6 prefix.
                        
                        ''',
                        'binding_ipv6info',
                        'ietf-softwire', True),
                ]),
            _MetaInfoClassMember('b4-ipv6-addr-format', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The format of lwB4 (CE) IPv6 address. If set to true,
                it indicates that the IPv6 source address of the lwB4
                is constructed according to the description in
                [RFC7596]; if set to false, the lwB4 (CE)
                can use any /128 address from the assigned IPv6
                prefix.
                ''',
                'b4_ipv6_addr_format',
                'ietf-softwire', False),
            _MetaInfoClassMember('binding-ipv4-addr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv4 address assigned to the lwB4, which is
                used as the IPv4 external address
                for lwB4 local NAPT44.
                ''',
                'binding_ipv4_addr',
                'ietf-softwire', False),
            _MetaInfoClassMember('br-ipv6-addr', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv6 address for lwaftr.
                ''',
                'br_ipv6_addr',
                'ietf-softwire', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The lifetime for the binding entry
                ''',
                'lifetime',
                'ietf-softwire', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The CE's name.
                ''',
                'name',
                'ietf-softwire', False),
            _MetaInfoClassMember('port-set', REFERENCE_CLASS, 'PortSet' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Binding.Ce.CeInstances.CeInstance.PortSet', 
                [], [], 
                '''                For Lightweight 4over6, the default value
                of offset should be 0, to configure one contiguous
                port range.
                ''',
                'port_set',
                'ietf-softwire', False),
            _MetaInfoClassMember('tunnel-path-mru', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The path MRU for Lightweight 4over6 tunnel.
                ''',
                'tunnel_path_mru',
                'ietf-softwire', False),
            _MetaInfoClassMember('tunnel-payload-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The payload MTU for Lightweight 4over6 tunnel.
                ''',
                'tunnel_payload_mtu',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'ce-instance',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Binding.Ce.CeInstances' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Binding.Ce.CeInstances',
            False, 
            [
            _MetaInfoClassMember('ce-instance', REFERENCE_LIST, 'CeInstance' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Binding.Ce.CeInstances.CeInstance', 
                [], [], 
                '''                instances for CE
                ''',
                'ce_instance',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'ce-instances',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Binding.Ce' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Binding.Ce',
            False, 
            [
            _MetaInfoClassMember('ce-instances', REFERENCE_CLASS, 'CeInstances' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Binding.Ce.CeInstances', 
                [], [], 
                '''                A set of CEs to be configured.
                ''',
                'ce_instances',
                'ietf-softwire', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable the lwB4 (CE) function.
                ''',
                'enable',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'ce',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Binding' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Binding',
            False, 
            [
            _MetaInfoClassMember('br', REFERENCE_CLASS, 'Br' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Binding.Br', 
                [], [], 
                '''                Indicate this instance supports the lwAFTR (BR) function.
                The instances advertise the BR feature through the
                capability exchange mechanism when a NETCONF session is
                established.
                ''',
                'br',
                'ietf-softwire', False),
            _MetaInfoClassMember('ce', REFERENCE_CLASS, 'Ce' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Binding.Ce', 
                [], [], 
                '''                Indicate this instance supports the lwB4 (CE) function.
                The instances advertise the CE feature through the
                capability exchange mechanism when a NETCONF session is
                established.
                ''',
                'ce',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'binding',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance.AlgoVersioning' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance.AlgoVersioning',
            False, 
            [
            _MetaInfoClassMember('algo-date', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp to the algorithm
                ''',
                'algo_date',
                'ietf-softwire', False),
            _MetaInfoClassMember('algo-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Incremental version number to
                the algorithm
                ''',
                'algo_version',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'algo-versioning',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance.DataPlaneEnum' : _MetaInfoEnum('DataPlaneEnum', 'ydk.models.ietf.ietf_softwire',
        {
            'encapsulation':'encapsulation',
            'translation':'translation',
        }, 'ietf-softwire', _yang_ns._namespaces['ietf-softwire']),
    'SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Algorithm Instance ID
                ''',
                'id',
                'ietf-softwire', True),
            _MetaInfoClassMember('algo-versioning', REFERENCE_CLASS, 'AlgoVersioning' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance.AlgoVersioning', 
                [], [], 
                '''                algorithm's version
                ''',
                'algo_versioning',
                'ietf-softwire', False),
            _MetaInfoClassMember('br-ipv6-addr', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv6 address of the MAP-E BR.
                ''',
                'br_ipv6_addr',
                'ietf-softwire', False),
            _MetaInfoClassMember('data-plane', REFERENCE_ENUM_CLASS, 'DataPlaneEnum' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance.DataPlaneEnum', 
                [], [], 
                '''                Encapsulation is for MAP-E while translation is
                for MAP-T
                ''',
                'data_plane',
                'ietf-softwire', False),
            _MetaInfoClassMember('dmr-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IPv6 prefix of the MAP-T BR. 
                ''',
                'dmr_ipv6_prefix',
                'ietf-softwire', False),
            _MetaInfoClassMember('ea-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Embedded Address (EA) bits are the IPv4 EA-bits
                in the IPv6 address identify an IPv4
                prefix/address (or part thereof) or
                a shared IPv4 address (or part thereof)
                and a port-set identifier.
                The length of the EA-bits is defined as
                part of a MAP rule for a MAP domain.
                ''',
                'ea_len',
                'ietf-softwire', False),
            _MetaInfoClassMember('forwarding', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This parameter specifies whether the rule may be used for
                forwarding (FMR). If set, this rule is used as an FMR;
                if not set, this rule is a BMR only and must not be used
                for forwarding.
                ''',
                'forwarding',
                'ietf-softwire', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name for the instance.
                ''',
                'name',
                'ietf-softwire', False),
            _MetaInfoClassMember('psid-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '15')], [], 
                '''                The length of PSID, representing the sharing ratio for an
                IPv4 address.
                ''',
                'psid_len',
                'ietf-softwire', False),
            _MetaInfoClassMember('psid-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '16')], [], 
                '''                The number of offset bits. In Lightweight 4over6, the default
                value is 0 for assigning one contiguous port range. In MAP-E/T,
                the default value is 6, which excludes system ports by default
                and assigns distributed port ranges. If the this parameter is
                larger than 0, the value of offset MUST be greater than 0.
                ''',
                'psid_offset',
                'ietf-softwire', False),
            _MetaInfoClassMember('rule-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                The Rule IPv4 prefix defined in the mapping rule.
                ''',
                'rule_ipv4_prefix',
                'ietf-softwire', False),
            _MetaInfoClassMember('rule-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The Rule IPv6 prefix defined in the mapping rule.
                ''',
                'rule_ipv6_prefix',
                'ietf-softwire', False),
            _MetaInfoClassMember('tunnel-path-mru', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The path MRU for MAP-E tunnel.
                ''',
                'tunnel_path_mru',
                'ietf-softwire', False),
            _MetaInfoClassMember('tunnel-payload-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The payload MTU for MAP-E tunnel.
                ''',
                'tunnel_payload_mtu',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'algo-instance',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Algorithm.AlgoInstances' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Algorithm.AlgoInstances',
            False, 
            [
            _MetaInfoClassMember('algo-instance', REFERENCE_LIST, 'AlgoInstance' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance', 
                [], [], 
                '''                instance for MAP-E/MAP-T
                ''',
                'algo_instance',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'algo-instances',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig.Algorithm' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig.Algorithm',
            False, 
            [
            _MetaInfoClassMember('algo-instances', REFERENCE_CLASS, 'AlgoInstances' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Algorithm.AlgoInstances', 
                [], [], 
                '''                A set of MAP-E or MAP-T instances to be configured,
                applying to BRs and CEs. A MAP-E/T instance defines a MAP
                domain comprising one or more MAP-CE and MAP-BR
                ''',
                'algo_instances',
                'ietf-softwire', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable the MAP-E or MAP-T function.
                ''',
                'enable',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'algorithm',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireConfig' : {
        'meta_info' : _MetaInfoClass('SoftwireConfig',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_CLASS, 'Algorithm' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Algorithm', 
                [], [], 
                '''                Indicate the instances support the MAP-E and MAP-T function.
                The instances advertise the map-e feature through the
                capability exchange mechanism when a NETCONF session is
                established.
                ''',
                'algorithm',
                'ietf-softwire', False),
            _MetaInfoClassMember('binding', REFERENCE_CLASS, 'Binding' , 'ydk.models.ietf.ietf_softwire', 'SoftwireConfig.Binding', 
                [], [], 
                '''                lw4over6 (binding) configuration.
                ''',
                'binding',
                'ietf-softwire', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A textual description of Softwire.
                ''',
                'description',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'softwire-config',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireState.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry' : {
        'meta_info' : _MetaInfoClass('SoftwireState.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry',
            False, 
            [
            _MetaInfoClassMember('binding-ipv6info', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IPv6 information used to identify
                 a binding entry. 
                ''',
                'binding_ipv6info',
                'ietf-softwire', True, [
                    _MetaInfoClassMember('binding-ipv6info', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IPv6 information used to identify
                         a binding entry. 
                        ''',
                        'binding_ipv6info',
                        'ietf-softwire', True),
                    _MetaInfoClassMember('binding-ipv6info', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        The IPv6 information used to identify
                         a binding entry. 
                        ''',
                        'binding_ipv6info',
                        'ietf-softwire', True),
                ]),
            _MetaInfoClassMember('active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Status of a specific tunnel.
                ''',
                'active',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'binding-entry',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireState.Binding.Br.BrInstances.BrInstance.BindingTable' : {
        'meta_info' : _MetaInfoClass('SoftwireState.Binding.Br.BrInstances.BrInstance.BindingTable',
            False, 
            [
            _MetaInfoClassMember('binding-entry', REFERENCE_LIST, 'BindingEntry' , 'ydk.models.ietf.ietf_softwire', 'SoftwireState.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry', 
                [], [], 
                '''                An identifier of the binding entry.
                ''',
                'binding_entry',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'binding-table',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireState.Binding.Br.BrInstances.BrInstance' : {
        'meta_info' : _MetaInfoClass('SoftwireState.Binding.Br.BrInstances.BrInstance',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                id
                ''',
                'id',
                'ietf-softwire', True),
            _MetaInfoClassMember('active-softwire-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of currently active tunnels on the
                lw4over6 (binding) instance.
                ''',
                'active_softwire_num',
                'ietf-softwire', False),
            _MetaInfoClassMember('binding-table', REFERENCE_CLASS, 'BindingTable' , 'ydk.models.ietf.ietf_softwire', 'SoftwireState.Binding.Br.BrInstances.BrInstance.BindingTable', 
                [], [], 
                '''                id
                ''',
                'binding_table',
                'ietf-softwire', False),
            _MetaInfoClassMember('droppedByte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic dropped, in bytes
                ''',
                'droppedbyte',
                'ietf-softwire', False),
            _MetaInfoClassMember('droppedPacket', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets dropped.
                ''',
                'droppedpacket',
                'ietf-softwire', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name for this lwaftr.
                ''',
                'name',
                'ietf-softwire', False),
            _MetaInfoClassMember('rcvdByte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic received, in bytes
                ''',
                'rcvdbyte',
                'ietf-softwire', False),
            _MetaInfoClassMember('rcvdPacket', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets received.
                ''',
                'rcvdpacket',
                'ietf-softwire', False),
            _MetaInfoClassMember('sentByte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic sent, in bytes
                ''',
                'sentbyte',
                'ietf-softwire', False),
            _MetaInfoClassMember('sentPacket', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets sent.
                ''',
                'sentpacket',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'br-instance',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireState.Binding.Br.BrInstances' : {
        'meta_info' : _MetaInfoClass('SoftwireState.Binding.Br.BrInstances',
            False, 
            [
            _MetaInfoClassMember('br-instance', REFERENCE_LIST, 'BrInstance' , 'ydk.models.ietf.ietf_softwire', 'SoftwireState.Binding.Br.BrInstances.BrInstance', 
                [], [], 
                '''                instances for BR
                ''',
                'br_instance',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'br-instances',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireState.Binding.Br' : {
        'meta_info' : _MetaInfoClass('SoftwireState.Binding.Br',
            False, 
            [
            _MetaInfoClassMember('br-instances', REFERENCE_CLASS, 'BrInstances' , 'ydk.models.ietf.ietf_softwire', 'SoftwireState.Binding.Br.BrInstances', 
                [], [], 
                '''                A set of BRs.
                ''',
                'br_instances',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'br',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireState.Binding.Ce.CeInstances.CeInstance' : {
        'meta_info' : _MetaInfoClass('SoftwireState.Binding.Ce.CeInstances.CeInstance',
            False, 
            [
            _MetaInfoClassMember('binding-ipv6info', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IPv6 information used to identify
                a binding entry. 
                ''',
                'binding_ipv6info',
                'ietf-softwire', True, [
                    _MetaInfoClassMember('binding-ipv6info', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IPv6 information used to identify
                        a binding entry. 
                        ''',
                        'binding_ipv6info',
                        'ietf-softwire', True),
                    _MetaInfoClassMember('binding-ipv6info', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        The IPv6 information used to identify
                        a binding entry. 
                        ''',
                        'binding_ipv6info',
                        'ietf-softwire', True),
                ]),
            _MetaInfoClassMember('droppedByte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic dropped, in bytes
                ''',
                'droppedbyte',
                'ietf-softwire', False),
            _MetaInfoClassMember('droppedPacket', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets dropped.
                ''',
                'droppedpacket',
                'ietf-softwire', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The CE's name.
                ''',
                'name',
                'ietf-softwire', False),
            _MetaInfoClassMember('rcvdByte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic received, in bytes
                ''',
                'rcvdbyte',
                'ietf-softwire', False),
            _MetaInfoClassMember('rcvdPacket', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets received.
                ''',
                'rcvdpacket',
                'ietf-softwire', False),
            _MetaInfoClassMember('sentByte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic sent, in bytes
                ''',
                'sentbyte',
                'ietf-softwire', False),
            _MetaInfoClassMember('sentPacket', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets sent.
                ''',
                'sentpacket',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'ce-instance',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireState.Binding.Ce.CeInstances' : {
        'meta_info' : _MetaInfoClass('SoftwireState.Binding.Ce.CeInstances',
            False, 
            [
            _MetaInfoClassMember('ce-instance', REFERENCE_LIST, 'CeInstance' , 'ydk.models.ietf.ietf_softwire', 'SoftwireState.Binding.Ce.CeInstances.CeInstance', 
                [], [], 
                '''                a lwB4 (CE) instance.
                ''',
                'ce_instance',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'ce-instances',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireState.Binding.Ce' : {
        'meta_info' : _MetaInfoClass('SoftwireState.Binding.Ce',
            False, 
            [
            _MetaInfoClassMember('ce-instances', REFERENCE_CLASS, 'CeInstances' , 'ydk.models.ietf.ietf_softwire', 'SoftwireState.Binding.Ce.CeInstances', 
                [], [], 
                '''                Status of the configured CEs.
                ''',
                'ce_instances',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'ce',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireState.Binding' : {
        'meta_info' : _MetaInfoClass('SoftwireState.Binding',
            False, 
            [
            _MetaInfoClassMember('br', REFERENCE_CLASS, 'Br' , 'ydk.models.ietf.ietf_softwire', 'SoftwireState.Binding.Br', 
                [], [], 
                '''                Indicate this instance supports the lwAFTR (BR) function.
                The instances advertise the lwaftr (BR) feature through the
                capability exchange mechanism when a NETCONF session is
                established.
                ''',
                'br',
                'ietf-softwire', False),
            _MetaInfoClassMember('ce', REFERENCE_CLASS, 'Ce' , 'ydk.models.ietf.ietf_softwire', 'SoftwireState.Binding.Ce', 
                [], [], 
                '''                Indicate this instance supports the lwB4 (CE) function.
                The instances advertise the lwb4 (CE) feature through the
                capability exchange mechanism when a NETCONF session is
                established.
                ''',
                'ce',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'binding',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireState.Algorithm.AlgoInstances.AlgoInstance' : {
        'meta_info' : _MetaInfoClass('SoftwireState.Algorithm.AlgoInstances.AlgoInstance',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                id
                ''',
                'id',
                'ietf-softwire', True),
            _MetaInfoClassMember('droppedByte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic dropped, in bytes
                ''',
                'droppedbyte',
                'ietf-softwire', False),
            _MetaInfoClassMember('droppedPacket', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets dropped.
                ''',
                'droppedpacket',
                'ietf-softwire', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The map-e instance name.
                ''',
                'name',
                'ietf-softwire', False),
            _MetaInfoClassMember('rcvdByte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic received, in bytes
                ''',
                'rcvdbyte',
                'ietf-softwire', False),
            _MetaInfoClassMember('rcvdPacket', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets received.
                ''',
                'rcvdpacket',
                'ietf-softwire', False),
            _MetaInfoClassMember('sentByte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic sent, in bytes
                ''',
                'sentbyte',
                'ietf-softwire', False),
            _MetaInfoClassMember('sentPacket', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets sent.
                ''',
                'sentpacket',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'algo-instance',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireState.Algorithm.AlgoInstances' : {
        'meta_info' : _MetaInfoClass('SoftwireState.Algorithm.AlgoInstances',
            False, 
            [
            _MetaInfoClassMember('algo-instance', REFERENCE_LIST, 'AlgoInstance' , 'ydk.models.ietf.ietf_softwire', 'SoftwireState.Algorithm.AlgoInstances.AlgoInstance', 
                [], [], 
                '''                Instances for algorithm
                ''',
                'algo_instance',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'algo-instances',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireState.Algorithm' : {
        'meta_info' : _MetaInfoClass('SoftwireState.Algorithm',
            False, 
            [
            _MetaInfoClassMember('algo-instances', REFERENCE_CLASS, 'AlgoInstances' , 'ydk.models.ietf.ietf_softwire', 'SoftwireState.Algorithm.AlgoInstances', 
                [], [], 
                '''                Status of MAP-E instance(s).
                ''',
                'algo_instances',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'algorithm',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
    'SoftwireState' : {
        'meta_info' : _MetaInfoClass('SoftwireState',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_CLASS, 'Algorithm' , 'ydk.models.ietf.ietf_softwire', 'SoftwireState.Algorithm', 
                [], [], 
                '''                Indicate the instances support the MAP-E and MAP-T function.
                The instances advertise the map-e/map-t feature through the
                capability exchange mechanism when a NETCONF session is
                established.
                ''',
                'algorithm',
                'ietf-softwire', False),
            _MetaInfoClassMember('binding', REFERENCE_CLASS, 'Binding' , 'ydk.models.ietf.ietf_softwire', 'SoftwireState.Binding', 
                [], [], 
                '''                lw4over6 (binding) state.
                ''',
                'binding',
                'ietf-softwire', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A textual description of the softwire instances.
                ''',
                'description',
                'ietf-softwire', False),
            ],
            'ietf-softwire',
            'softwire-state',
            _yang_ns._namespaces['ietf-softwire'],
        'ydk.models.ietf.ietf_softwire'
        ),
    },
}
_meta_table['SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry.PortSet']['meta_info'].parent =_meta_table['SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry']['meta_info']
_meta_table['SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry']['meta_info'].parent =_meta_table['SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable']['meta_info']
_meta_table['SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTableVersion']['meta_info'].parent =_meta_table['SoftwireConfig.Binding.Br.BrInstances.BrInstance']['meta_info']
_meta_table['SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable']['meta_info'].parent =_meta_table['SoftwireConfig.Binding.Br.BrInstances.BrInstance']['meta_info']
_meta_table['SoftwireConfig.Binding.Br.BrInstances.BrInstance']['meta_info'].parent =_meta_table['SoftwireConfig.Binding.Br.BrInstances']['meta_info']
_meta_table['SoftwireConfig.Binding.Br.BrInstances']['meta_info'].parent =_meta_table['SoftwireConfig.Binding.Br']['meta_info']
_meta_table['SoftwireConfig.Binding.Ce.CeInstances.CeInstance.PortSet']['meta_info'].parent =_meta_table['SoftwireConfig.Binding.Ce.CeInstances.CeInstance']['meta_info']
_meta_table['SoftwireConfig.Binding.Ce.CeInstances.CeInstance']['meta_info'].parent =_meta_table['SoftwireConfig.Binding.Ce.CeInstances']['meta_info']
_meta_table['SoftwireConfig.Binding.Ce.CeInstances']['meta_info'].parent =_meta_table['SoftwireConfig.Binding.Ce']['meta_info']
_meta_table['SoftwireConfig.Binding.Br']['meta_info'].parent =_meta_table['SoftwireConfig.Binding']['meta_info']
_meta_table['SoftwireConfig.Binding.Ce']['meta_info'].parent =_meta_table['SoftwireConfig.Binding']['meta_info']
_meta_table['SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance.AlgoVersioning']['meta_info'].parent =_meta_table['SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance']['meta_info']
_meta_table['SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance']['meta_info'].parent =_meta_table['SoftwireConfig.Algorithm.AlgoInstances']['meta_info']
_meta_table['SoftwireConfig.Algorithm.AlgoInstances']['meta_info'].parent =_meta_table['SoftwireConfig.Algorithm']['meta_info']
_meta_table['SoftwireConfig.Binding']['meta_info'].parent =_meta_table['SoftwireConfig']['meta_info']
_meta_table['SoftwireConfig.Algorithm']['meta_info'].parent =_meta_table['SoftwireConfig']['meta_info']
_meta_table['SoftwireState.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry']['meta_info'].parent =_meta_table['SoftwireState.Binding.Br.BrInstances.BrInstance.BindingTable']['meta_info']
_meta_table['SoftwireState.Binding.Br.BrInstances.BrInstance.BindingTable']['meta_info'].parent =_meta_table['SoftwireState.Binding.Br.BrInstances.BrInstance']['meta_info']
_meta_table['SoftwireState.Binding.Br.BrInstances.BrInstance']['meta_info'].parent =_meta_table['SoftwireState.Binding.Br.BrInstances']['meta_info']
_meta_table['SoftwireState.Binding.Br.BrInstances']['meta_info'].parent =_meta_table['SoftwireState.Binding.Br']['meta_info']
_meta_table['SoftwireState.Binding.Ce.CeInstances.CeInstance']['meta_info'].parent =_meta_table['SoftwireState.Binding.Ce.CeInstances']['meta_info']
_meta_table['SoftwireState.Binding.Ce.CeInstances']['meta_info'].parent =_meta_table['SoftwireState.Binding.Ce']['meta_info']
_meta_table['SoftwireState.Binding.Br']['meta_info'].parent =_meta_table['SoftwireState.Binding']['meta_info']
_meta_table['SoftwireState.Binding.Ce']['meta_info'].parent =_meta_table['SoftwireState.Binding']['meta_info']
_meta_table['SoftwireState.Algorithm.AlgoInstances.AlgoInstance']['meta_info'].parent =_meta_table['SoftwireState.Algorithm.AlgoInstances']['meta_info']
_meta_table['SoftwireState.Algorithm.AlgoInstances']['meta_info'].parent =_meta_table['SoftwireState.Algorithm']['meta_info']
_meta_table['SoftwireState.Binding']['meta_info'].parent =_meta_table['SoftwireState']['meta_info']
_meta_table['SoftwireState.Algorithm']['meta_info'].parent =_meta_table['SoftwireState']['meta_info']
