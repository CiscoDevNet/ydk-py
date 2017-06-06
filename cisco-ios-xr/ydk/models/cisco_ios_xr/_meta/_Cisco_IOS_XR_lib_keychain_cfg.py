


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CryptoAlgEnum' : _MetaInfoEnum('CryptoAlgEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg',
        {
            'alg-hmac-sha1-12':'alg_hmac_sha1_12',
            'alg-md5-16':'alg_md5_16',
            'alg-sha1-20':'alg_sha1_20',
            'alg-hmac-md5-16':'alg_hmac_md5_16',
            'alg-hmac-sha1-20':'alg_hmac_sha1_20',
        }, 'Cisco-IOS-XR-lib-keychain-cfg', _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-cfg']),
    'KeyChainMonthEnum' : _MetaInfoEnum('KeyChainMonthEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg',
        {
            'jan':'jan',
            'feb':'feb',
            'mar':'mar',
            'apr':'apr',
            'may':'may',
            'jun':'jun',
            'jul':'jul',
            'aug':'aug',
            'sep':'sep',
            'oct':'oct',
            'nov':'nov',
            'dec':'dec',
        }, 'Cisco-IOS-XR-lib-keychain-cfg', _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-cfg']),
    'Keychains.Keychain.AcceptTolerance' : {
        'meta_info' : _MetaInfoClass('Keychains.Keychain.AcceptTolerance',
            False, 
            [
            _MetaInfoClassMember('infinite', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Infinite tolerance
                ''',
                'infinite',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('1', '8640000')], [], 
                '''                Value in seconds
                ''',
                'value',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-cfg',
            'accept-tolerance',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg'
        ),
    },
    'Keychains.Keychain.Keies.Key.AcceptLifetime' : {
        'meta_info' : _MetaInfoClass('Keychains.Keychain.Keies.Key.AcceptLifetime',
            False, 
            [
            _MetaInfoClassMember('end-date', ATTRIBUTE, 'int' , None, None, 
                [('1', '31')], [], 
                '''                End Date
                ''',
                'end_date',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('end-hour', ATTRIBUTE, 'int' , None, None, 
                [('0', '23')], [], 
                '''                End Hour
                ''',
                'end_hour',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('end-minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                End Minutes
                ''',
                'end_minutes',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('end-month', REFERENCE_ENUM_CLASS, 'KeyChainMonthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'KeyChainMonthEnum', 
                [], [], 
                '''                End Month
                ''',
                'end_month',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('end-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                End Seconds
                ''',
                'end_seconds',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('end-year', ATTRIBUTE, 'int' , None, None, 
                [('1993', '2035')], [], 
                '''                End Year
                ''',
                'end_year',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('infinite-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Infinite Lifetime flag
                ''',
                'infinite_flag',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('life-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Lifetime duration in seconds
                ''',
                'life_time',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('start-date', ATTRIBUTE, 'int' , None, None, 
                [('1', '31')], [], 
                '''                Start Date
                ''',
                'start_date',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('start-hour', ATTRIBUTE, 'int' , None, None, 
                [('0', '23')], [], 
                '''                Start Hour
                ''',
                'start_hour',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('start-minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                Start Minutes
                ''',
                'start_minutes',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('start-month', REFERENCE_ENUM_CLASS, 'KeyChainMonthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'KeyChainMonthEnum', 
                [], [], 
                '''                Start Month
                ''',
                'start_month',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('start-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                Start Seconds
                ''',
                'start_seconds',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('start-year', ATTRIBUTE, 'int' , None, None, 
                [('1993', '2035')], [], 
                '''                Start Year
                ''',
                'start_year',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-cfg',
            'accept-lifetime',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg'
        ),
    },
    'Keychains.Keychain.Keies.Key.SendLifetime' : {
        'meta_info' : _MetaInfoClass('Keychains.Keychain.Keies.Key.SendLifetime',
            False, 
            [
            _MetaInfoClassMember('end-date', ATTRIBUTE, 'int' , None, None, 
                [('1', '31')], [], 
                '''                End Date
                ''',
                'end_date',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('end-hour', ATTRIBUTE, 'int' , None, None, 
                [('0', '23')], [], 
                '''                End Hour
                ''',
                'end_hour',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('end-minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                End Minutes
                ''',
                'end_minutes',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('end-month', REFERENCE_ENUM_CLASS, 'KeyChainMonthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'KeyChainMonthEnum', 
                [], [], 
                '''                End Month
                ''',
                'end_month',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('end-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                End Seconds
                ''',
                'end_seconds',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('end-year', ATTRIBUTE, 'int' , None, None, 
                [('1993', '2035')], [], 
                '''                End Year
                ''',
                'end_year',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('infinite-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Infinite Lifetime flag
                ''',
                'infinite_flag',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('life-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Lifetime duration in seconds
                ''',
                'life_time',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('start-date', ATTRIBUTE, 'int' , None, None, 
                [('1', '31')], [], 
                '''                Start Date
                ''',
                'start_date',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('start-hour', ATTRIBUTE, 'int' , None, None, 
                [('0', '23')], [], 
                '''                Start Hour
                ''',
                'start_hour',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('start-minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                Start Minutes
                ''',
                'start_minutes',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('start-month', REFERENCE_ENUM_CLASS, 'KeyChainMonthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'KeyChainMonthEnum', 
                [], [], 
                '''                Start Month
                ''',
                'start_month',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('start-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                Start Seconds
                ''',
                'start_seconds',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('start-year', ATTRIBUTE, 'int' , None, None, 
                [('1993', '2035')], [], 
                '''                Start Year
                ''',
                'start_year',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-cfg',
            'send-lifetime',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg'
        ),
    },
    'Keychains.Keychain.Keies.Key' : {
        'meta_info' : _MetaInfoClass('Keychains.Keychain.Keies.Key',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                48-bit Key identifier
                ''',
                'key_id',
                'Cisco-IOS-XR-lib-keychain-cfg', True),
            _MetaInfoClassMember('accept-lifetime', REFERENCE_CLASS, 'AcceptLifetime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'Keychains.Keychain.Keies.Key.AcceptLifetime', 
                [], [], 
                '''                Configure a key Acceptance Lifetime
                ''',
                'accept_lifetime',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('cryptographic-algorithm', REFERENCE_ENUM_CLASS, 'CryptoAlgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'CryptoAlgEnum', 
                [], [], 
                '''                Configure the cryptographic algorithm
                ''',
                'cryptographic_algorithm',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('key-string', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Configure a clear text/encrypted Key string 
                ''',
                'key_string',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('send-lifetime', REFERENCE_CLASS, 'SendLifetime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'Keychains.Keychain.Keies.Key.SendLifetime', 
                [], [], 
                '''                Configure a Send Lifetime
                ''',
                'send_lifetime',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-cfg',
            'key',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg'
        ),
    },
    'Keychains.Keychain.Keies' : {
        'meta_info' : _MetaInfoClass('Keychains.Keychain.Keies',
            False, 
            [
            _MetaInfoClassMember('key', REFERENCE_LIST, 'Key' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'Keychains.Keychain.Keies.Key', 
                [], [], 
                '''                Key Identifier
                ''',
                'key',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-cfg',
            'keies',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg'
        ),
    },
    'Keychains.Keychain' : {
        'meta_info' : _MetaInfoClass('Keychains.Keychain',
            False, 
            [
            _MetaInfoClassMember('chain-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the key chain
                ''',
                'chain_name',
                'Cisco-IOS-XR-lib-keychain-cfg', True),
            _MetaInfoClassMember('accept-tolerance', REFERENCE_CLASS, 'AcceptTolerance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'Keychains.Keychain.AcceptTolerance', 
                [], [], 
                '''                Accept Tolerance in seconds or infinite
                ''',
                'accept_tolerance',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            _MetaInfoClassMember('keies', REFERENCE_CLASS, 'Keies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'Keychains.Keychain.Keies', 
                [], [], 
                '''                Configure a Key
                ''',
                'keies',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-cfg',
            'keychain',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg'
        ),
    },
    'Keychains' : {
        'meta_info' : _MetaInfoClass('Keychains',
            False, 
            [
            _MetaInfoClassMember('keychain', REFERENCE_LIST, 'Keychain' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg', 'Keychains.Keychain', 
                [], [], 
                '''                Name of the key chain
                ''',
                'keychain',
                'Cisco-IOS-XR-lib-keychain-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-cfg',
            'keychains',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_cfg'
        ),
    },
}
_meta_table['Keychains.Keychain.Keies.Key.AcceptLifetime']['meta_info'].parent =_meta_table['Keychains.Keychain.Keies.Key']['meta_info']
_meta_table['Keychains.Keychain.Keies.Key.SendLifetime']['meta_info'].parent =_meta_table['Keychains.Keychain.Keies.Key']['meta_info']
_meta_table['Keychains.Keychain.Keies.Key']['meta_info'].parent =_meta_table['Keychains.Keychain.Keies']['meta_info']
_meta_table['Keychains.Keychain.AcceptTolerance']['meta_info'].parent =_meta_table['Keychains.Keychain']['meta_info']
_meta_table['Keychains.Keychain.Keies']['meta_info'].parent =_meta_table['Keychains.Keychain']['meta_info']
_meta_table['Keychains.Keychain']['meta_info'].parent =_meta_table['Keychains']['meta_info']
