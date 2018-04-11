""" Cisco_IOS_XR_spirit_fpd_infra_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR spirit\-fpd\-infra package configuration.

This module contains definitions
for the following management objects\:
  fpd\: Configuration for fpd auto\-upgrade enable/disable 

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


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
    
    .. attribute:: auto_upgrade
    
    	Variable for fpd auto\-upgrade enable/disable
    	**type**\:  :py:class:`AutoUpgrade <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_fpd_infra_cfg.AutoUpgrade>`
    
    

    """

    _prefix = 'spirit-fpd-infra-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Fpd, self).__init__()
        self._top_entity = None

        self.yang_name = "fpd"
        self.yang_parent_name = "Cisco-IOS-XR-spirit-fpd-infra-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('auto_upgrade', YLeaf(YType.enumeration, 'auto-upgrade')),
        ])
        self.auto_upgrade = None
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-fpd-infra-cfg:fpd"

    def __setattr__(self, name, value):
        self._perform_setattr(Fpd, ['auto_upgrade'], name, value)

    def clone_ptr(self):
        self._top_entity = Fpd()
        return self._top_entity

