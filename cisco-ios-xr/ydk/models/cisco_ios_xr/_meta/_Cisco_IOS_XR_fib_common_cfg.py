


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'FibPbtsForwardClassEnum' : _MetaInfoEnum('FibPbtsForwardClassEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg',
        {
            'any':'any',
        }, 'Cisco-IOS-XR-fib-common-cfg', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-cfg']),
    'FibPbtsFallbackEnum' : _MetaInfoEnum('FibPbtsFallbackEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg',
        {
            'list':'list',
            'any':'any',
            'drop':'drop',
        }, 'Cisco-IOS-XR-fib-common-cfg', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-cfg']),
    'Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback' : {
        'meta_info' : _MetaInfoClass('Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback',
            False, 
            [
            _MetaInfoClassMember('forward-class-number', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                PBTS forward class number
                ''',
                'forward_class_number',
                'Cisco-IOS-XR-fib-common-cfg', True, [
                    _MetaInfoClassMember('forward-class-number', REFERENCE_ENUM_CLASS, 'FibPbtsForwardClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'FibPbtsForwardClassEnum', 
                        [], [], 
                        '''                        PBTS forward class number
                        ''',
                        'forward_class_number',
                        'Cisco-IOS-XR-fib-common-cfg', True),
                    _MetaInfoClassMember('forward-class-number', ATTRIBUTE, 'int' , None, None, 
                        [('0', '8')], [], 
                        '''                        PBTS forward class number
                        ''',
                        'forward_class_number',
                        'Cisco-IOS-XR-fib-common-cfg', True),
                ]),
            _MetaInfoClassMember('fallback-class-number-array', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Set PBTS fallback class number array
                ''',
                'fallback_class_number_array',
                'Cisco-IOS-XR-fib-common-cfg', False, max_elements=7),
            _MetaInfoClassMember('fallback-type', REFERENCE_ENUM_CLASS, 'FibPbtsFallbackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'FibPbtsFallbackEnum', 
                [], [], 
                '''                Set PBTS fallback type
                ''',
                'fallback_type',
                'Cisco-IOS-XR-fib-common-cfg', False),
            ],
            'Cisco-IOS-XR-fib-common-cfg',
            'pbts-forward-class-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg'
        ),
    },
    'Fib.PbtsForwardClassFallbacks' : {
        'meta_info' : _MetaInfoClass('Fib.PbtsForwardClassFallbacks',
            False, 
            [
            _MetaInfoClassMember('pbts-forward-class-fallback', REFERENCE_LIST, 'PbtsForwardClassFallback' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback', 
                [], [], 
                '''                Set PBTS class for fallback
                ''',
                'pbts_forward_class_fallback',
                'Cisco-IOS-XR-fib-common-cfg', False),
            ],
            'Cisco-IOS-XR-fib-common-cfg',
            'pbts-forward-class-fallbacks',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg'
        ),
    },
    'Fib.Platform.LabelSwitchedMulticast' : {
        'meta_info' : _MetaInfoClass('Fib.Platform.LabelSwitchedMulticast',
            False, 
            [
            _MetaInfoClassMember('frr-holdtime', ATTRIBUTE, 'int' , None, None, 
                [('3', '180')], [], 
                '''                Set time to keep FRR slots programmed post FRR
                ''',
                'frr_holdtime',
                'Cisco-IOS-XR-fib-common-cfg', False),
            ],
            'Cisco-IOS-XR-fib-common-cfg',
            'label-switched-multicast',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg'
        ),
    },
    'Fib.Platform' : {
        'meta_info' : _MetaInfoClass('Fib.Platform',
            False, 
            [
            _MetaInfoClassMember('label-switched-multicast', REFERENCE_CLASS, 'LabelSwitchedMulticast' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'Fib.Platform.LabelSwitchedMulticast', 
                [], [], 
                '''                Options for label-switched-multicast parameters
                ''',
                'label_switched_multicast',
                'Cisco-IOS-XR-fib-common-cfg', False),
            ],
            'Cisco-IOS-XR-fib-common-cfg',
            'platform',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg'
        ),
    },
    'Fib' : {
        'meta_info' : _MetaInfoClass('Fib',
            False, 
            [
            _MetaInfoClassMember('pbts-forward-class-fallbacks', REFERENCE_CLASS, 'PbtsForwardClassFallbacks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'Fib.PbtsForwardClassFallbacks', 
                [], [], 
                '''                PBTS class configuration
                ''',
                'pbts_forward_class_fallbacks',
                'Cisco-IOS-XR-fib-common-cfg', False),
            _MetaInfoClassMember('platform', REFERENCE_CLASS, 'Platform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg', 'Fib.Platform', 
                [], [], 
                '''                FIB platform parameters
                ''',
                'platform',
                'Cisco-IOS-XR-fib-common-cfg', False),
            _MetaInfoClassMember('prefer-aib-routes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set options for adjacency routes overriding RIB
                routes
                ''',
                'prefer_aib_routes',
                'Cisco-IOS-XR-fib-common-cfg', False),
            ],
            'Cisco-IOS-XR-fib-common-cfg',
            'fib',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_cfg'
        ),
    },
}
_meta_table['Fib.PbtsForwardClassFallbacks.PbtsForwardClassFallback']['meta_info'].parent =_meta_table['Fib.PbtsForwardClassFallbacks']['meta_info']
_meta_table['Fib.Platform.LabelSwitchedMulticast']['meta_info'].parent =_meta_table['Fib.Platform']['meta_info']
_meta_table['Fib.PbtsForwardClassFallbacks']['meta_info'].parent =_meta_table['Fib']['meta_info']
_meta_table['Fib.Platform']['meta_info'].parent =_meta_table['Fib']['meta_info']
