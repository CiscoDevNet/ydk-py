""" Cisco_IOS_XR_fpd_infra_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fpd\-infra package configuration.

This module contains definitions
for the following management objects\:
  fpd\: Configuration for fpd auto\-upgrade enable/disable 

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AutoReload(Enum):
    """
    AutoReload (Enum Class)

    Auto reload

    .. data:: disable = 0

    	fpd auto-reload disable

    .. data:: enable = 1

    	fpd auto-reload enable

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class AutoUpgrade(Enum):
    """
    AutoUpgrade (Enum Class)

    Auto upgrade

    .. data:: disable = 0

    	fpd auto-upgrade disable

    .. data:: enable = 1

    	fpd auto-upgrade enable

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")



class Fpd(Entity):
    """
    Configuration for fpd auto\-upgrade enable/disable
    
    .. attribute:: auto_reload
    
    	Variable for fpd auto\-reload enable/disable
    	**type**\:  :py:class:`AutoReload <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fpd_infra_cfg.AutoReload>`
    
    .. attribute:: auto_upgrade
    
    	Variable for fpd auto\-upgrade enable/disable
    	**type**\:  :py:class:`AutoUpgrade <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fpd_infra_cfg.AutoUpgrade>`
    
    

    """

    _prefix = 'fpd-infra-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Fpd, self).__init__()
        self._top_entity = None

        self.yang_name = "fpd"
        self.yang_parent_name = "Cisco-IOS-XR-fpd-infra-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('auto_reload', (YLeaf(YType.enumeration, 'auto-reload'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_fpd_infra_cfg', 'AutoReload', '')])),
            ('auto_upgrade', (YLeaf(YType.enumeration, 'auto-upgrade'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_fpd_infra_cfg', 'AutoUpgrade', '')])),
        ])
        self.auto_reload = None
        self.auto_upgrade = None
        self._segment_path = lambda: "Cisco-IOS-XR-fpd-infra-cfg:fpd"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Fpd, ['auto_reload', 'auto_upgrade'], name, value)

    def clone_ptr(self):
        self._top_entity = Fpd()
        return self._top_entity

