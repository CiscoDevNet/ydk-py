


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'PcpClientConfig.PcpClientInstances.PcpClientInstance.Version' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig.PcpClientInstances.PcpClientInstance.Version',
            False, 
            [
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Indicates a PCP server.
                 Current versions are: 0, 1, and 2.
                ''',
                'version',
                'ietf-pcp-client', True),
            ],
            'ietf-pcp-client',
            'version',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientConfig.PcpClientInstances.PcpClientInstance.PcpServers.PcpServerIpAddress' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig.PcpClientInstances.PcpClientInstance.PcpServers.PcpServerIpAddress',
            False, 
            [
            _MetaInfoClassMember('address-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier
                ''',
                'address_id',
                'ietf-pcp-client', True),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                An IP address of a PCP server.
                ''',
                'ip_address',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'pcp-server-ip-address',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientConfig.PcpClientInstances.PcpClientInstance.PcpServers' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig.PcpClientInstances.PcpClientInstance.PcpServers',
            False, 
            [
            _MetaInfoClassMember('pcp-server-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique identifier.
                ''',
                'pcp_server_id',
                'ietf-pcp-client', True),
            _MetaInfoClassMember('external-address-familly', REFERENCE_ENUM_CLASS, 'IpVersionEnum' , 'ydk.models.ietf.ietf_inet_types', 'IpVersionEnum', 
                [], [], 
                '''                The address family of the external address(es)
                managed by the PCP server.
                Can be IPv4, IPv6 or both.
                ''',
                'external_address_familly',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('pcp-server-ip-address', REFERENCE_LIST, 'PcpServerIpAddress' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances.PcpClientInstance.PcpServers.PcpServerIpAddress', 
                [], [], 
                '''                a list of IP addresses of a PCP server
                ''',
                'pcp_server_ip_address',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('stale-external-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                A stale address that can be used by the PCP client
                to be assigned the same address upon reboot
                or other failure events.
                ''',
                'stale_external_ip_address',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'pcp-servers',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientConfig.PcpClientInstances.PcpClientInstance.OpcodeConfiguration' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig.PcpClientInstances.PcpClientInstance.OpcodeConfiguration',
            False, 
            [
            _MetaInfoClassMember('announce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ANNOUNCE opcode.
                ''',
                'announce',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('map', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MAP opcode
                ''',
                'map',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('peer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PEER opcode
                ''',
                'peer',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'opcode-configuration',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientConfig.PcpClientInstances.PcpClientInstance.OptionConfiguration.Filter' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig.PcpClientInstances.PcpClientInstance.OptionConfiguration.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable FILTER option.
                ''',
                'filter_enabled',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('max-filters', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum number of filters
                 associated with a mapping.
                ''',
                'max_filters',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'filter',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientConfig.PcpClientInstances.PcpClientInstance.OptionConfiguration.Description' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig.PcpClientInstances.PcpClientInstance.OptionConfiguration.Description',
            False, 
            [
            _MetaInfoClassMember('description-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable DESCRIPTION option.
                ''',
                'description_enabled',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('max-description', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum length of the description
                 associated with a mapping.
                ''',
                'max_description',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'description',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientConfig.PcpClientInstances.PcpClientInstance.OptionConfiguration' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig.PcpClientInstances.PcpClientInstance.OptionConfiguration',
            False, 
            [
            _MetaInfoClassMember('description', REFERENCE_CLASS, 'Description' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances.PcpClientInstance.OptionConfiguration.Description', 
                [], [], 
                '''                Associates a description with a mapping [RFC7220].
                ''',
                'description',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('filter', REFERENCE_CLASS, 'Filter' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances.PcpClientInstance.OptionConfiguration.Filter', 
                [], [], 
                '''                This option indicates that filtering incoming packets
                is desired.
                ''',
                'filter',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('port-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether PORT_SET is supported/enabled.
                ''',
                'port_set',
                'ietf-pcp-client', False),
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
                'ietf-pcp-client', False),
            _MetaInfoClassMember('prefix64', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PREFIX64 PCP option [RFC7225].
                ''',
                'prefix64',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('third-party', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                THIRD_PARTY option is used when a PCP client wants
                 to control a mapping to an internal host other
                 than itself [RFC6887].
                ''',
                'third_party',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'option-configuration',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.InternalPort' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.InternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'internal-port',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.ExternalPort' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.ExternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'external-port',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.Filter' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of the filter.
                ''',
                'filter_id',
                'ietf-pcp-client', True),
            _MetaInfoClassMember('remote-ip-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IP address of the remote peer.
                ''',
                'remote_ip_prefix',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('remote-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The port number of the remote peer. Value 0
                indicates 'all ports'.
                ''',
                'remote_port_number',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'filter',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.ietf.ietf_pcp_client',
        {
            'disabled':'disabled',
            'requested':'requested',
            'assigned':'assigned',
            'stale':'stale',
        }, 'ietf-pcp', _yang_ns._namespaces['ietf-pcp']),
    'PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique identifier of a mapping entry.
                ''',
                'index',
                'ietf-pcp-client', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                a description string associated with the mapping.
                ''',
                'description',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('external-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                External IP address. Can be 'Suggested' or 'Assigned'.
                
                It can be set by a client to stale-ip-address, if available
                or to (::) (for requesting external IPv6 addresses)
                or (::ffff:0:0) (for requesting external IPv4 addresses).
                ''',
                'external_ip_address',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('external-port', REFERENCE_CLASS, 'ExternalPort' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.ExternalPort', 
                [], [], 
                '''                External port number. Can be 'Suggested' or 'Assigned'.
                ''',
                'external_port',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('filter', REFERENCE_LIST, 'Filter' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.Filter', 
                [], [], 
                '''                a list of filters associated with the mapping.
                ''',
                'filter',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('internal-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Corresponds to the PCP Client's IP Address
                defined in [RFC6887].
                ''',
                'internal_ip_address',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('internal-port', REFERENCE_CLASS, 'InternalPort' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.InternalPort', 
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
                'ietf-pcp-client', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lifetime of the mapping.
                 Can be requested/assigned/remaining
                ''',
                'lifetime',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('mapping-nonce', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A random value chosen by the PCP client
                ''',
                'mapping_nonce',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('prefer-failure-tagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                a tag which indicates whether PREFER_FAILURE
                 is (to be) used.
                ''',
                'prefer_failure_tagged',
                'ietf-pcp-client', False),
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
                'ietf-pcp-client', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.StatusEnum', 
                [], [], 
                '''                Indicates the status of a mapping entry.
                ''',
                'status',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('third-party-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                used to indicate the internal IP address
                 when THIRD_PARTY is in use.
                ''',
                'third_party_address',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'mapping-entry',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable',
            False, 
            [
            _MetaInfoClassMember('mapping-entry', REFERENCE_LIST, 'MappingEntry' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry', 
                [], [], 
                '''                PCP Mapping entry.
                ''',
                'mapping_entry',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'mapping-table',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientConfig.PcpClientInstances.PcpClientInstance' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig.PcpClientInstances.PcpClientInstance',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of the PCP client instance.
                ''',
                'id',
                'ietf-pcp-client', True),
            _MetaInfoClassMember('authentication-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable PCP authentication.
                ''',
                'authentication_enable',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('mapping-table', REFERENCE_CLASS, 'MappingTable' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable', 
                [], [], 
                '''                Mapping table maintained by a PCP client
                 instance.
                ''',
                'mapping_table',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A name of the PCP client instance.
                ''',
                'name',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('opcode-configuration', REFERENCE_CLASS, 'OpcodeConfiguration' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances.PcpClientInstance.OpcodeConfiguration', 
                [], [], 
                '''                Opcode-related configuration
                ''',
                'opcode_configuration',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('option-configuration', REFERENCE_CLASS, 'OptionConfiguration' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances.PcpClientInstance.OptionConfiguration', 
                [], [], 
                '''                Options-related configuration.
                ''',
                'option_configuration',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('pcp-servers', REFERENCE_LIST, 'PcpServers' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances.PcpClientInstance.PcpServers', 
                [], [], 
                '''                List of provisioned PCP servers.
                ''',
                'pcp_servers',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('version', REFERENCE_LIST, 'Version' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances.PcpClientInstance.Version', 
                [], [], 
                '''                Indicates the set of supported PCP versions
                 (0, 1, 2)
                ''',
                'version',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'pcp-client-instance',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientConfig.PcpClientInstances' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig.PcpClientInstances',
            False, 
            [
            _MetaInfoClassMember('pcp-client-instance', REFERENCE_LIST, 'PcpClientInstance' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances.PcpClientInstance', 
                [], [], 
                '''                A PCP client instance.
                ''',
                'pcp_client_instance',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'pcp-client-instances',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientConfig' : {
        'meta_info' : _MetaInfoClass('PcpClientConfig',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Associated a description with the module.
                ''',
                'description',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable the PCP client.
                ''',
                'enable',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('pcp-client-instances', REFERENCE_CLASS, 'PcpClientInstances' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientConfig.PcpClientInstances', 
                [], [], 
                '''                A set of PCP client instances.
                ''',
                'pcp_client_instances',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'pcp-client-config',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.PcpClientIpAddress' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.PcpClientIpAddress',
            False, 
            [
            _MetaInfoClassMember('address-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Address identifier
                ''',
                'address_id',
                'ietf-pcp-client', True),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'ip_address',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'pcp-client-ip-address',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.SupportedVersion' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.SupportedVersion',
            False, 
            [
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Indicates a PCP server.
                 Current versions are: 0, 1, and 2.
                ''',
                'version',
                'ietf-pcp-client', True),
            ],
            'ietf-pcp-client',
            'supported-version',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.PcpServerAddress.PcpServerIpAddress' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.PcpServerAddress.PcpServerIpAddress',
            False, 
            [
            _MetaInfoClassMember('address-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier
                ''',
                'address_id',
                'ietf-pcp-client', True),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                An IP address of a PCP server.
                ''',
                'ip_address',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'pcp-server-ip-address',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.PcpServerAddress.SourceEnum' : _MetaInfoEnum('SourceEnum', 'ydk.models.ietf.ietf_pcp_client',
        {
            'manual-configuration':'manual_configuration',
            'dhcpv6':'dhcpv6',
            'dhcpv4':'dhcpv4',
            'else':'else_',
        }, 'ietf-pcp', _yang_ns._namespaces['ietf-pcp']),
    'PcpClientState.PcpClientInstances.PcpClientInstance.PcpServerAddress' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.PcpServerAddress',
            False, 
            [
            _MetaInfoClassMember('pcp-server-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique identifier.
                ''',
                'pcp_server_id',
                'ietf-pcp-client', True),
            _MetaInfoClassMember('client-epoch', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The PCP client's Epoch.
                ''',
                'client_epoch',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('current-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The version that is selected as per the version negotiation
                procedure specified in Section 9 of [RFC6877].
                ''',
                'current_version',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('external-address-familly', REFERENCE_ENUM_CLASS, 'IpVersionEnum' , 'ydk.models.ietf.ietf_inet_types', 'IpVersionEnum', 
                [], [], 
                '''                The address family of the external address(es)
                managed by the PCP server.
                Can be IPv4, IPv6 or both.
                ''',
                'external_address_familly',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('in-use', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether this in-use instance of the server
                is the result of the selection
                process defined in [RFC7488].
                ''',
                'in_use',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('pcp-server-ip-address', REFERENCE_LIST, 'PcpServerIpAddress' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.PcpServerAddress.PcpServerIpAddress', 
                [], [], 
                '''                a list of IP addresses of a PCP server
                ''',
                'pcp_server_ip_address',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('server-epoch', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The PCP server's Epoch.
                ''',
                'server_epoch',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('source', REFERENCE_ENUM_CLASS, 'SourceEnum' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.PcpServerAddress.SourceEnum', 
                [], [], 
                '''                source of the PCP server reachability information.
                ''',
                'source',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('stale-external-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                A stale address that can be used by the PCP client
                to be assigned the same address upon reboot
                or other failure events.
                ''',
                'stale_external_ip_address',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'pcp-server-address',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.OpcodeCapability' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.OpcodeCapability',
            False, 
            [
            _MetaInfoClassMember('announce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ANNOUNCE opcode.
                ''',
                'announce',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('map', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MAP opcode
                ''',
                'map',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('peer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PEER opcode
                ''',
                'peer',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'opcode-capability',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.OptionCapability.Filter' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.OptionCapability.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable FILTER option.
                ''',
                'filter_enabled',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('max-filters', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum number of filters
                 associated with a mapping.
                ''',
                'max_filters',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'filter',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.OptionCapability.Description' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.OptionCapability.Description',
            False, 
            [
            _MetaInfoClassMember('description-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable DESCRIPTION option.
                ''',
                'description_enabled',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('max-description', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum length of the description
                 associated with a mapping.
                ''',
                'max_description',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'description',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.OptionCapability' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.OptionCapability',
            False, 
            [
            _MetaInfoClassMember('description', REFERENCE_CLASS, 'Description' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.OptionCapability.Description', 
                [], [], 
                '''                Associates a description with a mapping [RFC7220].
                ''',
                'description',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('filter', REFERENCE_CLASS, 'Filter' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.OptionCapability.Filter', 
                [], [], 
                '''                This option indicates that filtering incoming packets
                is desired.
                ''',
                'filter',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('port-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether PORT_SET is supported/enabled.
                ''',
                'port_set',
                'ietf-pcp-client', False),
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
                'ietf-pcp-client', False),
            _MetaInfoClassMember('prefix64', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PREFIX64 PCP option [RFC7225].
                ''',
                'prefix64',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('third-party', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                THIRD_PARTY option is used when a PCP client wants
                 to control a mapping to an internal host other
                 than itself [RFC6887].
                ''',
                'third_party',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'option-capability',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.OpcodeConfiguration' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.OpcodeConfiguration',
            False, 
            [
            _MetaInfoClassMember('announce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ANNOUNCE opcode.
                ''',
                'announce',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('map', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MAP opcode
                ''',
                'map',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('peer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PEER opcode
                ''',
                'peer',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'opcode-configuration',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.OptionConfiguration.Filter' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.OptionConfiguration.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable FILTER option.
                ''',
                'filter_enabled',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('max-filters', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum number of filters
                 associated with a mapping.
                ''',
                'max_filters',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'filter',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.OptionConfiguration.Description' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.OptionConfiguration.Description',
            False, 
            [
            _MetaInfoClassMember('description-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable DESCRIPTION option.
                ''',
                'description_enabled',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('max-description', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum length of the description
                 associated with a mapping.
                ''',
                'max_description',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'description',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.OptionConfiguration' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.OptionConfiguration',
            False, 
            [
            _MetaInfoClassMember('description', REFERENCE_CLASS, 'Description' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.OptionConfiguration.Description', 
                [], [], 
                '''                Associates a description with a mapping [RFC7220].
                ''',
                'description',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('filter', REFERENCE_CLASS, 'Filter' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.OptionConfiguration.Filter', 
                [], [], 
                '''                This option indicates that filtering incoming packets
                is desired.
                ''',
                'filter',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('port-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether PORT_SET is supported/enabled.
                ''',
                'port_set',
                'ietf-pcp-client', False),
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
                'ietf-pcp-client', False),
            _MetaInfoClassMember('prefix64', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PREFIX64 PCP option [RFC7225].
                ''',
                'prefix64',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('third-party', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                THIRD_PARTY option is used when a PCP client wants
                 to control a mapping to an internal host other
                 than itself [RFC6887].
                ''',
                'third_party',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'option-configuration',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.InternalPort' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.InternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'internal-port',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.ExternalPort' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.ExternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'external-port',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.Filter' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of the filter.
                ''',
                'filter_id',
                'ietf-pcp-client', True),
            _MetaInfoClassMember('remote-ip-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IP address of the remote peer.
                ''',
                'remote_ip_prefix',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('remote-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The port number of the remote peer. Value 0
                indicates 'all ports'.
                ''',
                'remote_port_number',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'filter',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.StatusCodeEnum' : _MetaInfoEnum('StatusCodeEnum', 'ydk.models.ietf.ietf_pcp_client',
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
    'PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.ietf.ietf_pcp_client',
        {
            'disabled':'disabled',
            'requested':'requested',
            'assigned':'assigned',
            'stale':'stale',
        }, 'ietf-pcp', _yang_ns._namespaces['ietf-pcp']),
    'PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique identifier of a mapping entry.
                ''',
                'index',
                'ietf-pcp-client', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                a description string associated with the mapping.
                ''',
                'description',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('external-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                External IP address. Can be 'Suggested' or 'Assigned'.
                
                It can be set by a client to stale-ip-address, if available
                or to (::) (for requesting external IPv6 addresses)
                or (::ffff:0:0) (for requesting external IPv4 addresses).
                ''',
                'external_ip_address',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('external-port', REFERENCE_CLASS, 'ExternalPort' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.ExternalPort', 
                [], [], 
                '''                External port number. Can be 'Suggested' or 'Assigned'.
                ''',
                'external_port',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('filter', REFERENCE_LIST, 'Filter' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.Filter', 
                [], [], 
                '''                a list of filters associated with the mapping.
                ''',
                'filter',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('internal-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Corresponds to the PCP Client's IP Address
                defined in [RFC6887].
                ''',
                'internal_ip_address',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('internal-port', REFERENCE_CLASS, 'InternalPort' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.InternalPort', 
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
                'ietf-pcp-client', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lifetime of the mapping.
                 Can be requested/assigned/remaining
                ''',
                'lifetime',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('mapping-nonce', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A random value chosen by the PCP client
                ''',
                'mapping_nonce',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('prefer-failure-tagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                a tag which indicates whether PREFER_FAILURE
                 is (to be) used.
                ''',
                'prefer_failure_tagged',
                'ietf-pcp-client', False),
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
                'ietf-pcp-client', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.StatusEnum', 
                [], [], 
                '''                Indicates the status of a mapping entry.
                ''',
                'status',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('status-code', REFERENCE_ENUM_CLASS, 'StatusCodeEnum' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.StatusCodeEnum', 
                [], [], 
                '''                result status code.
                ''',
                'status_code',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('third-party-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                used to indicate the internal IP address
                 when THIRD_PARTY is in use.
                ''',
                'third_party_address',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'mapping-entry',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable',
            False, 
            [
            _MetaInfoClassMember('mapping-entry', REFERENCE_LIST, 'MappingEntry' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry', 
                [], [], 
                '''                Mapping entry
                ''',
                'mapping_entry',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'mapping-table',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics.TrafficStatistics_' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics.TrafficStatistics_',
            False, 
            [
            _MetaInfoClassMember('dropped-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for dropped traffic in bytes.
                ''',
                'dropped_byte',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('dropped-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for dropped packets.
                ''',
                'dropped_packet',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('rcvd-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received traffic in bytes.
                ''',
                'rcvd_byte',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('rcvd-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received packets.
                ''',
                'rcvd_packet',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('sent-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent traffic in bytes.
                ''',
                'sent_byte',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('sent-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets sent
                ''',
                'sent_packet',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'traffic-statistics',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics.OpcodeStatistics' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics.OpcodeStatistics',
            False, 
            [
            _MetaInfoClassMember('rcvd-announce', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received ANNOUNCED messages
                ''',
                'rcvd_announce',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('rcvd-malformed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received malformed opcodes
                ''',
                'rcvd_malformed',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('rcvd-map', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received MAP messages
                ''',
                'rcvd_map',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('rcvd-peer', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received PEER messages
                ''',
                'rcvd_peer',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('rcvd-unknown', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received unknown opcodes
                ''',
                'rcvd_unknown',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('sent-annonce', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent ANNOUNCE messages
                ''',
                'sent_annonce',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('sent-map', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent MAP messages
                ''',
                'sent_map',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('sent-peer', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent PEER messages
                ''',
                'sent_peer',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'opcode-statistics',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics.MappingTable' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics.MappingTable',
            False, 
            [
            _MetaInfoClassMember('current-mt-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Size of the mapping table
                ''',
                'current_mt_size',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('max-mt-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum configured size of the mapping table.
                ''',
                'max_mt_size',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'mapping-table',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics',
            False, 
            [
            _MetaInfoClassMember('mapping-table', REFERENCE_CLASS, 'MappingTable' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics.MappingTable', 
                [], [], 
                '''                mapping table related statistics.
                ''',
                'mapping_table',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('opcode-statistics', REFERENCE_CLASS, 'OpcodeStatistics' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics.OpcodeStatistics', 
                [], [], 
                '''                Opcode-related statistics.
                ''',
                'opcode_statistics',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('traffic-statistics', REFERENCE_CLASS, 'TrafficStatistics_' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics.TrafficStatistics_', 
                [], [], 
                '''                Generic traffic statistics.
                ''',
                'traffic_statistics',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'traffic-statistics',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances.PcpClientInstance' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances.PcpClientInstance',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                PCP client instance identifier.
                ''',
                'id',
                'ietf-pcp-client', True),
            _MetaInfoClassMember('authentication-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable PCP authentication
                ''',
                'authentication_enabled',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('authentication-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether PCP authentication is
                 supported.
                ''',
                'authentication_support',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('mapping-table', REFERENCE_CLASS, 'MappingTable' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable', 
                [], [], 
                '''                Mapping table
                ''',
                'mapping_table',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A name associated with the PCP client instance.
                ''',
                'name',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('opcode-capability', REFERENCE_CLASS, 'OpcodeCapability' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.OpcodeCapability', 
                [], [], 
                '''                Opcode-related capabilities.
                ''',
                'opcode_capability',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('opcode-configuration', REFERENCE_CLASS, 'OpcodeConfiguration' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.OpcodeConfiguration', 
                [], [], 
                '''                Opcode-related configuration.
                ''',
                'opcode_configuration',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('option-capability', REFERENCE_CLASS, 'OptionCapability' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.OptionCapability', 
                [], [], 
                '''                Option-related capabilities
                ''',
                'option_capability',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('option-configuration', REFERENCE_CLASS, 'OptionConfiguration' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.OptionConfiguration', 
                [], [], 
                '''                Option-related configuration.
                ''',
                'option_configuration',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('pcp-client-ip-address', REFERENCE_LIST, 'PcpClientIpAddress' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.PcpClientIpAddress', 
                [], [], 
                '''                list of configured PCP client addresses.
                ''',
                'pcp_client_ip_address',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('pcp-server-address', REFERENCE_LIST, 'PcpServerAddress' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.PcpServerAddress', 
                [], [], 
                '''                list of provisioned PCP server.
                ''',
                'pcp_server_address',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('preferred-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The preferred version configured
                 by an administrator.
                ''',
                'preferred_version',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('supported-version', REFERENCE_LIST, 'SupportedVersion' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.SupportedVersion', 
                [], [], 
                '''                list of supported PCP versions
                ''',
                'supported_version',
                'ietf-pcp-client', False),
            _MetaInfoClassMember('traffic-statistics', REFERENCE_CLASS, 'TrafficStatistics' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics', 
                [], [], 
                '''                traffic statistics.
                ''',
                'traffic_statistics',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'pcp-client-instance',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState.PcpClientInstances' : {
        'meta_info' : _MetaInfoClass('PcpClientState.PcpClientInstances',
            False, 
            [
            _MetaInfoClassMember('pcp-client-instance', REFERENCE_LIST, 'PcpClientInstance' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances.PcpClientInstance', 
                [], [], 
                '''                PCP client instance
                ''',
                'pcp_client_instance',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'pcp-client-instances',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
    'PcpClientState' : {
        'meta_info' : _MetaInfoClass('PcpClientState',
            False, 
            [
            _MetaInfoClassMember('pcp-client-instances', REFERENCE_CLASS, 'PcpClientInstances' , 'ydk.models.ietf.ietf_pcp_client', 'PcpClientState.PcpClientInstances', 
                [], [], 
                '''                PCP client instances
                ''',
                'pcp_client_instances',
                'ietf-pcp-client', False),
            ],
            'ietf-pcp-client',
            'pcp-client-state',
            _yang_ns._namespaces['ietf-pcp-client'],
        'ydk.models.ietf.ietf_pcp_client'
        ),
    },
}
_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.PcpServers.PcpServerIpAddress']['meta_info'].parent =_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.PcpServers']['meta_info']
_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.OptionConfiguration.Filter']['meta_info'].parent =_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.OptionConfiguration']['meta_info']
_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.OptionConfiguration.Description']['meta_info'].parent =_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.OptionConfiguration']['meta_info']
_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.InternalPort']['meta_info'].parent =_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.ExternalPort']['meta_info'].parent =_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.Filter']['meta_info'].parent =_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry']['meta_info'].parent =_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable']['meta_info']
_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.Version']['meta_info'].parent =_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance']['meta_info']
_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.PcpServers']['meta_info'].parent =_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance']['meta_info']
_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.OpcodeConfiguration']['meta_info'].parent =_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance']['meta_info']
_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.OptionConfiguration']['meta_info'].parent =_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance']['meta_info']
_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance.MappingTable']['meta_info'].parent =_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance']['meta_info']
_meta_table['PcpClientConfig.PcpClientInstances.PcpClientInstance']['meta_info'].parent =_meta_table['PcpClientConfig.PcpClientInstances']['meta_info']
_meta_table['PcpClientConfig.PcpClientInstances']['meta_info'].parent =_meta_table['PcpClientConfig']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.PcpServerAddress.PcpServerIpAddress']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.PcpServerAddress']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.OptionCapability.Filter']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.OptionCapability']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.OptionCapability.Description']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.OptionCapability']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.OptionConfiguration.Filter']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.OptionConfiguration']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.OptionConfiguration.Description']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.OptionConfiguration']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.InternalPort']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.ExternalPort']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry.Filter']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable.MappingEntry']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics.TrafficStatistics_']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics.OpcodeStatistics']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics.MappingTable']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.PcpClientIpAddress']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.SupportedVersion']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.PcpServerAddress']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.OpcodeCapability']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.OptionCapability']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.OpcodeConfiguration']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.OptionConfiguration']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.MappingTable']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance.TrafficStatistics']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance']['meta_info']
_meta_table['PcpClientState.PcpClientInstances.PcpClientInstance']['meta_info'].parent =_meta_table['PcpClientState.PcpClientInstances']['meta_info']
_meta_table['PcpClientState.PcpClientInstances']['meta_info'].parent =_meta_table['PcpClientState']['meta_info']
