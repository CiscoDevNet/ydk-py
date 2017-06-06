


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EsAclGrantEnumEnum' : _MetaInfoEnum('EsAclGrantEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg',
        {
            'deny':'deny',
            'permit':'permit',
        }, 'Cisco-IOS-XR-es-acl-cfg', _yang_ns._namespaces['Cisco-IOS-XR-es-acl-cfg']),
    'EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork' : {
        'meta_info' : _MetaInfoClass('EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork',
            False, 
            [
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{1,4}(\\.[0-9a-fA-F]{1,4}){2})'], 
                '''                Source address to match, leave unspecified
                for any.
                ''',
                'source_address',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('source-wild-card-bits', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{1,4}(\\.[0-9a-fA-F]{1,4}){2})'], 
                '''                Wildcard bits to apply to source address
                (if specified), leave unspecified for no
                wildcarding.
                ''',
                'source_wild_card_bits',
                'Cisco-IOS-XR-es-acl-cfg', False),
            ],
            'Cisco-IOS-XR-es-acl-cfg',
            'source-network',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg'
        ),
    },
    'EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork' : {
        'meta_info' : _MetaInfoClass('EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{1,4}(\\.[0-9a-fA-F]{1,4}){2})'], 
                '''                Destination address to match (if a protocol
                was specified), leave unspecified for any.
                ''',
                'destination_address',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('destination-wild-card-bits', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{1,4}(\\.[0-9a-fA-F]{1,4}){2})'], 
                '''                Wildcard bits to apply to destination address
                (if specified), leave unspecified for no
                wildcarding.
                ''',
                'destination_wild_card_bits',
                'Cisco-IOS-XR-es-acl-cfg', False),
            ],
            'Cisco-IOS-XR-es-acl-cfg',
            'destination-network',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg'
        ),
    },
    'EsAcl.Accesses.Access.AccessListEntries.AccessListEntry' : {
        'meta_info' : _MetaInfoClass('EsAcl.Accesses.Access.AccessListEntries.AccessListEntry',
            False, 
            [
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483646')], [], 
                '''                Sequence number of access list entry
                ''',
                'sequence_number',
                'Cisco-IOS-XR-es-acl-cfg', True),
            _MetaInfoClassMember('capture', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable capture.
                ''',
                'capture',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                COS value
                ''',
                'cos',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DEI bit
                ''',
                'dei',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('destination-network', REFERENCE_CLASS, 'DestinationNetwork' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork', 
                [], [], 
                '''                Destination network settings.
                ''',
                'destination_network',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('ether-type-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Ethernet type Number
                ''',
                'ether_type_number',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('grant', REFERENCE_ENUM_CLASS, 'EsAclGrantEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAclGrantEnumEnum', 
                [], [], 
                '''                Whether to forward or drop packets matching the
                ACE.
                ''',
                'grant',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('inner-cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Inner COS value
                ''',
                'inner_cos',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('inner-dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Inner DEI bit
                ''',
                'inner_dei',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('inner-vlan1', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Inner VLAN ID/range lower limit
                ''',
                'inner_vlan1',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('inner-vlan2', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Inner VLAN ID range higher limit
                ''',
                'inner_vlan2',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('log-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Whether and how to log matches against this
                entry.
                ''',
                'log_option',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('remark', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Comments or a description for the access list.
                ''',
                'remark',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('sequence-str', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Sequence String for the ace.
                ''',
                'sequence_str',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('source-network', REFERENCE_CLASS, 'SourceNetwork' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork', 
                [], [], 
                '''                Source network settings.
                ''',
                'source_network',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('vlan1', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN ID/range lower limit
                ''',
                'vlan1',
                'Cisco-IOS-XR-es-acl-cfg', False),
            _MetaInfoClassMember('vlan2', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN ID range higher limit
                ''',
                'vlan2',
                'Cisco-IOS-XR-es-acl-cfg', False),
            ],
            'Cisco-IOS-XR-es-acl-cfg',
            'access-list-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg'
        ),
    },
    'EsAcl.Accesses.Access.AccessListEntries' : {
        'meta_info' : _MetaInfoClass('EsAcl.Accesses.Access.AccessListEntries',
            False, 
            [
            _MetaInfoClassMember('access-list-entry', REFERENCE_LIST, 'AccessListEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAcl.Accesses.Access.AccessListEntries.AccessListEntry', 
                [], [], 
                '''                An ACL entry; either a description (remark)
                or anAccess List Entry to match against
                ''',
                'access_list_entry',
                'Cisco-IOS-XR-es-acl-cfg', False),
            ],
            'Cisco-IOS-XR-es-acl-cfg',
            'access-list-entries',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg'
        ),
    },
    'EsAcl.Accesses.Access' : {
        'meta_info' : _MetaInfoClass('EsAcl.Accesses.Access',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 65)], [], 
                '''                Name of the access list
                ''',
                'name',
                'Cisco-IOS-XR-es-acl-cfg', True),
            _MetaInfoClassMember('access-list-entries', REFERENCE_CLASS, 'AccessListEntries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAcl.Accesses.Access.AccessListEntries', 
                [], [], 
                '''                ACL entry table; contains list of access list
                entries
                ''',
                'access_list_entries',
                'Cisco-IOS-XR-es-acl-cfg', False),
            ],
            'Cisco-IOS-XR-es-acl-cfg',
            'access',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg'
        ),
    },
    'EsAcl.Accesses' : {
        'meta_info' : _MetaInfoClass('EsAcl.Accesses',
            False, 
            [
            _MetaInfoClassMember('access', REFERENCE_LIST, 'Access' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAcl.Accesses.Access', 
                [], [], 
                '''                An ACL
                ''',
                'access',
                'Cisco-IOS-XR-es-acl-cfg', False),
            ],
            'Cisco-IOS-XR-es-acl-cfg',
            'accesses',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg'
        ),
    },
    'EsAcl' : {
        'meta_info' : _MetaInfoClass('EsAcl',
            False, 
            [
            _MetaInfoClassMember('accesses', REFERENCE_CLASS, 'Accesses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAcl.Accesses', 
                [], [], 
                '''                Table of access lists
                ''',
                'accesses',
                'Cisco-IOS-XR-es-acl-cfg', False),
            ],
            'Cisco-IOS-XR-es-acl-cfg',
            'es-acl',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg'
        ),
    },
}
_meta_table['EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork']['meta_info'].parent =_meta_table['EsAcl.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork']['meta_info'].parent =_meta_table['EsAcl.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['EsAcl.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info'].parent =_meta_table['EsAcl.Accesses.Access.AccessListEntries']['meta_info']
_meta_table['EsAcl.Accesses.Access.AccessListEntries']['meta_info'].parent =_meta_table['EsAcl.Accesses.Access']['meta_info']
_meta_table['EsAcl.Accesses.Access']['meta_info'].parent =_meta_table['EsAcl.Accesses']['meta_info']
_meta_table['EsAcl.Accesses']['meta_info'].parent =_meta_table['EsAcl']['meta_info']
