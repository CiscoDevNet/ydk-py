


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'Domain.MplDomain.Domains' : {
        'meta_info' : _MetaInfoClass('Domain.MplDomain.Domains',
            False, 
            [
            _MetaInfoClassMember('domainID', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Entry uniquely identifies the domain in the
                forwarder.
                ''',
                'domainid',
                'ietf-yang-mpl-domain', True),
            _MetaInfoClassMember('MClist', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                List of associated IPv6 Addresses.
                ''',
                'mclist',
                'ietf-yang-mpl-domain', False),
            ],
            'ietf-yang-mpl-domain',
            'domains',
            _yang_ns._namespaces['ietf-yang-mpl-domain'],
        'ydk.models.ietf.ietf_yang_mpl_domain'
        ),
    },
    'Domain.MplDomain.Addresses' : {
        'meta_info' : _MetaInfoClass('Domain.MplDomain.Addresses',
            False, 
            [
            _MetaInfoClassMember('MCaddress', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                MC address belonging to a MPL domain.
                ''',
                'mcaddress',
                'ietf-yang-mpl-domain', True),
            _MetaInfoClassMember('interfaces', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                List of names of interfaces enabled for this
                Multicast address. Interface name is defined in [RFC6206].
                ''',
                'interfaces',
                'ietf-yang-mpl-domain', False),
            ],
            'ietf-yang-mpl-domain',
            'addresses',
            _yang_ns._namespaces['ietf-yang-mpl-domain'],
        'ydk.models.ietf.ietf_yang_mpl_domain'
        ),
    },
    'Domain.MplDomain' : {
        'meta_info' : _MetaInfoClass('Domain.MplDomain',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_LIST, 'Addresses' , 'ydk.models.ietf.ietf_yang_mpl_domain', 'Domain.MplDomain.Addresses', 
                [], [], 
                '''                The entries describe the interfaces enabled
                with the specified MC address.
                ''',
                'addresses',
                'ietf-yang-mpl-domain', False),
            _MetaInfoClassMember('domains', REFERENCE_LIST, 'Domains' , 'ydk.models.ietf.ietf_yang_mpl_domain', 'Domain.MplDomain.Domains', 
                [], [], 
                '''                The entries describe a given domain identified with
                domainID and the associated Multicast addresses.
                ''',
                'domains',
                'ietf-yang-mpl-domain', False),
            ],
            'ietf-yang-mpl-domain',
            'mpl-domain',
            _yang_ns._namespaces['ietf-yang-mpl-domain'],
        'ydk.models.ietf.ietf_yang_mpl_domain'
        ),
    },
    'Domain.MplSingle' : {
        'meta_info' : _MetaInfoClass('Domain.MplSingle',
            False, 
            [
            _MetaInfoClassMember('MCaddresses', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                list of MC addresses belonging to one single
                domain and interface.
                ''',
                'mcaddresses',
                'ietf-yang-mpl-domain', False),
            ],
            'ietf-yang-mpl-domain',
            'mpl-single',
            _yang_ns._namespaces['ietf-yang-mpl-domain'],
        'ydk.models.ietf.ietf_yang_mpl_domain'
        ),
    },
    'Domain' : {
        'meta_info' : _MetaInfoClass('Domain',
            False, 
            [
            _MetaInfoClassMember('mpl-domain', REFERENCE_CLASS, 'MplDomain' , 'ydk.models.ietf.ietf_yang_mpl_domain', 'Domain.MplDomain', 
                [], [], 
                '''                The entries describe the MPL domains, the associated
                Multicast addresses and interfaces.
                ''',
                'mpl_domain',
                'ietf-yang-mpl-domain', False),
            _MetaInfoClassMember('mpl-single', REFERENCE_CLASS, 'MplSingle' , 'ydk.models.ietf.ietf_yang_mpl_domain', 'Domain.MplSingle', 
                [], [], 
                '''                For small devices list of MC addresses for single
                interface and domain.
                ''',
                'mpl_single',
                'ietf-yang-mpl-domain', False),
            ],
            'ietf-yang-mpl-domain',
            'domain',
            _yang_ns._namespaces['ietf-yang-mpl-domain'],
        'ydk.models.ietf.ietf_yang_mpl_domain'
        ),
    },
}
_meta_table['Domain.MplDomain.Domains']['meta_info'].parent =_meta_table['Domain.MplDomain']['meta_info']
_meta_table['Domain.MplDomain.Addresses']['meta_info'].parent =_meta_table['Domain.MplDomain']['meta_info']
_meta_table['Domain.MplDomain']['meta_info'].parent =_meta_table['Domain']['meta_info']
_meta_table['Domain.MplSingle']['meta_info'].parent =_meta_table['Domain']['meta_info']
