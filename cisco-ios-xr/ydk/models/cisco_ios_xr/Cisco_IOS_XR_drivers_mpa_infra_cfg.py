""" Cisco_IOS_XR_drivers_mpa_infra_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR drivers\-mpa\-infra package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\: Configure subslot h/w module

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class HwModuleShutdownPowerMode(Enum):
    """
    HwModuleShutdownPowerMode (Enum Class)

    Hw module shutdown power mode

    .. data:: powered = 2

    	Keep the showdown module powered (default)

    """

    powered = Enum.YLeaf(2, "powered")



class HardwareModule(Entity):
    """
    Configure subslot h/w module
    
    .. attribute:: nodes
    
    	 subslot h/w module
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_mpa_infra_cfg.HardwareModule.Nodes>`
    
    

    """

    _prefix = 'drivers-mpa-infra-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module"
        self.yang_parent_name = "Cisco-IOS-XR-drivers-mpa-infra-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", HardwareModule.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = HardwareModule.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-drivers-mpa-infra-cfg:hardware-module"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HardwareModule, [], name, value)


    class Nodes(Entity):
        """
         subslot h/w module
        
        .. attribute:: node
        
        	The identifier for a SPA node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_mpa_infra_cfg.HardwareModule.Nodes.Node>`
        
        

        """

        _prefix = 'drivers-mpa-infra-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModule.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "hardware-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", HardwareModule.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-drivers-mpa-infra-cfg:hardware-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModule.Nodes, [], name, value)


        class Node(Entity):
            """
            The identifier for a SPA node
            
            .. attribute:: node_name  (key)
            
            	A SPA node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: shutdown
            
            	Shutdown a subslot h/w module
            	**type**\:  :py:class:`HwModuleShutdownPowerMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_mpa_infra_cfg.HwModuleShutdownPowerMode>`
            
            

            """

            _prefix = 'drivers-mpa-infra-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModule.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                    ('shutdown', (YLeaf(YType.enumeration, 'shutdown'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_mpa_infra_cfg', 'HwModuleShutdownPowerMode', '')])),
                ])
                self.node_name = None
                self.shutdown = None
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-drivers-mpa-infra-cfg:hardware-module/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModule.Nodes.Node, ['node_name', 'shutdown'], name, value)

    def clone_ptr(self):
        self._top_entity = HardwareModule()
        return self._top_entity

