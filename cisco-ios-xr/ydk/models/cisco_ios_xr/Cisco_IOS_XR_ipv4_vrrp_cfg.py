""" Cisco_IOS_XR_ipv4_vrrp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-vrrp package configuration.

This module contains definitions
for the following management objects\:
  vrrp\: VRRP configuration

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Vrrp(Entity):
    """
    VRRP configuration
    
    .. attribute:: interfaces
    
    	Interface configuration table
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces>`
    
    .. attribute:: logging
    
    	VRRP logging options
    	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Logging>`
    
    

    """

    _prefix = 'ipv4-vrrp-cfg'
    _revision = '2017-05-19'

    def __init__(self):
        super(Vrrp, self).__init__()
        self._top_entity = None

        self.yang_name = "vrrp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-vrrp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"interfaces" : ("interfaces", Vrrp.Interfaces), "logging" : ("logging", Vrrp.Logging)}
        self._child_list_classes = {}

        self.interfaces = Vrrp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.logging = Vrrp.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"
        self._children_yang_names.add("logging")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp"


    class Interfaces(Entity):
        """
        Interface configuration table
        
        .. attribute:: interface
        
        	The interface being configured
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-vrrp-cfg'
        _revision = '2017-05-19'

        def __init__(self):
            super(Vrrp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "vrrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", Vrrp.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Vrrp.Interfaces, [], name, value)


        class Interface(Entity):
            """
            The interface being configured
            
            .. attribute:: interface_name  <key>
            
            	Interface name to configure
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: bfd
            
            	BFD configuration
            	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Bfd>`
            
            .. attribute:: delay
            
            	Minimum and Reload Delay
            	**type**\:   :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Delay>`
            
            	**presence node**\: True
            
            .. attribute:: ipv4
            
            	IPv4 VRRP configuration
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4>`
            
            .. attribute:: ipv6
            
            	IPv6 VRRP configuration
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6>`
            
            .. attribute:: mac_refresh
            
            	VRRP Slave MAC\-refresh rate in seconds
            	**type**\:  int
            
            	**range:** 0..10000
            
            	**units**\: second
            
            	**default value**\: 60
            
            

            """

            _prefix = 'ipv4-vrrp-cfg'
            _revision = '2017-05-19'

            def __init__(self):
                super(Vrrp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bfd" : ("bfd", Vrrp.Interfaces.Interface.Bfd), "delay" : ("delay", Vrrp.Interfaces.Interface.Delay), "ipv4" : ("ipv4", Vrrp.Interfaces.Interface.Ipv4), "ipv6" : ("ipv6", Vrrp.Interfaces.Interface.Ipv6)}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.mac_refresh = YLeaf(YType.uint32, "mac-refresh")

                self.bfd = Vrrp.Interfaces.Interface.Bfd()
                self.bfd.parent = self
                self._children_name_map["bfd"] = "bfd"
                self._children_yang_names.add("bfd")

                self.delay = None
                self._children_name_map["delay"] = "delay"
                self._children_yang_names.add("delay")

                self.ipv4 = Vrrp.Interfaces.Interface.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._children_yang_names.add("ipv4")

                self.ipv6 = Vrrp.Interfaces.Interface.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._children_yang_names.add("ipv6")
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vrrp.Interfaces.Interface, ['interface_name', 'mac_refresh'], name, value)


            class Bfd(Entity):
                """
                BFD configuration
                
                .. attribute:: detection_multiplier
                
                	Detection multiplier for BFD sessions created by vrrp
                	**type**\:  int
                
                	**range:** 2..50
                
                .. attribute:: interval
                
                	Hello interval for BFD sessions created by vrrp
                	**type**\:  int
                
                	**range:** 3..30000
                
                	**units**\: millisecond
                
                

                """

                _prefix = 'ipv4-vrrp-cfg'
                _revision = '2017-05-19'

                def __init__(self):
                    super(Vrrp.Interfaces.Interface.Bfd, self).__init__()

                    self.yang_name = "bfd"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.detection_multiplier = YLeaf(YType.uint32, "detection-multiplier")

                    self.interval = YLeaf(YType.uint32, "interval")
                    self._segment_path = lambda: "bfd"

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrrp.Interfaces.Interface.Bfd, ['detection_multiplier', 'interval'], name, value)


            class Delay(Entity):
                """
                Minimum and Reload Delay
                
                .. attribute:: min_delay
                
                	Minimum delay in seconds
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**mandatory**\: True
                
                	**units**\: second
                
                .. attribute:: reload_delay
                
                	Reload delay in seconds
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**mandatory**\: True
                
                	**units**\: second
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-vrrp-cfg'
                _revision = '2017-05-19'

                def __init__(self):
                    super(Vrrp.Interfaces.Interface.Delay, self).__init__()

                    self.yang_name = "delay"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.min_delay = YLeaf(YType.uint32, "min-delay")

                    self.reload_delay = YLeaf(YType.uint32, "reload-delay")
                    self._segment_path = lambda: "delay"

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrrp.Interfaces.Interface.Delay, ['min_delay', 'reload_delay'], name, value)


            class Ipv4(Entity):
                """
                IPv4 VRRP configuration
                
                .. attribute:: slave_virtual_routers
                
                	The VRRP slave group configuration table
                	**type**\:   :py:class:`SlaveVirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters>`
                
                .. attribute:: version2
                
                	Version 2 VRRP configuration
                	**type**\:   :py:class:`Version2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2>`
                
                .. attribute:: version3
                
                	Version 3 VRRP configuration
                	**type**\:   :py:class:`Version3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3>`
                
                

                """

                _prefix = 'ipv4-vrrp-cfg'
                _revision = '2017-05-19'

                def __init__(self):
                    super(Vrrp.Interfaces.Interface.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"slave-virtual-routers" : ("slave_virtual_routers", Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters), "version2" : ("version2", Vrrp.Interfaces.Interface.Ipv4.Version2), "version3" : ("version3", Vrrp.Interfaces.Interface.Ipv4.Version3)}
                    self._child_list_classes = {}

                    self.slave_virtual_routers = Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters()
                    self.slave_virtual_routers.parent = self
                    self._children_name_map["slave_virtual_routers"] = "slave-virtual-routers"
                    self._children_yang_names.add("slave-virtual-routers")

                    self.version2 = Vrrp.Interfaces.Interface.Ipv4.Version2()
                    self.version2.parent = self
                    self._children_name_map["version2"] = "version2"
                    self._children_yang_names.add("version2")

                    self.version3 = Vrrp.Interfaces.Interface.Ipv4.Version3()
                    self.version3.parent = self
                    self._children_name_map["version3"] = "version3"
                    self._children_yang_names.add("version3")
                    self._segment_path = lambda: "ipv4"


                class SlaveVirtualRouters(Entity):
                    """
                    The VRRP slave group configuration table
                    
                    .. attribute:: slave_virtual_router
                    
                    	The VRRP slave being configured
                    	**type**\: list of    :py:class:`SlaveVirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2017-05-19'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters, self).__init__()

                        self.yang_name = "slave-virtual-routers"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"slave-virtual-router" : ("slave_virtual_router", Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter)}

                        self.slave_virtual_router = YList(self)
                        self._segment_path = lambda: "slave-virtual-routers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters, [], name, value)


                    class SlaveVirtualRouter(Entity):
                        """
                        The VRRP slave being configured
                        
                        .. attribute:: slave_virtual_router_id  <key>
                        
                        	Virtual Router ID
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        .. attribute:: accept_mode_disable
                        
                        	Disable Accept Mode for this virtual IPAddress
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: follow
                        
                        	VRRP Session name for this slave to follow
                        	**type**\:  str
                        
                        .. attribute:: primary_ipv4_address
                        
                        	The Primary VRRP IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: secondary_ipv4_addresses
                        
                        	The table of VRRP secondary IPv4 addresses
                        	**type**\:   :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2017-05-19'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter, self).__init__()

                            self.yang_name = "slave-virtual-router"
                            self.yang_parent_name = "slave-virtual-routers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"secondary-ipv4-addresses" : ("secondary_ipv4_addresses", Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses)}
                            self._child_list_classes = {}

                            self.slave_virtual_router_id = YLeaf(YType.uint32, "slave-virtual-router-id")

                            self.accept_mode_disable = YLeaf(YType.empty, "accept-mode-disable")

                            self.follow = YLeaf(YType.str, "follow")

                            self.primary_ipv4_address = YLeaf(YType.str, "primary-ipv4-address")

                            self.secondary_ipv4_addresses = Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses()
                            self.secondary_ipv4_addresses.parent = self
                            self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                            self._children_yang_names.add("secondary-ipv4-addresses")
                            self._segment_path = lambda: "slave-virtual-router" + "[slave-virtual-router-id='" + self.slave_virtual_router_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter, ['slave_virtual_router_id', 'accept_mode_disable', 'follow', 'primary_ipv4_address'], name, value)


                        class SecondaryIpv4Addresses(Entity):
                            """
                            The table of VRRP secondary IPv4 addresses
                            
                            .. attribute:: secondary_ipv4_address
                            
                            	A VRRP secondary IPv4 address
                            	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2017-05-19'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses, self).__init__()

                                self.yang_name = "secondary-ipv4-addresses"
                                self.yang_parent_name = "slave-virtual-router"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"secondary-ipv4-address" : ("secondary_ipv4_address", Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address)}

                                self.secondary_ipv4_address = YList(self)
                                self._segment_path = lambda: "secondary-ipv4-addresses"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses, [], name, value)


                            class SecondaryIpv4Address(Entity):
                                """
                                A VRRP secondary IPv4 address
                                
                                .. attribute:: ip_address  <key>
                                
                                	VRRP Secondary IPv4 address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                    self.yang_name = "secondary-ipv4-address"
                                    self.yang_parent_name = "secondary-ipv4-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ip_address = YLeaf(YType.str, "ip-address")
                                    self._segment_path = lambda: "secondary-ipv4-address" + "[ip-address='" + self.ip_address.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, ['ip_address'], name, value)


                class Version2(Entity):
                    """
                    Version 2 VRRP configuration
                    
                    .. attribute:: virtual_routers
                    
                    	The VRRP virtual router configuration table
                    	**type**\:   :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2017-05-19'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv4.Version2, self).__init__()

                        self.yang_name = "version2"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"virtual-routers" : ("virtual_routers", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters)}
                        self._child_list_classes = {}

                        self.virtual_routers = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters()
                        self.virtual_routers.parent = self
                        self._children_name_map["virtual_routers"] = "virtual-routers"
                        self._children_yang_names.add("virtual-routers")
                        self._segment_path = lambda: "version2"


                    class VirtualRouters(Entity):
                        """
                        The VRRP virtual router configuration table
                        
                        .. attribute:: virtual_router
                        
                        	The VRRP virtual router being configured
                        	**type**\: list of    :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2017-05-19'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters, self).__init__()

                            self.yang_name = "virtual-routers"
                            self.yang_parent_name = "version2"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"virtual-router" : ("virtual_router", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter)}

                            self.virtual_router = YList(self)
                            self._segment_path = lambda: "virtual-routers"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters, [], name, value)


                        class VirtualRouter(Entity):
                            """
                            The VRRP virtual router being configured
                            
                            .. attribute:: vr_id  <key>
                            
                            	VRID Virtual Router Identifier
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            .. attribute:: accept_mode_disable
                            
                            	Disable Accept Mode for this virtual IPAddress
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection for this IP
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: preempt
                            
                            	Preempt Master router if higher priority
                            	**type**\:  int
                            
                            	**range:** 0..3600
                            
                            	**default value**\: 0
                            
                            .. attribute:: primary_ipv4_address
                            
                            	The Primary VRRP IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\:  int
                            
                            	**range:** 1..254
                            
                            	**default value**\: 100
                            
                            .. attribute:: secondary_ipv4_addresses
                            
                            	The table of VRRP secondary IPv4 addresses
                            	**type**\:   :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses>`
                            
                            .. attribute:: session_name
                            
                            	VRRP Session Name
                            	**type**\:  str
                            
                            	**length:** 1..16
                            
                            .. attribute:: text_password
                            
                            	Authentication password, 8 chars max
                            	**type**\:  str
                            
                            .. attribute:: timer
                            
                            	Set advertisement timer
                            	**type**\:   :py:class:`Timer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer>`
                            
                            .. attribute:: tracked_objects
                            
                            	Track an object, reducing priority if it goes down
                            	**type**\:   :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects>`
                            
                            .. attribute:: tracks
                            
                            	Track an item, reducing priority if it goes down
                            	**type**\:   :py:class:`Tracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2017-05-19'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter, self).__init__()

                                self.yang_name = "virtual-router"
                                self.yang_parent_name = "virtual-routers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"secondary-ipv4-addresses" : ("secondary_ipv4_addresses", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses), "timer" : ("timer", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer), "tracked-objects" : ("tracked_objects", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects), "tracks" : ("tracks", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks)}
                                self._child_list_classes = {}

                                self.vr_id = YLeaf(YType.uint32, "vr-id")

                                self.accept_mode_disable = YLeaf(YType.empty, "accept-mode-disable")

                                self.bfd = YLeaf(YType.str, "bfd")

                                self.preempt = YLeaf(YType.uint32, "preempt")

                                self.primary_ipv4_address = YLeaf(YType.str, "primary-ipv4-address")

                                self.priority = YLeaf(YType.uint32, "priority")

                                self.session_name = YLeaf(YType.str, "session-name")

                                self.text_password = YLeaf(YType.str, "text-password")

                                self.secondary_ipv4_addresses = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses()
                                self.secondary_ipv4_addresses.parent = self
                                self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                                self._children_yang_names.add("secondary-ipv4-addresses")

                                self.timer = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer()
                                self.timer.parent = self
                                self._children_name_map["timer"] = "timer"
                                self._children_yang_names.add("timer")

                                self.tracked_objects = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects()
                                self.tracked_objects.parent = self
                                self._children_name_map["tracked_objects"] = "tracked-objects"
                                self._children_yang_names.add("tracked-objects")

                                self.tracks = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks()
                                self.tracks.parent = self
                                self._children_name_map["tracks"] = "tracks"
                                self._children_yang_names.add("tracks")
                                self._segment_path = lambda: "virtual-router" + "[vr-id='" + self.vr_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter, ['vr_id', 'accept_mode_disable', 'bfd', 'preempt', 'primary_ipv4_address', 'priority', 'session_name', 'text_password'], name, value)


                            class SecondaryIpv4Addresses(Entity):
                                """
                                The table of VRRP secondary IPv4 addresses
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	A VRRP secondary IPv4 address
                                	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses, self).__init__()

                                    self.yang_name = "secondary-ipv4-addresses"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"secondary-ipv4-address" : ("secondary_ipv4_address", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address)}

                                    self.secondary_ipv4_address = YList(self)
                                    self._segment_path = lambda: "secondary-ipv4-addresses"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses, [], name, value)


                                class SecondaryIpv4Address(Entity):
                                    """
                                    A VRRP secondary IPv4 address
                                    
                                    .. attribute:: ip_address  <key>
                                    
                                    	VRRP Secondary IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2017-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                        self.yang_name = "secondary-ipv4-address"
                                        self.yang_parent_name = "secondary-ipv4-addresses"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.ip_address = YLeaf(YType.str, "ip-address")
                                        self._segment_path = lambda: "secondary-ipv4-address" + "[ip-address='" + self.ip_address.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, ['ip_address'], name, value)


                            class Timer(Entity):
                                """
                                Set advertisement timer
                                
                                .. attribute:: advertisement_time_in_msec
                                
                                	Advertisement time in milliseconds
                                	**type**\:  int
                                
                                	**range:** 100..40950
                                
                                	**units**\: millisecond
                                
                                .. attribute:: advertisement_time_in_sec
                                
                                	Advertisement time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                .. attribute:: forced
                                
                                	TRUE \- Force configured timer values to be used, required when configured in milliseconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: in_msec
                                
                                	TRUE \- Advertise time configured in milliseconds, FALSE \- Advertise time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer, self).__init__()

                                    self.yang_name = "timer"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.advertisement_time_in_msec = YLeaf(YType.uint32, "advertisement-time-in-msec")

                                    self.advertisement_time_in_sec = YLeaf(YType.uint32, "advertisement-time-in-sec")

                                    self.forced = YLeaf(YType.boolean, "forced")

                                    self.in_msec = YLeaf(YType.boolean, "in-msec")
                                    self._segment_path = lambda: "timer"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer, ['advertisement_time_in_msec', 'advertisement_time_in_sec', 'forced', 'in_msec'], name, value)


                            class TrackedObjects(Entity):
                                """
                                Track an object, reducing priority if it
                                goes down
                                
                                .. attribute:: tracked_object
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"tracked-object" : ("tracked_object", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject)}

                                    self.tracked_object = YList(self)
                                    self._segment_path = lambda: "tracked-objects"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects, [], name, value)


                                class TrackedObject(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: object_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2017-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__init__()

                                        self.yang_name = "tracked-object"
                                        self.yang_parent_name = "tracked-objects"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.object_name = YLeaf(YType.str, "object-name")

                                        self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")
                                        self._segment_path = lambda: "tracked-object" + "[object-name='" + self.object_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, ['object_name', 'priority_decrement'], name, value)


                            class Tracks(Entity):
                                """
                                Track an item, reducing priority if it
                                goes down
                                
                                .. attribute:: track
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks, self).__init__()

                                    self.yang_name = "tracks"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"track" : ("track", Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track)}

                                    self.track = YList(self)
                                    self._segment_path = lambda: "tracks"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks, [], name, value)


                                class Track(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                                    
                                    .. attribute:: priority
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2017-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track, self).__init__()

                                        self.yang_name = "track"
                                        self.yang_parent_name = "tracks"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.interface_name = YLeaf(YType.str, "interface-name")

                                        self.priority = YLeaf(YType.uint32, "priority")
                                        self._segment_path = lambda: "track" + "[interface-name='" + self.interface_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track, ['interface_name', 'priority'], name, value)


                class Version3(Entity):
                    """
                    Version 3 VRRP configuration
                    
                    .. attribute:: virtual_routers
                    
                    	The VRRP virtual router configuration table
                    	**type**\:   :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2017-05-19'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv4.Version3, self).__init__()

                        self.yang_name = "version3"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"virtual-routers" : ("virtual_routers", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters)}
                        self._child_list_classes = {}

                        self.virtual_routers = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters()
                        self.virtual_routers.parent = self
                        self._children_name_map["virtual_routers"] = "virtual-routers"
                        self._children_yang_names.add("virtual-routers")
                        self._segment_path = lambda: "version3"


                    class VirtualRouters(Entity):
                        """
                        The VRRP virtual router configuration table
                        
                        .. attribute:: virtual_router
                        
                        	The VRRP virtual router being configured
                        	**type**\: list of    :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2017-05-19'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters, self).__init__()

                            self.yang_name = "virtual-routers"
                            self.yang_parent_name = "version3"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"virtual-router" : ("virtual_router", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter)}

                            self.virtual_router = YList(self)
                            self._segment_path = lambda: "virtual-routers"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters, [], name, value)


                        class VirtualRouter(Entity):
                            """
                            The VRRP virtual router being configured
                            
                            .. attribute:: vr_id  <key>
                            
                            	VRID Virtual Router Identifier
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            .. attribute:: accept_mode_disable
                            
                            	Disable Accept Mode for this virtual IPAddress
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection for this IP
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: preempt
                            
                            	Preempt Master router if higher priority
                            	**type**\:  int
                            
                            	**range:** 0..3600
                            
                            	**default value**\: 0
                            
                            .. attribute:: primary_ipv4_address
                            
                            	The Primary VRRP IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\:  int
                            
                            	**range:** 1..254
                            
                            	**default value**\: 100
                            
                            .. attribute:: secondary_ipv4_addresses
                            
                            	The table of VRRP secondary IPv4 addresses
                            	**type**\:   :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses>`
                            
                            .. attribute:: session_name
                            
                            	VRRP Session Name
                            	**type**\:  str
                            
                            	**length:** 1..16
                            
                            .. attribute:: timer
                            
                            	Set advertisement timer
                            	**type**\:   :py:class:`Timer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer>`
                            
                            .. attribute:: tracked_objects
                            
                            	Track an object, reducing priority if it goes down
                            	**type**\:   :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects>`
                            
                            .. attribute:: tracks
                            
                            	Track an item, reducing priority if it goes down
                            	**type**\:   :py:class:`Tracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2017-05-19'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter, self).__init__()

                                self.yang_name = "virtual-router"
                                self.yang_parent_name = "virtual-routers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"secondary-ipv4-addresses" : ("secondary_ipv4_addresses", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses), "timer" : ("timer", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer), "tracked-objects" : ("tracked_objects", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects), "tracks" : ("tracks", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks)}
                                self._child_list_classes = {}

                                self.vr_id = YLeaf(YType.uint32, "vr-id")

                                self.accept_mode_disable = YLeaf(YType.empty, "accept-mode-disable")

                                self.bfd = YLeaf(YType.str, "bfd")

                                self.preempt = YLeaf(YType.uint32, "preempt")

                                self.primary_ipv4_address = YLeaf(YType.str, "primary-ipv4-address")

                                self.priority = YLeaf(YType.uint32, "priority")

                                self.session_name = YLeaf(YType.str, "session-name")

                                self.secondary_ipv4_addresses = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses()
                                self.secondary_ipv4_addresses.parent = self
                                self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                                self._children_yang_names.add("secondary-ipv4-addresses")

                                self.timer = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer()
                                self.timer.parent = self
                                self._children_name_map["timer"] = "timer"
                                self._children_yang_names.add("timer")

                                self.tracked_objects = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects()
                                self.tracked_objects.parent = self
                                self._children_name_map["tracked_objects"] = "tracked-objects"
                                self._children_yang_names.add("tracked-objects")

                                self.tracks = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks()
                                self.tracks.parent = self
                                self._children_name_map["tracks"] = "tracks"
                                self._children_yang_names.add("tracks")
                                self._segment_path = lambda: "virtual-router" + "[vr-id='" + self.vr_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter, ['vr_id', 'accept_mode_disable', 'bfd', 'preempt', 'primary_ipv4_address', 'priority', 'session_name'], name, value)


                            class SecondaryIpv4Addresses(Entity):
                                """
                                The table of VRRP secondary IPv4 addresses
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	A VRRP secondary IPv4 address
                                	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses, self).__init__()

                                    self.yang_name = "secondary-ipv4-addresses"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"secondary-ipv4-address" : ("secondary_ipv4_address", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address)}

                                    self.secondary_ipv4_address = YList(self)
                                    self._segment_path = lambda: "secondary-ipv4-addresses"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses, [], name, value)


                                class SecondaryIpv4Address(Entity):
                                    """
                                    A VRRP secondary IPv4 address
                                    
                                    .. attribute:: ip_address  <key>
                                    
                                    	VRRP Secondary IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2017-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                        self.yang_name = "secondary-ipv4-address"
                                        self.yang_parent_name = "secondary-ipv4-addresses"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.ip_address = YLeaf(YType.str, "ip-address")
                                        self._segment_path = lambda: "secondary-ipv4-address" + "[ip-address='" + self.ip_address.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, ['ip_address'], name, value)


                            class Timer(Entity):
                                """
                                Set advertisement timer
                                
                                .. attribute:: advertisement_time_in_msec
                                
                                	Advertisement time in milliseconds
                                	**type**\:  int
                                
                                	**range:** 100..40950
                                
                                	**units**\: millisecond
                                
                                .. attribute:: advertisement_time_in_sec
                                
                                	Advertisement time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..40
                                
                                	**units**\: second
                                
                                .. attribute:: forced
                                
                                	TRUE \- Force configured timer values to be used, required when configured in milliseconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: in_msec
                                
                                	TRUE \- Advertise time configured in milliseconds, FALSE \- Advertise time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer, self).__init__()

                                    self.yang_name = "timer"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.advertisement_time_in_msec = YLeaf(YType.uint32, "advertisement-time-in-msec")

                                    self.advertisement_time_in_sec = YLeaf(YType.uint32, "advertisement-time-in-sec")

                                    self.forced = YLeaf(YType.boolean, "forced")

                                    self.in_msec = YLeaf(YType.boolean, "in-msec")
                                    self._segment_path = lambda: "timer"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer, ['advertisement_time_in_msec', 'advertisement_time_in_sec', 'forced', 'in_msec'], name, value)


                            class TrackedObjects(Entity):
                                """
                                Track an object, reducing priority if it
                                goes down
                                
                                .. attribute:: tracked_object
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"tracked-object" : ("tracked_object", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject)}

                                    self.tracked_object = YList(self)
                                    self._segment_path = lambda: "tracked-objects"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects, [], name, value)


                                class TrackedObject(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: object_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2017-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__init__()

                                        self.yang_name = "tracked-object"
                                        self.yang_parent_name = "tracked-objects"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.object_name = YLeaf(YType.str, "object-name")

                                        self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")
                                        self._segment_path = lambda: "tracked-object" + "[object-name='" + self.object_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, ['object_name', 'priority_decrement'], name, value)


                            class Tracks(Entity):
                                """
                                Track an item, reducing priority if it
                                goes down
                                
                                .. attribute:: track
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks, self).__init__()

                                    self.yang_name = "tracks"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"track" : ("track", Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track)}

                                    self.track = YList(self)
                                    self._segment_path = lambda: "tracks"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks, [], name, value)


                                class Track(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                                    
                                    .. attribute:: priority
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2017-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track, self).__init__()

                                        self.yang_name = "track"
                                        self.yang_parent_name = "tracks"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.interface_name = YLeaf(YType.str, "interface-name")

                                        self.priority = YLeaf(YType.uint32, "priority")
                                        self._segment_path = lambda: "track" + "[interface-name='" + self.interface_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track, ['interface_name', 'priority'], name, value)


            class Ipv6(Entity):
                """
                IPv6 VRRP configuration
                
                .. attribute:: slave_virtual_routers
                
                	The VRRP slave group configuration table
                	**type**\:   :py:class:`SlaveVirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters>`
                
                .. attribute:: version3
                
                	Version 3 VRRP configuration
                	**type**\:   :py:class:`Version3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3>`
                
                

                """

                _prefix = 'ipv4-vrrp-cfg'
                _revision = '2017-05-19'

                def __init__(self):
                    super(Vrrp.Interfaces.Interface.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"slave-virtual-routers" : ("slave_virtual_routers", Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters), "version3" : ("version3", Vrrp.Interfaces.Interface.Ipv6.Version3)}
                    self._child_list_classes = {}

                    self.slave_virtual_routers = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters()
                    self.slave_virtual_routers.parent = self
                    self._children_name_map["slave_virtual_routers"] = "slave-virtual-routers"
                    self._children_yang_names.add("slave-virtual-routers")

                    self.version3 = Vrrp.Interfaces.Interface.Ipv6.Version3()
                    self.version3.parent = self
                    self._children_name_map["version3"] = "version3"
                    self._children_yang_names.add("version3")
                    self._segment_path = lambda: "ipv6"


                class SlaveVirtualRouters(Entity):
                    """
                    The VRRP slave group configuration table
                    
                    .. attribute:: slave_virtual_router
                    
                    	The VRRP slave being configured
                    	**type**\: list of    :py:class:`SlaveVirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2017-05-19'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters, self).__init__()

                        self.yang_name = "slave-virtual-routers"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"slave-virtual-router" : ("slave_virtual_router", Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter)}

                        self.slave_virtual_router = YList(self)
                        self._segment_path = lambda: "slave-virtual-routers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters, [], name, value)


                    class SlaveVirtualRouter(Entity):
                        """
                        The VRRP slave being configured
                        
                        .. attribute:: slave_virtual_router_id  <key>
                        
                        	Virtual Router ID
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        .. attribute:: accept_mode_disable
                        
                        	Disable Accept Mode for this virtual IPAddress
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: follow
                        
                        	VRRP Session name for this slave to follow
                        	**type**\:  str
                        
                        .. attribute:: global_ipv6_addresses
                        
                        	The table of VRRP virtual global IPv6 addresses
                        	**type**\:   :py:class:`GlobalIpv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses>`
                        
                        .. attribute:: link_local_ipv6_address
                        
                        	The VRRP IPv6 virtual linklocal address
                        	**type**\:   :py:class:`LinkLocalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2017-05-19'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter, self).__init__()

                            self.yang_name = "slave-virtual-router"
                            self.yang_parent_name = "slave-virtual-routers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"global-ipv6-addresses" : ("global_ipv6_addresses", Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses), "link-local-ipv6-address" : ("link_local_ipv6_address", Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address)}
                            self._child_list_classes = {}

                            self.slave_virtual_router_id = YLeaf(YType.uint32, "slave-virtual-router-id")

                            self.accept_mode_disable = YLeaf(YType.empty, "accept-mode-disable")

                            self.follow = YLeaf(YType.str, "follow")

                            self.global_ipv6_addresses = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses()
                            self.global_ipv6_addresses.parent = self
                            self._children_name_map["global_ipv6_addresses"] = "global-ipv6-addresses"
                            self._children_yang_names.add("global-ipv6-addresses")

                            self.link_local_ipv6_address = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address()
                            self.link_local_ipv6_address.parent = self
                            self._children_name_map["link_local_ipv6_address"] = "link-local-ipv6-address"
                            self._children_yang_names.add("link-local-ipv6-address")
                            self._segment_path = lambda: "slave-virtual-router" + "[slave-virtual-router-id='" + self.slave_virtual_router_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter, ['slave_virtual_router_id', 'accept_mode_disable', 'follow'], name, value)


                        class GlobalIpv6Addresses(Entity):
                            """
                            The table of VRRP virtual global IPv6
                            addresses
                            
                            .. attribute:: global_ipv6_address
                            
                            	A VRRP virtual global IPv6 IP address
                            	**type**\: list of    :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2017-05-19'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses, self).__init__()

                                self.yang_name = "global-ipv6-addresses"
                                self.yang_parent_name = "slave-virtual-router"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"global-ipv6-address" : ("global_ipv6_address", Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address)}

                                self.global_ipv6_address = YList(self)
                                self._segment_path = lambda: "global-ipv6-addresses"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses, [], name, value)


                            class GlobalIpv6Address(Entity):
                                """
                                A VRRP virtual global IPv6 IP address
                                
                                .. attribute:: ip_address  <key>
                                
                                	VRRP virtual global IPv6 address
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address, self).__init__()

                                    self.yang_name = "global-ipv6-address"
                                    self.yang_parent_name = "global-ipv6-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ip_address = YLeaf(YType.str, "ip-address")
                                    self._segment_path = lambda: "global-ipv6-address" + "[ip-address='" + self.ip_address.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address, ['ip_address'], name, value)


                        class LinkLocalIpv6Address(Entity):
                            """
                            The VRRP IPv6 virtual linklocal address
                            
                            .. attribute:: auto_configure
                            
                            	TRUE if the virtual linklocal address is to be autoconfigured FALSE if an IPv6 virtual linklocal address is configured
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            .. attribute:: ip_address
                            
                            	VRRP IPv6 virtual linklocal address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2017-05-19'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address, self).__init__()

                                self.yang_name = "link-local-ipv6-address"
                                self.yang_parent_name = "slave-virtual-router"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.auto_configure = YLeaf(YType.boolean, "auto-configure")

                                self.ip_address = YLeaf(YType.str, "ip-address")
                                self._segment_path = lambda: "link-local-ipv6-address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address, ['auto_configure', 'ip_address'], name, value)


                class Version3(Entity):
                    """
                    Version 3 VRRP configuration
                    
                    .. attribute:: virtual_routers
                    
                    	The VRRP virtual router configuration table
                    	**type**\:   :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2017-05-19'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv6.Version3, self).__init__()

                        self.yang_name = "version3"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"virtual-routers" : ("virtual_routers", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters)}
                        self._child_list_classes = {}

                        self.virtual_routers = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters()
                        self.virtual_routers.parent = self
                        self._children_name_map["virtual_routers"] = "virtual-routers"
                        self._children_yang_names.add("virtual-routers")
                        self._segment_path = lambda: "version3"


                    class VirtualRouters(Entity):
                        """
                        The VRRP virtual router configuration table
                        
                        .. attribute:: virtual_router
                        
                        	The VRRP virtual router being configured
                        	**type**\: list of    :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2017-05-19'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters, self).__init__()

                            self.yang_name = "virtual-routers"
                            self.yang_parent_name = "version3"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"virtual-router" : ("virtual_router", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter)}

                            self.virtual_router = YList(self)
                            self._segment_path = lambda: "virtual-routers"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters, [], name, value)


                        class VirtualRouter(Entity):
                            """
                            The VRRP virtual router being configured
                            
                            .. attribute:: vr_id  <key>
                            
                            	VRID Virtual Router Identifier
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            .. attribute:: accept_mode_disable
                            
                            	Disable Accept Mode for this virtual IPAddress
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection for this IP
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: global_ipv6_addresses
                            
                            	The table of VRRP virtual global IPv6 addresses
                            	**type**\:   :py:class:`GlobalIpv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses>`
                            
                            .. attribute:: link_local_ipv6_address
                            
                            	The VRRP IPv6 virtual linklocal address
                            	**type**\:   :py:class:`LinkLocalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address>`
                            
                            .. attribute:: preempt
                            
                            	Preempt Master router if higher priority
                            	**type**\:  int
                            
                            	**range:** 0..3600
                            
                            	**default value**\: 0
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\:  int
                            
                            	**range:** 1..254
                            
                            	**default value**\: 100
                            
                            .. attribute:: session_name
                            
                            	VRRP Session Name
                            	**type**\:  str
                            
                            	**length:** 1..16
                            
                            .. attribute:: timer
                            
                            	Set advertisement timer
                            	**type**\:   :py:class:`Timer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer>`
                            
                            .. attribute:: tracked_objects
                            
                            	Track an object, reducing priority if it goes down
                            	**type**\:   :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects>`
                            
                            .. attribute:: tracks
                            
                            	Track an item, reducing priority if it goes down
                            	**type**\:   :py:class:`Tracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2017-05-19'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter, self).__init__()

                                self.yang_name = "virtual-router"
                                self.yang_parent_name = "virtual-routers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"global-ipv6-addresses" : ("global_ipv6_addresses", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses), "link-local-ipv6-address" : ("link_local_ipv6_address", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address), "timer" : ("timer", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer), "tracked-objects" : ("tracked_objects", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects), "tracks" : ("tracks", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks)}
                                self._child_list_classes = {}

                                self.vr_id = YLeaf(YType.uint32, "vr-id")

                                self.accept_mode_disable = YLeaf(YType.empty, "accept-mode-disable")

                                self.bfd = YLeaf(YType.str, "bfd")

                                self.preempt = YLeaf(YType.uint32, "preempt")

                                self.priority = YLeaf(YType.uint32, "priority")

                                self.session_name = YLeaf(YType.str, "session-name")

                                self.global_ipv6_addresses = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses()
                                self.global_ipv6_addresses.parent = self
                                self._children_name_map["global_ipv6_addresses"] = "global-ipv6-addresses"
                                self._children_yang_names.add("global-ipv6-addresses")

                                self.link_local_ipv6_address = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address()
                                self.link_local_ipv6_address.parent = self
                                self._children_name_map["link_local_ipv6_address"] = "link-local-ipv6-address"
                                self._children_yang_names.add("link-local-ipv6-address")

                                self.timer = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer()
                                self.timer.parent = self
                                self._children_name_map["timer"] = "timer"
                                self._children_yang_names.add("timer")

                                self.tracked_objects = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects()
                                self.tracked_objects.parent = self
                                self._children_name_map["tracked_objects"] = "tracked-objects"
                                self._children_yang_names.add("tracked-objects")

                                self.tracks = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks()
                                self.tracks.parent = self
                                self._children_name_map["tracks"] = "tracks"
                                self._children_yang_names.add("tracks")
                                self._segment_path = lambda: "virtual-router" + "[vr-id='" + self.vr_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter, ['vr_id', 'accept_mode_disable', 'bfd', 'preempt', 'priority', 'session_name'], name, value)


                            class GlobalIpv6Addresses(Entity):
                                """
                                The table of VRRP virtual global IPv6
                                addresses
                                
                                .. attribute:: global_ipv6_address
                                
                                	A VRRP virtual global IPv6 IP address
                                	**type**\: list of    :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses, self).__init__()

                                    self.yang_name = "global-ipv6-addresses"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"global-ipv6-address" : ("global_ipv6_address", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address)}

                                    self.global_ipv6_address = YList(self)
                                    self._segment_path = lambda: "global-ipv6-addresses"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses, [], name, value)


                                class GlobalIpv6Address(Entity):
                                    """
                                    A VRRP virtual global IPv6 IP address
                                    
                                    .. attribute:: ip_address  <key>
                                    
                                    	VRRP virtual global IPv6 address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2017-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address, self).__init__()

                                        self.yang_name = "global-ipv6-address"
                                        self.yang_parent_name = "global-ipv6-addresses"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.ip_address = YLeaf(YType.str, "ip-address")
                                        self._segment_path = lambda: "global-ipv6-address" + "[ip-address='" + self.ip_address.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address, ['ip_address'], name, value)


                            class LinkLocalIpv6Address(Entity):
                                """
                                The VRRP IPv6 virtual linklocal address
                                
                                .. attribute:: auto_configure
                                
                                	TRUE if the virtual linklocal address is to be autoconfigured FALSE if an IPv6 virtual linklocal address is configured
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: ip_address
                                
                                	VRRP IPv6 virtual linklocal address
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address, self).__init__()

                                    self.yang_name = "link-local-ipv6-address"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.auto_configure = YLeaf(YType.boolean, "auto-configure")

                                    self.ip_address = YLeaf(YType.str, "ip-address")
                                    self._segment_path = lambda: "link-local-ipv6-address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address, ['auto_configure', 'ip_address'], name, value)


                            class Timer(Entity):
                                """
                                Set advertisement timer
                                
                                .. attribute:: advertisement_time_in_msec
                                
                                	Advertisement time in milliseconds
                                	**type**\:  int
                                
                                	**range:** 100..40950
                                
                                	**units**\: millisecond
                                
                                .. attribute:: advertisement_time_in_sec
                                
                                	Advertisement time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..40
                                
                                	**units**\: second
                                
                                .. attribute:: forced
                                
                                	TRUE \- Force configured timer values to be used, required when configured in milliseconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: in_msec
                                
                                	TRUE \- Advertise time configured in milliseconds, FALSE \- Advertise time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer, self).__init__()

                                    self.yang_name = "timer"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.advertisement_time_in_msec = YLeaf(YType.uint32, "advertisement-time-in-msec")

                                    self.advertisement_time_in_sec = YLeaf(YType.uint32, "advertisement-time-in-sec")

                                    self.forced = YLeaf(YType.boolean, "forced")

                                    self.in_msec = YLeaf(YType.boolean, "in-msec")
                                    self._segment_path = lambda: "timer"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer, ['advertisement_time_in_msec', 'advertisement_time_in_sec', 'forced', 'in_msec'], name, value)


                            class TrackedObjects(Entity):
                                """
                                Track an object, reducing priority if it
                                goes down
                                
                                .. attribute:: tracked_object
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"tracked-object" : ("tracked_object", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject)}

                                    self.tracked_object = YList(self)
                                    self._segment_path = lambda: "tracked-objects"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects, [], name, value)


                                class TrackedObject(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: object_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2017-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__init__()

                                        self.yang_name = "tracked-object"
                                        self.yang_parent_name = "tracked-objects"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.object_name = YLeaf(YType.str, "object-name")

                                        self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")
                                        self._segment_path = lambda: "tracked-object" + "[object-name='" + self.object_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, ['object_name', 'priority_decrement'], name, value)


                            class Tracks(Entity):
                                """
                                Track an item, reducing priority if it
                                goes down
                                
                                .. attribute:: track
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2017-05-19'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks, self).__init__()

                                    self.yang_name = "tracks"
                                    self.yang_parent_name = "virtual-router"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"track" : ("track", Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track)}

                                    self.track = YList(self)
                                    self._segment_path = lambda: "tracks"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks, [], name, value)


                                class Track(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                                    
                                    .. attribute:: priority
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2017-05-19'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track, self).__init__()

                                        self.yang_name = "track"
                                        self.yang_parent_name = "tracks"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.interface_name = YLeaf(YType.str, "interface-name")

                                        self.priority = YLeaf(YType.uint32, "priority")
                                        self._segment_path = lambda: "track" + "[interface-name='" + self.interface_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track, ['interface_name', 'priority'], name, value)


    class Logging(Entity):
        """
        VRRP logging options
        
        .. attribute:: state_change_disable
        
        	VRRP state change IOS messages disable
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ipv4-vrrp-cfg'
        _revision = '2017-05-19'

        def __init__(self):
            super(Vrrp.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "vrrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.state_change_disable = YLeaf(YType.empty, "state-change-disable")
            self._segment_path = lambda: "logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Vrrp.Logging, ['state_change_disable'], name, value)

    def clone_ptr(self):
        self._top_entity = Vrrp()
        return self._top_entity

