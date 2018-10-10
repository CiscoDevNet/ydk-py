""" Cisco_IOS_XR_ipv4_vrrp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-vrrp package configuration.

This module contains definitions
for the following management objects\:
  vrrp\: VRRP configuration

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Vrrp(Entity):
    """
    VRRP configuration
    
    .. attribute:: logging
    
    	VRRP logging options
    	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Logging>`
    
    .. attribute:: interfaces
    
    	Interface configuration table
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces>`
    
    .. attribute:: enable
    
    	Enable vrrp process
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'ipv4-vrrp-cfg'
    _revision = '2018-05-19'

    def __init__(self):
        super(Vrrp, self).__init__()
        self._top_entity = None

        self.yang_name = "vrrp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-vrrp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("logging", ("logging", Vrrp.Logging)), ("interfaces", ("interfaces", Vrrp.Interfaces))])
        self._leafs = OrderedDict([
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
        ])
        self.enable = None

        self.logging = Vrrp.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"

        self.interfaces = Vrrp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Vrrp, ['enable'], name, value)


    class Logging(Entity):
        """
        VRRP logging options
        
        .. attribute:: state_change_disable
        
        	VRRP state change IOS messages disable
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ipv4-vrrp-cfg'
        _revision = '2018-05-19'

        def __init__(self):
            super(Vrrp.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "vrrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('state_change_disable', (YLeaf(YType.empty, 'state-change-disable'), ['Empty'])),
            ])
            self.state_change_disable = None
            self._segment_path = lambda: "logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vrrp.Logging, ['state_change_disable'], name, value)


    class Interfaces(Entity):
        """
        Interface configuration table
        
        .. attribute:: interface
        
        	The interface being configured
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-vrrp-cfg'
        _revision = '2018-05-19'

        def __init__(self):
            super(Vrrp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "vrrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Vrrp.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vrrp.Interfaces, [], name, value)


        class Interface(Entity):
            """
            The interface being configured
            
            .. attribute:: interface_name  (key)
            
            	Interface name to configure
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: ipv6
            
            	IPv6 VRRP configuration
            	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6>`
            
            .. attribute:: delay
            
            	Minimum and Reload Delay
            	**type**\:  :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Delay>`
            
            	**presence node**\: True
            
            .. attribute:: ipv4
            
            	IPv4 VRRP configuration
            	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4>`
            
            .. attribute:: bfd
            
            	BFD configuration
            	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Bfd>`
            
            .. attribute:: mac_refresh
            
            	VRRP Slave MAC\-refresh rate in seconds
            	**type**\: int
            
            	**range:** 0..10000
            
            	**units**\: second
            
            	**default value**\: 60
            
            

            """

            _prefix = 'ipv4-vrrp-cfg'
            _revision = '2018-05-19'

            def __init__(self):
                super(Vrrp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("ipv6", ("ipv6", Vrrp.Interfaces.Interface.Ipv6)), ("delay", ("delay", Vrrp.Interfaces.Interface.Delay)), ("ipv4", ("ipv4", Vrrp.Interfaces.Interface.Ipv4)), ("bfd", ("bfd", Vrrp.Interfaces.Interface.Bfd))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('mac_refresh', (YLeaf(YType.uint32, 'mac-refresh'), ['int'])),
                ])
                self.interface_name = None
                self.mac_refresh = None

                self.ipv6 = Vrrp.Interfaces.Interface.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"

                self.delay = None
                self._children_name_map["delay"] = "delay"

                self.ipv4 = Vrrp.Interfaces.Interface.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"

                self.bfd = Vrrp.Interfaces.Interface.Bfd()
                self.bfd.parent = self
                self._children_name_map["bfd"] = "bfd"
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vrrp.Interfaces.Interface, ['interface_name', 'mac_refresh'], name, value)


            class Ipv6(Entity):
                """
                IPv6 VRRP configuration
                
                .. attribute:: version3
                
                	Version 3 VRRP configuration
                	**type**\:  :py:class:`Version3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3>`
                
                .. attribute:: slave_virtual_routers
                
                	The VRRP slave group configuration table
                	**type**\:  :py:class:`SlaveVirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters>`
                
                

                """

                _prefix = 'ipv4-vrrp-cfg'
                _revision = '2018-05-19'

                def __init__(self):
                    super(Vrrp.Interfaces.Interface.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("version3", ("version3", Vrrp.Interfaces.Interface.Ipv6.Version3)), ("slave-virtual-routers", ("slave_virtual_routers", Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters))])
                    self._leafs = OrderedDict()

                    self.version3 = Vrrp.Interfaces.Interface.Ipv6.Version3()
                    self.version3.parent = self
                    self._children_name_map["version3"] = "version3"

                    self.slave_virtual_routers = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters()
                    self.slave_virtual_routers.parent = self
                    self._children_name_map["slave_virtual_routers"] = "slave-virtual-routers"
                    self._segment_path = lambda: "ipv6"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6, [], name, value)


                class Version3(Entity):
                    """
                    Version 3 VRRP configuration
                    
                    .. attribute:: virtual_routers
                    
                    	The VRRP virtual router configuration table
                    	**type**\:  :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2018-05-19'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv6.Version3, self).__init__()

                        self.yang_name = "version3"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("virtual-routers", ("virtual_routers", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters))])
                        self._leafs = OrderedDict()

                        self.virtual_routers = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters()
                        self.virtual_routers.parent = self
                        self._children_name_map["virtual_routers"] = "virtual-routers"
                        self._segment_path = lambda: "version3"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3, [], name, value)


                    class VirtualRouters(Entity):
                        """
                        The VRRP virtual router configuration table
                        
                        .. attribute:: virtual_router
                        
                        	The VRRP virtual router being configured
                        	**type**\: list of  		 :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2018-05-19'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters, self).__init__()

                            self.yang_name = "virtual-routers"
                            self.yang_parent_name = "version3"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("virtual-router", ("virtual_router", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter))])
                            self._leafs = OrderedDict()

                            self.virtual_router = YList(self)
                            self._segment_path = lambda: "virtual-routers"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters, [], name, value)


                        class VirtualRouter(Entity):
                            """
                            The VRRP virtual router being configured
                            
                            .. attribute:: vr_id  (key)
                            
                            	VRID Virtual Router Identifier
                            	**type**\: int
                            
                            	**range:** 1..255
                            
                            .. attribute:: global_ipv6_addresses
                            
                            	The table of VRRP virtual global IPv6 addresses
                            	**type**\:  :py:class:`GlobalIpv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses>`
                            
                            .. attribute:: tracks
                            
                            	Track an item, reducing priority if it goes down
                            	**type**\:  :py:class:`Tracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks>`
                            
                            .. attribute:: timer
                            
                            	Set advertisement timer
                            	**type**\:  :py:class:`Timer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer>`
                            
                            .. attribute:: tracked_objects
                            
                            	Track an object, reducing priority if it goes down
                            	**type**\:  :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects>`
                            
                            .. attribute:: link_local_ipv6_address
                            
                            	The VRRP IPv6 virtual linklocal address
                            	**type**\:  :py:class:`LinkLocalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address>`
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection for this IP
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\: int
                            
                            	**range:** 1..254
                            
                            	**default value**\: 100
                            
                            .. attribute:: accept_mode_disable
                            
                            	Disable Accept Mode for this virtual IPAddress
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: preempt
                            
                            	Preempt Master router if higher priority
                            	**type**\: int
                            
                            	**range:** 0..3600
                            
                            	**default value**\: 0
                            
                            .. attribute:: session_name
                            
                            	VRRP Session Name
                            	**type**\: str
                            
                            	**length:** 1..16
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2018-05-19'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter, self).__init__()

                                self.yang_name = "virtual-router"
                                self.yang_parent_name = "virtual-routers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['vr_id']
                                self._child_classes = OrderedDict([("global-ipv6-addresses", ("global_ipv6_addresses", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses)), ("tracks", ("tracks", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks)), ("timer", ("timer", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer)), ("tracked-objects", ("tracked_objects", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects)), ("link-local-ipv6-address", ("link_local_ipv6_address", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address))])
                                self._leafs = OrderedDict([
                                    ('vr_id', (YLeaf(YType.uint32, 'vr-id'), ['int'])),
                                    ('bfd', (YLeaf(YType.str, 'bfd'), ['str','str'])),
                                    ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                    ('accept_mode_disable', (YLeaf(YType.empty, 'accept-mode-disable'), ['Empty'])),
                                    ('preempt', (YLeaf(YType.uint32, 'preempt'), ['int'])),
                                    ('session_name', (YLeaf(YType.str, 'session-name'), ['str'])),
                                ])
                                self.vr_id = None
                                self.bfd = None
                                self.priority = None
                                self.accept_mode_disable = None
                                self.preempt = None
                                self.session_name = None

                                self.global_ipv6_addresses = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses()
                                self.global_ipv6_addresses.parent = self
                                self._children_name_map["global_ipv6_addresses"] = "global-ipv6-addresses"

                                self.tracks = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks()
                                self.tracks.parent = self
                                self._children_name_map["tracks"] = "tracks"

                                self.timer = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer()
                                self.timer.parent = self
                                self._children_name_map["timer"] = "timer"

                                self.tracked_objects = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects()
                                self.tracked_objects.parent = self
                                self._children_name_map["tracked_objects"] = "tracked-objects"

                                self.link_local_ipv6_address = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address()
                                self.link_local_ipv6_address.parent = self
                                self._children_name_map["link_local_ipv6_address"] = "link-local-ipv6-address"
                                self._segment_path = lambda: "virtual-router" + "[vr-id='" + str(self.vr_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter, ['vr_id', 'bfd', 'priority', 'accept_mode_disable', 'preempt', 'session_name'], name, value)


                            class GlobalIpv6Addresses(Entity):
                                """
                                The table of VRRP virtual global IPv6
                                addresses
                                
                                .. attribute:: global_ipv6_address
                                
                                	A VRRP virtual global IPv6 IP address
                                	**type**\: list of  		 :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses, self).__init__()

                                    self.yang_name = "global-ipv6-addresses"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("global-ipv6-address", ("global_ipv6_address", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address))])
                                    self._leafs = OrderedDict()

                                    self.global_ipv6_address = YList(self)
                                    self._segment_path = lambda: "global-ipv6-addresses"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses, [], name, value)


                                class GlobalIpv6Address(Entity):
                                    """
                                    A VRRP virtual global IPv6 IP address
                                    
                                    .. attribute:: ip_address  (key)
                                    
                                    	VRRP virtual global IPv6 address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2018-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address, self).__init__()

                                        self.yang_name = "global-ipv6-address"
                                        self.yang_parent_name = "global-ipv6-addresses"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['ip_address']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                                        ])
                                        self.ip_address = None
                                        self._segment_path = lambda: "global-ipv6-address" + "[ip-address='" + str(self.ip_address) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address, ['ip_address'], name, value)


                            class Tracks(Entity):
                                """
                                Track an item, reducing priority if it
                                goes down
                                
                                .. attribute:: track
                                
                                	Object to be tracked
                                	**type**\: list of  		 :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks, self).__init__()

                                    self.yang_name = "tracks"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("track", ("track", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track))])
                                    self._leafs = OrderedDict()

                                    self.track = YList(self)
                                    self._segment_path = lambda: "tracks"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks, [], name, value)


                                class Track(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: interface_name  (key)
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    .. attribute:: priority
                                    
                                    	Priority decrement
                                    	**type**\: int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2018-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track, self).__init__()

                                        self.yang_name = "track"
                                        self.yang_parent_name = "tracks"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['interface_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                            ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                        ])
                                        self.interface_name = None
                                        self.priority = None
                                        self._segment_path = lambda: "track" + "[interface-name='" + str(self.interface_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track, ['interface_name', 'priority'], name, value)


                            class Timer(Entity):
                                """
                                Set advertisement timer
                                
                                .. attribute:: advertisement_time_in_msec
                                
                                	Advertisement time in milliseconds
                                	**type**\: int
                                
                                	**range:** 100..40950
                                
                                	**units**\: millisecond
                                
                                .. attribute:: advertisement_time_in_sec
                                
                                	Advertisement time in seconds
                                	**type**\: int
                                
                                	**range:** 1..40
                                
                                	**units**\: second
                                
                                .. attribute:: forced
                                
                                	TRUE \- Force configured timer values to be used, required when configured in milliseconds
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                	**units**\: millisecond
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer, self).__init__()

                                    self.yang_name = "timer"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('advertisement_time_in_msec', (YLeaf(YType.uint32, 'advertisement-time-in-msec'), ['int'])),
                                        ('advertisement_time_in_sec', (YLeaf(YType.uint32, 'advertisement-time-in-sec'), ['int'])),
                                        ('forced', (YLeaf(YType.empty, 'forced'), ['Empty'])),
                                    ])
                                    self.advertisement_time_in_msec = None
                                    self.advertisement_time_in_sec = None
                                    self.forced = None
                                    self._segment_path = lambda: "timer"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer, ['advertisement_time_in_msec', 'advertisement_time_in_sec', 'forced'], name, value)


                            class TrackedObjects(Entity):
                                """
                                Track an object, reducing priority if it
                                goes down
                                
                                .. attribute:: tracked_object
                                
                                	Object to be tracked
                                	**type**\: list of  		 :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("tracked-object", ("tracked_object", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject))])
                                    self._leafs = OrderedDict()

                                    self.tracked_object = YList(self)
                                    self._segment_path = lambda: "tracked-objects"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects, [], name, value)


                                class TrackedObject(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: object_name  (key)
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\: int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2018-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__init__()

                                        self.yang_name = "tracked-object"
                                        self.yang_parent_name = "tracked-objects"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['object_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                                            ('priority_decrement', (YLeaf(YType.uint32, 'priority-decrement'), ['int'])),
                                        ])
                                        self.object_name = None
                                        self.priority_decrement = None
                                        self._segment_path = lambda: "tracked-object" + "[object-name='" + str(self.object_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, ['object_name', 'priority_decrement'], name, value)


                            class LinkLocalIpv6Address(Entity):
                                """
                                The VRRP IPv6 virtual linklocal address
                                
                                .. attribute:: ip_address
                                
                                	VRRP IPv6 virtual linklocal address
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: auto_configure
                                
                                	TRUE if the virtual linklocal address is to be autoconfigured FALSE if an IPv6 virtual linklocal address is configured
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address, self).__init__()

                                    self.yang_name = "link-local-ipv6-address"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                                        ('auto_configure', (YLeaf(YType.boolean, 'auto-configure'), ['bool'])),
                                    ])
                                    self.ip_address = None
                                    self.auto_configure = None
                                    self._segment_path = lambda: "link-local-ipv6-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address, ['ip_address', 'auto_configure'], name, value)


                class SlaveVirtualRouters(Entity):
                    """
                    The VRRP slave group configuration table
                    
                    .. attribute:: slave_virtual_router
                    
                    	The VRRP slave being configured
                    	**type**\: list of  		 :py:class:`SlaveVirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2018-05-19'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters, self).__init__()

                        self.yang_name = "slave-virtual-routers"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("slave-virtual-router", ("slave_virtual_router", Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter))])
                        self._leafs = OrderedDict()

                        self.slave_virtual_router = YList(self)
                        self._segment_path = lambda: "slave-virtual-routers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters, [], name, value)


                    class SlaveVirtualRouter(Entity):
                        """
                        The VRRP slave being configured
                        
                        .. attribute:: slave_virtual_router_id  (key)
                        
                        	Virtual Router ID
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        .. attribute:: link_local_ipv6_address
                        
                        	The VRRP IPv6 virtual linklocal address
                        	**type**\:  :py:class:`LinkLocalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address>`
                        
                        .. attribute:: global_ipv6_addresses
                        
                        	The table of VRRP virtual global IPv6 addresses
                        	**type**\:  :py:class:`GlobalIpv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses>`
                        
                        .. attribute:: follow
                        
                        	VRRP Session name for this slave to follow
                        	**type**\: str
                        
                        .. attribute:: accept_mode_disable
                        
                        	Disable Accept Mode for this virtual IPAddress
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2018-05-19'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter, self).__init__()

                            self.yang_name = "slave-virtual-router"
                            self.yang_parent_name = "slave-virtual-routers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['slave_virtual_router_id']
                            self._child_classes = OrderedDict([("link-local-ipv6-address", ("link_local_ipv6_address", Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address)), ("global-ipv6-addresses", ("global_ipv6_addresses", Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses))])
                            self._leafs = OrderedDict([
                                ('slave_virtual_router_id', (YLeaf(YType.uint32, 'slave-virtual-router-id'), ['int'])),
                                ('follow', (YLeaf(YType.str, 'follow'), ['str'])),
                                ('accept_mode_disable', (YLeaf(YType.empty, 'accept-mode-disable'), ['Empty'])),
                            ])
                            self.slave_virtual_router_id = None
                            self.follow = None
                            self.accept_mode_disable = None

                            self.link_local_ipv6_address = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address()
                            self.link_local_ipv6_address.parent = self
                            self._children_name_map["link_local_ipv6_address"] = "link-local-ipv6-address"

                            self.global_ipv6_addresses = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses()
                            self.global_ipv6_addresses.parent = self
                            self._children_name_map["global_ipv6_addresses"] = "global-ipv6-addresses"
                            self._segment_path = lambda: "slave-virtual-router" + "[slave-virtual-router-id='" + str(self.slave_virtual_router_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter, ['slave_virtual_router_id', 'follow', 'accept_mode_disable'], name, value)


                        class LinkLocalIpv6Address(Entity):
                            """
                            The VRRP IPv6 virtual linklocal address
                            
                            .. attribute:: ip_address
                            
                            	VRRP IPv6 virtual linklocal address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: auto_configure
                            
                            	TRUE if the virtual linklocal address is to be autoconfigured FALSE if an IPv6 virtual linklocal address is configured
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2018-05-19'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address, self).__init__()

                                self.yang_name = "link-local-ipv6-address"
                                self.yang_parent_name = "slave-virtual-router"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                                    ('auto_configure', (YLeaf(YType.boolean, 'auto-configure'), ['bool'])),
                                ])
                                self.ip_address = None
                                self.auto_configure = None
                                self._segment_path = lambda: "link-local-ipv6-address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address, ['ip_address', 'auto_configure'], name, value)


                        class GlobalIpv6Addresses(Entity):
                            """
                            The table of VRRP virtual global IPv6
                            addresses
                            
                            .. attribute:: global_ipv6_address
                            
                            	A VRRP virtual global IPv6 IP address
                            	**type**\: list of  		 :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2018-05-19'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses, self).__init__()

                                self.yang_name = "global-ipv6-addresses"
                                self.yang_parent_name = "slave-virtual-router"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("global-ipv6-address", ("global_ipv6_address", Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address))])
                                self._leafs = OrderedDict()

                                self.global_ipv6_address = YList(self)
                                self._segment_path = lambda: "global-ipv6-addresses"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses, [], name, value)


                            class GlobalIpv6Address(Entity):
                                """
                                A VRRP virtual global IPv6 IP address
                                
                                .. attribute:: ip_address  (key)
                                
                                	VRRP virtual global IPv6 address
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address, self).__init__()

                                    self.yang_name = "global-ipv6-address"
                                    self.yang_parent_name = "global-ipv6-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['ip_address']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                                    ])
                                    self.ip_address = None
                                    self._segment_path = lambda: "global-ipv6-address" + "[ip-address='" + str(self.ip_address) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address, ['ip_address'], name, value)


            class Delay(Entity):
                """
                Minimum and Reload Delay
                
                .. attribute:: min_delay
                
                	Minimum delay in seconds
                	**type**\: int
                
                	**range:** 0..10000
                
                	**mandatory**\: True
                
                	**units**\: second
                
                .. attribute:: reload_delay
                
                	Reload delay in seconds
                	**type**\: int
                
                	**range:** 0..10000
                
                	**mandatory**\: True
                
                	**units**\: second
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-vrrp-cfg'
                _revision = '2018-05-19'

                def __init__(self):
                    super(Vrrp.Interfaces.Interface.Delay, self).__init__()

                    self.yang_name = "delay"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('min_delay', (YLeaf(YType.uint32, 'min-delay'), ['int'])),
                        ('reload_delay', (YLeaf(YType.uint32, 'reload-delay'), ['int'])),
                    ])
                    self.min_delay = None
                    self.reload_delay = None
                    self._segment_path = lambda: "delay"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrrp.Interfaces.Interface.Delay, ['min_delay', 'reload_delay'], name, value)


            class Ipv4(Entity):
                """
                IPv4 VRRP configuration
                
                .. attribute:: version3
                
                	Version 3 VRRP configuration
                	**type**\:  :py:class:`Version3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3>`
                
                .. attribute:: slave_virtual_routers
                
                	The VRRP slave group configuration table
                	**type**\:  :py:class:`SlaveVirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters>`
                
                .. attribute:: version2
                
                	Version 2 VRRP configuration
                	**type**\:  :py:class:`Version2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2>`
                
                

                """

                _prefix = 'ipv4-vrrp-cfg'
                _revision = '2018-05-19'

                def __init__(self):
                    super(Vrrp.Interfaces.Interface.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("version3", ("version3", Vrrp.Interfaces.Interface.Ipv4.Version3)), ("slave-virtual-routers", ("slave_virtual_routers", Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters)), ("version2", ("version2", Vrrp.Interfaces.Interface.Ipv4.Version2))])
                    self._leafs = OrderedDict()

                    self.version3 = Vrrp.Interfaces.Interface.Ipv4.Version3()
                    self.version3.parent = self
                    self._children_name_map["version3"] = "version3"

                    self.slave_virtual_routers = Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters()
                    self.slave_virtual_routers.parent = self
                    self._children_name_map["slave_virtual_routers"] = "slave-virtual-routers"

                    self.version2 = Vrrp.Interfaces.Interface.Ipv4.Version2()
                    self.version2.parent = self
                    self._children_name_map["version2"] = "version2"
                    self._segment_path = lambda: "ipv4"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4, [], name, value)


                class Version3(Entity):
                    """
                    Version 3 VRRP configuration
                    
                    .. attribute:: virtual_routers
                    
                    	The VRRP virtual router configuration table
                    	**type**\:  :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2018-05-19'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv4.Version3, self).__init__()

                        self.yang_name = "version3"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("virtual-routers", ("virtual_routers", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters))])
                        self._leafs = OrderedDict()

                        self.virtual_routers = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters()
                        self.virtual_routers.parent = self
                        self._children_name_map["virtual_routers"] = "virtual-routers"
                        self._segment_path = lambda: "version3"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3, [], name, value)


                    class VirtualRouters(Entity):
                        """
                        The VRRP virtual router configuration table
                        
                        .. attribute:: virtual_router
                        
                        	The VRRP virtual router being configured
                        	**type**\: list of  		 :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2018-05-19'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters, self).__init__()

                            self.yang_name = "virtual-routers"
                            self.yang_parent_name = "version3"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("virtual-router", ("virtual_router", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter))])
                            self._leafs = OrderedDict()

                            self.virtual_router = YList(self)
                            self._segment_path = lambda: "virtual-routers"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters, [], name, value)


                        class VirtualRouter(Entity):
                            """
                            The VRRP virtual router being configured
                            
                            .. attribute:: vr_id  (key)
                            
                            	VRID Virtual Router Identifier
                            	**type**\: int
                            
                            	**range:** 1..255
                            
                            .. attribute:: timer
                            
                            	Set advertisement timer
                            	**type**\:  :py:class:`Timer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer>`
                            
                            .. attribute:: secondary_ipv4_addresses
                            
                            	The table of VRRP secondary IPv4 addresses
                            	**type**\:  :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses>`
                            
                            .. attribute:: tracked_objects
                            
                            	Track an object, reducing priority if it goes down
                            	**type**\:  :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects>`
                            
                            .. attribute:: tracks
                            
                            	Track an item, reducing priority if it goes down
                            	**type**\:  :py:class:`Tracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks>`
                            
                            .. attribute:: session_name
                            
                            	VRRP Session Name
                            	**type**\: str
                            
                            	**length:** 1..16
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection for this IP
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: primary_ipv4_address
                            
                            	The Primary VRRP IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: preempt
                            
                            	Preempt Master router if higher priority
                            	**type**\: int
                            
                            	**range:** 0..3600
                            
                            	**default value**\: 0
                            
                            .. attribute:: accept_mode_disable
                            
                            	Disable Accept Mode for this virtual IPAddress
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\: int
                            
                            	**range:** 1..254
                            
                            	**default value**\: 100
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2018-05-19'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter, self).__init__()

                                self.yang_name = "virtual-router"
                                self.yang_parent_name = "virtual-routers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['vr_id']
                                self._child_classes = OrderedDict([("timer", ("timer", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer)), ("secondary-ipv4-addresses", ("secondary_ipv4_addresses", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses)), ("tracked-objects", ("tracked_objects", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects)), ("tracks", ("tracks", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks))])
                                self._leafs = OrderedDict([
                                    ('vr_id', (YLeaf(YType.uint32, 'vr-id'), ['int'])),
                                    ('session_name', (YLeaf(YType.str, 'session-name'), ['str'])),
                                    ('bfd', (YLeaf(YType.str, 'bfd'), ['str'])),
                                    ('primary_ipv4_address', (YLeaf(YType.str, 'primary-ipv4-address'), ['str'])),
                                    ('preempt', (YLeaf(YType.uint32, 'preempt'), ['int'])),
                                    ('accept_mode_disable', (YLeaf(YType.empty, 'accept-mode-disable'), ['Empty'])),
                                    ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                ])
                                self.vr_id = None
                                self.session_name = None
                                self.bfd = None
                                self.primary_ipv4_address = None
                                self.preempt = None
                                self.accept_mode_disable = None
                                self.priority = None

                                self.timer = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer()
                                self.timer.parent = self
                                self._children_name_map["timer"] = "timer"

                                self.secondary_ipv4_addresses = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses()
                                self.secondary_ipv4_addresses.parent = self
                                self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"

                                self.tracked_objects = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects()
                                self.tracked_objects.parent = self
                                self._children_name_map["tracked_objects"] = "tracked-objects"

                                self.tracks = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks()
                                self.tracks.parent = self
                                self._children_name_map["tracks"] = "tracks"
                                self._segment_path = lambda: "virtual-router" + "[vr-id='" + str(self.vr_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter, ['vr_id', 'session_name', 'bfd', 'primary_ipv4_address', 'preempt', 'accept_mode_disable', 'priority'], name, value)


                            class Timer(Entity):
                                """
                                Set advertisement timer
                                
                                .. attribute:: advertisement_time_in_msec
                                
                                	Advertisement time in milliseconds
                                	**type**\: int
                                
                                	**range:** 100..40950
                                
                                	**units**\: millisecond
                                
                                .. attribute:: advertisement_time_in_sec
                                
                                	Advertisement time in seconds
                                	**type**\: int
                                
                                	**range:** 1..40
                                
                                	**units**\: second
                                
                                .. attribute:: forced
                                
                                	TRUE \- Force configured timer values to be used, required when configured in milliseconds
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                	**units**\: millisecond
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer, self).__init__()

                                    self.yang_name = "timer"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('advertisement_time_in_msec', (YLeaf(YType.uint32, 'advertisement-time-in-msec'), ['int'])),
                                        ('advertisement_time_in_sec', (YLeaf(YType.uint32, 'advertisement-time-in-sec'), ['int'])),
                                        ('forced', (YLeaf(YType.empty, 'forced'), ['Empty'])),
                                    ])
                                    self.advertisement_time_in_msec = None
                                    self.advertisement_time_in_sec = None
                                    self.forced = None
                                    self._segment_path = lambda: "timer"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer, ['advertisement_time_in_msec', 'advertisement_time_in_sec', 'forced'], name, value)


                            class SecondaryIpv4Addresses(Entity):
                                """
                                The table of VRRP secondary IPv4 addresses
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	A VRRP secondary IPv4 address
                                	**type**\: list of  		 :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses, self).__init__()

                                    self.yang_name = "secondary-ipv4-addresses"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("secondary-ipv4-address", ("secondary_ipv4_address", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address))])
                                    self._leafs = OrderedDict()

                                    self.secondary_ipv4_address = YList(self)
                                    self._segment_path = lambda: "secondary-ipv4-addresses"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses, [], name, value)


                                class SecondaryIpv4Address(Entity):
                                    """
                                    A VRRP secondary IPv4 address
                                    
                                    .. attribute:: ip_address  (key)
                                    
                                    	VRRP Secondary IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2018-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                        self.yang_name = "secondary-ipv4-address"
                                        self.yang_parent_name = "secondary-ipv4-addresses"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['ip_address']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                        ])
                                        self.ip_address = None
                                        self._segment_path = lambda: "secondary-ipv4-address" + "[ip-address='" + str(self.ip_address) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, ['ip_address'], name, value)


                            class TrackedObjects(Entity):
                                """
                                Track an object, reducing priority if it
                                goes down
                                
                                .. attribute:: tracked_object
                                
                                	Object to be tracked
                                	**type**\: list of  		 :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("tracked-object", ("tracked_object", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject))])
                                    self._leafs = OrderedDict()

                                    self.tracked_object = YList(self)
                                    self._segment_path = lambda: "tracked-objects"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects, [], name, value)


                                class TrackedObject(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: object_name  (key)
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\: int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2018-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__init__()

                                        self.yang_name = "tracked-object"
                                        self.yang_parent_name = "tracked-objects"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['object_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                                            ('priority_decrement', (YLeaf(YType.uint32, 'priority-decrement'), ['int'])),
                                        ])
                                        self.object_name = None
                                        self.priority_decrement = None
                                        self._segment_path = lambda: "tracked-object" + "[object-name='" + str(self.object_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, ['object_name', 'priority_decrement'], name, value)


                            class Tracks(Entity):
                                """
                                Track an item, reducing priority if it
                                goes down
                                
                                .. attribute:: track
                                
                                	Object to be tracked
                                	**type**\: list of  		 :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks, self).__init__()

                                    self.yang_name = "tracks"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("track", ("track", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track))])
                                    self._leafs = OrderedDict()

                                    self.track = YList(self)
                                    self._segment_path = lambda: "tracks"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks, [], name, value)


                                class Track(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: interface_name  (key)
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    .. attribute:: priority
                                    
                                    	Priority decrement
                                    	**type**\: int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2018-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track, self).__init__()

                                        self.yang_name = "track"
                                        self.yang_parent_name = "tracks"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['interface_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                            ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                        ])
                                        self.interface_name = None
                                        self.priority = None
                                        self._segment_path = lambda: "track" + "[interface-name='" + str(self.interface_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track, ['interface_name', 'priority'], name, value)


                class SlaveVirtualRouters(Entity):
                    """
                    The VRRP slave group configuration table
                    
                    .. attribute:: slave_virtual_router
                    
                    	The VRRP slave being configured
                    	**type**\: list of  		 :py:class:`SlaveVirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2018-05-19'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters, self).__init__()

                        self.yang_name = "slave-virtual-routers"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("slave-virtual-router", ("slave_virtual_router", Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter))])
                        self._leafs = OrderedDict()

                        self.slave_virtual_router = YList(self)
                        self._segment_path = lambda: "slave-virtual-routers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters, [], name, value)


                    class SlaveVirtualRouter(Entity):
                        """
                        The VRRP slave being configured
                        
                        .. attribute:: slave_virtual_router_id  (key)
                        
                        	Virtual Router ID
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        .. attribute:: secondary_ipv4_addresses
                        
                        	The table of VRRP secondary IPv4 addresses
                        	**type**\:  :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses>`
                        
                        .. attribute:: follow
                        
                        	VRRP Session name for this slave to follow
                        	**type**\: str
                        
                        .. attribute:: accept_mode_disable
                        
                        	Disable Accept Mode for this virtual IPAddress
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: primary_ipv4_address
                        
                        	The Primary VRRP IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2018-05-19'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter, self).__init__()

                            self.yang_name = "slave-virtual-router"
                            self.yang_parent_name = "slave-virtual-routers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['slave_virtual_router_id']
                            self._child_classes = OrderedDict([("secondary-ipv4-addresses", ("secondary_ipv4_addresses", Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses))])
                            self._leafs = OrderedDict([
                                ('slave_virtual_router_id', (YLeaf(YType.uint32, 'slave-virtual-router-id'), ['int'])),
                                ('follow', (YLeaf(YType.str, 'follow'), ['str'])),
                                ('accept_mode_disable', (YLeaf(YType.empty, 'accept-mode-disable'), ['Empty'])),
                                ('primary_ipv4_address', (YLeaf(YType.str, 'primary-ipv4-address'), ['str'])),
                            ])
                            self.slave_virtual_router_id = None
                            self.follow = None
                            self.accept_mode_disable = None
                            self.primary_ipv4_address = None

                            self.secondary_ipv4_addresses = Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses()
                            self.secondary_ipv4_addresses.parent = self
                            self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                            self._segment_path = lambda: "slave-virtual-router" + "[slave-virtual-router-id='" + str(self.slave_virtual_router_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter, ['slave_virtual_router_id', 'follow', 'accept_mode_disable', 'primary_ipv4_address'], name, value)


                        class SecondaryIpv4Addresses(Entity):
                            """
                            The table of VRRP secondary IPv4 addresses
                            
                            .. attribute:: secondary_ipv4_address
                            
                            	A VRRP secondary IPv4 address
                            	**type**\: list of  		 :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2018-05-19'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses, self).__init__()

                                self.yang_name = "secondary-ipv4-addresses"
                                self.yang_parent_name = "slave-virtual-router"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("secondary-ipv4-address", ("secondary_ipv4_address", Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address))])
                                self._leafs = OrderedDict()

                                self.secondary_ipv4_address = YList(self)
                                self._segment_path = lambda: "secondary-ipv4-addresses"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses, [], name, value)


                            class SecondaryIpv4Address(Entity):
                                """
                                A VRRP secondary IPv4 address
                                
                                .. attribute:: ip_address  (key)
                                
                                	VRRP Secondary IPv4 address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                    self.yang_name = "secondary-ipv4-address"
                                    self.yang_parent_name = "secondary-ipv4-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['ip_address']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                    ])
                                    self.ip_address = None
                                    self._segment_path = lambda: "secondary-ipv4-address" + "[ip-address='" + str(self.ip_address) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, ['ip_address'], name, value)


                class Version2(Entity):
                    """
                    Version 2 VRRP configuration
                    
                    .. attribute:: virtual_routers
                    
                    	The VRRP virtual router configuration table
                    	**type**\:  :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2018-05-19'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv4.Version2, self).__init__()

                        self.yang_name = "version2"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("virtual-routers", ("virtual_routers", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters))])
                        self._leafs = OrderedDict()

                        self.virtual_routers = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters()
                        self.virtual_routers.parent = self
                        self._children_name_map["virtual_routers"] = "virtual-routers"
                        self._segment_path = lambda: "version2"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2, [], name, value)


                    class VirtualRouters(Entity):
                        """
                        The VRRP virtual router configuration table
                        
                        .. attribute:: virtual_router
                        
                        	The VRRP virtual router being configured
                        	**type**\: list of  		 :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2018-05-19'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters, self).__init__()

                            self.yang_name = "virtual-routers"
                            self.yang_parent_name = "version2"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("virtual-router", ("virtual_router", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter))])
                            self._leafs = OrderedDict()

                            self.virtual_router = YList(self)
                            self._segment_path = lambda: "virtual-routers"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters, [], name, value)


                        class VirtualRouter(Entity):
                            """
                            The VRRP virtual router being configured
                            
                            .. attribute:: vr_id  (key)
                            
                            	VRID Virtual Router Identifier
                            	**type**\: int
                            
                            	**range:** 1..255
                            
                            .. attribute:: timer
                            
                            	Set advertisement timer
                            	**type**\:  :py:class:`Timer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer>`
                            
                            .. attribute:: secondary_ipv4_addresses
                            
                            	The table of VRRP secondary IPv4 addresses
                            	**type**\:  :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses>`
                            
                            .. attribute:: tracks
                            
                            	Track an item, reducing priority if it goes down
                            	**type**\:  :py:class:`Tracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks>`
                            
                            .. attribute:: tracked_objects
                            
                            	Track an object, reducing priority if it goes down
                            	**type**\:  :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects>`
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\: int
                            
                            	**range:** 1..254
                            
                            	**default value**\: 100
                            
                            .. attribute:: primary_ipv4_address
                            
                            	The Primary VRRP IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: preempt
                            
                            	Preempt Master router if higher priority
                            	**type**\: int
                            
                            	**range:** 0..3600
                            
                            	**default value**\: 0
                            
                            .. attribute:: text_password
                            
                            	Authentication password, 8 chars max
                            	**type**\: str
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection for this IP
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: session_name
                            
                            	VRRP Session Name
                            	**type**\: str
                            
                            	**length:** 1..16
                            
                            .. attribute:: accept_mode_disable
                            
                            	Disable Accept Mode for this virtual IPAddress
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2018-05-19'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter, self).__init__()

                                self.yang_name = "virtual-router"
                                self.yang_parent_name = "virtual-routers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['vr_id']
                                self._child_classes = OrderedDict([("timer", ("timer", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer)), ("secondary-ipv4-addresses", ("secondary_ipv4_addresses", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses)), ("tracks", ("tracks", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks)), ("tracked-objects", ("tracked_objects", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects))])
                                self._leafs = OrderedDict([
                                    ('vr_id', (YLeaf(YType.uint32, 'vr-id'), ['int'])),
                                    ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                    ('primary_ipv4_address', (YLeaf(YType.str, 'primary-ipv4-address'), ['str'])),
                                    ('preempt', (YLeaf(YType.uint32, 'preempt'), ['int'])),
                                    ('text_password', (YLeaf(YType.str, 'text-password'), ['str'])),
                                    ('bfd', (YLeaf(YType.str, 'bfd'), ['str'])),
                                    ('session_name', (YLeaf(YType.str, 'session-name'), ['str'])),
                                    ('accept_mode_disable', (YLeaf(YType.empty, 'accept-mode-disable'), ['Empty'])),
                                ])
                                self.vr_id = None
                                self.priority = None
                                self.primary_ipv4_address = None
                                self.preempt = None
                                self.text_password = None
                                self.bfd = None
                                self.session_name = None
                                self.accept_mode_disable = None

                                self.timer = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer()
                                self.timer.parent = self
                                self._children_name_map["timer"] = "timer"

                                self.secondary_ipv4_addresses = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses()
                                self.secondary_ipv4_addresses.parent = self
                                self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"

                                self.tracks = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks()
                                self.tracks.parent = self
                                self._children_name_map["tracks"] = "tracks"

                                self.tracked_objects = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects()
                                self.tracked_objects.parent = self
                                self._children_name_map["tracked_objects"] = "tracked-objects"
                                self._segment_path = lambda: "virtual-router" + "[vr-id='" + str(self.vr_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter, ['vr_id', 'priority', 'primary_ipv4_address', 'preempt', 'text_password', 'bfd', 'session_name', 'accept_mode_disable'], name, value)


                            class Timer(Entity):
                                """
                                Set advertisement timer
                                
                                .. attribute:: advertisement_time_in_msec
                                
                                	Advertisement time in milliseconds
                                	**type**\: int
                                
                                	**range:** 100..40950
                                
                                	**units**\: millisecond
                                
                                .. attribute:: advertisement_time_in_sec
                                
                                	Advertisement time in seconds
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                .. attribute:: forced
                                
                                	TRUE \- Force configured timer values to be used, required when configured in milliseconds
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                	**units**\: millisecond
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer, self).__init__()

                                    self.yang_name = "timer"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('advertisement_time_in_msec', (YLeaf(YType.uint32, 'advertisement-time-in-msec'), ['int'])),
                                        ('advertisement_time_in_sec', (YLeaf(YType.uint32, 'advertisement-time-in-sec'), ['int'])),
                                        ('forced', (YLeaf(YType.empty, 'forced'), ['Empty'])),
                                    ])
                                    self.advertisement_time_in_msec = None
                                    self.advertisement_time_in_sec = None
                                    self.forced = None
                                    self._segment_path = lambda: "timer"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer, ['advertisement_time_in_msec', 'advertisement_time_in_sec', 'forced'], name, value)


                            class SecondaryIpv4Addresses(Entity):
                                """
                                The table of VRRP secondary IPv4 addresses
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	A VRRP secondary IPv4 address
                                	**type**\: list of  		 :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses, self).__init__()

                                    self.yang_name = "secondary-ipv4-addresses"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("secondary-ipv4-address", ("secondary_ipv4_address", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address))])
                                    self._leafs = OrderedDict()

                                    self.secondary_ipv4_address = YList(self)
                                    self._segment_path = lambda: "secondary-ipv4-addresses"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses, [], name, value)


                                class SecondaryIpv4Address(Entity):
                                    """
                                    A VRRP secondary IPv4 address
                                    
                                    .. attribute:: ip_address  (key)
                                    
                                    	VRRP Secondary IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2018-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                        self.yang_name = "secondary-ipv4-address"
                                        self.yang_parent_name = "secondary-ipv4-addresses"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['ip_address']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                        ])
                                        self.ip_address = None
                                        self._segment_path = lambda: "secondary-ipv4-address" + "[ip-address='" + str(self.ip_address) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, ['ip_address'], name, value)


                            class Tracks(Entity):
                                """
                                Track an item, reducing priority if it
                                goes down
                                
                                .. attribute:: track
                                
                                	Object to be tracked
                                	**type**\: list of  		 :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks, self).__init__()

                                    self.yang_name = "tracks"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("track", ("track", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track))])
                                    self._leafs = OrderedDict()

                                    self.track = YList(self)
                                    self._segment_path = lambda: "tracks"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks, [], name, value)


                                class Track(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: interface_name  (key)
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    .. attribute:: priority
                                    
                                    	Priority decrement
                                    	**type**\: int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2018-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track, self).__init__()

                                        self.yang_name = "track"
                                        self.yang_parent_name = "tracks"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['interface_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                            ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                        ])
                                        self.interface_name = None
                                        self.priority = None
                                        self._segment_path = lambda: "track" + "[interface-name='" + str(self.interface_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track, ['interface_name', 'priority'], name, value)


                            class TrackedObjects(Entity):
                                """
                                Track an object, reducing priority if it
                                goes down
                                
                                .. attribute:: tracked_object
                                
                                	Object to be tracked
                                	**type**\: list of  		 :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2018-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("tracked-object", ("tracked_object", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject))])
                                    self._leafs = OrderedDict()

                                    self.tracked_object = YList(self)
                                    self._segment_path = lambda: "tracked-objects"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects, [], name, value)


                                class TrackedObject(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: object_name  (key)
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\: int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2018-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__init__()

                                        self.yang_name = "tracked-object"
                                        self.yang_parent_name = "tracked-objects"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['object_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                                            ('priority_decrement', (YLeaf(YType.uint32, 'priority-decrement'), ['int'])),
                                        ])
                                        self.object_name = None
                                        self.priority_decrement = None
                                        self._segment_path = lambda: "tracked-object" + "[object-name='" + str(self.object_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, ['object_name', 'priority_decrement'], name, value)


            class Bfd(Entity):
                """
                BFD configuration
                
                .. attribute:: interval
                
                	Hello interval for BFD sessions created by vrrp
                	**type**\: int
                
                	**range:** 3..30000
                
                	**units**\: millisecond
                
                .. attribute:: detection_multiplier
                
                	Detection multiplier for BFD sessions created by vrrp
                	**type**\: int
                
                	**range:** 2..50
                
                

                """

                _prefix = 'ipv4-vrrp-cfg'
                _revision = '2018-05-19'

                def __init__(self):
                    super(Vrrp.Interfaces.Interface.Bfd, self).__init__()

                    self.yang_name = "bfd"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                        ('detection_multiplier', (YLeaf(YType.uint32, 'detection-multiplier'), ['int'])),
                    ])
                    self.interval = None
                    self.detection_multiplier = None
                    self._segment_path = lambda: "bfd"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrrp.Interfaces.Interface.Bfd, ['interval', 'detection_multiplier'], name, value)

    def clone_ptr(self):
        self._top_entity = Vrrp()
        return self._top_entity

