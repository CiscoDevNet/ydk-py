""" Cisco_IOS_XR_invmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR invmgr package configuration.

This module contains definitions
for the following management objects\:
  inventory\-configurations\: Configuration for inventory entities

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class InventoryConfigurations(object):
    """
    Configuration for inventory entities
    
    .. attribute:: entity
    
    	Entity name
    	**type**\: list of    :py:class:`Entity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_invmgr_cfg.InventoryConfigurations.Entity>`
    
    

    """

    _prefix = 'invmgr-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.entity = YList()
        self.entity.parent = self
        self.entity.name = 'entity'


    class Entity(object):
        """
        Entity name
        
        .. attribute:: name  <key>
        
        	Entity name
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: name_xr
        
        	Entity name
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'invmgr-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.name = None
            self.name_xr = None

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/Cisco-IOS-XR-invmgr-cfg:inventory-configurations/Cisco-IOS-XR-invmgr-cfg:entity[Cisco-IOS-XR-invmgr-cfg:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.name is not None:
                return True

            if self.name_xr is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_invmgr_cfg as meta
            return meta._meta_table['InventoryConfigurations.Entity']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-invmgr-cfg:inventory-configurations'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.entity is not None:
            for child_ref in self.entity:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_invmgr_cfg as meta
        return meta._meta_table['InventoryConfigurations']['meta_info']


