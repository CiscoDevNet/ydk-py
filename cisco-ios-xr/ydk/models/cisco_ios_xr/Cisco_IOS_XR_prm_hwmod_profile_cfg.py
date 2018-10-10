""" Cisco_IOS_XR_prm_hwmod_profile_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR prm\-hwmod\-profile package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\: HardwareModule

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ProfileTypeData(Enum):
    """
    ProfileTypeData (Enum Class)

    Profile type data

    .. data:: sp = 1

    	SP Profile

    .. data:: dc = 2

    	DC Profile

    """

    sp = Enum.YLeaf(1, "sp")

    dc = Enum.YLeaf(2, "dc")



class HardwareModule(Entity):
    """
    HardwareModule
    
    .. attribute:: profile
    
    	Specify Profile type
    	**type**\:  :py:class:`ProfileTypeData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_profile_cfg.ProfileTypeData>`
    
    

    """

    _prefix = 'prm-hwmod-profile-cfg'
    _revision = '2017-12-05'

    def __init__(self):
        super(HardwareModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module"
        self.yang_parent_name = "Cisco-IOS-XR-prm-hwmod-profile-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('profile', (YLeaf(YType.enumeration, 'profile'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_hwmod_profile_cfg', 'ProfileTypeData', '')])),
        ])
        self.profile = None
        self._segment_path = lambda: "Cisco-IOS-XR-prm-hwmod-profile-cfg:hardware-module"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HardwareModule, ['profile'], name, value)

    def clone_ptr(self):
        self._top_entity = HardwareModule()
        return self._top_entity

