


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'TrunkDataRateEnum' : _MetaInfoEnum('TrunkDataRateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg',
        {
            'hundred-gig':'hundred_gig',
            'two-hundred-gig':'two_hundred_gig',
            'two-hundred-fifty-gig':'two_hundred_fifty_gig',
        }, 'Cisco-IOS-XR-ncs1k-mxp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-cfg']),
    'ClientDataRateEnum' : _MetaInfoEnum('ClientDataRateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg',
        {
            'ten-gig':'ten_gig',
            'forty-gig':'forty_gig',
            'hundred-gig':'hundred_gig',
        }, 'Cisco-IOS-XR-ncs1k-mxp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-cfg']),
    'FecEnum' : _MetaInfoEnum('FecEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg',
        {
            'sd7':'sd7',
            'sd20':'sd20',
        }, 'Cisco-IOS-XR-ncs1k-mxp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-cfg']),
    'HardwareModule.Node.Slice.Values' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Node.Slice.Values',
            False, 
            [
            _MetaInfoClassMember('client-rate', REFERENCE_ENUM_CLASS, 'ClientDataRateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg', 'ClientDataRateEnum', 
                [], [], 
                '''                Client Rate
                ''',
                'client_rate',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', False),
            _MetaInfoClassMember('encrypted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Encrypted
                ''',
                'encrypted',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', False),
            _MetaInfoClassMember('fec', REFERENCE_ENUM_CLASS, 'FecEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg', 'FecEnum', 
                [], [], 
                '''                FEC
                ''',
                'fec',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', False),
            _MetaInfoClassMember('trunk-rate', REFERENCE_ENUM_CLASS, 'TrunkDataRateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg', 'TrunkDataRateEnum', 
                [], [], 
                '''                TrunkRate
                ''',
                'trunk_rate',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-cfg',
            'values',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg'
        ),
    },
    'HardwareModule.Node.Slice' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Node.Slice',
            False, 
            [
            _MetaInfoClassMember('slice-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set Slice
                ''',
                'slice_id',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', True),
            _MetaInfoClassMember('lldp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Drop LLDP Packets
                ''',
                'lldp',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', False),
            _MetaInfoClassMember('values', REFERENCE_CLASS, 'Values' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg', 'HardwareModule.Node.Slice.Values', 
                [], [], 
                '''                Data rates & FEC
                ''',
                'values',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-cfg',
            'slice',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg'
        ),
    },
    'HardwareModule.Node' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Node',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Fully qualified line card specification
                ''',
                'location',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', True),
            _MetaInfoClassMember('slice', REFERENCE_LIST, 'Slice' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg', 'HardwareModule.Node.Slice', 
                [], [], 
                '''                Slice to be Provisioned
                ''',
                'slice',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg'
        ),
    },
    'HardwareModule' : {
        'meta_info' : _MetaInfoClass('HardwareModule',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg', 'HardwareModule.Node', 
                [], [], 
                '''                Node
                ''',
                'node',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-cfg',
            'hardware-module',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_cfg'
        ),
    },
}
_meta_table['HardwareModule.Node.Slice.Values']['meta_info'].parent =_meta_table['HardwareModule.Node.Slice']['meta_info']
_meta_table['HardwareModule.Node.Slice']['meta_info'].parent =_meta_table['HardwareModule.Node']['meta_info']
_meta_table['HardwareModule.Node']['meta_info'].parent =_meta_table['HardwareModule']['meta_info']
