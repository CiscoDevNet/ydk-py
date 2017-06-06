


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'RipAuthModeEnum' : _MetaInfoEnum('RipAuthModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg',
        {
            'text':'text',
            'md5':'md5',
        }, 'Cisco-IOS-XR-ip-rip-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg']),
    'RipExtCommunityEnum' : _MetaInfoEnum('RipExtCommunityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg',
        {
            'as':'as_',
            'ipv4-address':'ipv4_address',
            'four-byte-as':'four_byte_as',
        }, 'Cisco-IOS-XR-ip-rip-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg']),
    'DefaultRedistRouteEnum' : _MetaInfoEnum('DefaultRedistRouteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg',
        {
            'all':'all',
        }, 'Cisco-IOS-XR-ip-rip-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg']),
    'IsisRedistRouteEnum' : _MetaInfoEnum('IsisRedistRouteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg',
        {
            'level1':'level1',
            'level2':'level2',
            'level1-and2':'level1_and2',
        }, 'Cisco-IOS-XR-ip-rip-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg']),
    'BgpRedistRouteEnum' : _MetaInfoEnum('BgpRedistRouteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg',
        {
            'all':'all',
            'internal':'internal',
            'external':'external',
            'local':'local',
        }, 'Cisco-IOS-XR-ip-rip-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg']),
    'DefaultInformationOptionEnum' : _MetaInfoEnum('DefaultInformationOptionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg',
        {
            'always':'always',
            'policy':'policy',
        }, 'Cisco-IOS-XR-ip-rip-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg']),
    'Rip.DefaultVrf.DefaultInformation' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.DefaultInformation',
            False, 
            [
            _MetaInfoClassMember('option', REFERENCE_ENUM_CLASS, 'DefaultInformationOptionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultInformationOptionEnum', 
                [], [], 
                '''                Origination option
                ''',
                'option',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'default-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Redistribution.Connected' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Redistribution.Connected',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'DefaultRedistRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultRedistRouteEnum', 
                [], [], 
                '''                Route type
                ''',
                'route_type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'connected',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Redistribution.Bgps.Bgp' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Redistribution.Bgps.Bgp',
            False, 
            [
            _MetaInfoClassMember('asnxx', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Higher 16 bits of 4-byte BGP AS number
                ''',
                'asnxx',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('asnyy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                2-byte or 4-byte BGP AS number
                ''',
                'asnyy',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'policy',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpRedistRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'BgpRedistRouteEnum', 
                [], [], 
                '''                Route type
                ''',
                'type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Redistribution.Bgps' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Redistribution.Bgps',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_LIST, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Redistribution.Bgps.Bgp', 
                [], [], 
                '''                Autonomous system number
                ''',
                'bgp',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'bgps',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Redistribution.Isises.Isis' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Redistribution.Isises.Isis',
            False, 
            [
            _MetaInfoClassMember('isis-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IS-IS instance name
                ''',
                'isis_name',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'IsisRedistRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'IsisRedistRouteEnum', 
                [], [], 
                '''                Route type
                ''',
                'route_type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Redistribution.Isises' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Redistribution.Isises',
            False, 
            [
            _MetaInfoClassMember('isis', REFERENCE_LIST, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Redistribution.Isises.Isis', 
                [], [], 
                '''                Redistribute IS-IS routes
                ''',
                'isis',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'isises',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Redistribution.EigrpS.Eigrp' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Redistribution.EigrpS.Eigrp',
            False, 
            [
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Autonomous system number
                ''',
                'as_',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'DefaultRedistRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultRedistRouteEnum', 
                [], [], 
                '''                Route type
                ''',
                'route_type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'eigrp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Redistribution.EigrpS' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Redistribution.EigrpS',
            False, 
            [
            _MetaInfoClassMember('eigrp', REFERENCE_LIST, 'Eigrp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Redistribution.EigrpS.Eigrp', 
                [], [], 
                '''                Redistribute EIGRP routes
                ''',
                'eigrp',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'eigrp-s',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Redistribution.Static' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Redistribution.Static',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'DefaultRedistRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultRedistRouteEnum', 
                [], [], 
                '''                Route type
                ''',
                'route_type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'static',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Redistribution.Ospfs.Ospf' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Redistribution.Ospfs.Ospf',
            False, 
            [
            _MetaInfoClassMember('ospf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Process ID for the OSPF instance
                ''',
                'ospf_name',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('external', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                External routes
                ''',
                'external',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('external-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                External route type
                ''',
                'external_type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('internal', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Internal routes
                ''',
                'internal',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('nssa-external', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                NSSA External routes
                ''',
                'nssa_external',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('nssa-external-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                NSSA External route type
                ''',
                'nssa_external_type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Redistribution.Ospfs' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Redistribution.Ospfs',
            False, 
            [
            _MetaInfoClassMember('ospf', REFERENCE_LIST, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Redistribution.Ospfs.Ospf', 
                [], [], 
                '''                Redistribute OSPF routes
                ''',
                'ospf',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'ospfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Redistribution' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Redistribution',
            False, 
            [
            _MetaInfoClassMember('bgps', REFERENCE_CLASS, 'Bgps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Redistribution.Bgps', 
                [], [], 
                '''                Redistribute BGP routes
                ''',
                'bgps',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('connected', REFERENCE_CLASS, 'Connected' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Redistribution.Connected', 
                [], [], 
                '''                Redistribute connected routes
                ''',
                'connected',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('eigrp-s', REFERENCE_CLASS, 'EigrpS' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Redistribution.EigrpS', 
                [], [], 
                '''                Redistribute EIGRP routes
                ''',
                'eigrp_s',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('isises', REFERENCE_CLASS, 'Isises' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Redistribution.Isises', 
                [], [], 
                '''                Redistribute IS-IS routes
                ''',
                'isises',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('ospfs', REFERENCE_CLASS, 'Ospfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Redistribution.Ospfs', 
                [], [], 
                '''                Redistribute OSPF routes
                ''',
                'ospfs',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('static', REFERENCE_CLASS, 'Static' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Redistribution.Static', 
                [], [], 
                '''                Redistribute static routes
                ''',
                'static',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'redistribution',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.IpDistances.IpDistance' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.IpDistances.IpDistance',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP Source address
                ''',
                'address',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address mask
                ''',
                'netmask',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('distance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'ip-distance',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.IpDistances' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.IpDistances',
            False, 
            [
            _MetaInfoClassMember('ip-distance', REFERENCE_LIST, 'IpDistance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.IpDistances.IpDistance', 
                [], [], 
                '''                IP specific administrative distance
                ''',
                'ip_distance',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'ip-distances',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Interfaces.Interface.Authentication' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Interfaces.Interface.Authentication',
            False, 
            [
            _MetaInfoClassMember('keychain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of keychain
                ''',
                'keychain',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'RipAuthModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'RipAuthModeEnum', 
                [], [], 
                '''                Authentication mode
                ''',
                'mode',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 address for IPV4Address:nn format
                ''',
                'address',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('address-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                16bit value for IPV4Address:nn format
                ''',
                'address_index',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS Number Index
                ''',
                'as_index',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AS Number for AS:nn format
                ''',
                'as_xx',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit value for AS:nn format
                ''',
                'as_yy',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'RipExtCommunityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'RipExtCommunityEnum', 
                [], [], 
                '''                Extended community type
                ''',
                'type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'site-of-origin',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion',
            False, 
            [
            _MetaInfoClassMember('version1', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Support RIP version 1
                ''',
                'version1',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('version2', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Support RIP version 2
                ''',
                'version2',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'receive-version',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Interfaces.Interface.SendVersion' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Interfaces.Interface.SendVersion',
            False, 
            [
            _MetaInfoClassMember('version1', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Support RIP version 1
                ''',
                'version1',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('version2', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Support RIP version 2
                ''',
                'version2',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'send-version',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('accept-metric-zero', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Accept RIP updates with metric 0
                ''',
                'accept_metric_zero',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Interfaces.Interface.Authentication', 
                [], [], 
                '''                Authentication keychain and mode
                ''',
                'authentication',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('broadcast-for-v2', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Send RIP v2 output packets to broadcast
                address
                ''',
                'broadcast_for_v2',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Starts RIP interface configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress routing updates on this interface
                ''',
                'passive',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('poison-reverse', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable poison reverse
                ''',
                'poison_reverse',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy for inbound routing updates
                ''',
                'policy_in',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('policy-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy for outbound routing updates
                ''',
                'policy_out',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('receive-version', REFERENCE_CLASS, 'ReceiveVersion' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion', 
                [], [], 
                '''                RIP versions supported for receiving
                advertisements
                ''',
                'receive_version',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('send-version', REFERENCE_CLASS, 'SendVersion' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Interfaces.Interface.SendVersion', 
                [], [], 
                '''                RIP versions supported for sending
                advertisements
                ''',
                'send_version',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('site-of-origin', REFERENCE_CLASS, 'SiteOfOrigin' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin', 
                [], [], 
                '''                SOO community for prefixes learned over this
                interface
                ''',
                'site_of_origin',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('split-horizon-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable split horizon
                ''',
                'split_horizon_disable',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Interfaces' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Interfaces.Interface', 
                [], [], 
                '''                RIP interface name
                ''',
                'interface',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Neighbors' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Neighbors.Neighbor', 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf.Timers' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Timers',
            False, 
            [
            _MetaInfoClassMember('flush-timer', ATTRIBUTE, 'int' , None, None, 
                [('16', '250000')], [], 
                '''                Flush
                ''',
                'flush_timer',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('holddown-timer', ATTRIBUTE, 'int' , None, None, 
                [('15', '200000')], [], 
                '''                Holddown
                ''',
                'holddown_timer',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('invalid-timer', ATTRIBUTE, 'int' , None, None, 
                [('15', '200000')], [], 
                '''                Invalid
                ''',
                'invalid_timer',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('update-timer', ATTRIBUTE, 'int' , None, None, 
                [('5', '50000')], [], 
                '''                Interval between updates
                ''',
                'update_timer',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.DefaultVrf' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf',
            False, 
            [
            _MetaInfoClassMember('auto-summary', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable automatic network number summarization
                ''',
                'auto_summary',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('broadcast-for-v2', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Send RIP v2 output packets to broadcast address
                ''',
                'broadcast_for_v2',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('default-information', REFERENCE_CLASS, 'DefaultInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.DefaultInformation', 
                [], [], 
                '''                Controls default information origination
                ''',
                'default_information',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16')], [], 
                '''                Default metric of redistributed routes
                ''',
                'default_metric',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('distance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Starts RIP configuration for Default VRF
                ''',
                'enable',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Interfaces', 
                [], [], 
                '''                Table of RIP interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('ip-distances', REFERENCE_CLASS, 'IpDistances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.IpDistances', 
                [], [], 
                '''                Table of IP specific administrative distances
                ''',
                'ip_distances',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('1', '128')], [], 
                '''                Maximum number of paths allowed per route
                ''',
                'maximum_paths',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Neighbors', 
                [], [], 
                '''                Configure RIP Neighbors
                ''',
                'neighbors',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('nsf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Cisco Non Stop Forwarding
                ''',
                'nsf',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('output-delay', ATTRIBUTE, 'int' , None, None, 
                [('8', '50')], [], 
                '''                Inter-packet delay for RIP updates
                ''',
                'output_delay',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy for inbbound routing updates
                ''',
                'policy_in',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('policy-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy for outbound routing updates
                ''',
                'policy_out',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('redistribution', REFERENCE_CLASS, 'Redistribution' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Redistribution', 
                [], [], 
                '''                Redistribute information from another routing
                protocol
                ''',
                'redistribution',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf.Timers', 
                [], [], 
                '''                Various routing timers
                ''',
                'timers',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('validate-source-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable validation of source address of routing
                updates
                ''',
                'validate_source_disable',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'default-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.DefaultInformation' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.DefaultInformation',
            False, 
            [
            _MetaInfoClassMember('option', REFERENCE_ENUM_CLASS, 'DefaultInformationOptionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultInformationOptionEnum', 
                [], [], 
                '''                Origination option
                ''',
                'option',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'default-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Redistribution.Connected' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Redistribution.Connected',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'DefaultRedistRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultRedistRouteEnum', 
                [], [], 
                '''                Route type
                ''',
                'route_type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'connected',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp',
            False, 
            [
            _MetaInfoClassMember('asnxx', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Higher 16 bits of 4-byte BGP AS number
                ''',
                'asnxx',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('asnyy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                2-byte or 4-byte BGP AS number
                ''',
                'asnyy',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'policy',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpRedistRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'BgpRedistRouteEnum', 
                [], [], 
                '''                Route type
                ''',
                'type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Redistribution.Bgps' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Redistribution.Bgps',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_LIST, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp', 
                [], [], 
                '''                Autonomous system number
                ''',
                'bgp',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'bgps',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Redistribution.Isises.Isis' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Redistribution.Isises.Isis',
            False, 
            [
            _MetaInfoClassMember('isis-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IS-IS instance name
                ''',
                'isis_name',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'IsisRedistRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'IsisRedistRouteEnum', 
                [], [], 
                '''                Route type
                ''',
                'route_type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Redistribution.Isises' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Redistribution.Isises',
            False, 
            [
            _MetaInfoClassMember('isis', REFERENCE_LIST, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Redistribution.Isises.Isis', 
                [], [], 
                '''                Redistribute IS-IS routes
                ''',
                'isis',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'isises',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp',
            False, 
            [
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Autonomous system number
                ''',
                'as_',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'DefaultRedistRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultRedistRouteEnum', 
                [], [], 
                '''                Route type
                ''',
                'route_type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'eigrp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Redistribution.EigrpS' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Redistribution.EigrpS',
            False, 
            [
            _MetaInfoClassMember('eigrp', REFERENCE_LIST, 'Eigrp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp', 
                [], [], 
                '''                Redistribute EIGRP routes
                ''',
                'eigrp',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'eigrp-s',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Redistribution.Static' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Redistribution.Static',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'DefaultRedistRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'DefaultRedistRouteEnum', 
                [], [], 
                '''                Route type
                ''',
                'route_type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'static',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf',
            False, 
            [
            _MetaInfoClassMember('ospf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Process ID for the OSPF instance
                ''',
                'ospf_name',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('external', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                External routes
                ''',
                'external',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('external-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                External route type
                ''',
                'external_type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('internal', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Internal routes
                ''',
                'internal',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('nssa-external', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                NSSA External routes
                ''',
                'nssa_external',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('nssa-external-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                NSSA External route type
                ''',
                'nssa_external_type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Redistribution.Ospfs' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Redistribution.Ospfs',
            False, 
            [
            _MetaInfoClassMember('ospf', REFERENCE_LIST, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf', 
                [], [], 
                '''                Redistribute OSPF routes
                ''',
                'ospf',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'ospfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Redistribution' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Redistribution',
            False, 
            [
            _MetaInfoClassMember('bgps', REFERENCE_CLASS, 'Bgps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Redistribution.Bgps', 
                [], [], 
                '''                Redistribute BGP routes
                ''',
                'bgps',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('connected', REFERENCE_CLASS, 'Connected' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Redistribution.Connected', 
                [], [], 
                '''                Redistribute connected routes
                ''',
                'connected',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('eigrp-s', REFERENCE_CLASS, 'EigrpS' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Redistribution.EigrpS', 
                [], [], 
                '''                Redistribute EIGRP routes
                ''',
                'eigrp_s',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('isises', REFERENCE_CLASS, 'Isises' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Redistribution.Isises', 
                [], [], 
                '''                Redistribute IS-IS routes
                ''',
                'isises',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('ospfs', REFERENCE_CLASS, 'Ospfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Redistribution.Ospfs', 
                [], [], 
                '''                Redistribute OSPF routes
                ''',
                'ospfs',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('static', REFERENCE_CLASS, 'Static' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Redistribution.Static', 
                [], [], 
                '''                Redistribute static routes
                ''',
                'static',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'redistribution',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.IpDistances.IpDistance' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.IpDistances.IpDistance',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP Source address
                ''',
                'address',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address mask
                ''',
                'netmask',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('distance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'ip-distance',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.IpDistances' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.IpDistances',
            False, 
            [
            _MetaInfoClassMember('ip-distance', REFERENCE_LIST, 'IpDistance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.IpDistances.IpDistance', 
                [], [], 
                '''                IP specific administrative distance
                ''',
                'ip_distance',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'ip-distances',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Interfaces.Interface.Authentication' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Interfaces.Interface.Authentication',
            False, 
            [
            _MetaInfoClassMember('keychain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of keychain
                ''',
                'keychain',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'RipAuthModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'RipAuthModeEnum', 
                [], [], 
                '''                Authentication mode
                ''',
                'mode',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 address for IPV4Address:nn format
                ''',
                'address',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('address-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                16bit value for IPV4Address:nn format
                ''',
                'address_index',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS Number Index
                ''',
                'as_index',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AS Number for AS:nn format
                ''',
                'as_xx',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit value for AS:nn format
                ''',
                'as_yy',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'RipExtCommunityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'RipExtCommunityEnum', 
                [], [], 
                '''                Extended community type
                ''',
                'type',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'site-of-origin',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion',
            False, 
            [
            _MetaInfoClassMember('version1', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Support RIP version 1
                ''',
                'version1',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('version2', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Support RIP version 2
                ''',
                'version2',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'receive-version',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion',
            False, 
            [
            _MetaInfoClassMember('version1', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Support RIP version 1
                ''',
                'version1',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('version2', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Support RIP version 2
                ''',
                'version2',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'send-version',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('accept-metric-zero', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Accept RIP updates with metric 0
                ''',
                'accept_metric_zero',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Interfaces.Interface.Authentication', 
                [], [], 
                '''                Authentication keychain and mode
                ''',
                'authentication',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('broadcast-for-v2', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Send RIP v2 output packets to broadcast
                address
                ''',
                'broadcast_for_v2',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Starts RIP interface configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress routing updates on this interface
                ''',
                'passive',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('poison-reverse', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable poison reverse
                ''',
                'poison_reverse',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy for inbound routing updates
                ''',
                'policy_in',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('policy-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy for outbound routing updates
                ''',
                'policy_out',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('receive-version', REFERENCE_CLASS, 'ReceiveVersion' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion', 
                [], [], 
                '''                RIP versions supported for receiving
                advertisements
                ''',
                'receive_version',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('send-version', REFERENCE_CLASS, 'SendVersion' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion', 
                [], [], 
                '''                RIP versions supported for sending
                advertisements
                ''',
                'send_version',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('site-of-origin', REFERENCE_CLASS, 'SiteOfOrigin' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin', 
                [], [], 
                '''                SOO community for prefixes learned over this
                interface
                ''',
                'site_of_origin',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('split-horizon-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable split horizon
                ''',
                'split_horizon_disable',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Interfaces' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Interfaces.Interface', 
                [], [], 
                '''                RIP interface name
                ''',
                'interface',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Neighbors' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Neighbors.Neighbor', 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf.Timers' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Timers',
            False, 
            [
            _MetaInfoClassMember('flush-timer', ATTRIBUTE, 'int' , None, None, 
                [('16', '250000')], [], 
                '''                Flush
                ''',
                'flush_timer',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('holddown-timer', ATTRIBUTE, 'int' , None, None, 
                [('15', '200000')], [], 
                '''                Holddown
                ''',
                'holddown_timer',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('invalid-timer', ATTRIBUTE, 'int' , None, None, 
                [('15', '200000')], [], 
                '''                Invalid
                ''',
                'invalid_timer',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('update-timer', ATTRIBUTE, 'int' , None, None, 
                [('5', '50000')], [], 
                '''                Interval between updates
                ''',
                'update_timer',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-rip-cfg', True),
            _MetaInfoClassMember('auto-summary', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable automatic network number summarization
                ''',
                'auto_summary',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('broadcast-for-v2', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Send RIP v2 output packets to broadcast address
                ''',
                'broadcast_for_v2',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('default-information', REFERENCE_CLASS, 'DefaultInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.DefaultInformation', 
                [], [], 
                '''                Controls default information origination
                ''',
                'default_information',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16')], [], 
                '''                Default metric of redistributed routes
                ''',
                'default_metric',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('distance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Starts RIP configuration for a particular VRF
                ''',
                'enable',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Interfaces', 
                [], [], 
                '''                Table of RIP interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('ip-distances', REFERENCE_CLASS, 'IpDistances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.IpDistances', 
                [], [], 
                '''                Table of IP specific administrative distances
                ''',
                'ip_distances',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('1', '128')], [], 
                '''                Maximum number of paths allowed per route
                ''',
                'maximum_paths',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Neighbors', 
                [], [], 
                '''                Configure RIP Neighbors
                ''',
                'neighbors',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('nsf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Cisco Non Stop Forwarding
                ''',
                'nsf',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('output-delay', ATTRIBUTE, 'int' , None, None, 
                [('8', '50')], [], 
                '''                Inter-packet delay for RIP updates
                ''',
                'output_delay',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy for inbbound routing updates
                ''',
                'policy_in',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('policy-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy for outbound routing updates
                ''',
                'policy_out',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('redistribution', REFERENCE_CLASS, 'Redistribution' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Redistribution', 
                [], [], 
                '''                Redistribute information from another routing
                protocol
                ''',
                'redistribution',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf.Timers', 
                [], [], 
                '''                Various routing timers
                ''',
                'timers',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('validate-source-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable validation of source address of routing
                updates
                ''',
                'validate_source_disable',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip.Vrfs' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs.Vrf', 
                [], [], 
                '''                RIP configuration for a particular VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
    'Rip' : {
        'meta_info' : _MetaInfoClass('Rip',
            False, 
            [
            _MetaInfoClassMember('default-vrf', REFERENCE_CLASS, 'DefaultVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.DefaultVrf', 
                [], [], 
                '''                RIP configuration for Default VRF
                ''',
                'default_vrf',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg', 'Rip.Vrfs', 
                [], [], 
                '''                VRF related RIP configuration
                ''',
                'vrfs',
                'Cisco-IOS-XR-ip-rip-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rip-cfg',
            'rip',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_cfg'
        ),
    },
}
_meta_table['Rip.DefaultVrf.Redistribution.Bgps.Bgp']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Redistribution.Bgps']['meta_info']
_meta_table['Rip.DefaultVrf.Redistribution.Isises.Isis']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Redistribution.Isises']['meta_info']
_meta_table['Rip.DefaultVrf.Redistribution.EigrpS.Eigrp']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Redistribution.EigrpS']['meta_info']
_meta_table['Rip.DefaultVrf.Redistribution.Ospfs.Ospf']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Redistribution.Ospfs']['meta_info']
_meta_table['Rip.DefaultVrf.Redistribution.Connected']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Redistribution']['meta_info']
_meta_table['Rip.DefaultVrf.Redistribution.Bgps']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Redistribution']['meta_info']
_meta_table['Rip.DefaultVrf.Redistribution.Isises']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Redistribution']['meta_info']
_meta_table['Rip.DefaultVrf.Redistribution.EigrpS']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Redistribution']['meta_info']
_meta_table['Rip.DefaultVrf.Redistribution.Static']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Redistribution']['meta_info']
_meta_table['Rip.DefaultVrf.Redistribution.Ospfs']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Redistribution']['meta_info']
_meta_table['Rip.DefaultVrf.IpDistances.IpDistance']['meta_info'].parent =_meta_table['Rip.DefaultVrf.IpDistances']['meta_info']
_meta_table['Rip.DefaultVrf.Interfaces.Interface.Authentication']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Interfaces.Interface']['meta_info']
_meta_table['Rip.DefaultVrf.Interfaces.Interface.SiteOfOrigin']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Interfaces.Interface']['meta_info']
_meta_table['Rip.DefaultVrf.Interfaces.Interface.ReceiveVersion']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Interfaces.Interface']['meta_info']
_meta_table['Rip.DefaultVrf.Interfaces.Interface.SendVersion']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Interfaces.Interface']['meta_info']
_meta_table['Rip.DefaultVrf.Interfaces.Interface']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Interfaces']['meta_info']
_meta_table['Rip.DefaultVrf.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Neighbors']['meta_info']
_meta_table['Rip.DefaultVrf.DefaultInformation']['meta_info'].parent =_meta_table['Rip.DefaultVrf']['meta_info']
_meta_table['Rip.DefaultVrf.Redistribution']['meta_info'].parent =_meta_table['Rip.DefaultVrf']['meta_info']
_meta_table['Rip.DefaultVrf.IpDistances']['meta_info'].parent =_meta_table['Rip.DefaultVrf']['meta_info']
_meta_table['Rip.DefaultVrf.Interfaces']['meta_info'].parent =_meta_table['Rip.DefaultVrf']['meta_info']
_meta_table['Rip.DefaultVrf.Neighbors']['meta_info'].parent =_meta_table['Rip.DefaultVrf']['meta_info']
_meta_table['Rip.DefaultVrf.Timers']['meta_info'].parent =_meta_table['Rip.DefaultVrf']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Redistribution.Bgps.Bgp']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Redistribution.Bgps']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Redistribution.Isises.Isis']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Redistribution.Isises']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Redistribution.EigrpS.Eigrp']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Redistribution.EigrpS']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Redistribution.Ospfs.Ospf']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Redistribution.Ospfs']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Redistribution.Connected']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Redistribution']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Redistribution.Bgps']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Redistribution']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Redistribution.Isises']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Redistribution']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Redistribution.EigrpS']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Redistribution']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Redistribution.Static']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Redistribution']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Redistribution.Ospfs']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Redistribution']['meta_info']
_meta_table['Rip.Vrfs.Vrf.IpDistances.IpDistance']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.IpDistances']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Interfaces.Interface.Authentication']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Interfaces.Interface.SiteOfOrigin']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Interfaces.Interface.ReceiveVersion']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Interfaces.Interface.SendVersion']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Interfaces.Interface']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Interfaces']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Neighbors']['meta_info']
_meta_table['Rip.Vrfs.Vrf.DefaultInformation']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Redistribution']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf']['meta_info']
_meta_table['Rip.Vrfs.Vrf.IpDistances']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Interfaces']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Neighbors']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Timers']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf']['meta_info']
_meta_table['Rip.Vrfs.Vrf']['meta_info'].parent =_meta_table['Rip.Vrfs']['meta_info']
_meta_table['Rip.DefaultVrf']['meta_info'].parent =_meta_table['Rip']['meta_info']
_meta_table['Rip.Vrfs']['meta_info'].parent =_meta_table['Rip']['meta_info']
