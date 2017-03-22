


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Cfgmgr' : {
        'meta_info' : _MetaInfoClass('Cfgmgr',
            False, 
            [
            _MetaInfoClassMember('mode-exclusive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or Disabled
                ''',
                'mode_exclusive',
                'Cisco-IOS-XR-config-cfgmgr-cfg', False),
            ],
            'Cisco-IOS-XR-config-cfgmgr-cfg',
            'cfgmgr',
            _yang_ns._namespaces['Cisco-IOS-XR-config-cfgmgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_cfg'
        ),
    },
}
