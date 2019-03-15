""" Cisco_IOS_XR_asr9k_lc_pwrglide_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-lc\-pwrglide package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\-port\-mode\: HW module port\-mode config

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class HardwareModulePortMode(Entity):
    """
    HW module port\-mode config
    
    .. attribute:: config_mode
    
    	Active or Pre configuration
    	**type**\: list of  		 :py:class:`ConfigMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_pwrglide_cfg.HardwareModulePortMode.ConfigMode>`
    
    

    """

    _prefix = 'asr9k-lc-pwrglide-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(HardwareModulePortMode, self).__init__()
        self._top_entity = None

        self.yang_name = "hardware-module-port-mode"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-lc-pwrglide-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("config-mode", ("config_mode", HardwareModulePortMode.ConfigMode))])
        self._leafs = OrderedDict()

        self.config_mode = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-lc-pwrglide-cfg:hardware-module-port-mode"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HardwareModulePortMode, [], name, value)


    class ConfigMode(Entity):
        """
        Active or Pre configuration
        
        .. attribute:: id1  (key)
        
        	act\- or pre\-config
        	**type**\: str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: node
        
        	A node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_pwrglide_cfg.HardwareModulePortMode.ConfigMode.Node>`
        
        

        """

        _prefix = 'asr9k-lc-pwrglide-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(HardwareModulePortMode.ConfigMode, self).__init__()

            self.yang_name = "config-mode"
            self.yang_parent_name = "hardware-module-port-mode"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['id1']
            self._child_classes = OrderedDict([("node", ("node", HardwareModulePortMode.ConfigMode.Node))])
            self._leafs = OrderedDict([
                ('id1', (YLeaf(YType.str, 'id1'), ['str'])),
            ])
            self.id1 = None

            self.node = YList(self)
            self._segment_path = lambda: "config-mode" + "[id1='" + str(self.id1) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-lc-pwrglide-cfg:hardware-module-port-mode/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HardwareModulePortMode.ConfigMode, ['id1'], name, value)


        class Node(Entity):
            """
            A node
            
            .. attribute:: id2  (key)
            
            	Fully qualified line card specification
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: port_mode
            
            	Linecard port\-mode
            	**type**\:  :py:class:`PortMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_pwrglide_cfg.HardwareModulePortMode.ConfigMode.Node.PortMode>`
            
            

            """

            _prefix = 'asr9k-lc-pwrglide-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(HardwareModulePortMode.ConfigMode.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "config-mode"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['id2']
                self._child_classes = OrderedDict([("port-mode", ("port_mode", HardwareModulePortMode.ConfigMode.Node.PortMode))])
                self._leafs = OrderedDict([
                    ('id2', (YLeaf(YType.str, 'id2'), ['str'])),
                ])
                self.id2 = None

                self.port_mode = HardwareModulePortMode.ConfigMode.Node.PortMode()
                self.port_mode.parent = self
                self._children_name_map["port_mode"] = "port-mode"
                self._segment_path = lambda: "node" + "[id2='" + str(self.id2) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HardwareModulePortMode.ConfigMode.Node, ['id2'], name, value)


            class PortMode(Entity):
                """
                Linecard port\-mode
                
                .. attribute:: if_port_mode
                
                	Linecard interface port\-mode
                	**type**\: str
                
                

                """

                _prefix = 'asr9k-lc-pwrglide-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(HardwareModulePortMode.ConfigMode.Node.PortMode, self).__init__()

                    self.yang_name = "port-mode"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('if_port_mode', (YLeaf(YType.str, 'if-port-mode'), ['str'])),
                    ])
                    self.if_port_mode = None
                    self._segment_path = lambda: "port-mode"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HardwareModulePortMode.ConfigMode.Node.PortMode, ['if_port_mode'], name, value)




    def clone_ptr(self):
        self._top_entity = HardwareModulePortMode()
        return self._top_entity



