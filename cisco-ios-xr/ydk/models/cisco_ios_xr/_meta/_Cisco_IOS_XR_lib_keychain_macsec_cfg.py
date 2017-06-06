


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MacSecKeyChainMonthEnum' : _MetaInfoEnum('MacSecKeyChainMonthEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg',
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
        }, 'Cisco-IOS-XR-lib-keychain-macsec-cfg', _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-macsec-cfg']),
    'MacSecCryptoAlgEnum' : _MetaInfoEnum('MacSecCryptoAlgEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg',
        {
            'aes-128-cmac':'aes_128_cmac',
            'aes-256-cmac':'aes_256_cmac',
        }, 'Cisco-IOS-XR-lib-keychain-macsec-cfg', _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-macsec-cfg']),
    'MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime' : {
        'meta_info' : _MetaInfoClass('MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime',
            False, 
            [
            _MetaInfoClassMember('end-date', ATTRIBUTE, 'int' , None, None, 
                [('1', '31')], [], 
                '''                End Date
                ''',
                'end_date',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('end-hour', ATTRIBUTE, 'int' , None, None, 
                [('0', '23')], [], 
                '''                End Hour
                ''',
                'end_hour',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('end-minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                End Minutes
                ''',
                'end_minutes',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('end-month', REFERENCE_ENUM_CLASS, 'MacSecKeyChainMonthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg', 'MacSecKeyChainMonthEnum', 
                [], [], 
                '''                End Month
                ''',
                'end_month',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('end-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                End Seconds
                ''',
                'end_seconds',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('end-year', ATTRIBUTE, 'int' , None, None, 
                [('1993', '2035')], [], 
                '''                End Year
                ''',
                'end_year',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('infinite-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Infinite Lifetime flag
                ''',
                'infinite_flag',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('life-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Lifetime duration in seconds
                ''',
                'life_time',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('start-date', ATTRIBUTE, 'int' , None, None, 
                [('1', '31')], [], 
                '''                Start Date
                ''',
                'start_date',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('start-hour', ATTRIBUTE, 'int' , None, None, 
                [('0', '23')], [], 
                '''                Start Hour
                ''',
                'start_hour',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('start-minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                Start Minutes
                ''',
                'start_minutes',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('start-month', REFERENCE_ENUM_CLASS, 'MacSecKeyChainMonthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg', 'MacSecKeyChainMonthEnum', 
                [], [], 
                '''                Start Month
                ''',
                'start_month',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('start-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                Start Seconds
                ''',
                'start_seconds',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('start-year', ATTRIBUTE, 'int' , None, None, 
                [('1993', '2035')], [], 
                '''                Start Year
                ''',
                'start_year',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-macsec-cfg',
            'lifetime',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-macsec-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg'
        ),
    },
    'MacSecKeychains.MacSecKeychain.Keies.Key.KeyString' : {
        'meta_info' : _MetaInfoClass('MacSecKeychains.MacSecKeychain.Keies.Key.KeyString',
            False, 
            [
            _MetaInfoClassMember('cryptographic-algorithm', REFERENCE_ENUM_CLASS, 'MacSecCryptoAlgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg', 'MacSecCryptoAlgEnum', 
                [], [], 
                '''                Cryptographic Algorithm
                ''',
                'cryptographic_algorithm',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('string', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Key String
                ''',
                'string',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-macsec-cfg',
            'key-string',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-macsec-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg'
        ),
    },
    'MacSecKeychains.MacSecKeychain.Keies.Key' : {
        'meta_info' : _MetaInfoClass('MacSecKeychains.MacSecKeychain.Keies.Key',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                48-bit Key identifier
                ''',
                'key_id',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', True),
            _MetaInfoClassMember('key-string', REFERENCE_CLASS, 'KeyString' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg', 'MacSecKeychains.MacSecKeychain.Keies.Key.KeyString', 
                [], [], 
                '''                Configure a clear text/encrypted Key string
                along with cryptographic algorithm
                ''',
                'key_string',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            _MetaInfoClassMember('lifetime', REFERENCE_CLASS, 'Lifetime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg', 'MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime', 
                [], [], 
                '''                Configure a key Lifetime
                ''',
                'lifetime',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-macsec-cfg',
            'key',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-macsec-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg'
        ),
    },
    'MacSecKeychains.MacSecKeychain.Keies' : {
        'meta_info' : _MetaInfoClass('MacSecKeychains.MacSecKeychain.Keies',
            False, 
            [
            _MetaInfoClassMember('key', REFERENCE_LIST, 'Key' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg', 'MacSecKeychains.MacSecKeychain.Keies.Key', 
                [], [], 
                '''                Key Identifier
                ''',
                'key',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-macsec-cfg',
            'keies',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-macsec-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg'
        ),
    },
    'MacSecKeychains.MacSecKeychain' : {
        'meta_info' : _MetaInfoClass('MacSecKeychains.MacSecKeychain',
            False, 
            [
            _MetaInfoClassMember('chain-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the key chain
                ''',
                'chain_name',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', True),
            _MetaInfoClassMember('keies', REFERENCE_CLASS, 'Keies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg', 'MacSecKeychains.MacSecKeychain.Keies', 
                [], [], 
                '''                Configure a Key
                ''',
                'keies',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-macsec-cfg',
            'mac-sec-keychain',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-macsec-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg'
        ),
    },
    'MacSecKeychains' : {
        'meta_info' : _MetaInfoClass('MacSecKeychains',
            False, 
            [
            _MetaInfoClassMember('mac-sec-keychain', REFERENCE_LIST, 'MacSecKeychain' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg', 'MacSecKeychains.MacSecKeychain', 
                [], [], 
                '''                Name of the key chain for MACSec
                ''',
                'mac_sec_keychain',
                'Cisco-IOS-XR-lib-keychain-macsec-cfg', False),
            ],
            'Cisco-IOS-XR-lib-keychain-macsec-cfg',
            'mac-sec-keychains',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-keychain-macsec-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_macsec_cfg'
        ),
    },
}
_meta_table['MacSecKeychains.MacSecKeychain.Keies.Key.Lifetime']['meta_info'].parent =_meta_table['MacSecKeychains.MacSecKeychain.Keies.Key']['meta_info']
_meta_table['MacSecKeychains.MacSecKeychain.Keies.Key.KeyString']['meta_info'].parent =_meta_table['MacSecKeychains.MacSecKeychain.Keies.Key']['meta_info']
_meta_table['MacSecKeychains.MacSecKeychain.Keies.Key']['meta_info'].parent =_meta_table['MacSecKeychains.MacSecKeychain.Keies']['meta_info']
_meta_table['MacSecKeychains.MacSecKeychain.Keies']['meta_info'].parent =_meta_table['MacSecKeychains.MacSecKeychain']['meta_info']
_meta_table['MacSecKeychains.MacSecKeychain']['meta_info'].parent =_meta_table['MacSecKeychains']['meta_info']
