""" Cisco_IOS_XR_tty_vty_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-vty package configuration.

This module contains definitions
for the following management objects\:
  vty\: VTY Pools configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Vty(Entity):
    """
    VTY Pools configuration
    
    .. attribute:: vty_pools
    
    	List of VTY Pools
    	**type**\:  :py:class:`VtyPools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_vty_cfg.Vty.VtyPools>`
    
    

    """

    _prefix = 'tty-vty-cfg'
    _revision = '2017-09-07'

    def __init__(self):
        super(Vty, self).__init__()
        self._top_entity = None

        self.yang_name = "vty"
        self.yang_parent_name = "Cisco-IOS-XR-tty-vty-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vty-pools", ("vty_pools", Vty.VtyPools))])
        self._leafs = OrderedDict()

        self.vty_pools = Vty.VtyPools()
        self.vty_pools.parent = self
        self._children_name_map["vty_pools"] = "vty-pools"
        self._segment_path = lambda: "Cisco-IOS-XR-tty-vty-cfg:vty"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Vty, [], name, value)


    class VtyPools(Entity):
        """
        List of VTY Pools
        
        .. attribute:: vty_pool
        
        	VTY Pool
        	**type**\: list of  		 :py:class:`VtyPool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_vty_cfg.Vty.VtyPools.VtyPool>`
        
        

        """

        _prefix = 'tty-vty-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Vty.VtyPools, self).__init__()

            self.yang_name = "vty-pools"
            self.yang_parent_name = "vty"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vty-pool", ("vty_pool", Vty.VtyPools.VtyPool))])
            self._leafs = OrderedDict()

            self.vty_pool = YList(self)
            self._segment_path = lambda: "vty-pools"
            self._absolute_path = lambda: "Cisco-IOS-XR-tty-vty-cfg:vty/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vty.VtyPools, [], name, value)


        class VtyPool(Entity):
            """
            VTY Pool
            
            .. attribute:: pool_name  (key)
            
            	For configuring range for default pool use 'default',For configuring range for fault\-manager pool use 'fm',For configuring range for any user defined pool use any other string
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: first_vty
            
            	First VTY number,For default VTY use 0,For user\-defined use 5,For fault\-manager use 100
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            .. attribute:: last_vty
            
            	Last VTY number,For default configure between 0\-99,For user\-defined configure between 5\-99 ,For fault\-manager configure between 100\-199
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            .. attribute:: line_template
            
            	Name of line template
            	**type**\: str
            
            .. attribute:: none
            
            	Empty Option
            	**type**\: str
            
            

            """

            _prefix = 'tty-vty-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Vty.VtyPools.VtyPool, self).__init__()

                self.yang_name = "vty-pool"
                self.yang_parent_name = "vty-pools"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['pool_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('pool_name', (YLeaf(YType.str, 'pool-name'), ['str'])),
                    ('first_vty', (YLeaf(YType.uint32, 'first-vty'), ['int'])),
                    ('last_vty', (YLeaf(YType.uint32, 'last-vty'), ['int'])),
                    ('line_template', (YLeaf(YType.str, 'line-template'), ['str'])),
                    ('none', (YLeaf(YType.str, 'none'), ['str'])),
                ])
                self.pool_name = None
                self.first_vty = None
                self.last_vty = None
                self.line_template = None
                self.none = None
                self._segment_path = lambda: "vty-pool" + "[pool-name='" + str(self.pool_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tty-vty-cfg:vty/vty-pools/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vty.VtyPools.VtyPool, ['pool_name', 'first_vty', 'last_vty', 'line_template', 'none'], name, value)

    def clone_ptr(self):
        self._top_entity = Vty()
        return self._top_entity

