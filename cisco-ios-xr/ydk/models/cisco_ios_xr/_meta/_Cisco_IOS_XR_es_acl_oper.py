


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AclAce1Enum' : _MetaInfoEnum('AclAce1Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper',
        {
            'normal':'normal',
            'remark':'remark',
            'abf':'abf',
        }, 'Cisco-IOS-XR-es-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper']),
    'AclActionEnum' : _MetaInfoEnum('AclActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper',
        {
            'deny':'deny',
            'permit':'permit',
            'encrypt':'encrypt',
            'bypass':'bypass',
            'fallthrough':'fallthrough',
            'invalid':'invalid',
        }, 'Cisco-IOS-XR-es-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper']),
    'AclAce1Enum' : _MetaInfoEnum('AclAce1Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper',
        {
            'normal':'normal',
            'remark':'remark',
            'abf':'abf',
        }, 'Cisco-IOS-XR-es-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper']),
    'EsAcl.Active.Oor.AclSummary.Details' : {
        'meta_info' : _MetaInfoClass('EsAcl.Active.Oor.AclSummary.Details',
            False, 
            [
            _MetaInfoClassMember('current-configured-ac-es', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current configured aces
                ''',
                'current_configured_ac_es',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('current-configured-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current configured acls
                ''',
                'current_configured_ac_ls',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('maximum-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                max configurable aces
                ''',
                'maximum_configurable_ac_es',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('maximum-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                max configurable acls
                ''',
                'maximum_configurable_ac_ls',
                'Cisco-IOS-XR-es-acl-oper', False),
            ],
            'Cisco-IOS-XR-es-acl-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper'
        ),
    },
    'EsAcl.Active.Oor.AclSummary' : {
        'meta_info' : _MetaInfoClass('EsAcl.Active.Oor.AclSummary',
            False, 
            [
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'EsAcl.Active.Oor.AclSummary.Details', 
                [], [], 
                '''                Details containing the resource limits of the
                ACLs
                ''',
                'details',
                'Cisco-IOS-XR-es-acl-oper', False),
            ],
            'Cisco-IOS-XR-es-acl-oper',
            'acl-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper'
        ),
    },
    'EsAcl.Active.Oor' : {
        'meta_info' : _MetaInfoClass('EsAcl.Active.Oor',
            False, 
            [
            _MetaInfoClassMember('acl-summary', REFERENCE_CLASS, 'AclSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'EsAcl.Active.Oor.AclSummary', 
                [], [], 
                '''                Resource Limits pertaining to ACLs only
                ''',
                'acl_summary',
                'Cisco-IOS-XR-es-acl-oper', False),
            ],
            'Cisco-IOS-XR-es-acl-oper',
            'oor',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper'
        ),
    },
    'EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber' : {
        'meta_info' : _MetaInfoClass('EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber',
            False, 
            [
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483646')], [], 
                '''                ACLEntry Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-es-acl-oper', True),
            _MetaInfoClassMember('ace-sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ACE sequence number
                ''',
                'ace_sequence_number',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('ace-type', REFERENCE_ENUM_CLASS, 'AclAce1Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'AclAce1Enum', 
                [], [], 
                '''                ACE type (acl, remark)
                ''',
                'ace_type',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Acl Name
                ''',
                'acl_name',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('capture', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Capture option, TRUE if enabled
                ''',
                'capture',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                COS value
                ''',
                'cos',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DEI bit
                ''',
                'dei',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[a-fA-F0-9]{4}(\\.[a-fA-F0-9]{4}){2}'], 
                '''                Destination MAC address
                ''',
                'destination_address',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('destination-wild-card-bits', ATTRIBUTE, 'str' , None, None, 
                [], [b'[a-fA-F0-9]{4}(\\.[a-fA-F0-9]{4}){2}'], 
                '''                Destination wild card bits
                ''',
                'destination_wild_card_bits',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('ether-type-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Ethernet type Number
                ''',
                'ether_type_number',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('grant', REFERENCE_ENUM_CLASS, 'AclActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'AclActionEnum', 
                [], [], 
                '''                Grant value permit/deny 
                ''',
                'grant',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('hits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ACE hit number
                ''',
                'hits',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('inner-header-cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Inner header COS value
                ''',
                'inner_header_cos',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('inner-header-dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Inner header DEI bit
                ''',
                'inner_header_dei',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('inner-header-vlan1', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Inner header VLAN ID/range lower limit
                ''',
                'inner_header_vlan1',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('inner-header-vlan2', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Inner header VLAN ID range higher limit
                ''',
                'inner_header_vlan2',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('log-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Log option
                ''',
                'log_option',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('remark', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remark string
                ''',
                'remark',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('sequence-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Sring
                ''',
                'sequence_string',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[a-fA-F0-9]{4}(\\.[a-fA-F0-9]{4}){2}'], 
                '''                Source MAC address
                ''',
                'source_address',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('source-wild-card-bits', ATTRIBUTE, 'str' , None, None, 
                [], [b'[a-fA-F0-9]{4}(\\.[a-fA-F0-9]{4}){2}'], 
                '''                Source wild card bits
                ''',
                'source_wild_card_bits',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('vlan1', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN ID/range lower limit
                ''',
                'vlan1',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('vlan2', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN ID range higher limit
                ''',
                'vlan2',
                'Cisco-IOS-XR-es-acl-oper', False),
            ],
            'Cisco-IOS-XR-es-acl-oper',
            'acl-sequence-number',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper'
        ),
    },
    'EsAcl.Active.List.Acls.Acl.AclSequenceNumbers' : {
        'meta_info' : _MetaInfoClass('EsAcl.Active.List.Acls.Acl.AclSequenceNumbers',
            False, 
            [
            _MetaInfoClassMember('acl-sequence-number', REFERENCE_LIST, 'AclSequenceNumber' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber', 
                [], [], 
                '''                Sequence Number of an ACL entry
                ''',
                'acl_sequence_number',
                'Cisco-IOS-XR-es-acl-oper', False),
            ],
            'Cisco-IOS-XR-es-acl-oper',
            'acl-sequence-numbers',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper'
        ),
    },
    'EsAcl.Active.List.Acls.Acl' : {
        'meta_info' : _MetaInfoClass('EsAcl.Active.List.Acls.Acl',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 65)], [], 
                '''                Name of the Access List
                ''',
                'name',
                'Cisco-IOS-XR-es-acl-oper', True),
            _MetaInfoClassMember('acl-sequence-numbers', REFERENCE_CLASS, 'AclSequenceNumbers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'EsAcl.Active.List.Acls.Acl.AclSequenceNumbers', 
                [], [], 
                '''                Table of all the SequenceNumbers per ACL
                ''',
                'acl_sequence_numbers',
                'Cisco-IOS-XR-es-acl-oper', False),
            ],
            'Cisco-IOS-XR-es-acl-oper',
            'acl',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper'
        ),
    },
    'EsAcl.Active.List.Acls' : {
        'meta_info' : _MetaInfoClass('EsAcl.Active.List.Acls',
            False, 
            [
            _MetaInfoClassMember('acl', REFERENCE_LIST, 'Acl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'EsAcl.Active.List.Acls.Acl', 
                [], [], 
                '''                Name of the Access List
                ''',
                'acl',
                'Cisco-IOS-XR-es-acl-oper', False),
            ],
            'Cisco-IOS-XR-es-acl-oper',
            'acls',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper'
        ),
    },
    'EsAcl.Active.List' : {
        'meta_info' : _MetaInfoClass('EsAcl.Active.List',
            False, 
            [
            _MetaInfoClassMember('acls', REFERENCE_CLASS, 'Acls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'EsAcl.Active.List.Acls', 
                [], [], 
                '''                ACL class displaying Usage and Entries
                ''',
                'acls',
                'Cisco-IOS-XR-es-acl-oper', False),
            ],
            'Cisco-IOS-XR-es-acl-oper',
            'list',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper'
        ),
    },
    'EsAcl.Active.OorAcls.OorAcl' : {
        'meta_info' : _MetaInfoClass('EsAcl.Active.OorAcls.OorAcl',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 65)], [], 
                '''                Name of the Access List
                ''',
                'name',
                'Cisco-IOS-XR-es-acl-oper', True),
            _MetaInfoClassMember('current-configured-ac-es', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current configured aces
                ''',
                'current_configured_ac_es',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('current-configured-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current configured acls
                ''',
                'current_configured_ac_ls',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('maximum-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                max configurable aces
                ''',
                'maximum_configurable_ac_es',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('maximum-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                max configurable acls
                ''',
                'maximum_configurable_ac_ls',
                'Cisco-IOS-XR-es-acl-oper', False),
            ],
            'Cisco-IOS-XR-es-acl-oper',
            'oor-acl',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper'
        ),
    },
    'EsAcl.Active.OorAcls' : {
        'meta_info' : _MetaInfoClass('EsAcl.Active.OorAcls',
            False, 
            [
            _MetaInfoClassMember('oor-acl', REFERENCE_LIST, 'OorAcl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'EsAcl.Active.OorAcls.OorAcl', 
                [], [], 
                '''                Resource occupation details for a particular
                ACL
                ''',
                'oor_acl',
                'Cisco-IOS-XR-es-acl-oper', False),
            ],
            'Cisco-IOS-XR-es-acl-oper',
            'oor-acls',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper'
        ),
    },
    'EsAcl.Active.Usages.Usage' : {
        'meta_info' : _MetaInfoClass('EsAcl.Active.Usages.Usage',
            False, 
            [
            _MetaInfoClassMember('application-id', REFERENCE_ENUM_CLASS, 'AclUsageAppIdEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_common_acl_datatypes', 'AclUsageAppIdEnumEnum', 
                [], [], 
                '''                Application ID
                ''',
                'application_id',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node where ACL is applied
                ''',
                'location',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 65)], [], 
                '''                Name of the ACL
                ''',
                'name',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('usage-details', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Usage Statistics Details
                ''',
                'usage_details',
                'Cisco-IOS-XR-es-acl-oper', False),
            ],
            'Cisco-IOS-XR-es-acl-oper',
            'usage',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper'
        ),
    },
    'EsAcl.Active.Usages' : {
        'meta_info' : _MetaInfoClass('EsAcl.Active.Usages',
            False, 
            [
            _MetaInfoClassMember('usage', REFERENCE_LIST, 'Usage' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'EsAcl.Active.Usages.Usage', 
                [], [], 
                '''                Usage statistics of an ACL at a node
                ''',
                'usage',
                'Cisco-IOS-XR-es-acl-oper', False),
            ],
            'Cisco-IOS-XR-es-acl-oper',
            'usages',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper'
        ),
    },
    'EsAcl.Active' : {
        'meta_info' : _MetaInfoClass('EsAcl.Active',
            False, 
            [
            _MetaInfoClassMember('list', REFERENCE_CLASS, 'List' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'EsAcl.Active.List', 
                [], [], 
                '''                List containing ACLs
                ''',
                'list',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('oor', REFERENCE_CLASS, 'Oor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'EsAcl.Active.Oor', 
                [], [], 
                '''                Out Of Resources, Limits to the resources
                allocatable
                ''',
                'oor',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('oor-acls', REFERENCE_CLASS, 'OorAcls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'EsAcl.Active.OorAcls', 
                [], [], 
                '''                Resource occupation details for ACLs
                ''',
                'oor_acls',
                'Cisco-IOS-XR-es-acl-oper', False),
            _MetaInfoClassMember('usages', REFERENCE_CLASS, 'Usages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'EsAcl.Active.Usages', 
                [], [], 
                '''                Table of Usage statistics of ACLs at different
                nodes
                ''',
                'usages',
                'Cisco-IOS-XR-es-acl-oper', False),
            ],
            'Cisco-IOS-XR-es-acl-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper'
        ),
    },
    'EsAcl' : {
        'meta_info' : _MetaInfoClass('EsAcl',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper', 'EsAcl.Active', 
                [], [], 
                '''                Out Of Resources, Limits to the resources
                allocatable
                ''',
                'active',
                'Cisco-IOS-XR-es-acl-oper', False),
            ],
            'Cisco-IOS-XR-es-acl-oper',
            'es-acl',
            _yang_ns._namespaces['Cisco-IOS-XR-es-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_oper'
        ),
    },
}
_meta_table['EsAcl.Active.Oor.AclSummary.Details']['meta_info'].parent =_meta_table['EsAcl.Active.Oor.AclSummary']['meta_info']
_meta_table['EsAcl.Active.Oor.AclSummary']['meta_info'].parent =_meta_table['EsAcl.Active.Oor']['meta_info']
_meta_table['EsAcl.Active.List.Acls.Acl.AclSequenceNumbers.AclSequenceNumber']['meta_info'].parent =_meta_table['EsAcl.Active.List.Acls.Acl.AclSequenceNumbers']['meta_info']
_meta_table['EsAcl.Active.List.Acls.Acl.AclSequenceNumbers']['meta_info'].parent =_meta_table['EsAcl.Active.List.Acls.Acl']['meta_info']
_meta_table['EsAcl.Active.List.Acls.Acl']['meta_info'].parent =_meta_table['EsAcl.Active.List.Acls']['meta_info']
_meta_table['EsAcl.Active.List.Acls']['meta_info'].parent =_meta_table['EsAcl.Active.List']['meta_info']
_meta_table['EsAcl.Active.OorAcls.OorAcl']['meta_info'].parent =_meta_table['EsAcl.Active.OorAcls']['meta_info']
_meta_table['EsAcl.Active.Usages.Usage']['meta_info'].parent =_meta_table['EsAcl.Active.Usages']['meta_info']
_meta_table['EsAcl.Active.Oor']['meta_info'].parent =_meta_table['EsAcl.Active']['meta_info']
_meta_table['EsAcl.Active.List']['meta_info'].parent =_meta_table['EsAcl.Active']['meta_info']
_meta_table['EsAcl.Active.OorAcls']['meta_info'].parent =_meta_table['EsAcl.Active']['meta_info']
_meta_table['EsAcl.Active.Usages']['meta_info'].parent =_meta_table['EsAcl.Active']['meta_info']
_meta_table['EsAcl.Active']['meta_info'].parent =_meta_table['EsAcl']['meta_info']
