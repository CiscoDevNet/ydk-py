


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Vty.VtyPools.VtyPool' : {
        'meta_info' : _MetaInfoClass('Vty.VtyPools.VtyPool',
            False, 
            [
            _MetaInfoClassMember('pool-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                For configuring range for default pool use
                'default',For configuring range for
                fault-manager pool use 'fm',For configuring
                range for any user defined pool use any other
                string
                ''',
                'pool_name',
                'Cisco-IOS-XR-tty-vty-cfg', True),
            _MetaInfoClassMember('first-vty', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                First VTY number,For default VTY use 0,For
                user-defined use 5,For fault-manager use 100
                ''',
                'first_vty',
                'Cisco-IOS-XR-tty-vty-cfg', False),
            _MetaInfoClassMember('last-vty', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Last VTY number,For default configure between
                0-99,For user-defined configure between 5-99
                ,For fault-manager configure between 100-199
                ''',
                'last_vty',
                'Cisco-IOS-XR-tty-vty-cfg', False),
            _MetaInfoClassMember('line-template', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of line template
                ''',
                'line_template',
                'Cisco-IOS-XR-tty-vty-cfg', False),
            _MetaInfoClassMember('none', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Empty Option
                ''',
                'none',
                'Cisco-IOS-XR-tty-vty-cfg', False),
            ],
            'Cisco-IOS-XR-tty-vty-cfg',
            'vty-pool',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-vty-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_vty_cfg'
        ),
    },
    'Vty.VtyPools' : {
        'meta_info' : _MetaInfoClass('Vty.VtyPools',
            False, 
            [
            _MetaInfoClassMember('vty-pool', REFERENCE_LIST, 'VtyPool' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_vty_cfg', 'Vty.VtyPools.VtyPool', 
                [], [], 
                '''                VTY Pool
                ''',
                'vty_pool',
                'Cisco-IOS-XR-tty-vty-cfg', False),
            ],
            'Cisco-IOS-XR-tty-vty-cfg',
            'vty-pools',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-vty-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_vty_cfg'
        ),
    },
    'Vty' : {
        'meta_info' : _MetaInfoClass('Vty',
            False, 
            [
            _MetaInfoClassMember('vty-pools', REFERENCE_CLASS, 'VtyPools' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_vty_cfg', 'Vty.VtyPools', 
                [], [], 
                '''                List of VTY Pools
                ''',
                'vty_pools',
                'Cisco-IOS-XR-tty-vty-cfg', False),
            ],
            'Cisco-IOS-XR-tty-vty-cfg',
            'vty',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-vty-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_vty_cfg'
        ),
    },
}
_meta_table['Vty.VtyPools.VtyPool']['meta_info'].parent =_meta_table['Vty.VtyPools']['meta_info']
_meta_table['Vty.VtyPools']['meta_info'].parent =_meta_table['Vty']['meta_info']
