""" Cisco_IOS_XR_ipv4_hsrp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-hsrp package configuration.

This module contains definitions
for the following management objects\:
  hsrp\: HSRP configuration

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
    _revision = '2017-05-01'

    def __init__(self):
        super(Hsrp, self).__init__()
        self._top_entity = None

        self.yang_name = "hsrp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-hsrp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"interfaces" : ("interfaces", Hsrp.Interfaces), "logging" : ("logging", Hsrp.Logging)}
        self._child_list_classes = {}

        self.interfaces = Hsrp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.logging = Hsrp.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"
        self._children_yang_names.add("logging")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp"


    class Interfaces(Entity):
        """
        Interface Table for HSRP configuration
        
        .. attribute:: interface
        
        	Per\-interface HSRP configuration
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-hsrp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Hsrp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "hsrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", Hsrp.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Hsrp.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Per\-interface HSRP configuration
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
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
            _revision = '2017-05-01'

            def __init__(self):
                super(Hsrp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bfd" : ("bfd", Hsrp.Interfaces.Interface.Bfd), "delay" : ("delay", Hsrp.Interfaces.Interface.Delay), "ipv4" : ("ipv4", Hsrp.Interfaces.Interface.Ipv4), "ipv6" : ("ipv6", Hsrp.Interfaces.Interface.Ipv6)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Hsrp.Interfaces.Interface, ['interface_name', 'mac_refresh', 'redirects_disable', 'use_bia'], name, value)


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
                _revision = '2017-05-01'

                def __init__(self):
                    super(Hsrp.Interfaces.Interface.Bfd, self).__init__()

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
                    self._perform_setattr(Hsrp.Interfaces.Interface.Bfd, ['detection_multiplier', 'interval'], name, value)


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
                _revision = '2017-05-01'

                def __init__(self):
                    super(Hsrp.Interfaces.Interface.Delay, self).__init__()

                    self.yang_name = "delay"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.minimum_delay = YLeaf(YType.uint32, "minimum-delay")

                    self.reload_delay = YLeaf(YType.uint32, "reload-delay")
                    self._segment_path = lambda: "delay"

                def __setattr__(self, name, value):
                    self._perform_setattr(Hsrp.Interfaces.Interface.Delay, ['minimum_delay', 'reload_delay'], name, value)


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
                _revision = '2017-05-01'

                def __init__(self):
                    super(Hsrp.Interfaces.Interface.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"slave-groups" : ("slave_groups", Hsrp.Interfaces.Interface.Ipv4.SlaveGroups), "version1" : ("version1", Hsrp.Interfaces.Interface.Ipv4.Version1), "version2" : ("version2", Hsrp.Interfaces.Interface.Ipv4.Version2)}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "ipv4"


                class SlaveGroups(Entity):
                    """
                    The HSRP slave group configuration table
                    
                    .. attribute:: slave_group
                    
                    	The HSRP slave group being configured
                    	**type**\: list of    :py:class:`SlaveGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups, self).__init__()

                        self.yang_name = "slave-groups"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"slave-group" : ("slave_group", Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup)}

                        self.slave_group = YList(self)
                        self._segment_path = lambda: "slave-groups"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups, [], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup, self).__init__()

                            self.yang_name = "slave-group"
                            self.yang_parent_name = "slave-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"secondary-ipv4-addresses" : ("secondary_ipv4_addresses", Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses)}
                            self._child_list_classes = {}

                            self.slave_group_number = YLeaf(YType.uint32, "slave-group-number")

                            self.follow = YLeaf(YType.str, "follow")

                            self.primary_ipv4_address = YLeaf(YType.str, "primary-ipv4-address")

                            self.virtual_mac_address = YLeaf(YType.str, "virtual-mac-address")

                            self.secondary_ipv4_addresses = Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses()
                            self.secondary_ipv4_addresses.parent = self
                            self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                            self._children_yang_names.add("secondary-ipv4-addresses")
                            self._segment_path = lambda: "slave-group" + "[slave-group-number='" + self.slave_group_number.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup, ['slave_group_number', 'follow', 'primary_ipv4_address', 'virtual_mac_address'], name, value)


                        class SecondaryIpv4Addresses(Entity):
                            """
                            Secondary HSRP IP address Table
                            
                            .. attribute:: secondary_ipv4_address
                            
                            	Secondary HSRP IP address
                            	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses, self).__init__()

                                self.yang_name = "secondary-ipv4-addresses"
                                self.yang_parent_name = "slave-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"secondary-ipv4-address" : ("secondary_ipv4_address", Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address)}

                                self.secondary_ipv4_address = YList(self)
                                self._segment_path = lambda: "secondary-ipv4-addresses"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses, [], name, value)


                            class SecondaryIpv4Address(Entity):
                                """
                                Secondary HSRP IP address
                                
                                .. attribute:: address  <key>
                                
                                	HSRP IP address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                    self.yang_name = "secondary-ipv4-address"
                                    self.yang_parent_name = "secondary-ipv4-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address = YLeaf(YType.str, "address")
                                    self._segment_path = lambda: "secondary-ipv4-address" + "[address='" + self.address.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address, ['address'], name, value)


                class Version1(Entity):
                    """
                    Version 1 HSRP configuration
                    
                    .. attribute:: groups
                    
                    	The HSRP group configuration table
                    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv4.Version1, self).__init__()

                        self.yang_name = "version1"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"groups" : ("groups", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups)}
                        self._child_list_classes = {}

                        self.groups = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups()
                        self.groups.parent = self
                        self._children_name_map["groups"] = "groups"
                        self._children_yang_names.add("groups")
                        self._segment_path = lambda: "version1"


                    class Groups(Entity):
                        """
                        The HSRP group configuration table
                        
                        .. attribute:: group
                        
                        	The HSRP group being configured
                        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group>`
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups, self).__init__()

                            self.yang_name = "groups"
                            self.yang_parent_name = "version1"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"group" : ("group", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group)}

                            self.group = YList(self)
                            self._segment_path = lambda: "groups"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups, [], name, value)


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group, self).__init__()

                                self.yang_name = "group"
                                self.yang_parent_name = "groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"bfd" : ("bfd", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd), "primary-ipv4-address" : ("primary_ipv4_address", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address), "secondary-ipv4-addresses" : ("secondary_ipv4_addresses", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses), "timers" : ("timers", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers), "tracked-interfaces" : ("tracked_interfaces", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces), "tracked-objects" : ("tracked_objects", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects)}
                                self._child_list_classes = {}

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
                                self._segment_path = lambda: "group" + "[group-number='" + self.group_number.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group, ['group_number', 'authentication', 'preempt', 'priority', 'session_name', 'virtual_mac_address'], name, value)


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
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd, self).__init__()

                                    self.yang_name = "bfd"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address = YLeaf(YType.str, "address")

                                    self.interface_name = YLeaf(YType.str, "interface-name")
                                    self._segment_path = lambda: "bfd"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd, ['address', 'interface_name'], name, value)


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
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address, self).__init__()

                                    self.yang_name = "primary-ipv4-address"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address = YLeaf(YType.str, "address")

                                    self.virtual_ip_learn = YLeaf(YType.boolean, "virtual-ip-learn")
                                    self._segment_path = lambda: "primary-ipv4-address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address, ['address', 'virtual_ip_learn'], name, value)


                            class SecondaryIpv4Addresses(Entity):
                                """
                                Secondary HSRP IP address Table
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	Secondary HSRP IP address
                                	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses, self).__init__()

                                    self.yang_name = "secondary-ipv4-addresses"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"secondary-ipv4-address" : ("secondary_ipv4_address", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address)}

                                    self.secondary_ipv4_address = YList(self)
                                    self._segment_path = lambda: "secondary-ipv4-addresses"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses, [], name, value)


                                class SecondaryIpv4Address(Entity):
                                    """
                                    Secondary HSRP IP address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	HSRP IP address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                        self.yang_name = "secondary-ipv4-address"
                                        self.yang_parent_name = "secondary-ipv4-addresses"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.address = YLeaf(YType.str, "address")
                                        self._segment_path = lambda: "secondary-ipv4-address" + "[address='" + self.address.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address, ['address'], name, value)


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
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers, self).__init__()

                                    self.yang_name = "timers"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.hello_msec = YLeaf(YType.uint32, "hello-msec")

                                    self.hello_msec_flag = YLeaf(YType.boolean, "hello-msec-flag")

                                    self.hello_sec = YLeaf(YType.uint32, "hello-sec")

                                    self.hold_msec = YLeaf(YType.uint32, "hold-msec")

                                    self.hold_msec_flag = YLeaf(YType.boolean, "hold-msec-flag")

                                    self.hold_sec = YLeaf(YType.uint32, "hold-sec")
                                    self._segment_path = lambda: "timers"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers, ['hello_msec', 'hello_msec_flag', 'hello_sec', 'hold_msec', 'hold_msec_flag', 'hold_sec'], name, value)


                            class TrackedInterfaces(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_interface
                                
                                	Interface being tracked
                                	**type**\: list of    :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces, self).__init__()

                                    self.yang_name = "tracked-interfaces"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"tracked-interface" : ("tracked_interface", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface)}

                                    self.tracked_interface = YList(self)
                                    self._segment_path = lambda: "tracked-interfaces"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces, [], name, value)


                                class TrackedInterface(Entity):
                                    """
                                    Interface being tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface, self).__init__()

                                        self.yang_name = "tracked-interface"
                                        self.yang_parent_name = "tracked-interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.interface_name = YLeaf(YType.str, "interface-name")

                                        self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")
                                        self._segment_path = lambda: "tracked-interface" + "[interface-name='" + self.interface_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface, ['interface_name', 'priority_decrement'], name, value)


                            class TrackedObjects(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_object
                                
                                	Object being tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"tracked-object" : ("tracked_object", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject)}

                                    self.tracked_object = YList(self)
                                    self._segment_path = lambda: "tracked-objects"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects, [], name, value)


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
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject, self).__init__()

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
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject, ['object_name', 'priority_decrement'], name, value)


                class Version2(Entity):
                    """
                    Version 2 HSRP configuration
                    
                    .. attribute:: groups
                    
                    	The HSRP group configuration table
                    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv4.Version2, self).__init__()

                        self.yang_name = "version2"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"groups" : ("groups", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups)}
                        self._child_list_classes = {}

                        self.groups = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups()
                        self.groups.parent = self
                        self._children_name_map["groups"] = "groups"
                        self._children_yang_names.add("groups")
                        self._segment_path = lambda: "version2"


                    class Groups(Entity):
                        """
                        The HSRP group configuration table
                        
                        .. attribute:: group
                        
                        	The HSRP group being configured
                        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group>`
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups, self).__init__()

                            self.yang_name = "groups"
                            self.yang_parent_name = "version2"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"group" : ("group", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group)}

                            self.group = YList(self)
                            self._segment_path = lambda: "groups"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups, [], name, value)


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group, self).__init__()

                                self.yang_name = "group"
                                self.yang_parent_name = "groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"bfd" : ("bfd", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd), "primary-ipv4-address" : ("primary_ipv4_address", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address), "secondary-ipv4-addresses" : ("secondary_ipv4_addresses", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses), "timers" : ("timers", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers), "tracked-interfaces" : ("tracked_interfaces", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces), "tracked-objects" : ("tracked_objects", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects)}
                                self._child_list_classes = {}

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
                                self._segment_path = lambda: "group" + "[group-number='" + self.group_number.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group, ['group_number', 'preempt', 'priority', 'session_name', 'virtual_mac_address'], name, value)


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
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd, self).__init__()

                                    self.yang_name = "bfd"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address = YLeaf(YType.str, "address")

                                    self.interface_name = YLeaf(YType.str, "interface-name")
                                    self._segment_path = lambda: "bfd"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd, ['address', 'interface_name'], name, value)


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
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address, self).__init__()

                                    self.yang_name = "primary-ipv4-address"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address = YLeaf(YType.str, "address")

                                    self.virtual_ip_learn = YLeaf(YType.boolean, "virtual-ip-learn")
                                    self._segment_path = lambda: "primary-ipv4-address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address, ['address', 'virtual_ip_learn'], name, value)


                            class SecondaryIpv4Addresses(Entity):
                                """
                                Secondary HSRP IP address Table
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	Secondary HSRP IP address
                                	**type**\: list of    :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses, self).__init__()

                                    self.yang_name = "secondary-ipv4-addresses"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"secondary-ipv4-address" : ("secondary_ipv4_address", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address)}

                                    self.secondary_ipv4_address = YList(self)
                                    self._segment_path = lambda: "secondary-ipv4-addresses"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses, [], name, value)


                                class SecondaryIpv4Address(Entity):
                                    """
                                    Secondary HSRP IP address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	HSRP IP address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                        self.yang_name = "secondary-ipv4-address"
                                        self.yang_parent_name = "secondary-ipv4-addresses"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.address = YLeaf(YType.str, "address")
                                        self._segment_path = lambda: "secondary-ipv4-address" + "[address='" + self.address.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address, ['address'], name, value)


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
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers, self).__init__()

                                    self.yang_name = "timers"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.hello_msec = YLeaf(YType.uint32, "hello-msec")

                                    self.hello_msec_flag = YLeaf(YType.boolean, "hello-msec-flag")

                                    self.hello_sec = YLeaf(YType.uint32, "hello-sec")

                                    self.hold_msec = YLeaf(YType.uint32, "hold-msec")

                                    self.hold_msec_flag = YLeaf(YType.boolean, "hold-msec-flag")

                                    self.hold_sec = YLeaf(YType.uint32, "hold-sec")
                                    self._segment_path = lambda: "timers"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers, ['hello_msec', 'hello_msec_flag', 'hello_sec', 'hold_msec', 'hold_msec_flag', 'hold_sec'], name, value)


                            class TrackedInterfaces(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_interface
                                
                                	Interface being tracked
                                	**type**\: list of    :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces, self).__init__()

                                    self.yang_name = "tracked-interfaces"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"tracked-interface" : ("tracked_interface", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface)}

                                    self.tracked_interface = YList(self)
                                    self._segment_path = lambda: "tracked-interfaces"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces, [], name, value)


                                class TrackedInterface(Entity):
                                    """
                                    Interface being tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface, self).__init__()

                                        self.yang_name = "tracked-interface"
                                        self.yang_parent_name = "tracked-interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.interface_name = YLeaf(YType.str, "interface-name")

                                        self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")
                                        self._segment_path = lambda: "tracked-interface" + "[interface-name='" + self.interface_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface, ['interface_name', 'priority_decrement'], name, value)


                            class TrackedObjects(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_object
                                
                                	Object being tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"tracked-object" : ("tracked_object", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject)}

                                    self.tracked_object = YList(self)
                                    self._segment_path = lambda: "tracked-objects"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects, [], name, value)


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
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject, self).__init__()

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
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject, ['object_name', 'priority_decrement'], name, value)


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
                _revision = '2017-05-01'

                def __init__(self):
                    super(Hsrp.Interfaces.Interface.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"slave-groups" : ("slave_groups", Hsrp.Interfaces.Interface.Ipv6.SlaveGroups), "version2" : ("version2", Hsrp.Interfaces.Interface.Ipv6.Version2)}
                    self._child_list_classes = {}

                    self.slave_groups = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups()
                    self.slave_groups.parent = self
                    self._children_name_map["slave_groups"] = "slave-groups"
                    self._children_yang_names.add("slave-groups")

                    self.version2 = Hsrp.Interfaces.Interface.Ipv6.Version2()
                    self.version2.parent = self
                    self._children_name_map["version2"] = "version2"
                    self._children_yang_names.add("version2")
                    self._segment_path = lambda: "ipv6"


                class SlaveGroups(Entity):
                    """
                    The HSRP slave group configuration table
                    
                    .. attribute:: slave_group
                    
                    	The HSRP slave group being configured
                    	**type**\: list of    :py:class:`SlaveGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups, self).__init__()

                        self.yang_name = "slave-groups"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"slave-group" : ("slave_group", Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup)}

                        self.slave_group = YList(self)
                        self._segment_path = lambda: "slave-groups"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups, [], name, value)


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
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup, self).__init__()

                            self.yang_name = "slave-group"
                            self.yang_parent_name = "slave-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"global-ipv6-addresses" : ("global_ipv6_addresses", Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses), "link-local-ipv6-address" : ("link_local_ipv6_address", Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address)}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "slave-group" + "[slave-group-number='" + self.slave_group_number.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup, ['slave_group_number', 'follow', 'virtual_mac_address'], name, value)


                        class GlobalIpv6Addresses(Entity):
                            """
                            The table of HSRP virtual global IPv6
                            addresses
                            
                            .. attribute:: global_ipv6_address
                            
                            	A HSRP virtual global IPv6 IP address
                            	**type**\: list of    :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address>`
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses, self).__init__()

                                self.yang_name = "global-ipv6-addresses"
                                self.yang_parent_name = "slave-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"global-ipv6-address" : ("global_ipv6_address", Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address)}

                                self.global_ipv6_address = YList(self)
                                self._segment_path = lambda: "global-ipv6-addresses"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses, [], name, value)


                            class GlobalIpv6Address(Entity):
                                """
                                A HSRP virtual global IPv6 IP address
                                
                                .. attribute:: address  <key>
                                
                                	HSRP virtual global IPv6 address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address, self).__init__()

                                    self.yang_name = "global-ipv6-address"
                                    self.yang_parent_name = "global-ipv6-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address = YLeaf(YType.str, "address")
                                    self._segment_path = lambda: "global-ipv6-address" + "[address='" + self.address.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address, ['address'], name, value)


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address, self).__init__()

                                self.yang_name = "link-local-ipv6-address"
                                self.yang_parent_name = "slave-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.address = YLeaf(YType.str, "address")

                                self.auto_configure = YLeaf(YType.enumeration, "auto-configure")
                                self._segment_path = lambda: "link-local-ipv6-address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address, ['address', 'auto_configure'], name, value)


                class Version2(Entity):
                    """
                    Version 2 HSRP configuration
                    
                    .. attribute:: groups
                    
                    	The HSRP group configuration table
                    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv6.Version2, self).__init__()

                        self.yang_name = "version2"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"groups" : ("groups", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups)}
                        self._child_list_classes = {}

                        self.groups = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups()
                        self.groups.parent = self
                        self._children_name_map["groups"] = "groups"
                        self._children_yang_names.add("groups")
                        self._segment_path = lambda: "version2"


                    class Groups(Entity):
                        """
                        The HSRP group configuration table
                        
                        .. attribute:: group
                        
                        	The HSRP group being configured
                        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group>`
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups, self).__init__()

                            self.yang_name = "groups"
                            self.yang_parent_name = "version2"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"group" : ("group", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group)}

                            self.group = YList(self)
                            self._segment_path = lambda: "groups"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups, [], name, value)


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
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group, self).__init__()

                                self.yang_name = "group"
                                self.yang_parent_name = "groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"bfd" : ("bfd", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd), "global-ipv6-addresses" : ("global_ipv6_addresses", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses), "link-local-ipv6-address" : ("link_local_ipv6_address", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address), "timers" : ("timers", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers), "tracked-interfaces" : ("tracked_interfaces", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces), "tracked-objects" : ("tracked_objects", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects)}
                                self._child_list_classes = {}

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
                                self._segment_path = lambda: "group" + "[group-number='" + self.group_number.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group, ['group_number', 'preempt', 'priority', 'session_name', 'virtual_mac_address'], name, value)


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
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd, self).__init__()

                                    self.yang_name = "bfd"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address = YLeaf(YType.str, "address")

                                    self.interface_name = YLeaf(YType.str, "interface-name")
                                    self._segment_path = lambda: "bfd"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd, ['address', 'interface_name'], name, value)


                            class GlobalIpv6Addresses(Entity):
                                """
                                The table of HSRP virtual global IPv6
                                addresses
                                
                                .. attribute:: global_ipv6_address
                                
                                	A HSRP virtual global IPv6 IP address
                                	**type**\: list of    :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses, self).__init__()

                                    self.yang_name = "global-ipv6-addresses"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"global-ipv6-address" : ("global_ipv6_address", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address)}

                                    self.global_ipv6_address = YList(self)
                                    self._segment_path = lambda: "global-ipv6-addresses"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses, [], name, value)


                                class GlobalIpv6Address(Entity):
                                    """
                                    A HSRP virtual global IPv6 IP address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	HSRP virtual global IPv6 address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address, self).__init__()

                                        self.yang_name = "global-ipv6-address"
                                        self.yang_parent_name = "global-ipv6-addresses"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.address = YLeaf(YType.str, "address")
                                        self._segment_path = lambda: "global-ipv6-address" + "[address='" + self.address.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address, ['address'], name, value)


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
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address, self).__init__()

                                    self.yang_name = "link-local-ipv6-address"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address = YLeaf(YType.str, "address")

                                    self.auto_configure = YLeaf(YType.enumeration, "auto-configure")
                                    self._segment_path = lambda: "link-local-ipv6-address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address, ['address', 'auto_configure'], name, value)


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
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers, self).__init__()

                                    self.yang_name = "timers"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.hello_msec = YLeaf(YType.uint32, "hello-msec")

                                    self.hello_msec_flag = YLeaf(YType.boolean, "hello-msec-flag")

                                    self.hello_sec = YLeaf(YType.uint32, "hello-sec")

                                    self.hold_msec = YLeaf(YType.uint32, "hold-msec")

                                    self.hold_msec_flag = YLeaf(YType.boolean, "hold-msec-flag")

                                    self.hold_sec = YLeaf(YType.uint32, "hold-sec")
                                    self._segment_path = lambda: "timers"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers, ['hello_msec', 'hello_msec_flag', 'hello_sec', 'hold_msec', 'hold_msec_flag', 'hold_sec'], name, value)


                            class TrackedInterfaces(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_interface
                                
                                	Interface being tracked
                                	**type**\: list of    :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces, self).__init__()

                                    self.yang_name = "tracked-interfaces"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"tracked-interface" : ("tracked_interface", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface)}

                                    self.tracked_interface = YList(self)
                                    self._segment_path = lambda: "tracked-interfaces"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces, [], name, value)


                                class TrackedInterface(Entity):
                                    """
                                    Interface being tracked
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Interface being tracked
                                    	**type**\:  str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface, self).__init__()

                                        self.yang_name = "tracked-interface"
                                        self.yang_parent_name = "tracked-interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.interface_name = YLeaf(YType.str, "interface-name")

                                        self.priority_decrement = YLeaf(YType.uint32, "priority-decrement")
                                        self._segment_path = lambda: "tracked-interface" + "[interface-name='" + self.interface_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface, ['interface_name', 'priority_decrement'], name, value)


                            class TrackedObjects(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_object
                                
                                	Object being tracked
                                	**type**\: list of    :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"tracked-object" : ("tracked_object", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject)}

                                    self.tracked_object = YList(self)
                                    self._segment_path = lambda: "tracked-objects"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects, [], name, value)


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
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject, self).__init__()

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
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject, ['object_name', 'priority_decrement'], name, value)


    class Logging(Entity):
        """
        HSRP logging options
        
        .. attribute:: state_change_disable
        
        	HSRP state change IOS messages disable
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ipv4-hsrp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Hsrp.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "hsrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.state_change_disable = YLeaf(YType.empty, "state-change-disable")
            self._segment_path = lambda: "logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Hsrp.Logging, ['state_change_disable'], name, value)

    def clone_ptr(self):
        self._top_entity = Hsrp()
        return self._top_entity

