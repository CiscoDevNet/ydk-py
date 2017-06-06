


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'FabVqiConfig.Operates.Operate' : {
        'meta_info' : _MetaInfoClass('FabVqiConfig.Operates.Operate',
            False, 
            [
            _MetaInfoClassMember('id1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                none
                ''',
                'id1',
                'Cisco-IOS-XR-asr9k-fab-cfg', True),
            _MetaInfoClassMember('id1-xr', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                none
                ''',
                'id1_xr',
                'Cisco-IOS-XR-asr9k-fab-cfg', False),
            _MetaInfoClassMember('id2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                none
                ''',
                'id2',
                'Cisco-IOS-XR-asr9k-fab-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-fab-cfg',
            'operate',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-fab-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg'
        ),
    },
    'FabVqiConfig.Operates' : {
        'meta_info' : _MetaInfoClass('FabVqiConfig.Operates',
            False, 
            [
            _MetaInfoClassMember('operate', REFERENCE_LIST, 'Operate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg', 'FabVqiConfig.Operates.Operate', 
                [], [], 
                '''                none
                ''',
                'operate',
                'Cisco-IOS-XR-asr9k-fab-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-fab-cfg',
            'operates',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-fab-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg'
        ),
    },
    'FabVqiConfig' : {
        'meta_info' : _MetaInfoClass('FabVqiConfig',
            False, 
            [
            _MetaInfoClassMember('operates', REFERENCE_CLASS, 'Operates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg', 'FabVqiConfig.Operates', 
                [], [], 
                '''                none
                ''',
                'operates',
                'Cisco-IOS-XR-asr9k-fab-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-fab-cfg',
            'fab-vqi-config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-fab-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg'
        ),
    },
}
_meta_table['FabVqiConfig.Operates.Operate']['meta_info'].parent =_meta_table['FabVqiConfig.Operates']['meta_info']
_meta_table['FabVqiConfig.Operates']['meta_info'].parent =_meta_table['FabVqiConfig']['meta_info']
