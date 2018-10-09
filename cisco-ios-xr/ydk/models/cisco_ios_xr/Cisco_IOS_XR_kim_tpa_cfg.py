""" Cisco_IOS_XR_kim_tpa_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR kim\-tpa package configuration.

This module contains definitions
for the following management objects\:
  tpa\: tpa configuration commands

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Tpa(Entity):
    """
    tpa configuration commands
    
    .. attribute:: vrf_names
    
    	VRF container
    	**type**\:  :py:class:`VrfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames>`
    
    .. attribute:: logging
    
    	Third party app logging
    	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.Logging>`
    
    .. attribute:: statistics
    
    	Statistics
    	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.Statistics>`
    
    

    """

    _prefix = 'kim-tpa-cfg'
    _revision = '2017-09-07'

    def __init__(self):
        super(Tpa, self).__init__()
        self._top_entity = None

        self.yang_name = "tpa"
        self.yang_parent_name = "Cisco-IOS-XR-kim-tpa-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrf-names", ("vrf_names", Tpa.VrfNames)), ("logging", ("logging", Tpa.Logging)), ("statistics", ("statistics", Tpa.Statistics))])
        self._leafs = OrderedDict()

        self.vrf_names = Tpa.VrfNames()
        self.vrf_names.parent = self
        self._children_name_map["vrf_names"] = "vrf-names"

        self.logging = Tpa.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"

        self.statistics = Tpa.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"
        self._segment_path = lambda: "Cisco-IOS-XR-kim-tpa-cfg:tpa"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Tpa, [], name, value)


    class VrfNames(Entity):
        """
        VRF container
        
        .. attribute:: vrf_name
        
        	VRF name
        	**type**\: list of  		 :py:class:`VrfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName>`
        
        

        """

        _prefix = 'kim-tpa-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Tpa.VrfNames, self).__init__()

            self.yang_name = "vrf-names"
            self.yang_parent_name = "tpa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf-name", ("vrf_name", Tpa.VrfNames.VrfName))])
            self._leafs = OrderedDict()

            self.vrf_name = YList(self)
            self._segment_path = lambda: "vrf-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-kim-tpa-cfg:tpa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Tpa.VrfNames, [], name, value)


        class VrfName(Entity):
            """
            VRF name
            
            .. attribute:: vrf_name  (key)
            
            	VRF name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: east_west_names
            
            	EastWest container
            	**type**\:  :py:class:`EastWestNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.EastWestNames>`
            
            .. attribute:: address_family
            
            	Address family
            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.AddressFamily>`
            
            .. attribute:: disable
            
            	Disable routes and interfaces
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'kim-tpa-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Tpa.VrfNames.VrfName, self).__init__()

                self.yang_name = "vrf-name"
                self.yang_parent_name = "vrf-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("east-west-names", ("east_west_names", Tpa.VrfNames.VrfName.EastWestNames)), ("address-family", ("address_family", Tpa.VrfNames.VrfName.AddressFamily))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
                ])
                self.vrf_name = None
                self.disable = None

                self.east_west_names = Tpa.VrfNames.VrfName.EastWestNames()
                self.east_west_names.parent = self
                self._children_name_map["east_west_names"] = "east-west-names"

                self.address_family = Tpa.VrfNames.VrfName.AddressFamily()
                self.address_family.parent = self
                self._children_name_map["address_family"] = "address-family"
                self._segment_path = lambda: "vrf-name" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-kim-tpa-cfg:tpa/vrf-names/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Tpa.VrfNames.VrfName, ['vrf_name', 'disable'], name, value)


            class EastWestNames(Entity):
                """
                EastWest container
                
                .. attribute:: east_west_name
                
                	East West interface
                	**type**\: list of  		 :py:class:`EastWestName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.EastWestNames.EastWestName>`
                
                

                """

                _prefix = 'kim-tpa-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Tpa.VrfNames.VrfName.EastWestNames, self).__init__()

                    self.yang_name = "east-west-names"
                    self.yang_parent_name = "vrf-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("east-west-name", ("east_west_name", Tpa.VrfNames.VrfName.EastWestNames.EastWestName))])
                    self._leafs = OrderedDict()

                    self.east_west_name = YList(self)
                    self._segment_path = lambda: "east-west-names"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Tpa.VrfNames.VrfName.EastWestNames, [], name, value)


                class EastWestName(Entity):
                    """
                    East West interface
                    
                    .. attribute:: east_west_name  (key)
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: vrf
                    
                    	VRF name
                    	**type**\: str
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'kim-tpa-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tpa.VrfNames.VrfName.EastWestNames.EastWestName, self).__init__()

                        self.yang_name = "east-west-name"
                        self.yang_parent_name = "east-west-names"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['east_west_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('east_west_name', (YLeaf(YType.str, 'east-west-name'), ['str'])),
                            ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                        ])
                        self.east_west_name = None
                        self.vrf = None
                        self.interface = None
                        self._segment_path = lambda: "east-west-name" + "[east-west-name='" + str(self.east_west_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tpa.VrfNames.VrfName.EastWestNames.EastWestName, ['east_west_name', 'vrf', 'interface'], name, value)


            class AddressFamily(Entity):
                """
                Address family
                
                .. attribute:: ipv6
                
                	IPv6 configuration
                	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.AddressFamily.Ipv6>`
                
                .. attribute:: ipv4
                
                	IPv4 configuration
                	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.AddressFamily.Ipv4>`
                
                

                """

                _prefix = 'kim-tpa-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Tpa.VrfNames.VrfName.AddressFamily, self).__init__()

                    self.yang_name = "address-family"
                    self.yang_parent_name = "vrf-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ipv6", ("ipv6", Tpa.VrfNames.VrfName.AddressFamily.Ipv6)), ("ipv4", ("ipv4", Tpa.VrfNames.VrfName.AddressFamily.Ipv4))])
                    self._leafs = OrderedDict()

                    self.ipv6 = Tpa.VrfNames.VrfName.AddressFamily.Ipv6()
                    self.ipv6.parent = self
                    self._children_name_map["ipv6"] = "ipv6"

                    self.ipv4 = Tpa.VrfNames.VrfName.AddressFamily.Ipv4()
                    self.ipv4.parent = self
                    self._children_name_map["ipv4"] = "ipv4"
                    self._segment_path = lambda: "address-family"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Tpa.VrfNames.VrfName.AddressFamily, [], name, value)


                class Ipv6(Entity):
                    """
                    IPv6 configuration
                    
                    .. attribute:: default_route
                    
                    	Default interface used for routing
                    	**type**\: str
                    
                    .. attribute:: interface_names
                    
                    	Interface used for source address for egress interface
                    	**type**\:  :py:class:`InterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.AddressFamily.Ipv6.InterfaceNames>`
                    
                    .. attribute:: update_source
                    
                    	Interface used for Source Address
                    	**type**\:  :py:class:`UpdateSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.AddressFamily.Ipv6.UpdateSource>`
                    
                    

                    """

                    _prefix = 'kim-tpa-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tpa.VrfNames.VrfName.AddressFamily.Ipv6, self).__init__()

                        self.yang_name = "ipv6"
                        self.yang_parent_name = "address-family"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface-names", ("interface_names", Tpa.VrfNames.VrfName.AddressFamily.Ipv6.InterfaceNames)), ("update-source", ("update_source", Tpa.VrfNames.VrfName.AddressFamily.Ipv6.UpdateSource))])
                        self._leafs = OrderedDict([
                            ('default_route', (YLeaf(YType.str, 'default-route'), ['str'])),
                        ])
                        self.default_route = None

                        self.interface_names = Tpa.VrfNames.VrfName.AddressFamily.Ipv6.InterfaceNames()
                        self.interface_names.parent = self
                        self._children_name_map["interface_names"] = "interface-names"

                        self.update_source = Tpa.VrfNames.VrfName.AddressFamily.Ipv6.UpdateSource()
                        self.update_source.parent = self
                        self._children_name_map["update_source"] = "update-source"
                        self._segment_path = lambda: "ipv6"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tpa.VrfNames.VrfName.AddressFamily.Ipv6, ['default_route'], name, value)


                    class InterfaceNames(Entity):
                        """
                        Interface used for source address for egress
                        interface
                        
                        .. attribute:: interface_name
                        
                        	Egress interface name
                        	**type**\: list of  		 :py:class:`InterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.AddressFamily.Ipv6.InterfaceNames.InterfaceName>`
                        
                        

                        """

                        _prefix = 'kim-tpa-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tpa.VrfNames.VrfName.AddressFamily.Ipv6.InterfaceNames, self).__init__()

                            self.yang_name = "interface-names"
                            self.yang_parent_name = "ipv6"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface-name", ("interface_name", Tpa.VrfNames.VrfName.AddressFamily.Ipv6.InterfaceNames.InterfaceName))])
                            self._leafs = OrderedDict()

                            self.interface_name = YList(self)
                            self._segment_path = lambda: "interface-names"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tpa.VrfNames.VrfName.AddressFamily.Ipv6.InterfaceNames, [], name, value)


                        class InterfaceName(Entity):
                            """
                            Egress interface name
                            
                            .. attribute:: interface_name  (key)
                            
                            	Interface
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: egress_interface_source
                            
                            	Interface name for source address
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            

                            """

                            _prefix = 'kim-tpa-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Tpa.VrfNames.VrfName.AddressFamily.Ipv6.InterfaceNames.InterfaceName, self).__init__()

                                self.yang_name = "interface-name"
                                self.yang_parent_name = "interface-names"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('egress_interface_source', (YLeaf(YType.str, 'egress-interface-source'), ['str'])),
                                ])
                                self.interface_name = None
                                self.egress_interface_source = None
                                self._segment_path = lambda: "interface-name" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Tpa.VrfNames.VrfName.AddressFamily.Ipv6.InterfaceNames.InterfaceName, ['interface_name', 'egress_interface_source'], name, value)


                    class UpdateSource(Entity):
                        """
                        Interface used for Source Address
                        
                        .. attribute:: interface_name
                        
                        	Interface name for source address
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: active_management
                        
                        	Use the management port on the Active RP
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'kim-tpa-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tpa.VrfNames.VrfName.AddressFamily.Ipv6.UpdateSource, self).__init__()

                            self.yang_name = "update-source"
                            self.yang_parent_name = "ipv6"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('active_management', (YLeaf(YType.empty, 'active-management'), ['Empty'])),
                            ])
                            self.interface_name = None
                            self.active_management = None
                            self._segment_path = lambda: "update-source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tpa.VrfNames.VrfName.AddressFamily.Ipv6.UpdateSource, ['interface_name', 'active_management'], name, value)


                class Ipv4(Entity):
                    """
                    IPv4 configuration
                    
                    .. attribute:: default_route
                    
                    	Default interface used for routing
                    	**type**\: str
                    
                    .. attribute:: interface_names
                    
                    	Interface used for source address for egress interface
                    	**type**\:  :py:class:`InterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.AddressFamily.Ipv4.InterfaceNames>`
                    
                    .. attribute:: update_source
                    
                    	Interface used for Source Address
                    	**type**\:  :py:class:`UpdateSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.AddressFamily.Ipv4.UpdateSource>`
                    
                    

                    """

                    _prefix = 'kim-tpa-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tpa.VrfNames.VrfName.AddressFamily.Ipv4, self).__init__()

                        self.yang_name = "ipv4"
                        self.yang_parent_name = "address-family"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface-names", ("interface_names", Tpa.VrfNames.VrfName.AddressFamily.Ipv4.InterfaceNames)), ("update-source", ("update_source", Tpa.VrfNames.VrfName.AddressFamily.Ipv4.UpdateSource))])
                        self._leafs = OrderedDict([
                            ('default_route', (YLeaf(YType.str, 'default-route'), ['str'])),
                        ])
                        self.default_route = None

                        self.interface_names = Tpa.VrfNames.VrfName.AddressFamily.Ipv4.InterfaceNames()
                        self.interface_names.parent = self
                        self._children_name_map["interface_names"] = "interface-names"

                        self.update_source = Tpa.VrfNames.VrfName.AddressFamily.Ipv4.UpdateSource()
                        self.update_source.parent = self
                        self._children_name_map["update_source"] = "update-source"
                        self._segment_path = lambda: "ipv4"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tpa.VrfNames.VrfName.AddressFamily.Ipv4, ['default_route'], name, value)


                    class InterfaceNames(Entity):
                        """
                        Interface used for source address for egress
                        interface
                        
                        .. attribute:: interface_name
                        
                        	Egress interface name
                        	**type**\: list of  		 :py:class:`InterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.VrfNames.VrfName.AddressFamily.Ipv4.InterfaceNames.InterfaceName>`
                        
                        

                        """

                        _prefix = 'kim-tpa-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tpa.VrfNames.VrfName.AddressFamily.Ipv4.InterfaceNames, self).__init__()

                            self.yang_name = "interface-names"
                            self.yang_parent_name = "ipv4"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface-name", ("interface_name", Tpa.VrfNames.VrfName.AddressFamily.Ipv4.InterfaceNames.InterfaceName))])
                            self._leafs = OrderedDict()

                            self.interface_name = YList(self)
                            self._segment_path = lambda: "interface-names"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tpa.VrfNames.VrfName.AddressFamily.Ipv4.InterfaceNames, [], name, value)


                        class InterfaceName(Entity):
                            """
                            Egress interface name
                            
                            .. attribute:: interface_name  (key)
                            
                            	Interface
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: egress_interface_source
                            
                            	Interface name for source address
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            

                            """

                            _prefix = 'kim-tpa-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Tpa.VrfNames.VrfName.AddressFamily.Ipv4.InterfaceNames.InterfaceName, self).__init__()

                                self.yang_name = "interface-name"
                                self.yang_parent_name = "interface-names"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('egress_interface_source', (YLeaf(YType.str, 'egress-interface-source'), ['str'])),
                                ])
                                self.interface_name = None
                                self.egress_interface_source = None
                                self._segment_path = lambda: "interface-name" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Tpa.VrfNames.VrfName.AddressFamily.Ipv4.InterfaceNames.InterfaceName, ['interface_name', 'egress_interface_source'], name, value)


                    class UpdateSource(Entity):
                        """
                        Interface used for Source Address
                        
                        .. attribute:: interface_name
                        
                        	Interface name for source address
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: active_management
                        
                        	Use the management port on the Active RP
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'kim-tpa-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Tpa.VrfNames.VrfName.AddressFamily.Ipv4.UpdateSource, self).__init__()

                            self.yang_name = "update-source"
                            self.yang_parent_name = "ipv4"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('active_management', (YLeaf(YType.empty, 'active-management'), ['Empty'])),
                            ])
                            self.interface_name = None
                            self.active_management = None
                            self._segment_path = lambda: "update-source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tpa.VrfNames.VrfName.AddressFamily.Ipv4.UpdateSource, ['interface_name', 'active_management'], name, value)


    class Logging(Entity):
        """
        Third party app logging
        
        .. attribute:: kim
        
        	KIM logging
        	**type**\:  :py:class:`Kim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_kim_tpa_cfg.Tpa.Logging.Kim>`
        
        

        """

        _prefix = 'kim-tpa-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Tpa.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "tpa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("kim", ("kim", Tpa.Logging.Kim))])
            self._leafs = OrderedDict()

            self.kim = Tpa.Logging.Kim()
            self.kim.parent = self
            self._children_name_map["kim"] = "kim"
            self._segment_path = lambda: "logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-kim-tpa-cfg:tpa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Tpa.Logging, [], name, value)


        class Kim(Entity):
            """
            KIM logging
            
            .. attribute:: rotation_max
            
            	How many log rotation files to keep
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: file_size_max_kb
            
            	Size in Kilobytes of the log file
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: kilobyte
            
            

            """

            _prefix = 'kim-tpa-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Tpa.Logging.Kim, self).__init__()

                self.yang_name = "kim"
                self.yang_parent_name = "logging"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rotation_max', (YLeaf(YType.uint32, 'rotation-max'), ['int'])),
                    ('file_size_max_kb', (YLeaf(YType.uint32, 'file-size-max-kb'), ['int'])),
                ])
                self.rotation_max = None
                self.file_size_max_kb = None
                self._segment_path = lambda: "kim"
                self._absolute_path = lambda: "Cisco-IOS-XR-kim-tpa-cfg:tpa/logging/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Tpa.Logging.Kim, ['rotation_max', 'file_size_max_kb'], name, value)


    class Statistics(Entity):
        """
        Statistics
        
        .. attribute:: max_intf_events
        
        	How many interface events to record
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_lpts_events
        
        	How many LPTS events to record
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: statistics_update_frequency
        
        	Statistics update frequency into Linux
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: second
        
        

        """

        _prefix = 'kim-tpa-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Tpa.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "tpa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('max_intf_events', (YLeaf(YType.uint32, 'max-intf-events'), ['int'])),
                ('max_lpts_events', (YLeaf(YType.uint32, 'max-lpts-events'), ['int'])),
                ('statistics_update_frequency', (YLeaf(YType.uint32, 'statistics-update-frequency'), ['int'])),
            ])
            self.max_intf_events = None
            self.max_lpts_events = None
            self.statistics_update_frequency = None
            self._segment_path = lambda: "statistics"
            self._absolute_path = lambda: "Cisco-IOS-XR-kim-tpa-cfg:tpa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Tpa.Statistics, ['max_intf_events', 'max_lpts_events', 'statistics_update_frequency'], name, value)

    def clone_ptr(self):
        self._top_entity = Tpa()
        return self._top_entity

