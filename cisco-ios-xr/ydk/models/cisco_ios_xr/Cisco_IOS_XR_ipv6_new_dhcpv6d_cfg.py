""" Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-new\-dhcpv6d package configuration.

This module contains definitions
for the following management objects\:
  dhcpv6\: None

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Insert(Enum):
    """
    Insert

    Insert

    .. data:: local = 0

    	Insert locally generated/configured Interface

    	ID value

    .. data:: received = 1

    	Insert received Interface ID value

    .. data:: pppoe = 2

    	Insert received Interface ID value from SADB

    """

    local = Enum.YLeaf(0, "local")

    received = Enum.YLeaf(1, "received")

    pppoe = Enum.YLeaf(2, "pppoe")


class LinkLayerAddr(Enum):
    """
    LinkLayerAddr

    Link layer addr

    .. data:: set = 4

    	Insert Received LinkLayerAddr Value from SADB

    """

    set = Enum.YLeaf(4, "set")


class SubscriberId(Enum):
    """
    SubscriberId

    Subscriber id

    .. data:: pppoe = 3

    	Insert Received Subscriber-ID Value from SADB

    """

    pppoe = Enum.YLeaf(3, "pppoe")



class Dhcpv6(Entity):
    """
    None
    
    .. attribute:: allow_duid_change
    
    	For BNG session, allow duid change for a client MAC
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: database
    
    	Enable DHCP binding database storage to file system
    	**type**\:   :py:class:`Database <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Database>`
    
    .. attribute:: enable
    
    	Enable None. Deletion of this object also causes deletion of all associated objects under DHCPv6
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    	**mandatory**\: True
    
    .. attribute:: interfaces
    
    	Table of Interface
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces>`
    
    .. attribute:: profiles
    
    	Table of Profile
    	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles>`
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv6-new-dhcpv6d-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Dhcpv6, self).__init__()
        self._top_entity = None

        self.yang_name = "dhcpv6"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"database" : ("database", Dhcpv6.Database), "interfaces" : ("interfaces", Dhcpv6.Interfaces), "profiles" : ("profiles", Dhcpv6.Profiles)}
        self._child_list_classes = {}
        self.is_presence_container = True

        self.allow_duid_change = YLeaf(YType.empty, "allow-duid-change")

        self.enable = YLeaf(YType.empty, "enable")

        self.database = Dhcpv6.Database()
        self.database.parent = self
        self._children_name_map["database"] = "database"
        self._children_yang_names.add("database")

        self.interfaces = Dhcpv6.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.profiles = Dhcpv6.Profiles()
        self.profiles.parent = self
        self._children_name_map["profiles"] = "profiles"
        self._children_yang_names.add("profiles")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6"

    def __setattr__(self, name, value):
        self._perform_setattr(Dhcpv6, ['allow_duid_change', 'enable'], name, value)


    class Database(Entity):
        """
        Enable DHCP binding database storage to file
        system
        
        .. attribute:: full_write_interval
        
        	Full file write interval (default 10 minutes)
        	**type**\:  int
        
        	**range:** 1..1440
        
        	**default value**\: 10
        
        .. attribute:: incremental_write_interval
        
        	Incremental file write interval (default 1 minutes)
        	**type**\:  int
        
        	**range:** 1..1440
        
        	**default value**\: 1
        
        .. attribute:: proxy
        
        	Enable DHCP proxy binding database storage to file system
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: relay
        
        	Enable DHCP relay binding database storage to file system
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: server
        
        	Enable DHCP server binding database storage to file system
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Dhcpv6.Database, self).__init__()

            self.yang_name = "database"
            self.yang_parent_name = "dhcpv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.full_write_interval = YLeaf(YType.uint32, "full-write-interval")

            self.incremental_write_interval = YLeaf(YType.uint32, "incremental-write-interval")

            self.proxy = YLeaf(YType.empty, "proxy")

            self.relay = YLeaf(YType.empty, "relay")

            self.server = YLeaf(YType.empty, "server")
            self._segment_path = lambda: "database"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Dhcpv6.Database, ['full_write_interval', 'incremental_write_interval', 'proxy', 'relay', 'server'], name, value)


    class Interfaces(Entity):
        """
        Table of Interface
        
        .. attribute:: interface
        
        	None
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Dhcpv6.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "dhcpv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", Dhcpv6.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Dhcpv6.Interfaces, [], name, value)


        class Interface(Entity):
            """
            None
            
            .. attribute:: interface_name  <key>
            
            	Interface to configure
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: base
            
            	Assign a base profile to interface
            	**type**\:   :py:class:`Base <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Base>`
            
            .. attribute:: pppoe
            
            	PPPoE subscriber interface
            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Pppoe>`
            
            .. attribute:: proxy
            
            	Assign a proxy profile to interface
            	**type**\:   :py:class:`Proxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Proxy>`
            
            .. attribute:: relay
            
            	Assign a relay profile to interface
            	**type**\:   :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Relay>`
            
            .. attribute:: server
            
            	Assign a server profile to interface
            	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Server>`
            
            

            """

            _prefix = 'ipv6-new-dhcpv6d-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Dhcpv6.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"base" : ("base", Dhcpv6.Interfaces.Interface.Base), "pppoe" : ("pppoe", Dhcpv6.Interfaces.Interface.Pppoe), "proxy" : ("proxy", Dhcpv6.Interfaces.Interface.Proxy), "relay" : ("relay", Dhcpv6.Interfaces.Interface.Relay), "server" : ("server", Dhcpv6.Interfaces.Interface.Server)}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.base = Dhcpv6.Interfaces.Interface.Base()
                self.base.parent = self
                self._children_name_map["base"] = "base"
                self._children_yang_names.add("base")

                self.pppoe = Dhcpv6.Interfaces.Interface.Pppoe()
                self.pppoe.parent = self
                self._children_name_map["pppoe"] = "pppoe"
                self._children_yang_names.add("pppoe")

                self.proxy = Dhcpv6.Interfaces.Interface.Proxy()
                self.proxy.parent = self
                self._children_name_map["proxy"] = "proxy"
                self._children_yang_names.add("proxy")

                self.relay = Dhcpv6.Interfaces.Interface.Relay()
                self.relay.parent = self
                self._children_name_map["relay"] = "relay"
                self._children_yang_names.add("relay")

                self.server = Dhcpv6.Interfaces.Interface.Server()
                self.server.parent = self
                self._children_name_map["server"] = "server"
                self._children_yang_names.add("server")
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Dhcpv6.Interfaces.Interface, ['interface_name'], name, value)


            class Base(Entity):
                """
                Assign a base profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Dhcpv6.Interfaces.Interface.Base, self).__init__()

                    self.yang_name = "base"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.profile = YLeaf(YType.str, "profile")
                    self._segment_path = lambda: "base"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Base, ['profile'], name, value)


            class Pppoe(Entity):
                """
                PPPoE subscriber interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Dhcpv6.Interfaces.Interface.Pppoe, self).__init__()

                    self.yang_name = "pppoe"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.profile = YLeaf(YType.str, "profile")
                    self._segment_path = lambda: "pppoe"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Pppoe, ['profile'], name, value)


            class Proxy(Entity):
                """
                Assign a proxy profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Dhcpv6.Interfaces.Interface.Proxy, self).__init__()

                    self.yang_name = "proxy"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.profile = YLeaf(YType.str, "profile")
                    self._segment_path = lambda: "proxy"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Proxy, ['profile'], name, value)


            class Relay(Entity):
                """
                Assign a relay profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Dhcpv6.Interfaces.Interface.Relay, self).__init__()

                    self.yang_name = "relay"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.profile = YLeaf(YType.str, "profile")
                    self._segment_path = lambda: "relay"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Relay, ['profile'], name, value)


            class Server(Entity):
                """
                Assign a server profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Dhcpv6.Interfaces.Interface.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.profile = YLeaf(YType.str, "profile")
                    self._segment_path = lambda: "server"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Server, ['profile'], name, value)


    class Profiles(Entity):
        """
        Table of Profile
        
        .. attribute:: profile
        
        	None
        	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Dhcpv6.Profiles, self).__init__()

            self.yang_name = "profiles"
            self.yang_parent_name = "dhcpv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"profile" : ("profile", Dhcpv6.Profiles.Profile)}

            self.profile = YList(self)
            self._segment_path = lambda: "profiles"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Dhcpv6.Profiles, [], name, value)


        class Profile(Entity):
            """
            None
            
            .. attribute:: profile_name  <key>
            
            	Profile name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: base
            
            	None
            	**type**\:   :py:class:`Base <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base>`
            
            	**presence node**\: True
            
            .. attribute:: proxy
            
            	None
            	**type**\:   :py:class:`Proxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy>`
            
            	**presence node**\: True
            
            .. attribute:: relay
            
            	None
            	**type**\:   :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay>`
            
            	**presence node**\: True
            
            .. attribute:: server
            
            	None
            	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ipv6-new-dhcpv6d-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Dhcpv6.Profiles.Profile, self).__init__()

                self.yang_name = "profile"
                self.yang_parent_name = "profiles"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"base" : ("base", Dhcpv6.Profiles.Profile.Base), "proxy" : ("proxy", Dhcpv6.Profiles.Profile.Proxy), "relay" : ("relay", Dhcpv6.Profiles.Profile.Relay), "server" : ("server", Dhcpv6.Profiles.Profile.Server)}
                self._child_list_classes = {}

                self.profile_name = YLeaf(YType.str, "profile-name")

                self.base = None
                self._children_name_map["base"] = "base"
                self._children_yang_names.add("base")

                self.proxy = None
                self._children_name_map["proxy"] = "proxy"
                self._children_yang_names.add("proxy")

                self.relay = None
                self._children_name_map["relay"] = "relay"
                self._children_yang_names.add("relay")

                self.server = None
                self._children_name_map["server"] = "server"
                self._children_yang_names.add("server")
                self._segment_path = lambda: "profile" + "[profile-name='" + self.profile_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/profiles/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Dhcpv6.Profiles.Profile, ['profile_name'], name, value)


            class Base(Entity):
                """
                None
                
                .. attribute:: default
                
                	Default match option
                	**type**\:   :py:class:`Default <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Default>`
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Base
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: match
                
                	Enter match option
                	**type**\:   :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Dhcpv6.Profiles.Profile.Base, self).__init__()

                    self.yang_name = "base"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"default" : ("default", Dhcpv6.Profiles.Profile.Base.Default), "match" : ("match", Dhcpv6.Profiles.Profile.Base.Match)}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.enable = YLeaf(YType.empty, "enable")

                    self.default = Dhcpv6.Profiles.Profile.Base.Default()
                    self.default.parent = self
                    self._children_name_map["default"] = "default"
                    self._children_yang_names.add("default")

                    self.match = Dhcpv6.Profiles.Profile.Base.Match()
                    self.match.parent = self
                    self._children_name_map["match"] = "match"
                    self._children_yang_names.add("match")
                    self._segment_path = lambda: "base"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Profiles.Profile.Base, ['enable'], name, value)


                class Default(Entity):
                    """
                    Default match option
                    
                    .. attribute:: profile
                    
                    	Enter proxy or server profile
                    	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Default.Profile>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Base.Default, self).__init__()

                        self.yang_name = "default"
                        self.yang_parent_name = "base"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"profile" : ("profile", Dhcpv6.Profiles.Profile.Base.Default.Profile)}

                        self.profile = YList(self)
                        self._segment_path = lambda: "default"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Default, [], name, value)


                    class Profile(Entity):
                        """
                        Enter proxy or server profile
                        
                        .. attribute:: profile_name  <key>
                        
                        	Profile name
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: proxy_mode
                        
                        	Specify mode\-class based Proxy Option
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: server_mode
                        
                        	Specify mode\-class based Server option
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Base.Default.Profile, self).__init__()

                            self.yang_name = "profile"
                            self.yang_parent_name = "default"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.profile_name = YLeaf(YType.str, "profile-name")

                            self.proxy_mode = YLeaf(YType.empty, "proxy-mode")

                            self.server_mode = YLeaf(YType.empty, "server-mode")
                            self._segment_path = lambda: "profile" + "[profile-name='" + self.profile_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Default.Profile, ['profile_name', 'proxy_mode', 'server_mode'], name, value)


                class Match(Entity):
                    """
                    Enter match option
                    
                    .. attribute:: mode_classes
                    
                    	Table of ModeClass
                    	**type**\:   :py:class:`ModeClasses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match.ModeClasses>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Base.Match, self).__init__()

                        self.yang_name = "match"
                        self.yang_parent_name = "base"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"mode-classes" : ("mode_classes", Dhcpv6.Profiles.Profile.Base.Match.ModeClasses)}
                        self._child_list_classes = {}

                        self.mode_classes = Dhcpv6.Profiles.Profile.Base.Match.ModeClasses()
                        self.mode_classes.parent = self
                        self._children_name_map["mode_classes"] = "mode-classes"
                        self._children_yang_names.add("mode-classes")
                        self._segment_path = lambda: "match"


                    class ModeClasses(Entity):
                        """
                        Table of ModeClass
                        
                        .. attribute:: mode_class
                        
                        	Specify PPP/IPoE class option
                        	**type**\: list of    :py:class:`ModeClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses, self).__init__()

                            self.yang_name = "mode-classes"
                            self.yang_parent_name = "match"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"mode-class" : ("mode_class", Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass)}

                            self.mode_class = YList(self)
                            self._segment_path = lambda: "mode-classes"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses, [], name, value)


                        class ModeClass(Entity):
                            """
                            Specify PPP/IPoE class option
                            
                            .. attribute:: class_name  <key>
                            
                            	Class name
                            	**type**\:  str
                            
                            	**length:** 1..128
                            
                            .. attribute:: profile
                            
                            	Enter proxy or server profile
                            	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass, self).__init__()

                                self.yang_name = "mode-class"
                                self.yang_parent_name = "mode-classes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"profile" : ("profile", Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile)}

                                self.class_name = YLeaf(YType.str, "class-name")

                                self.profile = YList(self)
                                self._segment_path = lambda: "mode-class" + "[class-name='" + self.class_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass, ['class_name'], name, value)


                            class Profile(Entity):
                                """
                                Enter proxy or server profile
                                
                                .. attribute:: profile_name  <key>
                                
                                	Profile name
                                	**type**\:  str
                                
                                	**length:** 1..64
                                
                                .. attribute:: proxy_mode
                                
                                	Specify mode\-class based Proxy Option
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: server_mode
                                
                                	Specify mode\-class based Server option
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile, self).__init__()

                                    self.yang_name = "profile"
                                    self.yang_parent_name = "mode-class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.profile_name = YLeaf(YType.str, "profile-name")

                                    self.proxy_mode = YLeaf(YType.empty, "proxy-mode")

                                    self.server_mode = YLeaf(YType.empty, "server-mode")
                                    self._segment_path = lambda: "profile" + "[profile-name='" + self.profile_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile, ['profile_name', 'proxy_mode', 'server_mode'], name, value)


            class Proxy(Entity):
                """
                None
                
                .. attribute:: authentication
                
                	Authentication username format
                	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Authentication>`
                
                .. attribute:: classes
                
                	Table of Class
                	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes>`
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Proxy
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: interfaces
                
                	Table of Interface
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Interfaces>`
                
                .. attribute:: link_address
                
                	IPv6 address to be filled in link\-address
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: linkaddress_from_ra_enable
                
                	Fill linkaddress in Relay fwd msg with Prefix from Router Advertisement for PPPoE sessions
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: relay
                
                	Specify relay configuration
                	**type**\:   :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Relay>`
                
                .. attribute:: route_add_disable
                
                	RouteDisable
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: sessions
                
                	Change sessions configuration
                	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Sessions>`
                
                .. attribute:: src_intf_name
                
                	Create or enter proxy profile Source Interface Name
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: vrfs
                
                	VRF related configuration
                	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Dhcpv6.Profiles.Profile.Proxy, self).__init__()

                    self.yang_name = "proxy"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"authentication" : ("authentication", Dhcpv6.Profiles.Profile.Proxy.Authentication), "classes" : ("classes", Dhcpv6.Profiles.Profile.Proxy.Classes), "interfaces" : ("interfaces", Dhcpv6.Profiles.Profile.Proxy.Interfaces), "relay" : ("relay", Dhcpv6.Profiles.Profile.Proxy.Relay), "sessions" : ("sessions", Dhcpv6.Profiles.Profile.Proxy.Sessions), "vrfs" : ("vrfs", Dhcpv6.Profiles.Profile.Proxy.Vrfs)}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.enable = YLeaf(YType.empty, "enable")

                    self.link_address = YLeaf(YType.str, "link-address")

                    self.linkaddress_from_ra_enable = YLeaf(YType.empty, "linkaddress-from-ra-enable")

                    self.route_add_disable = YLeaf(YType.empty, "route-add-disable")

                    self.src_intf_name = YLeaf(YType.str, "src-intf-name")

                    self.authentication = Dhcpv6.Profiles.Profile.Proxy.Authentication()
                    self.authentication.parent = self
                    self._children_name_map["authentication"] = "authentication"
                    self._children_yang_names.add("authentication")

                    self.classes = Dhcpv6.Profiles.Profile.Proxy.Classes()
                    self.classes.parent = self
                    self._children_name_map["classes"] = "classes"
                    self._children_yang_names.add("classes")

                    self.interfaces = Dhcpv6.Profiles.Profile.Proxy.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")

                    self.relay = Dhcpv6.Profiles.Profile.Proxy.Relay()
                    self.relay.parent = self
                    self._children_name_map["relay"] = "relay"
                    self._children_yang_names.add("relay")

                    self.sessions = Dhcpv6.Profiles.Profile.Proxy.Sessions()
                    self.sessions.parent = self
                    self._children_name_map["sessions"] = "sessions"
                    self._children_yang_names.add("sessions")

                    self.vrfs = Dhcpv6.Profiles.Profile.Proxy.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                    self._children_yang_names.add("vrfs")
                    self._segment_path = lambda: "proxy"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy, ['enable', 'link_address', 'linkaddress_from_ra_enable', 'route_add_disable', 'src_intf_name'], name, value)


                class Authentication(Entity):
                    """
                    Authentication username format
                    
                    .. attribute:: username
                    
                    	Set username as DUID
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Authentication, self).__init__()

                        self.yang_name = "authentication"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.username = YLeaf(YType.empty, "username")
                        self._segment_path = lambda: "authentication"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Authentication, ['username'], name, value)


                class Classes(Entity):
                    """
                    Table of Class
                    
                    .. attribute:: class_
                    
                    	None
                    	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes.Class_>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Classes, self).__init__()

                        self.yang_name = "classes"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"class" : ("class_", Dhcpv6.Profiles.Profile.Proxy.Classes.Class_)}

                        self.class_ = YList(self)
                        self._segment_path = lambda: "classes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Classes, [], name, value)


                    class Class_(Entity):
                        """
                        None
                        
                        .. attribute:: class_name  <key>
                        
                        	Class name
                        	**type**\:  str
                        
                        	**length:** 1..128
                        
                        .. attribute:: helper_addresses
                        
                        	Table of HelperAddress
                        	**type**\:   :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses>`
                        
                        .. attribute:: link_address
                        
                        	IPv6 address to be filled in link\-address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_, self).__init__()

                            self.yang_name = "class"
                            self.yang_parent_name = "classes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"helper-addresses" : ("helper_addresses", Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses)}
                            self._child_list_classes = {}

                            self.class_name = YLeaf(YType.str, "class-name")

                            self.link_address = YLeaf(YType.str, "link-address")

                            self.helper_addresses = Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses()
                            self.helper_addresses.parent = self
                            self._children_name_map["helper_addresses"] = "helper-addresses"
                            self._children_yang_names.add("helper-addresses")
                            self._segment_path = lambda: "class" + "[class-name='" + self.class_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_, ['class_name', 'link_address'], name, value)


                        class HelperAddresses(Entity):
                            """
                            Table of HelperAddress
                            
                            .. attribute:: helper_address
                            
                            	Specify the server helper address
                            	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses.HelperAddress>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses, self).__init__()

                                self.yang_name = "helper-addresses"
                                self.yang_parent_name = "class"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"helper-address" : ("helper_address", Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses.HelperAddress)}

                                self.helper_address = YList(self)
                                self._segment_path = lambda: "helper-addresses"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses, [], name, value)


                            class HelperAddress(Entity):
                                """
                                Specify the server helper address
                                
                                .. attribute:: vrf_name  <key>
                                
                                	VRF name
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: helper_address  <key>
                                
                                	Server address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses.HelperAddress, self).__init__()

                                    self.yang_name = "helper-address"
                                    self.yang_parent_name = "helper-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                                    self.helper_address = YLeaf(YType.str, "helper-address")
                                    self._segment_path = lambda: "helper-address" + "[vrf-name='" + self.vrf_name.get() + "']" + "[helper-address='" + self.helper_address.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses.HelperAddress, ['vrf_name', 'helper_address'], name, value)


                class Interfaces(Entity):
                    """
                    Table of Interface
                    
                    .. attribute:: interface
                    
                    	None
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"interface" : ("interface", Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface)}

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        None
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface to configure
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: interface_id
                        
                        	Physical interface ID
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.interface_id = YLeaf(YType.str, "interface-id")
                            self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface, ['interface_name', 'interface_id'], name, value)


                class Relay(Entity):
                    """
                    Specify relay configuration
                    
                    .. attribute:: option
                    
                    	Specify relay option configuration
                    	**type**\:   :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Relay.Option>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Relay, self).__init__()

                        self.yang_name = "relay"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"option" : ("option", Dhcpv6.Profiles.Profile.Proxy.Relay.Option)}
                        self._child_list_classes = {}

                        self.option = Dhcpv6.Profiles.Profile.Proxy.Relay.Option()
                        self.option.parent = self
                        self._children_name_map["option"] = "option"
                        self._children_yang_names.add("option")
                        self._segment_path = lambda: "relay"


                    class Option(Entity):
                        """
                        Specify relay option configuration
                        
                        .. attribute:: interface_id
                        
                        	Interface Id option
                        	**type**\:   :py:class:`InterfaceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId>`
                        
                        .. attribute:: link_layer_addr
                        
                        	Configure Received link\-layer\-Addr
                        	**type**\:   :py:class:`LinkLayerAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.LinkLayerAddr>`
                        
                        .. attribute:: remote_i_dreceived
                        
                        	Set remote\-id value from SADB
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: remote_id
                        
                        	Enter remote\-id value
                        	**type**\:  str
                        
                        	**length:** 1..256
                        
                        .. attribute:: subscriber_id
                        
                        	Configure Received SubscriberID
                        	**type**\:   :py:class:`SubscriberId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.SubscriberId>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Relay.Option, self).__init__()

                            self.yang_name = "option"
                            self.yang_parent_name = "relay"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"interface-id" : ("interface_id", Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId)}
                            self._child_list_classes = {}

                            self.link_layer_addr = YLeaf(YType.enumeration, "link-layer-addr")

                            self.remote_i_dreceived = YLeaf(YType.int32, "remote-i-dreceived")

                            self.remote_id = YLeaf(YType.str, "remote-id")

                            self.subscriber_id = YLeaf(YType.enumeration, "subscriber-id")

                            self.interface_id = Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId()
                            self.interface_id.parent = self
                            self._children_name_map["interface_id"] = "interface-id"
                            self._children_yang_names.add("interface-id")
                            self._segment_path = lambda: "option"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Relay.Option, ['link_layer_addr', 'remote_i_dreceived', 'remote_id', 'subscriber_id'], name, value)


                        class InterfaceId(Entity):
                            """
                            Interface Id option
                            
                            .. attribute:: insert
                            
                            	Configure InterfaceID insert type
                            	**type**\:   :py:class:`Insert <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Insert>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId, self).__init__()

                                self.yang_name = "interface-id"
                                self.yang_parent_name = "option"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.insert = YLeaf(YType.enumeration, "insert")
                                self._segment_path = lambda: "interface-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId, ['insert'], name, value)


                class Sessions(Entity):
                    """
                    Change sessions configuration
                    
                    .. attribute:: mac
                    
                    	Throttle DHCP sessions based on MAC address
                    	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Sessions, self).__init__()

                        self.yang_name = "sessions"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"mac" : ("mac", Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac)}
                        self._child_list_classes = {}

                        self.mac = Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac()
                        self.mac.parent = self
                        self._children_name_map["mac"] = "mac"
                        self._children_yang_names.add("mac")
                        self._segment_path = lambda: "sessions"


                    class Mac(Entity):
                        """
                        Throttle DHCP sessions based on MAC address
                        
                        .. attribute:: throttle
                        
                        	Throttle DHCP sessions from any one MAC address
                        	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac, self).__init__()

                            self.yang_name = "mac"
                            self.yang_parent_name = "sessions"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"throttle" : ("throttle", Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle)}
                            self._child_list_classes = {}

                            self.throttle = Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle()
                            self.throttle.parent = self
                            self._children_name_map["throttle"] = "throttle"
                            self._children_yang_names.add("throttle")
                            self._segment_path = lambda: "mac"


                        class Throttle(Entity):
                            """
                            Throttle DHCP sessions from any one MAC
                            address
                            
                            .. attribute:: block
                            
                            	Throttle blocking period (in secs)
                            	**type**\:  int
                            
                            	**range:** 1..100
                            
                            	**units**\: second
                            
                            .. attribute:: limit
                            
                            	Number of solicits at which to throttle
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: request
                            
                            	Throttle request period (in secs)
                            	**type**\:  int
                            
                            	**range:** 1..100
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle, self).__init__()

                                self.yang_name = "throttle"
                                self.yang_parent_name = "mac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.block = YLeaf(YType.uint32, "block")

                                self.limit = YLeaf(YType.uint32, "limit")

                                self.request = YLeaf(YType.uint32, "request")
                                self._segment_path = lambda: "throttle"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle, ['block', 'limit', 'request'], name, value)


                class Vrfs(Entity):
                    """
                    VRF related configuration
                    
                    .. attribute:: vrf
                    
                    	IPv6 DHCP proxy VRF name
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"vrf" : ("vrf", Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf)}

                        self.vrf = YList(self)
                        self._segment_path = lambda: "vrfs"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Vrfs, [], name, value)


                    class Vrf(Entity):
                        """
                        IPv6 DHCP proxy VRF name
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: helper_addresses
                        
                        	Table of HelperAddress
                        	**type**\:   :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"helper-addresses" : ("helper_addresses", Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses)}
                            self._child_list_classes = {}

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.helper_addresses = Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses()
                            self.helper_addresses.parent = self
                            self._children_name_map["helper_addresses"] = "helper-addresses"
                            self._children_yang_names.add("helper-addresses")
                            self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf, ['vrf_name'], name, value)


                        class HelperAddresses(Entity):
                            """
                            Table of HelperAddress
                            
                            .. attribute:: helper_address
                            
                            	DHCPv6 Helper Address
                            	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses, self).__init__()

                                self.yang_name = "helper-addresses"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"helper-address" : ("helper_address", Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress)}

                                self.helper_address = YList(self)
                                self._segment_path = lambda: "helper-addresses"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses, [], name, value)


                            class HelperAddress(Entity):
                                """
                                DHCPv6 Helper Address
                                
                                .. attribute:: helper_address  <key>
                                
                                	DHCPv6 Helper Address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: any_out_interface
                                
                                	DHCPv6 HelperAddress Output Interface
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: out_interface
                                
                                	DHCPv6 HelperAddress Specific Output Interface
                                	**type**\:  str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__init__()

                                    self.yang_name = "helper-address"
                                    self.yang_parent_name = "helper-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.helper_address = YLeaf(YType.str, "helper-address")

                                    self.any_out_interface = YLeaf(YType.empty, "any-out-interface")

                                    self.out_interface = YLeaf(YType.str, "out-interface")
                                    self._segment_path = lambda: "helper-address" + "[helper-address='" + self.helper_address.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, ['helper_address', 'any_out_interface', 'out_interface'], name, value)


            class Relay(Entity):
                """
                None
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Relay
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: helper_addresses
                
                	Table of HelperAddress
                	**type**\:   :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay.HelperAddresses>`
                
                .. attribute:: iana_route_add
                
                	Enable route addition for IANA
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Dhcpv6.Profiles.Profile.Relay, self).__init__()

                    self.yang_name = "relay"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"helper-addresses" : ("helper_addresses", Dhcpv6.Profiles.Profile.Relay.HelperAddresses)}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.enable = YLeaf(YType.empty, "enable")

                    self.iana_route_add = YLeaf(YType.empty, "iana-route-add")

                    self.helper_addresses = Dhcpv6.Profiles.Profile.Relay.HelperAddresses()
                    self.helper_addresses.parent = self
                    self._children_name_map["helper_addresses"] = "helper-addresses"
                    self._children_yang_names.add("helper-addresses")
                    self._segment_path = lambda: "relay"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Profiles.Profile.Relay, ['enable', 'iana_route_add'], name, value)


                class HelperAddresses(Entity):
                    """
                    Table of HelperAddress
                    
                    .. attribute:: helper_address
                    
                    	Specify the server helper address
                    	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Relay.HelperAddresses, self).__init__()

                        self.yang_name = "helper-addresses"
                        self.yang_parent_name = "relay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"helper-address" : ("helper_address", Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress)}

                        self.helper_address = YList(self)
                        self._segment_path = lambda: "helper-addresses"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Relay.HelperAddresses, [], name, value)


                    class HelperAddress(Entity):
                        """
                        Specify the server helper address
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: helper_address  <key>
                        
                        	Server Global unicast address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress, self).__init__()

                            self.yang_name = "helper-address"
                            self.yang_parent_name = "helper-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.helper_address = YLeaf(YType.str, "helper-address")
                            self._segment_path = lambda: "helper-address" + "[vrf-name='" + self.vrf_name.get() + "']" + "[helper-address='" + self.helper_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress, ['vrf_name', 'helper_address'], name, value)


            class Server(Entity):
                """
                None
                
                .. attribute:: address_pool
                
                	Address pool name
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: aftr_name
                
                	AFTR name
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: classes
                
                	Table of Class
                	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes>`
                
                .. attribute:: dhcpv6_options
                
                	DHCPv6 options
                	**type**\:   :py:class:`Dhcpv6Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Dhcpv6Options>`
                
                .. attribute:: dns_servers
                
                	DNS servers
                	**type**\:   :py:class:`DnsServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.DnsServers>`
                
                .. attribute:: domain_name
                
                	Domain name
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Server
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: lease
                
                	lease
                	**type**\:   :py:class:`Lease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Lease>`
                
                .. attribute:: preference
                
                	DHCP Server Preference
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: prefix_pool
                
                	Prefix pool name
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: rapid_commit
                
                	Allow RAPID Commit
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: sessions
                
                	Change sessions configuration
                	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Sessions>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Dhcpv6.Profiles.Profile.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"classes" : ("classes", Dhcpv6.Profiles.Profile.Server.Classes), "dhcpv6-options" : ("dhcpv6_options", Dhcpv6.Profiles.Profile.Server.Dhcpv6Options), "dns-servers" : ("dns_servers", Dhcpv6.Profiles.Profile.Server.DnsServers), "lease" : ("lease", Dhcpv6.Profiles.Profile.Server.Lease), "sessions" : ("sessions", Dhcpv6.Profiles.Profile.Server.Sessions)}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.address_pool = YLeaf(YType.str, "address-pool")

                    self.aftr_name = YLeaf(YType.str, "aftr-name")

                    self.domain_name = YLeaf(YType.str, "domain-name")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.preference = YLeaf(YType.uint32, "preference")

                    self.prefix_pool = YLeaf(YType.str, "prefix-pool")

                    self.rapid_commit = YLeaf(YType.empty, "rapid-commit")

                    self.classes = Dhcpv6.Profiles.Profile.Server.Classes()
                    self.classes.parent = self
                    self._children_name_map["classes"] = "classes"
                    self._children_yang_names.add("classes")

                    self.dhcpv6_options = Dhcpv6.Profiles.Profile.Server.Dhcpv6Options()
                    self.dhcpv6_options.parent = self
                    self._children_name_map["dhcpv6_options"] = "dhcpv6-options"
                    self._children_yang_names.add("dhcpv6-options")

                    self.dns_servers = Dhcpv6.Profiles.Profile.Server.DnsServers()
                    self.dns_servers.parent = self
                    self._children_name_map["dns_servers"] = "dns-servers"
                    self._children_yang_names.add("dns-servers")

                    self.lease = Dhcpv6.Profiles.Profile.Server.Lease()
                    self.lease.parent = self
                    self._children_name_map["lease"] = "lease"
                    self._children_yang_names.add("lease")

                    self.sessions = Dhcpv6.Profiles.Profile.Server.Sessions()
                    self.sessions.parent = self
                    self._children_name_map["sessions"] = "sessions"
                    self._children_yang_names.add("sessions")
                    self._segment_path = lambda: "server"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Profiles.Profile.Server, ['address_pool', 'aftr_name', 'domain_name', 'enable', 'preference', 'prefix_pool', 'rapid_commit'], name, value)


                class Classes(Entity):
                    """
                    Table of Class
                    
                    .. attribute:: class_
                    
                    	None
                    	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes.Class_>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.Classes, self).__init__()

                        self.yang_name = "classes"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"class" : ("class_", Dhcpv6.Profiles.Profile.Server.Classes.Class_)}

                        self.class_ = YList(self)
                        self._segment_path = lambda: "classes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Classes, [], name, value)


                    class Class_(Entity):
                        """
                        None
                        
                        .. attribute:: class_name  <key>
                        
                        	class name
                        	**type**\:  str
                        
                        	**length:** 1..128
                        
                        .. attribute:: address_pool
                        
                        	Address pool name
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: dns_servers
                        
                        	DNS servers
                        	**type**\:   :py:class:`DnsServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers>`
                        
                        .. attribute:: domain_name
                        
                        	Domain name
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: preference
                        
                        	DHCP Server Preference
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        .. attribute:: prefix_pool
                        
                        	Prefix pool name
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Server.Classes.Class_, self).__init__()

                            self.yang_name = "class"
                            self.yang_parent_name = "classes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"dns-servers" : ("dns_servers", Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers)}
                            self._child_list_classes = {}

                            self.class_name = YLeaf(YType.str, "class-name")

                            self.address_pool = YLeaf(YType.str, "address-pool")

                            self.domain_name = YLeaf(YType.str, "domain-name")

                            self.preference = YLeaf(YType.uint32, "preference")

                            self.prefix_pool = YLeaf(YType.str, "prefix-pool")

                            self.dns_servers = Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers()
                            self.dns_servers.parent = self
                            self._children_name_map["dns_servers"] = "dns-servers"
                            self._children_yang_names.add("dns-servers")
                            self._segment_path = lambda: "class" + "[class-name='" + self.class_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Classes.Class_, ['class_name', 'address_pool', 'domain_name', 'preference', 'prefix_pool'], name, value)


                        class DnsServers(Entity):
                            """
                            DNS servers
                            
                            .. attribute:: dns_server
                            
                            	Server's IPv6 address
                            	**type**\: one of the below types:
                            
                            	**type**\:  list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  list of str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers, self).__init__()

                                self.yang_name = "dns-servers"
                                self.yang_parent_name = "class"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.dns_server = YLeafList(YType.str, "dns-server")
                                self._segment_path = lambda: "dns-servers"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers, ['dns_server'], name, value)


                class Dhcpv6Options(Entity):
                    """
                    DHCPv6 options
                    
                    .. attribute:: vendor_options
                    
                    	Vendor options
                    	**type**\:   :py:class:`VendorOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.Dhcpv6Options, self).__init__()

                        self.yang_name = "dhcpv6-options"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"vendor-options" : ("vendor_options", Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions)}
                        self._child_list_classes = {}

                        self.vendor_options = Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions()
                        self.vendor_options.parent = self
                        self._children_name_map["vendor_options"] = "vendor-options"
                        self._children_yang_names.add("vendor-options")
                        self._segment_path = lambda: "dhcpv6-options"


                    class VendorOptions(Entity):
                        """
                        Vendor options
                        
                        .. attribute:: type
                        
                        	Set string
                        	**type**\:  str
                        
                        .. attribute:: vendor_options
                        
                        	Vendor options
                        	**type**\:  str
                        
                        	**length:** 1..512
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions, self).__init__()

                            self.yang_name = "vendor-options"
                            self.yang_parent_name = "dhcpv6-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.type = YLeaf(YType.str, "type")

                            self.vendor_options = YLeaf(YType.str, "vendor-options")
                            self._segment_path = lambda: "vendor-options"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions, ['type', 'vendor_options'], name, value)


                class DnsServers(Entity):
                    """
                    DNS servers
                    
                    .. attribute:: dns_server
                    
                    	Server's IPv6 address
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.DnsServers, self).__init__()

                        self.yang_name = "dns-servers"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.dns_server = YLeafList(YType.str, "dns-server")
                        self._segment_path = lambda: "dns-servers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Server.DnsServers, ['dns_server'], name, value)


                class Lease(Entity):
                    """
                    lease
                    
                    .. attribute:: days
                    
                    	Days
                    	**type**\:  int
                    
                    	**range:** 0..365
                    
                    	**units**\: day
                    
                    .. attribute:: hours
                    
                    	Hours
                    	**type**\:  int
                    
                    	**range:** 0..23
                    
                    	**units**\: hour
                    
                    .. attribute:: infinite
                    
                    	Set string
                    	**type**\:  str
                    
                    .. attribute:: minutes
                    
                    	Minutes
                    	**type**\:  int
                    
                    	**range:** 1..59
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.Lease, self).__init__()

                        self.yang_name = "lease"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.days = YLeaf(YType.uint32, "days")

                        self.hours = YLeaf(YType.uint32, "hours")

                        self.infinite = YLeaf(YType.str, "infinite")

                        self.minutes = YLeaf(YType.uint32, "minutes")
                        self._segment_path = lambda: "lease"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Lease, ['days', 'hours', 'infinite', 'minutes'], name, value)


                class Sessions(Entity):
                    """
                    Change sessions configuration
                    
                    .. attribute:: mac
                    
                    	Throttle DHCP sessions based on MAC address
                    	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Sessions.Mac>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.Sessions, self).__init__()

                        self.yang_name = "sessions"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"mac" : ("mac", Dhcpv6.Profiles.Profile.Server.Sessions.Mac)}
                        self._child_list_classes = {}

                        self.mac = Dhcpv6.Profiles.Profile.Server.Sessions.Mac()
                        self.mac.parent = self
                        self._children_name_map["mac"] = "mac"
                        self._children_yang_names.add("mac")
                        self._segment_path = lambda: "sessions"


                    class Mac(Entity):
                        """
                        Throttle DHCP sessions based on MAC address
                        
                        .. attribute:: throttle
                        
                        	Throttle DHCP sessions from any one MAC address
                        	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Server.Sessions.Mac, self).__init__()

                            self.yang_name = "mac"
                            self.yang_parent_name = "sessions"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"throttle" : ("throttle", Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle)}
                            self._child_list_classes = {}

                            self.throttle = Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle()
                            self.throttle.parent = self
                            self._children_name_map["throttle"] = "throttle"
                            self._children_yang_names.add("throttle")
                            self._segment_path = lambda: "mac"


                        class Throttle(Entity):
                            """
                            Throttle DHCP sessions from any one MAC
                            address
                            
                            .. attribute:: block
                            
                            	Throttle blocking period (in secs)
                            	**type**\:  int
                            
                            	**range:** 1..100
                            
                            	**units**\: second
                            
                            .. attribute:: limit
                            
                            	Number of solicits at which to throttle
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: request
                            
                            	Throttle request period (in secs)
                            	**type**\:  int
                            
                            	**range:** 1..100
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle, self).__init__()

                                self.yang_name = "throttle"
                                self.yang_parent_name = "mac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.block = YLeaf(YType.uint32, "block")

                                self.limit = YLeaf(YType.uint32, "limit")

                                self.request = YLeaf(YType.uint32, "request")
                                self._segment_path = lambda: "throttle"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle, ['block', 'limit', 'request'], name, value)

    def clone_ptr(self):
        self._top_entity = Dhcpv6()
        return self._top_entity

