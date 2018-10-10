""" Cisco_IOS_XR_ipv4_hsrp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-hsrp package configuration.

This module contains definitions
for the following management objects\:
  hsrp\: HSRP configuration

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



class HsrpLinklocal(Enum):
    """
    HsrpLinklocal (Enum Class)

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
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces>`
    
    .. attribute:: logging
    
    	HSRP logging options
    	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Logging>`
    
    

    """

    _prefix = 'ipv4-hsrp-cfg'
    _revision = '2017-11-05'

    def __init__(self):
        super(Hsrp, self).__init__()
        self._top_entity = None

        self.yang_name = "hsrp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-hsrp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("interfaces", ("interfaces", Hsrp.Interfaces)), ("logging", ("logging", Hsrp.Logging))])
        self._leafs = OrderedDict()

        self.interfaces = Hsrp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"

        self.logging = Hsrp.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Hsrp, [], name, value)


    class Interfaces(Entity):
        """
        Interface Table for HSRP configuration
        
        .. attribute:: interface
        
        	Per\-interface HSRP configuration
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-hsrp-cfg'
        _revision = '2017-11-05'

        def __init__(self):
            super(Hsrp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "hsrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Hsrp.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Hsrp.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Per\-interface HSRP configuration
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: ipv6
            
            	IPv6 HSRP configuration
            	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6>`
            
            .. attribute:: bfd
            
            	BFD configuration
            	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Bfd>`
            
            .. attribute:: delay
            
            	Minimum and Reload Delay
            	**type**\:  :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Delay>`
            
            	**presence node**\: True
            
            .. attribute:: ipv4
            
            	IPv4 HSRP configuration
            	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4>`
            
            .. attribute:: mac_refresh
            
            	HSRP MGO slave MAC refresh rate
            	**type**\: int
            
            	**range:** 0..10000
            
            	**default value**\: 60
            
            .. attribute:: use_bia
            
            	Use burned\-in address
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: redirects_disable
            
            	Disable HSRP filtered ICMP redirects
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ipv4-hsrp-cfg'
            _revision = '2017-11-05'

            def __init__(self):
                super(Hsrp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("ipv6", ("ipv6", Hsrp.Interfaces.Interface.Ipv6)), ("bfd", ("bfd", Hsrp.Interfaces.Interface.Bfd)), ("delay", ("delay", Hsrp.Interfaces.Interface.Delay)), ("ipv4", ("ipv4", Hsrp.Interfaces.Interface.Ipv4))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('mac_refresh', (YLeaf(YType.uint32, 'mac-refresh'), ['int'])),
                    ('use_bia', (YLeaf(YType.empty, 'use-bia'), ['Empty'])),
                    ('redirects_disable', (YLeaf(YType.empty, 'redirects-disable'), ['Empty'])),
                ])
                self.interface_name = None
                self.mac_refresh = None
                self.use_bia = None
                self.redirects_disable = None

                self.ipv6 = Hsrp.Interfaces.Interface.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"

                self.bfd = Hsrp.Interfaces.Interface.Bfd()
                self.bfd.parent = self
                self._children_name_map["bfd"] = "bfd"

                self.delay = None
                self._children_name_map["delay"] = "delay"

                self.ipv4 = Hsrp.Interfaces.Interface.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Hsrp.Interfaces.Interface, ['interface_name', 'mac_refresh', 'use_bia', 'redirects_disable'], name, value)


            class Ipv6(Entity):
                """
                IPv6 HSRP configuration
                
                .. attribute:: version2
                
                	Version 2 HSRP configuration
                	**type**\:  :py:class:`Version2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2>`
                
                .. attribute:: slave_groups
                
                	The HSRP slave group configuration table
                	**type**\:  :py:class:`SlaveGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups>`
                
                

                """

                _prefix = 'ipv4-hsrp-cfg'
                _revision = '2017-11-05'

                def __init__(self):
                    super(Hsrp.Interfaces.Interface.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("version2", ("version2", Hsrp.Interfaces.Interface.Ipv6.Version2)), ("slave-groups", ("slave_groups", Hsrp.Interfaces.Interface.Ipv6.SlaveGroups))])
                    self._leafs = OrderedDict()

                    self.version2 = Hsrp.Interfaces.Interface.Ipv6.Version2()
                    self.version2.parent = self
                    self._children_name_map["version2"] = "version2"

                    self.slave_groups = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups()
                    self.slave_groups.parent = self
                    self._children_name_map["slave_groups"] = "slave-groups"
                    self._segment_path = lambda: "ipv6"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6, [], name, value)


                class Version2(Entity):
                    """
                    Version 2 HSRP configuration
                    
                    .. attribute:: groups
                    
                    	The HSRP group configuration table
                    	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2017-11-05'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv6.Version2, self).__init__()

                        self.yang_name = "version2"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("groups", ("groups", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups))])
                        self._leafs = OrderedDict()

                        self.groups = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups()
                        self.groups.parent = self
                        self._children_name_map["groups"] = "groups"
                        self._segment_path = lambda: "version2"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2, [], name, value)


                    class Groups(Entity):
                        """
                        The HSRP group configuration table
                        
                        .. attribute:: group
                        
                        	The HSRP group being configured
                        	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group>`
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2017-11-05'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups, self).__init__()

                            self.yang_name = "groups"
                            self.yang_parent_name = "version2"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("group", ("group", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group))])
                            self._leafs = OrderedDict()

                            self.group = YList(self)
                            self._segment_path = lambda: "groups"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups, [], name, value)


                        class Group(Entity):
                            """
                            The HSRP group being configured
                            
                            .. attribute:: group_number  (key)
                            
                            	HSRP group number
                            	**type**\: int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection
                            	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd>`
                            
                            .. attribute:: tracked_interfaces
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:  :py:class:`TrackedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces>`
                            
                            .. attribute:: tracked_objects
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:  :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects>`
                            
                            .. attribute:: timers
                            
                            	Hello and hold timers
                            	**type**\:  :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers>`
                            
                            .. attribute:: link_local_ipv6_address
                            
                            	The HSRP IPv6 virtual linklocal address
                            	**type**\:  :py:class:`LinkLocalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address>`
                            
                            .. attribute:: global_ipv6_addresses
                            
                            	The table of HSRP virtual global IPv6 addresses
                            	**type**\:  :py:class:`GlobalIpv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses>`
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**default value**\: 100
                            
                            .. attribute:: preempt
                            
                            	Force active if higher priority
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 0
                            
                            .. attribute:: session_name
                            
                            	HSRP Session name (for MGO)
                            	**type**\: str
                            
                            	**length:** 1..16
                            
                            .. attribute:: virtual_mac_address
                            
                            	HSRP MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2017-11-05'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group, self).__init__()

                                self.yang_name = "group"
                                self.yang_parent_name = "groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_number']
                                self._child_classes = OrderedDict([("bfd", ("bfd", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd)), ("tracked-interfaces", ("tracked_interfaces", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces)), ("tracked-objects", ("tracked_objects", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects)), ("timers", ("timers", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers)), ("link-local-ipv6-address", ("link_local_ipv6_address", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address)), ("global-ipv6-addresses", ("global_ipv6_addresses", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses))])
                                self._leafs = OrderedDict([
                                    ('group_number', (YLeaf(YType.uint32, 'group-number'), ['int'])),
                                    ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                    ('preempt', (YLeaf(YType.uint32, 'preempt'), ['int'])),
                                    ('session_name', (YLeaf(YType.str, 'session-name'), ['str'])),
                                    ('virtual_mac_address', (YLeaf(YType.str, 'virtual-mac-address'), ['str'])),
                                ])
                                self.group_number = None
                                self.priority = None
                                self.preempt = None
                                self.session_name = None
                                self.virtual_mac_address = None

                                self.bfd = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd()
                                self.bfd.parent = self
                                self._children_name_map["bfd"] = "bfd"

                                self.tracked_interfaces = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces()
                                self.tracked_interfaces.parent = self
                                self._children_name_map["tracked_interfaces"] = "tracked-interfaces"

                                self.tracked_objects = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects()
                                self.tracked_objects.parent = self
                                self._children_name_map["tracked_objects"] = "tracked-objects"

                                self.timers = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers()
                                self.timers.parent = self
                                self._children_name_map["timers"] = "timers"

                                self.link_local_ipv6_address = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address()
                                self.link_local_ipv6_address.parent = self
                                self._children_name_map["link_local_ipv6_address"] = "link-local-ipv6-address"

                                self.global_ipv6_addresses = Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses()
                                self.global_ipv6_addresses.parent = self
                                self._children_name_map["global_ipv6_addresses"] = "global-ipv6-addresses"
                                self._segment_path = lambda: "group" + "[group-number='" + str(self.group_number) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group, ['group_number', 'priority', 'preempt', 'session_name', 'virtual_mac_address'], name, value)


                            class Bfd(Entity):
                                """
                                Enable use of Bidirectional Forwarding
                                Detection
                                
                                .. attribute:: address
                                
                                	Enable BFD for this remote IP
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface name to run BFD
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd, self).__init__()

                                    self.yang_name = "bfd"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ])
                                    self.address = None
                                    self.interface_name = None
                                    self._segment_path = lambda: "bfd"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Bfd, ['address', 'interface_name'], name, value)


                            class TrackedInterfaces(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_interface
                                
                                	Interface being tracked
                                	**type**\: list of  		 :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces, self).__init__()

                                    self.yang_name = "tracked-interfaces"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("tracked-interface", ("tracked_interface", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface))])
                                    self._leafs = OrderedDict()

                                    self.tracked_interface = YList(self)
                                    self._segment_path = lambda: "tracked-interfaces"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces, [], name, value)


                                class TrackedInterface(Entity):
                                    """
                                    Interface being tracked
                                    
                                    .. attribute:: interface_name  (key)
                                    
                                    	Interface being tracked
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-11-05'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface, self).__init__()

                                        self.yang_name = "tracked-interface"
                                        self.yang_parent_name = "tracked-interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['interface_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                            ('priority_decrement', (YLeaf(YType.uint32, 'priority-decrement'), ['int'])),
                                        ])
                                        self.interface_name = None
                                        self.priority_decrement = None
                                        self._segment_path = lambda: "tracked-interface" + "[interface-name='" + str(self.interface_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedInterfaces.TrackedInterface, ['interface_name', 'priority_decrement'], name, value)


                            class TrackedObjects(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_object
                                
                                	Object being tracked
                                	**type**\: list of  		 :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("tracked-object", ("tracked_object", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject))])
                                    self._leafs = OrderedDict()

                                    self.tracked_object = YList(self)
                                    self._segment_path = lambda: "tracked-objects"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects, [], name, value)


                                class TrackedObject(Entity):
                                    """
                                    Object being tracked
                                    
                                    .. attribute:: object_name  (key)
                                    
                                    	Interface being tracked
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-11-05'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject, self).__init__()

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
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.TrackedObjects.TrackedObject, ['object_name', 'priority_decrement'], name, value)


                            class Timers(Entity):
                                """
                                Hello and hold timers
                                
                                .. attribute:: hello_msec_flag
                                
                                	TRUE \- Hello time configured in milliseconds, FALSE \- Hello time configured in seconds
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hello_msec
                                
                                	Hello time in msecs
                                	**type**\: int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hello_sec
                                
                                	Hello time in seconds
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 3
                                
                                .. attribute:: hold_msec_flag
                                
                                	TRUE \- Hold time configured in milliseconds, FALSE \- Hold time configured in seconds
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hold_msec
                                
                                	Hold time in msecs
                                	**type**\: int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hold_sec
                                
                                	Hold time in seconds
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 10
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers, self).__init__()

                                    self.yang_name = "timers"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('hello_msec_flag', (YLeaf(YType.boolean, 'hello-msec-flag'), ['bool'])),
                                        ('hello_msec', (YLeaf(YType.uint32, 'hello-msec'), ['int'])),
                                        ('hello_sec', (YLeaf(YType.uint32, 'hello-sec'), ['int'])),
                                        ('hold_msec_flag', (YLeaf(YType.boolean, 'hold-msec-flag'), ['bool'])),
                                        ('hold_msec', (YLeaf(YType.uint32, 'hold-msec'), ['int'])),
                                        ('hold_sec', (YLeaf(YType.uint32, 'hold-sec'), ['int'])),
                                    ])
                                    self.hello_msec_flag = None
                                    self.hello_msec = None
                                    self.hello_sec = None
                                    self.hold_msec_flag = None
                                    self.hold_msec = None
                                    self.hold_sec = None
                                    self._segment_path = lambda: "timers"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.Timers, ['hello_msec_flag', 'hello_msec', 'hello_sec', 'hold_msec_flag', 'hold_msec', 'hold_sec'], name, value)


                            class LinkLocalIpv6Address(Entity):
                                """
                                The HSRP IPv6 virtual linklocal address
                                
                                .. attribute:: address
                                
                                	HSRP IPv6 virtual linklocal address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: auto_configure
                                
                                	Linklocal Configuration Type
                                	**type**\:  :py:class:`HsrpLinklocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.HsrpLinklocal>`
                                
                                	**default value**\: manual
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address, self).__init__()

                                    self.yang_name = "link-local-ipv6-address"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ('auto_configure', (YLeaf(YType.enumeration, 'auto-configure'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'HsrpLinklocal', '')])),
                                    ])
                                    self.address = None
                                    self.auto_configure = None
                                    self._segment_path = lambda: "link-local-ipv6-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.LinkLocalIpv6Address, ['address', 'auto_configure'], name, value)


                            class GlobalIpv6Addresses(Entity):
                                """
                                The table of HSRP virtual global IPv6
                                addresses
                                
                                .. attribute:: global_ipv6_address
                                
                                	A HSRP virtual global IPv6 IP address
                                	**type**\: list of  		 :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses, self).__init__()

                                    self.yang_name = "global-ipv6-addresses"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("global-ipv6-address", ("global_ipv6_address", Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address))])
                                    self._leafs = OrderedDict()

                                    self.global_ipv6_address = YList(self)
                                    self._segment_path = lambda: "global-ipv6-addresses"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses, [], name, value)


                                class GlobalIpv6Address(Entity):
                                    """
                                    A HSRP virtual global IPv6 IP address
                                    
                                    .. attribute:: address  (key)
                                    
                                    	HSRP virtual global IPv6 address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-11-05'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address, self).__init__()

                                        self.yang_name = "global-ipv6-address"
                                        self.yang_parent_name = "global-ipv6-addresses"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['address']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ])
                                        self.address = None
                                        self._segment_path = lambda: "global-ipv6-address" + "[address='" + str(self.address) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.Version2.Groups.Group.GlobalIpv6Addresses.GlobalIpv6Address, ['address'], name, value)


                class SlaveGroups(Entity):
                    """
                    The HSRP slave group configuration table
                    
                    .. attribute:: slave_group
                    
                    	The HSRP slave group being configured
                    	**type**\: list of  		 :py:class:`SlaveGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2017-11-05'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups, self).__init__()

                        self.yang_name = "slave-groups"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("slave-group", ("slave_group", Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup))])
                        self._leafs = OrderedDict()

                        self.slave_group = YList(self)
                        self._segment_path = lambda: "slave-groups"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups, [], name, value)


                    class SlaveGroup(Entity):
                        """
                        The HSRP slave group being configured
                        
                        .. attribute:: slave_group_number  (key)
                        
                        	HSRP group number
                        	**type**\: int
                        
                        	**range:** 0..4095
                        
                        .. attribute:: link_local_ipv6_address
                        
                        	The HSRP IPv6 virtual linklocal address
                        	**type**\:  :py:class:`LinkLocalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address>`
                        
                        .. attribute:: global_ipv6_addresses
                        
                        	The table of HSRP virtual global IPv6 addresses
                        	**type**\:  :py:class:`GlobalIpv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses>`
                        
                        .. attribute:: follow
                        
                        	HSRP Group name for this slave to follow
                        	**type**\: str
                        
                        .. attribute:: virtual_mac_address
                        
                        	HSRP MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2017-11-05'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup, self).__init__()

                            self.yang_name = "slave-group"
                            self.yang_parent_name = "slave-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['slave_group_number']
                            self._child_classes = OrderedDict([("link-local-ipv6-address", ("link_local_ipv6_address", Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address)), ("global-ipv6-addresses", ("global_ipv6_addresses", Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses))])
                            self._leafs = OrderedDict([
                                ('slave_group_number', (YLeaf(YType.uint32, 'slave-group-number'), ['int'])),
                                ('follow', (YLeaf(YType.str, 'follow'), ['str'])),
                                ('virtual_mac_address', (YLeaf(YType.str, 'virtual-mac-address'), ['str'])),
                            ])
                            self.slave_group_number = None
                            self.follow = None
                            self.virtual_mac_address = None

                            self.link_local_ipv6_address = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address()
                            self.link_local_ipv6_address.parent = self
                            self._children_name_map["link_local_ipv6_address"] = "link-local-ipv6-address"

                            self.global_ipv6_addresses = Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses()
                            self.global_ipv6_addresses.parent = self
                            self._children_name_map["global_ipv6_addresses"] = "global-ipv6-addresses"
                            self._segment_path = lambda: "slave-group" + "[slave-group-number='" + str(self.slave_group_number) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup, ['slave_group_number', 'follow', 'virtual_mac_address'], name, value)


                        class LinkLocalIpv6Address(Entity):
                            """
                            The HSRP IPv6 virtual linklocal address
                            
                            .. attribute:: address
                            
                            	HSRP IPv6 virtual linklocal address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: auto_configure
                            
                            	Linklocal Configuration Type
                            	**type**\:  :py:class:`HsrpLinklocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.HsrpLinklocal>`
                            
                            	**default value**\: manual
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2017-11-05'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address, self).__init__()

                                self.yang_name = "link-local-ipv6-address"
                                self.yang_parent_name = "slave-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                    ('auto_configure', (YLeaf(YType.enumeration, 'auto-configure'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg', 'HsrpLinklocal', '')])),
                                ])
                                self.address = None
                                self.auto_configure = None
                                self._segment_path = lambda: "link-local-ipv6-address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.LinkLocalIpv6Address, ['address', 'auto_configure'], name, value)


                        class GlobalIpv6Addresses(Entity):
                            """
                            The table of HSRP virtual global IPv6
                            addresses
                            
                            .. attribute:: global_ipv6_address
                            
                            	A HSRP virtual global IPv6 IP address
                            	**type**\: list of  		 :py:class:`GlobalIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address>`
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2017-11-05'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses, self).__init__()

                                self.yang_name = "global-ipv6-addresses"
                                self.yang_parent_name = "slave-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("global-ipv6-address", ("global_ipv6_address", Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address))])
                                self._leafs = OrderedDict()

                                self.global_ipv6_address = YList(self)
                                self._segment_path = lambda: "global-ipv6-addresses"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses, [], name, value)


                            class GlobalIpv6Address(Entity):
                                """
                                A HSRP virtual global IPv6 IP address
                                
                                .. attribute:: address  (key)
                                
                                	HSRP virtual global IPv6 address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address, self).__init__()

                                    self.yang_name = "global-ipv6-address"
                                    self.yang_parent_name = "global-ipv6-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['address']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                    ])
                                    self.address = None
                                    self._segment_path = lambda: "global-ipv6-address" + "[address='" + str(self.address) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv6.SlaveGroups.SlaveGroup.GlobalIpv6Addresses.GlobalIpv6Address, ['address'], name, value)


            class Bfd(Entity):
                """
                BFD configuration
                
                .. attribute:: detection_multiplier
                
                	Detection multiplier for BFD sessions created by hsrp
                	**type**\: int
                
                	**range:** 2..50
                
                .. attribute:: interval
                
                	Hello interval for BFD sessions created by hsrp
                	**type**\: int
                
                	**range:** 3..30000
                
                	**units**\: millisecond
                
                

                """

                _prefix = 'ipv4-hsrp-cfg'
                _revision = '2017-11-05'

                def __init__(self):
                    super(Hsrp.Interfaces.Interface.Bfd, self).__init__()

                    self.yang_name = "bfd"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('detection_multiplier', (YLeaf(YType.uint32, 'detection-multiplier'), ['int'])),
                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                    ])
                    self.detection_multiplier = None
                    self.interval = None
                    self._segment_path = lambda: "bfd"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Hsrp.Interfaces.Interface.Bfd, ['detection_multiplier', 'interval'], name, value)


            class Delay(Entity):
                """
                Minimum and Reload Delay
                
                .. attribute:: minimum_delay
                
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

                _prefix = 'ipv4-hsrp-cfg'
                _revision = '2017-11-05'

                def __init__(self):
                    super(Hsrp.Interfaces.Interface.Delay, self).__init__()

                    self.yang_name = "delay"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('minimum_delay', (YLeaf(YType.uint32, 'minimum-delay'), ['int'])),
                        ('reload_delay', (YLeaf(YType.uint32, 'reload-delay'), ['int'])),
                    ])
                    self.minimum_delay = None
                    self.reload_delay = None
                    self._segment_path = lambda: "delay"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Hsrp.Interfaces.Interface.Delay, ['minimum_delay', 'reload_delay'], name, value)


            class Ipv4(Entity):
                """
                IPv4 HSRP configuration
                
                .. attribute:: slave_groups
                
                	The HSRP slave group configuration table
                	**type**\:  :py:class:`SlaveGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.SlaveGroups>`
                
                .. attribute:: version1
                
                	Version 1 HSRP configuration
                	**type**\:  :py:class:`Version1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1>`
                
                .. attribute:: version2
                
                	Version 2 HSRP configuration
                	**type**\:  :py:class:`Version2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2>`
                
                

                """

                _prefix = 'ipv4-hsrp-cfg'
                _revision = '2017-11-05'

                def __init__(self):
                    super(Hsrp.Interfaces.Interface.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("slave-groups", ("slave_groups", Hsrp.Interfaces.Interface.Ipv4.SlaveGroups)), ("version1", ("version1", Hsrp.Interfaces.Interface.Ipv4.Version1)), ("version2", ("version2", Hsrp.Interfaces.Interface.Ipv4.Version2))])
                    self._leafs = OrderedDict()

                    self.slave_groups = Hsrp.Interfaces.Interface.Ipv4.SlaveGroups()
                    self.slave_groups.parent = self
                    self._children_name_map["slave_groups"] = "slave-groups"

                    self.version1 = Hsrp.Interfaces.Interface.Ipv4.Version1()
                    self.version1.parent = self
                    self._children_name_map["version1"] = "version1"

                    self.version2 = Hsrp.Interfaces.Interface.Ipv4.Version2()
                    self.version2.parent = self
                    self._children_name_map["version2"] = "version2"
                    self._segment_path = lambda: "ipv4"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4, [], name, value)


                class SlaveGroups(Entity):
                    """
                    The HSRP slave group configuration table
                    
                    .. attribute:: slave_group
                    
                    	The HSRP slave group being configured
                    	**type**\: list of  		 :py:class:`SlaveGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2017-11-05'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups, self).__init__()

                        self.yang_name = "slave-groups"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("slave-group", ("slave_group", Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup))])
                        self._leafs = OrderedDict()

                        self.slave_group = YList(self)
                        self._segment_path = lambda: "slave-groups"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups, [], name, value)


                    class SlaveGroup(Entity):
                        """
                        The HSRP slave group being configured
                        
                        .. attribute:: slave_group_number  (key)
                        
                        	HSRP group number
                        	**type**\: int
                        
                        	**range:** 0..4095
                        
                        .. attribute:: secondary_ipv4_addresses
                        
                        	Secondary HSRP IP address Table
                        	**type**\:  :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses>`
                        
                        .. attribute:: follow
                        
                        	HSRP Group name for this slave to follow
                        	**type**\: str
                        
                        .. attribute:: virtual_mac_address
                        
                        	HSRP MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: primary_ipv4_address
                        
                        	Primary HSRP IP address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2017-11-05'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup, self).__init__()

                            self.yang_name = "slave-group"
                            self.yang_parent_name = "slave-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['slave_group_number']
                            self._child_classes = OrderedDict([("secondary-ipv4-addresses", ("secondary_ipv4_addresses", Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses))])
                            self._leafs = OrderedDict([
                                ('slave_group_number', (YLeaf(YType.uint32, 'slave-group-number'), ['int'])),
                                ('follow', (YLeaf(YType.str, 'follow'), ['str'])),
                                ('virtual_mac_address', (YLeaf(YType.str, 'virtual-mac-address'), ['str'])),
                                ('primary_ipv4_address', (YLeaf(YType.str, 'primary-ipv4-address'), ['str'])),
                            ])
                            self.slave_group_number = None
                            self.follow = None
                            self.virtual_mac_address = None
                            self.primary_ipv4_address = None

                            self.secondary_ipv4_addresses = Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses()
                            self.secondary_ipv4_addresses.parent = self
                            self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                            self._segment_path = lambda: "slave-group" + "[slave-group-number='" + str(self.slave_group_number) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup, ['slave_group_number', 'follow', 'virtual_mac_address', 'primary_ipv4_address'], name, value)


                        class SecondaryIpv4Addresses(Entity):
                            """
                            Secondary HSRP IP address Table
                            
                            .. attribute:: secondary_ipv4_address
                            
                            	Secondary HSRP IP address
                            	**type**\: list of  		 :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2017-11-05'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses, self).__init__()

                                self.yang_name = "secondary-ipv4-addresses"
                                self.yang_parent_name = "slave-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("secondary-ipv4-address", ("secondary_ipv4_address", Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address))])
                                self._leafs = OrderedDict()

                                self.secondary_ipv4_address = YList(self)
                                self._segment_path = lambda: "secondary-ipv4-addresses"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses, [], name, value)


                            class SecondaryIpv4Address(Entity):
                                """
                                Secondary HSRP IP address
                                
                                .. attribute:: address  (key)
                                
                                	HSRP IP address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                    self.yang_name = "secondary-ipv4-address"
                                    self.yang_parent_name = "secondary-ipv4-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['address']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                    ])
                                    self.address = None
                                    self._segment_path = lambda: "secondary-ipv4-address" + "[address='" + str(self.address) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.SlaveGroups.SlaveGroup.SecondaryIpv4Addresses.SecondaryIpv4Address, ['address'], name, value)


                class Version1(Entity):
                    """
                    Version 1 HSRP configuration
                    
                    .. attribute:: groups
                    
                    	The HSRP group configuration table
                    	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2017-11-05'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv4.Version1, self).__init__()

                        self.yang_name = "version1"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("groups", ("groups", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups))])
                        self._leafs = OrderedDict()

                        self.groups = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups()
                        self.groups.parent = self
                        self._children_name_map["groups"] = "groups"
                        self._segment_path = lambda: "version1"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1, [], name, value)


                    class Groups(Entity):
                        """
                        The HSRP group configuration table
                        
                        .. attribute:: group
                        
                        	The HSRP group being configured
                        	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group>`
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2017-11-05'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups, self).__init__()

                            self.yang_name = "groups"
                            self.yang_parent_name = "version1"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("group", ("group", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group))])
                            self._leafs = OrderedDict()

                            self.group = YList(self)
                            self._segment_path = lambda: "groups"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups, [], name, value)


                        class Group(Entity):
                            """
                            The HSRP group being configured
                            
                            .. attribute:: group_number  (key)
                            
                            	HSRP group number
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: tracked_interfaces
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:  :py:class:`TrackedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces>`
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection
                            	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd>`
                            
                            .. attribute:: tracked_objects
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:  :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects>`
                            
                            .. attribute:: timers
                            
                            	Hello and hold timers
                            	**type**\:  :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers>`
                            
                            .. attribute:: primary_ipv4_address
                            
                            	Primary HSRP IP address
                            	**type**\:  :py:class:`PrimaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address>`
                            
                            .. attribute:: secondary_ipv4_addresses
                            
                            	Secondary HSRP IP address Table
                            	**type**\:  :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses>`
                            
                            .. attribute:: authentication
                            
                            	Authentication string
                            	**type**\: str
                            
                            	**length:** 1..8
                            
                            	**default value**\: cisco
                            
                            .. attribute:: session_name
                            
                            	HSRP Session name (for MGO)
                            	**type**\: str
                            
                            	**length:** 1..16
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**default value**\: 100
                            
                            .. attribute:: preempt
                            
                            	Force active if higher priority
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 0
                            
                            .. attribute:: virtual_mac_address
                            
                            	HSRP MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2017-11-05'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group, self).__init__()

                                self.yang_name = "group"
                                self.yang_parent_name = "groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_number']
                                self._child_classes = OrderedDict([("tracked-interfaces", ("tracked_interfaces", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces)), ("bfd", ("bfd", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd)), ("tracked-objects", ("tracked_objects", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects)), ("timers", ("timers", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers)), ("primary-ipv4-address", ("primary_ipv4_address", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address)), ("secondary-ipv4-addresses", ("secondary_ipv4_addresses", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses))])
                                self._leafs = OrderedDict([
                                    ('group_number', (YLeaf(YType.uint32, 'group-number'), ['int'])),
                                    ('authentication', (YLeaf(YType.str, 'authentication'), ['str'])),
                                    ('session_name', (YLeaf(YType.str, 'session-name'), ['str'])),
                                    ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                    ('preempt', (YLeaf(YType.uint32, 'preempt'), ['int'])),
                                    ('virtual_mac_address', (YLeaf(YType.str, 'virtual-mac-address'), ['str'])),
                                ])
                                self.group_number = None
                                self.authentication = None
                                self.session_name = None
                                self.priority = None
                                self.preempt = None
                                self.virtual_mac_address = None

                                self.tracked_interfaces = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces()
                                self.tracked_interfaces.parent = self
                                self._children_name_map["tracked_interfaces"] = "tracked-interfaces"

                                self.bfd = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd()
                                self.bfd.parent = self
                                self._children_name_map["bfd"] = "bfd"

                                self.tracked_objects = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects()
                                self.tracked_objects.parent = self
                                self._children_name_map["tracked_objects"] = "tracked-objects"

                                self.timers = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers()
                                self.timers.parent = self
                                self._children_name_map["timers"] = "timers"

                                self.primary_ipv4_address = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address()
                                self.primary_ipv4_address.parent = self
                                self._children_name_map["primary_ipv4_address"] = "primary-ipv4-address"

                                self.secondary_ipv4_addresses = Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses()
                                self.secondary_ipv4_addresses.parent = self
                                self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"
                                self._segment_path = lambda: "group" + "[group-number='" + str(self.group_number) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group, ['group_number', 'authentication', 'session_name', 'priority', 'preempt', 'virtual_mac_address'], name, value)


                            class TrackedInterfaces(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_interface
                                
                                	Interface being tracked
                                	**type**\: list of  		 :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces, self).__init__()

                                    self.yang_name = "tracked-interfaces"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("tracked-interface", ("tracked_interface", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface))])
                                    self._leafs = OrderedDict()

                                    self.tracked_interface = YList(self)
                                    self._segment_path = lambda: "tracked-interfaces"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces, [], name, value)


                                class TrackedInterface(Entity):
                                    """
                                    Interface being tracked
                                    
                                    .. attribute:: interface_name  (key)
                                    
                                    	Interface being tracked
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-11-05'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface, self).__init__()

                                        self.yang_name = "tracked-interface"
                                        self.yang_parent_name = "tracked-interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['interface_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                            ('priority_decrement', (YLeaf(YType.uint32, 'priority-decrement'), ['int'])),
                                        ])
                                        self.interface_name = None
                                        self.priority_decrement = None
                                        self._segment_path = lambda: "tracked-interface" + "[interface-name='" + str(self.interface_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedInterfaces.TrackedInterface, ['interface_name', 'priority_decrement'], name, value)


                            class Bfd(Entity):
                                """
                                Enable use of Bidirectional Forwarding
                                Detection
                                
                                .. attribute:: address
                                
                                	Enable BFD for this remote IP
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface name to run BFD
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd, self).__init__()

                                    self.yang_name = "bfd"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ])
                                    self.address = None
                                    self.interface_name = None
                                    self._segment_path = lambda: "bfd"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Bfd, ['address', 'interface_name'], name, value)


                            class TrackedObjects(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_object
                                
                                	Object being tracked
                                	**type**\: list of  		 :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("tracked-object", ("tracked_object", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject))])
                                    self._leafs = OrderedDict()

                                    self.tracked_object = YList(self)
                                    self._segment_path = lambda: "tracked-objects"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects, [], name, value)


                                class TrackedObject(Entity):
                                    """
                                    Object being tracked
                                    
                                    .. attribute:: object_name  (key)
                                    
                                    	Interface being tracked
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-11-05'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject, self).__init__()

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
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.TrackedObjects.TrackedObject, ['object_name', 'priority_decrement'], name, value)


                            class Timers(Entity):
                                """
                                Hello and hold timers
                                
                                .. attribute:: hello_msec_flag
                                
                                	TRUE \- Hello time configured in milliseconds, FALSE \- Hello time configured in seconds
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hello_msec
                                
                                	Hello time in msecs
                                	**type**\: int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hello_sec
                                
                                	Hello time in seconds
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 3
                                
                                .. attribute:: hold_msec_flag
                                
                                	TRUE \- Hold time configured in milliseconds, FALSE \- Hold time configured in seconds
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hold_msec
                                
                                	Hold time in msecs
                                	**type**\: int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hold_sec
                                
                                	Hold time in seconds
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 10
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers, self).__init__()

                                    self.yang_name = "timers"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('hello_msec_flag', (YLeaf(YType.boolean, 'hello-msec-flag'), ['bool'])),
                                        ('hello_msec', (YLeaf(YType.uint32, 'hello-msec'), ['int'])),
                                        ('hello_sec', (YLeaf(YType.uint32, 'hello-sec'), ['int'])),
                                        ('hold_msec_flag', (YLeaf(YType.boolean, 'hold-msec-flag'), ['bool'])),
                                        ('hold_msec', (YLeaf(YType.uint32, 'hold-msec'), ['int'])),
                                        ('hold_sec', (YLeaf(YType.uint32, 'hold-sec'), ['int'])),
                                    ])
                                    self.hello_msec_flag = None
                                    self.hello_msec = None
                                    self.hello_sec = None
                                    self.hold_msec_flag = None
                                    self.hold_msec = None
                                    self.hold_sec = None
                                    self._segment_path = lambda: "timers"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.Timers, ['hello_msec_flag', 'hello_msec', 'hello_sec', 'hold_msec_flag', 'hold_msec', 'hold_sec'], name, value)


                            class PrimaryIpv4Address(Entity):
                                """
                                Primary HSRP IP address
                                
                                .. attribute:: virtual_ip_learn
                                
                                	TRUE if the HSRP protocol is to learn the virtual IP address it is to use
                                	**type**\: bool
                                
                                .. attribute:: address
                                
                                	HSRP IP address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address, self).__init__()

                                    self.yang_name = "primary-ipv4-address"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('virtual_ip_learn', (YLeaf(YType.boolean, 'virtual-ip-learn'), ['bool'])),
                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                    ])
                                    self.virtual_ip_learn = None
                                    self.address = None
                                    self._segment_path = lambda: "primary-ipv4-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.PrimaryIpv4Address, ['virtual_ip_learn', 'address'], name, value)


                            class SecondaryIpv4Addresses(Entity):
                                """
                                Secondary HSRP IP address Table
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	Secondary HSRP IP address
                                	**type**\: list of  		 :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses, self).__init__()

                                    self.yang_name = "secondary-ipv4-addresses"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("secondary-ipv4-address", ("secondary_ipv4_address", Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address))])
                                    self._leafs = OrderedDict()

                                    self.secondary_ipv4_address = YList(self)
                                    self._segment_path = lambda: "secondary-ipv4-addresses"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses, [], name, value)


                                class SecondaryIpv4Address(Entity):
                                    """
                                    Secondary HSRP IP address
                                    
                                    .. attribute:: address  (key)
                                    
                                    	HSRP IP address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-11-05'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                        self.yang_name = "secondary-ipv4-address"
                                        self.yang_parent_name = "secondary-ipv4-addresses"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['address']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ])
                                        self.address = None
                                        self._segment_path = lambda: "secondary-ipv4-address" + "[address='" + str(self.address) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version1.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address, ['address'], name, value)


                class Version2(Entity):
                    """
                    Version 2 HSRP configuration
                    
                    .. attribute:: groups
                    
                    	The HSRP group configuration table
                    	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups>`
                    
                    

                    """

                    _prefix = 'ipv4-hsrp-cfg'
                    _revision = '2017-11-05'

                    def __init__(self):
                        super(Hsrp.Interfaces.Interface.Ipv4.Version2, self).__init__()

                        self.yang_name = "version2"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("groups", ("groups", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups))])
                        self._leafs = OrderedDict()

                        self.groups = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups()
                        self.groups.parent = self
                        self._children_name_map["groups"] = "groups"
                        self._segment_path = lambda: "version2"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2, [], name, value)


                    class Groups(Entity):
                        """
                        The HSRP group configuration table
                        
                        .. attribute:: group
                        
                        	The HSRP group being configured
                        	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group>`
                        
                        

                        """

                        _prefix = 'ipv4-hsrp-cfg'
                        _revision = '2017-11-05'

                        def __init__(self):
                            super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups, self).__init__()

                            self.yang_name = "groups"
                            self.yang_parent_name = "version2"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("group", ("group", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group))])
                            self._leafs = OrderedDict()

                            self.group = YList(self)
                            self._segment_path = lambda: "groups"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups, [], name, value)


                        class Group(Entity):
                            """
                            The HSRP group being configured
                            
                            .. attribute:: group_number  (key)
                            
                            	HSRP group number
                            	**type**\: int
                            
                            	**range:** 0..4095
                            
                            .. attribute:: secondary_ipv4_addresses
                            
                            	Secondary HSRP IP address Table
                            	**type**\:  :py:class:`SecondaryIpv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses>`
                            
                            .. attribute:: bfd
                            
                            	Enable use of Bidirectional Forwarding Detection
                            	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd>`
                            
                            .. attribute:: primary_ipv4_address
                            
                            	Primary HSRP IP address
                            	**type**\:  :py:class:`PrimaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address>`
                            
                            .. attribute:: tracked_objects
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:  :py:class:`TrackedObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects>`
                            
                            .. attribute:: tracked_interfaces
                            
                            	The HSRP tracked interface configuration table
                            	**type**\:  :py:class:`TrackedInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces>`
                            
                            .. attribute:: timers
                            
                            	Hello and hold timers
                            	**type**\:  :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers>`
                            
                            .. attribute:: preempt
                            
                            	Force active if higher priority
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 0
                            
                            .. attribute:: priority
                            
                            	Priority value
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**default value**\: 100
                            
                            .. attribute:: virtual_mac_address
                            
                            	HSRP MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: session_name
                            
                            	HSRP Session name (for MGO)
                            	**type**\: str
                            
                            	**length:** 1..16
                            
                            

                            """

                            _prefix = 'ipv4-hsrp-cfg'
                            _revision = '2017-11-05'

                            def __init__(self):
                                super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group, self).__init__()

                                self.yang_name = "group"
                                self.yang_parent_name = "groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['group_number']
                                self._child_classes = OrderedDict([("secondary-ipv4-addresses", ("secondary_ipv4_addresses", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses)), ("bfd", ("bfd", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd)), ("primary-ipv4-address", ("primary_ipv4_address", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address)), ("tracked-objects", ("tracked_objects", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects)), ("tracked-interfaces", ("tracked_interfaces", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces)), ("timers", ("timers", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers))])
                                self._leafs = OrderedDict([
                                    ('group_number', (YLeaf(YType.uint32, 'group-number'), ['int'])),
                                    ('preempt', (YLeaf(YType.uint32, 'preempt'), ['int'])),
                                    ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                    ('virtual_mac_address', (YLeaf(YType.str, 'virtual-mac-address'), ['str'])),
                                    ('session_name', (YLeaf(YType.str, 'session-name'), ['str'])),
                                ])
                                self.group_number = None
                                self.preempt = None
                                self.priority = None
                                self.virtual_mac_address = None
                                self.session_name = None

                                self.secondary_ipv4_addresses = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses()
                                self.secondary_ipv4_addresses.parent = self
                                self._children_name_map["secondary_ipv4_addresses"] = "secondary-ipv4-addresses"

                                self.bfd = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd()
                                self.bfd.parent = self
                                self._children_name_map["bfd"] = "bfd"

                                self.primary_ipv4_address = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address()
                                self.primary_ipv4_address.parent = self
                                self._children_name_map["primary_ipv4_address"] = "primary-ipv4-address"

                                self.tracked_objects = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects()
                                self.tracked_objects.parent = self
                                self._children_name_map["tracked_objects"] = "tracked-objects"

                                self.tracked_interfaces = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces()
                                self.tracked_interfaces.parent = self
                                self._children_name_map["tracked_interfaces"] = "tracked-interfaces"

                                self.timers = Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers()
                                self.timers.parent = self
                                self._children_name_map["timers"] = "timers"
                                self._segment_path = lambda: "group" + "[group-number='" + str(self.group_number) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group, ['group_number', 'preempt', 'priority', 'virtual_mac_address', 'session_name'], name, value)


                            class SecondaryIpv4Addresses(Entity):
                                """
                                Secondary HSRP IP address Table
                                
                                .. attribute:: secondary_ipv4_address
                                
                                	Secondary HSRP IP address
                                	**type**\: list of  		 :py:class:`SecondaryIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses, self).__init__()

                                    self.yang_name = "secondary-ipv4-addresses"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("secondary-ipv4-address", ("secondary_ipv4_address", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address))])
                                    self._leafs = OrderedDict()

                                    self.secondary_ipv4_address = YList(self)
                                    self._segment_path = lambda: "secondary-ipv4-addresses"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses, [], name, value)


                                class SecondaryIpv4Address(Entity):
                                    """
                                    Secondary HSRP IP address
                                    
                                    .. attribute:: address  (key)
                                    
                                    	HSRP IP address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-11-05'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address, self).__init__()

                                        self.yang_name = "secondary-ipv4-address"
                                        self.yang_parent_name = "secondary-ipv4-addresses"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['address']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ])
                                        self.address = None
                                        self._segment_path = lambda: "secondary-ipv4-address" + "[address='" + str(self.address) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.SecondaryIpv4Addresses.SecondaryIpv4Address, ['address'], name, value)


                            class Bfd(Entity):
                                """
                                Enable use of Bidirectional Forwarding
                                Detection
                                
                                .. attribute:: address
                                
                                	Enable BFD for this remote IP
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface name to run BFD
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd, self).__init__()

                                    self.yang_name = "bfd"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ])
                                    self.address = None
                                    self.interface_name = None
                                    self._segment_path = lambda: "bfd"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Bfd, ['address', 'interface_name'], name, value)


                            class PrimaryIpv4Address(Entity):
                                """
                                Primary HSRP IP address
                                
                                .. attribute:: virtual_ip_learn
                                
                                	TRUE if the HSRP protocol is to learn the virtual IP address it is to use
                                	**type**\: bool
                                
                                .. attribute:: address
                                
                                	HSRP IP address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address, self).__init__()

                                    self.yang_name = "primary-ipv4-address"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('virtual_ip_learn', (YLeaf(YType.boolean, 'virtual-ip-learn'), ['bool'])),
                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                    ])
                                    self.virtual_ip_learn = None
                                    self.address = None
                                    self._segment_path = lambda: "primary-ipv4-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.PrimaryIpv4Address, ['virtual_ip_learn', 'address'], name, value)


                            class TrackedObjects(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_object
                                
                                	Object being tracked
                                	**type**\: list of  		 :py:class:`TrackedObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects, self).__init__()

                                    self.yang_name = "tracked-objects"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("tracked-object", ("tracked_object", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject))])
                                    self._leafs = OrderedDict()

                                    self.tracked_object = YList(self)
                                    self._segment_path = lambda: "tracked-objects"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects, [], name, value)


                                class TrackedObject(Entity):
                                    """
                                    Object being tracked
                                    
                                    .. attribute:: object_name  (key)
                                    
                                    	Interface being tracked
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-11-05'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject, self).__init__()

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
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedObjects.TrackedObject, ['object_name', 'priority_decrement'], name, value)


                            class TrackedInterfaces(Entity):
                                """
                                The HSRP tracked interface configuration
                                table
                                
                                .. attribute:: tracked_interface
                                
                                	Interface being tracked
                                	**type**\: list of  		 :py:class:`TrackedInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_cfg.Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface>`
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces, self).__init__()

                                    self.yang_name = "tracked-interfaces"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("tracked-interface", ("tracked_interface", Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface))])
                                    self._leafs = OrderedDict()

                                    self.tracked_interface = YList(self)
                                    self._segment_path = lambda: "tracked-interfaces"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces, [], name, value)


                                class TrackedInterface(Entity):
                                    """
                                    Interface being tracked
                                    
                                    .. attribute:: interface_name  (key)
                                    
                                    	Interface being tracked
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Priority decrement
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-hsrp-cfg'
                                    _revision = '2017-11-05'

                                    def __init__(self):
                                        super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface, self).__init__()

                                        self.yang_name = "tracked-interface"
                                        self.yang_parent_name = "tracked-interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['interface_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                            ('priority_decrement', (YLeaf(YType.uint32, 'priority-decrement'), ['int'])),
                                        ])
                                        self.interface_name = None
                                        self.priority_decrement = None
                                        self._segment_path = lambda: "tracked-interface" + "[interface-name='" + str(self.interface_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.TrackedInterfaces.TrackedInterface, ['interface_name', 'priority_decrement'], name, value)


                            class Timers(Entity):
                                """
                                Hello and hold timers
                                
                                .. attribute:: hello_msec_flag
                                
                                	TRUE \- Hello time configured in milliseconds, FALSE \- Hello time configured in seconds
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hello_msec
                                
                                	Hello time in msecs
                                	**type**\: int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hello_sec
                                
                                	Hello time in seconds
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 3
                                
                                .. attribute:: hold_msec_flag
                                
                                	TRUE \- Hold time configured in milliseconds, FALSE \- Hold time configured in seconds
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                .. attribute:: hold_msec
                                
                                	Hold time in msecs
                                	**type**\: int
                                
                                	**range:** 100..3000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: hold_sec
                                
                                	Hold time in seconds
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                	**units**\: second
                                
                                	**default value**\: 10
                                
                                

                                """

                                _prefix = 'ipv4-hsrp-cfg'
                                _revision = '2017-11-05'

                                def __init__(self):
                                    super(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers, self).__init__()

                                    self.yang_name = "timers"
                                    self.yang_parent_name = "group"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('hello_msec_flag', (YLeaf(YType.boolean, 'hello-msec-flag'), ['bool'])),
                                        ('hello_msec', (YLeaf(YType.uint32, 'hello-msec'), ['int'])),
                                        ('hello_sec', (YLeaf(YType.uint32, 'hello-sec'), ['int'])),
                                        ('hold_msec_flag', (YLeaf(YType.boolean, 'hold-msec-flag'), ['bool'])),
                                        ('hold_msec', (YLeaf(YType.uint32, 'hold-msec'), ['int'])),
                                        ('hold_sec', (YLeaf(YType.uint32, 'hold-sec'), ['int'])),
                                    ])
                                    self.hello_msec_flag = None
                                    self.hello_msec = None
                                    self.hello_sec = None
                                    self.hold_msec_flag = None
                                    self.hold_msec = None
                                    self.hold_sec = None
                                    self._segment_path = lambda: "timers"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Hsrp.Interfaces.Interface.Ipv4.Version2.Groups.Group.Timers, ['hello_msec_flag', 'hello_msec', 'hello_sec', 'hold_msec_flag', 'hold_msec', 'hold_sec'], name, value)


    class Logging(Entity):
        """
        HSRP logging options
        
        .. attribute:: state_change_disable
        
        	HSRP state change IOS messages disable
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ipv4-hsrp-cfg'
        _revision = '2017-11-05'

        def __init__(self):
            super(Hsrp.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "hsrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('state_change_disable', (YLeaf(YType.empty, 'state-change-disable'), ['Empty'])),
            ])
            self.state_change_disable = None
            self._segment_path = lambda: "logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-hsrp-cfg:hsrp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Hsrp.Logging, ['state_change_disable'], name, value)

    def clone_ptr(self):
        self._top_entity = Hsrp()
        return self._top_entity

