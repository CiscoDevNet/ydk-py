


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Telnet.Vrfs.Vrf.Ipv4' : {
        'meta_info' : _MetaInfoClass('Telnet.Vrfs.Vrf.Ipv4',
            False, 
            [
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                Specify the DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-ipv4-telnet-mgmt-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-telnet-mgmt-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-telnet-mgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_mgmt_cfg'
        ),
    },
    'Telnet.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Telnet.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-telnet-mgmt-cfg', True),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_mgmt_cfg', 'Telnet.Vrfs.Vrf.Ipv4', 
                [], [], 
                '''                IPv4 configuration
                ''',
                'ipv4',
                'Cisco-IOS-XR-ipv4-telnet-mgmt-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-telnet-mgmt-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-telnet-mgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_mgmt_cfg'
        ),
    },
    'Telnet.Vrfs' : {
        'meta_info' : _MetaInfoClass('Telnet.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_mgmt_cfg', 'Telnet.Vrfs.Vrf', 
                [], [], 
                '''                VRF name for telnet service
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-telnet-mgmt-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-telnet-mgmt-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-telnet-mgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_mgmt_cfg'
        ),
    },
    'Telnet' : {
        'meta_info' : _MetaInfoClass('Telnet',
            False, 
            [
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_mgmt_cfg', 'Telnet.Vrfs', 
                [], [], 
                '''                VRF name for telnet service
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-telnet-mgmt-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-telnet-mgmt-cfg',
            'telnet',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-telnet-mgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_telnet_mgmt_cfg'
        ),
    },
}
_meta_table['Telnet.Vrfs.Vrf.Ipv4']['meta_info'].parent =_meta_table['Telnet.Vrfs.Vrf']['meta_info']
_meta_table['Telnet.Vrfs.Vrf']['meta_info'].parent =_meta_table['Telnet.Vrfs']['meta_info']
_meta_table['Telnet.Vrfs']['meta_info'].parent =_meta_table['Telnet']['meta_info']
