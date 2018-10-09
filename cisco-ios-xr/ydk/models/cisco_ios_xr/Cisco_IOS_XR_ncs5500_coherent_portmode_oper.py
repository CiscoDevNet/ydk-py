""" Cisco_IOS_XR_ncs5500_coherent_portmode_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-coherent\-portmode package operational data.

This module contains definitions
for the following management objects\:
  controller\-port\-mode\: Coherent PortMode  operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ControllerPortMode(Entity):
    """
    Coherent PortMode  operational data
    
    .. attribute:: optics_name
    
    	Name of optics controller
    	**type**\: list of  		 :py:class:`OpticsName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_portmode_oper.ControllerPortMode.OpticsName>`
    
    

    """

    _prefix = 'ncs5500-coherent-portmode-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(ControllerPortMode, self).__init__()
        self._top_entity = None

        self.yang_name = "controller-port-mode"
        self.yang_parent_name = "Cisco-IOS-XR-ncs5500-coherent-portmode-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("optics-name", ("optics_name", ControllerPortMode.OpticsName))])
        self._leafs = OrderedDict()

        self.optics_name = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-ncs5500-coherent-portmode-oper:controller-port-mode"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ControllerPortMode, [], name, value)


    class OpticsName(Entity):
        """
        Name of optics controller
        
        .. attribute:: interface_name  (key)
        
        	Interface Name
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
        
        .. attribute:: port_mode_info
        
        	PortMode  operational data
        	**type**\:  :py:class:`PortModeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_portmode_oper.ControllerPortMode.OpticsName.PortModeInfo>`
        
        

        """

        _prefix = 'ncs5500-coherent-portmode-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ControllerPortMode.OpticsName, self).__init__()

            self.yang_name = "optics-name"
            self.yang_parent_name = "controller-port-mode"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['interface_name']
            self._child_classes = OrderedDict([("port-mode-info", ("port_mode_info", ControllerPortMode.OpticsName.PortModeInfo))])
            self._leafs = OrderedDict([
                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
            ])
            self.interface_name = None

            self.port_mode_info = ControllerPortMode.OpticsName.PortModeInfo()
            self.port_mode_info.parent = self
            self._children_name_map["port_mode_info"] = "port-mode-info"
            self._segment_path = lambda: "optics-name" + "[interface-name='" + str(self.interface_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-ncs5500-coherent-portmode-oper:controller-port-mode/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ControllerPortMode.OpticsName, ['interface_name'], name, value)


        class PortModeInfo(Entity):
            """
            PortMode  operational data
            
            .. attribute:: intf_name
            
            	intf name
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: speed
            
            	speed
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: fec
            
            	fec
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: diff
            
            	diff
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: modulation
            
            	modulation
            	**type**\: str
            
            	**length:** 0..128
            
            

            """

            _prefix = 'ncs5500-coherent-portmode-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ControllerPortMode.OpticsName.PortModeInfo, self).__init__()

                self.yang_name = "port-mode-info"
                self.yang_parent_name = "optics-name"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('intf_name', (YLeaf(YType.str, 'intf-name'), ['str'])),
                    ('speed', (YLeaf(YType.str, 'speed'), ['str'])),
                    ('fec', (YLeaf(YType.str, 'fec'), ['str'])),
                    ('diff', (YLeaf(YType.str, 'diff'), ['str'])),
                    ('modulation', (YLeaf(YType.str, 'modulation'), ['str'])),
                ])
                self.intf_name = None
                self.speed = None
                self.fec = None
                self.diff = None
                self.modulation = None
                self._segment_path = lambda: "port-mode-info"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ControllerPortMode.OpticsName.PortModeInfo, ['intf_name', 'speed', 'fec', 'diff', 'modulation'], name, value)

    def clone_ptr(self):
        self._top_entity = ControllerPortMode()
        return self._top_entity

