


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'KeyGenerateRsaGeneralKeysRpc.Input' : {
        'meta_info' : _MetaInfoClass('KeyGenerateRsaGeneralKeysRpc.Input',
            False, 
            [
            _MetaInfoClassMember('key-label', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                RSA keypair label
                ''',
                'key_label',
                'Cisco-IOS-XR-crypto-act', False),
            _MetaInfoClassMember('key-modulus', ATTRIBUTE, 'int' , None, None, 
                [('512', '4096')], [], 
                '''                Key modulus in the range of 512 to 4096 for your General Purpose Keypair. Choosing a key modulus greater than 512 may take a few minutes
                ''',
                'key_modulus',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'KeyGenerateRsaGeneralKeysRpc' : {
        'meta_info' : _MetaInfoClass('KeyGenerateRsaGeneralKeysRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'KeyGenerateRsaGeneralKeysRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'key-generate-rsa-general-keys',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'KeyGenerateRsaUsageKeysRpc.Input' : {
        'meta_info' : _MetaInfoClass('KeyGenerateRsaUsageKeysRpc.Input',
            False, 
            [
            _MetaInfoClassMember('key-label', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                RSA keypair label
                ''',
                'key_label',
                'Cisco-IOS-XR-crypto-act', False),
            _MetaInfoClassMember('key-modulus', ATTRIBUTE, 'int' , None, None, 
                [('512', '4096')], [], 
                '''                Key modulus in the range of 512 to 4096 for your General Purpose Keypair. Choosing a key modulus greater than 512 may take a few minutes
                ''',
                'key_modulus',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'KeyGenerateRsaUsageKeysRpc' : {
        'meta_info' : _MetaInfoClass('KeyGenerateRsaUsageKeysRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'KeyGenerateRsaUsageKeysRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'key-generate-rsa-usage-keys',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'KeyGenerateRsaRpc.Input' : {
        'meta_info' : _MetaInfoClass('KeyGenerateRsaRpc.Input',
            False, 
            [
            _MetaInfoClassMember('key-label', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                RSA keypair label
                ''',
                'key_label',
                'Cisco-IOS-XR-crypto-act', False),
            _MetaInfoClassMember('key-modulus', ATTRIBUTE, 'int' , None, None, 
                [('512', '4096')], [], 
                '''                Key modulus in the range of 512 to 4096 for your General Purpose Keypair. Choosing a key modulus greater than 512 may take a few minutes
                ''',
                'key_modulus',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'KeyGenerateRsaRpc' : {
        'meta_info' : _MetaInfoClass('KeyGenerateRsaRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'KeyGenerateRsaRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'key-generate-rsa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'KeyGenerateDsaRpc.Input' : {
        'meta_info' : _MetaInfoClass('KeyGenerateDsaRpc.Input',
            False, 
            [
            _MetaInfoClassMember('key-modulus', ATTRIBUTE, 'int' , None, None, 
                [('512', 'None'), ('768', 'None'), ('1024', 'None')], [], 
                '''                Key modulus size can be 512, 768, or 1024 bits.
                ''',
                'key_modulus',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'KeyGenerateDsaRpc' : {
        'meta_info' : _MetaInfoClass('KeyGenerateDsaRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'KeyGenerateDsaRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'key-generate-dsa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'KeyZeroizeRsaRpc.Input' : {
        'meta_info' : _MetaInfoClass('KeyZeroizeRsaRpc.Input',
            False, 
            [
            _MetaInfoClassMember('key-label', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                RSA key label
                ''',
                'key_label',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'KeyZeroizeRsaRpc' : {
        'meta_info' : _MetaInfoClass('KeyZeroizeRsaRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'KeyZeroizeRsaRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'key-zeroize-rsa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'KeyZeroizeDsaRpc' : {
        'meta_info' : _MetaInfoClass('KeyZeroizeDsaRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-crypto-act',
            'key-zeroize-dsa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'KeyZeroizeAuthenticationRsaRpc' : {
        'meta_info' : _MetaInfoClass('KeyZeroizeAuthenticationRsaRpc',
            False, 
            [
            ],
            'Cisco-IOS-XR-crypto-act',
            'key-zeroize-authentication-rsa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'KeyImportAuthenticationRsaRpc.Input' : {
        'meta_info' : _MetaInfoClass('KeyImportAuthenticationRsaRpc.Input',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path to RSA pubkey file
                ''',
                'path',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'KeyImportAuthenticationRsaRpc' : {
        'meta_info' : _MetaInfoClass('KeyImportAuthenticationRsaRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'KeyImportAuthenticationRsaRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'key-import-authentication-rsa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaAuthenticateRpc.Input' : {
        'meta_info' : _MetaInfoClass('CaAuthenticateRpc.Input',
            False, 
            [
            _MetaInfoClassMember('server-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                CA Server Name
                ''',
                'server_name',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaAuthenticateRpc' : {
        'meta_info' : _MetaInfoClass('CaAuthenticateRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'CaAuthenticateRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'ca-authenticate',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaEnrollRpc.Input' : {
        'meta_info' : _MetaInfoClass('CaEnrollRpc.Input',
            False, 
            [
            _MetaInfoClassMember('server-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                CA Server Name
                ''',
                'server_name',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaEnrollRpc' : {
        'meta_info' : _MetaInfoClass('CaEnrollRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'CaEnrollRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'ca-enroll',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaImportCertificateRpc.Input' : {
        'meta_info' : _MetaInfoClass('CaImportCertificateRpc.Input',
            False, 
            [
            _MetaInfoClassMember('server-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                CA Server Name
                ''',
                'server_name',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaImportCertificateRpc' : {
        'meta_info' : _MetaInfoClass('CaImportCertificateRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'CaImportCertificateRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'ca-import-certificate',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaCancelEnrollRpc.Input' : {
        'meta_info' : _MetaInfoClass('CaCancelEnrollRpc.Input',
            False, 
            [
            _MetaInfoClassMember('server-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                CA Server Name
                ''',
                'server_name',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaCancelEnrollRpc' : {
        'meta_info' : _MetaInfoClass('CaCancelEnrollRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'CaCancelEnrollRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'ca-cancel-enroll',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaCrlRequestRpc.Input' : {
        'meta_info' : _MetaInfoClass('CaCrlRequestRpc.Input',
            False, 
            [
            _MetaInfoClassMember('uri', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                CRL Distribution Point in URI format
                ''',
                'uri',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaCrlRequestRpc.Output' : {
        'meta_info' : _MetaInfoClass('CaCrlRequestRpc.Output',
            False, 
            [
            _MetaInfoClassMember('certificate', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Certificate returned
                ''',
                'certificate',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaCrlRequestRpc' : {
        'meta_info' : _MetaInfoClass('CaCrlRequestRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'CaCrlRequestRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-crypto-act', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'CaCrlRequestRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'ca-crl-request',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaTrustpoolImportUrlRpc.Input' : {
        'meta_info' : _MetaInfoClass('CaTrustpoolImportUrlRpc.Input',
            False, 
            [
            _MetaInfoClassMember('url', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                in URL format
                ''',
                'url',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaTrustpoolImportUrlRpc' : {
        'meta_info' : _MetaInfoClass('CaTrustpoolImportUrlRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'CaTrustpoolImportUrlRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'ca-trustpool-import-url',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaTrustpoolImportUrlCleanRpc.Input' : {
        'meta_info' : _MetaInfoClass('CaTrustpoolImportUrlCleanRpc.Input',
            False, 
            [
            _MetaInfoClassMember('url', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                in URL format
                ''',
                'url',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
    'CaTrustpoolImportUrlCleanRpc' : {
        'meta_info' : _MetaInfoClass('CaTrustpoolImportUrlCleanRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act', 'CaTrustpoolImportUrlCleanRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-crypto-act', False),
            ],
            'Cisco-IOS-XR-crypto-act',
            'ca-trustpool-import-url-clean',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_act'
        ),
    },
}
_meta_table['KeyGenerateRsaGeneralKeysRpc.Input']['meta_info'].parent =_meta_table['KeyGenerateRsaGeneralKeysRpc']['meta_info']
_meta_table['KeyGenerateRsaUsageKeysRpc.Input']['meta_info'].parent =_meta_table['KeyGenerateRsaUsageKeysRpc']['meta_info']
_meta_table['KeyGenerateRsaRpc.Input']['meta_info'].parent =_meta_table['KeyGenerateRsaRpc']['meta_info']
_meta_table['KeyGenerateDsaRpc.Input']['meta_info'].parent =_meta_table['KeyGenerateDsaRpc']['meta_info']
_meta_table['KeyZeroizeRsaRpc.Input']['meta_info'].parent =_meta_table['KeyZeroizeRsaRpc']['meta_info']
_meta_table['KeyImportAuthenticationRsaRpc.Input']['meta_info'].parent =_meta_table['KeyImportAuthenticationRsaRpc']['meta_info']
_meta_table['CaAuthenticateRpc.Input']['meta_info'].parent =_meta_table['CaAuthenticateRpc']['meta_info']
_meta_table['CaEnrollRpc.Input']['meta_info'].parent =_meta_table['CaEnrollRpc']['meta_info']
_meta_table['CaImportCertificateRpc.Input']['meta_info'].parent =_meta_table['CaImportCertificateRpc']['meta_info']
_meta_table['CaCancelEnrollRpc.Input']['meta_info'].parent =_meta_table['CaCancelEnrollRpc']['meta_info']
_meta_table['CaCrlRequestRpc.Input']['meta_info'].parent =_meta_table['CaCrlRequestRpc']['meta_info']
_meta_table['CaCrlRequestRpc.Output']['meta_info'].parent =_meta_table['CaCrlRequestRpc']['meta_info']
_meta_table['CaTrustpoolImportUrlRpc.Input']['meta_info'].parent =_meta_table['CaTrustpoolImportUrlRpc']['meta_info']
_meta_table['CaTrustpoolImportUrlCleanRpc.Input']['meta_info'].parent =_meta_table['CaTrustpoolImportUrlCleanRpc']['meta_info']
