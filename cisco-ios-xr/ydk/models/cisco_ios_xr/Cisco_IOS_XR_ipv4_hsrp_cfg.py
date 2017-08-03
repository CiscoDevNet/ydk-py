""" Cisco_IOS_XR_ipv4_hsrp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-hsrp package configuration.

This module contains definitions
for the following management objects\:
  hsrp\: HSRP configuration

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


class HsrpLinklocal(Enum):
    """
    HsrpLinklocal

    Hsrp linklocal

    .. data:: manual = 0

    	Manual Linklocal address configuration

    .. data:: auto = 1

    	Automatic Linklocal address configuration

    .. data:: legacy = 2

    	Automatic legacy-compatible Linklocal address

    	configuration

    """

    manual = Enum.YLeaf(0, "manual")

    auto = Enum.YLeaf(1, "auto")

    legacy = Enum.YLeaf(2, "legacy")



class Hsrp(Entity):
    """
    HSRP configuration
    
    .. attribute:: interfaces
    
    	Interface Table for HSRP configuration
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces>`
    
    .. attribute:: logging
    
    	HSRP logging options
    	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Logging>`
    
    

    """

    _prefix = 'ipv4-hsrp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Hsrp, self).__init__()
        self._top_entity = None

        self.yang_name = "hsrp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-hsrp-cfg"

        self.interfaces = Hsrp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.logging = Hsrp.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"
        self._children_yang_names.add("logging")


    class Interfaces(Entity):
        """
        Interface Table for HSRP configuration
        
        .. attribute:: interface
        
        	Per\-interface HSRP configuration
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-hsrp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Hsrp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "hsrp"

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
                        super(Hsrp.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Hsrp.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            Per\-interface HSRP configuration
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: bfd
            
            	BFD configuration
            	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Bfd>`
            
            .. attribute:: delay
            
            	Minimum and Reload Delay
            	**type**\:   :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Delay>`
            
            .. attribute:: ipv4
            
            	IPv4 HSRP configuration
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4>`
            
            .. attribute:: ipv6
            
            	IPv6 HSRP configuration
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6>`
            
            .. attribute:: mac_refresh
            
            	HSRP MGO slave MAC refresh rate
            	**type**\:  int
            
            	**range:** 0..10000
            
            	**default value**\: 60
            
            .. attribute:: redirects_disable
            
            	Disable HSRP filtered ICMP redirects
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: use_bia
            
            	Use burned\-in address
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ipv4-hsrp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Hsrp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.mac_refresh = YLeaf(YType.uint32, "mac-refresh")

                self.redirects_disable = YLeaf(YType.empty, "redirects-disable")

                self.use_bia = YLeaf(YType.empty, "use-bia")

                self.bfd = Hsrp.Interfaces.Interface.Bfd()
                self.bfd.parent = self
                self._children_name_map["bfd"] = "bfd"
                self._children_yang_names.add("bfd")

                self.delay = Hsrp.Interfaces.Interface.Delay()
                self.delay.parent = self
                self._children_name_map["delay"] = "delay"
                self._children_yang_names.add("delay")

                self.ipv4 = Hsrp.Interfaces.Interface.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._children_yang_names.add("ipv4")

                self.ipv6 = Hsrp.Interfaces.Interface.Ipv6()
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
                                "mac_refresh",
                                "redirects_disable",
                                "use_bia") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Hsrp.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Hsrp.Interfaces.Interface, self).__setattr__(name, value)


            class Ipv6(Entity):
                """
                IPv6 HSRP configuration
                
                .. attribute:: slave_groups
                
                	The HSRP slave group configuration table
                	**type**\:   :py:class:`SlaveGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups>`
                
                .. attribute:: version2
                
                	Version 2 HSRP configuration
                	**type**\:   :py:class:`Version2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2>`
                
                

                """

                _prefix = 'ipv4-hsrp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Interfaces.Interface.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "interface"

                    self.slave_groups = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups()
                    self.slave_groups.parent = self
                    self._children_name_map["slave_groups"] = "slave-groups"
                    self._children_yang_names.add("slave-groups")

                    self.version2 = Hsrp.Interfaces.Interface.Ipv6.Version2()
                    self.version2.parent = self
                    self._children_name_map["version2"] = "version2"
                    self._children_yang_names.add("version2")


                class Version2(Entity):
                    """
                    Version 2 HSRP configuration
                    
                    .. attribute:: groups
                    
                    	The HSRP group configuration table
                    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv6.Version2, self).__init__()

                        self.yang_name = "version2"
                        self.yang_parent_name = "ipv6"

                        self.groups = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups()
                        self.groups.parent = self
                        self._children_name_map["groups"] = "groups"
                        self._children_yang_names.add("groups")


                    class Groups(Entity):
                        """
                        The HSRP group configuration table
                        
                        .. attribute:: group
                        
                        	The HSRP group being configured
                        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group>`
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups, self).__init__()

                            self.yang_name = "groups"
                            self.yang_parent_name = "version2"

                            self.group = YList(self)

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
                                        super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups, self).__setattr__(name, value)


                        class Group(Entity):
                            """
                            The HSRP group being configured
                            
                            .. attribute:: group_number  <key>
                            
                            	HSRP group number
                            	**type**\:  int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection
                            	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd>`
                            
                            .. attribute:: global_ipv6_addresses
                            
                            	The table of HSRP virtual global IPv6 addresses
                            	**type**\:   :py:class:`GlobalIpv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses>`
                            
                            .. attribute:: link_local_ipv6_address
                            
                            	The HSRP IPv6 virtual linklocal address
                            	**type**\:   :py:class:`LinkLocalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address>`
                            
                            .. attribute:: preempt
                            
                            	Force active if higher priority
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 0
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            	**default value**\: 100
                            
                            .. attribute:: session_name
                            
                            	HSRP Session name (for MGO)
                            	**type**\:  str
                            
                            	**length:** 1..16
                            
                            .. attribute:: timers
                            
                            	Hello and hold timers
                            	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers>`
                            
                            .. attribute:: tracked_interfaces
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:   :py:class:`TrackedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces>`
                            
                            .. attribute:: tracked_objects
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:   :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects>`
                            
                            .. attribute:: virtual_mac_address
                            
                            	HSRP MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group, self).__init__()

                                self.yang_name = "group"
                                self.yang_parent_name = "groups"

                                self.group_number = YLeaf(YType.uint32, "group-number")

                                self.preempt = YLeaf(YType.int32, "preempt")

                                self.priority = YLeaf(YType.uint32, "priority")

                                self.session_name = YLeaf(YType.str, "session-name")

                                self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                                self.bfd = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd()
                                self.bfd.parent = self
                                self._children_name_map["bfd"] = "bfd"
                                self._children_yang_names.add("bfd")

                                self.global_ipv6_addresses = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses()
                                self.global_ipv6_addresses.parent = self
                                self._children_name_map["global_ipv6_addresses"] = "global-ipv6-addresses"
                                self._children_yang_names.add("global-ipv6-addresses")

                                self.link_local_ipv6_address = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address()
                                self.link_local_ipv6_address.parent = self
                                self._children_name_map["link_local_ipv6_address"] = "link-local-ipv6-address"
                                self._children_yang_names.add("link-local-ipv6-address")

                                self.timers = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers()
                                self.timers.parent = self
                                self._children_name_map["timers"] = "timers"
                                self._children_yang_names.add("timers")

                                self.tracked_interfaces = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces()
                                self.tracked_interfaces.parent = self
                                self._children_name_map["tracked_interfaces"] = "tracked-interfaces"
                                self._children_yang_names.add("tracked-interfaces")

                                self.tracked_objects = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects()
                                self.tracked_objects.parent = self
                                self._children_name_map["tracked_objects"] = "tracked-objects"
                                self._children_yang_names.add("tracked-objects")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_number",
                                                "preempt",
                                                "priority",
                                                "session_name",
                                                "virtual_mac_address") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group, self).__setattr__(name, value)


                            class Bfd(Entity):
                                """
                                Enable use of Bidirectional Forwarding
                                Detection
                                
                                .. attribute:: address
                                
                                	Enable BFD for this remote IP
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface name to run BFD
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd, self).__init__()

                                    self.yang_name = "bfd"
                                    self.yang_parent_name = "group"

                                    self.address = YLeaf(YType.str, "address")

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("address",
                                                    "interface_name") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.address.is_set or
                                        self.interface_name.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.address.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set)

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
                                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.address.get_name_leafdata())
                                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_name.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address" or name == "interface-name"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "address"):
                                        self.address = value
                                        self.address.value_namespace = name_space
                                        self.address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix


                            class TrackedInterfaces(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_interface
                                
                                	Interface being tracked
                                	**type**\: list of    :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces, self).__init__()

                                    self.yang_name = "tracked-interfaces"
                                    self.yang_parent_name = "group"

                                    self.tracked_interface = YList(self)

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
                                                super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces, self).__setattr__(name, value)


                                class TrackedInterface(Entity):
                                    """
                                    Interface being tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface, self).__init__()

                                        self.yang_name = "tracked-interface"
                                        self.yang_parent_name = "tracked-interfaces"

                                        self.interface_name = YLeaf(YType.str, "interface-name")

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
                                            if name in ("interface_name",
                                                        "priority_decrement") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.interface_name.is_set or
                                            self.priority_decrement.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.interface_name.yfilter != YFilter.not_set or
                                            self.priority_decrement.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "tracked-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                                        if(name == "interface-name" or name == "priority-decrement"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "interface-name"):
                                            self.interface_name = value
                                            self.interface_name.value_namespace = name_space
                                            self.interface_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "priority-decrement"):
                                            self.priority_decrement = value
                                            self.priority_decrement.value_namespace = name_space
                                            self.priority_decrement.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.tracked_interface:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.tracked_interface:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tracked-interfaces" + path_buffer

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

                                    if (child_yang_name == "tracked-interface"):
                                        for c in self.tracked_interface:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.tracked_interface.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "tracked-interface"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class TrackedObjects(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_object
                                
                                	Object being tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "group"

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
                                                super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects, self).__setattr__(name, value)


                                class TrackedObject(Entity):
                                    """
                                    Object being tracked
                                    
                                    .. attribute:: object_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject, self).__init__()

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
                                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject, self).__setattr__(name, value)

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
                                        c = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject()
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


                            class Timers(Entity):
                                """
                                Hello and hold timers
                                
                                .. attribute:: hello_msec
                                
                                	Hello time in msecs
                                	**type**\:  int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hello_msec_flag
                                
                                	TRUE \- Hello time configured in milliseconds, FALSE \- Hello time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hello_sec
                                
                                	Hello time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 3
                                
                                .. attribute:: hold_msec
                                
                                	Hold time in msecs
                                	**type**\:  int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hold_msec_flag
                                
                                	TRUE \- Hold time configured in milliseconds, FALSE \- Hold time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hold_sec
                                
                                	Hold time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 10
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers, self).__init__()

                                    self.yang_name = "timers"
                                    self.yang_parent_name = "group"

                                    self.hello_msec = YLeaf(YType.uint32, "hello-msec")

                                    self.hello_msec_flag = YLeaf(YType.boolean, "hello-msec-flag")

                                    self.hello_sec = YLeaf(YType.uint32, "hello-sec")

                                    self.hold_msec = YLeaf(YType.uint32, "hold-msec")

                                    self.hold_msec_flag = YLeaf(YType.boolean, "hold-msec-flag")

                                    self.hold_sec = YLeaf(YType.uint32, "hold-sec")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("hello_msec",
                                                    "hello_msec_flag",
                                                    "hello_sec",
                                                    "hold_msec",
                                                    "hold_msec_flag",
                                                    "hold_sec") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.hello_msec.is_set or
                                        self.hello_msec_flag.is_set or
                                        self.hello_sec.is_set or
                                        self.hold_msec.is_set or
                                        self.hold_msec_flag.is_set or
                                        self.hold_sec.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.hello_msec.yfilter != YFilter.not_set or
                                        self.hello_msec_flag.yfilter != YFilter.not_set or
                                        self.hello_sec.yfilter != YFilter.not_set or
                                        self.hold_msec.yfilter != YFilter.not_set or
                                        self.hold_msec_flag.yfilter != YFilter.not_set or
                                        self.hold_sec.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "timers" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.hello_msec.is_set or self.hello_msec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hello_msec.get_name_leafdata())
                                    if (self.hello_msec_flag.is_set or self.hello_msec_flag.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hello_msec_flag.get_name_leafdata())
                                    if (self.hello_sec.is_set or self.hello_sec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hello_sec.get_name_leafdata())
                                    if (self.hold_msec.is_set or self.hold_msec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hold_msec.get_name_leafdata())
                                    if (self.hold_msec_flag.is_set or self.hold_msec_flag.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hold_msec_flag.get_name_leafdata())
                                    if (self.hold_sec.is_set or self.hold_sec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hold_sec.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "hello-msec" or name == "hello-msec-flag" or name == "hello-sec" or name == "hold-msec" or name == "hold-msec-flag" or name == "hold-sec"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "hello-msec"):
                                        self.hello_msec = value
                                        self.hello_msec.value_namespace = name_space
                                        self.hello_msec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hello-msec-flag"):
                                        self.hello_msec_flag = value
                                        self.hello_msec_flag.value_namespace = name_space
                                        self.hello_msec_flag.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hello-sec"):
                                        self.hello_sec = value
                                        self.hello_sec.value_namespace = name_space
                                        self.hello_sec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hold-msec"):
                                        self.hold_msec = value
                                        self.hold_msec.value_namespace = name_space
                                        self.hold_msec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hold-msec-flag"):
                                        self.hold_msec_flag = value
                                        self.hold_msec_flag.value_namespace = name_space
                                        self.hold_msec_flag.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hold-sec"):
                                        self.hold_sec = value
                                        self.hold_sec.value_namespace = name_space
                                        self.hold_sec.value_namespace_prefix = name_space_prefix


                            class LinkLocalIpv6Address(Entity):
                                """
                                The HSRP IPv6 virtual linklocal address
                                
                                .. attribute:: address
                                
                                	HSRP IPv6 virtual linklocal address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: auto_configure
                                
                                	Linklocal Configuration Type
                                	**type**\:   :py:class:`HsrpLinklocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.HsrpLinklocal>`
                                
                                	**default value**\: manual
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address, self).__init__()

                                    self.yang_name = "link-local-ipv6-address"
                                    self.yang_parent_name = "group"

                                    self.address = YLeaf(YType.str, "address")

                                    self.auto_configure = YLeaf(YType.enumeration, "auto-configure")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("address",
                                                    "auto_configure") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.address.is_set or
                                        self.auto_configure.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.address.yfilter != YFilter.not_set or
                                        self.auto_configure.yfilter != YFilter.not_set)

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
                                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.address.get_name_leafdata())
                                    if (self.auto_configure.is_set or self.auto_configure.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.auto_configure.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address" or name == "auto-configure"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "address"):
                                        self.address = value
                                        self.address.value_namespace = name_space
                                        self.address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "auto-configure"):
                                        self.auto_configure = value
                                        self.auto_configure.value_namespace = name_space
                                        self.auto_configure.value_namespace_prefix = name_space_prefix


                            class GlobalIpv6Addresses(Entity):
                                """
                                The table of HSRP virtual global IPv6
                                addresses
                                
                                .. attribute:: global_ipv6_address
                                
                                	A HSRP virtual global IPv6 IP address
                                	**type**\: list of    :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses, self).__init__()

                                    self.yang_name = "global-ipv6-addresses"
                                    self.yang_parent_name = "group"

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
                                                super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses, self).__setattr__(name, value)


                                class GlobalIpv6Address(Entity):
                                    """
                                    A HSRP virtual global IPv6 IP address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	HSRP virtual global IPv6 address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address, self).__init__()

                                        self.yang_name = "global-ipv6-address"
                                        self.yang_parent_name = "global-ipv6-addresses"

                                        self.address = YLeaf(YType.str, "address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return self.address.is_set

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "global-ipv6-address" + "[address='" + self.address.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix

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
                                        c = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address()
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
                                    self.group_number.is_set or
                                    self.preempt.is_set or
                                    self.priority.is_set or
                                    self.session_name.is_set or
                                    self.virtual_mac_address.is_set or
                                    (self.bfd is not None and self.bfd.has_data()) or
                                    (self.global_ipv6_addresses is not None and self.global_ipv6_addresses.has_data()) or
                                    (self.link_local_ipv6_address is not None and self.link_local_ipv6_address.has_data()) or
                                    (self.timers is not None and self.timers.has_data()) or
                                    (self.tracked_interfaces is not None and self.tracked_interfaces.has_data()) or
                                    (self.tracked_objects is not None and self.tracked_objects.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_number.yfilter != YFilter.not_set or
                                    self.preempt.yfilter != YFilter.not_set or
                                    self.priority.yfilter != YFilter.not_set or
                                    self.session_name.yfilter != YFilter.not_set or
                                    self.virtual_mac_address.yfilter != YFilter.not_set or
                                    (self.bfd is not None and self.bfd.has_operation()) or
                                    (self.global_ipv6_addresses is not None and self.global_ipv6_addresses.has_operation()) or
                                    (self.link_local_ipv6_address is not None and self.link_local_ipv6_address.has_operation()) or
                                    (self.timers is not None and self.timers.has_operation()) or
                                    (self.tracked_interfaces is not None and self.tracked_interfaces.has_operation()) or
                                    (self.tracked_objects is not None and self.tracked_objects.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "group" + "[group-number='" + self.group_number.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_number.is_set or self.group_number.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_number.get_name_leafdata())
                                if (self.preempt.is_set or self.preempt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.preempt.get_name_leafdata())
                                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority.get_name_leafdata())
                                if (self.session_name.is_set or self.session_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_name.get_name_leafdata())
                                if (self.virtual_mac_address.is_set or self.virtual_mac_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.virtual_mac_address.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "bfd"):
                                    if (self.bfd is None):
                                        self.bfd = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd()
                                        self.bfd.parent = self
                                        self._children_name_map["bfd"] = "bfd"
                                    return self.bfd

                                if (child_yang_name == "global-ipv6-addresses"):
                                    if (self.global_ipv6_addresses is None):
                                        self.global_ipv6_addresses = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses()
                                        self.global_ipv6_addresses.parent = self
                                        self._children_name_map["global_ipv6_addresses"] = "global-ipv6-addresses"
                                    return self.global_ipv6_addresses

                                if (child_yang_name == "link-local-ipv6-address"):
                                    if (self.link_local_ipv6_address is None):
                                        self.link_local_ipv6_address = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address()
                                        self.link_local_ipv6_address.parent = self
                                        self._children_name_map["link_local_ipv6_address"] = "link-local-ipv6-address"
                                    return self.link_local_ipv6_address

                                if (child_yang_name == "timers"):
                                    if (self.timers is None):
                                        self.timers = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers()
                                        self.timers.parent = self
                                        self._children_name_map["timers"] = "timers"
                                    return self.timers

                                if (child_yang_name == "tracked-interfaces"):
                                    if (self.tracked_interfaces is None):
                                        self.tracked_interfaces = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces()
                                        self.tracked_interfaces.parent = self
                                        self._children_name_map["tracked_interfaces"] = "tracked-interfaces"
                                    return self.tracked_interfaces

                                if (child_yang_name == "tracked-objects"):
                                    if (self.tracked_objects is None):
                                        self.tracked_objects = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects()
                                        self.tracked_objects.parent = self
                                        self._children_name_map["tracked_objects"] = "tracked-objects"
                                    return self.tracked_objects

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bfd" or name == "global-ipv6-addresses" or name == "link-local-ipv6-address" or name == "timers" or name == "tracked-interfaces" or name == "tracked-objects" or name == "group-number" or name == "preempt" or name == "priority" or name == "session-name" or name == "virtual-mac-address"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-number"):
                                    self.group_number = value
                                    self.group_number.value_namespace = name_space
                                    self.group_number.value_namespace_prefix = name_space_prefix
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
                                if(value_path == "virtual-mac-address"):
                                    self.virtual_mac_address = value
                                    self.virtual_mac_address.value_namespace = name_space
                                    self.virtual_mac_address.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.group:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.group:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "groups" + path_buffer

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

                            if (child_yang_name == "group"):
                                for c in self.group:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.group.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.groups is not None and self.groups.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.groups is not None and self.groups.has_operation()))

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

                        if (child_yang_name == "groups"):
                            if (self.groups is None):
                                self.groups = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups()
                                self.groups.parent = self
                                self._children_name_map["groups"] = "groups"
                            return self.groups

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "groups"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class SlaveGroups(Entity):
                    """
                    The HSRP slave group configuration table
                    
                    .. attribute:: slave_group
                    
                    	The HSRP slave group being configured
                    	**type**\: list of    :py:class:`SlaveGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups, self).__init__()

                        self.yang_name = "slave-groups"
                        self.yang_parent_name = "ipv6"

                        self.slave_group = YList(self)

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
                                    super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups, self).__setattr__(name, value)


                    class SlaveGroup(Entity):
                        """
                        The HSRP slave group being configured
                        
                        .. attribute:: slave_group_number  <key>
                        
                        	HSRP group number
                        	**type**\:  int
                        
                        	**range:** 0..4095
                        
                        .. attribute:: follow
                        
                        	HSRP Group name for this slave to follow
                        	**type**\:  str
                        
                        .. attribute:: global_ipv6_addresses
                        
                        	The table of HSRP virtual global IPv6 addresses
                        	**type**\:   :py:class:`GlobalIpv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses>`
                        
                        .. attribute:: link_local_ipv6_address
                        
                        	The HSRP IPv6 virtual linklocal address
                        	**type**\:   :py:class:`LinkLocalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address>`
                        
                        .. attribute:: virtual_mac_address
                        
                        	HSRP MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup, self).__init__()

                            self.yang_name = "slave-group"
                            self.yang_parent_name = "slave-groups"

                            self.slave_group_number = YLeaf(YType.uint32, "slave-group-number")

                            self.follow = YLeaf(YType.str, "follow")

                            self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                            self.global_ipv6_addresses = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses()
                            self.global_ipv6_addresses.parent = self
                            self._children_name_map["global_ipv6_addresses"] = "global-ipv6-addresses"
                            self._children_yang_names.add("global-ipv6-addresses")

                            self.link_local_ipv6_address = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address()
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
                                if name in ("slave_group_number",
                                            "follow",
                                            "virtual_mac_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup, self).__setattr__(name, value)


                        class LinkLocalIpv6Address(Entity):
                            """
                            The HSRP IPv6 virtual linklocal address
                            
                            .. attribute:: address
                            
                            	HSRP IPv6 virtual linklocal address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: auto_configure
                            
                            	Linklocal Configuration Type
                            	**type**\:   :py:class:`HsrpLinklocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.HsrpLinklocal>`
                            
                            	**default value**\: manual
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address, self).__init__()

                                self.yang_name = "link-local-ipv6-address"
                                self.yang_parent_name = "slave-group"

                                self.address = YLeaf(YType.str, "address")

                                self.auto_configure = YLeaf(YType.enumeration, "auto-configure")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("address",
                                                "auto_configure") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.address.is_set or
                                    self.auto_configure.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.address.yfilter != YFilter.not_set or
                                    self.auto_configure.yfilter != YFilter.not_set)

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
                                if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.address.get_name_leafdata())
                                if (self.auto_configure.is_set or self.auto_configure.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.auto_configure.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "address" or name == "auto-configure"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "address"):
                                    self.address = value
                                    self.address.value_namespace = name_space
                                    self.address.value_namespace_prefix = name_space_prefix
                                if(value_path == "auto-configure"):
                                    self.auto_configure = value
                                    self.auto_configure.value_namespace = name_space
                                    self.auto_configure.value_namespace_prefix = name_space_prefix


                        class GlobalIpv6Addresses(Entity):
                            """
                            The table of HSRP virtual global IPv6
                            addresses
                            
                            .. attribute:: global_ipv6_address
                            
                            	A HSRP virtual global IPv6 IP address
                            	**type**\: list of    :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address>`
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses, self).__init__()

                                self.yang_name = "global-ipv6-addresses"
                                self.yang_parent_name = "slave-group"

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
                                            super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses, self).__setattr__(name, value)


                            class GlobalIpv6Address(Entity):
                                """
                                A HSRP virtual global IPv6 IP address
                                
                                .. attribute:: address  <key>
                                
                                	HSRP virtual global IPv6 address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address, self).__init__()

                                    self.yang_name = "global-ipv6-address"
                                    self.yang_parent_name = "global-ipv6-addresses"

                                    self.address = YLeaf(YType.str, "address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.address.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "global-ipv6-address" + "[address='" + self.address.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "address"):
                                        self.address = value
                                        self.address.value_namespace = name_space
                                        self.address.value_namespace_prefix = name_space_prefix

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
                                    c = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address()
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
                                self.slave_group_number.is_set or
                                self.follow.is_set or
                                self.virtual_mac_address.is_set or
                                (self.global_ipv6_addresses is not None and self.global_ipv6_addresses.has_data()) or
                                (self.link_local_ipv6_address is not None and self.link_local_ipv6_address.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.slave_group_number.yfilter != YFilter.not_set or
                                self.follow.yfilter != YFilter.not_set or
                                self.virtual_mac_address.yfilter != YFilter.not_set or
                                (self.global_ipv6_addresses is not None and self.global_ipv6_addresses.has_operation()) or
                                (self.link_local_ipv6_address is not None and self.link_local_ipv6_address.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "slave-group" + "[slave-group-number='" + self.slave_group_number.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.slave_group_number.is_set or self.slave_group_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.slave_group_number.get_name_leafdata())
                            if (self.follow.is_set or self.follow.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.follow.get_name_leafdata())
                            if (self.virtual_mac_address.is_set or self.virtual_mac_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.virtual_mac_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "global-ipv6-addresses"):
                                if (self.global_ipv6_addresses is None):
                                    self.global_ipv6_addresses = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses()
                                    self.global_ipv6_addresses.parent = self
                                    self._children_name_map["global_ipv6_addresses"] = "global-ipv6-addresses"
                                return self.global_ipv6_addresses

                            if (child_yang_name == "link-local-ipv6-address"):
                                if (self.link_local_ipv6_address is None):
                                    self.link_local_ipv6_address = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address()
                                    self.link_local_ipv6_address.parent = self
                                    self._children_name_map["link_local_ipv6_address"] = "link-local-ipv6-address"
                                return self.link_local_ipv6_address

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "global-ipv6-addresses" or name == "link-local-ipv6-address" or name == "slave-group-number" or name == "follow" or name == "virtual-mac-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "slave-group-number"):
                                self.slave_group_number = value
                                self.slave_group_number.value_namespace = name_space
                                self.slave_group_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "follow"):
                                self.follow = value
                                self.follow.value_namespace = name_space
                                self.follow.value_namespace_prefix = name_space_prefix
                            if(value_path == "virtual-mac-address"):
                                self.virtual_mac_address = value
                                self.virtual_mac_address.value_namespace = name_space
                                self.virtual_mac_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.slave_group:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.slave_group:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "slave-groups" + path_buffer

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

                        if (child_yang_name == "slave-group"):
                            for c in self.slave_group:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.slave_group.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "slave-group"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.slave_groups is not None and self.slave_groups.has_data()) or
                        (self.version2 is not None and self.version2.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.slave_groups is not None and self.slave_groups.has_operation()) or
                        (self.version2 is not None and self.version2.has_operation()))

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

                    if (child_yang_name == "slave-groups"):
                        if (self.slave_groups is None):
                            self.slave_groups = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups()
                            self.slave_groups.parent = self
                            self._children_name_map["slave_groups"] = "slave-groups"
                        return self.slave_groups

                    if (child_yang_name == "version2"):
                        if (self.version2 is None):
                            self.version2 = Hsrp.Interfaces.Interface.Ipv6.Version2()
                            self.version2.parent = self
                            self._children_name_map["version2"] = "version2"
                        return self.version2

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "slave-groups" or name == "version2"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Bfd(Entity):
                """
                BFD configuration
                
                .. attribute:: detection_multiplier
                
                	Detection multiplier for BFD sessions created by hsrp
                	**type**\:  int
                
                	**range:** 2..50
                
                .. attribute:: interval
                
                	Hello interval for BFD sessions created by hsrp
                	**type**\:  int
                
                	**range:** 3..30000
                
                	**units**\: millisecond
                
                

                """

                _prefix = 'ipv4-hsrp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Interfaces.Interface.Bfd, self).__init__()

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
                                super(Hsrp.Interfaces.Interface.Bfd, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Hsrp.Interfaces.Interface.Bfd, self).__setattr__(name, value)

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


            class Delay(Entity):
                """
                Minimum and Reload Delay
                
                .. attribute:: minimum_delay
                
                	Minimum delay in seconds
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: second
                
                	**default value**\: 1
                
                .. attribute:: reload_delay
                
                	Reload delay in seconds
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: second
                
                	**default value**\: 5
                
                

                """

                _prefix = 'ipv4-hsrp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Interfaces.Interface.Delay, self).__init__()

                    self.yang_name = "delay"
                    self.yang_parent_name = "interface"

                    self.minimum_delay = YLeaf(YType.uint32, "minimum-delay")

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
                        if name in ("minimum_delay",
                                    "reload_delay") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Hsrp.Interfaces.Interface.Delay, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Hsrp.Interfaces.Interface.Delay, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.minimum_delay.is_set or
                        self.reload_delay.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.minimum_delay.yfilter != YFilter.not_set or
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
                    if (self.minimum_delay.is_set or self.minimum_delay.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.minimum_delay.get_name_leafdata())
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
                    if(name == "minimum-delay" or name == "reload-delay"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "minimum-delay"):
                        self.minimum_delay = value
                        self.minimum_delay.value_namespace = name_space
                        self.minimum_delay.value_namespace_prefix = name_space_prefix
                    if(value_path == "reload-delay"):
                        self.reload_delay = value
                        self.reload_delay.value_namespace = name_space
                        self.reload_delay.value_namespace_prefix = name_space_prefix


            class Ipv4(Entity):
                """
                IPv4 HSRP configuration
                
                .. attribute:: slave_groups
                
                	The HSRP slave group configuration table
                	**type**\:   :py:class:`SlaveGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.SlaveGroups>`
                
                .. attribute:: version1
                
                	Version 1 HSRP configuration
                	**type**\:   :py:class:`Version1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1>`
                
                .. attribute:: version2
                
                	Version 2 HSRP configuration
                	**type**\:   :py:class:`Version2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2>`
                
                

                """

                _prefix = 'ipv4-hsrp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Hsrp.Interfaces.Interface.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "interface"

                    self.slave_groups = Hsrp.Interfaces.Interface.Ipv4.SlaveGroups()
                    self.slave_groups.parent = self
                    self._children_name_map["slave_groups"] = "slave-groups"
                    self._children_yang_names.add("slave-groups")

                    self.version1 = Hsrp.Interfaces.Interface.Ipv4.Version1()
                    self.version1.parent = self
                    self._children_name_map["version1"] = "version1"
                    self._children_yang_names.add("version1")

                    self.version2 = Hsrp.Interfaces.Interface.Ipv4.Version2()
                    self.version2.parent = self
                    self._children_name_map["version2"] = "version2"
                    self._children_yang_names.add("version2")


                class SlaveGroups(Entity):
                    """
                    The HSRP slave group configuration table
                    
                    .. attribute:: slave_group
                    
                    	The HSRP slave group being configured
                    	**type**\: list of    :py:class:`SlaveGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups, self).__init__()

                        self.yang_name = "slave-groups"
                        self.yang_parent_name = "ipv4"

                        self.slave_group = YList(self)

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
                                    super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups, self).__setattr__(name, value)


                    class SlaveGroup(Entity):
                        """
                        The HSRP slave group being configured
                        
                        .. attribute:: slave_group_number  <key>
                        
                        	HSRP group number
                        	**type**\:  int
                        
                        	**range:** 0..4095
                        
                        .. attribute:: follow
                        
                        	HSRP Group name for this slave to follow
                        	**type**\:  str
                        
                        .. attribute:: primary_ipv4_address
                        
                        	Primary HSRP IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: secondary_ipv4_addresses
                        
                        	Secondary HSRP IP address Table
                        	**type**\:   :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses>`
                        
                        .. attribute:: virtual_mac_address
                        
                        	HSRP MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup, self).__init__()

                            self.yang_name = "slave-group"
                            self.yang_parent_name = "slave-groups"

                            self.slave_group_number = YLeaf(YType.uint32, "slave-group-number")

                            self.follow = YLeaf(YType.str, "follow")

                            self.primary_ipv4_address = YLeaf(YType.str, "primary-ipv4-address")

                            self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                            self.secondary_ipv4_addresses = Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses()
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
                                if name in ("slave_group_number",
                                            "follow",
                                            "primary_ipv4_address",
                                            "virtual_mac_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup, self).__setattr__(name, value)


                        class SecondaryIpv4Addresses(Entity):
                            """
                            Secondary HSRP IP address Table
                            
                            .. attribute:: secondary_ipv4_address
                            
                            	Secondary HSRP IP address
                            	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses, self).__init__()

                                self.yang_name = "secondary-ipv4-addresses"
                                self.yang_parent_name = "slave-group"

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
                                            super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses, self).__setattr__(name, value)


                            class SecondaryIpv4Address(Entity):
                                """
                                Secondary HSRP IP address
                                
                                .. attribute:: address  <key>
                                
                                	HSRP IP address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                    self.yang_name = "secondary-ipv4-address"
                                    self.yang_parent_name = "secondary-ipv4-addresses"

                                    self.address = YLeaf(YType.str, "address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.address.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "secondary-ipv4-address" + "[address='" + self.address.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "address"):
                                        self.address = value
                                        self.address.value_namespace = name_space
                                        self.address.value_namespace_prefix = name_space_prefix

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
                                    c = Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address()
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
                                self.slave_group_number.is_set or
                                self.follow.is_set or
                                self.primary_ipv4_address.is_set or
                                self.virtual_mac_address.is_set or
                                (self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.slave_group_number.yfilter != YFilter.not_set or
                                self.follow.yfilter != YFilter.not_set or
                                self.primary_ipv4_address.yfilter != YFilter.not_set or
                                self.virtual_mac_address.yfilter != YFilter.not_set or
                                (self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "slave-group" + "[slave-group-number='" + self.slave_group_number.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.slave_group_number.is_set or self.slave_group_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.slave_group_number.get_name_leafdata())
                            if (self.follow.is_set or self.follow.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.follow.get_name_leafdata())
                            if (self.primary_ipv4_address.is_set or self.primary_ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.primary_ipv4_address.get_name_leafdata())
                            if (self.virtual_mac_address.is_set or self.virtual_mac_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.virtual_mac_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "secondary-ipv4-addresses"):
                                if (self.secondary_ipv4_addresses is None):
                                    self.secondary_ipv4_addresses = Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses()
                                    self.secondary_ipv4_addresses.parent = self
                                    self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                                return self.secondary_ipv4_addresses

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "secondary-ipv4-addresses" or name == "slave-group-number" or name == "follow" or name == "primary-ipv4-address" or name == "virtual-mac-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "slave-group-number"):
                                self.slave_group_number = value
                                self.slave_group_number.value_namespace = name_space
                                self.slave_group_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "follow"):
                                self.follow = value
                                self.follow.value_namespace = name_space
                                self.follow.value_namespace_prefix = name_space_prefix
                            if(value_path == "primary-ipv4-address"):
                                self.primary_ipv4_address = value
                                self.primary_ipv4_address.value_namespace = name_space
                                self.primary_ipv4_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "virtual-mac-address"):
                                self.virtual_mac_address = value
                                self.virtual_mac_address.value_namespace = name_space
                                self.virtual_mac_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.slave_group:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.slave_group:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "slave-groups" + path_buffer

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

                        if (child_yang_name == "slave-group"):
                            for c in self.slave_group:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.slave_group.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "slave-group"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Version1(Entity):
                    """
                    Version 1 HSRP configuration
                    
                    .. attribute:: groups
                    
                    	The HSRP group configuration table
                    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv4.Version1, self).__init__()

                        self.yang_name = "version1"
                        self.yang_parent_name = "ipv4"

                        self.groups = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups()
                        self.groups.parent = self
                        self._children_name_map["groups"] = "groups"
                        self._children_yang_names.add("groups")


                    class Groups(Entity):
                        """
                        The HSRP group configuration table
                        
                        .. attribute:: group
                        
                        	The HSRP group being configured
                        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group>`
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups, self).__init__()

                            self.yang_name = "groups"
                            self.yang_parent_name = "version1"

                            self.group = YList(self)

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
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups, self).__setattr__(name, value)


                        class Group(Entity):
                            """
                            The HSRP group being configured
                            
                            .. attribute:: group_number  <key>
                            
                            	HSRP group number
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: authentication
                            
                            	Authentication string
                            	**type**\:  str
                            
                            	**length:** 1..8
                            
                            	**default value**\: cisco
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection
                            	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd>`
                            
                            .. attribute:: preempt
                            
                            	Force active if higher priority
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 0
                            
                            .. attribute:: primary_ipv4_address
                            
                            	Primary HSRP IP address
                            	**type**\:   :py:class:`PrimaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address>`
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            	**default value**\: 100
                            
                            .. attribute:: secondary_ipv4_addresses
                            
                            	Secondary HSRP IP address Table
                            	**type**\:   :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses>`
                            
                            .. attribute:: session_name
                            
                            	HSRP Session name (for MGO)
                            	**type**\:  str
                            
                            	**length:** 1..16
                            
                            .. attribute:: timers
                            
                            	Hello and hold timers
                            	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers>`
                            
                            .. attribute:: tracked_interfaces
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:   :py:class:`TrackedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces>`
                            
                            .. attribute:: tracked_objects
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:   :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects>`
                            
                            .. attribute:: virtual_mac_address
                            
                            	HSRP MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group, self).__init__()

                                self.yang_name = "group"
                                self.yang_parent_name = "groups"

                                self.group_number = YLeaf(YType.uint32, "group-number")

                                self.authentication = YLeaf(YType.str, "authentication")

                                self.preempt = YLeaf(YType.int32, "preempt")

                                self.priority = YLeaf(YType.uint32, "priority")

                                self.session_name = YLeaf(YType.str, "session-name")

                                self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                                self.bfd = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd()
                                self.bfd.parent = self
                                self._children_name_map["bfd"] = "bfd"
                                self._children_yang_names.add("bfd")

                                self.primary_ipv4_address = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address()
                                self.primary_ipv4_address.parent = self
                                self._children_name_map["primary_ipv4_address"] = "primary-ipv4-address"
                                self._children_yang_names.add("primary-ipv4-address")

                                self.secondary_ipv4_addresses = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses()
                                self.secondary_ipv4_addresses.parent = self
                                self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                                self._children_yang_names.add("secondary-ipv4-addresses")

                                self.timers = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers()
                                self.timers.parent = self
                                self._children_name_map["timers"] = "timers"
                                self._children_yang_names.add("timers")

                                self.tracked_interfaces = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces()
                                self.tracked_interfaces.parent = self
                                self._children_name_map["tracked_interfaces"] = "tracked-interfaces"
                                self._children_yang_names.add("tracked-interfaces")

                                self.tracked_objects = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects()
                                self.tracked_objects.parent = self
                                self._children_name_map["tracked_objects"] = "tracked-objects"
                                self._children_yang_names.add("tracked-objects")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_number",
                                                "authentication",
                                                "preempt",
                                                "priority",
                                                "session_name",
                                                "virtual_mac_address") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group, self).__setattr__(name, value)


                            class TrackedInterfaces(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_interface
                                
                                	Interface being tracked
                                	**type**\: list of    :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces, self).__init__()

                                    self.yang_name = "tracked-interfaces"
                                    self.yang_parent_name = "group"

                                    self.tracked_interface = YList(self)

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
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces, self).__setattr__(name, value)


                                class TrackedInterface(Entity):
                                    """
                                    Interface being tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface, self).__init__()

                                        self.yang_name = "tracked-interface"
                                        self.yang_parent_name = "tracked-interfaces"

                                        self.interface_name = YLeaf(YType.str, "interface-name")

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
                                            if name in ("interface_name",
                                                        "priority_decrement") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.interface_name.is_set or
                                            self.priority_decrement.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.interface_name.yfilter != YFilter.not_set or
                                            self.priority_decrement.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "tracked-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                                        if(name == "interface-name" or name == "priority-decrement"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "interface-name"):
                                            self.interface_name = value
                                            self.interface_name.value_namespace = name_space
                                            self.interface_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "priority-decrement"):
                                            self.priority_decrement = value
                                            self.priority_decrement.value_namespace = name_space
                                            self.priority_decrement.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.tracked_interface:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.tracked_interface:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tracked-interfaces" + path_buffer

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

                                    if (child_yang_name == "tracked-interface"):
                                        for c in self.tracked_interface:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.tracked_interface.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "tracked-interface"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class Bfd(Entity):
                                """
                                Enable use of Bidirectional Forwarding
                                Detection
                                
                                .. attribute:: address
                                
                                	Enable BFD for this remote IP
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface name to run BFD
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd, self).__init__()

                                    self.yang_name = "bfd"
                                    self.yang_parent_name = "group"

                                    self.address = YLeaf(YType.str, "address")

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("address",
                                                    "interface_name") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.address.is_set or
                                        self.interface_name.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.address.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set)

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
                                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.address.get_name_leafdata())
                                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_name.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address" or name == "interface-name"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "address"):
                                        self.address = value
                                        self.address.value_namespace = name_space
                                        self.address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix


                            class TrackedObjects(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_object
                                
                                	Object being tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "group"

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
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects, self).__setattr__(name, value)


                                class TrackedObject(Entity):
                                    """
                                    Object being tracked
                                    
                                    .. attribute:: object_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject, self).__init__()

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
                                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject, self).__setattr__(name, value)

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
                                        c = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject()
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


                            class Timers(Entity):
                                """
                                Hello and hold timers
                                
                                .. attribute:: hello_msec
                                
                                	Hello time in msecs
                                	**type**\:  int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hello_msec_flag
                                
                                	TRUE \- Hello time configured in milliseconds, FALSE \- Hello time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hello_sec
                                
                                	Hello time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 3
                                
                                .. attribute:: hold_msec
                                
                                	Hold time in msecs
                                	**type**\:  int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hold_msec_flag
                                
                                	TRUE \- Hold time configured in milliseconds, FALSE \- Hold time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hold_sec
                                
                                	Hold time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 10
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers, self).__init__()

                                    self.yang_name = "timers"
                                    self.yang_parent_name = "group"

                                    self.hello_msec = YLeaf(YType.uint32, "hello-msec")

                                    self.hello_msec_flag = YLeaf(YType.boolean, "hello-msec-flag")

                                    self.hello_sec = YLeaf(YType.uint32, "hello-sec")

                                    self.hold_msec = YLeaf(YType.uint32, "hold-msec")

                                    self.hold_msec_flag = YLeaf(YType.boolean, "hold-msec-flag")

                                    self.hold_sec = YLeaf(YType.uint32, "hold-sec")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("hello_msec",
                                                    "hello_msec_flag",
                                                    "hello_sec",
                                                    "hold_msec",
                                                    "hold_msec_flag",
                                                    "hold_sec") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.hello_msec.is_set or
                                        self.hello_msec_flag.is_set or
                                        self.hello_sec.is_set or
                                        self.hold_msec.is_set or
                                        self.hold_msec_flag.is_set or
                                        self.hold_sec.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.hello_msec.yfilter != YFilter.not_set or
                                        self.hello_msec_flag.yfilter != YFilter.not_set or
                                        self.hello_sec.yfilter != YFilter.not_set or
                                        self.hold_msec.yfilter != YFilter.not_set or
                                        self.hold_msec_flag.yfilter != YFilter.not_set or
                                        self.hold_sec.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "timers" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.hello_msec.is_set or self.hello_msec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hello_msec.get_name_leafdata())
                                    if (self.hello_msec_flag.is_set or self.hello_msec_flag.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hello_msec_flag.get_name_leafdata())
                                    if (self.hello_sec.is_set or self.hello_sec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hello_sec.get_name_leafdata())
                                    if (self.hold_msec.is_set or self.hold_msec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hold_msec.get_name_leafdata())
                                    if (self.hold_msec_flag.is_set or self.hold_msec_flag.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hold_msec_flag.get_name_leafdata())
                                    if (self.hold_sec.is_set or self.hold_sec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hold_sec.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "hello-msec" or name == "hello-msec-flag" or name == "hello-sec" or name == "hold-msec" or name == "hold-msec-flag" or name == "hold-sec"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "hello-msec"):
                                        self.hello_msec = value
                                        self.hello_msec.value_namespace = name_space
                                        self.hello_msec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hello-msec-flag"):
                                        self.hello_msec_flag = value
                                        self.hello_msec_flag.value_namespace = name_space
                                        self.hello_msec_flag.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hello-sec"):
                                        self.hello_sec = value
                                        self.hello_sec.value_namespace = name_space
                                        self.hello_sec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hold-msec"):
                                        self.hold_msec = value
                                        self.hold_msec.value_namespace = name_space
                                        self.hold_msec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hold-msec-flag"):
                                        self.hold_msec_flag = value
                                        self.hold_msec_flag.value_namespace = name_space
                                        self.hold_msec_flag.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hold-sec"):
                                        self.hold_sec = value
                                        self.hold_sec.value_namespace = name_space
                                        self.hold_sec.value_namespace_prefix = name_space_prefix


                            class PrimaryIpv4Address(Entity):
                                """
                                Primary HSRP IP address
                                
                                .. attribute:: address
                                
                                	HSRP IP address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: virtual_ip_learn
                                
                                	TRUE if the HSRP protocol is to learn the virtual IP address it is to use
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address, self).__init__()

                                    self.yang_name = "primary-ipv4-address"
                                    self.yang_parent_name = "group"

                                    self.address = YLeaf(YType.str, "address")

                                    self.virtual_ip_learn = YLeaf(YType.boolean, "virtual-ip-learn")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("address",
                                                    "virtual_ip_learn") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.address.is_set or
                                        self.virtual_ip_learn.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.address.yfilter != YFilter.not_set or
                                        self.virtual_ip_learn.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "primary-ipv4-address" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.address.get_name_leafdata())
                                    if (self.virtual_ip_learn.is_set or self.virtual_ip_learn.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.virtual_ip_learn.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address" or name == "virtual-ip-learn"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "address"):
                                        self.address = value
                                        self.address.value_namespace = name_space
                                        self.address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "virtual-ip-learn"):
                                        self.virtual_ip_learn = value
                                        self.virtual_ip_learn.value_namespace = name_space
                                        self.virtual_ip_learn.value_namespace_prefix = name_space_prefix


                            class SecondaryIpv4Addresses(Entity):
                                """
                                Secondary HSRP IP address Table
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	Secondary HSRP IP address
                                	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses, self).__init__()

                                    self.yang_name = "secondary-ipv4-addresses"
                                    self.yang_parent_name = "group"

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
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses, self).__setattr__(name, value)


                                class SecondaryIpv4Address(Entity):
                                    """
                                    Secondary HSRP IP address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	HSRP IP address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                        self.yang_name = "secondary-ipv4-address"
                                        self.yang_parent_name = "secondary-ipv4-addresses"

                                        self.address = YLeaf(YType.str, "address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return self.address.is_set

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "secondary-ipv4-address" + "[address='" + self.address.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix

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
                                        c = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address()
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
                                    self.group_number.is_set or
                                    self.authentication.is_set or
                                    self.preempt.is_set or
                                    self.priority.is_set or
                                    self.session_name.is_set or
                                    self.virtual_mac_address.is_set or
                                    (self.bfd is not None and self.bfd.has_data()) or
                                    (self.primary_ipv4_address is not None and self.primary_ipv4_address.has_data()) or
                                    (self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses.has_data()) or
                                    (self.timers is not None and self.timers.has_data()) or
                                    (self.tracked_interfaces is not None and self.tracked_interfaces.has_data()) or
                                    (self.tracked_objects is not None and self.tracked_objects.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_number.yfilter != YFilter.not_set or
                                    self.authentication.yfilter != YFilter.not_set or
                                    self.preempt.yfilter != YFilter.not_set or
                                    self.priority.yfilter != YFilter.not_set or
                                    self.session_name.yfilter != YFilter.not_set or
                                    self.virtual_mac_address.yfilter != YFilter.not_set or
                                    (self.bfd is not None and self.bfd.has_operation()) or
                                    (self.primary_ipv4_address is not None and self.primary_ipv4_address.has_operation()) or
                                    (self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses.has_operation()) or
                                    (self.timers is not None and self.timers.has_operation()) or
                                    (self.tracked_interfaces is not None and self.tracked_interfaces.has_operation()) or
                                    (self.tracked_objects is not None and self.tracked_objects.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "group" + "[group-number='" + self.group_number.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_number.is_set or self.group_number.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_number.get_name_leafdata())
                                if (self.authentication.is_set or self.authentication.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.authentication.get_name_leafdata())
                                if (self.preempt.is_set or self.preempt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.preempt.get_name_leafdata())
                                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority.get_name_leafdata())
                                if (self.session_name.is_set or self.session_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_name.get_name_leafdata())
                                if (self.virtual_mac_address.is_set or self.virtual_mac_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.virtual_mac_address.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "bfd"):
                                    if (self.bfd is None):
                                        self.bfd = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd()
                                        self.bfd.parent = self
                                        self._children_name_map["bfd"] = "bfd"
                                    return self.bfd

                                if (child_yang_name == "primary-ipv4-address"):
                                    if (self.primary_ipv4_address is None):
                                        self.primary_ipv4_address = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address()
                                        self.primary_ipv4_address.parent = self
                                        self._children_name_map["primary_ipv4_address"] = "primary-ipv4-address"
                                    return self.primary_ipv4_address

                                if (child_yang_name == "secondary-ipv4-addresses"):
                                    if (self.secondary_ipv4_addresses is None):
                                        self.secondary_ipv4_addresses = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses()
                                        self.secondary_ipv4_addresses.parent = self
                                        self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                                    return self.secondary_ipv4_addresses

                                if (child_yang_name == "timers"):
                                    if (self.timers is None):
                                        self.timers = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers()
                                        self.timers.parent = self
                                        self._children_name_map["timers"] = "timers"
                                    return self.timers

                                if (child_yang_name == "tracked-interfaces"):
                                    if (self.tracked_interfaces is None):
                                        self.tracked_interfaces = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces()
                                        self.tracked_interfaces.parent = self
                                        self._children_name_map["tracked_interfaces"] = "tracked-interfaces"
                                    return self.tracked_interfaces

                                if (child_yang_name == "tracked-objects"):
                                    if (self.tracked_objects is None):
                                        self.tracked_objects = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects()
                                        self.tracked_objects.parent = self
                                        self._children_name_map["tracked_objects"] = "tracked-objects"
                                    return self.tracked_objects

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bfd" or name == "primary-ipv4-address" or name == "secondary-ipv4-addresses" or name == "timers" or name == "tracked-interfaces" or name == "tracked-objects" or name == "group-number" or name == "authentication" or name == "preempt" or name == "priority" or name == "session-name" or name == "virtual-mac-address"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-number"):
                                    self.group_number = value
                                    self.group_number.value_namespace = name_space
                                    self.group_number.value_namespace_prefix = name_space_prefix
                                if(value_path == "authentication"):
                                    self.authentication = value
                                    self.authentication.value_namespace = name_space
                                    self.authentication.value_namespace_prefix = name_space_prefix
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
                                if(value_path == "virtual-mac-address"):
                                    self.virtual_mac_address = value
                                    self.virtual_mac_address.value_namespace = name_space
                                    self.virtual_mac_address.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.group:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.group:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "groups" + path_buffer

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

                            if (child_yang_name == "group"):
                                for c in self.group:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.group.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.groups is not None and self.groups.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.groups is not None and self.groups.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "version1" + path_buffer

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

                        if (child_yang_name == "groups"):
                            if (self.groups is None):
                                self.groups = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups()
                                self.groups.parent = self
                                self._children_name_map["groups"] = "groups"
                            return self.groups

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "groups"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Version2(Entity):
                    """
                    Version 2 HSRP configuration
                    
                    .. attribute:: groups
                    
                    	The HSRP group configuration table
                    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv4.Version2, self).__init__()

                        self.yang_name = "version2"
                        self.yang_parent_name = "ipv4"

                        self.groups = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups()
                        self.groups.parent = self
                        self._children_name_map["groups"] = "groups"
                        self._children_yang_names.add("groups")


                    class Groups(Entity):
                        """
                        The HSRP group configuration table
                        
                        .. attribute:: group
                        
                        	The HSRP group being configured
                        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group>`
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups, self).__init__()

                            self.yang_name = "groups"
                            self.yang_parent_name = "version2"

                            self.group = YList(self)

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
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups, self).__setattr__(name, value)


                        class Group(Entity):
                            """
                            The HSRP group being configured
                            
                            .. attribute:: group_number  <key>
                            
                            	HSRP group number
                            	**type**\:  int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection
                            	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd>`
                            
                            .. attribute:: preempt
                            
                            	Force active if higher priority
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 0
                            
                            .. attribute:: primary_ipv4_address
                            
                            	Primary HSRP IP address
                            	**type**\:   :py:class:`PrimaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address>`
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            	**default value**\: 100
                            
                            .. attribute:: secondary_ipv4_addresses
                            
                            	Secondary HSRP IP address Table
                            	**type**\:   :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses>`
                            
                            .. attribute:: session_name
                            
                            	HSRP Session name (for MGO)
                            	**type**\:  str
                            
                            	**length:** 1..16
                            
                            .. attribute:: timers
                            
                            	Hello and hold timers
                            	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers>`
                            
                            .. attribute:: tracked_interfaces
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:   :py:class:`TrackedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces>`
                            
                            .. attribute:: tracked_objects
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:   :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects>`
                            
                            .. attribute:: virtual_mac_address
                            
                            	HSRP MAC address
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group, self).__init__()

                                self.yang_name = "group"
                                self.yang_parent_name = "groups"

                                self.group_number = YLeaf(YType.uint32, "group-number")

                                self.preempt = YLeaf(YType.int32, "preempt")

                                self.priority = YLeaf(YType.uint32, "priority")

                                self.session_name = YLeaf(YType.str, "session-name")

                                self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                                self.bfd = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd()
                                self.bfd.parent = self
                                self._children_name_map["bfd"] = "bfd"
                                self._children_yang_names.add("bfd")

                                self.primary_ipv4_address = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address()
                                self.primary_ipv4_address.parent = self
                                self._children_name_map["primary_ipv4_address"] = "primary-ipv4-address"
                                self._children_yang_names.add("primary-ipv4-address")

                                self.secondary_ipv4_addresses = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses()
                                self.secondary_ipv4_addresses.parent = self
                                self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                                self._children_yang_names.add("secondary-ipv4-addresses")

                                self.timers = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers()
                                self.timers.parent = self
                                self._children_name_map["timers"] = "timers"
                                self._children_yang_names.add("timers")

                                self.tracked_interfaces = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces()
                                self.tracked_interfaces.parent = self
                                self._children_name_map["tracked_interfaces"] = "tracked-interfaces"
                                self._children_yang_names.add("tracked-interfaces")

                                self.tracked_objects = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects()
                                self.tracked_objects.parent = self
                                self._children_name_map["tracked_objects"] = "tracked-objects"
                                self._children_yang_names.add("tracked-objects")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_number",
                                                "preempt",
                                                "priority",
                                                "session_name",
                                                "virtual_mac_address") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group, self).__setattr__(name, value)


                            class SecondaryIpv4Addresses(Entity):
                                """
                                Secondary HSRP IP address Table
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	Secondary HSRP IP address
                                	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses, self).__init__()

                                    self.yang_name = "secondary-ipv4-addresses"
                                    self.yang_parent_name = "group"

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
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses, self).__setattr__(name, value)


                                class SecondaryIpv4Address(Entity):
                                    """
                                    Secondary HSRP IP address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	HSRP IP address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                        self.yang_name = "secondary-ipv4-address"
                                        self.yang_parent_name = "secondary-ipv4-addresses"

                                        self.address = YLeaf(YType.str, "address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return self.address.is_set

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "secondary-ipv4-address" + "[address='" + self.address.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix

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
                                        c = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address()
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


                            class Bfd(Entity):
                                """
                                Enable use of Bidirectional Forwarding
                                Detection
                                
                                .. attribute:: address
                                
                                	Enable BFD for this remote IP
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface name to run BFD
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd, self).__init__()

                                    self.yang_name = "bfd"
                                    self.yang_parent_name = "group"

                                    self.address = YLeaf(YType.str, "address")

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("address",
                                                    "interface_name") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.address.is_set or
                                        self.interface_name.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.address.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set)

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
                                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.address.get_name_leafdata())
                                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_name.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address" or name == "interface-name"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "address"):
                                        self.address = value
                                        self.address.value_namespace = name_space
                                        self.address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix


                            class PrimaryIpv4Address(Entity):
                                """
                                Primary HSRP IP address
                                
                                .. attribute:: address
                                
                                	HSRP IP address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: virtual_ip_learn
                                
                                	TRUE if the HSRP protocol is to learn the virtual IP address it is to use
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address, self).__init__()

                                    self.yang_name = "primary-ipv4-address"
                                    self.yang_parent_name = "group"

                                    self.address = YLeaf(YType.str, "address")

                                    self.virtual_ip_learn = YLeaf(YType.boolean, "virtual-ip-learn")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("address",
                                                    "virtual_ip_learn") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.address.is_set or
                                        self.virtual_ip_learn.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.address.yfilter != YFilter.not_set or
                                        self.virtual_ip_learn.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "primary-ipv4-address" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.address.get_name_leafdata())
                                    if (self.virtual_ip_learn.is_set or self.virtual_ip_learn.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.virtual_ip_learn.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address" or name == "virtual-ip-learn"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "address"):
                                        self.address = value
                                        self.address.value_namespace = name_space
                                        self.address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "virtual-ip-learn"):
                                        self.virtual_ip_learn = value
                                        self.virtual_ip_learn.value_namespace = name_space
                                        self.virtual_ip_learn.value_namespace_prefix = name_space_prefix


                            class TrackedObjects(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_object
                                
                                	Object being tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "group"

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
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects, self).__setattr__(name, value)


                                class TrackedObject(Entity):
                                    """
                                    Object being tracked
                                    
                                    .. attribute:: object_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject, self).__init__()

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
                                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject, self).__setattr__(name, value)

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
                                        c = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject()
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


                            class TrackedInterfaces(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_interface
                                
                                	Interface being tracked
                                	**type**\: list of    :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces, self).__init__()

                                    self.yang_name = "tracked-interfaces"
                                    self.yang_parent_name = "group"

                                    self.tracked_interface = YList(self)

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
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces, self).__setattr__(name, value)


                                class TrackedInterface(Entity):
                                    """
                                    Interface being tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface, self).__init__()

                                        self.yang_name = "tracked-interface"
                                        self.yang_parent_name = "tracked-interfaces"

                                        self.interface_name = YLeaf(YType.str, "interface-name")

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
                                            if name in ("interface_name",
                                                        "priority_decrement") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.interface_name.is_set or
                                            self.priority_decrement.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.interface_name.yfilter != YFilter.not_set or
                                            self.priority_decrement.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "tracked-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                                        if(name == "interface-name" or name == "priority-decrement"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "interface-name"):
                                            self.interface_name = value
                                            self.interface_name.value_namespace = name_space
                                            self.interface_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "priority-decrement"):
                                            self.priority_decrement = value
                                            self.priority_decrement.value_namespace = name_space
                                            self.priority_decrement.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.tracked_interface:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.tracked_interface:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tracked-interfaces" + path_buffer

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

                                    if (child_yang_name == "tracked-interface"):
                                        for c in self.tracked_interface:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.tracked_interface.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "tracked-interface"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class Timers(Entity):
                                """
                                Hello and hold timers
                                
                                .. attribute:: hello_msec
                                
                                	Hello time in msecs
                                	**type**\:  int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hello_msec_flag
                                
                                	TRUE \- Hello time configured in milliseconds, FALSE \- Hello time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hello_sec
                                
                                	Hello time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 3
                                
                                .. attribute:: hold_msec
                                
                                	Hold time in msecs
                                	**type**\:  int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hold_msec_flag
                                
                                	TRUE \- Hold time configured in milliseconds, FALSE \- Hold time configured in seconds
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hold_sec
                                
                                	Hold time in seconds
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 10
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers, self).__init__()

                                    self.yang_name = "timers"
                                    self.yang_parent_name = "group"

                                    self.hello_msec = YLeaf(YType.uint32, "hello-msec")

                                    self.hello_msec_flag = YLeaf(YType.boolean, "hello-msec-flag")

                                    self.hello_sec = YLeaf(YType.uint32, "hello-sec")

                                    self.hold_msec = YLeaf(YType.uint32, "hold-msec")

                                    self.hold_msec_flag = YLeaf(YType.boolean, "hold-msec-flag")

                                    self.hold_sec = YLeaf(YType.uint32, "hold-sec")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("hello_msec",
                                                    "hello_msec_flag",
                                                    "hello_sec",
                                                    "hold_msec",
                                                    "hold_msec_flag",
                                                    "hold_sec") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.hello_msec.is_set or
                                        self.hello_msec_flag.is_set or
                                        self.hello_sec.is_set or
                                        self.hold_msec.is_set or
                                        self.hold_msec_flag.is_set or
                                        self.hold_sec.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.hello_msec.yfilter != YFilter.not_set or
                                        self.hello_msec_flag.yfilter != YFilter.not_set or
                                        self.hello_sec.yfilter != YFilter.not_set or
                                        self.hold_msec.yfilter != YFilter.not_set or
                                        self.hold_msec_flag.yfilter != YFilter.not_set or
                                        self.hold_sec.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "timers" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.hello_msec.is_set or self.hello_msec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hello_msec.get_name_leafdata())
                                    if (self.hello_msec_flag.is_set or self.hello_msec_flag.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hello_msec_flag.get_name_leafdata())
                                    if (self.hello_sec.is_set or self.hello_sec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hello_sec.get_name_leafdata())
                                    if (self.hold_msec.is_set or self.hold_msec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hold_msec.get_name_leafdata())
                                    if (self.hold_msec_flag.is_set or self.hold_msec_flag.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hold_msec_flag.get_name_leafdata())
                                    if (self.hold_sec.is_set or self.hold_sec.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hold_sec.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "hello-msec" or name == "hello-msec-flag" or name == "hello-sec" or name == "hold-msec" or name == "hold-msec-flag" or name == "hold-sec"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "hello-msec"):
                                        self.hello_msec = value
                                        self.hello_msec.value_namespace = name_space
                                        self.hello_msec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hello-msec-flag"):
                                        self.hello_msec_flag = value
                                        self.hello_msec_flag.value_namespace = name_space
                                        self.hello_msec_flag.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hello-sec"):
                                        self.hello_sec = value
                                        self.hello_sec.value_namespace = name_space
                                        self.hello_sec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hold-msec"):
                                        self.hold_msec = value
                                        self.hold_msec.value_namespace = name_space
                                        self.hold_msec.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hold-msec-flag"):
                                        self.hold_msec_flag = value
                                        self.hold_msec_flag.value_namespace = name_space
                                        self.hold_msec_flag.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hold-sec"):
                                        self.hold_sec = value
                                        self.hold_sec.value_namespace = name_space
                                        self.hold_sec.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.group_number.is_set or
                                    self.preempt.is_set or
                                    self.priority.is_set or
                                    self.session_name.is_set or
                                    self.virtual_mac_address.is_set or
                                    (self.bfd is not None and self.bfd.has_data()) or
                                    (self.primary_ipv4_address is not None and self.primary_ipv4_address.has_data()) or
                                    (self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses.has_data()) or
                                    (self.timers is not None and self.timers.has_data()) or
                                    (self.tracked_interfaces is not None and self.tracked_interfaces.has_data()) or
                                    (self.tracked_objects is not None and self.tracked_objects.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_number.yfilter != YFilter.not_set or
                                    self.preempt.yfilter != YFilter.not_set or
                                    self.priority.yfilter != YFilter.not_set or
                                    self.session_name.yfilter != YFilter.not_set or
                                    self.virtual_mac_address.yfilter != YFilter.not_set or
                                    (self.bfd is not None and self.bfd.has_operation()) or
                                    (self.primary_ipv4_address is not None and self.primary_ipv4_address.has_operation()) or
                                    (self.secondary_ipv4_addresses is not None and self.secondary_ipv4_addresses.has_operation()) or
                                    (self.timers is not None and self.timers.has_operation()) or
                                    (self.tracked_interfaces is not None and self.tracked_interfaces.has_operation()) or
                                    (self.tracked_objects is not None and self.tracked_objects.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "group" + "[group-number='" + self.group_number.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_number.is_set or self.group_number.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_number.get_name_leafdata())
                                if (self.preempt.is_set or self.preempt.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.preempt.get_name_leafdata())
                                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.priority.get_name_leafdata())
                                if (self.session_name.is_set or self.session_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.session_name.get_name_leafdata())
                                if (self.virtual_mac_address.is_set or self.virtual_mac_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.virtual_mac_address.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "bfd"):
                                    if (self.bfd is None):
                                        self.bfd = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd()
                                        self.bfd.parent = self
                                        self._children_name_map["bfd"] = "bfd"
                                    return self.bfd

                                if (child_yang_name == "primary-ipv4-address"):
                                    if (self.primary_ipv4_address is None):
                                        self.primary_ipv4_address = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address()
                                        self.primary_ipv4_address.parent = self
                                        self._children_name_map["primary_ipv4_address"] = "primary-ipv4-address"
                                    return self.primary_ipv4_address

                                if (child_yang_name == "secondary-ipv4-addresses"):
                                    if (self.secondary_ipv4_addresses is None):
                                        self.secondary_ipv4_addresses = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses()
                                        self.secondary_ipv4_addresses.parent = self
                                        self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                                    return self.secondary_ipv4_addresses

                                if (child_yang_name == "timers"):
                                    if (self.timers is None):
                                        self.timers = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers()
                                        self.timers.parent = self
                                        self._children_name_map["timers"] = "timers"
                                    return self.timers

                                if (child_yang_name == "tracked-interfaces"):
                                    if (self.tracked_interfaces is None):
                                        self.tracked_interfaces = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces()
                                        self.tracked_interfaces.parent = self
                                        self._children_name_map["tracked_interfaces"] = "tracked-interfaces"
                                    return self.tracked_interfaces

                                if (child_yang_name == "tracked-objects"):
                                    if (self.tracked_objects is None):
                                        self.tracked_objects = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects()
                                        self.tracked_objects.parent = self
                                        self._children_name_map["tracked_objects"] = "tracked-objects"
                                    return self.tracked_objects

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bfd" or name == "primary-ipv4-address" or name == "secondary-ipv4-addresses" or name == "timers" or name == "tracked-interfaces" or name == "tracked-objects" or name == "group-number" or name == "preempt" or name == "priority" or name == "session-name" or name == "virtual-mac-address"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-number"):
                                    self.group_number = value
                                    self.group_number.value_namespace = name_space
                                    self.group_number.value_namespace_prefix = name_space_prefix
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
                                if(value_path == "virtual-mac-address"):
                                    self.virtual_mac_address = value
                                    self.virtual_mac_address.value_namespace = name_space
                                    self.virtual_mac_address.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.group:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.group:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "groups" + path_buffer

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

                            if (child_yang_name == "group"):
                                for c in self.group:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.group.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.groups is not None and self.groups.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.groups is not None and self.groups.has_operation()))

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

                        if (child_yang_name == "groups"):
                            if (self.groups is None):
                                self.groups = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups()
                                self.groups.parent = self
                                self._children_name_map["groups"] = "groups"
                            return self.groups

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "groups"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.slave_groups is not None and self.slave_groups.has_data()) or
                        (self.version1 is not None and self.version1.has_data()) or
                        (self.version2 is not None and self.version2.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.slave_groups is not None and self.slave_groups.has_operation()) or
                        (self.version1 is not None and self.version1.has_operation()) or
                        (self.version2 is not None and self.version2.has_operation()))

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

                    if (child_yang_name == "slave-groups"):
                        if (self.slave_groups is None):
                            self.slave_groups = Hsrp.Interfaces.Interface.Ipv4.SlaveGroups()
                            self.slave_groups.parent = self
                            self._children_name_map["slave_groups"] = "slave-groups"
                        return self.slave_groups

                    if (child_yang_name == "version1"):
                        if (self.version1 is None):
                            self.version1 = Hsrp.Interfaces.Interface.Ipv4.Version1()
                            self.version1.parent = self
                            self._children_name_map["version1"] = "version1"
                        return self.version1

                    if (child_yang_name == "version2"):
                        if (self.version2 is None):
                            self.version2 = Hsrp.Interfaces.Interface.Ipv4.Version2()
                            self.version2.parent = self
                            self._children_name_map["version2"] = "version2"
                        return self.version2

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "slave-groups" or name == "version1" or name == "version2"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    self.mac_refresh.is_set or
                    self.redirects_disable.is_set or
                    self.use_bia.is_set or
                    (self.bfd is not None and self.bfd.has_data()) or
                    (self.delay is not None and self.delay.has_data()) or
                    (self.ipv4 is not None and self.ipv4.has_data()) or
                    (self.ipv6 is not None and self.ipv6.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.mac_refresh.yfilter != YFilter.not_set or
                    self.redirects_disable.yfilter != YFilter.not_set or
                    self.use_bia.yfilter != YFilter.not_set or
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
                    path_buffer = "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.mac_refresh.is_set or self.mac_refresh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mac_refresh.get_name_leafdata())
                if (self.redirects_disable.is_set or self.redirects_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.redirects_disable.get_name_leafdata())
                if (self.use_bia.is_set or self.use_bia.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.use_bia.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bfd"):
                    if (self.bfd is None):
                        self.bfd = Hsrp.Interfaces.Interface.Bfd()
                        self.bfd.parent = self
                        self._children_name_map["bfd"] = "bfd"
                    return self.bfd

                if (child_yang_name == "delay"):
                    if (self.delay is None):
                        self.delay = Hsrp.Interfaces.Interface.Delay()
                        self.delay.parent = self
                        self._children_name_map["delay"] = "delay"
                    return self.delay

                if (child_yang_name == "ipv4"):
                    if (self.ipv4 is None):
                        self.ipv4 = Hsrp.Interfaces.Interface.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"
                    return self.ipv4

                if (child_yang_name == "ipv6"):
                    if (self.ipv6 is None):
                        self.ipv6 = Hsrp.Interfaces.Interface.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"
                    return self.ipv6

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bfd" or name == "delay" or name == "ipv4" or name == "ipv6" or name == "interface-name" or name == "mac-refresh" or name == "redirects-disable" or name == "use-bia"):
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
                if(value_path == "redirects-disable"):
                    self.redirects_disable = value
                    self.redirects_disable.value_namespace = name_space
                    self.redirects_disable.value_namespace_prefix = name_space_prefix
                if(value_path == "use-bia"):
                    self.use_bia = value
                    self.use_bia.value_namespace = name_space
                    self.use_bia.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp/%s" % self.get_segment_path()
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
                c = Hsrp.Interfaces.Interface()
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


    class Logging(Entity):
        """
        HSRP logging options
        
        .. attribute:: state_change_disable
        
        	HSRP state change IOS messages disable
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ipv4-hsrp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Hsrp.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "hsrp"

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
                        super(Hsrp.Logging, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Hsrp.Logging, self).__setattr__(name, value)

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
                path_buffer = "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp/%s" % self.get_segment_path()
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
        path_buffer = "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp" + path_buffer

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
                self.interfaces = Hsrp.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "logging"):
            if (self.logging is None):
                self.logging = Hsrp.Logging()
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
        self._top_entity = Hsrp()
        return self._top_entity

