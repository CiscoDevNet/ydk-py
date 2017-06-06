


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IepHopEnum' : _MetaInfoEnum('IepHopEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper',
        {
            'strict':'strict',
            'loose':'loose',
        }, 'Cisco-IOS-XR-ip-iep-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-oper']),
    'IepAddressEnum' : _MetaInfoEnum('IepAddressEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper',
        {
            'next':'next',
            'exclude':'exclude',
            'exclude-srlg':'exclude_srlg',
        }, 'Cisco-IOS-XR-ip-iep-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-oper']),
    'IepStatusEnum' : _MetaInfoEnum('IepStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'Cisco-IOS-XR-ip-iep-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-oper']),
    'ExplicitPaths.Identifiers.Identifier.Address' : {
        'meta_info' : _MetaInfoClass('ExplicitPaths.Identifiers.Identifier.Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 unicast address
                ''',
                'address',
                'Cisco-IOS-XR-ip-iep-oper', False),
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'IepAddressEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepAddressEnum', 
                [], [], 
                '''                Specifies the address type
                ''',
                'address_type',
                'Cisco-IOS-XR-ip-iep-oper', False),
            _MetaInfoClassMember('hop-type', REFERENCE_ENUM_CLASS, 'IepHopEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepHopEnum', 
                [], [], 
                '''                Specifies the next unicast address in the path
                as a strict or loose hop
                ''',
                'hop_type',
                'Cisco-IOS-XR-ip-iep-oper', False),
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Index of the path
                ''',
                'if_index',
                'Cisco-IOS-XR-ip-iep-oper', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index number at which the path entry is inserted
                or modified
                ''',
                'index',
                'Cisco-IOS-XR-ip-iep-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-ip-iep-oper', False),
            ],
            'Cisco-IOS-XR-ip-iep-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper'
        ),
    },
    'ExplicitPaths.Identifiers.Identifier' : {
        'meta_info' : _MetaInfoClass('ExplicitPaths.Identifiers.Identifier',
            False, 
            [
            _MetaInfoClassMember('identifier-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Identifier ID
                ''',
                'identifier_id',
                'Cisco-IOS-XR-ip-iep-oper', True),
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'ExplicitPaths.Identifiers.Identifier.Address', 
                [], [], 
                '''                List of IP addresses configured in the explicit
                path
                ''',
                'address',
                'Cisco-IOS-XR-ip-iep-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'IepStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepStatusEnum', 
                [], [], 
                '''                Status of the path
                ''',
                'status',
                'Cisco-IOS-XR-ip-iep-oper', False),
            ],
            'Cisco-IOS-XR-ip-iep-oper',
            'identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper'
        ),
    },
    'ExplicitPaths.Identifiers' : {
        'meta_info' : _MetaInfoClass('ExplicitPaths.Identifiers',
            False, 
            [
            _MetaInfoClassMember('identifier', REFERENCE_LIST, 'Identifier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'ExplicitPaths.Identifiers.Identifier', 
                [], [], 
                '''                IP explicit path configured for a particular
                identifier
                ''',
                'identifier',
                'Cisco-IOS-XR-ip-iep-oper', False),
            ],
            'Cisco-IOS-XR-ip-iep-oper',
            'identifiers',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper'
        ),
    },
    'ExplicitPaths.Names.Name.Address' : {
        'meta_info' : _MetaInfoClass('ExplicitPaths.Names.Name.Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 unicast address
                ''',
                'address',
                'Cisco-IOS-XR-ip-iep-oper', False),
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'IepAddressEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepAddressEnum', 
                [], [], 
                '''                Specifies the address type
                ''',
                'address_type',
                'Cisco-IOS-XR-ip-iep-oper', False),
            _MetaInfoClassMember('hop-type', REFERENCE_ENUM_CLASS, 'IepHopEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepHopEnum', 
                [], [], 
                '''                Specifies the next unicast address in the path
                as a strict or loose hop
                ''',
                'hop_type',
                'Cisco-IOS-XR-ip-iep-oper', False),
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Index of the path
                ''',
                'if_index',
                'Cisco-IOS-XR-ip-iep-oper', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index number at which the path entry is inserted
                or modified
                ''',
                'index',
                'Cisco-IOS-XR-ip-iep-oper', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-ip-iep-oper', False),
            ],
            'Cisco-IOS-XR-ip-iep-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper'
        ),
    },
    'ExplicitPaths.Names.Name' : {
        'meta_info' : _MetaInfoClass('ExplicitPaths.Names.Name',
            False, 
            [
            _MetaInfoClassMember('path-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Path name
                ''',
                'path_name',
                'Cisco-IOS-XR-ip-iep-oper', True),
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'ExplicitPaths.Names.Name.Address', 
                [], [], 
                '''                List of IP addresses configured in the explicit
                path
                ''',
                'address',
                'Cisco-IOS-XR-ip-iep-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'IepStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'IepStatusEnum', 
                [], [], 
                '''                Status of the path
                ''',
                'status',
                'Cisco-IOS-XR-ip-iep-oper', False),
            ],
            'Cisco-IOS-XR-ip-iep-oper',
            'name',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper'
        ),
    },
    'ExplicitPaths.Names' : {
        'meta_info' : _MetaInfoClass('ExplicitPaths.Names',
            False, 
            [
            _MetaInfoClassMember('name', REFERENCE_LIST, 'Name' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'ExplicitPaths.Names.Name', 
                [], [], 
                '''                IP explicit path configured for a particular
                path name
                ''',
                'name',
                'Cisco-IOS-XR-ip-iep-oper', False),
            ],
            'Cisco-IOS-XR-ip-iep-oper',
            'names',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper'
        ),
    },
    'ExplicitPaths' : {
        'meta_info' : _MetaInfoClass('ExplicitPaths',
            False, 
            [
            _MetaInfoClassMember('identifiers', REFERENCE_CLASS, 'Identifiers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'ExplicitPaths.Identifiers', 
                [], [], 
                '''                List of configured IP explicit path identifiers,
                this corresponds to mplsTunnelHopTable in TE MIB
                ''',
                'identifiers',
                'Cisco-IOS-XR-ip-iep-oper', False),
            _MetaInfoClassMember('names', REFERENCE_CLASS, 'Names' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper', 'ExplicitPaths.Names', 
                [], [], 
                '''                List of configured IP explicit path names, this
                corresponds to mplsTunnelHopTable in TE MIB
                ''',
                'names',
                'Cisco-IOS-XR-ip-iep-oper', False),
            ],
            'Cisco-IOS-XR-ip-iep-oper',
            'explicit-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper'
        ),
    },
}
_meta_table['ExplicitPaths.Identifiers.Identifier.Address']['meta_info'].parent =_meta_table['ExplicitPaths.Identifiers.Identifier']['meta_info']
_meta_table['ExplicitPaths.Identifiers.Identifier']['meta_info'].parent =_meta_table['ExplicitPaths.Identifiers']['meta_info']
_meta_table['ExplicitPaths.Names.Name.Address']['meta_info'].parent =_meta_table['ExplicitPaths.Names.Name']['meta_info']
_meta_table['ExplicitPaths.Names.Name']['meta_info'].parent =_meta_table['ExplicitPaths.Names']['meta_info']
_meta_table['ExplicitPaths.Identifiers']['meta_info'].parent =_meta_table['ExplicitPaths']['meta_info']
_meta_table['ExplicitPaths.Names']['meta_info'].parent =_meta_table['ExplicitPaths']['meta_info']
