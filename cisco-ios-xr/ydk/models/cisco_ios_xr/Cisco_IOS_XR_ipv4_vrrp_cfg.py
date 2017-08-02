""" Cisco_IOS_XR_ipv4_vrrp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-vrrp package configuration.

This module contains definitions
for the following management objects\:
  vrrp\: VRRP configuration

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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
    _revision = '2016-12-16'

    def __init__(self):
        super(Vrrp, self).__init__()
        self._top_entity = None

        self.yang_name = "vrrp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-vrrp-cfg"

        self.interfaces = Vrrp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.logging = Vrrp.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"
        self._children_yang_names.add("logging")


    class Logging(Entity):
        """
        VRRP logging options
        
        .. attribute:: state_change_disable
        
        	VRRP state change IOS messages disable
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ipv4-vrrp-cfg'
        _revision = '2016-12-16'

        def __init__(self):
            super(Vrrp.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "vrrp"

            self.state_change_disable = YLeaf(YType.empty, "state-change-disable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("state_change_disable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vrrp.Logging, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vrrp.Logging, self).__setattr__(name, value)

        def has_data(self):
            return self.state_change_disable.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.state_change_disable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "logging" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.state_change_disable.is_set or self.state_change_disable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.state_change_disable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "state-change-disable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "state-change-disable"):
                self.state_change_disable = value
                self.state_change_disable.value_namespace = name_space
                self.state_change_disable.value_namespace_prefix = name_space_prefix


    class Interfaces(Entity):
        """
        Interface configuration table
        
        .. attribute:: interface
        
        	The interface being configured
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-vrrp-cfg'
        _revision = '2016-12-16'

        def __init__(self):
            super(Vrrp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "vrrp"

            self.interface = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vrrp.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vrrp.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            The interface being configured
            
            .. attribute:: interface_name  <key>
            
            	Interface name to configure
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: bfd
            
            	BFD configuration
            	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Bfd>`
            
            .. attribute:: delay
            
            	Minimum and Reload Delay
            	**type**\:   :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Delay>`
            
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
            _revision = '2016-12-16'

            def __init__(self):
                super(Vrrp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.mac_refresh = YLeaf(YType.uint32, "mac-refresh")

                self.bfd = Vrrp.Interfaces.Interface.Bfd()
                self.bfd.parent = self
                self._children_name_map["bfd"] = "bfd"
                self._children_yang_names.add("bfd")

                self.delay = Vrrp.Interfaces.Interface.Delay()
                self.delay.parent = self
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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name",
                                "mac_refresh") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vrrp.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vrrp.Interfaces.Interface, self).__setattr__(name, value)


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
                _revision = '2016-12-16'

                def __init__(self):
                    super(Vrrp.Interfaces.Interface.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "interface"

                    self.slave_virtual_routers = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters()
                    self.slave_virtual_routers.parent = self
                    self._children_name_map["slave_virtual_routers"] = "slave-virtual-routers"
                    self._children_yang_names.add("slave-virtual-routers")

                    self.version3 = Vrrp.Interfaces.Interface.Ipv6.Version3()
                    self.version3.parent = self
                    self._children_name_map["version3"] = "version3"
                    self._children_yang_names.add("version3")


                class Version3(Entity):
                    """
                    Version 3 VRRP configuration
                    
                    .. attribute:: virtual_routers
                    
                    	The VRRP virtual router configuration table
                    	**type**\:   :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2016-12-16'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv6.Version3, self).__init__()

                        self.yang_name = "version3"
                        self.yang_parent_name = "ipv6"

                        self.virtual_routers = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters()
                        self.virtual_routers.parent = self
                        self._children_name_map["virtual_routers"] = "virtual-routers"
                        self._children_yang_names.add("virtual-routers")


                    class VirtualRouters(Entity):
                        """
                        The VRRP virtual router configuration table
                        
                        .. attribute:: virtual_router
                        
                        	The VRRP virtual router being configured
                        	**type**\: list of    :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2016-12-16'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters, self).__init__()

                            self.yang_name = "virtual-routers"
                            self.yang_parent_name = "version3"

                            self.virtual_router = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters, self).__setattr__(name, value)


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
                            _revision = '2016-12-16'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter, self).__init__()

                                self.yang_name = "virtual-router"
                                self.yang_parent_name = "virtual-routers"

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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("vr_id",
                                                "accept_mode_disable",
                                                "bfd",
                                                "preempt",
                                                "priority",
                                                "session_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter, self).__setattr__(name, value)


                            class GlobalIpv6Addresses(Entity):
                                """
                                The table of VRRP virtual global IPv6
                                addresses
                                
                                .. attribute:: global_ipv6_address
                                
                                	A VRRP virtual global IPv6 IP address
                                	**type**\: list of    :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses, self).__init__()

                                    self.yang_name = "global-ipv6-addresses"
                                    self.yang_parent_name = "virtual-router"

                                    self.global_ipv6_address = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses, self).__setattr__(name, value)


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
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address, self).__init__()

                                        self.yang_name = "global-ipv6-address"
                                        self.yang_parent_name = "global-ipv6-addresses"

                                        self.ip_address = YLeaf(YType.str, "ip-address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("ip_address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return self.ip_address.is_set

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.ip_address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "global-ipv6-address" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ip_address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "ip-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "ip-address"):
                                            self.ip_address = value
                                            self.ip_address.value_namespace = name_space
                                            self.ip_address.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.global_ipv6_address:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.global_ipv6_address:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "global-ipv6-addresses" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "global-ipv6-address"):
                                        for c in self.global_ipv6_address:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.global_ipv6_address.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "global-ipv6-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class Tracks(Entity):
                                """
                                Track an item, reducing priority if it
                                goes down
                                
                                .. attribute:: track
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks, self).__init__()

                                    self.yang_name = "tracks"
                                    self.yang_parent_name = "virtual-router"

                                    self.track = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks, self).__setattr__(name, value)


                                class Track(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: priority
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track, self).__init__()

                                        self.yang_name = "track"
                                        self.yang_parent_name = "tracks"

                                        self.interface_name = YLeaf(YType.str, "interface-name")

                                        self.priority = YLeaf(YType.uint32, "priority")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("interface_name",
                                                        "priority") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.interface_name.is_set or
                                            self.priority.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.interface_name.yfilter != YFilter.not_set or
                                            self.priority.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "track" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                                        if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.priority.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "interface-name" or name == "priority"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "interface-name"):
                                            self.interface_name = value
                                            self.interface_name.value_namespace = name_space
                                            self.interface_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "priority"):
                                            self.priority = value
                                            self.priority.value_namespace = name_space
                                            self.priority.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.track:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.track:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tracks" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "track"):
                                        for c in self.track:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks.Track()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.track.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "track"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


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
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer, self).__init__()

                                    self.yang_name = "timer"
                                    self.yang_parent_name = "virtual-router"

                                    self.advertisement_time_in_msec = YLeaf(YType.uint32, "advertisement-time-in-msec")

                                    self.advertisement_time_in_sec = YLeaf(YType.uint32, "advertisement-time-in-sec")

                                    self.forced = YLeaf(YType.boolean, "forced")

                                    self.in_msec = YLeaf(YType.boolean, "in-msec")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("advertisement_time_in_msec",
                                                    "advertisement_time_in_sec",
                                                    "forced",
                                                    "in_msec") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.advertisement_time_in_msec.is_set or
                                        self.advertisement_time_in_sec.is_set or
                                        self.forced.is_set or
                                        self.in_msec.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.advertisement_time_in_msec.yfilter != YFilter.not_set or
                                        self.advertisement_time_in_sec.yfilter != YFilter.not_set or
                                        self.forced.yfilter != YFilter.not_set or
                                        self.in_msec.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "timer" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.advertisement_time_in_msec.is_set or self.advertisement_time_in_msec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.advertisement_time_in_msec.get_name_leafdata())
                                    if (self.advertisement_time_in_sec.is_set or self.advertisement_time_in_sec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.advertisement_time_in_sec.get_name_leafdata())
                                    if (self.forced.is_set or self.forced.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.forced.get_name_leafdata())
                                    if (self.in_msec.is_set or self.in_msec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.in_msec.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "advertisement-time-in-msec" or name == "advertisement-time-in-sec" or name == "forced" or name == "in-msec"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "advertisement-time-in-msec"):
                                        self.advertisement_time_in_msec = value
                                        self.advertisement_time_in_msec.value_namespace = name_space
                                        self.advertisement_time_in_msec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "advertisement-time-in-sec"):
                                        self.advertisement_time_in_sec = value
                                        self.advertisement_time_in_sec.value_namespace = name_space
                                        self.advertisement_time_in_sec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "forced"):
                                        self.forced = value
                                        self.forced.value_namespace = name_space
                                        self.forced.value_namespace_prefix = name_space_prefix
                                    if(value_path == "in-msec"):
                                        self.in_msec = value
                                        self.in_msec.value_namespace = name_space
                                        self.in_msec.value_namespace_prefix = name_space_prefix


                            class TrackedObjects(Entity):
                                """
                                Track an object, reducing priority if it
                                goes down
                                
                                .. attribute:: tracked_object
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "virtual-router"

                                    self.tracked_object = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects, self).__setattr__(name, value)


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
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__init__()

                                        self.yang_name = "tracked-object"
                                        self.yang_parent_name = "tracked-objects"

                                        self.object_name = YLeaf(YType.str, "object-name")

                                        self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("object_name",
                                                        "priority_decrement") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.object_name.is_set or
                                            self.priority_decrement.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.object_name.yfilter != YFilter.not_set or
                                            self.priority_decrement.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "tracked-object" + "[object-name='" + self.object_name.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.object_name.get_name_leafdata())
                                        if (self.priority_decrement.is_set or self.priority_decrement.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.priority_decrement.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "object-name" or name == "priority-decrement"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "object-name"):
                                            self.object_name = value
                                            self.object_name.value_namespace = name_space
                                            self.object_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "priority-decrement"):
                                            self.priority_decrement = value
                                            self.priority_decrement.value_namespace = name_space
                                            self.priority_decrement.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.tracked_object:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.tracked_object:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tracked-objects" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "tracked-object"):
                                        for c in self.tracked_object:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.tracked_object.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "tracked-object"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


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
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address, self).__init__()

                                    self.yang_name = "link-local-ipv6-address"
                                    self.yang_parent_name = "virtual-router"

                                    self.auto_configure = YLeaf(YType.boolean, "auto-configure")

                                    self.ip_address = YLeaf(YType.str, "ip-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("auto_configure",
                                                    "ip_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.auto_configure.is_set or
                                        self.ip_address.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.auto_configure.yfilter != YFilter.not_set or
                                        self.ip_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "link-local-ipv6-address" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.auto_configure.is_set or self.auto_configure.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.auto_configure.get_name_leafdata())
                                    if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ip_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "auto-configure" or name == "ip-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "auto-configure"):
                                        self.auto_configure = value
                                        self.auto_configure.value_namespace = name_space
                                        self.auto_configure.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ip-address"):
                                        self.ip_address = value
                                        self.ip_address.value_namespace = name_space
                                        self.ip_address.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.vr_id.is_set or
                                    self.accept_mode_disable.is_set or
                                    self.bfd.is_set or
                                    self.preempt.is_set or
                                    self.priority.is_set or
                                    self.session_name.is_set or
                                    (self.global_ipv6_addresses is not None and self.global_ipv6_addresses.has_data()) or
                                    (self.link_local_ipv6_address is not None and self.link_local_ipv6_address.has_data()) or
                                    (self.timer is not None and self.timer.has_data()) or
                                    (self.tracked_objects is not None and self.tracked_objects.has_data()) or
                                    (self.tracks is not None and self.tracks.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.vr_id.yfilter != YFilter.not_set or
                                    self.accept_mode_disable.yfilter != YFilter.not_set or
                                    self.bfd.yfilter != YFilter.not_set or
                                    self.preempt.yfilter != YFilter.not_set or
                                    self.priority.yfilter != YFilter.not_set or
                                    self.session_name.yfilter != YFilter.not_set or
                                    (self.global_ipv6_addresses is not None and self.global_ipv6_addresses.has_operation()) or
                                    (self.link_local_ipv6_address is not None and self.link_local_ipv6_address.has_operation()) or
                                    (self.timer is not None and self.timer.has_operation()) or
                                    (self.tracked_objects is not None and self.tracked_objects.has_operation()) or
                                    (self.tracks is not None and self.tracks.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "virtual-router" + "[vr-id='" + self.vr_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.vr_id.is_set or self.vr_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vr_id.get_name_leafdata())
                                if (self.accept_mode_disable.is_set or self.accept_mode_disable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.accept_mode_disable.get_name_leafdata())
                                if (self.bfd.is_set or self.bfd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bfd.get_name_leafdata())
                                if (self.preempt.is_set or self.preempt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.preempt.get_name_leafdata())
                                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority.get_name_leafdata())
                                if (self.session_name.is_set or self.session_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "global-ipv6-addresses"):
                                    if (self.global_ipv6_addresses is None):
                                        self.global_ipv6_addresses = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.GlobalIpv6Addresses()
                                        self.global_ipv6_addresses.parent = self
                                        self._children_name_map["global_ipv6_addresses"] = "global-ipv6-addresses"
                                    return self.global_ipv6_addresses

                                if (child_yang_name == "link-local-ipv6-address"):
                                    if (self.link_local_ipv6_address is None):
                                        self.link_local_ipv6_address = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.LinkLocalIpv6Address()
                                        self.link_local_ipv6_address.parent = self
                                        self._children_name_map["link_local_ipv6_address"] = "link-local-ipv6-address"
                                    return self.link_local_ipv6_address

                                if (child_yang_name == "timer"):
                                    if (self.timer is None):
                                        self.timer = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Timer()
                                        self.timer.parent = self
                                        self._children_name_map["timer"] = "timer"
                                    return self.timer

                                if (child_yang_name == "tracked-objects"):
                                    if (self.tracked_objects is None):
                                        self.tracked_objects = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.TrackedObjects()
                                        self.tracked_objects.parent = self
                                        self._children_name_map["tracked_objects"] = "tracked-objects"
                                    return self.tracked_objects

                                if (child_yang_name == "tracks"):
                                    if (self.tracks is None):
                                        self.tracks = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter.Tracks()
                                        self.tracks.parent = self
                                        self._children_name_map["tracks"] = "tracks"
                                    return self.tracks

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "global-ipv6-addresses" or name == "link-local-ipv6-address" or name == "timer" or name == "tracked-objects" or name == "tracks" or name == "vr-id" or name == "accept-mode-disable" or name == "bfd" or name == "preempt" or name == "priority" or name == "session-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "vr-id"):
                                    self.vr_id = value
                                    self.vr_id.value_namespace = name_space
                                    self.vr_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "accept-mode-disable"):
                                    self.accept_mode_disable = value
                                    self.accept_mode_disable.value_namespace = name_space
                                    self.accept_mode_disable.value_namespace_prefix = name_space_prefix
                                if(value_path == "bfd"):
                                    self.bfd = value
                                    self.bfd.value_namespace = name_space
                                    self.bfd.value_namespace_prefix = name_space_prefix
                                if(value_path == "preempt"):
                                    self.preempt = value
                                    self.preempt.value_namespace = name_space
                                    self.preempt.value_namespace_prefix = name_space_prefix
                                if(value_path == "priority"):
                                    self.priority = value
                                    self.priority.value_namespace = name_space
                                    self.priority.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-name"):
                                    self.session_name = value
                                    self.session_name.value_namespace = name_space
                                    self.session_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.virtual_router:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.virtual_router:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "virtual-routers" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "virtual-router"):
                                for c in self.virtual_router:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters.VirtualRouter()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.virtual_router.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "virtual-router"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.virtual_routers is not None and self.virtual_routers.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.virtual_routers is not None and self.virtual_routers.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "version3" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "virtual-routers"):
                            if (self.virtual_routers is None):
                                self.virtual_routers = Vrrp.Interfaces.Interface.Ipv6.Version3.VirtualRouters()
                                self.virtual_routers.parent = self
                                self._children_name_map["virtual_routers"] = "virtual-routers"
                            return self.virtual_routers

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "virtual-routers"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class SlaveVirtualRouters(Entity):
                    """
                    The VRRP slave group configuration table
                    
                    .. attribute:: slave_virtual_router
                    
                    	The VRRP slave being configured
                    	**type**\: list of    :py:class:`SlaveVirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2016-12-16'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters, self).__init__()

                        self.yang_name = "slave-virtual-routers"
                        self.yang_parent_name = "ipv6"

                        self.slave_virtual_router = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters, self).__setattr__(name, value)


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
                        _revision = '2016-12-16'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter, self).__init__()

                            self.yang_name = "slave-virtual-router"
                            self.yang_parent_name = "slave-virtual-routers"

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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("slave_virtual_router_id",
                                            "accept_mode_disable",
                                            "follow") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter, self).__setattr__(name, value)


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
                            _revision = '2016-12-16'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address, self).__init__()

                                self.yang_name = "link-local-ipv6-address"
                                self.yang_parent_name = "slave-virtual-router"

                                self.auto_configure = YLeaf(YType.boolean, "auto-configure")

                                self.ip_address = YLeaf(YType.str, "ip-address")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("auto_configure",
                                                "ip_address") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.auto_configure.is_set or
                                    self.ip_address.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.auto_configure.yfilter != YFilter.not_set or
                                    self.ip_address.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "link-local-ipv6-address" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.auto_configure.is_set or self.auto_configure.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.auto_configure.get_name_leafdata())
                                if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ip_address.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "auto-configure" or name == "ip-address"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "auto-configure"):
                                    self.auto_configure = value
                                    self.auto_configure.value_namespace = name_space
                                    self.auto_configure.value_namespace_prefix = name_space_prefix
                                if(value_path == "ip-address"):
                                    self.ip_address = value
                                    self.ip_address.value_namespace = name_space
                                    self.ip_address.value_namespace_prefix = name_space_prefix


                        class GlobalIpv6Addresses(Entity):
                            """
                            The table of VRRP virtual global IPv6
                            addresses
                            
                            .. attribute:: global_ipv6_address
                            
                            	A VRRP virtual global IPv6 IP address
                            	**type**\: list of    :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2016-12-16'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses, self).__init__()

                                self.yang_name = "global-ipv6-addresses"
                                self.yang_parent_name = "slave-virtual-router"

                                self.global_ipv6_address = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in () and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses, self).__setattr__(name, value)


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
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address, self).__init__()

                                    self.yang_name = "global-ipv6-address"
                                    self.yang_parent_name = "global-ipv6-addresses"

                                    self.ip_address = YLeaf(YType.str, "ip-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("ip_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.ip_address.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.ip_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "global-ipv6-address" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ip_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "ip-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "ip-address"):
                                        self.ip_address = value
                                        self.ip_address.value_namespace = name_space
                                        self.ip_address.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.global_ipv6_address:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.global_ipv6_address:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "global-ipv6-addresses" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "global-ipv6-address"):
                                    for c in self.global_ipv6_address:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses.GlobalIpv6Address()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.global_ipv6_address.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "global-ipv6-address"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.slave_virtual_router_id.is_set or
                                self.accept_mode_disable.is_set or
                                self.follow.is_set or
                                (self.global_ipv6_addresses is not None and self.global_ipv6_addresses.has_data()) or
                                (self.link_local_ipv6_address is not None and self.link_local_ipv6_address.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.slave_virtual_router_id.yfilter != YFilter.not_set or
                                self.accept_mode_disable.yfilter != YFilter.not_set or
                                self.follow.yfilter != YFilter.not_set or
                                (self.global_ipv6_addresses is not None and self.global_ipv6_addresses.has_operation()) or
                                (self.link_local_ipv6_address is not None and self.link_local_ipv6_address.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "slave-virtual-router" + "[slave-virtual-router-id='" + self.slave_virtual_router_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.slave_virtual_router_id.is_set or self.slave_virtual_router_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.slave_virtual_router_id.get_name_leafdata())
                            if (self.accept_mode_disable.is_set or self.accept_mode_disable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.accept_mode_disable.get_name_leafdata())
                            if (self.follow.is_set or self.follow.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.follow.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "global-ipv6-addresses"):
                                if (self.global_ipv6_addresses is None):
                                    self.global_ipv6_addresses = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.GlobalIpv6Addresses()
                                    self.global_ipv6_addresses.parent = self
                                    self._children_name_map["global_ipv6_addresses"] = "global-ipv6-addresses"
                                return self.global_ipv6_addresses

                            if (child_yang_name == "link-local-ipv6-address"):
                                if (self.link_local_ipv6_address is None):
                                    self.link_local_ipv6_address = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter.LinkLocalIpv6Address()
                                    self.link_local_ipv6_address.parent = self
                                    self._children_name_map["link_local_ipv6_address"] = "link-local-ipv6-address"
                                return self.link_local_ipv6_address

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "global-ipv6-addresses" or name == "link-local-ipv6-address" or name == "slave-virtual-router-id" or name == "accept-mode-disable" or name == "follow"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "slave-virtual-router-id"):
                                self.slave_virtual_router_id = value
                                self.slave_virtual_router_id.value_namespace = name_space
                                self.slave_virtual_router_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "accept-mode-disable"):
                                self.accept_mode_disable = value
                                self.accept_mode_disable.value_namespace = name_space
                                self.accept_mode_disable.value_namespace_prefix = name_space_prefix
                            if(value_path == "follow"):
                                self.follow = value
                                self.follow.value_namespace = name_space
                                self.follow.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.slave_virtual_router:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.slave_virtual_router:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "slave-virtual-routers" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "slave-virtual-router"):
                            for c in self.slave_virtual_router:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters.SlaveVirtualRouter()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.slave_virtual_router.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "slave-virtual-router"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.slave_virtual_routers is not None and self.slave_virtual_routers.has_data()) or
                        (self.version3 is not None and self.version3.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.slave_virtual_routers is not None and self.slave_virtual_routers.has_operation()) or
                        (self.version3 is not None and self.version3.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv6" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "slave-virtual-routers"):
                        if (self.slave_virtual_routers is None):
                            self.slave_virtual_routers = Vrrp.Interfaces.Interface.Ipv6.SlaveVirtualRouters()
                            self.slave_virtual_routers.parent = self
                            self._children_name_map["slave_virtual_routers"] = "slave-virtual-routers"
                        return self.slave_virtual_routers

                    if (child_yang_name == "version3"):
                        if (self.version3 is None):
                            self.version3 = Vrrp.Interfaces.Interface.Ipv6.Version3()
                            self.version3.parent = self
                            self._children_name_map["version3"] = "version3"
                        return self.version3

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "slave-virtual-routers" or name == "version3"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Delay(Entity):
                """
                Minimum and Reload Delay
                
                .. attribute:: min_delay
                
                	Minimum delay in seconds
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: second
                
                .. attribute:: reload_delay
                
                	Reload delay in seconds
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: second
                
                

                """

                _prefix = 'ipv4-vrrp-cfg'
                _revision = '2016-12-16'

                def __init__(self):
                    super(Vrrp.Interfaces.Interface.Delay, self).__init__()

                    self.yang_name = "delay"
                    self.yang_parent_name = "interface"

                    self.min_delay = YLeaf(YType.uint32, "min-delay")

                    self.reload_delay = YLeaf(YType.uint32, "reload-delay")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("min_delay",
                                    "reload_delay") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vrrp.Interfaces.Interface.Delay, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vrrp.Interfaces.Interface.Delay, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.min_delay.is_set or
                        self.reload_delay.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.min_delay.yfilter != YFilter.not_set or
                        self.reload_delay.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "delay" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.min_delay.is_set or self.min_delay.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.min_delay.get_name_leafdata())
                    if (self.reload_delay.is_set or self.reload_delay.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reload_delay.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "min-delay" or name == "reload-delay"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "min-delay"):
                        self.min_delay = value
                        self.min_delay.value_namespace = name_space
                        self.min_delay.value_namespace_prefix = name_space_prefix
                    if(value_path == "reload-delay"):
                        self.reload_delay = value
                        self.reload_delay.value_namespace = name_space
                        self.reload_delay.value_namespace_prefix = name_space_prefix


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
                _revision = '2016-12-16'

                def __init__(self):
                    super(Vrrp.Interfaces.Interface.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "interface"

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


                class Version3(Entity):
                    """
                    Version 3 VRRP configuration
                    
                    .. attribute:: virtual_routers
                    
                    	The VRRP virtual router configuration table
                    	**type**\:   :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2016-12-16'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv4.Version3, self).__init__()

                        self.yang_name = "version3"
                        self.yang_parent_name = "ipv4"

                        self.virtual_routers = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters()
                        self.virtual_routers.parent = self
                        self._children_name_map["virtual_routers"] = "virtual-routers"
                        self._children_yang_names.add("virtual-routers")


                    class VirtualRouters(Entity):
                        """
                        The VRRP virtual router configuration table
                        
                        .. attribute:: virtual_router
                        
                        	The VRRP virtual router being configured
                        	**type**\: list of    :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2016-12-16'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters, self).__init__()

                            self.yang_name = "virtual-routers"
                            self.yang_parent_name = "version3"

                            self.virtual_router = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters, self).__setattr__(name, value)


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
                            _revision = '2016-12-16'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter, self).__init__()

                                self.yang_name = "virtual-router"
                                self.yang_parent_name = "virtual-routers"

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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("vr_id",
                                                "accept_mode_disable",
                                                "bfd",
                                                "preempt",
                                                "primary_ipv4_address",
                                                "priority",
                                                "session_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter, self).__setattr__(name, value)


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
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer, self).__init__()

                                    self.yang_name = "timer"
                                    self.yang_parent_name = "virtual-router"

                                    self.advertisement_time_in_msec = YLeaf(YType.uint32, "advertisement-time-in-msec")

                                    self.advertisement_time_in_sec = YLeaf(YType.uint32, "advertisement-time-in-sec")

                                    self.forced = YLeaf(YType.boolean, "forced")

                                    self.in_msec = YLeaf(YType.boolean, "in-msec")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("advertisement_time_in_msec",
                                                    "advertisement_time_in_sec",
                                                    "forced",
                                                    "in_msec") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.advertisement_time_in_msec.is_set or
                                        self.advertisement_time_in_sec.is_set or
                                        self.forced.is_set or
                                        self.in_msec.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.advertisement_time_in_msec.yfilter != YFilter.not_set or
                                        self.advertisement_time_in_sec.yfilter != YFilter.not_set or
                                        self.forced.yfilter != YFilter.not_set or
                                        self.in_msec.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "timer" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.advertisement_time_in_msec.is_set or self.advertisement_time_in_msec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.advertisement_time_in_msec.get_name_leafdata())
                                    if (self.advertisement_time_in_sec.is_set or self.advertisement_time_in_sec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.advertisement_time_in_sec.get_name_leafdata())
                                    if (self.forced.is_set or self.forced.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.forced.get_name_leafdata())
                                    if (self.in_msec.is_set or self.in_msec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.in_msec.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "advertisement-time-in-msec" or name == "advertisement-time-in-sec" or name == "forced" or name == "in-msec"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "advertisement-time-in-msec"):
                                        self.advertisement_time_in_msec = value
                                        self.advertisement_time_in_msec.value_namespace = name_space
                                        self.advertisement_time_in_msec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "advertisement-time-in-sec"):
                                        self.advertisement_time_in_sec = value
                                        self.advertisement_time_in_sec.value_namespace = name_space
                                        self.advertisement_time_in_sec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "forced"):
                                        self.forced = value
                                        self.forced.value_namespace = name_space
                                        self.forced.value_namespace_prefix = name_space_prefix
                                    if(value_path == "in-msec"):
                                        self.in_msec = value
                                        self.in_msec.value_namespace = name_space
                                        self.in_msec.value_namespace_prefix = name_space_prefix


                            class SecondaryIpv4Addresses(Entity):
                                """
                                The table of VRRP secondary IPv4 addresses
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	A VRRP secondary IPv4 address
                                	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses, self).__init__()

                                    self.yang_name = "secondary-ipv4-addresses"
                                    self.yang_parent_name = "virtual-router"

                                    self.secondary_ipv4_address = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses, self).__setattr__(name, value)


                                class SecondaryIpv4Address(Entity):
                                    """
                                    A VRRP secondary IPv4 address
                                    
                                    .. attribute:: ip_address  <key>
                                    
                                    	VRRP Secondary IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                        self.yang_name = "secondary-ipv4-address"
                                        self.yang_parent_name = "secondary-ipv4-addresses"

                                        self.ip_address = YLeaf(YType.str, "ip-address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("ip_address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return self.ip_address.is_set

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.ip_address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "secondary-ipv4-address" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ip_address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "ip-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "ip-address"):
                                            self.ip_address = value
                                            self.ip_address.value_namespace = name_space
                                            self.ip_address.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.secondary_ipv4_address:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.secondary_ipv4_address:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "secondary-ipv4-addresses" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "secondary-ipv4-address"):
                                        for c in self.secondary_ipv4_address:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.secondary_ipv4_address.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "secondary-ipv4-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class TrackedObjects(Entity):
                                """
                                Track an object, reducing priority if it
                                goes down
                                
                                .. attribute:: tracked_object
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "virtual-router"

                                    self.tracked_object = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects, self).__setattr__(name, value)


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
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__init__()

                                        self.yang_name = "tracked-object"
                                        self.yang_parent_name = "tracked-objects"

                                        self.object_name = YLeaf(YType.str, "object-name")

                                        self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("object_name",
                                                        "priority_decrement") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.object_name.is_set or
                                            self.priority_decrement.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.object_name.yfilter != YFilter.not_set or
                                            self.priority_decrement.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "tracked-object" + "[object-name='" + self.object_name.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.object_name.get_name_leafdata())
                                        if (self.priority_decrement.is_set or self.priority_decrement.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.priority_decrement.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "object-name" or name == "priority-decrement"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "object-name"):
                                            self.object_name = value
                                            self.object_name.value_namespace = name_space
                                            self.object_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "priority-decrement"):
                                            self.priority_decrement = value
                                            self.priority_decrement.value_namespace = name_space
                                            self.priority_decrement.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.tracked_object:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.tracked_object:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tracked-objects" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "tracked-object"):
                                        for c in self.tracked_object:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.tracked_object.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "tracked-object"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class Tracks(Entity):
                                """
                                Track an item, reducing priority if it
                                goes down
                                
                                .. attribute:: track
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks, self).__init__()

                                    self.yang_name = "tracks"
                                    self.yang_parent_name = "virtual-router"

                                    self.track = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks, self).__setattr__(name, value)


                                class Track(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: priority
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track, self).__init__()

                                        self.yang_name = "track"
                                        self.yang_parent_name = "tracks"

                                        self.interface_name = YLeaf(YType.str, "interface-name")

                                        self.priority = YLeaf(YType.uint32, "priority")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("interface_name",
                                                        "priority") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.interface_name.is_set or
                                            self.priority.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.interface_name.yfilter != YFilter.not_set or
                                            self.priority.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "track" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                                        if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.priority.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "interface-name" or name == "priority"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "interface-name"):
                                            self.interface_name = value
                                            self.interface_name.value_namespace = name_space
                                            self.interface_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "priority"):
                                            self.priority = value
                                            self.priority.value_namespace = name_space
                                            self.priority.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.track:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.track:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tracks" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "track"):
                                        for c in self.track:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks.Track()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.track.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "track"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.vr_id.is_set or
                                    self.accept_mode_disable.is_set or
                                    self.bfd.is_set or
                                    self.preempt.is_set or
                                    self.primary_ipv4_address.is_set or
                                    self.priority.is_set or
                                    self.session_name.is_set or
                                    (self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses.has_data()) or
                                    (self.timer is not None and self.timer.has_data()) or
                                    (self.tracked_objects is not None and self.tracked_objects.has_data()) or
                                    (self.tracks is not None and self.tracks.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.vr_id.yfilter != YFilter.not_set or
                                    self.accept_mode_disable.yfilter != YFilter.not_set or
                                    self.bfd.yfilter != YFilter.not_set or
                                    self.preempt.yfilter != YFilter.not_set or
                                    self.primary_ipv4_address.yfilter != YFilter.not_set or
                                    self.priority.yfilter != YFilter.not_set or
                                    self.session_name.yfilter != YFilter.not_set or
                                    (self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses.has_operation()) or
                                    (self.timer is not None and self.timer.has_operation()) or
                                    (self.tracked_objects is not None and self.tracked_objects.has_operation()) or
                                    (self.tracks is not None and self.tracks.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "virtual-router" + "[vr-id='" + self.vr_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.vr_id.is_set or self.vr_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vr_id.get_name_leafdata())
                                if (self.accept_mode_disable.is_set or self.accept_mode_disable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.accept_mode_disable.get_name_leafdata())
                                if (self.bfd.is_set or self.bfd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bfd.get_name_leafdata())
                                if (self.preempt.is_set or self.preempt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.preempt.get_name_leafdata())
                                if (self.primary_ipv4_address.is_set or self.primary_ipv4_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.primary_ipv4_address.get_name_leafdata())
                                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority.get_name_leafdata())
                                if (self.session_name.is_set or self.session_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "secondary-ipv4-addresses"):
                                    if (self.secondary_ipv4_addresses is None):
                                        self.secondary_ipv4_addresses = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses()
                                        self.secondary_ipv4_addresses.parent = self
                                        self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                                    return self.secondary_ipv4_addresses

                                if (child_yang_name == "timer"):
                                    if (self.timer is None):
                                        self.timer = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Timer()
                                        self.timer.parent = self
                                        self._children_name_map["timer"] = "timer"
                                    return self.timer

                                if (child_yang_name == "tracked-objects"):
                                    if (self.tracked_objects is None):
                                        self.tracked_objects = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.TrackedObjects()
                                        self.tracked_objects.parent = self
                                        self._children_name_map["tracked_objects"] = "tracked-objects"
                                    return self.tracked_objects

                                if (child_yang_name == "tracks"):
                                    if (self.tracks is None):
                                        self.tracks = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter.Tracks()
                                        self.tracks.parent = self
                                        self._children_name_map["tracks"] = "tracks"
                                    return self.tracks

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "secondary-ipv4-addresses" or name == "timer" or name == "tracked-objects" or name == "tracks" or name == "vr-id" or name == "accept-mode-disable" or name == "bfd" or name == "preempt" or name == "primary-ipv4-address" or name == "priority" or name == "session-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "vr-id"):
                                    self.vr_id = value
                                    self.vr_id.value_namespace = name_space
                                    self.vr_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "accept-mode-disable"):
                                    self.accept_mode_disable = value
                                    self.accept_mode_disable.value_namespace = name_space
                                    self.accept_mode_disable.value_namespace_prefix = name_space_prefix
                                if(value_path == "bfd"):
                                    self.bfd = value
                                    self.bfd.value_namespace = name_space
                                    self.bfd.value_namespace_prefix = name_space_prefix
                                if(value_path == "preempt"):
                                    self.preempt = value
                                    self.preempt.value_namespace = name_space
                                    self.preempt.value_namespace_prefix = name_space_prefix
                                if(value_path == "primary-ipv4-address"):
                                    self.primary_ipv4_address = value
                                    self.primary_ipv4_address.value_namespace = name_space
                                    self.primary_ipv4_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "priority"):
                                    self.priority = value
                                    self.priority.value_namespace = name_space
                                    self.priority.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-name"):
                                    self.session_name = value
                                    self.session_name.value_namespace = name_space
                                    self.session_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.virtual_router:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.virtual_router:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "virtual-routers" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "virtual-router"):
                                for c in self.virtual_router:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters.VirtualRouter()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.virtual_router.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "virtual-router"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.virtual_routers is not None and self.virtual_routers.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.virtual_routers is not None and self.virtual_routers.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "version3" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "virtual-routers"):
                            if (self.virtual_routers is None):
                                self.virtual_routers = Vrrp.Interfaces.Interface.Ipv4.Version3.VirtualRouters()
                                self.virtual_routers.parent = self
                                self._children_name_map["virtual_routers"] = "virtual-routers"
                            return self.virtual_routers

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "virtual-routers"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class SlaveVirtualRouters(Entity):
                    """
                    The VRRP slave group configuration table
                    
                    .. attribute:: slave_virtual_router
                    
                    	The VRRP slave being configured
                    	**type**\: list of    :py:class:`SlaveVirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2016-12-16'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters, self).__init__()

                        self.yang_name = "slave-virtual-routers"
                        self.yang_parent_name = "ipv4"

                        self.slave_virtual_router = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters, self).__setattr__(name, value)


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
                        _revision = '2016-12-16'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter, self).__init__()

                            self.yang_name = "slave-virtual-router"
                            self.yang_parent_name = "slave-virtual-routers"

                            self.slave_virtual_router_id = YLeaf(YType.uint32, "slave-virtual-router-id")

                            self.accept_mode_disable = YLeaf(YType.empty, "accept-mode-disable")

                            self.follow = YLeaf(YType.str, "follow")

                            self.primary_ipv4_address = YLeaf(YType.str, "primary-ipv4-address")

                            self.secondary_ipv4_addresses = Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses()
                            self.secondary_ipv4_addresses.parent = self
                            self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                            self._children_yang_names.add("secondary-ipv4-addresses")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("slave_virtual_router_id",
                                            "accept_mode_disable",
                                            "follow",
                                            "primary_ipv4_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter, self).__setattr__(name, value)


                        class SecondaryIpv4Addresses(Entity):
                            """
                            The table of VRRP secondary IPv4 addresses
                            
                            .. attribute:: secondary_ipv4_address
                            
                            	A VRRP secondary IPv4 address
                            	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                            
                            

                            """

                            _prefix = 'ipv4-vrrp-cfg'
                            _revision = '2016-12-16'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses, self).__init__()

                                self.yang_name = "secondary-ipv4-addresses"
                                self.yang_parent_name = "slave-virtual-router"

                                self.secondary_ipv4_address = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in () and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses, self).__setattr__(name, value)


                            class SecondaryIpv4Address(Entity):
                                """
                                A VRRP secondary IPv4 address
                                
                                .. attribute:: ip_address  <key>
                                
                                	VRRP Secondary IPv4 address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                    self.yang_name = "secondary-ipv4-address"
                                    self.yang_parent_name = "secondary-ipv4-addresses"

                                    self.ip_address = YLeaf(YType.str, "ip-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("ip_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.ip_address.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.ip_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "secondary-ipv4-address" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ip_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "ip-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "ip-address"):
                                        self.ip_address = value
                                        self.ip_address.value_namespace = name_space
                                        self.ip_address.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.secondary_ipv4_address:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.secondary_ipv4_address:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "secondary-ipv4-addresses" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "secondary-ipv4-address"):
                                    for c in self.secondary_ipv4_address:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.secondary_ipv4_address.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "secondary-ipv4-address"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.slave_virtual_router_id.is_set or
                                self.accept_mode_disable.is_set or
                                self.follow.is_set or
                                self.primary_ipv4_address.is_set or
                                (self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.slave_virtual_router_id.yfilter != YFilter.not_set or
                                self.accept_mode_disable.yfilter != YFilter.not_set or
                                self.follow.yfilter != YFilter.not_set or
                                self.primary_ipv4_address.yfilter != YFilter.not_set or
                                (self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "slave-virtual-router" + "[slave-virtual-router-id='" + self.slave_virtual_router_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.slave_virtual_router_id.is_set or self.slave_virtual_router_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.slave_virtual_router_id.get_name_leafdata())
                            if (self.accept_mode_disable.is_set or self.accept_mode_disable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.accept_mode_disable.get_name_leafdata())
                            if (self.follow.is_set or self.follow.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.follow.get_name_leafdata())
                            if (self.primary_ipv4_address.is_set or self.primary_ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.primary_ipv4_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "secondary-ipv4-addresses"):
                                if (self.secondary_ipv4_addresses is None):
                                    self.secondary_ipv4_addresses = Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter.SecondaryIpv4Addresses()
                                    self.secondary_ipv4_addresses.parent = self
                                    self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                                return self.secondary_ipv4_addresses

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "secondary-ipv4-addresses" or name == "slave-virtual-router-id" or name == "accept-mode-disable" or name == "follow" or name == "primary-ipv4-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "slave-virtual-router-id"):
                                self.slave_virtual_router_id = value
                                self.slave_virtual_router_id.value_namespace = name_space
                                self.slave_virtual_router_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "accept-mode-disable"):
                                self.accept_mode_disable = value
                                self.accept_mode_disable.value_namespace = name_space
                                self.accept_mode_disable.value_namespace_prefix = name_space_prefix
                            if(value_path == "follow"):
                                self.follow = value
                                self.follow.value_namespace = name_space
                                self.follow.value_namespace_prefix = name_space_prefix
                            if(value_path == "primary-ipv4-address"):
                                self.primary_ipv4_address = value
                                self.primary_ipv4_address.value_namespace = name_space
                                self.primary_ipv4_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.slave_virtual_router:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.slave_virtual_router:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "slave-virtual-routers" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "slave-virtual-router"):
                            for c in self.slave_virtual_router:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters.SlaveVirtualRouter()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.slave_virtual_router.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "slave-virtual-router"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Version2(Entity):
                    """
                    Version 2 VRRP configuration
                    
                    .. attribute:: virtual_routers
                    
                    	The VRRP virtual router configuration table
                    	**type**\:   :py:class:`VirtualRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters>`
                    
                    

                    """

                    _prefix = 'ipv4-vrrp-cfg'
                    _revision = '2016-12-16'

                    def __init__(self):
                        super(Vrrp.Interfaces.Interface.Ipv4.Version2, self).__init__()

                        self.yang_name = "version2"
                        self.yang_parent_name = "ipv4"

                        self.virtual_routers = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters()
                        self.virtual_routers.parent = self
                        self._children_name_map["virtual_routers"] = "virtual-routers"
                        self._children_yang_names.add("virtual-routers")


                    class VirtualRouters(Entity):
                        """
                        The VRRP virtual router configuration table
                        
                        .. attribute:: virtual_router
                        
                        	The VRRP virtual router being configured
                        	**type**\: list of    :py:class:`VirtualRouter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter>`
                        
                        

                        """

                        _prefix = 'ipv4-vrrp-cfg'
                        _revision = '2016-12-16'

                        def __init__(self):
                            super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters, self).__init__()

                            self.yang_name = "virtual-routers"
                            self.yang_parent_name = "version2"

                            self.virtual_router = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters, self).__setattr__(name, value)


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
                            _revision = '2016-12-16'

                            def __init__(self):
                                super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter, self).__init__()

                                self.yang_name = "virtual-router"
                                self.yang_parent_name = "virtual-routers"

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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("vr_id",
                                                "accept_mode_disable",
                                                "bfd",
                                                "preempt",
                                                "primary_ipv4_address",
                                                "priority",
                                                "session_name",
                                                "text_password") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter, self).__setattr__(name, value)


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
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer, self).__init__()

                                    self.yang_name = "timer"
                                    self.yang_parent_name = "virtual-router"

                                    self.advertisement_time_in_msec = YLeaf(YType.uint32, "advertisement-time-in-msec")

                                    self.advertisement_time_in_sec = YLeaf(YType.uint32, "advertisement-time-in-sec")

                                    self.forced = YLeaf(YType.boolean, "forced")

                                    self.in_msec = YLeaf(YType.boolean, "in-msec")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("advertisement_time_in_msec",
                                                    "advertisement_time_in_sec",
                                                    "forced",
                                                    "in_msec") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.advertisement_time_in_msec.is_set or
                                        self.advertisement_time_in_sec.is_set or
                                        self.forced.is_set or
                                        self.in_msec.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.advertisement_time_in_msec.yfilter != YFilter.not_set or
                                        self.advertisement_time_in_sec.yfilter != YFilter.not_set or
                                        self.forced.yfilter != YFilter.not_set or
                                        self.in_msec.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "timer" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.advertisement_time_in_msec.is_set or self.advertisement_time_in_msec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.advertisement_time_in_msec.get_name_leafdata())
                                    if (self.advertisement_time_in_sec.is_set or self.advertisement_time_in_sec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.advertisement_time_in_sec.get_name_leafdata())
                                    if (self.forced.is_set or self.forced.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.forced.get_name_leafdata())
                                    if (self.in_msec.is_set or self.in_msec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.in_msec.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "advertisement-time-in-msec" or name == "advertisement-time-in-sec" or name == "forced" or name == "in-msec"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "advertisement-time-in-msec"):
                                        self.advertisement_time_in_msec = value
                                        self.advertisement_time_in_msec.value_namespace = name_space
                                        self.advertisement_time_in_msec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "advertisement-time-in-sec"):
                                        self.advertisement_time_in_sec = value
                                        self.advertisement_time_in_sec.value_namespace = name_space
                                        self.advertisement_time_in_sec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "forced"):
                                        self.forced = value
                                        self.forced.value_namespace = name_space
                                        self.forced.value_namespace_prefix = name_space_prefix
                                    if(value_path == "in-msec"):
                                        self.in_msec = value
                                        self.in_msec.value_namespace = name_space
                                        self.in_msec.value_namespace_prefix = name_space_prefix


                            class SecondaryIpv4Addresses(Entity):
                                """
                                The table of VRRP secondary IPv4 addresses
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	A VRRP secondary IPv4 address
                                	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses, self).__init__()

                                    self.yang_name = "secondary-ipv4-addresses"
                                    self.yang_parent_name = "virtual-router"

                                    self.secondary_ipv4_address = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses, self).__setattr__(name, value)


                                class SecondaryIpv4Address(Entity):
                                    """
                                    A VRRP secondary IPv4 address
                                    
                                    .. attribute:: ip_address  <key>
                                    
                                    	VRRP Secondary IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                        self.yang_name = "secondary-ipv4-address"
                                        self.yang_parent_name = "secondary-ipv4-addresses"

                                        self.ip_address = YLeaf(YType.str, "ip-address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("ip_address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return self.ip_address.is_set

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.ip_address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "secondary-ipv4-address" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ip_address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "ip-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "ip-address"):
                                            self.ip_address = value
                                            self.ip_address.value_namespace = name_space
                                            self.ip_address.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.secondary_ipv4_address:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.secondary_ipv4_address:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "secondary-ipv4-addresses" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "secondary-ipv4-address"):
                                        for c in self.secondary_ipv4_address:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses.SecondaryIpv4Address()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.secondary_ipv4_address.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "secondary-ipv4-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class Tracks(Entity):
                                """
                                Track an item, reducing priority if it
                                goes down
                                
                                .. attribute:: track
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks, self).__init__()

                                    self.yang_name = "tracks"
                                    self.yang_parent_name = "virtual-router"

                                    self.track = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks, self).__setattr__(name, value)


                                class Track(Entity):
                                    """
                                    Object to be tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Object to be tracked, interface name for interfaces
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: priority
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-vrrp-cfg'
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track, self).__init__()

                                        self.yang_name = "track"
                                        self.yang_parent_name = "tracks"

                                        self.interface_name = YLeaf(YType.str, "interface-name")

                                        self.priority = YLeaf(YType.uint32, "priority")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("interface_name",
                                                        "priority") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.interface_name.is_set or
                                            self.priority.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.interface_name.yfilter != YFilter.not_set or
                                            self.priority.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "track" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                                        if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.priority.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "interface-name" or name == "priority"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "interface-name"):
                                            self.interface_name = value
                                            self.interface_name.value_namespace = name_space
                                            self.interface_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "priority"):
                                            self.priority = value
                                            self.priority.value_namespace = name_space
                                            self.priority.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.track:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.track:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tracks" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "track"):
                                        for c in self.track:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks.Track()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.track.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "track"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class TrackedObjects(Entity):
                                """
                                Track an object, reducing priority if it
                                goes down
                                
                                .. attribute:: tracked_object
                                
                                	Object to be tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_cfg.Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-vrrp-cfg'
                                _revision = '2016-12-16'

                                def __init__(self):
                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "virtual-router"

                                    self.tracked_object = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects, self).__setattr__(name, value)


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
                                    _revision = '2016-12-16'

                                    def __init__(self):
                                        super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__init__()

                                        self.yang_name = "tracked-object"
                                        self.yang_parent_name = "tracked-objects"

                                        self.object_name = YLeaf(YType.str, "object-name")

                                        self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("object_name",
                                                        "priority_decrement") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.object_name.is_set or
                                            self.priority_decrement.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.object_name.yfilter != YFilter.not_set or
                                            self.priority_decrement.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "tracked-object" + "[object-name='" + self.object_name.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.object_name.get_name_leafdata())
                                        if (self.priority_decrement.is_set or self.priority_decrement.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.priority_decrement.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "object-name" or name == "priority-decrement"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "object-name"):
                                            self.object_name = value
                                            self.object_name.value_namespace = name_space
                                            self.object_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "priority-decrement"):
                                            self.priority_decrement = value
                                            self.priority_decrement.value_namespace = name_space
                                            self.priority_decrement.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.tracked_object:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.tracked_object:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tracked-objects" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "tracked-object"):
                                        for c in self.tracked_object:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects.TrackedObject()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.tracked_object.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "tracked-object"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.vr_id.is_set or
                                    self.accept_mode_disable.is_set or
                                    self.bfd.is_set or
                                    self.preempt.is_set or
                                    self.primary_ipv4_address.is_set or
                                    self.priority.is_set or
                                    self.session_name.is_set or
                                    self.text_password.is_set or
                                    (self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses.has_data()) or
                                    (self.timer is not None and self.timer.has_data()) or
                                    (self.tracked_objects is not None and self.tracked_objects.has_data()) or
                                    (self.tracks is not None and self.tracks.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.vr_id.yfilter != YFilter.not_set or
                                    self.accept_mode_disable.yfilter != YFilter.not_set or
                                    self.bfd.yfilter != YFilter.not_set or
                                    self.preempt.yfilter != YFilter.not_set or
                                    self.primary_ipv4_address.yfilter != YFilter.not_set or
                                    self.priority.yfilter != YFilter.not_set or
                                    self.session_name.yfilter != YFilter.not_set or
                                    self.text_password.yfilter != YFilter.not_set or
                                    (self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses.has_operation()) or
                                    (self.timer is not None and self.timer.has_operation()) or
                                    (self.tracked_objects is not None and self.tracked_objects.has_operation()) or
                                    (self.tracks is not None and self.tracks.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "virtual-router" + "[vr-id='" + self.vr_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.vr_id.is_set or self.vr_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vr_id.get_name_leafdata())
                                if (self.accept_mode_disable.is_set or self.accept_mode_disable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.accept_mode_disable.get_name_leafdata())
                                if (self.bfd.is_set or self.bfd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bfd.get_name_leafdata())
                                if (self.preempt.is_set or self.preempt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.preempt.get_name_leafdata())
                                if (self.primary_ipv4_address.is_set or self.primary_ipv4_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.primary_ipv4_address.get_name_leafdata())
                                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority.get_name_leafdata())
                                if (self.session_name.is_set or self.session_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_name.get_name_leafdata())
                                if (self.text_password.is_set or self.text_password.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.text_password.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "secondary-ipv4-addresses"):
                                    if (self.secondary_ipv4_addresses is None):
                                        self.secondary_ipv4_addresses = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.SecondaryIpv4Addresses()
                                        self.secondary_ipv4_addresses.parent = self
                                        self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                                    return self.secondary_ipv4_addresses

                                if (child_yang_name == "timer"):
                                    if (self.timer is None):
                                        self.timer = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Timer()
                                        self.timer.parent = self
                                        self._children_name_map["timer"] = "timer"
                                    return self.timer

                                if (child_yang_name == "tracked-objects"):
                                    if (self.tracked_objects is None):
                                        self.tracked_objects = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.TrackedObjects()
                                        self.tracked_objects.parent = self
                                        self._children_name_map["tracked_objects"] = "tracked-objects"
                                    return self.tracked_objects

                                if (child_yang_name == "tracks"):
                                    if (self.tracks is None):
                                        self.tracks = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter.Tracks()
                                        self.tracks.parent = self
                                        self._children_name_map["tracks"] = "tracks"
                                    return self.tracks

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "secondary-ipv4-addresses" or name == "timer" or name == "tracked-objects" or name == "tracks" or name == "vr-id" or name == "accept-mode-disable" or name == "bfd" or name == "preempt" or name == "primary-ipv4-address" or name == "priority" or name == "session-name" or name == "text-password"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "vr-id"):
                                    self.vr_id = value
                                    self.vr_id.value_namespace = name_space
                                    self.vr_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "accept-mode-disable"):
                                    self.accept_mode_disable = value
                                    self.accept_mode_disable.value_namespace = name_space
                                    self.accept_mode_disable.value_namespace_prefix = name_space_prefix
                                if(value_path == "bfd"):
                                    self.bfd = value
                                    self.bfd.value_namespace = name_space
                                    self.bfd.value_namespace_prefix = name_space_prefix
                                if(value_path == "preempt"):
                                    self.preempt = value
                                    self.preempt.value_namespace = name_space
                                    self.preempt.value_namespace_prefix = name_space_prefix
                                if(value_path == "primary-ipv4-address"):
                                    self.primary_ipv4_address = value
                                    self.primary_ipv4_address.value_namespace = name_space
                                    self.primary_ipv4_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "priority"):
                                    self.priority = value
                                    self.priority.value_namespace = name_space
                                    self.priority.value_namespace_prefix = name_space_prefix
                                if(value_path == "session-name"):
                                    self.session_name = value
                                    self.session_name.value_namespace = name_space
                                    self.session_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "text-password"):
                                    self.text_password = value
                                    self.text_password.value_namespace = name_space
                                    self.text_password.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.virtual_router:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.virtual_router:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "virtual-routers" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "virtual-router"):
                                for c in self.virtual_router:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters.VirtualRouter()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.virtual_router.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "virtual-router"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.virtual_routers is not None and self.virtual_routers.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.virtual_routers is not None and self.virtual_routers.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "version2" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "virtual-routers"):
                            if (self.virtual_routers is None):
                                self.virtual_routers = Vrrp.Interfaces.Interface.Ipv4.Version2.VirtualRouters()
                                self.virtual_routers.parent = self
                                self._children_name_map["virtual_routers"] = "virtual-routers"
                            return self.virtual_routers

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "virtual-routers"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.slave_virtual_routers is not None and self.slave_virtual_routers.has_data()) or
                        (self.version2 is not None and self.version2.has_data()) or
                        (self.version3 is not None and self.version3.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.slave_virtual_routers is not None and self.slave_virtual_routers.has_operation()) or
                        (self.version2 is not None and self.version2.has_operation()) or
                        (self.version3 is not None and self.version3.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "slave-virtual-routers"):
                        if (self.slave_virtual_routers is None):
                            self.slave_virtual_routers = Vrrp.Interfaces.Interface.Ipv4.SlaveVirtualRouters()
                            self.slave_virtual_routers.parent = self
                            self._children_name_map["slave_virtual_routers"] = "slave-virtual-routers"
                        return self.slave_virtual_routers

                    if (child_yang_name == "version2"):
                        if (self.version2 is None):
                            self.version2 = Vrrp.Interfaces.Interface.Ipv4.Version2()
                            self.version2.parent = self
                            self._children_name_map["version2"] = "version2"
                        return self.version2

                    if (child_yang_name == "version3"):
                        if (self.version3 is None):
                            self.version3 = Vrrp.Interfaces.Interface.Ipv4.Version3()
                            self.version3.parent = self
                            self._children_name_map["version3"] = "version3"
                        return self.version3

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "slave-virtual-routers" or name == "version2" or name == "version3"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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
                _revision = '2016-12-16'

                def __init__(self):
                    super(Vrrp.Interfaces.Interface.Bfd, self).__init__()

                    self.yang_name = "bfd"
                    self.yang_parent_name = "interface"

                    self.detection_multiplier = YLeaf(YType.uint32, "detection-multiplier")

                    self.interval = YLeaf(YType.uint32, "interval")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("detection_multiplier",
                                    "interval") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vrrp.Interfaces.Interface.Bfd, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vrrp.Interfaces.Interface.Bfd, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.detection_multiplier.is_set or
                        self.interval.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.detection_multiplier.yfilter != YFilter.not_set or
                        self.interval.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bfd" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.detection_multiplier.is_set or self.detection_multiplier.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.detection_multiplier.get_name_leafdata())
                    if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interval.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "detection-multiplier" or name == "interval"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "detection-multiplier"):
                        self.detection_multiplier = value
                        self.detection_multiplier.value_namespace = name_space
                        self.detection_multiplier.value_namespace_prefix = name_space_prefix
                    if(value_path == "interval"):
                        self.interval = value
                        self.interval.value_namespace = name_space
                        self.interval.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    self.mac_refresh.is_set or
                    (self.bfd is not None and self.bfd.has_data()) or
                    (self.delay is not None and self.delay.has_data()) or
                    (self.ipv4 is not None and self.ipv4.has_data()) or
                    (self.ipv6 is not None and self.ipv6.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.mac_refresh.yfilter != YFilter.not_set or
                    (self.bfd is not None and self.bfd.has_operation()) or
                    (self.delay is not None and self.delay.has_operation()) or
                    (self.ipv4 is not None and self.ipv4.has_operation()) or
                    (self.ipv6 is not None and self.ipv6.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.mac_refresh.is_set or self.mac_refresh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mac_refresh.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bfd"):
                    if (self.bfd is None):
                        self.bfd = Vrrp.Interfaces.Interface.Bfd()
                        self.bfd.parent = self
                        self._children_name_map["bfd"] = "bfd"
                    return self.bfd

                if (child_yang_name == "delay"):
                    if (self.delay is None):
                        self.delay = Vrrp.Interfaces.Interface.Delay()
                        self.delay.parent = self
                        self._children_name_map["delay"] = "delay"
                    return self.delay

                if (child_yang_name == "ipv4"):
                    if (self.ipv4 is None):
                        self.ipv4 = Vrrp.Interfaces.Interface.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"
                    return self.ipv4

                if (child_yang_name == "ipv6"):
                    if (self.ipv6 is None):
                        self.ipv6 = Vrrp.Interfaces.Interface.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"
                    return self.ipv6

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bfd" or name == "delay" or name == "ipv4" or name == "ipv6" or name == "interface-name" or name == "mac-refresh"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "mac-refresh"):
                    self.mac_refresh = value
                    self.mac_refresh.value_namespace = name_space
                    self.mac_refresh.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interface"):
                for c in self.interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Vrrp.Interfaces.Interface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.logging is not None and self.logging.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.logging is not None and self.logging.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-vrrp-cfg:vrrp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = Vrrp.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "logging"):
            if (self.logging is None):
                self.logging = Vrrp.Logging()
                self.logging.parent = self
                self._children_name_map["logging"] = "logging"
            return self.logging

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "interfaces" or name == "logging"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Vrrp()
        return self._top_entity

