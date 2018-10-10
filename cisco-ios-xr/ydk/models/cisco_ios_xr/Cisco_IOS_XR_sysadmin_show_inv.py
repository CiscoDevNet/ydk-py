""" Cisco_IOS_XR_sysadmin_show_inv 

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

Calvados Inventory Service maintain entity database

Copyright(c) 2011\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Inventory(Entity):
    """
    show inventory
    
    .. attribute:: location
    
    	
    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_inv.Inventory.Location>`
    
    .. attribute:: all
    
    	
    	**type**\: list of  		 :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_inv.Inventory.All>`
    
    .. attribute:: chassis
    
    	
    	**type**\: list of  		 :py:class:`Chassis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_inv.Inventory.Chassis>`
    
    .. attribute:: power
    
    	
    	**type**\: list of  		 :py:class:`Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_inv.Inventory.Power>`
    
    .. attribute:: fan
    
    	
    	**type**\: list of  		 :py:class:`Fan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_inv.Inventory.Fan>`
    
    .. attribute:: raw
    
    	
    	**type**\: list of  		 :py:class:`Raw <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_inv.Inventory.Raw>`
    
    

    """

    _prefix = 'inv'
    _revision = '2017-04-12'

    def __init__(self):
        super(Inventory, self).__init__()
        self._top_entity = None

        self.yang_name = "inventory"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-show-inv"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("location", ("location", Inventory.Location)), ("all", ("all", Inventory.All)), ("chassis", ("chassis", Inventory.Chassis)), ("power", ("power", Inventory.Power)), ("fan", ("fan", Inventory.Fan)), ("raw", ("raw", Inventory.Raw))])
        self._leafs = OrderedDict()

        self.location = YList(self)
        self.all = YList(self)
        self.chassis = YList(self)
        self.power = YList(self)
        self.fan = YList(self)
        self.raw = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-show-inv:inventory"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Inventory, [], name, value)


    class Location(Entity):
        """
        
        
        .. attribute:: loc  (key)
        
        	Node id of the entity
        	**type**\: str
        
        .. attribute:: name
        
        	Name of the entity
        	**type**\: str
        
        .. attribute:: description
        
        	Description of the entity
        	**type**\: str
        
        .. attribute:: pid
        
        	Product ID of the entity
        	**type**\: str
        
        .. attribute:: vid
        
        	Version ID of the entity
        	**type**\: str
        
        .. attribute:: sn
        
        	Serial Numbe of the entity
        	**type**\: str
        
        .. attribute:: index
        
        	Index for the entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'inv'
        _revision = '2017-04-12'

        def __init__(self):
            super(Inventory.Location, self).__init__()

            self.yang_name = "location"
            self.yang_parent_name = "inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['loc']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('loc', (YLeaf(YType.str, 'loc'), ['str'])),
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('description', (YLeaf(YType.str, 'Description'), ['str'])),
                ('pid', (YLeaf(YType.str, 'PID'), ['str'])),
                ('vid', (YLeaf(YType.str, 'VID'), ['str'])),
                ('sn', (YLeaf(YType.str, 'SN'), ['str'])),
                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
            ])
            self.loc = None
            self.name = None
            self.description = None
            self.pid = None
            self.vid = None
            self.sn = None
            self.index = None
            self._segment_path = lambda: "location" + "[loc='" + str(self.loc) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-inv:inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Inventory.Location, ['loc', 'name', 'description', 'pid', 'vid', 'sn', 'index'], name, value)


    class All(Entity):
        """
        
        
        .. attribute:: index  (key)
        
        	Index for the entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: name
        
        	Name of the entity
        	**type**\: str
        
        .. attribute:: description
        
        	Description of the entity
        	**type**\: str
        
        .. attribute:: pid
        
        	Product ID of the entity
        	**type**\: str
        
        .. attribute:: vid
        
        	Version ID of the entity
        	**type**\: str
        
        .. attribute:: sn
        
        	Serial Numbe of the entity
        	**type**\: str
        
        .. attribute:: loc
        
        	Node id of the entity
        	**type**\: str
        
        

        """

        _prefix = 'inv'
        _revision = '2017-04-12'

        def __init__(self):
            super(Inventory.All, self).__init__()

            self.yang_name = "all"
            self.yang_parent_name = "inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['index']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('description', (YLeaf(YType.str, 'Description'), ['str'])),
                ('pid', (YLeaf(YType.str, 'PID'), ['str'])),
                ('vid', (YLeaf(YType.str, 'VID'), ['str'])),
                ('sn', (YLeaf(YType.str, 'SN'), ['str'])),
                ('loc', (YLeaf(YType.str, 'loc'), ['str'])),
            ])
            self.index = None
            self.name = None
            self.description = None
            self.pid = None
            self.vid = None
            self.sn = None
            self.loc = None
            self._segment_path = lambda: "all" + "[index='" + str(self.index) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-inv:inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Inventory.All, ['index', 'name', 'description', 'pid', 'vid', 'sn', 'loc'], name, value)


    class Chassis(Entity):
        """
        
        
        .. attribute:: index  (key)
        
        	Index for the entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: name
        
        	Name of the entity
        	**type**\: str
        
        .. attribute:: description
        
        	Description of the entity
        	**type**\: str
        
        .. attribute:: pid
        
        	Product ID of the entity
        	**type**\: str
        
        .. attribute:: vid
        
        	Version ID of the entity
        	**type**\: str
        
        .. attribute:: sn
        
        	Serial Numbe of the entity
        	**type**\: str
        
        .. attribute:: loc
        
        	Node id of the entity
        	**type**\: str
        
        

        """

        _prefix = 'inv'
        _revision = '2017-04-12'

        def __init__(self):
            super(Inventory.Chassis, self).__init__()

            self.yang_name = "chassis"
            self.yang_parent_name = "inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['index']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('description', (YLeaf(YType.str, 'Description'), ['str'])),
                ('pid', (YLeaf(YType.str, 'PID'), ['str'])),
                ('vid', (YLeaf(YType.str, 'VID'), ['str'])),
                ('sn', (YLeaf(YType.str, 'SN'), ['str'])),
                ('loc', (YLeaf(YType.str, 'loc'), ['str'])),
            ])
            self.index = None
            self.name = None
            self.description = None
            self.pid = None
            self.vid = None
            self.sn = None
            self.loc = None
            self._segment_path = lambda: "chassis" + "[index='" + str(self.index) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-inv:inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Inventory.Chassis, ['index', 'name', 'description', 'pid', 'vid', 'sn', 'loc'], name, value)


    class Power(Entity):
        """
        
        
        .. attribute:: index  (key)
        
        	Index for the entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: name
        
        	Name of the entity
        	**type**\: str
        
        .. attribute:: description
        
        	Description of the entity
        	**type**\: str
        
        .. attribute:: pid
        
        	Product ID of the entity
        	**type**\: str
        
        .. attribute:: vid
        
        	Version ID of the entity
        	**type**\: str
        
        .. attribute:: sn
        
        	Serial Numbe of the entity
        	**type**\: str
        
        .. attribute:: loc
        
        	Node id of the entity
        	**type**\: str
        
        

        """

        _prefix = 'inv'
        _revision = '2017-04-12'

        def __init__(self):
            super(Inventory.Power, self).__init__()

            self.yang_name = "power"
            self.yang_parent_name = "inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['index']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('description', (YLeaf(YType.str, 'Description'), ['str'])),
                ('pid', (YLeaf(YType.str, 'PID'), ['str'])),
                ('vid', (YLeaf(YType.str, 'VID'), ['str'])),
                ('sn', (YLeaf(YType.str, 'SN'), ['str'])),
                ('loc', (YLeaf(YType.str, 'loc'), ['str'])),
            ])
            self.index = None
            self.name = None
            self.description = None
            self.pid = None
            self.vid = None
            self.sn = None
            self.loc = None
            self._segment_path = lambda: "power" + "[index='" + str(self.index) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-inv:inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Inventory.Power, ['index', 'name', 'description', 'pid', 'vid', 'sn', 'loc'], name, value)


    class Fan(Entity):
        """
        
        
        .. attribute:: index  (key)
        
        	Index for the entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: name
        
        	Name of the entity
        	**type**\: str
        
        .. attribute:: description
        
        	Description of the entity
        	**type**\: str
        
        .. attribute:: pid
        
        	Product ID of the entity
        	**type**\: str
        
        .. attribute:: vid
        
        	Version ID of the entity
        	**type**\: str
        
        .. attribute:: sn
        
        	Serial Numbe of the entity
        	**type**\: str
        
        .. attribute:: loc
        
        	Node id of the entity
        	**type**\: str
        
        

        """

        _prefix = 'inv'
        _revision = '2017-04-12'

        def __init__(self):
            super(Inventory.Fan, self).__init__()

            self.yang_name = "fan"
            self.yang_parent_name = "inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['index']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('description', (YLeaf(YType.str, 'Description'), ['str'])),
                ('pid', (YLeaf(YType.str, 'PID'), ['str'])),
                ('vid', (YLeaf(YType.str, 'VID'), ['str'])),
                ('sn', (YLeaf(YType.str, 'SN'), ['str'])),
                ('loc', (YLeaf(YType.str, 'loc'), ['str'])),
            ])
            self.index = None
            self.name = None
            self.description = None
            self.pid = None
            self.vid = None
            self.sn = None
            self.loc = None
            self._segment_path = lambda: "fan" + "[index='" + str(self.index) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-inv:inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Inventory.Fan, ['index', 'name', 'description', 'pid', 'vid', 'sn', 'loc'], name, value)


    class Raw(Entity):
        """
        
        
        .. attribute:: index  (key)
        
        	Index for the entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: name
        
        	Name of the entity
        	**type**\: str
        
        .. attribute:: description
        
        	Description of the entity
        	**type**\: str
        
        .. attribute:: pid
        
        	Product ID of the entity
        	**type**\: str
        
        .. attribute:: vid
        
        	Version ID of the entity
        	**type**\: str
        
        .. attribute:: sn
        
        	Serial Numbe of the entity
        	**type**\: str
        
        .. attribute:: loc
        
        	Node id of the entity
        	**type**\: str
        
        

        """

        _prefix = 'inv'
        _revision = '2017-04-12'

        def __init__(self):
            super(Inventory.Raw, self).__init__()

            self.yang_name = "raw"
            self.yang_parent_name = "inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['index']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('description', (YLeaf(YType.str, 'Description'), ['str'])),
                ('pid', (YLeaf(YType.str, 'PID'), ['str'])),
                ('vid', (YLeaf(YType.str, 'VID'), ['str'])),
                ('sn', (YLeaf(YType.str, 'SN'), ['str'])),
                ('loc', (YLeaf(YType.str, 'loc'), ['str'])),
            ])
            self.index = None
            self.name = None
            self.description = None
            self.pid = None
            self.vid = None
            self.sn = None
            self.loc = None
            self._segment_path = lambda: "raw" + "[index='" + str(self.index) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-inv:inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Inventory.Raw, ['index', 'name', 'description', 'pid', 'vid', 'sn', 'loc'], name, value)

    def clone_ptr(self):
        self._top_entity = Inventory()
        return self._top_entity

