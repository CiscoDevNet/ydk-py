


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.Version' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.Version',
            False, 
            [
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Indicates a PCP server.
                 Current versions are: 0, 1, and 2.
                ''',
                'version',
                'ietf-pcp-proxy', True),
            ],
            'ietf-pcp-proxy',
            'version',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.PcpServers.PcpServerIpAddress' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.PcpServers.PcpServerIpAddress',
            False, 
            [
            _MetaInfoClassMember('address-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier
                ''',
                'address_id',
                'ietf-pcp-proxy', True),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                An IP address of a PCP server.
                ''',
                'ip_address',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'pcp-server-ip-address',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.PcpServers' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.PcpServers',
            False, 
            [
            _MetaInfoClassMember('pcp-server-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique identifier.
                ''',
                'pcp_server_id',
                'ietf-pcp-proxy', True),
            _MetaInfoClassMember('external-address-familly', REFERENCE_ENUM_CLASS, 'IpVersionEnum' , 'ydk.models.ietf.ietf_inet_types', 'IpVersionEnum', 
                [], [], 
                '''                The address family of the external address(es)
                managed by the PCP server.
                Can be IPv4, IPv6 or both.
                ''',
                'external_address_familly',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('pcp-server-ip-address', REFERENCE_LIST, 'PcpServerIpAddress' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.PcpServers.PcpServerIpAddress', 
                [], [], 
                '''                a list of IP addresses of a PCP server
                ''',
                'pcp_server_ip_address',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('stale-external-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                A stale address that can be used by the PCP client
                to be assigned the same address upon reboot
                or other failure events.
                ''',
                'stale_external_ip_address',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'pcp-servers',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.OpcodeConfiguration' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.OpcodeConfiguration',
            False, 
            [
            _MetaInfoClassMember('announce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ANNOUNCE opcode.
                ''',
                'announce',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('map', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MAP opcode
                ''',
                'map',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('peer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PEER opcode
                ''',
                'peer',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('relay-unknown-opcode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The proxy can be instructed to relay
                 or to reject unknown opcodes.
                ''',
                'relay_unknown_opcode',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'opcode-configuration',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig.PcpProxyInstances.PcpProxyInstance' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances.PcpProxyInstance',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of the PCP proxy instance
                ''',
                'id',
                'ietf-pcp-proxy', True),
            _MetaInfoClassMember('authentication-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable PCP authentication.
                ''',
                'authentication_enable',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A name of the PCP proxy instance
                ''',
                'name',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('opcode-configuration', REFERENCE_CLASS, 'OpcodeConfiguration' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.OpcodeConfiguration', 
                [], [], 
                '''                Opcode-related configuration
                ''',
                'opcode_configuration',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('pcp-servers', REFERENCE_LIST, 'PcpServers' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.PcpServers', 
                [], [], 
                '''                List of provisioned PCP servers.
                ''',
                'pcp_servers',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('version', REFERENCE_LIST, 'Version' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.Version', 
                [], [], 
                '''                Supported PCP versions.
                ''',
                'version',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'pcp-proxy-instance',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig.PcpProxyInstances.OptionConfiguration.Filter' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances.OptionConfiguration.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable FILTER option.
                ''',
                'filter_enabled',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('max-filters', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum number of filters
                 associated with a mapping.
                ''',
                'max_filters',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'filter',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig.PcpProxyInstances.OptionConfiguration.Description' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances.OptionConfiguration.Description',
            False, 
            [
            _MetaInfoClassMember('description-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable DESCRIPTION option.
                ''',
                'description_enabled',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('max-description', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum length of the description
                 associated with a mapping.
                ''',
                'max_description',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'description',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig.PcpProxyInstances.OptionConfiguration' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances.OptionConfiguration',
            False, 
            [
            _MetaInfoClassMember('description', REFERENCE_CLASS, 'Description' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.OptionConfiguration.Description', 
                [], [], 
                '''                Associates a description with a mapping [RFC7220].
                ''',
                'description',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('filter', REFERENCE_CLASS, 'Filter' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.OptionConfiguration.Filter', 
                [], [], 
                '''                This option indicates that filtering incoming packets
                is desired.
                ''',
                'filter',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('port-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether PORT_SET is supported/enabled.
                ''',
                'port_set',
                'ietf-pcp-proxy', False),
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
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('prefix64', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PREFIX64 PCP option [RFC7225].
                ''',
                'prefix64',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('relay-mandatory-unknown-option', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The proxy can be instructed to relay or
                 to reject mandatory unknown options.
                ''',
                'relay_mandatory_unknown_option',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('relay-optionnal-unknown-option', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The proxy can be instructed to relay or
                 to reject optional unknown options.
                ''',
                'relay_optionnal_unknown_option',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('third-party', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                THIRD_PARTY option is used when a PCP client wants
                 to control a mapping to an internal host other
                 than itself [RFC6887].
                ''',
                'third_party',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'option-configuration',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.InternalPort' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.InternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'internal-port',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.ExternalPort' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.ExternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'external-port',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.Filter' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of the filter.
                ''',
                'filter_id',
                'ietf-pcp-proxy', True),
            _MetaInfoClassMember('remote-ip-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IP address of the remote peer.
                ''',
                'remote_ip_prefix',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('remote-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The port number of the remote peer. Value 0
                indicates 'all ports'.
                ''',
                'remote_port_number',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'filter',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.LocalAssignedPort' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.LocalAssignedPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'local-assigned-port',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.ietf.ietf_pcp_proxy',
        {
            'disabled':'disabled',
            'requested':'requested',
            'assigned':'assigned',
            'stale':'stale',
        }, 'ietf-pcp', _yang_ns._namespaces['ietf-pcp']),
    'PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique identifier of a mapping entry.
                ''',
                'index',
                'ietf-pcp-proxy', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                a description string associated with the mapping.
                ''',
                'description',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('external-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                External IP address. Can be 'Suggested' or 'Assigned'.
                
                It can be set by a client to stale-ip-address, if available
                or to (::) (for requesting external IPv6 addresses)
                or (::ffff:0:0) (for requesting external IPv4 addresses).
                ''',
                'external_ip_address',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('external-port', REFERENCE_CLASS, 'ExternalPort' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.ExternalPort', 
                [], [], 
                '''                External port number. Can be 'Suggested' or 'Assigned'.
                ''',
                'external_port',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('filter', REFERENCE_LIST, 'Filter' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.Filter', 
                [], [], 
                '''                a list of filters associated with the mapping.
                ''',
                'filter',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('internal-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Corresponds to the PCP Client's IP Address
                defined in [RFC6887].
                ''',
                'internal_ip_address',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('internal-port', REFERENCE_CLASS, 'InternalPort' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.InternalPort', 
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
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lifetime of the mapping.
                 Can be requested/assigned/remaining
                ''',
                'lifetime',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('local-assigned-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                If the local PCP-controlled function
                 alters the source IP address, this
                 information must be stored.
                ''',
                'local_assigned_ip_address',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('local-assigned-port', REFERENCE_CLASS, 'LocalAssignedPort' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.LocalAssignedPort', 
                [], [], 
                '''                If the local PCP-controlled function
                 alters the source port, this
                 information must be stored.
                ''',
                'local_assigned_port',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('mapping-nonce', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A random value chosen by the PCP client
                ''',
                'mapping_nonce',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('prefer-failure-tagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                a tag which indicates whether PREFER_FAILURE
                 is (to be) used.
                ''',
                'prefer_failure_tagged',
                'ietf-pcp-proxy', False),
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
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.StatusEnum', 
                [], [], 
                '''                Indicates the status of a mapping entry.
                ''',
                'status',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('third-party-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                used to indicate the internal IP address
                 when THIRD_PARTY is in use.
                ''',
                'third_party_address',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'mapping-entry',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig.PcpProxyInstances.MappingTable' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances.MappingTable',
            False, 
            [
            _MetaInfoClassMember('mapping-entry', REFERENCE_LIST, 'MappingEntry' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry', 
                [], [], 
                '''                PCP mapping entry
                ''',
                'mapping_entry',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'mapping-table',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig.PcpProxyInstances' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig.PcpProxyInstances',
            False, 
            [
            _MetaInfoClassMember('mapping-table', REFERENCE_CLASS, 'MappingTable' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.MappingTable', 
                [], [], 
                '''                PCP mapping table maintained by the PCP proxy
                ''',
                'mapping_table',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('option-configuration', REFERENCE_CLASS, 'OptionConfiguration' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.OptionConfiguration', 
                [], [], 
                '''                Option-related configuration
                ''',
                'option_configuration',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('pcp-proxy-instance', REFERENCE_LIST, 'PcpProxyInstance' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances.PcpProxyInstance', 
                [], [], 
                '''                PCP proxy instance
                ''',
                'pcp_proxy_instance',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('terminate-proxy-recursion', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The proxy can be instructed to terminate
                 proxy recursion.
                ''',
                'terminate_proxy_recursion',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'pcp-proxy-instances',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyConfig' : {
        'meta_info' : _MetaInfoClass('PcpProxyConfig',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Associated a description with the module.
                ''',
                'description',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable PCP proxy
                ''',
                'enable',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('pcp-proxy-instances', REFERENCE_CLASS, 'PcpProxyInstances' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyConfig.PcpProxyInstances', 
                [], [], 
                '''                PCP proxy instances
                ''',
                'pcp_proxy_instances',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'pcp-proxy-config',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.SupportedVersion' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.SupportedVersion',
            False, 
            [
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Indicates a PCP server.
                 Current versions are: 0, 1, and 2.
                ''',
                'version',
                'ietf-pcp-proxy', True),
            ],
            'ietf-pcp-proxy',
            'supported-version',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpProxyIpAddress' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpProxyIpAddress',
            False, 
            [
            _MetaInfoClassMember('address-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier
                ''',
                'address_id',
                'ietf-pcp-proxy', True),
            _MetaInfoClassMember('pcp-proxy-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                An address
                ''',
                'pcp_proxy_ip_address',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'pcp-proxy-ip-address',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpServerAddress.PcpServerIpAddress' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpServerAddress.PcpServerIpAddress',
            False, 
            [
            _MetaInfoClassMember('address-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier
                ''',
                'address_id',
                'ietf-pcp-proxy', True),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                An IP address of a PCP server.
                ''',
                'ip_address',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'pcp-server-ip-address',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpServerAddress.SourceEnum' : _MetaInfoEnum('SourceEnum', 'ydk.models.ietf.ietf_pcp_proxy',
        {
            'manual-configuration':'manual_configuration',
            'dhcpv6':'dhcpv6',
            'dhcpv4':'dhcpv4',
            'else':'else_',
        }, 'ietf-pcp', _yang_ns._namespaces['ietf-pcp']),
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpServerAddress' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpServerAddress',
            False, 
            [
            _MetaInfoClassMember('pcp-server-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique identifier.
                ''',
                'pcp_server_id',
                'ietf-pcp-proxy', True),
            _MetaInfoClassMember('client-epoch', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The PCP client's Epoch.
                ''',
                'client_epoch',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('current-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The version that is selected as per the version negotiation
                procedure specified in Section 9 of [RFC6877].
                ''',
                'current_version',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('external-address-familly', REFERENCE_ENUM_CLASS, 'IpVersionEnum' , 'ydk.models.ietf.ietf_inet_types', 'IpVersionEnum', 
                [], [], 
                '''                The address family of the external address(es)
                managed by the PCP server.
                Can be IPv4, IPv6 or both.
                ''',
                'external_address_familly',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('in-use', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether this in-use instance of the server
                is the result of the selection
                process defined in [RFC7488].
                ''',
                'in_use',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('pcp-server-ip-address', REFERENCE_LIST, 'PcpServerIpAddress' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpServerAddress.PcpServerIpAddress', 
                [], [], 
                '''                a list of IP addresses of a PCP server
                ''',
                'pcp_server_ip_address',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('server-epoch', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The PCP server's Epoch.
                ''',
                'server_epoch',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('source', REFERENCE_ENUM_CLASS, 'SourceEnum' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpServerAddress.SourceEnum', 
                [], [], 
                '''                source of the PCP server reachability information.
                ''',
                'source',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('stale-external-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                A stale address that can be used by the PCP client
                to be assigned the same address upon reboot
                or other failure events.
                ''',
                'stale_external_ip_address',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'pcp-server-address',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpControlledFunctionCapability' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpControlledFunctionCapability',
            False, 
            [
            _MetaInfoClassMember('ds-lite', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                DS-Lite
                ''',
                'ds_lite',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('ipv4-firewall', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IPv4 firewall
                ''',
                'ipv4_firewall',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('ipv6-firewall', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IPv6 firewall
                ''',
                'ipv6_firewall',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('nat44', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                NAT44
                ''',
                'nat44',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('nat64', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                NAT64
                ''',
                'nat64',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('nptv6', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                NPTv6
                ''',
                'nptv6',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('port-range-router', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Port Range Router
                ''',
                'port_range_router',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'pcp-controlled-function-capability',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OpcodeCapability' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.OpcodeCapability',
            False, 
            [
            _MetaInfoClassMember('announce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ANNOUNCE opcode.
                ''',
                'announce',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('map', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MAP opcode
                ''',
                'map',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('peer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PEER opcode
                ''',
                'peer',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('relay-unknown-opcode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                instruction related to the processing of unknown
                 opcodes.
                ''',
                'relay_unknown_opcode',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'opcode-capability',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionCapability.Filter' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionCapability.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable FILTER option.
                ''',
                'filter_enabled',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('max-filters', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum number of filters
                 associated with a mapping.
                ''',
                'max_filters',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'filter',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionCapability.Description' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionCapability.Description',
            False, 
            [
            _MetaInfoClassMember('description-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable DESCRIPTION option.
                ''',
                'description_enabled',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('max-description', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum length of the description
                 associated with a mapping.
                ''',
                'max_description',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'description',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionCapability' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionCapability',
            False, 
            [
            _MetaInfoClassMember('description', REFERENCE_CLASS, 'Description' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionCapability.Description', 
                [], [], 
                '''                Associates a description with a mapping [RFC7220].
                ''',
                'description',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('filter', REFERENCE_CLASS, 'Filter' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionCapability.Filter', 
                [], [], 
                '''                This option indicates that filtering incoming packets
                is desired.
                ''',
                'filter',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('port-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether PORT_SET is supported/enabled.
                ''',
                'port_set',
                'ietf-pcp-proxy', False),
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
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('prefix64', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PREFIX64 PCP option [RFC7225].
                ''',
                'prefix64',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('relay-mandatory-unknown-option', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                instruction related to the processing
                 of mandatory unknown options.
                ''',
                'relay_mandatory_unknown_option',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('relay-optionnal-unknown-option', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                instruction related to the processing
                 of optional unknown options.
                ''',
                'relay_optionnal_unknown_option',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('third-party', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                THIRD_PARTY option is used when a PCP client wants
                 to control a mapping to an internal host other
                 than itself [RFC6887].
                ''',
                'third_party',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'option-capability',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OpcodeConfiguration' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.OpcodeConfiguration',
            False, 
            [
            _MetaInfoClassMember('announce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ANNOUNCE opcode.
                ''',
                'announce',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('map', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MAP opcode
                ''',
                'map',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('peer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PEER opcode
                ''',
                'peer',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'opcode-configuration',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionConfiguration.Filter' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionConfiguration.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable FILTER option.
                ''',
                'filter_enabled',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('max-filters', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum number of filters
                 associated with a mapping.
                ''',
                'max_filters',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'filter',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionConfiguration.Description' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionConfiguration.Description',
            False, 
            [
            _MetaInfoClassMember('description-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable DESCRIPTION option.
                ''',
                'description_enabled',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('max-description', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum length of the description
                 associated with a mapping.
                ''',
                'max_description',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'description',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionConfiguration' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionConfiguration',
            False, 
            [
            _MetaInfoClassMember('description', REFERENCE_CLASS, 'Description' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionConfiguration.Description', 
                [], [], 
                '''                Associates a description with a mapping [RFC7220].
                ''',
                'description',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('filter', REFERENCE_CLASS, 'Filter' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionConfiguration.Filter', 
                [], [], 
                '''                This option indicates that filtering incoming packets
                is desired.
                ''',
                'filter',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('port-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether PORT_SET is supported/enabled.
                ''',
                'port_set',
                'ietf-pcp-proxy', False),
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
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('prefix64', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PREFIX64 PCP option [RFC7225].
                ''',
                'prefix64',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('relay-mandatory-unknown-option', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                instruction related to the processing
                 of mandatory unknown options.
                ''',
                'relay_mandatory_unknown_option',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('relay-optionnal-unknown-option', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                instruction related to the processing
                 of optional unknown options.
                ''',
                'relay_optionnal_unknown_option',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('third-party', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                THIRD_PARTY option is used when a PCP client wants
                 to control a mapping to an internal host other
                 than itself [RFC6887].
                ''',
                'third_party',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'option-configuration',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.InternalPort' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.InternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'internal-port',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.ExternalPort' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.ExternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'external-port',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.Filter' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of the filter.
                ''',
                'filter_id',
                'ietf-pcp-proxy', True),
            _MetaInfoClassMember('remote-ip-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IP address of the remote peer.
                ''',
                'remote_ip_prefix',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('remote-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The port number of the remote peer. Value 0
                indicates 'all ports'.
                ''',
                'remote_port_number',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'filter',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.LocalAssignedPort' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.LocalAssignedPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'local-assigned-port',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.StatusCodeEnum' : _MetaInfoEnum('StatusCodeEnum', 'ydk.models.ietf.ietf_pcp_proxy',
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
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.ietf.ietf_pcp_proxy',
        {
            'disabled':'disabled',
            'requested':'requested',
            'assigned':'assigned',
            'stale':'stale',
        }, 'ietf-pcp', _yang_ns._namespaces['ietf-pcp']),
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique identifier of a mapping entry.
                ''',
                'index',
                'ietf-pcp-proxy', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                a description string associated with the mapping.
                ''',
                'description',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('external-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                External IP address. Can be 'Suggested' or 'Assigned'.
                
                It can be set by a client to stale-ip-address, if available
                or to (::) (for requesting external IPv6 addresses)
                or (::ffff:0:0) (for requesting external IPv4 addresses).
                ''',
                'external_ip_address',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('external-port', REFERENCE_CLASS, 'ExternalPort' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.ExternalPort', 
                [], [], 
                '''                External port number. Can be 'Suggested' or 'Assigned'.
                ''',
                'external_port',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('filter', REFERENCE_LIST, 'Filter' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.Filter', 
                [], [], 
                '''                a list of filters associated with the mapping.
                ''',
                'filter',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('internal-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Corresponds to the PCP Client's IP Address
                defined in [RFC6887].
                ''',
                'internal_ip_address',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('internal-port', REFERENCE_CLASS, 'InternalPort' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.InternalPort', 
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
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lifetime of the mapping.
                 Can be requested/assigned/remaining
                ''',
                'lifetime',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('local-assigned-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                An address assigned locally by
                the proxy
                ''',
                'local_assigned_ip_address',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('local-assigned-port', REFERENCE_CLASS, 'LocalAssignedPort' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.LocalAssignedPort', 
                [], [], 
                '''                a port assigned locally by the proxy
                ''',
                'local_assigned_port',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('mapping-nonce', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A random value chosen by the PCP client
                ''',
                'mapping_nonce',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('prefer-failure-tagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                a tag which indicates whether PREFER_FAILURE
                 is (to be) used.
                ''',
                'prefer_failure_tagged',
                'ietf-pcp-proxy', False),
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
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.StatusEnum', 
                [], [], 
                '''                Indicates the status of a mapping entry.
                ''',
                'status',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('status-code', REFERENCE_ENUM_CLASS, 'StatusCodeEnum' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.StatusCodeEnum', 
                [], [], 
                '''                result status code.
                ''',
                'status_code',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('third-party-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                used to indicate the internal IP address
                 when THIRD_PARTY is in use.
                ''',
                'third_party_address',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'mapping-entry',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable',
            False, 
            [
            _MetaInfoClassMember('mapping-entry', REFERENCE_LIST, 'MappingEntry' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry', 
                [], [], 
                '''                mapping entry
                ''',
                'mapping_entry',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'mapping-table',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ClientFacingInterface.TrafficStatistics_' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ClientFacingInterface.TrafficStatistics_',
            False, 
            [
            _MetaInfoClassMember('dropped-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for dropped traffic in bytes.
                ''',
                'dropped_byte',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('dropped-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for dropped packets.
                ''',
                'dropped_packet',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('rcvd-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received traffic in bytes.
                ''',
                'rcvd_byte',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('rcvd-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received packets.
                ''',
                'rcvd_packet',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('sent-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent traffic in bytes.
                ''',
                'sent_byte',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('sent-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets sent
                ''',
                'sent_packet',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'traffic-statistics',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ClientFacingInterface.OpcodeStatistics' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ClientFacingInterface.OpcodeStatistics',
            False, 
            [
            _MetaInfoClassMember('rcvd-announce', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received ANNOUNCED messages
                ''',
                'rcvd_announce',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('rcvd-malformed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received malformed opcodes
                ''',
                'rcvd_malformed',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('rcvd-map', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received MAP messages
                ''',
                'rcvd_map',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('rcvd-peer', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received PEER messages
                ''',
                'rcvd_peer',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('rcvd-unknown', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received unknown opcodes
                ''',
                'rcvd_unknown',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('sent-annonce', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent ANNOUNCE messages
                ''',
                'sent_annonce',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('sent-map', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent MAP messages
                ''',
                'sent_map',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('sent-peer', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent PEER messages
                ''',
                'sent_peer',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'opcode-statistics',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ClientFacingInterface' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ClientFacingInterface',
            False, 
            [
            _MetaInfoClassMember('opcode-statistics', REFERENCE_CLASS, 'OpcodeStatistics' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ClientFacingInterface.OpcodeStatistics', 
                [], [], 
                '''                Opcode-related statistics.
                ''',
                'opcode_statistics',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('traffic-statistics', REFERENCE_CLASS, 'TrafficStatistics_' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ClientFacingInterface.TrafficStatistics_', 
                [], [], 
                '''                Generic traffic statistics.
                ''',
                'traffic_statistics',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'client-facing-interface',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ServerFacingInterface.TrafficStatistics_' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ServerFacingInterface.TrafficStatistics_',
            False, 
            [
            _MetaInfoClassMember('dropped-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for dropped traffic in bytes.
                ''',
                'dropped_byte',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('dropped-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for dropped packets.
                ''',
                'dropped_packet',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('rcvd-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received traffic in bytes.
                ''',
                'rcvd_byte',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('rcvd-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received packets.
                ''',
                'rcvd_packet',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('sent-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent traffic in bytes.
                ''',
                'sent_byte',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('sent-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets sent
                ''',
                'sent_packet',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'traffic-statistics',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ServerFacingInterface.OpcodeStatistics' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ServerFacingInterface.OpcodeStatistics',
            False, 
            [
            _MetaInfoClassMember('rcvd-announce', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received ANNOUNCED messages
                ''',
                'rcvd_announce',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('rcvd-malformed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received malformed opcodes
                ''',
                'rcvd_malformed',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('rcvd-map', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received MAP messages
                ''',
                'rcvd_map',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('rcvd-peer', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received PEER messages
                ''',
                'rcvd_peer',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('rcvd-unknown', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received unknown opcodes
                ''',
                'rcvd_unknown',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('sent-annonce', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent ANNOUNCE messages
                ''',
                'sent_annonce',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('sent-map', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent MAP messages
                ''',
                'sent_map',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('sent-peer', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent PEER messages
                ''',
                'sent_peer',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'opcode-statistics',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ServerFacingInterface' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ServerFacingInterface',
            False, 
            [
            _MetaInfoClassMember('opcode-statistics', REFERENCE_CLASS, 'OpcodeStatistics' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ServerFacingInterface.OpcodeStatistics', 
                [], [], 
                '''                Opcode-related statistics.
                ''',
                'opcode_statistics',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('traffic-statistics', REFERENCE_CLASS, 'TrafficStatistics_' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ServerFacingInterface.TrafficStatistics_', 
                [], [], 
                '''                Generic traffic statistics.
                ''',
                'traffic_statistics',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'server-facing-interface',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.MappingTable' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.MappingTable',
            False, 
            [
            _MetaInfoClassMember('current-mt-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Size of the mapping table
                ''',
                'current_mt_size',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('max-mt-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum configured size of the mapping table.
                ''',
                'max_mt_size',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'mapping-table',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics',
            False, 
            [
            _MetaInfoClassMember('client-facing-interface', REFERENCE_CLASS, 'ClientFacingInterface' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ClientFacingInterface', 
                [], [], 
                '''                traffic statistics in the client-facing
                 interface
                ''',
                'client_facing_interface',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('mapping-table', REFERENCE_CLASS, 'MappingTable' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.MappingTable', 
                [], [], 
                '''                mapping table statistics
                ''',
                'mapping_table',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('server-facing-interface', REFERENCE_CLASS, 'ServerFacingInterface' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ServerFacingInterface', 
                [], [], 
                '''                traffic statistics in the server-facing
                 interface
                ''',
                'server_facing_interface',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'traffic-statistics',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances.PcpProxyInstance' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances.PcpProxyInstance',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Identifier
                ''',
                'id',
                'ietf-pcp-proxy', True),
            _MetaInfoClassMember('authentication-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                status of the PCP authentication activation
                ''',
                'authentication_enabled',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('authentication-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether PCP authentication is
                 enabled/disabled.
                ''',
                'authentication_support',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('mapping-table', REFERENCE_CLASS, 'MappingTable' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable', 
                [], [], 
                '''                mapping table
                ''',
                'mapping_table',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the PCP proxy Instance
                ''',
                'name',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('opcode-capability', REFERENCE_CLASS, 'OpcodeCapability' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OpcodeCapability', 
                [], [], 
                '''                Opcode-related capabilities.
                ''',
                'opcode_capability',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('opcode-configuration', REFERENCE_CLASS, 'OpcodeConfiguration' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OpcodeConfiguration', 
                [], [], 
                '''                opcode-related configurations.
                ''',
                'opcode_configuration',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('option-capability', REFERENCE_CLASS, 'OptionCapability' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionCapability', 
                [], [], 
                '''                Option-related capabilities.
                ''',
                'option_capability',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('option-configuration', REFERENCE_CLASS, 'OptionConfiguration' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionConfiguration', 
                [], [], 
                '''                opcode-related configurations.
                ''',
                'option_configuration',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('pcp-controlled-function-capability', REFERENCE_CLASS, 'PcpControlledFunctionCapability' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpControlledFunctionCapability', 
                [], [], 
                '''                list of controlled local functions.
                ''',
                'pcp_controlled_function_capability',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('pcp-proxy-ip-address', REFERENCE_LIST, 'PcpProxyIpAddress' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpProxyIpAddress', 
                [], [], 
                '''                List of configured addresses to the
                 PCP proxy instance.
                ''',
                'pcp_proxy_ip_address',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('pcp-server-address', REFERENCE_LIST, 'PcpServerAddress' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpServerAddress', 
                [], [], 
                '''                list of provisioned PCP servers.
                ''',
                'pcp_server_address',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('preferred-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Configured preferred version
                ''',
                'preferred_version',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('supported-version', REFERENCE_LIST, 'SupportedVersion' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.SupportedVersion', 
                [], [], 
                '''                List of supported versions
                ''',
                'supported_version',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('terminate-proxy-recursion-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether recursion is
                 terminated or not
                ''',
                'terminate_proxy_recursion_status',
                'ietf-pcp-proxy', False),
            _MetaInfoClassMember('traffic-statistics', REFERENCE_CLASS, 'TrafficStatistics' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics', 
                [], [], 
                '''                traffic statistics
                ''',
                'traffic_statistics',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'pcp-proxy-instance',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState.PcpProxyInstances' : {
        'meta_info' : _MetaInfoClass('PcpProxyState.PcpProxyInstances',
            False, 
            [
            _MetaInfoClassMember('pcp-proxy-instance', REFERENCE_LIST, 'PcpProxyInstance' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances.PcpProxyInstance', 
                [], [], 
                '''                PCP proxy Instance
                ''',
                'pcp_proxy_instance',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'pcp-proxy-instances',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
    'PcpProxyState' : {
        'meta_info' : _MetaInfoClass('PcpProxyState',
            False, 
            [
            _MetaInfoClassMember('pcp-proxy-instances', REFERENCE_CLASS, 'PcpProxyInstances' , 'ydk.models.ietf.ietf_pcp_proxy', 'PcpProxyState.PcpProxyInstances', 
                [], [], 
                '''                PCP proxy Instances
                ''',
                'pcp_proxy_instances',
                'ietf-pcp-proxy', False),
            ],
            'ietf-pcp-proxy',
            'pcp-proxy-state',
            _yang_ns._namespaces['ietf-pcp-proxy'],
        'ydk.models.ietf.ietf_pcp_proxy'
        ),
    },
}
_meta_table['PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.PcpServers.PcpServerIpAddress']['meta_info'].parent =_meta_table['PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.PcpServers']['meta_info']
_meta_table['PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.Version']['meta_info'].parent =_meta_table['PcpProxyConfig.PcpProxyInstances.PcpProxyInstance']['meta_info']
_meta_table['PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.PcpServers']['meta_info'].parent =_meta_table['PcpProxyConfig.PcpProxyInstances.PcpProxyInstance']['meta_info']
_meta_table['PcpProxyConfig.PcpProxyInstances.PcpProxyInstance.OpcodeConfiguration']['meta_info'].parent =_meta_table['PcpProxyConfig.PcpProxyInstances.PcpProxyInstance']['meta_info']
_meta_table['PcpProxyConfig.PcpProxyInstances.OptionConfiguration.Filter']['meta_info'].parent =_meta_table['PcpProxyConfig.PcpProxyInstances.OptionConfiguration']['meta_info']
_meta_table['PcpProxyConfig.PcpProxyInstances.OptionConfiguration.Description']['meta_info'].parent =_meta_table['PcpProxyConfig.PcpProxyInstances.OptionConfiguration']['meta_info']
_meta_table['PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.InternalPort']['meta_info'].parent =_meta_table['PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.ExternalPort']['meta_info'].parent =_meta_table['PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.Filter']['meta_info'].parent =_meta_table['PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry.LocalAssignedPort']['meta_info'].parent =_meta_table['PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpProxyConfig.PcpProxyInstances.MappingTable.MappingEntry']['meta_info'].parent =_meta_table['PcpProxyConfig.PcpProxyInstances.MappingTable']['meta_info']
_meta_table['PcpProxyConfig.PcpProxyInstances.PcpProxyInstance']['meta_info'].parent =_meta_table['PcpProxyConfig.PcpProxyInstances']['meta_info']
_meta_table['PcpProxyConfig.PcpProxyInstances.OptionConfiguration']['meta_info'].parent =_meta_table['PcpProxyConfig.PcpProxyInstances']['meta_info']
_meta_table['PcpProxyConfig.PcpProxyInstances.MappingTable']['meta_info'].parent =_meta_table['PcpProxyConfig.PcpProxyInstances']['meta_info']
_meta_table['PcpProxyConfig.PcpProxyInstances']['meta_info'].parent =_meta_table['PcpProxyConfig']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpServerAddress.PcpServerIpAddress']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpServerAddress']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionCapability.Filter']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionCapability']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionCapability.Description']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionCapability']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionConfiguration.Filter']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionConfiguration']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionConfiguration.Description']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionConfiguration']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.InternalPort']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.ExternalPort']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.Filter']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry.LocalAssignedPort']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable.MappingEntry']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ClientFacingInterface.TrafficStatistics_']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ClientFacingInterface']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ClientFacingInterface.OpcodeStatistics']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ClientFacingInterface']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ServerFacingInterface.TrafficStatistics_']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ServerFacingInterface']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ServerFacingInterface.OpcodeStatistics']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ServerFacingInterface']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ClientFacingInterface']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.ServerFacingInterface']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics.MappingTable']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.SupportedVersion']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpProxyIpAddress']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpServerAddress']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.PcpControlledFunctionCapability']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.OpcodeCapability']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionCapability']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.OpcodeConfiguration']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.OptionConfiguration']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.MappingTable']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance.TrafficStatistics']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances.PcpProxyInstance']['meta_info'].parent =_meta_table['PcpProxyState.PcpProxyInstances']['meta_info']
_meta_table['PcpProxyState.PcpProxyInstances']['meta_info'].parent =_meta_table['PcpProxyState']['meta_info']
