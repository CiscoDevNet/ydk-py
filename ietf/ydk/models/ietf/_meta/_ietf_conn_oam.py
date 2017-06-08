


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'IdentifierFormatIdentity' : {
        'meta_info' : _MetaInfoClass('IdentifierFormatIdentity',
            False, 
            [
            ],
            'ietf-conn-oam',
            'identifier-format',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'TechnologyTypesIdentity' : {
        'meta_info' : _MetaInfoClass('TechnologyTypesIdentity',
            False, 
            [
            ],
            'ietf-conn-oam',
            'technology-types',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'NameFormatIdentity' : {
        'meta_info' : _MetaInfoClass('NameFormatIdentity',
            False, 
            [
            ],
            'ietf-conn-oam',
            'name-format',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'CommandSubTypeIdentity' : {
        'meta_info' : _MetaInfoClass('CommandSubTypeIdentity',
            False, 
            [
            ],
            'ietf-conn-oam',
            'command-sub-type',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'DefectTypesIdentity' : {
        'meta_info' : _MetaInfoClass('DefectTypesIdentity',
            False, 
            [
            ],
            'ietf-conn-oam',
            'defect-types',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'Domains.Domain.Mas.Ma.Mep.Session.DestinationMep' : {
        'meta_info' : _MetaInfoClass('Domains.Domain.Mas.Ma.Mep.Session.DestinationMep',
            False, 
            [
            _MetaInfoClassMember('MEP-ID-format', REFERENCE_IDENTITY_CLASS, 'IdentifierFormatIdentity' , 'ydk.models.ietf.ietf_conn_oam', 'IdentifierFormatIdentity', 
                [], [], 
                '''                MEP ID format.
                ''',
                'mep_id_format',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MEP-ID-int', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                MEP ID in integer format
                ''',
                'mep_id_int',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'destination-mep',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'Domains.Domain.Mas.Ma.Mep.Session.DestinationMepAddress' : {
        'meta_info' : _MetaInfoClass('Domains.Domain.Mas.Ma.Mep.Session.DestinationMepAddress',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC Address
                ''',
                'mac_address',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'destination-mep-address',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'Domains.Domain.Mas.Ma.Mep.Session' : {
        'meta_info' : _MetaInfoClass('Domains.Domain.Mas.Ma.Mep.Session',
            False, 
            [
            _MetaInfoClassMember('session-cookie', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cookie to identify different sessions, when there
                are multiple remote MEPs or multiple sessions to
                the same remote MEP.
                ''',
                'session_cookie',
                'ietf-conn-oam', True),
            _MetaInfoClassMember('cos-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class of service
                ''',
                'cos_id',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('destination-mep', REFERENCE_CLASS, 'DestinationMep' , 'ydk.models.ietf.ietf_conn_oam', 'Domains.Domain.Mas.Ma.Mep.Session.DestinationMep', 
                [], [], 
                '''                Destination MEP
                ''',
                'destination_mep',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('destination-mep-address', REFERENCE_CLASS, 'DestinationMepAddress' , 'ydk.models.ietf.ietf_conn_oam', 'Domains.Domain.Mas.Ma.Mep.Session.DestinationMepAddress', 
                [], [], 
                '''                Destination MEP Address
                ''',
                'destination_mep_address',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'session',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'Domains.Domain.Mas.Ma.Mep' : {
        'meta_info' : _MetaInfoClass('Domains.Domain.Mas.Ma.Mep',
            False, 
            [
            _MetaInfoClassMember('mep-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Generic administrative name of the MEP
                ''',
                'mep_name',
                'ietf-conn-oam', True),
            _MetaInfoClassMember('cc-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate whether the CC enable.
                ''',
                'cc_enable',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('cos-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class of service
                ''',
                'cos_id',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC Address
                ''',
                'mac_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MEP-ID-format', REFERENCE_IDENTITY_CLASS, 'IdentifierFormatIdentity' , 'ydk.models.ietf.ietf_conn_oam', 'IdentifierFormatIdentity', 
                [], [], 
                '''                MEP ID format.
                ''',
                'mep_id_format',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MEP-ID-int', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                MEP ID in integer format
                ''',
                'mep_id_int',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.ietf.ietf_conn_oam', 'Domains.Domain.Mas.Ma.Mep.Session', 
                [], [], 
                '''                Monitoring session to/from a particular remote MEP.
                Depending on the protocol, this could represent CC
                messages received from a single remote MEP (if the
                protocol uses multicast CCs) or a target to which
                unicast echo request CCs are sent and from which
                responses are received (if the protocol uses a
                unicast request/response mechanism).
                ''',
                'session',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'MEP',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'Domains.Domain.Mas.Ma.Mip' : {
        'meta_info' : _MetaInfoClass('Domains.Domain.Mas.Ma.Mip',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface
                ''',
                'interface',
                'ietf-conn-oam', True),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Configure a level of maintenance intermediate point (MIP)
                for the interface. The MIP level range is 0 to 7.
                ''',
                'level',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC Address
                ''',
                'mac_address',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'MIP',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'Domains.Domain.Mas.Ma' : {
        'meta_info' : _MetaInfoClass('Domains.Domain.Mas.Ma',
            False, 
            [
            _MetaInfoClassMember('MA-name-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MA name string.
                ''',
                'ma_name_string',
                'ietf-conn-oam', True),
            _MetaInfoClassMember('cc-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate whether the CC enable.
                ''',
                'cc_enable',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('context-null', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                There is no context define
                ''',
                'context_null',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('cos-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class of service
                ''',
                'cos_id',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MA-name-format', REFERENCE_IDENTITY_CLASS, 'NameFormatIdentity' , 'ydk.models.ietf.ietf_conn_oam', 'NameFormatIdentity', 
                [], [], 
                '''                Ma name format
                ''',
                'ma_name_format',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MA-name-null', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Empty
                ''',
                'ma_name_null',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MEP', REFERENCE_LIST, 'Mep' , 'ydk.models.ietf.ietf_conn_oam', 'Domains.Domain.Mas.Ma.Mep', 
                [], [], 
                '''                Contain list of MEPS
                ''',
                'mep',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MIP', REFERENCE_LIST, 'Mip' , 'ydk.models.ietf.ietf_conn_oam', 'Domains.Domain.Mas.Ma.Mip', 
                [], [], 
                '''                List for MIP
                ''',
                'mip',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'MA',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'Domains.Domain.Mas' : {
        'meta_info' : _MetaInfoClass('Domains.Domain.Mas',
            False, 
            [
            _MetaInfoClassMember('MA', REFERENCE_LIST, 'Ma' , 'ydk.models.ietf.ietf_conn_oam', 'Domains.Domain.Mas.Ma', 
                [], [], 
                '''                Maintenance Association list
                ''',
                'ma',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'MAs',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'Domains.Domain' : {
        'meta_info' : _MetaInfoClass('Domains.Domain',
            False, 
            [
            _MetaInfoClassMember('MD-name-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Defines the generic administrative maintenance domain name
                ''',
                'md_name_string',
                'ietf-conn-oam', True),
            _MetaInfoClassMember('technology', REFERENCE_IDENTITY_CLASS, 'TechnologyTypesIdentity' , 'ydk.models.ietf.ietf_conn_oam', 'TechnologyTypesIdentity', 
                [], [], 
                '''                Defines the technology
                ''',
                'technology',
                'ietf-conn-oam', True),
            _MetaInfoClassMember('MAs', REFERENCE_CLASS, 'Mas' , 'ydk.models.ietf.ietf_conn_oam', 'Domains.Domain.Mas', 
                [], [], 
                '''                This container defines MA, within that have multiple MA
                and within MA have MEP
                ''',
                'mas',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('md-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Defines the MD-Level
                ''',
                'md_level',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MD-name-format', REFERENCE_IDENTITY_CLASS, 'NameFormatIdentity' , 'ydk.models.ietf.ietf_conn_oam', 'NameFormatIdentity', 
                [], [], 
                '''                Name format.
                ''',
                'md_name_format',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MD-name-null', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                MD name Null.
                ''',
                'md_name_null',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'domain',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'Domains' : {
        'meta_info' : _MetaInfoClass('Domains',
            False, 
            [
            _MetaInfoClassMember('domain', REFERENCE_LIST, 'Domain' , 'ydk.models.ietf.ietf_conn_oam', 'Domains.Domain', 
                [], [], 
                '''                Define the list of Domains within the IETF-OAM
                ''',
                'domain',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'domains',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'ContinuityCheckRpc.Input.DestinationMep' : {
        'meta_info' : _MetaInfoClass('ContinuityCheckRpc.Input.DestinationMep',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC Address
                ''',
                'mac_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MEP-ID-int', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                MEP ID in integer format
                ''',
                'mep_id_int',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MEP-ID-format', REFERENCE_IDENTITY_CLASS, 'IdentifierFormatIdentity' , 'ydk.models.ietf.ietf_conn_oam', 'IdentifierFormatIdentity', 
                [], [], 
                '''                MEP ID format.
                ''',
                'mep_id_format',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'destination-mep',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'ContinuityCheckRpc.Input' : {
        'meta_info' : _MetaInfoClass('ContinuityCheckRpc.Input',
            False, 
            [
            _MetaInfoClassMember('technology', REFERENCE_IDENTITY_CLASS, 'TechnologyTypesIdentity' , 'ydk.models.ietf.ietf_conn_oam', 'TechnologyTypesIdentity', 
                [], [], 
                '''                The technology
                ''',
                'technology',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MD-name-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Indicate which MD is seeing the defect
                ''',
                'md_name_string',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MA-name-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Indicate which MA is seeing the defect
                ''',
                'ma_name_string',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('cos-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class of service
                ''',
                'cos_id',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ip-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Time to live
                ''',
                'ip_ttl',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('mpls-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Time to live. When an IP packet is imposed with a label,
                the IP TTL value is first decremented then copied into
                the MPLS TTL. As each LSR the MPLS frame's TTL is
                decremented.This behavior can be modified with no
                mpls ip ttl. When a MPLS label is popped, the MPLS
                TTL value is decremented then copied in the IP TTL
                field. If the MPLS TTL value is great than IP TTL,
                that values is not copied over. This is to prevent
                a possible condition of forwarding loop and TTL
                never reaching 0. When two MPLS labels are swapped,
                decrement by 1 and copy over the result into the new label.
                When a new MPLS labels is pushed, decrement by 1 and copy
                over the result into the new label. When a new MPLS labels
                is popped, decrement by 1 and copy over the result into
                the label below.[RFC3443]
                ''',
                'mpls_ttl',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('sub-type', REFERENCE_IDENTITY_CLASS, 'CommandSubTypeIdentity' , 'ydk.models.ietf.ietf_conn_oam', 'CommandSubTypeIdentity', 
                [], [], 
                '''                Defines different command types
                ''',
                'sub_type',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('source-mep', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source MEP
                ''',
                'source_mep',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('destination-mep', REFERENCE_CLASS, 'DestinationMep' , 'ydk.models.ietf.ietf_conn_oam', 'ContinuityCheckRpc.Input.DestinationMep', 
                [], [], 
                '''                Destination MEP
                ''',
                'destination_mep',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of continuity-check message to send
                ''',
                'count',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('cc-transmit-interval', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Interval between echo requests
                ''',
                'cc_transmit_interval',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                Size of continuity-check packets, in octets
                ''',
                'packet_size',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'input',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'ContinuityCheckRpc.Output' : {
        'meta_info' : _MetaInfoClass('ContinuityCheckRpc.Output',
            False, 
            [
            _MetaInfoClassMember('monitor-null', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                There is no monitoring statistics to be defined
                ''',
                'monitor_null',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'output',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'ContinuityCheckRpc' : {
        'meta_info' : _MetaInfoClass('ContinuityCheckRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_conn_oam', 'ContinuityCheckRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_conn_oam', 'ContinuityCheckRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'continuity-check',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'ContinuityVerificationRpc.Input.DestinationMep' : {
        'meta_info' : _MetaInfoClass('ContinuityVerificationRpc.Input.DestinationMep',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC Address
                ''',
                'mac_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MEP-ID-int', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                MEP ID in integer format
                ''',
                'mep_id_int',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MEP-ID-format', REFERENCE_IDENTITY_CLASS, 'IdentifierFormatIdentity' , 'ydk.models.ietf.ietf_conn_oam', 'IdentifierFormatIdentity', 
                [], [], 
                '''                MEP ID format.
                ''',
                'mep_id_format',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'destination-mep',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'ContinuityVerificationRpc.Input' : {
        'meta_info' : _MetaInfoClass('ContinuityVerificationRpc.Input',
            False, 
            [
            _MetaInfoClassMember('MD-name-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Indicate which MD is seeing the defect
                ''',
                'md_name_string',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MA-name-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Indicate which MA is seeing the defect
                ''',
                'ma_name_string',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('cos-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class of service
                ''',
                'cos_id',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ip-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Time to live
                ''',
                'ip_ttl',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('mpls-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Time to live. When an IP packet is imposed with a label,
                the IP TTL value is first decremented then copied into
                the MPLS TTL. As each LSR the MPLS frame's TTL is
                decremented.This behavior can be modified with no
                mpls ip ttl. When a MPLS label is popped, the MPLS
                TTL value is decremented then copied in the IP TTL
                field. If the MPLS TTL value is great than IP TTL,
                that values is not copied over. This is to prevent
                a possible condition of forwarding loop and TTL
                never reaching 0. When two MPLS labels are swapped,
                decrement by 1 and copy over the result into the new label.
                When a new MPLS labels is pushed, decrement by 1 and copy
                over the result into the new label. When a new MPLS labels
                is popped, decrement by 1 and copy over the result into
                the label below.[RFC3443]
                ''',
                'mpls_ttl',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('sub-type', REFERENCE_IDENTITY_CLASS, 'CommandSubTypeIdentity' , 'ydk.models.ietf.ietf_conn_oam', 'CommandSubTypeIdentity', 
                [], [], 
                '''                Defines different command types
                ''',
                'sub_type',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('source-mep', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source MEP
                ''',
                'source_mep',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('destination-mep', REFERENCE_CLASS, 'DestinationMep' , 'ydk.models.ietf.ietf_conn_oam', 'ContinuityVerificationRpc.Input.DestinationMep', 
                [], [], 
                '''                Destination MEP
                ''',
                'destination_mep',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of continuity-verification message to send
                ''',
                'count',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Interval between echo requests
                ''',
                'interval',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [('64', '10000')], [], 
                '''                Size of continuity-verification packets, in octets
                ''',
                'packet_size',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'input',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'ContinuityVerificationRpc.Output' : {
        'meta_info' : _MetaInfoClass('ContinuityVerificationRpc.Output',
            False, 
            [
            _MetaInfoClassMember('monitor-null', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                There is no monitoring statistics to be defined
                ''',
                'monitor_null',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'output',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'ContinuityVerificationRpc' : {
        'meta_info' : _MetaInfoClass('ContinuityVerificationRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_conn_oam', 'ContinuityVerificationRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_conn_oam', 'ContinuityVerificationRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'continuity-verification',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'TracerouteRpc.Input.DestinationMep' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Input.DestinationMep',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC Address
                ''',
                'mac_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MEP-ID-int', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                MEP ID in integer format
                ''',
                'mep_id_int',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MEP-ID-format', REFERENCE_IDENTITY_CLASS, 'IdentifierFormatIdentity' , 'ydk.models.ietf.ietf_conn_oam', 'IdentifierFormatIdentity', 
                [], [], 
                '''                MEP ID format.
                ''',
                'mep_id_format',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'destination-mep',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'TracerouteRpc.Input' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Input',
            False, 
            [
            _MetaInfoClassMember('MD-name-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Indicate which MD is seeing the defect
                ''',
                'md_name_string',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MA-name-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Indicate which MA is seeing the defect
                ''',
                'ma_name_string',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('cos-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Class of service
                ''',
                'cos_id',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ip-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Time to live
                ''',
                'ip_ttl',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('mpls-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Time to live. When an IP packet is imposed with a label,
                the IP TTL value is first decremented then copied into
                the MPLS TTL. As each LSR the MPLS frame's TTL is
                decremented.This behavior can be modified with no
                mpls ip ttl. When a MPLS label is popped, the MPLS
                TTL value is decremented then copied in the IP TTL
                field. If the MPLS TTL value is great than IP TTL,
                that values is not copied over. This is to prevent
                a possible condition of forwarding loop and TTL
                never reaching 0. When two MPLS labels are swapped,
                decrement by 1 and copy over the result into the new label.
                When a new MPLS labels is pushed, decrement by 1 and copy
                over the result into the new label. When a new MPLS labels
                is popped, decrement by 1 and copy over the result into
                the label below.[RFC3443]
                ''',
                'mpls_ttl',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('command-sub-type', REFERENCE_IDENTITY_CLASS, 'CommandSubTypeIdentity' , 'ydk.models.ietf.ietf_conn_oam', 'CommandSubTypeIdentity', 
                [], [], 
                '''                Defines different command types
                ''',
                'command_sub_type',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('source-mep', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source MEP
                ''',
                'source_mep',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('destination-mep', REFERENCE_CLASS, 'DestinationMep' , 'ydk.models.ietf.ietf_conn_oam', 'TracerouteRpc.Input.DestinationMep', 
                [], [], 
                '''                Destination MEP
                ''',
                'destination_mep',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of traceroute probes to send.  In protocols where a
                separate message is sent at each TTL, this is the number
                of packets to send at each TTL.
                ''',
                'count',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Interval between echo requests
                ''',
                'interval',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'input',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'TracerouteRpc.Output.Response.DestinationMep' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Output.Response.DestinationMep',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC Address
                ''',
                'mac_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MEP-ID-int', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                MEP ID in integer format
                ''',
                'mep_id_int',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('MEP-ID-format', REFERENCE_IDENTITY_CLASS, 'IdentifierFormatIdentity' , 'ydk.models.ietf.ietf_conn_oam', 'IdentifierFormatIdentity', 
                [], [], 
                '''                MEP ID format.
                ''',
                'mep_id_format',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'destination-mep',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'TracerouteRpc.Output.Response.Mip' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Output.Response.Mip',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MIP interface
                ''',
                'interface',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC Address
                ''',
                'mac_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'ipv6_address',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'mip',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'TracerouteRpc.Output.Response' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Output.Response',
            False, 
            [
            _MetaInfoClassMember('response-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Arbitrary index for the response.  In protocols that
                guarantee there is only a single response at each TTL
                , the TTL can be used as the response
                index.
                ''',
                'response_index',
                'ietf-conn-oam', True),
            _MetaInfoClassMember('ip-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Time to live
                ''',
                'ip_ttl',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('mpls-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Time to live. When an IP packet is imposed with a label,
                the IP TTL value is first decremented then copied into
                the MPLS TTL. As each LSR the MPLS frame's TTL is
                decremented.This behavior can be modified with no
                mpls ip ttl. When a MPLS label is popped, the MPLS
                TTL value is decremented then copied in the IP TTL
                field. If the MPLS TTL value is great than IP TTL,
                that values is not copied over. This is to prevent
                a possible condition of forwarding loop and TTL
                never reaching 0. When two MPLS labels are swapped,
                decrement by 1 and copy over the result into the new label.
                When a new MPLS labels is pushed, decrement by 1 and copy
                over the result into the new label. When a new MPLS labels
                is popped, decrement by 1 and copy over the result into
                the label below.[RFC3443]
                ''',
                'mpls_ttl',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('destination-mep', REFERENCE_CLASS, 'DestinationMep' , 'ydk.models.ietf.ietf_conn_oam', 'TracerouteRpc.Output.Response.DestinationMep', 
                [], [], 
                '''                MEP from which the response has been received
                ''',
                'destination_mep',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('mip', REFERENCE_CLASS, 'Mip' , 'ydk.models.ietf.ietf_conn_oam', 'TracerouteRpc.Output.Response.Mip', 
                [], [], 
                '''                MIP responding with traceroute
                ''',
                'mip',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('monitor-null', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                There is no monitoring statistics to be defined
                ''',
                'monitor_null',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'response',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'TracerouteRpc.Output' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc.Output',
            False, 
            [
            _MetaInfoClassMember('response', REFERENCE_LIST, 'Response' , 'ydk.models.ietf.ietf_conn_oam', 'TracerouteRpc.Output.Response', 
                [], [], 
                '''                List of response.
                ''',
                'response',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'output',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'TracerouteRpc' : {
        'meta_info' : _MetaInfoClass('TracerouteRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_conn_oam', 'TracerouteRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-conn-oam', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_conn_oam', 'TracerouteRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-conn-oam', False),
            ],
            'ietf-conn-oam',
            'traceroute',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'NameFormatNullIdentity' : {
        'meta_info' : _MetaInfoClass('NameFormatNullIdentity',
            False, 
            [
            ],
            'ietf-conn-oam',
            'name-format-null',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'OnDemandIdentity' : {
        'meta_info' : _MetaInfoClass('OnDemandIdentity',
            False, 
            [
            ],
            'ietf-conn-oam',
            'on-demand',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'InvalidOamDefectIdentity' : {
        'meta_info' : _MetaInfoClass('InvalidOamDefectIdentity',
            False, 
            [
            ],
            'ietf-conn-oam',
            'invalid-oam-defect',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'IdentifierFormatIntegerIdentity' : {
        'meta_info' : _MetaInfoClass('IdentifierFormatIntegerIdentity',
            False, 
            [
            ],
            'ietf-conn-oam',
            'identifier-format-integer',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'LossOfContinuityIdentity' : {
        'meta_info' : _MetaInfoClass('LossOfContinuityIdentity',
            False, 
            [
            ],
            'ietf-conn-oam',
            'loss-of-continuity',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'RemoteMepDefectIdentity' : {
        'meta_info' : _MetaInfoClass('RemoteMepDefectIdentity',
            False, 
            [
            ],
            'ietf-conn-oam',
            'remote-mep-defect',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'RdiIdentity' : {
        'meta_info' : _MetaInfoClass('RdiIdentity',
            False, 
            [
            ],
            'ietf-conn-oam',
            'rdi',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'CrossConnectDefectIdentity' : {
        'meta_info' : _MetaInfoClass('CrossConnectDefectIdentity',
            False, 
            [
            ],
            'ietf-conn-oam',
            'cross-connect-defect',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
    'ProactiveIdentity' : {
        'meta_info' : _MetaInfoClass('ProactiveIdentity',
            False, 
            [
            ],
            'ietf-conn-oam',
            'proactive',
            _yang_ns._namespaces['ietf-conn-oam'],
        'ydk.models.ietf.ietf_conn_oam'
        ),
    },
}
_meta_table['Domains.Domain.Mas.Ma.Mep.Session.DestinationMep']['meta_info'].parent =_meta_table['Domains.Domain.Mas.Ma.Mep.Session']['meta_info']
_meta_table['Domains.Domain.Mas.Ma.Mep.Session.DestinationMepAddress']['meta_info'].parent =_meta_table['Domains.Domain.Mas.Ma.Mep.Session']['meta_info']
_meta_table['Domains.Domain.Mas.Ma.Mep.Session']['meta_info'].parent =_meta_table['Domains.Domain.Mas.Ma.Mep']['meta_info']
_meta_table['Domains.Domain.Mas.Ma.Mep']['meta_info'].parent =_meta_table['Domains.Domain.Mas.Ma']['meta_info']
_meta_table['Domains.Domain.Mas.Ma.Mip']['meta_info'].parent =_meta_table['Domains.Domain.Mas.Ma']['meta_info']
_meta_table['Domains.Domain.Mas.Ma']['meta_info'].parent =_meta_table['Domains.Domain.Mas']['meta_info']
_meta_table['Domains.Domain.Mas']['meta_info'].parent =_meta_table['Domains.Domain']['meta_info']
_meta_table['Domains.Domain']['meta_info'].parent =_meta_table['Domains']['meta_info']
_meta_table['ContinuityCheckRpc.Input.DestinationMep']['meta_info'].parent =_meta_table['ContinuityCheckRpc.Input']['meta_info']
_meta_table['ContinuityCheckRpc.Input']['meta_info'].parent =_meta_table['ContinuityCheckRpc']['meta_info']
_meta_table['ContinuityCheckRpc.Output']['meta_info'].parent =_meta_table['ContinuityCheckRpc']['meta_info']
_meta_table['ContinuityVerificationRpc.Input.DestinationMep']['meta_info'].parent =_meta_table['ContinuityVerificationRpc.Input']['meta_info']
_meta_table['ContinuityVerificationRpc.Input']['meta_info'].parent =_meta_table['ContinuityVerificationRpc']['meta_info']
_meta_table['ContinuityVerificationRpc.Output']['meta_info'].parent =_meta_table['ContinuityVerificationRpc']['meta_info']
_meta_table['TracerouteRpc.Input.DestinationMep']['meta_info'].parent =_meta_table['TracerouteRpc.Input']['meta_info']
_meta_table['TracerouteRpc.Output.Response.DestinationMep']['meta_info'].parent =_meta_table['TracerouteRpc.Output.Response']['meta_info']
_meta_table['TracerouteRpc.Output.Response.Mip']['meta_info'].parent =_meta_table['TracerouteRpc.Output.Response']['meta_info']
_meta_table['TracerouteRpc.Output.Response']['meta_info'].parent =_meta_table['TracerouteRpc.Output']['meta_info']
_meta_table['TracerouteRpc.Input']['meta_info'].parent =_meta_table['TracerouteRpc']['meta_info']
_meta_table['TracerouteRpc.Output']['meta_info'].parent =_meta_table['TracerouteRpc']['meta_info']
