""" Cisco_IOS_XR_drivers_vpa_infra_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR drivers\-vpa\-infra package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\: Configure subslot h/w module

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



class HwModuleShutdownPowerMode(Enum):
    """
    HwModuleShutdownPowerMode (Enum Class)

    Hw module shutdown power mode

    .. data:: unpowered = 1

    	Keep the showdown module unpowered

    .. data:: powered = 2

    	Keep the showdown module powered (default)

    """

    unpowered = Enum.YLeaf(1, "unpowered")

    powered = Enum.YLeaf(2, "powered")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_vpa_infra_cfg as meta
        return meta._meta_table['HwModuleShutdownPowerMode']


class HwModuleSpaPhysicalInterface(Enum):
    """
    HwModuleSpaPhysicalInterface (Enum Class)

    Hw module spa physical interface

    .. data:: t3 = 1

    	T3 interface type(default)

    .. data:: e3 = 2

    	E3 interface type

    .. data:: t1 = 3

    	T1 interface type

    .. data:: e1 = 4

    	E1 interface type

    .. data:: sonet = 5

    	Sonet interface type

    .. data:: sdh = 6

    	SDH interface type

    """

    t3 = Enum.YLeaf(1, "t3")

    e3 = Enum.YLeaf(2, "e3")

    t1 = Enum.YLeaf(3, "t1")

    e1 = Enum.YLeaf(4, "e1")

    sonet = Enum.YLeaf(5, "sonet")

    sdh = Enum.YLeaf(6, "sdh")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_vpa_infra_cfg as meta
        return meta._meta_table['HwModuleSpaPhysicalInterface']


class HwModuleSpaPhysicalMode(Enum):
    """
    HwModuleSpaPhysicalMode (Enum Class)

    Hw module spa physical mode

    .. data:: cem = 1

    	CEM mode type

    """

    cem = Enum.YLeaf(1, "cem")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_vpa_infra_cfg as meta
        return meta._meta_table['HwModuleSpaPhysicalMode']



class HardwareModule(_Entity_):
    """
    Configure subslot h/w module
    
    .. attribute:: logging
    
    	Logging configuration
    	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_vpa_infra_cfg.HardwareModule.Logging>`
    
    .. attribute:: nodes
    
    	 subslot h/w module
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_vpa_infra_cfg.HardwareModule.Nodes>`
    
    

    """

    _prefix = 'drivers-vpa-infra-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(HardwareModule, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module"
        self.yang_parent_name = "Cisco-IOS-XR-drivers-vpa-infra-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("logging", ("logging", HardwareModule.Logging)), ("nodes", ("nodes", HardwareModule.Nodes))])
        self._leafs = OrderedDict()

        self.logging = HardwareModule.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"

        self.nodes = HardwareModule.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-drivers-vpa-infra-cfg:hardware-module"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HardwareModule, [], name, value)


    class Logging(_Entity_):
        """
        Logging configuration
        
        

        """

        _prefix = 'drivers-vpa-infra-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(HardwareModule.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "hardware-module"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict()
            self._segment_path = lambda: "logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-drivers-vpa-infra-cfg:hardware-module/%s" % self._segment_path()
            self._is_frozen = True

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_vpa_infra_cfg as meta
            return meta._meta_table['HardwareModule.Logging']['meta_info']


    class Nodes(_Entity_):
        """
         subslot h/w module
        
        .. attribute:: node
        
        	The identifier for a SPA node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_vpa_infra_cfg.HardwareModule.Nodes.Node>`
        
        

        """

        _prefix = 'drivers-vpa-infra-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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
            self._absolute_path = lambda: "Cisco-IOS-XR-drivers-vpa-infra-cfg:hardware-module/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModule.Nodes, [], name, value)


        class Node(_Entity_):
            """
            The identifier for a SPA node
            
            .. attribute:: node_name  (key)
            
            	A SPA node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: card_type
            
            	Configure the SPA physical interface type
            	**type**\:  :py:class:`HwModuleSpaPhysicalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_vpa_infra_cfg.HwModuleSpaPhysicalInterface>`
            
            .. attribute:: mode
            
            	Configure the SPA mode
            	**type**\:  :py:class:`HwModuleSpaPhysicalMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_vpa_infra_cfg.HwModuleSpaPhysicalMode>`
            
            .. attribute:: shutdown
            
            	Shutdown a subslot h/w module
            	**type**\:  :py:class:`HwModuleShutdownPowerMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_vpa_infra_cfg.HwModuleShutdownPowerMode>`
            
            

            """

            _prefix = 'drivers-vpa-infra-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(HardwareModule.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                    ('card_type', (YLeaf(YType.enumeration, 'card-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_vpa_infra_cfg', 'HwModuleSpaPhysicalInterface', '')])),
                    ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_vpa_infra_cfg', 'HwModuleSpaPhysicalMode', '')])),
                    ('shutdown', (YLeaf(YType.enumeration, 'shutdown'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_vpa_infra_cfg', 'HwModuleShutdownPowerMode', '')])),
                ])
                self.node_name = None
                self.card_type = None
                self.mode = None
                self.shutdown = None
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-drivers-vpa-infra-cfg:hardware-module/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModule.Nodes.Node, ['node_name', 'card_type', 'mode', 'shutdown'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_vpa_infra_cfg as meta
                return meta._meta_table['HardwareModule.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_vpa_infra_cfg as meta
            return meta._meta_table['HardwareModule.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = HardwareModule()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_vpa_infra_cfg as meta
        return meta._meta_table['HardwareModule']['meta_info']


