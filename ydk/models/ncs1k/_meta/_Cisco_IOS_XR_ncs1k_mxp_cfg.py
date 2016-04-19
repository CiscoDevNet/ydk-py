


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'ClientDataRateEnum' : _MetaInfoEnum('ClientDataRateEnum', 'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg',
        {
            'ten-gig':'TEN_GIG',
            'forty-gig':'FORTY_GIG',
            'hundred-gig':'HUNDRED_GIG',
        }, 'Cisco-IOS-XR-ncs1k-mxp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-cfg']),
    'TrunkDataRateEnum' : _MetaInfoEnum('TrunkDataRateEnum', 'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg',
        {
            'hundred-gig':'HUNDRED_GIG',
            'two-hundred-gig':'TWO_HUNDRED_GIG',
            'two-hundred-fifty-gig':'TWO_HUNDRED_FIFTY_GIG',
        }, 'Cisco-IOS-XR-ncs1k-mxp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-cfg']),
    'FecEnum' : _MetaInfoEnum('FecEnum', 'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg',
        {
            'sd7':'SD7',
            'sd20':'SD20',
        }, 'Cisco-IOS-XR-ncs1k-mxp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-cfg']),
    'HardwareModule.Node.Values.Value' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Node.Values.Value',
            False, 
            [
            _MetaInfoClassMember('slice-id', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set Slice
                ''',
                'slice_id',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', True),
            _MetaInfoClassMember('client-rate', REFERENCE_ENUM_CLASS, 'ClientDataRateEnum' , 'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg', 'ClientDataRateEnum', 
                [], [], 
                '''                Client Rate
                ''',
                'client_rate',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', False),
            _MetaInfoClassMember('fec', REFERENCE_ENUM_CLASS, 'FecEnum' , 'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg', 'FecEnum', 
                [], [], 
                '''                FEC
                ''',
                'fec',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', False),
            _MetaInfoClassMember('trunk-rate', REFERENCE_ENUM_CLASS, 'TrunkDataRateEnum' , 'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg', 'TrunkDataRateEnum', 
                [], [], 
                '''                TrunkRate
                ''',
                'trunk_rate',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-cfg',
            'value',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-cfg'],
        'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg'
        ),
    },
    'HardwareModule.Node.Values' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Node.Values',
            False, 
            [
            _MetaInfoClassMember('value', REFERENCE_LIST, 'Value' , 'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg', 'HardwareModule.Node.Values.Value', 
                [], [], 
                '''                Data rates & FEC
                ''',
                'value',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-cfg',
            'values',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-cfg'],
        'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg'
        ),
    },
    'HardwareModule.Node' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Node',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Fully qualified line card specification
                ''',
                'location',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', True),
            _MetaInfoClassMember('values', REFERENCE_CLASS, 'Values' , 'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg', 'HardwareModule.Node.Values', 
                [], [], 
                '''                Slice to be Provisioned
                ''',
                'values',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-cfg'],
        'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg'
        ),
    },
    'HardwareModule' : {
        'meta_info' : _MetaInfoClass('HardwareModule',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg', 'HardwareModule.Node', 
                [], [], 
                '''                Node
                ''',
                'node',
                'Cisco-IOS-XR-ncs1k-mxp-cfg', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-cfg',
            'hardware-module',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-cfg'],
        'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_cfg'
        ),
    },
}
_meta_table['HardwareModule.Node.Values.Value']['meta_info'].parent =_meta_table['HardwareModule.Node.Values']['meta_info']
_meta_table['HardwareModule.Node.Values']['meta_info'].parent =_meta_table['HardwareModule.Node']['meta_info']
_meta_table['HardwareModule.Node']['meta_info'].parent =_meta_table['HardwareModule']['meta_info']
