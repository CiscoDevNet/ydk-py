""" Cisco_IOS_XR_sysadmin_nto_misc_set_hostname 

This module contains a collection of YANG definitions
for Cisco IOS\-XR syadmin hostname configuration and cli.

This module contains definitions
for the following management objects\:
hostname cli and configuration data

Copyright (c) 2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Hostname(Entity):
    """
    Set system`s network name
    
    .. attribute:: name
    
    	
    	**type**\: str
    
    	**pattern:** [a\-zA\-Z0\-9\_.{}+\-]+
    
    

    """

    _prefix = 'hostname'
    _revision = '2017-04-12'

    def __init__(self):
        super(Hostname, self).__init__()
        self._top_entity = None

        self.yang_name = "hostname"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-nto-misc-set-hostname"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('name', (YLeaf(YType.str, 'name'), ['str'])),
        ])
        self.name = None
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-nto-misc-set-hostname:hostname"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Hostname, ['name'], name, value)

    def clone_ptr(self):
        self._top_entity = Hostname()
        return self._top_entity

