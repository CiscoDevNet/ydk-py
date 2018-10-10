""" Cisco_IOS_XR_invmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR invmgr package configuration.

This module contains definitions
for the following management objects\:
  inventory\-configurations\: Configuration for inventory entities

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class InventoryConfigurations(Entity):
    """
    Configuration for inventory entities
    
    .. attribute:: entity_
    
    	Entity name
    	**type**\: list of  		 :py:class:`Entity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_invmgr_cfg.InventoryConfigurations.Entity>`
    
    

    """

    _prefix = 'invmgr-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(InventoryConfigurations, self).__init__()
        self._top_entity = None

        self.yang_name = "inventory-configurations"
        self.yang_parent_name = "Cisco-IOS-XR-invmgr-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("entity", ("entity_", InventoryConfigurations.Entity))])
        self._leafs = OrderedDict()

        self.entity_ = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-invmgr-cfg:inventory-configurations"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(InventoryConfigurations, [], name, value)


    class Entity(Entity):
        """
        Entity name
        
        .. attribute:: name  (key)
        
        	Entity name
        	**type**\: str
        
        .. attribute:: name_xr
        
        	Entity name
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'invmgr-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(InventoryConfigurations.Entity, self).__init__()

            self.yang_name = "entity"
            self.yang_parent_name = "inventory-configurations"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('name_xr', (YLeaf(YType.str, 'name-xr'), ['str'])),
            ])
            self.name = None
            self.name_xr = None
            self._segment_path = lambda: "entity" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-invmgr-cfg:inventory-configurations/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InventoryConfigurations.Entity, ['name', 'name_xr'], name, value)

    def clone_ptr(self):
        self._top_entity = InventoryConfigurations()
        return self._top_entity

