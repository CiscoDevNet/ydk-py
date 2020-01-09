""" Cisco_IOS_XR_asr9k_ep_port_mode_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-ep\-port\-mode package configuration.

This module contains definitions
for the following management objects\:
  hw\-module\-ep\-port\-mode\: HW Module EP port\-mode configuration

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



class HwModuleEpIfPortMode(Enum):
    """
    HwModuleEpIfPortMode (Enum Class)

    Hw module ep if port mode

    .. data:: Y_2xhundredgige_16qam = 1

    	2xHundredGigE 16QAM mode configuration

    .. data:: Y_2xhundredgige_8qam = 2

    	2xHundredGigE 8QAM mode configuration

    """

    Y_2xhundredgige_16qam = Enum.YLeaf(1, "2xhundredgige-16qam")

    Y_2xhundredgige_8qam = Enum.YLeaf(2, "2xhundredgige-8qam")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_ep_port_mode_cfg as meta
        return meta._meta_table['HwModuleEpIfPortMode']



class HwModuleEpPortMode(_Entity_):
    """
    HW Module EP port\-mode configuration
    
    .. attribute:: ep_port_mode_configuration
    
    	active or pre configuration
    	**type**\: list of  		 :py:class:`EpPortModeConfiguration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg.HwModuleEpPortMode.EpPortModeConfiguration>`
    
    

    """

    _prefix = 'asr9k-ep-port-mode-cfg'
    _revision = '2019-01-06'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(HwModuleEpPortMode, self).__init__()
        self._top_entity = None

        self.yang_name = "hw-module-ep-port-mode"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-ep-port-mode-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ep-port-mode-configuration", ("ep_port_mode_configuration", HwModuleEpPortMode.EpPortModeConfiguration))])
        self._leafs = OrderedDict()

        self.ep_port_mode_configuration = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-ep-port-mode-cfg:hw-module-ep-port-mode"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HwModuleEpPortMode, [], name, value)


    class EpPortModeConfiguration(_Entity_):
        """
        active or pre configuration
        
        .. attribute:: active  (key)
        
        	act or pre configuration
        	**type**\: str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: node
        
        	line\-card node location
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg.HwModuleEpPortMode.EpPortModeConfiguration.Node>`
        
        

        """

        _prefix = 'asr9k-ep-port-mode-cfg'
        _revision = '2019-01-06'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(HwModuleEpPortMode.EpPortModeConfiguration, self).__init__()

            self.yang_name = "ep-port-mode-configuration"
            self.yang_parent_name = "hw-module-ep-port-mode"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['active']
            self._child_classes = OrderedDict([("node", ("node", HwModuleEpPortMode.EpPortModeConfiguration.Node))])
            self._leafs = OrderedDict([
                ('active', (YLeaf(YType.str, 'active'), ['str'])),
            ])
            self.active = None

            self.node = YList(self)
            self._segment_path = lambda: "ep-port-mode-configuration" + "[active='" + str(self.active) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-ep-port-mode-cfg:hw-module-ep-port-mode/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModuleEpPortMode.EpPortModeConfiguration, ['active'], name, value)


        class Node(_Entity_):
            """
            line\-card node location
            
            .. attribute:: location  (key)
            
            	Fully qualified line\-card location
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: bays
            
            	port\-mode configuration for EP bay number
            	**type**\:  :py:class:`Bays <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg.HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays>`
            
            

            """

            _prefix = 'asr9k-ep-port-mode-cfg'
            _revision = '2019-01-06'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(HwModuleEpPortMode.EpPortModeConfiguration.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "ep-port-mode-configuration"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['location']
                self._child_classes = OrderedDict([("bays", ("bays", HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays))])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ])
                self.location = None

                self.bays = HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays()
                self.bays.parent = self
                self._children_name_map["bays"] = "bays"
                self._segment_path = lambda: "node" + "[location='" + str(self.location) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleEpPortMode.EpPortModeConfiguration.Node, ['location'], name, value)


            class Bays(_Entity_):
                """
                port\-mode configuration for EP bay number
                
                .. attribute:: bay
                
                	EP Bay number
                	**type**\: list of  		 :py:class:`Bay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg.HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay>`
                
                

                """

                _prefix = 'asr9k-ep-port-mode-cfg'
                _revision = '2019-01-06'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays, self).__init__()

                    self.yang_name = "bays"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bay", ("bay", HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay))])
                    self._leafs = OrderedDict()

                    self.bay = YList(self)
                    self._segment_path = lambda: "bays"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays, [], name, value)


                class Bay(_Entity_):
                    """
                    EP Bay number
                    
                    .. attribute:: bay_number  (key)
                    
                    	bay number
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: ports
                    
                    	port\-mode configuration for port number
                    	**type**\:  :py:class:`Ports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg.HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports>`
                    
                    

                    """

                    _prefix = 'asr9k-ep-port-mode-cfg'
                    _revision = '2019-01-06'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay, self).__init__()

                        self.yang_name = "bay"
                        self.yang_parent_name = "bays"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['bay_number']
                        self._child_classes = OrderedDict([("ports", ("ports", HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports))])
                        self._leafs = OrderedDict([
                            ('bay_number', (YLeaf(YType.str, 'bay-number'), ['str'])),
                        ])
                        self.bay_number = None

                        self.ports = HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports()
                        self.ports.parent = self
                        self._children_name_map["ports"] = "ports"
                        self._segment_path = lambda: "bay" + "[bay-number='" + str(self.bay_number) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay, ['bay_number'], name, value)


                    class Ports(_Entity_):
                        """
                        port\-mode configuration for port number
                        
                        .. attribute:: port
                        
                        	Optics port number
                        	**type**\: list of  		 :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg.HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports.Port>`
                        
                        

                        """

                        _prefix = 'asr9k-ep-port-mode-cfg'
                        _revision = '2019-01-06'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports, self).__init__()

                            self.yang_name = "ports"
                            self.yang_parent_name = "bay"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("port", ("port", HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports.Port))])
                            self._leafs = OrderedDict()

                            self.port = YList(self)
                            self._segment_path = lambda: "ports"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports, [], name, value)


                        class Port(_Entity_):
                            """
                            Optics port number
                            
                            .. attribute:: port_number  (key)
                            
                            	Optics port number
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: if_port_mode
                            
                            	port\-mode type
                            	**type**\:  :py:class:`HwModuleEpIfPortMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg.HwModuleEpIfPortMode>`
                            
                            

                            """

                            _prefix = 'asr9k-ep-port-mode-cfg'
                            _revision = '2019-01-06'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports.Port, self).__init__()

                                self.yang_name = "port"
                                self.yang_parent_name = "ports"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['port_number']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('port_number', (YLeaf(YType.str, 'port-number'), ['str'])),
                                    ('if_port_mode', (YLeaf(YType.enumeration, 'if-port-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_ep_port_mode_cfg', 'HwModuleEpIfPortMode', '')])),
                                ])
                                self.port_number = None
                                self.if_port_mode = None
                                self._segment_path = lambda: "port" + "[port-number='" + str(self.port_number) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports.Port, ['port_number', 'if_port_mode'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_ep_port_mode_cfg as meta
                                return meta._meta_table['HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports.Port']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_ep_port_mode_cfg as meta
                            return meta._meta_table['HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay.Ports']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_ep_port_mode_cfg as meta
                        return meta._meta_table['HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays.Bay']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_ep_port_mode_cfg as meta
                    return meta._meta_table['HwModuleEpPortMode.EpPortModeConfiguration.Node.Bays']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_ep_port_mode_cfg as meta
                return meta._meta_table['HwModuleEpPortMode.EpPortModeConfiguration.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_ep_port_mode_cfg as meta
            return meta._meta_table['HwModuleEpPortMode.EpPortModeConfiguration']['meta_info']

    def clone_ptr(self):
        self._top_entity = HwModuleEpPortMode()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_ep_port_mode_cfg as meta
        return meta._meta_table['HwModuleEpPortMode']['meta_info']


