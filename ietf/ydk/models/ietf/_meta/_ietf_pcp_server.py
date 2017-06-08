


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.Version' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.Version',
            False, 
            [
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Indicates a PCP server.
                 Current versions are: 0, 1, and 2.
                ''',
                'version',
                'ietf-pcp-server', True),
            ],
            'ietf-pcp-server',
            'version',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.PcpServerIpAddress' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.PcpServerIpAddress',
            False, 
            [
            _MetaInfoClassMember('address-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The identifier of the address
                ''',
                'address_id',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IP (v4/v6) address of the PCP server
                ''',
                'ip_address',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'pcp-server-ip-address',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.OpcodeConfiguration' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.OpcodeConfiguration',
            False, 
            [
            _MetaInfoClassMember('announce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ANNOUNCE opcode.
                ''',
                'announce',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('map', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MAP opcode
                ''',
                'map',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('peer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PEER opcode
                ''',
                'peer',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'opcode-configuration',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Filter' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable FILTER option.
                ''',
                'filter_enabled',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('max-filters', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum number of filters
                 associated with a mapping.
                ''',
                'max_filters',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'filter',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.PortSetOption' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.PortSetOption',
            False, 
            [
            _MetaInfoClassMember('default-port-set-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Indicates the default size of a port set.
                ''',
                'default_port_set_size',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('maximum-port-set-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Indicates the maximum size of a port set.
                ''',
                'maximum_port_set_size',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-set-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable PORT_SET option.
                ''',
                'port_set_enable',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'port-set-option',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Description' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Description',
            False, 
            [
            _MetaInfoClassMember('description-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable DESCRIPTION option.
                ''',
                'description_enabled',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('max-description', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum length of the description
                 associated with a mapping.
                ''',
                'max_description',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'description',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64.DestIpv4Prefix' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64.DestIpv4Prefix',
            False, 
            [
            _MetaInfoClassMember('ipv4-prefix-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of a destination IPv4 prefix
                ''',
                'ipv4_prefix_id',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                an IPv4 prefix.
                ''',
                'ipv4_prefix',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'dest-ipv4-prefix',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64',
            False, 
            [
            _MetaInfoClassMember('prefix64-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of a Prefix64.
                ''',
                'prefix64_id',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('dest-ipv4-prefix', REFERENCE_LIST, 'DestIpv4Prefix' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64.DestIpv4Prefix', 
                [], [], 
                '''                used to solve the destination-dependent
                 Pref64::/n discovery problem discussed in
                 Section 5.1 of [RFC7050].
                ''',
                'dest_ipv4_prefix',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('prefix64', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                A Prefix64
                ''',
                'prefix64',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('suffix', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The suffix is used for constructing an
                 IPv4-converted IPv6 address from an IPv4 address as
                 specified in Section 2.2 of [RFC6052]. No suffix is
                 included if a /96 Prefix64 is used.
                ''',
                'suffix',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'prefix64',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option',
            False, 
            [
            _MetaInfoClassMember('prefix64', REFERENCE_LIST, 'Prefix64' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64', 
                [], [], 
                '''                maintains a list of Prefix64s.
                ''',
                'prefix64',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('prefix64-option-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the option is enabled/disabled.
                ''',
                'prefix64_option_enable',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'prefix64-option',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration',
            False, 
            [
            _MetaInfoClassMember('description', REFERENCE_CLASS, 'Description' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Description', 
                [], [], 
                '''                enable/disable DESCRIPTION option.
                ''',
                'description',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('filter', REFERENCE_CLASS, 'Filter' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Filter', 
                [], [], 
                '''                enable/disable FILTER option.
                ''',
                'filter',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-set-option', REFERENCE_CLASS, 'PortSetOption' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.PortSetOption', 
                [], [], 
                '''                enable/disable PORT_SET option.
                ''',
                'port_set_option',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('prefer-failure', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enable/disable PREFER_FAILURE option.
                ''',
                'prefer_failure',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('prefix64-option', REFERENCE_CLASS, 'Prefix64Option' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option', 
                [], [], 
                '''                enable/disable PREFIX64 option.
                ''',
                'prefix64_option',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('third-party', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enable/disable THIRD_PARTY option.
                ''',
                'third_party',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'option-configuration',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.ExcludePorts' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.ExcludePorts',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                An identifier
                ''',
                'id',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'exclude-ports',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.Protocol' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.Protocol',
            False, 
            [
            _MetaInfoClassMember('protocol-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                identifier of the protocol
                ''',
                'protocol_id',
                'ietf-pcp-server', True),
            ],
            'ietf-pcp-server',
            'protocol',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.Lifetime' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.Lifetime',
            False, 
            [
            _MetaInfoClassMember('maximum-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum lifetime.
                ''',
                'maximum_lifetime',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('minimum-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum lifetime.
                ''',
                'minimum_lifetime',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'lifetime',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.ErrorLifetime' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.ErrorLifetime',
            False, 
            [
            _MetaInfoClassMember('maximum-error-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum error lifetime, in seconds.
                
                [RFC6877] recommends that long lifetime
                errors use a 30-minute lifetime.
                ''',
                'maximum_error_lifetime',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('minimum-error-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum error lifetime, in seconds.
                
                [RFC6877] recommends that short lifetime
                errors use a 30-second lifetime.
                ''',
                'minimum_error_lifetime',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'error-lifetime',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.InternalPort' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.InternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'internal-port',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.ExternalPort' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.ExternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'external-port',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.Filter' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of the filter.
                ''',
                'filter_id',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('remote-ip-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IP address of the remote peer.
                ''',
                'remote_ip_prefix',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('remote-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The port number of the remote peer. Value 0
                indicates 'all ports'.
                ''',
                'remote_port_number',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'filter',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.ietf.ietf_pcp_server',
        {
            'disabled':'disabled',
            'requested':'requested',
            'assigned':'assigned',
            'stale':'stale',
        }, 'ietf-pcp', _yang_ns._namespaces['ietf-pcp']),
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique identifier of a mapping entry.
                ''',
                'index',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                a description string associated with the mapping.
                ''',
                'description',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('external-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                External IP address. Can be 'Suggested' or 'Assigned'.
                
                It can be set by a client to stale-ip-address, if available
                or to (::) (for requesting external IPv6 addresses)
                or (::ffff:0:0) (for requesting external IPv4 addresses).
                ''',
                'external_ip_address',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('external-port', REFERENCE_CLASS, 'ExternalPort' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.ExternalPort', 
                [], [], 
                '''                External port number. Can be 'Suggested' or 'Assigned'.
                ''',
                'external_port',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('filter', REFERENCE_LIST, 'Filter' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.Filter', 
                [], [], 
                '''                a list of filters associated with the mapping.
                ''',
                'filter',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('internal-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Corresponds to the PCP Client's IP Address
                defined in [RFC6887].
                ''',
                'internal_ip_address',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('internal-port', REFERENCE_CLASS, 'InternalPort' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.InternalPort', 
                [], [], 
                '''                Internal port for the mapping. Value 0 indicates
                'all ports', and is legal when the lifetime is zero
                (a delete request), if the protocol does not use
                16-bit port numbers, or the client is requesting
                'all ports'.  If the protocol is zero
                (meaning 'all protocols'), then internal port
                is set to zero.
                ''',
                'internal_port',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lifetime of the mapping.
                 Can be requested/assigned/remaining
                ''',
                'lifetime',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('mapping-nonce', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A random value chosen by the PCP client
                ''',
                'mapping_nonce',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('prefer-failure-tagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                a tag which indicates whether PREFER_FAILURE
                 is (to be) used.
                ''',
                'prefer_failure_tagged',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Upper-layer protocol associated with this Opcode.
                Values are taken from the IANA protocol registry.
                For example, this field contains 6 (TCP) if the Opcode
                is intended to create a TCP mapping.  This field contains
                17 (UDP) if the Opcode is intended to create a UDP mapping.
                The value 0 has a special meaning for 'all protocols'.
                ''',
                'protocol',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.StatusEnum', 
                [], [], 
                '''                Indicates the status of a mapping entry.
                ''',
                'status',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('third-party-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                used to indicate the internal IP address
                 when THIRD_PARTY is in use.
                ''',
                'third_party_address',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'mapping-entry',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable',
            False, 
            [
            _MetaInfoClassMember('mapping-entry', REFERENCE_LIST, 'MappingEntry' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry', 
                [], [], 
                '''                PCP mapping entry
                ''',
                'mapping_entry',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'mapping-table',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances.PcpServerInstance' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances.PcpServerInstance',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PCP server instance identifier.
                ''',
                'id',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('authentication-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable PCP authentication
                ''',
                'authentication_enable',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('epoch-set', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Set the Epoch parameter.
                ''',
                'epoch_set',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('error-lifetime', REFERENCE_CLASS, 'ErrorLifetime' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.ErrorLifetime', 
                [], [], 
                '''                Configure values for the error lifetime to be
                returned to requesting PCP clients.
                ''',
                'error_lifetime',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('exclude-ports', REFERENCE_LIST, 'ExcludePorts' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.ExcludePorts', 
                [], [], 
                '''                The set of ports not to be assigned
                 by the server.
                ''',
                'exclude_ports',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('lifetime', REFERENCE_CLASS, 'Lifetime' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.Lifetime', 
                [], [], 
                '''                Configure values for the lifetime to be
                assigned to requesting PCP clients.
                
                The client requests a certain lifetime, and the server
                responds with the assigned lifetime.
                
                The server may grant a lifetime smaller or larger than
                the requested lifetime.
                
                The minimum value should be 120 seconds.
                
                The maximum value should be the remaining
                lifetime of the IP address assigned to
                the PCP client if that information is available,
                or half the lifetime of IP address
                assignments, or 24 hours.
                
                Excessively long lifetimes can cause consumption
                of ports even if the internal host is no longer
                interested in receiving the traffic or is no
                longer connected to the network.
                (Section 15 [RFC6877].
                ''',
                'lifetime',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('mapping-table', REFERENCE_CLASS, 'MappingTable' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable', 
                [], [], 
                '''                PCP mapping table as maintained by
                 the PCP server
                ''',
                'mapping_table',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A name associated with the PCP server instance
                ''',
                'name',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('nonce-validation-checks-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the PCP server has to
                 disable/enable Nonce validation checks.
                ''',
                'nonce_validation_checks_enable',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('opcode-configuration', REFERENCE_CLASS, 'OpcodeConfiguration' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.OpcodeConfiguration', 
                [], [], 
                '''                Opcode-related configuration
                ''',
                'opcode_configuration',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('option-configuration', REFERENCE_CLASS, 'OptionConfiguration' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration', 
                [], [], 
                '''                Option-related configuration
                ''',
                'option_configuration',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('pcp-server-ip-address', REFERENCE_LIST, 'PcpServerIpAddress' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.PcpServerIpAddress', 
                [], [], 
                '''                set one or multiple IP addresses for
                the PCP server
                ''',
                'pcp_server_ip_address',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-parity-preservation-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the PCP server should
                 preserve the port parity of the
                 internal port number.
                ''',
                'port_parity_preservation_enable',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-preservation-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the PCP server should
                 preserve the internal port number.
                ''',
                'port_preservation_enable',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                configure a port quota to be assigned per
                 PCP client/subscriber.
                ''',
                'port_quota',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-randomization-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable port randomization
                 feature.
                ''',
                'port_randomization_enable',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('protocol', REFERENCE_LIST, 'Protocol' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.Protocol', 
                [], [], 
                '''                set of protocols supported by
                 the PCP-controlled function.
                ''',
                'protocol',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('subscriber-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                The subscriber-mask is an integer that indicates
                the length of significant bits to be applied on
                the source IPv6 address (internal side) to
                identify unambiguously a CPE.
                
                Subscriber-mask is a system-wide configuration
                parameter that is used to enforce generic per-subscriber
                policies (e.g., port-quota).
                
                Applying these generic policies does not require
                configuring every subscriber's prefix.
                
                Example: suppose the 2001:db8:100:100::/56 prefix is
                assigned to a DS-Lite enabled CPE. Suppose also that the
                2001:db8:100:100::1 is the IPv6 address used by the
                client that resides in that CPE. When the server
                receives a packet from this client,
                the server applies the subscriber-mask (e.g., 56) on
                the source IPv6 address to compute the associated prefix
                for this client (that is 2001:db8:100:100::/56).  Then,
                the server enforces policies based on that prefix
                (2001:db8:100:100::/56), not on the exact
                source IPv6 address.
                ''',
                'subscriber_mask',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('version', REFERENCE_LIST, 'Version' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance.Version', 
                [], [], 
                '''                Indicates the PCP version(s) supported by the
                 PCP server.
                 Current supported versions are 0, 1, and 2.
                ''',
                'version',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'pcp-server-instance',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig.PcpServerInstances' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig.PcpServerInstances',
            False, 
            [
            _MetaInfoClassMember('pcp-server-instance', REFERENCE_LIST, 'PcpServerInstance' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances.PcpServerInstance', 
                [], [], 
                '''                a PCP server instance.
                ''',
                'pcp_server_instance',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'pcp-server-instances',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerConfig' : {
        'meta_info' : _MetaInfoClass('PcpServerConfig',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable PCP server function.
                ''',
                'enable',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('pcp-server-instances', REFERENCE_CLASS, 'PcpServerInstances' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerConfig.PcpServerInstances', 
                [], [], 
                '''                PCP server instances
                ''',
                'pcp_server_instances',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'pcp-server-config',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.SupportedVersion' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.SupportedVersion',
            False, 
            [
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Indicates a PCP server.
                 Current versions are: 0, 1, and 2.
                ''',
                'version',
                'ietf-pcp-server', True),
            ],
            'ietf-pcp-server',
            'supported-version',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.ConfiguredPcpServerIpAddress' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.ConfiguredPcpServerIpAddress',
            False, 
            [
            _MetaInfoClassMember('address-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The identifier of the address
                ''',
                'address_id',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the PCP server
                ''',
                'ip_address',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'configured-pcp-server-ip-address',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.ExternalIpAddressPool' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.ExternalIpAddressPool',
            False, 
            [
            _MetaInfoClassMember('address-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier
                ''',
                'address_id',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('external-ip-pool', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                An address or prefix
                ''',
                'external_ip_pool',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'external-ip-address-pool',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.OpcodeCapability' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.OpcodeCapability',
            False, 
            [
            _MetaInfoClassMember('announce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ANNOUNCE opcode.
                ''',
                'announce',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('map', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MAP opcode
                ''',
                'map',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('peer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PEER opcode
                ''',
                'peer',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'opcode-capability',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability.Filter' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable FILTER option.
                ''',
                'filter_enabled',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('max-filters', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum number of filters
                 associated with a mapping.
                ''',
                'max_filters',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'filter',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability.Description' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability.Description',
            False, 
            [
            _MetaInfoClassMember('description-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable DESCRIPTION option.
                ''',
                'description_enabled',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('max-description', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum length of the description
                 associated with a mapping.
                ''',
                'max_description',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'description',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability',
            False, 
            [
            _MetaInfoClassMember('description', REFERENCE_CLASS, 'Description' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability.Description', 
                [], [], 
                '''                Associates a description with a mapping [RFC7220].
                ''',
                'description',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('filter', REFERENCE_CLASS, 'Filter' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability.Filter', 
                [], [], 
                '''                This option indicates that filtering incoming packets
                is desired.
                ''',
                'filter',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether PORT_SET is supported/enabled.
                ''',
                'port_set',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('prefer-failure', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This option indicates that if the PCP server is unable
                to map both the suggested external port and suggested
                external address, the PCP server should not create
                a mapping.  This differs from the behavior without this
                option, which is to create a mapping.
                
                PREFER_FAILURE is never necessary for a PCP client to
                manage mappings for itself, and its use causes
                additional work in the PCP client and in the PCP
                server. See Section 13.2 of [RFC6887].
                ''',
                'prefer_failure',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('prefix64', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PREFIX64 PCP option [RFC7225].
                ''',
                'prefix64',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('third-party', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                THIRD_PARTY option is used when a PCP client wants
                 to control a mapping to an internal host other
                 than itself [RFC6887].
                ''',
                'third_party',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'option-capability',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.ProtocolCapabilities' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.ProtocolCapabilities',
            False, 
            [
            _MetaInfoClassMember('protocol-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                transport protocol
                ''',
                'protocol_id',
                'ietf-pcp-server', True),
            ],
            'ietf-pcp-server',
            'protocol-capabilities',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.PcpControlledFunctionCapability' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.PcpControlledFunctionCapability',
            False, 
            [
            _MetaInfoClassMember('ds-lite', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                DS-Lite
                ''',
                'ds_lite',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('ipv4-firewall', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IPv4 firewall
                ''',
                'ipv4_firewall',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('ipv6-firewall', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IPv6 firewall
                ''',
                'ipv6_firewall',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('nat44', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                NAT44
                ''',
                'nat44',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('nat64', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                NAT64
                ''',
                'nat64',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('nptv6', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                NPTv6
                ''',
                'nptv6',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-range-router', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Port Range Router
                ''',
                'port_range_router',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'pcp-controlled-function-capability',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.OpcodeConfiguration' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.OpcodeConfiguration',
            False, 
            [
            _MetaInfoClassMember('announce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ANNOUNCE opcode.
                ''',
                'announce',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('map', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MAP opcode
                ''',
                'map',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('peer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PEER opcode
                ''',
                'peer',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'opcode-configuration',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Filter' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable FILTER option.
                ''',
                'filter_enabled',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('max-filters', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum number of filters
                 associated with a mapping.
                ''',
                'max_filters',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'filter',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.PortSetOption' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.PortSetOption',
            False, 
            [
            _MetaInfoClassMember('default-port-set-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Indicates the default size of a port set.
                ''',
                'default_port_set_size',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('maximum-port-set-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Indicates the maximum size of a port set.
                ''',
                'maximum_port_set_size',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-set-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable PORT_SET option.
                ''',
                'port_set_enable',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'port-set-option',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Description' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Description',
            False, 
            [
            _MetaInfoClassMember('description-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable DESCRIPTION option.
                ''',
                'description_enabled',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('max-description', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum length of the description
                 associated with a mapping.
                ''',
                'max_description',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'description',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64.DestIpv4Prefix' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64.DestIpv4Prefix',
            False, 
            [
            _MetaInfoClassMember('ipv4-prefix-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of a destination IPv4 prefix
                ''',
                'ipv4_prefix_id',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                an IPv4 prefix.
                ''',
                'ipv4_prefix',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'dest-ipv4-prefix',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64',
            False, 
            [
            _MetaInfoClassMember('prefix64-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of a Prefix64.
                ''',
                'prefix64_id',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('dest-ipv4-prefix', REFERENCE_LIST, 'DestIpv4Prefix' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64.DestIpv4Prefix', 
                [], [], 
                '''                used to solve the destination-dependent
                 Pref64::/n discovery problem discussed in
                 Section 5.1 of [RFC7050].
                ''',
                'dest_ipv4_prefix',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('prefix64', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                A Prefix64
                ''',
                'prefix64',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('suffix', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The suffix is used for constructing an
                 IPv4-converted IPv6 address from an IPv4 address as
                 specified in Section 2.2 of [RFC6052]. No suffix is
                 included if a /96 Prefix64 is used.
                ''',
                'suffix',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'prefix64',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option',
            False, 
            [
            _MetaInfoClassMember('prefix64', REFERENCE_LIST, 'Prefix64' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64', 
                [], [], 
                '''                maintains a list of Prefix64s.
                ''',
                'prefix64',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('prefix64-option-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether the option is enabled/disabled.
                ''',
                'prefix64_option_enable',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'prefix64-option',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration',
            False, 
            [
            _MetaInfoClassMember('description', REFERENCE_CLASS, 'Description' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Description', 
                [], [], 
                '''                enable/disable DESCRIPTION option.
                ''',
                'description',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('filter', REFERENCE_CLASS, 'Filter' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Filter', 
                [], [], 
                '''                enable/disable FILTER option.
                ''',
                'filter',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-set-option', REFERENCE_CLASS, 'PortSetOption' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.PortSetOption', 
                [], [], 
                '''                enable/disable PORT_SET option.
                ''',
                'port_set_option',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('prefer-failure', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enable/disable PREFER_FAILURE option.
                ''',
                'prefer_failure',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('prefix64-option', REFERENCE_CLASS, 'Prefix64Option' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option', 
                [], [], 
                '''                enable/disable PREFIX64 option.
                ''',
                'prefix64_option',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('third-party', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enable/disable THIRD_PARTY option.
                ''',
                'third_party',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'option-configuration',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.EnabledProtocol' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.EnabledProtocol',
            False, 
            [
            _MetaInfoClassMember('protocol-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                A transport protocol
                ''',
                'protocol_id',
                'ietf-pcp-server', True),
            ],
            'ietf-pcp-server',
            'enabled-protocol',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.ExcludePorts' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.ExcludePorts',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                identifier
                ''',
                'id',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'exclude-ports',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.Lifetime' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.Lifetime',
            False, 
            [
            _MetaInfoClassMember('maximum-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                configured maximum-lifetime
                ''',
                'maximum_lifetime',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('minimum-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                configured minimum lifetime
                ''',
                'minimum_lifetime',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'lifetime',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.ErrorLifetime' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.ErrorLifetime',
            False, 
            [
            _MetaInfoClassMember('maximum-error-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured maximum error lifetime,
                in seconds.
                ''',
                'maximum_error_lifetime',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('minimum-error-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured minimum error lifetime,
                in seconds.
                ''',
                'minimum_error_lifetime',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'error-lifetime',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.InternalPort' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.InternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'internal-port',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.ExternalPort' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.ExternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'external-port',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.Filter' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of the filter.
                ''',
                'filter_id',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('remote-ip-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IP address of the remote peer.
                ''',
                'remote_ip_prefix',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('remote-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The port number of the remote peer. Value 0
                indicates 'all ports'.
                ''',
                'remote_port_number',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'filter',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.StatusCodeEnum' : _MetaInfoEnum('StatusCodeEnum', 'ydk.models.ietf.ietf_pcp_server',
        {
            'SUCCESS':'SUCCESS',
            'unsupported-version':'unsupported_version',
            'not-authorized':'not_authorized',
            'malformed-request':'malformed_request',
            'unsupported-opcode':'unsupported_opcode',
            'unsupported-option':'unsupported_option',
            'malformed-option':'malformed_option',
            'network-failure':'network_failure',
            'no-resources':'no_resources',
            'unsupported-protocol':'unsupported_protocol',
            'ex-quota':'ex_quota',
            'cannot-provide-external':'cannot_provide_external',
            'address-mismatch':'address_mismatch',
            'extensive-remote-peer':'extensive_remote_peer',
        }, 'ietf-pcp', _yang_ns._namespaces['ietf-pcp']),
    'PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.ietf.ietf_pcp_server',
        {
            'disabled':'disabled',
            'requested':'requested',
            'assigned':'assigned',
            'stale':'stale',
        }, 'ietf-pcp', _yang_ns._namespaces['ietf-pcp']),
    'PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique identifier of a mapping entry.
                ''',
                'index',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                a description string associated with the mapping.
                ''',
                'description',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('external-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                External IP address. Can be 'Suggested' or 'Assigned'.
                
                It can be set by a client to stale-ip-address, if available
                or to (::) (for requesting external IPv6 addresses)
                or (::ffff:0:0) (for requesting external IPv4 addresses).
                ''',
                'external_ip_address',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('external-port', REFERENCE_CLASS, 'ExternalPort' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.ExternalPort', 
                [], [], 
                '''                External port number. Can be 'Suggested' or 'Assigned'.
                ''',
                'external_port',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('filter', REFERENCE_LIST, 'Filter' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.Filter', 
                [], [], 
                '''                a list of filters associated with the mapping.
                ''',
                'filter',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('internal-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Corresponds to the PCP Client's IP Address
                defined in [RFC6887].
                ''',
                'internal_ip_address',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('internal-port', REFERENCE_CLASS, 'InternalPort' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.InternalPort', 
                [], [], 
                '''                Internal port for the mapping. Value 0 indicates
                'all ports', and is legal when the lifetime is zero
                (a delete request), if the protocol does not use
                16-bit port numbers, or the client is requesting
                'all ports'.  If the protocol is zero
                (meaning 'all protocols'), then internal port
                is set to zero.
                ''',
                'internal_port',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lifetime of the mapping.
                 Can be requested/assigned/remaining
                ''',
                'lifetime',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('mapping-nonce', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A random value chosen by the PCP client
                ''',
                'mapping_nonce',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('prefer-failure-tagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                a tag which indicates whether PREFER_FAILURE
                 is (to be) used.
                ''',
                'prefer_failure_tagged',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Upper-layer protocol associated with this Opcode.
                Values are taken from the IANA protocol registry.
                For example, this field contains 6 (TCP) if the Opcode
                is intended to create a TCP mapping.  This field contains
                17 (UDP) if the Opcode is intended to create a UDP mapping.
                The value 0 has a special meaning for 'all protocols'.
                ''',
                'protocol',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.StatusEnum', 
                [], [], 
                '''                Indicates the status of a mapping entry.
                ''',
                'status',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('status-code', REFERENCE_ENUM_CLASS, 'StatusCodeEnum' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.StatusCodeEnum', 
                [], [], 
                '''                result status code.
                ''',
                'status_code',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('third-party-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                used to indicate the internal IP address
                 when THIRD_PARTY is in use.
                ''',
                'third_party_address',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'mapping-entry',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable',
            False, 
            [
            _MetaInfoClassMember('mapping-entry', REFERENCE_LIST, 'MappingEntry' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry', 
                [], [], 
                '''                mapping entry
                ''',
                'mapping_entry',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'mapping-table',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.TrafficStatistics_' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.TrafficStatistics_',
            False, 
            [
            _MetaInfoClassMember('dropped-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for dropped traffic in bytes.
                ''',
                'dropped_byte',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('dropped-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for dropped packets.
                ''',
                'dropped_packet',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('rcvd-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received traffic in bytes.
                ''',
                'rcvd_byte',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('rcvd-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received packets.
                ''',
                'rcvd_packet',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('sent-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent traffic in bytes.
                ''',
                'sent_byte',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('sent-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets sent
                ''',
                'sent_packet',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'traffic-statistics',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.OpcodeStatistics' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.OpcodeStatistics',
            False, 
            [
            _MetaInfoClassMember('rcvd-announce', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received ANNOUNCED messages
                ''',
                'rcvd_announce',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('rcvd-malformed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received malformed opcodes
                ''',
                'rcvd_malformed',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('rcvd-map', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received MAP messages
                ''',
                'rcvd_map',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('rcvd-peer', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received PEER messages
                ''',
                'rcvd_peer',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('rcvd-unknown', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received unknown opcodes
                ''',
                'rcvd_unknown',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('sent-annonce', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent ANNOUNCE messages
                ''',
                'sent_annonce',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('sent-map', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent MAP messages
                ''',
                'sent_map',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('sent-peer', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent PEER messages
                ''',
                'sent_peer',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'opcode-statistics',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.MappingTable' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.MappingTable',
            False, 
            [
            _MetaInfoClassMember('current-mt-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Size of the mapping table
                ''',
                'current_mt_size',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('max-mt-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum configured size of the mapping table.
                ''',
                'max_mt_size',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'mapping-table',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics',
            False, 
            [
            _MetaInfoClassMember('mapping-table', REFERENCE_CLASS, 'MappingTable' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.MappingTable', 
                [], [], 
                '''                mapping table statistics
                ''',
                'mapping_table',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('opcode-statistics', REFERENCE_CLASS, 'OpcodeStatistics' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.OpcodeStatistics', 
                [], [], 
                '''                Opcode-related statistics.
                ''',
                'opcode_statistics',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-in-use', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                ratio of the port usage.
                ''',
                'port_in_use',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('traffic-statistics', REFERENCE_CLASS, 'TrafficStatistics_' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.TrafficStatistics_', 
                [], [], 
                '''                Generic traffic statistics.
                ''',
                'traffic_statistics',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'traffic-statistics',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances.PcpServerInstance' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances.PcpServerInstance',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The identifier of the PCP server instance.
                ''',
                'id',
                'ietf-pcp-server', True),
            _MetaInfoClassMember('authentication-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether PCP authentication
                 is enabled/disabled
                ''',
                'authentication_enabled',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('authentication-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Status of the support of PCP authentication
                ''',
                'authentication_support',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('configured-pcp-server-ip-address', REFERENCE_LIST, 'ConfiguredPcpServerIpAddress' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.ConfiguredPcpServerIpAddress', 
                [], [], 
                '''                List of PCP server IP addresses
                ''',
                'configured_pcp_server_ip_address',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('enabled-protocol', REFERENCE_LIST, 'EnabledProtocol' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.EnabledProtocol', 
                [], [], 
                '''                Indicates the set of enabled transport protocols.
                ''',
                'enabled_protocol',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('epoch', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                value of the current server's epoch.
                ''',
                'epoch',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('error-lifetime', REFERENCE_CLASS, 'ErrorLifetime' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.ErrorLifetime', 
                [], [], 
                '''                Vvalues for the error lifetime to be
                returned to requesting PCP clients.
                ''',
                'error_lifetime',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('exclude-ports', REFERENCE_LIST, 'ExcludePorts' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.ExcludePorts', 
                [], [], 
                '''                Indicates ports that are excluded from
                 dynamic assignment.
                ''',
                'exclude_ports',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('external-ip-address-pool', REFERENCE_LIST, 'ExternalIpAddressPool' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.ExternalIpAddressPool', 
                [], [], 
                '''                Pool of external IP addresses used to service
                requesting clients.
                ''',
                'external_ip_address_pool',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('lifetime', REFERENCE_CLASS, 'Lifetime' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.Lifetime', 
                [], [], 
                '''                lifetime-related configuration
                ''',
                'lifetime',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('mapping-table', REFERENCE_CLASS, 'MappingTable' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable', 
                [], [], 
                '''                Mapping table
                ''',
                'mapping_table',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the PCP server instance
                ''',
                'name',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('nonce-validation-checks-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether NONCE validation checks are
                 enabled/disabled
                ''',
                'nonce_validation_checks_enable',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('opcode-capability', REFERENCE_CLASS, 'OpcodeCapability' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.OpcodeCapability', 
                [], [], 
                '''                Opcode-related capabilities
                ''',
                'opcode_capability',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('opcode-configuration', REFERENCE_CLASS, 'OpcodeConfiguration' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.OpcodeConfiguration', 
                [], [], 
                '''                Opcode-related configuration
                ''',
                'opcode_configuration',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('option-capability', REFERENCE_CLASS, 'OptionCapability' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability', 
                [], [], 
                '''                Option-related capabilities
                ''',
                'option_capability',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('option-configuration', REFERENCE_CLASS, 'OptionConfiguration' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration', 
                [], [], 
                '''                Option-related configuration
                ''',
                'option_configuration',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('pcp-controlled-function-capability', REFERENCE_CLASS, 'PcpControlledFunctionCapability' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.PcpControlledFunctionCapability', 
                [], [], 
                '''                list of controlled functions.
                ''',
                'pcp_controlled_function_capability',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-parity-preservation-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether port parity preservation
                 is enabled/disabled
                ''',
                'port_parity_preservation_enable',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-parity-preservation-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether port parity preservation is
                 supported.
                ''',
                'port_parity_preservation_support',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-preservation-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether port preservation
                 is enabled/disabled
                ''',
                'port_preservation_enable',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-preservation-suport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether port preservation
                 is supported.
                ''',
                'port_preservation_suport',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-quota', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Indicates the configured port quota.
                ''',
                'port_quota',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-randomization-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether port randomization
                 is enabled/disabled
                ''',
                'port_randomization_enable',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('port-randomization-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether port randomization is
                 supported.
                ''',
                'port_randomization_support',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('preferred-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                List of preferred version.
                 Mainly used for unsolicited messages.
                ''',
                'preferred_version',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('protocol-capabilities', REFERENCE_LIST, 'ProtocolCapabilities' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.ProtocolCapabilities', 
                [], [], 
                '''                A set of supported transported protocols
                ''',
                'protocol_capabilities',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('subscriber-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Indicates the configured subscriber-mask
                ''',
                'subscriber_mask',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('subscriber-mask-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates if the subscriber-mask feature is supported
                ''',
                'subscriber_mask_support',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('supported-version', REFERENCE_LIST, 'SupportedVersion' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.SupportedVersion', 
                [], [], 
                '''                List of supported PCP versions.
                ''',
                'supported_version',
                'ietf-pcp-server', False),
            _MetaInfoClassMember('traffic-statistics', REFERENCE_CLASS, 'TrafficStatistics' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics', 
                [], [], 
                '''                traffic statistics
                ''',
                'traffic_statistics',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'pcp-server-instance',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState.PcpServerInstances' : {
        'meta_info' : _MetaInfoClass('PcpServerState.PcpServerInstances',
            False, 
            [
            _MetaInfoClassMember('pcp-server-instance', REFERENCE_LIST, 'PcpServerInstance' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances.PcpServerInstance', 
                [], [], 
                '''                PCP server instance
                ''',
                'pcp_server_instance',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'pcp-server-instances',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
    'PcpServerState' : {
        'meta_info' : _MetaInfoClass('PcpServerState',
            False, 
            [
            _MetaInfoClassMember('pcp-server-instances', REFERENCE_CLASS, 'PcpServerInstances' , 'ydk.models.ietf.ietf_pcp_server', 'PcpServerState.PcpServerInstances', 
                [], [], 
                '''                PCP server instances
                ''',
                'pcp_server_instances',
                'ietf-pcp-server', False),
            ],
            'ietf-pcp-server',
            'pcp-server-state',
            _yang_ns._namespaces['ietf-pcp-server'],
        'ydk.models.ietf.ietf_pcp_server'
        ),
    },
}
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64.DestIpv4Prefix']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Filter']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.PortSetOption']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Description']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.InternalPort']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.ExternalPort']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.Filter']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.Version']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.PcpServerIpAddress']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OpcodeConfiguration']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.ExcludePorts']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.Protocol']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.Lifetime']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.ErrorLifetime']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance']['meta_info'].parent =_meta_table['PcpServerConfig.PcpServerInstances']['meta_info']
_meta_table['PcpServerConfig.PcpServerInstances']['meta_info'].parent =_meta_table['PcpServerConfig']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability.Filter']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability.Description']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64.DestIpv4Prefix']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Filter']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.PortSetOption']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Description']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.InternalPort']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.ExternalPort']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.Filter']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.TrafficStatistics_']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.OpcodeStatistics']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.MappingTable']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.SupportedVersion']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.ConfiguredPcpServerIpAddress']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.ExternalIpAddressPool']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OpcodeCapability']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.ProtocolCapabilities']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.PcpControlledFunctionCapability']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OpcodeConfiguration']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.EnabledProtocol']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.ExcludePorts']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.Lifetime']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.ErrorLifetime']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']
_meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info'].parent =_meta_table['PcpServerState.PcpServerInstances']['meta_info']
_meta_table['PcpServerState.PcpServerInstances']['meta_info'].parent =_meta_table['PcpServerState']['meta_info']
