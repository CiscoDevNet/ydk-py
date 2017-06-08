


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.Version' : {
        'meta_info' : _MetaInfoClass('PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.Version',
            False, 
            [
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Indicates a PCP server.
                 Current versions are: 0, 1, and 2.
                ''',
                'version',
                'ietf-pcp-iwf', True),
            ],
            'ietf-pcp-iwf',
            'version',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServers.PcpServerIpAddress' : {
        'meta_info' : _MetaInfoClass('PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServers.PcpServerIpAddress',
            False, 
            [
            _MetaInfoClassMember('address-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier
                ''',
                'address_id',
                'ietf-pcp-iwf', True),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                An IP address of a PCP server.
                ''',
                'ip_address',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'pcp-server-ip-address',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServers' : {
        'meta_info' : _MetaInfoClass('PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServers',
            False, 
            [
            _MetaInfoClassMember('pcp-server-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique identifier.
                ''',
                'pcp_server_id',
                'ietf-pcp-iwf', True),
            _MetaInfoClassMember('external-address-familly', REFERENCE_ENUM_CLASS, 'IpVersionEnum' , 'ydk.models.ietf.ietf_inet_types', 'IpVersionEnum', 
                [], [], 
                '''                The address family of the external address(es)
                managed by the PCP server.
                Can be IPv4, IPv6 or both.
                ''',
                'external_address_familly',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('pcp-server-ip-address', REFERENCE_LIST, 'PcpServerIpAddress' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServers.PcpServerIpAddress', 
                [], [], 
                '''                a list of IP addresses of a PCP server
                ''',
                'pcp_server_ip_address',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('stale-external-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                A stale address that can be used by the PCP client
                to be assigned the same address upon reboot
                or other failure events.
                ''',
                'stale_external_ip_address',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'pcp-servers',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersion.IgdVersionEnum' : _MetaInfoEnum('IgdVersionEnum', 'ydk.models.ietf.ietf_pcp_iwf',
        {
            'igd:1':'igd__COLON__1',
            'igd:2':'igd__COLON__2',
            'both':'both',
        }, 'ietf-pcp-iwf', _yang_ns._namespaces['ietf-pcp-iwf']),
    'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersion' : {
        'meta_info' : _MetaInfoClass('PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersion',
            False, 
            [
            _MetaInfoClassMember('igd-version', REFERENCE_ENUM_CLASS, 'IgdVersionEnum' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersion.IgdVersionEnum', 
                [], [], 
                '''                UPnP IGD Version
                ''',
                'igd_version',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'igd-version',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.InternalPort' : {
        'meta_info' : _MetaInfoClass('PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.InternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'internal-port',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.ExternalPort' : {
        'meta_info' : _MetaInfoClass('PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.ExternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'external-port',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.Filter' : {
        'meta_info' : _MetaInfoClass('PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of the filter.
                ''',
                'filter_id',
                'ietf-pcp-iwf', True),
            _MetaInfoClassMember('remote-ip-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IP address of the remote peer.
                ''',
                'remote_ip_prefix',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('remote-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The port number of the remote peer. Value 0
                indicates 'all ports'.
                ''',
                'remote_port_number',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'filter',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.ietf.ietf_pcp_iwf',
        {
            'disabled':'disabled',
            'requested':'requested',
            'assigned':'assigned',
            'stale':'stale',
        }, 'ietf-pcp', _yang_ns._namespaces['ietf-pcp']),
    'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry' : {
        'meta_info' : _MetaInfoClass('PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique identifier of a mapping entry.
                ''',
                'index',
                'ietf-pcp-iwf', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                a description string associated with the mapping.
                ''',
                'description',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('external-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                External IP address. Can be 'Suggested' or 'Assigned'.
                
                It can be set by a client to stale-ip-address, if available
                or to (::) (for requesting external IPv6 addresses)
                or (::ffff:0:0) (for requesting external IPv4 addresses).
                ''',
                'external_ip_address',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('external-port', REFERENCE_CLASS, 'ExternalPort' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.ExternalPort', 
                [], [], 
                '''                External port number. Can be 'Suggested' or 'Assigned'.
                ''',
                'external_port',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('filter', REFERENCE_LIST, 'Filter' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.Filter', 
                [], [], 
                '''                a list of filters associated with the mapping.
                ''',
                'filter',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('igd-control-point-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the UPnP Control Point.
                ''',
                'igd_control_point_address',
                'ietf-pcp-iwf', False, [
                    _MetaInfoClassMember('igd-control-point-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the UPnP Control Point.
                        ''',
                        'igd_control_point_address',
                        'ietf-pcp-iwf', False),
                    _MetaInfoClassMember('igd-control-point-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the UPnP Control Point.
                        ''',
                        'igd_control_point_address',
                        'ietf-pcp-iwf', False),
                ]),
            _MetaInfoClassMember('igd-control-point-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port number
                ''',
                'igd_control_point_port',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('internal-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Corresponds to the PCP Client's IP Address
                defined in [RFC6887].
                ''',
                'internal_ip_address',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('internal-port', REFERENCE_CLASS, 'InternalPort' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.InternalPort', 
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
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lifetime of the mapping.
                 Can be requested/assigned/remaining
                ''',
                'lifetime',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('mapping-nonce', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A random value chosen by the PCP client
                ''',
                'mapping_nonce',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('prefer-failure-tagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                a tag which indicates whether PREFER_FAILURE
                 is (to be) used.
                ''',
                'prefer_failure_tagged',
                'ietf-pcp-iwf', False),
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
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.StatusEnum', 
                [], [], 
                '''                Indicates the status of a mapping entry.
                ''',
                'status',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('third-party-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                used to indicate the internal IP address
                 when THIRD_PARTY is in use.
                ''',
                'third_party_address',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'mapping-entry',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable' : {
        'meta_info' : _MetaInfoClass('PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable',
            False, 
            [
            _MetaInfoClassMember('mapping-entry', REFERENCE_LIST, 'MappingEntry' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry', 
                [], [], 
                '''                PCP Mapping Entry.
                ''',
                'mapping_entry',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'mapping-table',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance' : {
        'meta_info' : _MetaInfoClass('PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of the IWF instance.
                ''',
                'id',
                'ietf-pcp-iwf', True),
            _MetaInfoClassMember('authentication-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable PCP authentication
                ''',
                'authentication_enable',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('igd-version', REFERENCE_CLASS, 'IgdVersion' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersion', 
                [], [], 
                '''                Configure UPnP IGD version(s).
                ''',
                'igd_version',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('mapping-table', REFERENCE_CLASS, 'MappingTable' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable', 
                [], [], 
                '''                Mapping table as maintained by a
                 UPnP IGD-PCP IWF instance
                ''',
                'mapping_table',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A name of the UPnP IGD-PCP IWF instance
                ''',
                'name',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('pcp-servers', REFERENCE_LIST, 'PcpServers' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServers', 
                [], [], 
                '''                List of configured PCP servers.
                ''',
                'pcp_servers',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('version', REFERENCE_LIST, 'Version' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.Version', 
                [], [], 
                '''                configures one or several PCP versions.
                ''',
                'version',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'pcp-igd-iwf-instance',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfConfig.PcpIgdIwfInstances' : {
        'meta_info' : _MetaInfoClass('PcpIwfConfig.PcpIgdIwfInstances',
            False, 
            [
            _MetaInfoClassMember('pcp-igd-iwf-instance', REFERENCE_LIST, 'PcpIgdIwfInstance' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance', 
                [], [], 
                '''                UPnP IGD/PCP Interworking Function instance
                ''',
                'pcp_igd_iwf_instance',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'pcp-igd-iwf-instances',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfConfig' : {
        'meta_info' : _MetaInfoClass('PcpIwfConfig',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable the UPnP IGD-PCP IWF
                ''',
                'enable',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('pcp-igd-iwf-instances', REFERENCE_CLASS, 'PcpIgdIwfInstances' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfConfig.PcpIgdIwfInstances', 
                [], [], 
                '''                UPnP IGD/PCP Interworking Function instances
                ''',
                'pcp_igd_iwf_instances',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'pcp-iwf-config',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.SupportedVersion' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.SupportedVersion',
            False, 
            [
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Indicates a PCP server.
                 Current versions are: 0, 1, and 2.
                ''',
                'version',
                'ietf-pcp-iwf', True),
            ],
            'ietf-pcp-iwf',
            'supported-version',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpIgdIwfIpAddress' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpIgdIwfIpAddress',
            False, 
            [
            _MetaInfoClassMember('address-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of the address
                ''',
                'address_id',
                'ietf-pcp-iwf', True),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                An address of the UPnP IGD-PCP IWF
                ''',
                'ip_address',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'pcp-igd-iwf-ip-address',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersionCapability.IgdVersionEnum' : _MetaInfoEnum('IgdVersionEnum', 'ydk.models.ietf.ietf_pcp_iwf',
        {
            'igd:1':'igd__COLON__1',
            'igd:2':'igd__COLON__2',
            'both':'both',
        }, 'ietf-pcp-iwf', _yang_ns._namespaces['ietf-pcp-iwf']),
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersionCapability' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersionCapability',
            False, 
            [
            _MetaInfoClassMember('igd-version', REFERENCE_ENUM_CLASS, 'IgdVersionEnum' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersionCapability.IgdVersionEnum', 
                [], [], 
                '''                UPnP IGD Version
                ''',
                'igd_version',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'igd-version-capability',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.EnabledIgdVersion.IgdVersionEnum' : _MetaInfoEnum('IgdVersionEnum', 'ydk.models.ietf.ietf_pcp_iwf',
        {
            'igd:1':'igd__COLON__1',
            'igd:2':'igd__COLON__2',
            'both':'both',
        }, 'ietf-pcp-iwf', _yang_ns._namespaces['ietf-pcp-iwf']),
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.EnabledIgdVersion' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.EnabledIgdVersion',
            False, 
            [
            _MetaInfoClassMember('igd-version', REFERENCE_ENUM_CLASS, 'IgdVersionEnum' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.EnabledIgdVersion.IgdVersionEnum', 
                [], [], 
                '''                UPnP IGD Version
                ''',
                'igd_version',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'enabled-igd-version',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress.PcpServerIpAddress' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress.PcpServerIpAddress',
            False, 
            [
            _MetaInfoClassMember('address-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier
                ''',
                'address_id',
                'ietf-pcp-iwf', True),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                An IP address of a PCP server.
                ''',
                'ip_address',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'pcp-server-ip-address',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress.SourceEnum' : _MetaInfoEnum('SourceEnum', 'ydk.models.ietf.ietf_pcp_iwf',
        {
            'manual-configuration':'manual_configuration',
            'dhcpv6':'dhcpv6',
            'dhcpv4':'dhcpv4',
            'else':'else_',
        }, 'ietf-pcp', _yang_ns._namespaces['ietf-pcp']),
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress',
            False, 
            [
            _MetaInfoClassMember('pcp-server-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique identifier.
                ''',
                'pcp_server_id',
                'ietf-pcp-iwf', True),
            _MetaInfoClassMember('client-epoch', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The PCP client's Epoch.
                ''',
                'client_epoch',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('current-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The version that is selected as per the version negotiation
                procedure specified in Section 9 of [RFC6877].
                ''',
                'current_version',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('external-address-familly', REFERENCE_ENUM_CLASS, 'IpVersionEnum' , 'ydk.models.ietf.ietf_inet_types', 'IpVersionEnum', 
                [], [], 
                '''                The address family of the external address(es)
                managed by the PCP server.
                Can be IPv4, IPv6 or both.
                ''',
                'external_address_familly',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('in-use', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether this in-use instance of the server
                is the result of the selection
                process defined in [RFC7488].
                ''',
                'in_use',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('pcp-server-ip-address', REFERENCE_LIST, 'PcpServerIpAddress' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress.PcpServerIpAddress', 
                [], [], 
                '''                a list of IP addresses of a PCP server
                ''',
                'pcp_server_ip_address',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('server-epoch', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The PCP server's Epoch.
                ''',
                'server_epoch',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('source', REFERENCE_ENUM_CLASS, 'SourceEnum' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress.SourceEnum', 
                [], [], 
                '''                source of the PCP server reachability information.
                ''',
                'source',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('stale-external-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                A stale address that can be used by the PCP client
                to be assigned the same address upon reboot
                or other failure events.
                ''',
                'stale_external_ip_address',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'pcp-server-address',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.InternalPort' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.InternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'internal-port',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.ExternalPort' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.ExternalPort',
            False, 
            [
            _MetaInfoClassMember('end-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                End of the port range.
                ''',
                'end_port_number',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('single-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                used for single port numbers.
                ''',
                'single_port_number',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('start-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Begining of the port range.
                ''',
                'start_port_number',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'external-port',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.Filter' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.Filter',
            False, 
            [
            _MetaInfoClassMember('filter-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier of the filter.
                ''',
                'filter_id',
                'ietf-pcp-iwf', True),
            _MetaInfoClassMember('remote-ip-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IP address of the remote peer.
                ''',
                'remote_ip_prefix',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('remote-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The port number of the remote peer. Value 0
                indicates 'all ports'.
                ''',
                'remote_port_number',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'filter',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.StatusCodeEnum' : _MetaInfoEnum('StatusCodeEnum', 'ydk.models.ietf.ietf_pcp_iwf',
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
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.ietf.ietf_pcp_iwf',
        {
            'disabled':'disabled',
            'requested':'requested',
            'assigned':'assigned',
            'stale':'stale',
        }, 'ietf-pcp', _yang_ns._namespaces['ietf-pcp']),
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A unique identifier of a mapping entry.
                ''',
                'index',
                'ietf-pcp-iwf', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                a description string associated with the mapping.
                ''',
                'description',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('external-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                External IP address. Can be 'Suggested' or 'Assigned'.
                
                It can be set by a client to stale-ip-address, if available
                or to (::) (for requesting external IPv6 addresses)
                or (::ffff:0:0) (for requesting external IPv4 addresses).
                ''',
                'external_ip_address',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('external-port', REFERENCE_CLASS, 'ExternalPort' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.ExternalPort', 
                [], [], 
                '''                External port number. Can be 'Suggested' or 'Assigned'.
                ''',
                'external_port',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('filter', REFERENCE_LIST, 'Filter' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.Filter', 
                [], [], 
                '''                a list of filters associated with the mapping.
                ''',
                'filter',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('igd-control-point-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address of a UPnP Control Point
                ''',
                'igd_control_point_address',
                'ietf-pcp-iwf', False, [
                    _MetaInfoClassMember('igd-control-point-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address of a UPnP Control Point
                        ''',
                        'igd_control_point_address',
                        'ietf-pcp-iwf', False),
                    _MetaInfoClassMember('igd-control-point-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address of a UPnP Control Point
                        ''',
                        'igd_control_point_address',
                        'ietf-pcp-iwf', False),
                ]),
            _MetaInfoClassMember('igd-control-point-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The port number of a UPnP Control Point
                ''',
                'igd_control_point_port',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('internal-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Corresponds to the PCP Client's IP Address
                defined in [RFC6887].
                ''',
                'internal_ip_address',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('internal-port', REFERENCE_CLASS, 'InternalPort' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.InternalPort', 
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
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lifetime of the mapping.
                 Can be requested/assigned/remaining
                ''',
                'lifetime',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('mapping-nonce', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A random value chosen by the PCP client
                ''',
                'mapping_nonce',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('prefer-failure-tagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                a tag which indicates whether PREFER_FAILURE
                 is (to be) used.
                ''',
                'prefer_failure_tagged',
                'ietf-pcp-iwf', False),
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
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.StatusEnum', 
                [], [], 
                '''                Indicates the status of a mapping entry.
                ''',
                'status',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('status-code', REFERENCE_ENUM_CLASS, 'StatusCodeEnum' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.StatusCodeEnum', 
                [], [], 
                '''                result status code.
                ''',
                'status_code',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('third-party-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                used to indicate the internal IP address
                 when THIRD_PARTY is in use.
                ''',
                'third_party_address',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'mapping-entry',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable',
            False, 
            [
            _MetaInfoClassMember('mapping-entry', REFERENCE_LIST, 'MappingEntry' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry', 
                [], [], 
                '''                PCP mapping entry.
                ''',
                'mapping_entry',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'mapping-table',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.TrafficStatistics_' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.TrafficStatistics_',
            False, 
            [
            _MetaInfoClassMember('dropped-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for dropped traffic in bytes.
                ''',
                'dropped_byte',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('dropped-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for dropped packets.
                ''',
                'dropped_packet',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('rcvd-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received traffic in bytes.
                ''',
                'rcvd_byte',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('rcvd-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received packets.
                ''',
                'rcvd_packet',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('sent-byte', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent traffic in bytes.
                ''',
                'sent_byte',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('sent-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets sent
                ''',
                'sent_packet',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'traffic-statistics',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.OpcodeStatistics' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.OpcodeStatistics',
            False, 
            [
            _MetaInfoClassMember('rcvd-announce', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received ANNOUNCED messages
                ''',
                'rcvd_announce',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('rcvd-malformed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received malformed opcodes
                ''',
                'rcvd_malformed',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('rcvd-map', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received MAP messages
                ''',
                'rcvd_map',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('rcvd-peer', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received PEER messages
                ''',
                'rcvd_peer',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('rcvd-unknown', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for received unknown opcodes
                ''',
                'rcvd_unknown',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('sent-annonce', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent ANNOUNCE messages
                ''',
                'sent_annonce',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('sent-map', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent MAP messages
                ''',
                'sent_map',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('sent-peer', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter for sent PEER messages
                ''',
                'sent_peer',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'opcode-statistics',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.MappingTable' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.MappingTable',
            False, 
            [
            _MetaInfoClassMember('current-mt-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Size of the mapping table
                ''',
                'current_mt_size',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('max-mt-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum configured size of the mapping table.
                ''',
                'max_mt_size',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'mapping-table',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics',
            False, 
            [
            _MetaInfoClassMember('mapping-table', REFERENCE_CLASS, 'MappingTable' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.MappingTable', 
                [], [], 
                '''                Mapping table related statistics
                ''',
                'mapping_table',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('opcode-statistics', REFERENCE_CLASS, 'OpcodeStatistics' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.OpcodeStatistics', 
                [], [], 
                '''                Opcode-related statistics.
                ''',
                'opcode_statistics',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('traffic-statistics', REFERENCE_CLASS, 'TrafficStatistics_' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.TrafficStatistics_', 
                [], [], 
                '''                Generic traffic statistics.
                ''',
                'traffic_statistics',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'traffic-statistics',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                the identifier of the instance
                ''',
                'id',
                'ietf-pcp-iwf', True),
            _MetaInfoClassMember('authentication-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether PCP authentication
                 is enabled.
                ''',
                'authentication_enabled',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('authentication-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether PCP authentication is
                 supported.
                ''',
                'authentication_support',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('enabled-igd-version', REFERENCE_CLASS, 'EnabledIgdVersion' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.EnabledIgdVersion', 
                [], [], 
                '''                Configured UPnP IGD versions
                ''',
                'enabled_igd_version',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('igd-version-capability', REFERENCE_CLASS, 'IgdVersionCapability' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersionCapability', 
                [], [], 
                '''                List of supported UPnP IGD versions.
                ''',
                'igd_version_capability',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('mapping-table', REFERENCE_CLASS, 'MappingTable' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable', 
                [], [], 
                '''                PCP Mapping table
                ''',
                'mapping_table',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                the name of the instance
                ''',
                'name',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('pcp-igd-iwf-ip-address', REFERENCE_LIST, 'PcpIgdIwfIpAddress' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpIgdIwfIpAddress', 
                [], [], 
                '''                local IP addresses of the UPnP IGD-PCP IWF
                ''',
                'pcp_igd_iwf_ip_address',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('pcp-server-address', REFERENCE_LIST, 'PcpServerAddress' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress', 
                [], [], 
                '''                List of provisioned PCP servers
                ''',
                'pcp_server_address',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('preferred-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Preferred version
                ''',
                'preferred_version',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('supported-version', REFERENCE_LIST, 'SupportedVersion' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.SupportedVersion', 
                [], [], 
                '''                list of supported PCP versions.
                ''',
                'supported_version',
                'ietf-pcp-iwf', False),
            _MetaInfoClassMember('traffic-statistics', REFERENCE_CLASS, 'TrafficStatistics' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics', 
                [], [], 
                '''                traffic statistics
                ''',
                'traffic_statistics',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'pcp-igd-iwf-instance',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState.PcpIgdIwfInstances' : {
        'meta_info' : _MetaInfoClass('PcpIwfState.PcpIgdIwfInstances',
            False, 
            [
            _MetaInfoClassMember('pcp-igd-iwf-instance', REFERENCE_LIST, 'PcpIgdIwfInstance' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance', 
                [], [], 
                '''                UPnP IGD/PCP Interworking Function instance
                ''',
                'pcp_igd_iwf_instance',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'pcp-igd-iwf-instances',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
    'PcpIwfState' : {
        'meta_info' : _MetaInfoClass('PcpIwfState',
            False, 
            [
            _MetaInfoClassMember('pcp-igd-iwf-instances', REFERENCE_CLASS, 'PcpIgdIwfInstances' , 'ydk.models.ietf.ietf_pcp_iwf', 'PcpIwfState.PcpIgdIwfInstances', 
                [], [], 
                '''                UPnP IGD/PCP Interworking Function instances
                ''',
                'pcp_igd_iwf_instances',
                'ietf-pcp-iwf', False),
            ],
            'ietf-pcp-iwf',
            'pcp-iwf-state',
            _yang_ns._namespaces['ietf-pcp-iwf'],
        'ydk.models.ietf.ietf_pcp_iwf'
        ),
    },
}
_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServers.PcpServerIpAddress']['meta_info'].parent =_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServers']['meta_info']
_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.InternalPort']['meta_info'].parent =_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.ExternalPort']['meta_info'].parent =_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.Filter']['meta_info'].parent =_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry']['meta_info'].parent =_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable']['meta_info']
_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.Version']['meta_info'].parent =_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info']
_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServers']['meta_info'].parent =_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info']
_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersion']['meta_info'].parent =_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info']
_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable']['meta_info'].parent =_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info']
_meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info'].parent =_meta_table['PcpIwfConfig.PcpIgdIwfInstances']['meta_info']
_meta_table['PcpIwfConfig.PcpIgdIwfInstances']['meta_info'].parent =_meta_table['PcpIwfConfig']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress.PcpServerIpAddress']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.InternalPort']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.ExternalPort']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.Filter']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.TrafficStatistics_']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.OpcodeStatistics']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.MappingTable']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.SupportedVersion']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpIgdIwfIpAddress']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersionCapability']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.EnabledIgdVersion']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info'].parent =_meta_table['PcpIwfState.PcpIgdIwfInstances']['meta_info']
_meta_table['PcpIwfState.PcpIgdIwfInstances']['meta_info'].parent =_meta_table['PcpIwfState']['meta_info']
