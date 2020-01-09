""" Cisco_IOS_XR_rgmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR rgmgr package operational data.

This module contains definitions
for the following management objects\:
  redundancy\-group\-manager\: Redundancy group manager operational
    data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class RedundancyGroupManager(_Entity_):
    """
    Redundancy group manager operational data
    
    .. attribute:: controllers
    
    	Redundancy group manager data
    	**type**\:  :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper.RedundancyGroupManager.Controllers>`
    
    	**config**\: False
    
    

    """

    _prefix = 'rgmgr-oper'
    _revision = '2015-01-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(RedundancyGroupManager, self).__init__()
        self._top_entity = None

        self.yang_name = "redundancy-group-manager"
        self.yang_parent_name = "Cisco-IOS-XR-rgmgr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("controllers", ("controllers", RedundancyGroupManager.Controllers))])
        self._leafs = OrderedDict()

        self.controllers = RedundancyGroupManager.Controllers()
        self.controllers.parent = self
        self._children_name_map["controllers"] = "controllers"
        self._segment_path = lambda: "Cisco-IOS-XR-rgmgr-oper:redundancy-group-manager"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(RedundancyGroupManager, [], name, value)


    class Controllers(_Entity_):
        """
        Redundancy group manager data
        
        .. attribute:: controller
        
        	Display redundancy group by controller name
        	**type**\: list of  		 :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_rgmgr_oper.RedundancyGroupManager.Controllers.Controller>`
        
        	**config**\: False
        
        

        """

        _prefix = 'rgmgr-oper'
        _revision = '2015-01-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(RedundancyGroupManager.Controllers, self).__init__()

            self.yang_name = "controllers"
            self.yang_parent_name = "redundancy-group-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("controller", ("controller", RedundancyGroupManager.Controllers.Controller))])
            self._leafs = OrderedDict()

            self.controller = YList(self)
            self._segment_path = lambda: "controllers"
            self._absolute_path = lambda: "Cisco-IOS-XR-rgmgr-oper:redundancy-group-manager/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RedundancyGroupManager.Controllers, [], name, value)


        class Controller(_Entity_):
            """
            Display redundancy group by controller name
            
            .. attribute:: controller_name  (key)
            
            	Controller name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: multi_router_aps_group_number
            
            	Configured interchassis redundancy group number
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: controller_name_xr
            
            	Name of controller being backed up
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: controller_handle
            
            	Handle of controller being backed up
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: backup_interface_name
            
            	Backup interface name
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: backup_interface_handle
            
            	Backup interface handle
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: backup_interface_next_hop_ip_address
            
            	Backup interface next hop IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: inter_chassis_group_state
            
            	Configured interchassis redundancy group state
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            

            """

            _prefix = 'rgmgr-oper'
            _revision = '2015-01-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(RedundancyGroupManager.Controllers.Controller, self).__init__()

                self.yang_name = "controller"
                self.yang_parent_name = "controllers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['controller_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('controller_name', (YLeaf(YType.str, 'controller-name'), ['str'])),
                    ('multi_router_aps_group_number', (YLeaf(YType.str, 'multi-router-aps-group-number'), ['str'])),
                    ('controller_name_xr', (YLeaf(YType.str, 'controller-name-xr'), ['str'])),
                    ('controller_handle', (YLeaf(YType.str, 'controller-handle'), ['str'])),
                    ('backup_interface_name', (YLeaf(YType.str, 'backup-interface-name'), ['str'])),
                    ('backup_interface_handle', (YLeaf(YType.str, 'backup-interface-handle'), ['str'])),
                    ('backup_interface_next_hop_ip_address', (YLeaf(YType.str, 'backup-interface-next-hop-ip-address'), ['str'])),
                    ('inter_chassis_group_state', (YLeaf(YType.str, 'inter-chassis-group-state'), ['str'])),
                ])
                self.controller_name = None
                self.multi_router_aps_group_number = None
                self.controller_name_xr = None
                self.controller_handle = None
                self.backup_interface_name = None
                self.backup_interface_handle = None
                self.backup_interface_next_hop_ip_address = None
                self.inter_chassis_group_state = None
                self._segment_path = lambda: "controller" + "[controller-name='" + str(self.controller_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-rgmgr-oper:redundancy-group-manager/controllers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RedundancyGroupManager.Controllers.Controller, ['controller_name', 'multi_router_aps_group_number', 'controller_name_xr', 'controller_handle', 'backup_interface_name', 'backup_interface_handle', 'backup_interface_next_hop_ip_address', 'inter_chassis_group_state'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_oper as meta
                return meta._meta_table['RedundancyGroupManager.Controllers.Controller']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_oper as meta
            return meta._meta_table['RedundancyGroupManager.Controllers']['meta_info']

    def clone_ptr(self):
        self._top_entity = RedundancyGroupManager()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_rgmgr_oper as meta
        return meta._meta_table['RedundancyGroupManager']['meta_info']


