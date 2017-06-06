


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'InventoryConfigurations.Entity' : {
        'meta_info' : _MetaInfoClass('InventoryConfigurations.Entity',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Entity name
                ''',
                'name',
                'Cisco-IOS-XR-invmgr-cfg', True),
            _MetaInfoClassMember('name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entity name
                ''',
                'name_xr',
                'Cisco-IOS-XR-invmgr-cfg', False),
            ],
            'Cisco-IOS-XR-invmgr-cfg',
            'entity',
            _yang_ns._namespaces['Cisco-IOS-XR-invmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_invmgr_cfg'
        ),
    },
    'InventoryConfigurations' : {
        'meta_info' : _MetaInfoClass('InventoryConfigurations',
            False, 
            [
            _MetaInfoClassMember('entity', REFERENCE_LIST, 'Entity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_invmgr_cfg', 'InventoryConfigurations.Entity', 
                [], [], 
                '''                Entity name
                ''',
                'entity',
                'Cisco-IOS-XR-invmgr-cfg', False),
            ],
            'Cisco-IOS-XR-invmgr-cfg',
            'inventory-configurations',
            _yang_ns._namespaces['Cisco-IOS-XR-invmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_invmgr_cfg'
        ),
    },
}
_meta_table['InventoryConfigurations.Entity']['meta_info'].parent =_meta_table['InventoryConfigurations']['meta_info']
