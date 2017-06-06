


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MacsecMkaSecurityPolicyEnum' : _MetaInfoEnum('MacsecMkaSecurityPolicyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg',
        {
            'should-secure':'should_secure',
            'must-secure':'must_secure',
        }, 'Cisco-IOS-XR-crypto-macsec-mka-cfg', _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-cfg']),
    'MacsecMkaConfOffsetEnum' : _MetaInfoEnum('MacsecMkaConfOffsetEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg',
        {
            'conf-off-set-0':'conf_off_set_0',
            'conf-off-set-30':'conf_off_set_30',
            'conf-off-set-50':'conf_off_set_50',
        }, 'Cisco-IOS-XR-crypto-macsec-mka-cfg', _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-cfg']),
    'MacsecMkaPolicyExceptionEnum' : _MetaInfoEnum('MacsecMkaPolicyExceptionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg',
        {
            'lacp-in-clear':'lacp_in_clear',
        }, 'Cisco-IOS-XR-crypto-macsec-mka-cfg', _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-cfg']),
    'MacsecMkaCipherSuiteEnum' : _MetaInfoEnum('MacsecMkaCipherSuiteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg',
        {
            'gcm-aes-128':'gcm_aes_128',
            'gcm-aes-256':'gcm_aes_256',
            'gcm-aes-xpn-128':'gcm_aes_xpn_128',
            'gcm-aes-xpn-256':'gcm_aes_xpn_256',
        }, 'Cisco-IOS-XR-crypto-macsec-mka-cfg', _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-cfg']),
    'Macsec.Policy' : {
        'meta_info' : _MetaInfoClass('Macsec.Policy',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 16)], [], 
                '''                Name of the Policy of maximum length 16
                ''',
                'name',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', True),
            _MetaInfoClassMember('cipher-suite', REFERENCE_ENUM_CLASS, 'MacsecMkaCipherSuiteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaCipherSuiteEnum', 
                [], [], 
                '''                Cipher-suite of Policy
                ''',
                'cipher_suite',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('conf-offset', REFERENCE_ENUM_CLASS, 'MacsecMkaConfOffsetEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaConfOffsetEnum', 
                [], [], 
                '''                Conf-Offset of Policy
                ''',
                'conf_offset',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('delay-protection', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE enables data delay protection
                ''',
                'delay_protection',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('include-icv-indicator', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE enables Include ICV Indicator paramset in
                MKPDU
                ''',
                'include_icv_indicator',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('key-server-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Key-Server-Priority of Policy
                ''',
                'key_server_priority',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('policy-exception', REFERENCE_ENUM_CLASS, 'MacsecMkaPolicyExceptionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaPolicyExceptionEnum', 
                [], [], 
                '''                Macsec policy exception for packets to be in
                clear
                ''',
                'policy_exception',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('sak-rekey-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '43200')], [], 
                '''                Interval after which key-server generates new
                SAK for a Secured Session
                ''',
                'sak_rekey_interval',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('security-policy', REFERENCE_ENUM_CLASS, 'MacsecMkaSecurityPolicyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'MacsecMkaSecurityPolicyEnum', 
                [], [], 
                '''                Security-Policy of Policy
                ''',
                'security_policy',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('vlan-tags-in-clear', ATTRIBUTE, 'int' , None, None, 
                [('1', '2')], [], 
                '''                VLAN-Tags-In-Clear of Policy
                ''',
                'vlan_tags_in_clear',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            _MetaInfoClassMember('window-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '1024')], [], 
                '''                Window-Size of Policy
                ''',
                'window_size',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-cfg',
            'policy',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg'
        ),
    },
    'Macsec' : {
        'meta_info' : _MetaInfoClass('Macsec',
            False, 
            [
            _MetaInfoClassMember('policy', REFERENCE_LIST, 'Policy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg', 'Macsec.Policy', 
                [], [], 
                '''                MACSec Policy
                ''',
                'policy',
                'Cisco-IOS-XR-crypto-macsec-mka-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-cfg',
            'macsec',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg'
        ),
    },
}
_meta_table['Macsec.Policy']['meta_info'].parent =_meta_table['Macsec']['meta_info']
