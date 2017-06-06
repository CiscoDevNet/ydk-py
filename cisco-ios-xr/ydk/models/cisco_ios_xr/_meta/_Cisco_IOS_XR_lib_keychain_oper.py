


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CrytoAlgoEnum' : _MetaInfoEnum('CrytoAlgoEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper',
        {
            'not-configured':'not_configured',
            'hmac-sha1-12':'hmac_sha1_12',
            'md5':'md5',
            'sha1':'sha1',
            'hmac-md5':'hmac_md5',
            'hmac-sha1-20':'hmac_sha1_20',
        }, 'Cisco-IOS-XR-lib-keychain-oper', _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-oper']),
    'Keychain.Keies.Key.Key_.KeyId.SendLifetime' : {
        'meta_info' : _MetaInfoClass('Keychain.Keies.Key.Key_.KeyId.SendLifetime',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Duration of the key in seconds. value 0xffffffff
                reflects infinite, never expires, is configured 
                ''',
                'duration',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            _MetaInfoClassMember('end', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Key life end time in format : day-of-week month
                date-of-month HH:MM:SS year eg: Thu Feb 1 18:32
                :14 2011
                ''',
                'end',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            _MetaInfoClassMember('is-always-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is TRUE if duration is 0xffffffff 
                ''',
                'is_always_valid',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            _MetaInfoClassMember('is-valid-now', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is TRUE if current time is betweenstart and end
                lifetime , else FALSE
                ''',
                'is_valid_now',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Key life start time in format : day-of-week
                month date-of-month HH:MM:SS year eg: Thu Feb 1
                18:32:14 2011
                ''',
                'start',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'send-lifetime',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper'
        ),
    },
    'Keychain.Keies.Key.Key_.KeyId.AcceptLifetime' : {
        'meta_info' : _MetaInfoClass('Keychain.Keies.Key.Key_.KeyId.AcceptLifetime',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Duration of the key in seconds. value 0xffffffff
                reflects infinite, never expires, is configured 
                ''',
                'duration',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            _MetaInfoClassMember('end', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Key life end time in format : day-of-week month
                date-of-month HH:MM:SS year eg: Thu Feb 1 18:32
                :14 2011
                ''',
                'end',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            _MetaInfoClassMember('is-always-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is TRUE if duration is 0xffffffff 
                ''',
                'is_always_valid',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            _MetaInfoClassMember('is-valid-now', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is TRUE if current time is betweenstart and end
                lifetime , else FALSE
                ''',
                'is_valid_now',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Key life start time in format : day-of-week
                month date-of-month HH:MM:SS year eg: Thu Feb 1
                18:32:14 2011
                ''',
                'start',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'accept-lifetime',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper'
        ),
    },
    'Keychain.Keies.Key.Key_.KeyId' : {
        'meta_info' : _MetaInfoClass('Keychain.Keies.Key.Key_.KeyId',
            False, 
            [
            _MetaInfoClassMember('accept-lifetime', REFERENCE_CLASS, 'AcceptLifetime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Keychain.Keies.Key.Key_.KeyId.AcceptLifetime', 
                [], [], 
                '''                Accept Lifetime of the key
                ''',
                'accept_lifetime',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            _MetaInfoClassMember('cryptographic-algorithm', REFERENCE_ENUM_CLASS, 'CrytoAlgoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'CrytoAlgoEnum', 
                [], [], 
                '''                Cryptographic algorithm
                ''',
                'cryptographic_algorithm',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            _MetaInfoClassMember('key-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Key string
                ''',
                'key_string',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            _MetaInfoClassMember('send-lifetime', REFERENCE_CLASS, 'SendLifetime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Keychain.Keies.Key.Key_.KeyId.SendLifetime', 
                [], [], 
                '''                Lifetime of the key
                ''',
                'send_lifetime',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'key-id',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper'
        ),
    },
    'Keychain.Keies.Key.Key_' : {
        'meta_info' : _MetaInfoClass('Keychain.Keies.Key.Key_',
            False, 
            [
            _MetaInfoClassMember('key-id', REFERENCE_LIST, 'KeyId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Keychain.Keies.Key.Key_.KeyId', 
                [], [], 
                '''                key id
                ''',
                'key_id',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'key',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper'
        ),
    },
    'Keychain.Keies.Key' : {
        'meta_info' : _MetaInfoClass('Keychain.Keies.Key',
            False, 
            [
            _MetaInfoClassMember('key-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Key name
                ''',
                'key_name',
                'Cisco-IOS-XR-lib-keychain-oper', True),
            _MetaInfoClassMember('accept-tolerance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Accept tolerance is infinite if value is
                0xffffffff
                ''',
                'accept_tolerance',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            _MetaInfoClassMember('key', REFERENCE_CLASS, 'Key_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Keychain.Keies.Key.Key_', 
                [], [], 
                '''                Key properties
                ''',
                'key',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'key',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper'
        ),
    },
    'Keychain.Keies' : {
        'meta_info' : _MetaInfoClass('Keychain.Keies',
            False, 
            [
            _MetaInfoClassMember('key', REFERENCE_LIST, 'Key' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Keychain.Keies.Key', 
                [], [], 
                '''                Configured key name
                ''',
                'key',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'keies',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper'
        ),
    },
    'Keychain' : {
        'meta_info' : _MetaInfoClass('Keychain',
            False, 
            [
            _MetaInfoClassMember('keies', REFERENCE_CLASS, 'Keies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper', 'Keychain.Keies', 
                [], [], 
                '''                List of configured key names
                ''',
                'keies',
                'Cisco-IOS-XR-lib-keychain-oper', False),
            ],
            'Cisco-IOS-XR-lib-keychain-oper',
            'keychain',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_oper'
        ),
    },
}
_meta_table['Keychain.Keies.Key.Key_.KeyId.SendLifetime']['meta_info'].parent =_meta_table['Keychain.Keies.Key.Key_.KeyId']['meta_info']
_meta_table['Keychain.Keies.Key.Key_.KeyId.AcceptLifetime']['meta_info'].parent =_meta_table['Keychain.Keies.Key.Key_.KeyId']['meta_info']
_meta_table['Keychain.Keies.Key.Key_.KeyId']['meta_info'].parent =_meta_table['Keychain.Keies.Key.Key_']['meta_info']
_meta_table['Keychain.Keies.Key.Key_']['meta_info'].parent =_meta_table['Keychain.Keies.Key']['meta_info']
_meta_table['Keychain.Keies.Key']['meta_info'].parent =_meta_table['Keychain.Keies']['meta_info']
_meta_table['Keychain.Keies']['meta_info'].parent =_meta_table['Keychain']['meta_info']
