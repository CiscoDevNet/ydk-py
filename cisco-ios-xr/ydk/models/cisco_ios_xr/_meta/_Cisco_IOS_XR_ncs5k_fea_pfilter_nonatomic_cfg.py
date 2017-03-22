


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AtomicDisableDfltActnEnum' : _MetaInfoEnum('AtomicDisableDfltActnEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg',
        {
            'default-action-deny':'default_action_deny',
            'default-action-permit':'default_action_permit',
        }, 'Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg']),
    'Hardware.AccessList' : {
        'meta_info' : _MetaInfoClass('Hardware.AccessList',
            False, 
            [
            _MetaInfoClassMember('atomic-disable', REFERENCE_ENUM_CLASS, 'AtomicDisableDfltActnEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg', 'AtomicDisableDfltActnEnum', 
                [], [], 
                '''                Specify Option for Atomic disable
                ''',
                'atomic_disable',
                'Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg', False),
            ],
            'Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg',
            'access-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg'
        ),
    },
    'Hardware' : {
        'meta_info' : _MetaInfoClass('Hardware',
            False, 
            [
            _MetaInfoClassMember('access-list', REFERENCE_CLASS, 'AccessList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg', 'Hardware.AccessList', 
                [], [], 
                '''                Access-list option
                ''',
                'access_list',
                'Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg', False),
            ],
            'Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg',
            'hardware',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg'
        ),
    },
}
_meta_table['Hardware.AccessList']['meta_info'].parent =_meta_table['Hardware']['meta_info']
