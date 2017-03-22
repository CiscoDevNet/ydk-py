


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'BannerEnum' : _MetaInfoEnum('BannerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg',
        {
            'exec':'exec_',
            'incoming':'incoming',
            'motd':'motd',
            'login':'login',
            'slip-ppp':'slip_ppp',
            'prompt-timeout':'prompt_timeout',
        }, 'Cisco-IOS-XR-infra-infra-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-infra-cfg']),
    'Banners.Banner' : {
        'meta_info' : _MetaInfoClass('Banners.Banner',
            False, 
            [
            _MetaInfoClassMember('banner-name', REFERENCE_ENUM_CLASS, 'BannerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg', 'BannerEnum', 
                [], [], 
                '''                Banner Type
                ''',
                'banner_name',
                'Cisco-IOS-XR-infra-infra-cfg', True),
            _MetaInfoClassMember('banner-text', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Banner text message
                ''',
                'banner_text',
                'Cisco-IOS-XR-infra-infra-cfg', False),
            ],
            'Cisco-IOS-XR-infra-infra-cfg',
            'banner',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-infra-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg'
        ),
    },
    'Banners' : {
        'meta_info' : _MetaInfoClass('Banners',
            False, 
            [
            _MetaInfoClassMember('banner', REFERENCE_LIST, 'Banner' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg', 'Banners.Banner', 
                [], [], 
                '''                Select a Banner Type
                ''',
                'banner',
                'Cisco-IOS-XR-infra-infra-cfg', False),
            ],
            'Cisco-IOS-XR-infra-infra-cfg',
            'banners',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-infra-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg'
        ),
    },
}
_meta_table['Banners.Banner']['meta_info'].parent =_meta_table['Banners']['meta_info']
