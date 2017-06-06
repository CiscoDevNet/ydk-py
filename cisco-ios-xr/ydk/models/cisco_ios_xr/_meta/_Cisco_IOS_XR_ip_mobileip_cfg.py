


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ServiceTypeEnum' : _MetaInfoEnum('ServiceTypeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'dual':'dual',
        }, 'Cisco-IOS-XR-ip-mobileip-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg']),
    'LmaRoleEnum' : _MetaInfoEnum('LmaRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg',
        {
            '3gma':'Y_3gma',
        }, 'Cisco-IOS-XR-ip-mobileip-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg']),
    'LmaServiceEnum' : _MetaInfoEnum('LmaServiceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg',
        {
            'service-mll':'service_mll',
        }, 'Cisco-IOS-XR-ip-mobileip-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg']),
    'EncapOptEnum' : _MetaInfoEnum('EncapOptEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg',
        {
            'greipv4':'greipv4',
            'greipv6':'greipv6',
            'mgreipv4':'mgreipv4',
            'mgreipv6':'mgreipv6',
        }, 'Cisco-IOS-XR-ip-mobileip-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg']),
    'LmaRatEnum' : _MetaInfoEnum('LmaRatEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg',
        {
            'virtual':'virtual',
            'ppp':'ppp',
            'ethernet':'ethernet',
            'wlan':'wlan',
            'wi-max':'wi_max',
            '3gppgeran':'Y_3gppgeran',
            '3gpputran':'Y_3gpputran',
            '3gppeutran':'Y_3gppeutran',
            '3gpp2ehrpd':'Y_3gpp2ehrpd',
            '3gpp2hrpd':'Y_3gpp2hrpd',
            '3gpp21rtt':'Y_3gpp21rtt',
            '3gpp2umb':'Y_3gpp2umb',
        }, 'Cisco-IOS-XR-ip-mobileip-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg']),
    'MobileIp.Domains.Domain.Mags.Mag' : {
        'meta_info' : _MetaInfoClass('MobileIp.Domains.Domain.Mags.Mag',
            False, 
            [
            _MetaInfoClassMember('mag-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                MAG Identifier
                ''',
                'mag_name',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mag',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Domains.Domain.Mags' : {
        'meta_info' : _MetaInfoClass('MobileIp.Domains.Domain.Mags',
            False, 
            [
            _MetaInfoClassMember('mag', REFERENCE_LIST, 'Mag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Domains.Domain.Mags.Mag', 
                [], [], 
                '''                MAG within domain
                ''',
                'mag',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mags',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Domains.Domain.Nais.Nai' : {
        'meta_info' : _MetaInfoClass('MobileIp.Domains.Domain.Nais.Nai',
            False, 
            [
            _MetaInfoClassMember('nai-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                MN Identifier
                ''',
                'nai_name',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('apn', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                Access point network for this MN
                ''',
                'apn',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('customer', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                Customer name for this MN
                ''',
                'customer',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('lma', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                LMA for this MN
                ''',
                'lma',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('network', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                Network name (Address pool) for this MN
                ''',
                'network',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('service', REFERENCE_ENUM_CLASS, 'ServiceTypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'ServiceTypeEnum', 
                [], [], 
                '''                Service type for this MN
                ''',
                'service',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'nai',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Domains.Domain.Nais' : {
        'meta_info' : _MetaInfoClass('MobileIp.Domains.Domain.Nais',
            False, 
            [
            _MetaInfoClassMember('nai', REFERENCE_LIST, 'Nai' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Domains.Domain.Nais.Nai', 
                [], [], 
                '''                Network access identifier or Realm
                ''',
                'nai',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'nais',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Domains.Domain.AuthenticateOption' : {
        'meta_info' : _MetaInfoClass('MobileIp.Domains.Domain.AuthenticateOption',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                ASCII string
                ''',
                'key',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                SPI in hex value
                ''',
                'spi',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'authenticate-option',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Domains.Domain.Lmas.Lma' : {
        'meta_info' : _MetaInfoClass('MobileIp.Domains.Domain.Lmas.Lma',
            False, 
            [
            _MetaInfoClassMember('lma-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                LMA Identifier
                ''',
                'lma_name',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'lma',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Domains.Domain.Lmas' : {
        'meta_info' : _MetaInfoClass('MobileIp.Domains.Domain.Lmas',
            False, 
            [
            _MetaInfoClassMember('lma', REFERENCE_LIST, 'Lma' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Domains.Domain.Lmas.Lma', 
                [], [], 
                '''                LMA within domain
                ''',
                'lma',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'lmas',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Domains.Domain' : {
        'meta_info' : _MetaInfoClass('MobileIp.Domains.Domain',
            False, 
            [
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                Domain Name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('authenticate-option', REFERENCE_CLASS, 'AuthenticateOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Domains.Domain.AuthenticateOption', 
                [], [], 
                '''                Authentication option between PMIPV6 entities
                ''',
                'authenticate_option',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable PMIPv6 domain configuration. Deletion
                of this object also causes deletion of all
                associated objects under Domain.
                ''',
                'enable',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('lmas', REFERENCE_CLASS, 'Lmas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Domains.Domain.Lmas', 
                [], [], 
                '''                Table of LMA
                ''',
                'lmas',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mags', REFERENCE_CLASS, 'Mags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Domains.Domain.Mags', 
                [], [], 
                '''                Table of MAG
                ''',
                'mags',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('nais', REFERENCE_CLASS, 'Nais' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Domains.Domain.Nais', 
                [], [], 
                '''                Table of NAI
                ''',
                'nais',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'domain',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Domains' : {
        'meta_info' : _MetaInfoClass('MobileIp.Domains',
            False, 
            [
            _MetaInfoClassMember('domain', REFERENCE_LIST, 'Domain' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Domains.Domain', 
                [], [], 
                '''                PMIPv6 domain configuration
                ''',
                'domain',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'domains',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay',
            False, 
            [
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('500', '65535')], [], 
                '''                Maximum time delay to send BRI
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('500', '65535')], [], 
                '''                Minimum time delay to send BRI
                ''',
                'minimum',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'delay',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.BindingRevocationAttributes' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.BindingRevocationAttributes',
            False, 
            [
            _MetaInfoClassMember('delay', REFERENCE_CLASS, 'Delay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay', 
                [], [], 
                '''                Time to wait before Retransmitting BRI
                Message
                ''',
                'delay',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('retry', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Number of Retransmissons Allowed for BRI
                Message
                ''',
                'retry',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'binding-revocation-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.RatAttributes' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.RatAttributes',
            False, 
            [
            _MetaInfoClassMember('lma-rat', REFERENCE_ENUM_CLASS, 'LmaRatEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'LmaRatEnum', 
                [], [], 
                '''                LMA rat type
                ''',
                'lma_rat',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('priority-value', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Specify the priority value
                ''',
                'priority_value',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'rat-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.HeartBeatAttributes' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.HeartBeatAttributes',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('10', '3600')], [], 
                '''                Specify the interval value in second
                ''',
                'interval',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('retries', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Specify the retry value
                ''',
                'retries',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Specify the timeout value
                ''',
                'timeout',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'heart-beat-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                LMA IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'lmaipv6-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Lmaipv6Addresses' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Lmaipv6Addresses',
            False, 
            [
            _MetaInfoClassMember('lmaipv6-address', REFERENCE_LIST, 'Lmaipv6Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address', 
                [], [], 
                '''                Configure IPv6 address for this LMA
                ''',
                'lmaipv6_address',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'lmaipv6-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Hnp' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Hnp',
            False, 
            [
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                maximum HNPs allowed per MN interface
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'hnp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Redistribute' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Redistribute',
            False, 
            [
            _MetaInfoClassMember('redist-sub-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'redist_sub_type',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('redist-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'redist_type',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'redistribute',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Dscp' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Dscp',
            False, 
            [
            _MetaInfoClassMember('force', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'force',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('1', '63')], [], 
                '''                Specify the DSCP value
                ''',
                'value',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'dscp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LMA IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'lmaipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Lmaipv4Addresses' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Lmaipv4Addresses',
            False, 
            [
            _MetaInfoClassMember('lmaipv4-address', REFERENCE_LIST, 'Lmaipv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address', 
                [], [], 
                '''                Configure IPv4 address for this LMA
                ''',
                'lmaipv4_address',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'lmaipv4-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Roles.Role' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Roles.Role',
            False, 
            [
            _MetaInfoClassMember('lma-role', REFERENCE_ENUM_CLASS, 'LmaRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'LmaRoleEnum', 
                [], [], 
                '''                LMA role mode
                ''',
                'lma_role',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'role',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Roles' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Roles',
            False, 
            [
            _MetaInfoClassMember('role', REFERENCE_LIST, 'Role' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Roles.Role', 
                [], [], 
                '''                Role of this LMA
                ''',
                'role',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'roles',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.BindingAttributes' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.BindingAttributes',
            False, 
            [
            _MetaInfoClassMember('create-wait-interval', ATTRIBUTE, 'int' , None, None, 
                [('100', '65535')], [], 
                '''                bce create wait time interval
                ''',
                'create_wait_interval',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('delete-wait-interval', ATTRIBUTE, 'int' , None, None, 
                [('100', '65535')], [], 
                '''                bce delete wait time interval
                ''',
                'delete_wait_interval',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('max-life-time', ATTRIBUTE, 'int' , None, None, 
                [('10', '65535')], [], 
                '''                Maximum bce lifetime permitted
                ''',
                'max_life_time',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('1', '128000')], [], 
                '''                Specify max. number of bindings
                ''',
                'maximum',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('refresh-time', ATTRIBUTE, 'int' , None, None, 
                [('4', '65000')], [], 
                '''                Specify in seconds, (multiples of 4)
                ''',
                'refresh_time',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'binding-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Aaa' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Aaa',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'enable',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('interim-interval', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'interim_interval',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'aaa',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                ASCII string
                ''',
                'key',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                SPI in hex value
                ''',
                'spi',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'authenticate-option',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Mags.Mag.Dscp' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Mags.Mag.Dscp',
            False, 
            [
            _MetaInfoClassMember('force', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'force',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('1', '63')], [], 
                '''                Specify the DSCP value
                ''',
                'value',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'dscp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Mags.Mag' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Mags.Mag',
            False, 
            [
            _MetaInfoClassMember('mag-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                MAG identifier
                ''',
                'mag_name',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('authenticate-option', REFERENCE_CLASS, 'AuthenticateOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption', 
                [], [], 
                '''                Authentication option between PMIPV6
                entities
                ''',
                'authenticate_option',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('dscp', REFERENCE_CLASS, 'Dscp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Mags.Mag.Dscp', 
                [], [], 
                '''                DSCP for packets originating from this MAG
                ''',
                'dscp',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('encap-option', REFERENCE_ENUM_CLASS, 'EncapOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'EncapOptEnum', 
                [], [], 
                '''                Encapsulation option between PMIPV6 entities
                ''',
                'encap_option',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configure IPv4 address for this MAG
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Configure IPv6 address for this MAG
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('tunnel', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                static tunnel for this peer MAG
                ''',
                'tunnel',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mag',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Mags' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Mags',
            False, 
            [
            _MetaInfoClassMember('mag', REFERENCE_LIST, 'Mag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Mags.Mag', 
                [], [], 
                '''                MAG within LMA
                ''',
                'mag',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mags',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.TunnelAttributes' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.TunnelAttributes',
            False, 
            [
            _MetaInfoClassMember('acl', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                access list to apply for tunnel
                ''',
                'acl',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('68', '17916')], [], 
                '''                maximum transmission unit for tunnel
                ''',
                'mtu',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'tunnel-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                ASCII string
                ''',
                'key',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                SPI in hex value
                ''',
                'spi',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'authenticate-option',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('10', '3600')], [], 
                '''                Specify the interval value in second
                ''',
                'interval',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('retries', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Specify the retry value
                ''',
                'retries',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Specify the timeout value
                ''',
                'timeout',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'heart-beat-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configure IPv4 address for this LMA
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Configure IPv6 address for this LMA
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'transport',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports',
            False, 
            [
            _MetaInfoClassMember('transport', REFERENCE_LIST, 'Transport' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport', 
                [], [], 
                '''                Customer transport attributes
                ''',
                'transport',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'transports',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool',
            False, 
            [
            _MetaInfoClassMember('pool-prefix', ATTRIBUTE, 'int' , None, None, 
                [('8', '30')], [], 
                '''                IPv4 Pool Prefix value
                ''',
                'pool_prefix',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Pool IPv4 start address
                ''',
                'start_address',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'ipv4-pool',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool',
            False, 
            [
            _MetaInfoClassMember('pool-prefix', ATTRIBUTE, 'int' , None, None, 
                [('8', '62')], [], 
                '''                IPv6 Pool Prefix value
                ''',
                'pool_prefix',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Pool IPv6 start address
                ''',
                'start_address',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'ipv6-pool',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode',
            False, 
            [
            _MetaInfoClassMember('ipv4-pool', REFERENCE_CLASS, 'Ipv4Pool' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool', 
                [], [], 
                '''                None
                ''',
                'ipv4_pool',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('ipv6-pool', REFERENCE_CLASS, 'Ipv6Pool' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool', 
                [], [], 
                '''                None
                ''',
                'ipv6_pool',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mobile-node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool',
            False, 
            [
            _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Pool IPv4 start address
                ''',
                'start_address',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('network-prefix', ATTRIBUTE, 'int' , None, None, 
                [('8', '32')], [], 
                '''                IPv4 Network Prefix value
                ''',
                'network_prefix',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('pool-prefix', ATTRIBUTE, 'int' , None, None, 
                [('8', '30')], [], 
                '''                IPv4 Pool Prefix value
                ''',
                'pool_prefix',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mripv4-pool',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools',
            False, 
            [
            _MetaInfoClassMember('mripv4-pool', REFERENCE_LIST, 'Mripv4Pool' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool', 
                [], [], 
                '''                ipv4 pool
                ''',
                'mripv4_pool',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mripv4-pools',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool',
            False, 
            [
            _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Pool IPv6 start address
                ''',
                'start_address',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('network-prefix', ATTRIBUTE, 'int' , None, None, 
                [('8', '64')], [], 
                '''                IPv4 Network Prefix value
                ''',
                'network_prefix',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('pool-prefix', ATTRIBUTE, 'int' , None, None, 
                [('8', '64')], [], 
                '''                IPv6 Pool Prefix value
                ''',
                'pool_prefix',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mripv6-pool',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools',
            False, 
            [
            _MetaInfoClassMember('mripv6-pool', REFERENCE_LIST, 'Mripv6Pool' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool', 
                [], [], 
                '''                ipv6 pool
                ''',
                'mripv6_pool',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mripv6-pools',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork',
            False, 
            [
            _MetaInfoClassMember('mripv4-pools', REFERENCE_CLASS, 'Mripv4Pools' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools', 
                [], [], 
                '''                Table of MRIPV4Pool
                ''',
                'mripv4_pools',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mripv6-pools', REFERENCE_CLASS, 'Mripv6Pools' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools', 
                [], [], 
                '''                Table of MRIPV6Pool
                ''',
                'mripv6_pools',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mobile-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes',
            False, 
            [
            _MetaInfoClassMember('mobile-network', REFERENCE_CLASS, 'MobileNetwork' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork', 
                [], [], 
                '''                pool configs for the mobile network
                ''',
                'mobile_network',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mobile-node', REFERENCE_CLASS, 'MobileNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode', 
                [], [], 
                '''                pool configs for the mobile nodes
                ''',
                'mobile_node',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'pool-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                ASCII string
                ''',
                'name',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('pool-attributes', REFERENCE_CLASS, 'PoolAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes', 
                [], [], 
                '''                Pool configs for this network
                ''',
                'pool_attributes',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'authorize',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes',
            False, 
            [
            _MetaInfoClassMember('authorize', REFERENCE_LIST, 'Authorize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize', 
                [], [], 
                '''                not authorize the network prefixes
                ''',
                'authorize',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'authorizes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes',
            False, 
            [
            _MetaInfoClassMember('authorizes', REFERENCE_CLASS, 'Authorizes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes', 
                [], [], 
                '''                Table of Authorize
                ''',
                'authorizes',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('unauthorize', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                not authorize the network prefixes
                ''',
                'unauthorize',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'network-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey',
            False, 
            [
            _MetaInfoClassMember('gre-key-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'gre_key_type',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('gre-key-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                GRE key value
                ''',
                'gre_key_value',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'gre-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes',
            False, 
            [
            _MetaInfoClassMember('max-life-time', ATTRIBUTE, 'int' , None, None, 
                [('10', '65535')], [], 
                '''                Maximum bce lifetime permitted
                ''',
                'max_life_time',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'binding-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers.Customer' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers.Customer',
            False, 
            [
            _MetaInfoClassMember('customer-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                Customer name
                ''',
                'customer_name',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('authenticate-option', REFERENCE_CLASS, 'AuthenticateOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption', 
                [], [], 
                '''                Authentication option between PMIPV6
                entities
                ''',
                'authenticate_option',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('bandwidth-aggregate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Aggregate bandwidth across all logical MNs
                ''',
                'bandwidth_aggregate',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('binding-attributes', REFERENCE_CLASS, 'BindingAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes', 
                [], [], 
                '''                Customer specific binding attributes
                ''',
                'binding_attributes',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('gre-key', REFERENCE_CLASS, 'GreKey' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey', 
                [], [], 
                '''                Customer specific GRE key
                ''',
                'gre_key',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('heart-beat-attributes', REFERENCE_CLASS, 'HeartBeatAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes', 
                [], [], 
                '''                heartbeat config for this Customer
                ''',
                'heart_beat_attributes',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mnp-customer', ATTRIBUTE, 'int' , None, None, 
                [('1', '4000000')], [], 
                '''                mnp limit config for customer
                ''',
                'mnp_customer',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mnp-ipv4-customer', ATTRIBUTE, 'int' , None, None, 
                [('1', '4000000')], [], 
                '''                mnp limit config for customer
                ''',
                'mnp_ipv4_customer',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mnp-ipv4-lmn', ATTRIBUTE, 'int' , None, None, 
                [('1', '32')], [], 
                '''                mnp limit config for customer specific
                logical mn
                ''',
                'mnp_ipv4_lmn',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mnp-ipv6-customer', ATTRIBUTE, 'int' , None, None, 
                [('1', '4000000')], [], 
                '''                mnp limit config for customer
                ''',
                'mnp_ipv6_customer',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mnp-ipv6-lmn', ATTRIBUTE, 'int' , None, None, 
                [('1', '32')], [], 
                '''                mnp limit config for customer specific
                logical mn
                ''',
                'mnp_ipv6_lmn',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mnp-lmn', ATTRIBUTE, 'int' , None, None, 
                [('1', '32')], [], 
                '''                mnp limit config for customer specific
                logical mn
                ''',
                'mnp_lmn',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mobile-route-ad', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Specify the Admin Distance value
                ''',
                'mobile_route_ad',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('network-attributes', REFERENCE_CLASS, 'NetworkAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes', 
                [], [], 
                '''                network parameters for the customer
                ''',
                'network_attributes',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('transports', REFERENCE_CLASS, 'Transports' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports', 
                [], [], 
                '''                Table of Transport
                ''',
                'transports',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'customer',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service.Customers' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service.Customers',
            False, 
            [
            _MetaInfoClassMember('customer', REFERENCE_LIST, 'Customer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers.Customer', 
                [], [], 
                '''                customer configuration on this mobile local
                loop service
                ''',
                'customer',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'customers',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services.Service' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services.Service',
            False, 
            [
            _MetaInfoClassMember('lma-service', REFERENCE_ENUM_CLASS, 'LmaServiceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'LmaServiceEnum', 
                [], [], 
                '''                LMA service mode
                ''',
                'lma_service',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('customers', REFERENCE_CLASS, 'Customers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service.Customers', 
                [], [], 
                '''                Table of Customer
                ''',
                'customers',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('ignore', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ignore options for mobile local loop service
                ''',
                'ignore',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mnp-customer', ATTRIBUTE, 'int' , None, None, 
                [('1', '4000000')], [], 
                '''                mnp limit config for all customer's
                ''',
                'mnp_customer',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mnp-ipv4-customer', ATTRIBUTE, 'int' , None, None, 
                [('1', '4000000')], [], 
                '''                mnp limit config for all customer's
                ''',
                'mnp_ipv4_customer',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mnp-ipv4-lmn', ATTRIBUTE, 'int' , None, None, 
                [('1', '32')], [], 
                '''                mnp limit config for all logical mn's
                ''',
                'mnp_ipv4_lmn',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mnp-ipv6-customer', ATTRIBUTE, 'int' , None, None, 
                [('1', '4000000')], [], 
                '''                mnp limit config for all customer's
                ''',
                'mnp_ipv6_customer',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mnp-ipv6-lmn', ATTRIBUTE, 'int' , None, None, 
                [('1', '32')], [], 
                '''                mnp limit config for all logical mn's
                ''',
                'mnp_ipv6_lmn',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mnp-lmn', ATTRIBUTE, 'int' , None, None, 
                [('1', '32')], [], 
                '''                mnp limit config for all logical mn's
                ''',
                'mnp_lmn',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'service',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Services' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Services',
            False, 
            [
            _MetaInfoClassMember('service', REFERENCE_LIST, 'Service' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services.Service', 
                [], [], 
                '''                Service of this LMA
                ''',
                'service',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'services',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.ReplayProtection' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.ReplayProtection',
            False, 
            [
            _MetaInfoClassMember('ignore', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'ignore',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('validity-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Specify window value in seconds
                ''',
                'validity_window',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'replay-protection',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool',
            False, 
            [
            _MetaInfoClassMember('pool-prefix', ATTRIBUTE, 'int' , None, None, 
                [('8', '30')], [], 
                '''                IPv4 Pool Prefix value
                ''',
                'pool_prefix',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Pool IPv4 start address
                ''',
                'start_address',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'ipv4-pool',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool',
            False, 
            [
            _MetaInfoClassMember('pool-prefix', ATTRIBUTE, 'int' , None, None, 
                [('8', '62')], [], 
                '''                IPv6 Pool Prefix value
                ''',
                'pool_prefix',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Pool IPv6 start address
                ''',
                'start_address',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'ipv6-pool',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode',
            False, 
            [
            _MetaInfoClassMember('ipv4-pool', REFERENCE_CLASS, 'Ipv4Pool' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool', 
                [], [], 
                '''                None
                ''',
                'ipv4_pool',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('ipv6-pool', REFERENCE_CLASS, 'Ipv6Pool' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool', 
                [], [], 
                '''                None
                ''',
                'ipv6_pool',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mobile-node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool',
            False, 
            [
            _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Pool IPv6 start address
                ''',
                'start_address',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('network-prefix', ATTRIBUTE, 'int' , None, None, 
                [('8', '64')], [], 
                '''                IPv4 Network Prefix value
                ''',
                'network_prefix',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('pool-prefix', ATTRIBUTE, 'int' , None, None, 
                [('8', '64')], [], 
                '''                IPv6 Pool Prefix value
                ''',
                'pool_prefix',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mripv6-pool',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools',
            False, 
            [
            _MetaInfoClassMember('mripv6-pool', REFERENCE_LIST, 'Mripv6Pool' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool', 
                [], [], 
                '''                ipv6 pool
                ''',
                'mripv6_pool',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mripv6-pools',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool',
            False, 
            [
            _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Pool IPv4 start address
                ''',
                'start_address',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('network-prefix', ATTRIBUTE, 'int' , None, None, 
                [('8', '32')], [], 
                '''                IPv4 Network Prefix value
                ''',
                'network_prefix',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('pool-prefix', ATTRIBUTE, 'int' , None, None, 
                [('8', '30')], [], 
                '''                IPv4 Pool Prefix value
                ''',
                'pool_prefix',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mripv4-pool',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools',
            False, 
            [
            _MetaInfoClassMember('mripv4-pool', REFERENCE_LIST, 'Mripv4Pool' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool', 
                [], [], 
                '''                ipv4 pool
                ''',
                'mripv4_pool',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mripv4-pools',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork',
            False, 
            [
            _MetaInfoClassMember('mripv4-pools', REFERENCE_CLASS, 'Mripv4Pools' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools', 
                [], [], 
                '''                Table of MRIPV4Pool
                ''',
                'mripv4_pools',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mripv6-pools', REFERENCE_CLASS, 'Mripv6Pools' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools', 
                [], [], 
                '''                Table of MRIPV6Pool
                ''',
                'mripv6_pools',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mobile-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Networks.Network.PoolAttributes',
            False, 
            [
            _MetaInfoClassMember('mobile-network', REFERENCE_CLASS, 'MobileNetwork' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork', 
                [], [], 
                '''                pool configs for the mobile network
                ''',
                'mobile_network',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mobile-node', REFERENCE_CLASS, 'MobileNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode', 
                [], [], 
                '''                pool configs for the mobile nodes
                ''',
                'mobile_node',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'pool-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Networks.Network' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Networks.Network',
            False, 
            [
            _MetaInfoClassMember('lma-network', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                Network name
                ''',
                'lma_network',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('pool-attributes', REFERENCE_CLASS, 'PoolAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Networks.Network.PoolAttributes', 
                [], [], 
                '''                Pool configs for this network
                ''',
                'pool_attributes',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'network',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma.Networks' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma.Networks',
            False, 
            [
            _MetaInfoClassMember('network', REFERENCE_LIST, 'Network' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Networks.Network', 
                [], [], 
                '''                network for this LMA
                ''',
                'network',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'networks',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas.Lma' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas.Lma',
            False, 
            [
            _MetaInfoClassMember('lma-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                LMA name
                ''',
                'lma_name',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ip-mobileip-cfg', True),
            _MetaInfoClassMember('aaa', REFERENCE_CLASS, 'Aaa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Aaa', 
                [], [], 
                '''                aaa config attributes for this LMA
                ''',
                'aaa',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('ani', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                enable ani option processing in LMA
                ''',
                'ani',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('binding-attributes', REFERENCE_CLASS, 'BindingAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.BindingAttributes', 
                [], [], 
                '''                LMA binding attributes
                ''',
                'binding_attributes',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('binding-revocation-attributes', REFERENCE_CLASS, 'BindingRevocationAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.BindingRevocationAttributes', 
                [], [], 
                '''                LMA Binding Revocation Attributes
                ''',
                'binding_revocation_attributes',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('default-profile', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                Default MN profile for LMA
                ''',
                'default_profile',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('dscp', REFERENCE_CLASS, 'Dscp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Dscp', 
                [], [], 
                '''                DSCP for packets originating from this LMA
                ''',
                'dscp',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('dynamic', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                enable dynamic mag learning for LMA
                ''',
                'dynamic',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('enforce', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                enforce heartbeat values to MAG
                ''',
                'enforce',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('generate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                generate gre key for LMA bindings
                ''',
                'generate',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('heart-beat-attributes', REFERENCE_CLASS, 'HeartBeatAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.HeartBeatAttributes', 
                [], [], 
                '''                heartbeat config for this LMA
                ''',
                'heart_beat_attributes',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('hnp', REFERENCE_CLASS, 'Hnp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Hnp', 
                [], [], 
                '''                LMA HNP options
                ''',
                'hnp',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                CN facing interface name
                ''',
                'interface',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('lmaipv4-addresses', REFERENCE_CLASS, 'Lmaipv4Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Lmaipv4Addresses', 
                [], [], 
                '''                Table of LMAIPv4Address
                ''',
                'lmaipv4_addresses',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('lmaipv6-addresses', REFERENCE_CLASS, 'Lmaipv6Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Lmaipv6Addresses', 
                [], [], 
                '''                Table of LMAIPv6Address
                ''',
                'lmaipv6_addresses',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mags', REFERENCE_CLASS, 'Mags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Mags', 
                [], [], 
                '''                Table of MAG
                ''',
                'mags',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mobile-map', ATTRIBUTE, 'str' , None, None, 
                [(1, 125)], [], 
                '''                Mobile Map for this LMA
                ''',
                'mobile_map',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('mobile-route-ad', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Specify the Admin Distance value
                ''',
                'mobile_route_ad',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('multipath', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                enable multipath support for LMA
                ''',
                'multipath',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('networks', REFERENCE_CLASS, 'Networks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Networks', 
                [], [], 
                '''                Table of Network
                ''',
                'networks',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('pgw-subs-cont', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Feature related to interface with PGW
                ''',
                'pgw_subs_cont',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('rat-attributes', REFERENCE_CLASS, 'RatAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.RatAttributes', 
                [], [], 
                '''                Radio access technology type config  this LMA
                ''',
                'rat_attributes',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('redistribute', REFERENCE_CLASS, 'Redistribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Redistribute', 
                [], [], 
                '''                Redistribute routes
                ''',
                'redistribute',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('replay-protection', REFERENCE_CLASS, 'ReplayProtection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.ReplayProtection', 
                [], [], 
                '''                Replay Protection Method
                ''',
                'replay_protection',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('roles', REFERENCE_CLASS, 'Roles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Roles', 
                [], [], 
                '''                Table of Role
                ''',
                'roles',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('services', REFERENCE_CLASS, 'Services' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.Services', 
                [], [], 
                '''                Table of Service
                ''',
                'services',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('tunnel-attributes', REFERENCE_CLASS, 'TunnelAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma.TunnelAttributes', 
                [], [], 
                '''                tunnel attributes
                ''',
                'tunnel_attributes',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'lma',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp.Lmas' : {
        'meta_info' : _MetaInfoClass('MobileIp.Lmas',
            False, 
            [
            _MetaInfoClassMember('lma', REFERENCE_LIST, 'Lma' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas.Lma', 
                [], [], 
                '''                PMIPv6 LMA configuration
                ''',
                'lma',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'lmas',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
    'MobileIp' : {
        'meta_info' : _MetaInfoClass('MobileIp',
            False, 
            [
            _MetaInfoClassMember('domains', REFERENCE_CLASS, 'Domains' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Domains', 
                [], [], 
                '''                Table of Domain
                ''',
                'domains',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            _MetaInfoClassMember('lmas', REFERENCE_CLASS, 'Lmas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg', 'MobileIp.Lmas', 
                [], [], 
                '''                Table of LMA
                ''',
                'lmas',
                'Cisco-IOS-XR-ip-mobileip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-mobileip-cfg',
            'mobile-ip',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-mobileip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg'
        ),
    },
}
_meta_table['MobileIp.Domains.Domain.Mags.Mag']['meta_info'].parent =_meta_table['MobileIp.Domains.Domain.Mags']['meta_info']
_meta_table['MobileIp.Domains.Domain.Nais.Nai']['meta_info'].parent =_meta_table['MobileIp.Domains.Domain.Nais']['meta_info']
_meta_table['MobileIp.Domains.Domain.Lmas.Lma']['meta_info'].parent =_meta_table['MobileIp.Domains.Domain.Lmas']['meta_info']
_meta_table['MobileIp.Domains.Domain.Mags']['meta_info'].parent =_meta_table['MobileIp.Domains.Domain']['meta_info']
_meta_table['MobileIp.Domains.Domain.Nais']['meta_info'].parent =_meta_table['MobileIp.Domains.Domain']['meta_info']
_meta_table['MobileIp.Domains.Domain.AuthenticateOption']['meta_info'].parent =_meta_table['MobileIp.Domains.Domain']['meta_info']
_meta_table['MobileIp.Domains.Domain.Lmas']['meta_info'].parent =_meta_table['MobileIp.Domains.Domain']['meta_info']
_meta_table['MobileIp.Domains.Domain']['meta_info'].parent =_meta_table['MobileIp.Domains']['meta_info']
_meta_table['MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.BindingRevocationAttributes']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Lmaipv6Addresses']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Lmaipv4Addresses']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Roles.Role']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Roles']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Mags.Mag']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Mags.Mag.Dscp']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Mags.Mag']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Mags.Mag']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Mags']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers.Customer']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service.Customers']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services.Service']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services.Service']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Services']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Networks.Network.PoolAttributes']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Networks.Network']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Networks.Network']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma.Networks']['meta_info']
_meta_table['MobileIp.Lmas.Lma.BindingRevocationAttributes']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.RatAttributes']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.HeartBeatAttributes']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Lmaipv6Addresses']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Hnp']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Redistribute']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Dscp']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Lmaipv4Addresses']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Roles']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.BindingAttributes']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Aaa']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Mags']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.TunnelAttributes']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Services']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.ReplayProtection']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma.Networks']['meta_info'].parent =_meta_table['MobileIp.Lmas.Lma']['meta_info']
_meta_table['MobileIp.Lmas.Lma']['meta_info'].parent =_meta_table['MobileIp.Lmas']['meta_info']
_meta_table['MobileIp.Domains']['meta_info'].parent =_meta_table['MobileIp']['meta_info']
_meta_table['MobileIp.Lmas']['meta_info'].parent =_meta_table['MobileIp']['meta_info']
