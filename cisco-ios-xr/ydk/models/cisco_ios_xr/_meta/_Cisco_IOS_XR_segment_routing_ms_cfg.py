


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SrmsMiFlagEnum' : _MetaInfoEnum('SrmsMiFlagEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-segment-routing-ms-cfg', _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-cfg']),
    'Sr.GlobalBlock' : {
        'meta_info' : _MetaInfoClass('Sr.GlobalBlock',
            False, 
            [
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int' , None, None, 
                [('16000', '1048574')], [], 
                '''                SRGB Lower Bound
                ''',
                'lower_bound',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int' , None, None, 
                [('16001', '1048575')], [], 
                '''                SRGB Upper Bound
                ''',
                'upper_bound',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'global-block',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg'
        ),
    },
    'Sr.Mappings.Mapping' : {
        'meta_info' : _MetaInfoClass('Sr.Mappings.Mapping',
            False, 
            [
            _MetaInfoClassMember('af', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Address Family
                ''',
                'af',
                'Cisco-IOS-XR-segment-routing-ms-cfg', True),
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IP prefix
                ''',
                'ip',
                'Cisco-IOS-XR-segment-routing-ms-cfg', True),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Mask
                ''',
                'mask',
                'Cisco-IOS-XR-segment-routing-ms-cfg', True),
            _MetaInfoClassMember('flag-attached', REFERENCE_ENUM_CLASS, 'SrmsMiFlagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'SrmsMiFlagEnum', 
                [], [], 
                '''                Enable/Disable Attached flag
                ''',
                'flag_attached',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            _MetaInfoClassMember('sid-range', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Range (number of SIDs)
                ''',
                'sid_range',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            _MetaInfoClassMember('sid-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '1048575')], [], 
                '''                Start of SID index range
                ''',
                'sid_start',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'mapping',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg'
        ),
    },
    'Sr.Mappings' : {
        'meta_info' : _MetaInfoClass('Sr.Mappings',
            False, 
            [
            _MetaInfoClassMember('mapping', REFERENCE_LIST, 'Mapping' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.Mappings.Mapping', 
                [], [], 
                '''                IP prefix to SID mapping
                ''',
                'mapping',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'mappings',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg'
        ),
    },
    'Sr' : {
        'meta_info' : _MetaInfoClass('Sr',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                enable SR
                ''',
                'enable',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            _MetaInfoClassMember('global-block', REFERENCE_CLASS, 'GlobalBlock' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.GlobalBlock', 
                [], [], 
                '''                Global Block Segment Routing
                ''',
                'global_block',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            _MetaInfoClassMember('mappings', REFERENCE_CLASS, 'Mappings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg', 'Sr.Mappings', 
                [], [], 
                '''                Mapping Server
                ''',
                'mappings',
                'Cisco-IOS-XR-segment-routing-ms-cfg', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-cfg',
            'sr',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_cfg'
        ),
    },
}
_meta_table['Sr.Mappings.Mapping']['meta_info'].parent =_meta_table['Sr.Mappings']['meta_info']
_meta_table['Sr.GlobalBlock']['meta_info'].parent =_meta_table['Sr']['meta_info']
_meta_table['Sr.Mappings']['meta_info'].parent =_meta_table['Sr']['meta_info']
