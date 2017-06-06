


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'KeyChains.AcceptTolerance' : {
        'meta_info' : _MetaInfoClass('KeyChains.AcceptTolerance',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tolerance range, in seconds.
                ''',
                'duration',
                'ietf-key-chain', False),
            ],
            'ietf-key-chain',
            'accept-tolerance',
            _yang_ns._namespaces['ietf-key-chain'],
        'ydk.models.ietf.ietf_key_chain'
        ),
    },
    'KeyChains.Key.KeyString' : {
        'meta_info' : _MetaInfoClass('KeyChains.Key.KeyString',
            False, 
            [
            _MetaInfoClassMember('hexadecimal-string', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Key in hexadecimal string format.
                ''',
                'hexadecimal_string',
                'ietf-key-chain', False),
            _MetaInfoClassMember('keystring', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Key string in ASCII format.
                ''',
                'keystring',
                'ietf-key-chain', False),
            ],
            'ietf-key-chain',
            'key-string',
            _yang_ns._namespaces['ietf-key-chain'],
        'ydk.models.ietf.ietf_key_chain'
        ),
    },
    'KeyChains.Key.Lifetime.SendAcceptLifetime' : {
        'meta_info' : _MetaInfoClass('KeyChains.Key.Lifetime.SendAcceptLifetime',
            False, 
            [
            _MetaInfoClassMember('always', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Indicates key lifetime is always valid.
                ''',
                'always',
                'ietf-key-chain', False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483646')], [], 
                '''                Key lifetime duration, in seconds
                ''',
                'duration',
                'ietf-key-chain', False),
            _MetaInfoClassMember('end-date-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                End time.
                ''',
                'end_date_time',
                'ietf-key-chain', False),
            _MetaInfoClassMember('no-end-time', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Indicates key lifetime end-time in infinite.
                ''',
                'no_end_time',
                'ietf-key-chain', False),
            _MetaInfoClassMember('start-date-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Start time.
                ''',
                'start_date_time',
                'ietf-key-chain', False),
            ],
            'ietf-key-chain',
            'send-accept-lifetime',
            _yang_ns._namespaces['ietf-key-chain'],
        'ydk.models.ietf.ietf_key_chain'
        ),
    },
    'KeyChains.Key.Lifetime.SendLifetime' : {
        'meta_info' : _MetaInfoClass('KeyChains.Key.Lifetime.SendLifetime',
            False, 
            [
            _MetaInfoClassMember('always', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Indicates key lifetime is always valid.
                ''',
                'always',
                'ietf-key-chain', False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483646')], [], 
                '''                Key lifetime duration, in seconds
                ''',
                'duration',
                'ietf-key-chain', False),
            _MetaInfoClassMember('end-date-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                End time.
                ''',
                'end_date_time',
                'ietf-key-chain', False),
            _MetaInfoClassMember('no-end-time', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Indicates key lifetime end-time in infinite.
                ''',
                'no_end_time',
                'ietf-key-chain', False),
            _MetaInfoClassMember('start-date-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Start time.
                ''',
                'start_date_time',
                'ietf-key-chain', False),
            ],
            'ietf-key-chain',
            'send-lifetime',
            _yang_ns._namespaces['ietf-key-chain'],
        'ydk.models.ietf.ietf_key_chain'
        ),
    },
    'KeyChains.Key.Lifetime.AcceptLifetime' : {
        'meta_info' : _MetaInfoClass('KeyChains.Key.Lifetime.AcceptLifetime',
            False, 
            [
            _MetaInfoClassMember('always', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Indicates key lifetime is always valid.
                ''',
                'always',
                'ietf-key-chain', False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483646')], [], 
                '''                Key lifetime duration, in seconds
                ''',
                'duration',
                'ietf-key-chain', False),
            _MetaInfoClassMember('end-date-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                End time.
                ''',
                'end_date_time',
                'ietf-key-chain', False),
            _MetaInfoClassMember('no-end-time', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Indicates key lifetime end-time in infinite.
                ''',
                'no_end_time',
                'ietf-key-chain', False),
            _MetaInfoClassMember('start-date-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Start time.
                ''',
                'start_date_time',
                'ietf-key-chain', False),
            ],
            'ietf-key-chain',
            'accept-lifetime',
            _yang_ns._namespaces['ietf-key-chain'],
        'ydk.models.ietf.ietf_key_chain'
        ),
    },
    'KeyChains.Key.Lifetime' : {
        'meta_info' : _MetaInfoClass('KeyChains.Key.Lifetime',
            False, 
            [
            _MetaInfoClassMember('accept-lifetime', REFERENCE_CLASS, 'AcceptLifetime' , 'ydk.models.ietf.ietf_key_chain', 'KeyChains.Key.Lifetime.AcceptLifetime', 
                [], [], 
                '''                Separate lifetime specification for accept
                lifetime.
                ''',
                'accept_lifetime',
                'ietf-key-chain', False),
            _MetaInfoClassMember('send-accept-lifetime', REFERENCE_CLASS, 'SendAcceptLifetime' , 'ydk.models.ietf.ietf_key_chain', 'KeyChains.Key.Lifetime.SendAcceptLifetime', 
                [], [], 
                '''                Single lifetime specification for both send and
                accept lifetimes.
                ''',
                'send_accept_lifetime',
                'ietf-key-chain', False),
            _MetaInfoClassMember('send-lifetime', REFERENCE_CLASS, 'SendLifetime' , 'ydk.models.ietf.ietf_key_chain', 'KeyChains.Key.Lifetime.SendLifetime', 
                [], [], 
                '''                Separate lifetime specification for send
                lifetime.
                ''',
                'send_lifetime',
                'ietf-key-chain', False),
            ],
            'ietf-key-chain',
            'lifetime',
            _yang_ns._namespaces['ietf-key-chain'],
        'ydk.models.ietf.ietf_key_chain'
        ),
    },
    'KeyChains.Key.CryptoAlgorithm' : {
        'meta_info' : _MetaInfoClass('KeyChains.Key.CryptoAlgorithm',
            False, 
            [
            _MetaInfoClassMember('hmac-sha1-12', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The HMAC-SHA1-12 algorithm.
                ''',
                'hmac_sha1_12',
                'ietf-key-chain', False),
            _MetaInfoClassMember('hmac-sha1-20', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The HMAC-SHA1-20 algorithm.
                ''',
                'hmac_sha1_20',
                'ietf-key-chain', False),
            _MetaInfoClassMember('hmac-sha-1', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-1 authentication algorithm.
                ''',
                'hmac_sha_1',
                'ietf-key-chain', False),
            _MetaInfoClassMember('hmac-sha-256', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-256 authentication algorithm.
                ''',
                'hmac_sha_256',
                'ietf-key-chain', False),
            _MetaInfoClassMember('hmac-sha-384', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-384 authentication algorithm.
                ''',
                'hmac_sha_384',
                'ietf-key-chain', False),
            _MetaInfoClassMember('hmac-sha-512', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-512 authentication algorithm.
                ''',
                'hmac_sha_512',
                'ietf-key-chain', False),
            _MetaInfoClassMember('md5', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The MD5 algorithm.
                ''',
                'md5',
                'ietf-key-chain', False),
            _MetaInfoClassMember('sha-1', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The SHA-1 algorithm.
                ''',
                'sha_1',
                'ietf-key-chain', False),
            ],
            'ietf-key-chain',
            'crypto-algorithm',
            _yang_ns._namespaces['ietf-key-chain'],
        'ydk.models.ietf.ietf_key_chain'
        ),
    },
    'KeyChains.Key' : {
        'meta_info' : _MetaInfoClass('KeyChains.Key',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Key id.
                ''',
                'key_id',
                'ietf-key-chain', True),
            _MetaInfoClassMember('crypto-algorithm', REFERENCE_CLASS, 'CryptoAlgorithm' , 'ydk.models.ietf.ietf_key_chain', 'KeyChains.Key.CryptoAlgorithm', 
                [], [], 
                '''                Cryptographic algorithm associated with key.
                ''',
                'crypto_algorithm',
                'ietf-key-chain', False),
            _MetaInfoClassMember('key-string', REFERENCE_CLASS, 'KeyString' , 'ydk.models.ietf.ietf_key_chain', 'KeyChains.Key.KeyString', 
                [], [], 
                '''                The key string.
                ''',
                'key_string',
                'ietf-key-chain', False),
            _MetaInfoClassMember('lifetime', REFERENCE_CLASS, 'Lifetime' , 'ydk.models.ietf.ietf_key_chain', 'KeyChains.Key.Lifetime', 
                [], [], 
                '''                Specify a key's lifetime.
                ''',
                'lifetime',
                'ietf-key-chain', False),
            ],
            'ietf-key-chain',
            'key',
            _yang_ns._namespaces['ietf-key-chain'],
        'ydk.models.ietf.ietf_key_chain'
        ),
    },
    'KeyChains' : {
        'meta_info' : _MetaInfoClass('KeyChains',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the key-chain.
                ''',
                'name',
                'ietf-key-chain', True),
            _MetaInfoClassMember('accept-tolerance', REFERENCE_CLASS, 'AcceptTolerance' , 'ydk.models.ietf.ietf_key_chain', 'KeyChains.AcceptTolerance', 
                [], [], 
                '''                Tolerance for key lifetime acceptance (seconds).
                ''',
                'accept_tolerance',
                'ietf-key-chain', False),
            _MetaInfoClassMember('key', REFERENCE_LIST, 'Key' , 'ydk.models.ietf.ietf_key_chain', 'KeyChains.Key', 
                [], [], 
                '''                One key.
                ''',
                'key',
                'ietf-key-chain', False),
            ],
            'ietf-key-chain',
            'key-chains',
            _yang_ns._namespaces['ietf-key-chain'],
        'ydk.models.ietf.ietf_key_chain'
        ),
    },
}
_meta_table['KeyChains.Key.Lifetime.SendAcceptLifetime']['meta_info'].parent =_meta_table['KeyChains.Key.Lifetime']['meta_info']
_meta_table['KeyChains.Key.Lifetime.SendLifetime']['meta_info'].parent =_meta_table['KeyChains.Key.Lifetime']['meta_info']
_meta_table['KeyChains.Key.Lifetime.AcceptLifetime']['meta_info'].parent =_meta_table['KeyChains.Key.Lifetime']['meta_info']
_meta_table['KeyChains.Key.KeyString']['meta_info'].parent =_meta_table['KeyChains.Key']['meta_info']
_meta_table['KeyChains.Key.Lifetime']['meta_info'].parent =_meta_table['KeyChains.Key']['meta_info']
_meta_table['KeyChains.Key.CryptoAlgorithm']['meta_info'].parent =_meta_table['KeyChains.Key']['meta_info']
_meta_table['KeyChains.AcceptTolerance']['meta_info'].parent =_meta_table['KeyChains']['meta_info']
_meta_table['KeyChains.Key']['meta_info'].parent =_meta_table['KeyChains']['meta_info']
