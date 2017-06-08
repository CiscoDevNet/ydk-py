


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'PotProfiles.PotProfileSet.PotProfileList' : {
        'meta_info' : _MetaInfoClass('PotProfiles.PotProfileSet.PotProfileList',
            False, 
            [
            _MetaInfoClassMember('pot-profile-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Proof of transit profile index.
                ''',
                'pot_profile_index',
                'ietf-pot-profile', True),
            _MetaInfoClassMember('bitmask', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bits as mask used in controlling the size of the
                random value generation. 32-bits of mask is default.
                ''',
                'bitmask',
                'ietf-pot-profile', False),
            _MetaInfoClassMember('lpc', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Lagrange Polynomial Coefficient
                ''',
                'lpc',
                'ietf-pot-profile', False),
            _MetaInfoClassMember('prime-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Prime number used for module math computation
                ''',
                'prime_number',
                'ietf-pot-profile', False),
            _MetaInfoClassMember('public-polynomial', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pre evaluated Public polynomial
                ''',
                'public_polynomial',
                'ietf-pot-profile', False),
            _MetaInfoClassMember('secret-share', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Share of the secret of polynomial 1 used in computation
                ''',
                'secret_share',
                'ietf-pot-profile', False),
            _MetaInfoClassMember('validator', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if the node is a verifier node
                ''',
                'validator',
                'ietf-pot-profile', False),
            _MetaInfoClassMember('validator-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Secret key for validating the path, constant of poly 1
                ''',
                'validator_key',
                'ietf-pot-profile', False),
            ],
            'ietf-pot-profile',
            'pot-profile-list',
            _yang_ns._namespaces['ietf-pot-profile'],
        'ydk.models.ietf.ietf_pot_profile'
        ),
    },
    'PotProfiles.PotProfileSet' : {
        'meta_info' : _MetaInfoClass('PotProfiles.PotProfileSet',
            False, 
            [
            _MetaInfoClassMember('pot-profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Unique identifier for each proof of transit profile
                ''',
                'pot_profile_name',
                'ietf-pot-profile', True),
            _MetaInfoClassMember('active-profile-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Proof of transit profile index that is currently active.
                Will be set in the first hop of the path or chain.
                Other nodes will not use this field.
                ''',
                'active_profile_index',
                'ietf-pot-profile', False),
            _MetaInfoClassMember('pot-profile-list', REFERENCE_LIST, 'PotProfileList' , 'ydk.models.ietf.ietf_pot_profile', 'PotProfiles.PotProfileSet.PotProfileList', 
                [], [], 
                '''                A set of pot profiles.
                ''',
                'pot_profile_list',
                'ietf-pot-profile', False),
            ],
            'ietf-pot-profile',
            'pot-profile-set',
            _yang_ns._namespaces['ietf-pot-profile'],
        'ydk.models.ietf.ietf_pot_profile'
        ),
    },
    'PotProfiles' : {
        'meta_info' : _MetaInfoClass('PotProfiles',
            False, 
            [
            _MetaInfoClassMember('pot-profile-set', REFERENCE_LIST, 'PotProfileSet' , 'ydk.models.ietf.ietf_pot_profile', 'PotProfiles.PotProfileSet', 
                [], [], 
                '''                Set of proof of transit profiles that group parameters
                required to classify and compute proof of transit
                metadata at a node
                ''',
                'pot_profile_set',
                'ietf-pot-profile', False),
            ],
            'ietf-pot-profile',
            'pot-profiles',
            _yang_ns._namespaces['ietf-pot-profile'],
        'ydk.models.ietf.ietf_pot_profile'
        ),
    },
}
_meta_table['PotProfiles.PotProfileSet.PotProfileList']['meta_info'].parent =_meta_table['PotProfiles.PotProfileSet']['meta_info']
_meta_table['PotProfiles.PotProfileSet']['meta_info'].parent =_meta_table['PotProfiles']['meta_info']
