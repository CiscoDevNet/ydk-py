


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'MacsecMkaConfOffsetEnum' : _MetaInfoEnum('MacsecMkaConfOffsetEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg',
        {
            'conf-off-set-0':'CONF_OFF_SET_0',
            'conf-off-set-30':'CONF_OFF_SET_30',
            'conf-off-set-50':'CONF_OFF_SET_50',
        }, 'Cisco-IOS-XR-crypto-macsec-mka-cfg', _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-cfg']),
    'MacsecMkaSecurityPolicyEnum' : _MetaInfoEnum('MacsecMkaSecurityPolicyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg',
        {
            'should-secure':'SHOULD_SECURE',
            'must-secure':'MUST_SECURE',
        }, 'Cisco-IOS-XR-crypto-macsec-mka-cfg', _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-cfg']),
    'MacsecMkaCipherSuiteEnum' : _MetaInfoEnum('MacsecMkaCipherSuiteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_cfg',
        {
            'gcm-aes-128':'GCM_AES_128',
            'gcm-aes-256':'GCM_AES_256',
            'gcm-aes-xpn-128':'GCM_AES_XPN_128',
            'gcm-aes-xpn-256':'GCM_AES_XPN_256',
        }, 'Cisco-IOS-XR-crypto-macsec-mka-cfg', _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-cfg']),
    'Macsec.Policy' : {
        'meta_info' : _MetaInfoClass('Macsec.Policy',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the Policy
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
            _MetaInfoClassMember('key-server-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Key-Server-Priority of Policy
                ''',
                'key_server_priority',
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
