


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SbfdAddressFamilyEnum' : _MetaInfoEnum('SbfdAddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-ip-sbfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-oper']),
    'BfdAfIdEnum' : _MetaInfoEnum('BfdAfIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper',
        {
            'bfd-af-id-none':'bfd_af_id_none',
            'bfd-af-id-ipv4':'bfd_af_id_ipv4',
            'bfd-af-id-ipv6':'bfd_af_id_ipv6',
        }, 'Cisco-IOS-XR-ip-sbfd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-oper']),
    'Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress' : {
        'meta_info' : _MetaInfoClass('Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BfdAfIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper', 'BfdAfIdEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No Address
                ''',
                'dummy',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address type
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-oper',
            'ip-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper'
        ),
    },
    'Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator' : {
        'meta_info' : _MetaInfoClass('Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address
                ''',
                'address',
                'Cisco-IOS-XR-ip-sbfd-oper', False, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address
                        ''',
                        'address',
                        'Cisco-IOS-XR-ip-sbfd-oper', False),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address
                        ''',
                        'address',
                        'Cisco-IOS-XR-ip-sbfd-oper', False),
                ]),
            _MetaInfoClassMember('discr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote discriminator
                ''',
                'discr',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('discr-src', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Discriminator source name
                ''',
                'discr_src',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('ip-address', REFERENCE_CLASS, 'IpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper', 'Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress', 
                [], [], 
                '''                IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Remote Discriminator
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Status
                ''',
                'status',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('tid-type', REFERENCE_ENUM_CLASS, 'SbfdAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper', 'SbfdAddressFamilyEnum', 
                [], [], 
                '''                Target identifier for sbfd
                ''',
                'tid_type',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF Name 
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('vrf-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name_xr',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-oper',
            'remote-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper'
        ),
    },
    'Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf' : {
        'meta_info' : _MetaInfoClass('Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-sbfd-oper', True),
            _MetaInfoClassMember('remote-discriminator', REFERENCE_LIST, 'RemoteDiscriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper', 'Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator', 
                [], [], 
                '''                SBFD remote discriminator 
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-oper',
            'remote-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper'
        ),
    },
    'Sbfd.TargetIdentifier.RemoteVrfs' : {
        'meta_info' : _MetaInfoClass('Sbfd.TargetIdentifier.RemoteVrfs',
            False, 
            [
            _MetaInfoClassMember('remote-vrf', REFERENCE_LIST, 'RemoteVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper', 'Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf', 
                [], [], 
                '''                Table of remote discriminator data per VRF
                ''',
                'remote_vrf',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-oper',
            'remote-vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper'
        ),
    },
    'Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator' : {
        'meta_info' : _MetaInfoClass('Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator',
            False, 
            [
            _MetaInfoClassMember('discr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local discriminator
                ''',
                'discr',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('discr-src', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Discriminator source name
                ''',
                'discr_src',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('flags', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MODE name
                ''',
                'flags',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('local-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Status
                ''',
                'status',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF Name 
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('vrf-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name_xr',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-oper',
            'local-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper'
        ),
    },
    'Sbfd.TargetIdentifier.LocalVrfs.LocalVrf' : {
        'meta_info' : _MetaInfoClass('Sbfd.TargetIdentifier.LocalVrfs.LocalVrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-sbfd-oper', True),
            _MetaInfoClassMember('local-discriminator', REFERENCE_LIST, 'LocalDiscriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper', 'Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator', 
                [], [], 
                '''                SBFD local discriminator 
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-oper',
            'local-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper'
        ),
    },
    'Sbfd.TargetIdentifier.LocalVrfs' : {
        'meta_info' : _MetaInfoClass('Sbfd.TargetIdentifier.LocalVrfs',
            False, 
            [
            _MetaInfoClassMember('local-vrf', REFERENCE_LIST, 'LocalVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper', 'Sbfd.TargetIdentifier.LocalVrfs.LocalVrf', 
                [], [], 
                '''                Table of local discriminator data per VRF
                ''',
                'local_vrf',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-oper',
            'local-vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper'
        ),
    },
    'Sbfd.TargetIdentifier' : {
        'meta_info' : _MetaInfoClass('Sbfd.TargetIdentifier',
            False, 
            [
            _MetaInfoClassMember('local-vrfs', REFERENCE_CLASS, 'LocalVrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper', 'Sbfd.TargetIdentifier.LocalVrfs', 
                [], [], 
                '''                SBFD local discriminator  data
                ''',
                'local_vrfs',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            _MetaInfoClassMember('remote-vrfs', REFERENCE_CLASS, 'RemoteVrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper', 'Sbfd.TargetIdentifier.RemoteVrfs', 
                [], [], 
                '''                SBFD remote discriminator data
                ''',
                'remote_vrfs',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-oper',
            'target-identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper'
        ),
    },
    'Sbfd' : {
        'meta_info' : _MetaInfoClass('Sbfd',
            False, 
            [
            _MetaInfoClassMember('target-identifier', REFERENCE_CLASS, 'TargetIdentifier' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper', 'Sbfd.TargetIdentifier', 
                [], [], 
                '''                Target-identifier information
                ''',
                'target_identifier',
                'Cisco-IOS-XR-ip-sbfd-oper', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-oper',
            'sbfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper'
        ),
    },
}
_meta_table['Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress']['meta_info'].parent =_meta_table['Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator']['meta_info']
_meta_table['Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator']['meta_info'].parent =_meta_table['Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf']['meta_info']
_meta_table['Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf']['meta_info'].parent =_meta_table['Sbfd.TargetIdentifier.RemoteVrfs']['meta_info']
_meta_table['Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator']['meta_info'].parent =_meta_table['Sbfd.TargetIdentifier.LocalVrfs.LocalVrf']['meta_info']
_meta_table['Sbfd.TargetIdentifier.LocalVrfs.LocalVrf']['meta_info'].parent =_meta_table['Sbfd.TargetIdentifier.LocalVrfs']['meta_info']
_meta_table['Sbfd.TargetIdentifier.RemoteVrfs']['meta_info'].parent =_meta_table['Sbfd.TargetIdentifier']['meta_info']
_meta_table['Sbfd.TargetIdentifier.LocalVrfs']['meta_info'].parent =_meta_table['Sbfd.TargetIdentifier']['meta_info']
_meta_table['Sbfd.TargetIdentifier']['meta_info'].parent =_meta_table['Sbfd']['meta_info']
