""" Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-new\-dhcpv6d package configuration.

This module contains definitions
for the following management objects\:
  dhcpv6\: None

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Insert(Enum):
    """
    Insert (Enum Class)

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
    LinkLayerAddr (Enum Class)

    Link layer addr

    .. data:: set = 4

    	Insert Received LinkLayerAddr Value from SADB

    """

    set = Enum.YLeaf(4, "set")


class SubscriberId(Enum):
    """
    SubscriberId (Enum Class)

    Subscriber id

    .. data:: pppoe = 3

    	Insert Received Subscriber-ID Value from SADB

    """

    pppoe = Enum.YLeaf(3, "pppoe")



class Dhcpv6(Entity):
    """
    None
    
    .. attribute:: database
    
    	Enable DHCP binding database storage to file system
    	**type**\:  :py:class:`Database <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Database>`
    
    .. attribute:: profiles
    
    	Table of Profile
    	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles>`
    
    .. attribute:: interfaces
    
    	Table of Interface
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces>`
    
    .. attribute:: enable
    
    	Enable None. Deletion of this object also causes deletion of all associated objects under DHCPv6
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    	**mandatory**\: True
    
    .. attribute:: allow_duid_change
    
    	For BNG session, allow duid change for a client MAC
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

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
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("database", ("database", Dhcpv6.Database)), ("profiles", ("profiles", Dhcpv6.Profiles)), ("interfaces", ("interfaces", Dhcpv6.Interfaces))])
        self._child_list_classes = OrderedDict([])
        self.is_presence_container = True
        self._leafs = OrderedDict([
            ('enable', YLeaf(YType.empty, 'enable')),
            ('allow_duid_change', YLeaf(YType.empty, 'allow-duid-change')),
        ])
        self.enable = None
        self.allow_duid_change = None

        self.database = Dhcpv6.Database()
        self.database.parent = self
        self._children_name_map["database"] = "database"
        self._children_yang_names.add("database")

        self.profiles = Dhcpv6.Profiles()
        self.profiles.parent = self
        self._children_name_map["profiles"] = "profiles"
        self._children_yang_names.add("profiles")

        self.interfaces = Dhcpv6.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6"

    def __setattr__(self, name, value):
        self._perform_setattr(Dhcpv6, ['enable', 'allow_duid_change'], name, value)


    class Database(Entity):
        """
        Enable DHCP binding database storage to file
        system
        
        .. attribute:: proxy
        
        	Enable DHCP proxy binding database storage to file system
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: server
        
        	Enable DHCP server binding database storage to file system
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: relay
        
        	Enable DHCP relay binding database storage to file system
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: full_write_interval
        
        	Full file write interval (default 10 minutes)
        	**type**\: int
        
        	**range:** 1..1440
        
        	**default value**\: 10
        
        .. attribute:: incremental_write_interval
        
        	Incremental file write interval (default 1 minutes)
        	**type**\: int
        
        	**range:** 1..1440
        
        	**default value**\: 1
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Dhcpv6.Database, self).__init__()

            self.yang_name = "database"
            self.yang_parent_name = "dhcpv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('proxy', YLeaf(YType.empty, 'proxy')),
                ('server', YLeaf(YType.empty, 'server')),
                ('relay', YLeaf(YType.empty, 'relay')),
                ('full_write_interval', YLeaf(YType.uint32, 'full-write-interval')),
                ('incremental_write_interval', YLeaf(YType.uint32, 'incremental-write-interval')),
            ])
            self.proxy = None
            self.server = None
            self.relay = None
            self.full_write_interval = None
            self.incremental_write_interval = None
            self._segment_path = lambda: "database"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Dhcpv6.Database, ['proxy', 'server', 'relay', 'full_write_interval', 'incremental_write_interval'], name, value)


    class Profiles(Entity):
        """
        Table of Profile
        
        .. attribute:: profile
        
        	None
        	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Dhcpv6.Profiles, self).__init__()

            self.yang_name = "profiles"
            self.yang_parent_name = "dhcpv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("profile", ("profile", Dhcpv6.Profiles.Profile))])
            self._leafs = OrderedDict()

            self.profile = YList(self)
            self._segment_path = lambda: "profiles"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Dhcpv6.Profiles, [], name, value)


        class Profile(Entity):
            """
            None
            
            .. attribute:: profile_name  (key)
            
            	Profile name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: relay
            
            	None
            	**type**\:  :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay>`
            
            	**presence node**\: True
            
            .. attribute:: base
            
            	None
            	**type**\:  :py:class:`Base <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base>`
            
            	**presence node**\: True
            
            .. attribute:: proxy
            
            	None
            	**type**\:  :py:class:`Proxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy>`
            
            	**presence node**\: True
            
            .. attribute:: server
            
            	None
            	**type**\:  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server>`
            
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
                self.ylist_key_names = ['profile_name']
                self._child_container_classes = OrderedDict([("relay", ("relay", Dhcpv6.Profiles.Profile.Relay)), ("base", ("base", Dhcpv6.Profiles.Profile.Base)), ("proxy", ("proxy", Dhcpv6.Profiles.Profile.Proxy)), ("server", ("server", Dhcpv6.Profiles.Profile.Server))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('profile_name', YLeaf(YType.str, 'profile-name')),
                ])
                self.profile_name = None

                self.relay = None
                self._children_name_map["relay"] = "relay"
                self._children_yang_names.add("relay")

                self.base = None
                self._children_name_map["base"] = "base"
                self._children_yang_names.add("base")

                self.proxy = None
                self._children_name_map["proxy"] = "proxy"
                self._children_yang_names.add("proxy")

                self.server = None
                self._children_name_map["server"] = "server"
                self._children_yang_names.add("server")
                self._segment_path = lambda: "profile" + "[profile-name='" + str(self.profile_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/profiles/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Dhcpv6.Profiles.Profile, ['profile_name'], name, value)


            class Relay(Entity):
                """
                None
                
                .. attribute:: helper_addresses
                
                	Table of HelperAddress
                	**type**\:  :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay.HelperAddresses>`
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Relay
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: iana_route_add
                
                	Enable route addition for IANA
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("helper-addresses", ("helper_addresses", Dhcpv6.Profiles.Profile.Relay.HelperAddresses))])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enable', YLeaf(YType.empty, 'enable')),
                        ('iana_route_add', YLeaf(YType.empty, 'iana-route-add')),
                    ])
                    self.enable = None
                    self.iana_route_add = None

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
                    	**type**\: list of  		 :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Relay.HelperAddresses, self).__init__()

                        self.yang_name = "helper-addresses"
                        self.yang_parent_name = "relay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("helper-address", ("helper_address", Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress))])
                        self._leafs = OrderedDict()

                        self.helper_address = YList(self)
                        self._segment_path = lambda: "helper-addresses"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Relay.HelperAddresses, [], name, value)


                    class HelperAddress(Entity):
                        """
                        Specify the server helper address
                        
                        .. attribute:: vrf_name  (key)
                        
                        	VRF name
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: helper_address  (key)
                        
                        	Server Global unicast address
                        	**type**\: str
                        
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
                            self.ylist_key_names = ['vrf_name','helper_address']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                ('helper_address', YLeaf(YType.str, 'helper-address')),
                            ])
                            self.vrf_name = None
                            self.helper_address = None
                            self._segment_path = lambda: "helper-address" + "[vrf-name='" + str(self.vrf_name) + "']" + "[helper-address='" + str(self.helper_address) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress, ['vrf_name', 'helper_address'], name, value)


            class Base(Entity):
                """
                None
                
                .. attribute:: default
                
                	Default match option
                	**type**\:  :py:class:`Default <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Default>`
                
                .. attribute:: match
                
                	Enter match option
                	**type**\:  :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match>`
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Base
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                

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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("default", ("default", Dhcpv6.Profiles.Profile.Base.Default)), ("match", ("match", Dhcpv6.Profiles.Profile.Base.Match))])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enable', YLeaf(YType.empty, 'enable')),
                    ])
                    self.enable = None

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
                    	**type**\: list of  		 :py:class:`Profile_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Default.Profile_>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Base.Default, self).__init__()

                        self.yang_name = "default"
                        self.yang_parent_name = "base"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("profile", ("profile", Dhcpv6.Profiles.Profile.Base.Default.Profile_))])
                        self._leafs = OrderedDict()

                        self.profile = YList(self)
                        self._segment_path = lambda: "default"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Default, [], name, value)


                    class Profile_(Entity):
                        """
                        Enter proxy or server profile
                        
                        .. attribute:: profile_name  (key)
                        
                        	Profile name
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: server_mode
                        
                        	Specify mode\-class based Server option
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: proxy_mode
                        
                        	Specify mode\-class based Proxy Option
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Base.Default.Profile_, self).__init__()

                            self.yang_name = "profile"
                            self.yang_parent_name = "default"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['profile_name']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('profile_name', YLeaf(YType.str, 'profile-name')),
                                ('server_mode', YLeaf(YType.empty, 'server-mode')),
                                ('proxy_mode', YLeaf(YType.empty, 'proxy-mode')),
                            ])
                            self.profile_name = None
                            self.server_mode = None
                            self.proxy_mode = None
                            self._segment_path = lambda: "profile" + "[profile-name='" + str(self.profile_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Default.Profile_, ['profile_name', 'server_mode', 'proxy_mode'], name, value)


                class Match(Entity):
                    """
                    Enter match option
                    
                    .. attribute:: mode_classes
                    
                    	Table of ModeClass
                    	**type**\:  :py:class:`ModeClasses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match.ModeClasses>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Base.Match, self).__init__()

                        self.yang_name = "match"
                        self.yang_parent_name = "base"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("mode-classes", ("mode_classes", Dhcpv6.Profiles.Profile.Base.Match.ModeClasses))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

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
                        	**type**\: list of  		 :py:class:`ModeClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses, self).__init__()

                            self.yang_name = "mode-classes"
                            self.yang_parent_name = "match"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("mode-class", ("mode_class", Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass))])
                            self._leafs = OrderedDict()

                            self.mode_class = YList(self)
                            self._segment_path = lambda: "mode-classes"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses, [], name, value)


                        class ModeClass(Entity):
                            """
                            Specify PPP/IPoE class option
                            
                            .. attribute:: class_name  (key)
                            
                            	Class name
                            	**type**\: str
                            
                            	**length:** 1..128
                            
                            .. attribute:: profile
                            
                            	Enter proxy or server profile
                            	**type**\: list of  		 :py:class:`Profile_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile_>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass, self).__init__()

                                self.yang_name = "mode-class"
                                self.yang_parent_name = "mode-classes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['class_name']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("profile", ("profile", Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile_))])
                                self._leafs = OrderedDict([
                                    ('class_name', YLeaf(YType.str, 'class-name')),
                                ])
                                self.class_name = None

                                self.profile = YList(self)
                                self._segment_path = lambda: "mode-class" + "[class-name='" + str(self.class_name) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass, ['class_name'], name, value)


                            class Profile_(Entity):
                                """
                                Enter proxy or server profile
                                
                                .. attribute:: profile_name  (key)
                                
                                	Profile name
                                	**type**\: str
                                
                                	**length:** 1..64
                                
                                .. attribute:: server_mode
                                
                                	Specify mode\-class based Server option
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: proxy_mode
                                
                                	Specify mode\-class based Proxy Option
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile_, self).__init__()

                                    self.yang_name = "profile"
                                    self.yang_parent_name = "mode-class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['profile_name']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('profile_name', YLeaf(YType.str, 'profile-name')),
                                        ('server_mode', YLeaf(YType.empty, 'server-mode')),
                                        ('proxy_mode', YLeaf(YType.empty, 'proxy-mode')),
                                    ])
                                    self.profile_name = None
                                    self.server_mode = None
                                    self.proxy_mode = None
                                    self._segment_path = lambda: "profile" + "[profile-name='" + str(self.profile_name) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile_, ['profile_name', 'server_mode', 'proxy_mode'], name, value)


            class Proxy(Entity):
                """
                None
                
                .. attribute:: interfaces
                
                	Table of Interface
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Interfaces>`
                
                .. attribute:: relay
                
                	Specify relay configuration
                	**type**\:  :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Relay>`
                
                .. attribute:: vrfs
                
                	VRF related configuration
                	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs>`
                
                .. attribute:: authentication
                
                	Authentication username format
                	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Authentication>`
                
                .. attribute:: classes
                
                	Table of Class
                	**type**\:  :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes>`
                
                .. attribute:: sessions
                
                	Change sessions configuration
                	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Sessions>`
                
                .. attribute:: linkaddress_from_ra_enable
                
                	Fill linkaddress in Relay fwd msg with Prefix from Router Advertisement for PPPoE sessions
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route_add_disable
                
                	RouteDisable
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: link_address
                
                	IPv6 address to be filled in link\-address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: src_intf_name
                
                	Create or enter proxy profile Source Interface Name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Proxy
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                

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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("interfaces", ("interfaces", Dhcpv6.Profiles.Profile.Proxy.Interfaces)), ("relay", ("relay", Dhcpv6.Profiles.Profile.Proxy.Relay)), ("vrfs", ("vrfs", Dhcpv6.Profiles.Profile.Proxy.Vrfs)), ("authentication", ("authentication", Dhcpv6.Profiles.Profile.Proxy.Authentication)), ("classes", ("classes", Dhcpv6.Profiles.Profile.Proxy.Classes)), ("sessions", ("sessions", Dhcpv6.Profiles.Profile.Proxy.Sessions))])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('linkaddress_from_ra_enable', YLeaf(YType.empty, 'linkaddress-from-ra-enable')),
                        ('route_add_disable', YLeaf(YType.empty, 'route-add-disable')),
                        ('link_address', YLeaf(YType.str, 'link-address')),
                        ('src_intf_name', YLeaf(YType.str, 'src-intf-name')),
                        ('enable', YLeaf(YType.empty, 'enable')),
                    ])
                    self.linkaddress_from_ra_enable = None
                    self.route_add_disable = None
                    self.link_address = None
                    self.src_intf_name = None
                    self.enable = None

                    self.interfaces = Dhcpv6.Profiles.Profile.Proxy.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")

                    self.relay = Dhcpv6.Profiles.Profile.Proxy.Relay()
                    self.relay.parent = self
                    self._children_name_map["relay"] = "relay"
                    self._children_yang_names.add("relay")

                    self.vrfs = Dhcpv6.Profiles.Profile.Proxy.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                    self._children_yang_names.add("vrfs")

                    self.authentication = Dhcpv6.Profiles.Profile.Proxy.Authentication()
                    self.authentication.parent = self
                    self._children_name_map["authentication"] = "authentication"
                    self._children_yang_names.add("authentication")

                    self.classes = Dhcpv6.Profiles.Profile.Proxy.Classes()
                    self.classes.parent = self
                    self._children_name_map["classes"] = "classes"
                    self._children_yang_names.add("classes")

                    self.sessions = Dhcpv6.Profiles.Profile.Proxy.Sessions()
                    self.sessions.parent = self
                    self._children_name_map["sessions"] = "sessions"
                    self._children_yang_names.add("sessions")
                    self._segment_path = lambda: "proxy"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy, ['linkaddress_from_ra_enable', 'route_add_disable', 'link_address', 'src_intf_name', 'enable'], name, value)


                class Interfaces(Entity):
                    """
                    Table of Interface
                    
                    .. attribute:: interface
                    
                    	None
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("interface", ("interface", Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        None
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface to configure
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: interface_id
                        
                        	Physical interface ID
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', YLeaf(YType.str, 'interface-name')),
                                ('interface_id', YLeaf(YType.str, 'interface-id')),
                            ])
                            self.interface_name = None
                            self.interface_id = None
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface, ['interface_name', 'interface_id'], name, value)


                class Relay(Entity):
                    """
                    Specify relay configuration
                    
                    .. attribute:: option
                    
                    	Specify relay option configuration
                    	**type**\:  :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Relay.Option>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Relay, self).__init__()

                        self.yang_name = "relay"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("option", ("option", Dhcpv6.Profiles.Profile.Proxy.Relay.Option))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

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
                        	**type**\:  :py:class:`InterfaceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId>`
                        
                        .. attribute:: subscriber_id
                        
                        	Configure Received SubscriberID
                        	**type**\:  :py:class:`SubscriberId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.SubscriberId>`
                        
                        .. attribute:: link_layer_addr
                        
                        	Configure Received link\-layer\-Addr
                        	**type**\:  :py:class:`LinkLayerAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.LinkLayerAddr>`
                        
                        .. attribute:: remote_i_dreceived
                        
                        	Set remote\-id value from SADB
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: remote_id
                        
                        	Enter remote\-id value
                        	**type**\: str
                        
                        	**length:** 1..256
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Relay.Option, self).__init__()

                            self.yang_name = "option"
                            self.yang_parent_name = "relay"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("interface-id", ("interface_id", Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('subscriber_id', YLeaf(YType.enumeration, 'subscriber-id')),
                                ('link_layer_addr', YLeaf(YType.enumeration, 'link-layer-addr')),
                                ('remote_i_dreceived', YLeaf(YType.int32, 'remote-i-dreceived')),
                                ('remote_id', YLeaf(YType.str, 'remote-id')),
                            ])
                            self.subscriber_id = None
                            self.link_layer_addr = None
                            self.remote_i_dreceived = None
                            self.remote_id = None

                            self.interface_id = Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId()
                            self.interface_id.parent = self
                            self._children_name_map["interface_id"] = "interface-id"
                            self._children_yang_names.add("interface-id")
                            self._segment_path = lambda: "option"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Relay.Option, ['subscriber_id', 'link_layer_addr', 'remote_i_dreceived', 'remote_id'], name, value)


                        class InterfaceId(Entity):
                            """
                            Interface Id option
                            
                            .. attribute:: insert
                            
                            	Configure InterfaceID insert type
                            	**type**\:  :py:class:`Insert <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Insert>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId, self).__init__()

                                self.yang_name = "interface-id"
                                self.yang_parent_name = "option"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('insert', YLeaf(YType.enumeration, 'insert')),
                                ])
                                self.insert = None
                                self._segment_path = lambda: "interface-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId, ['insert'], name, value)


                class Vrfs(Entity):
                    """
                    VRF related configuration
                    
                    .. attribute:: vrf
                    
                    	IPv6 DHCP proxy VRF name
                    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("vrf", ("vrf", Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf))])
                        self._leafs = OrderedDict()

                        self.vrf = YList(self)
                        self._segment_path = lambda: "vrfs"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Vrfs, [], name, value)


                    class Vrf(Entity):
                        """
                        IPv6 DHCP proxy VRF name
                        
                        .. attribute:: vrf_name  (key)
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: helper_addresses
                        
                        	Table of HelperAddress
                        	**type**\:  :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vrf_name']
                            self._child_container_classes = OrderedDict([("helper-addresses", ("helper_addresses", Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ])
                            self.vrf_name = None

                            self.helper_addresses = Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses()
                            self.helper_addresses.parent = self
                            self._children_name_map["helper_addresses"] = "helper-addresses"
                            self._children_yang_names.add("helper-addresses")
                            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf, ['vrf_name'], name, value)


                        class HelperAddresses(Entity):
                            """
                            Table of HelperAddress
                            
                            .. attribute:: helper_address
                            
                            	DHCPv6 Helper Address
                            	**type**\: list of  		 :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses, self).__init__()

                                self.yang_name = "helper-addresses"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("helper-address", ("helper_address", Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress))])
                                self._leafs = OrderedDict()

                                self.helper_address = YList(self)
                                self._segment_path = lambda: "helper-addresses"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses, [], name, value)


                            class HelperAddress(Entity):
                                """
                                DHCPv6 Helper Address
                                
                                .. attribute:: helper_address  (key)
                                
                                	DHCPv6 Helper Address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: out_interface
                                
                                	DHCPv6 HelperAddress Specific Output Interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                .. attribute:: any_out_interface
                                
                                	DHCPv6 HelperAddress Output Interface
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__init__()

                                    self.yang_name = "helper-address"
                                    self.yang_parent_name = "helper-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['helper_address']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('helper_address', YLeaf(YType.str, 'helper-address')),
                                        ('out_interface', YLeaf(YType.str, 'out-interface')),
                                        ('any_out_interface', YLeaf(YType.empty, 'any-out-interface')),
                                    ])
                                    self.helper_address = None
                                    self.out_interface = None
                                    self.any_out_interface = None
                                    self._segment_path = lambda: "helper-address" + "[helper-address='" + str(self.helper_address) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, ['helper_address', 'out_interface', 'any_out_interface'], name, value)


                class Authentication(Entity):
                    """
                    Authentication username format
                    
                    .. attribute:: username
                    
                    	Set username as DUID
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Authentication, self).__init__()

                        self.yang_name = "authentication"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('username', YLeaf(YType.empty, 'username')),
                        ])
                        self.username = None
                        self._segment_path = lambda: "authentication"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Authentication, ['username'], name, value)


                class Classes(Entity):
                    """
                    Table of Class
                    
                    .. attribute:: class_
                    
                    	None
                    	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes.Class>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Classes, self).__init__()

                        self.yang_name = "classes"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("class", ("class_", Dhcpv6.Profiles.Profile.Proxy.Classes.Class))])
                        self._leafs = OrderedDict()

                        self.class_ = YList(self)
                        self._segment_path = lambda: "classes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Classes, [], name, value)


                    class Class(Entity):
                        """
                        None
                        
                        .. attribute:: class_name  (key)
                        
                        	Class name
                        	**type**\: str
                        
                        	**length:** 1..128
                        
                        .. attribute:: helper_addresses
                        
                        	Table of HelperAddress
                        	**type**\:  :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses>`
                        
                        .. attribute:: link_address
                        
                        	IPv6 address to be filled in link\-address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class, self).__init__()

                            self.yang_name = "class"
                            self.yang_parent_name = "classes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['class_name']
                            self._child_container_classes = OrderedDict([("helper-addresses", ("helper_addresses", Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('class_name', YLeaf(YType.str, 'class-name')),
                                ('link_address', YLeaf(YType.str, 'link-address')),
                            ])
                            self.class_name = None
                            self.link_address = None

                            self.helper_addresses = Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses()
                            self.helper_addresses.parent = self
                            self._children_name_map["helper_addresses"] = "helper-addresses"
                            self._children_yang_names.add("helper-addresses")
                            self._segment_path = lambda: "class" + "[class-name='" + str(self.class_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Classes.Class, ['class_name', 'link_address'], name, value)


                        class HelperAddresses(Entity):
                            """
                            Table of HelperAddress
                            
                            .. attribute:: helper_address
                            
                            	Specify the server helper address
                            	**type**\: list of  		 :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses, self).__init__()

                                self.yang_name = "helper-addresses"
                                self.yang_parent_name = "class"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("helper-address", ("helper_address", Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress))])
                                self._leafs = OrderedDict()

                                self.helper_address = YList(self)
                                self._segment_path = lambda: "helper-addresses"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses, [], name, value)


                            class HelperAddress(Entity):
                                """
                                Specify the server helper address
                                
                                .. attribute:: vrf_name  (key)
                                
                                	VRF name
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                .. attribute:: helper_address  (key)
                                
                                	Server address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress, self).__init__()

                                    self.yang_name = "helper-address"
                                    self.yang_parent_name = "helper-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['vrf_name','helper_address']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                        ('helper_address', YLeaf(YType.str, 'helper-address')),
                                    ])
                                    self.vrf_name = None
                                    self.helper_address = None
                                    self._segment_path = lambda: "helper-address" + "[vrf-name='" + str(self.vrf_name) + "']" + "[helper-address='" + str(self.helper_address) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress, ['vrf_name', 'helper_address'], name, value)


                class Sessions(Entity):
                    """
                    Change sessions configuration
                    
                    .. attribute:: mac
                    
                    	Throttle DHCP sessions based on MAC address
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Sessions, self).__init__()

                        self.yang_name = "sessions"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("mac", ("mac", Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

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
                        	**type**\:  :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac, self).__init__()

                            self.yang_name = "mac"
                            self.yang_parent_name = "sessions"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("throttle", ("throttle", Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.throttle = Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle()
                            self.throttle.parent = self
                            self._children_name_map["throttle"] = "throttle"
                            self._children_yang_names.add("throttle")
                            self._segment_path = lambda: "mac"


                        class Throttle(Entity):
                            """
                            Throttle DHCP sessions from any one MAC
                            address
                            
                            .. attribute:: limit
                            
                            	Number of solicits at which to throttle
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: request
                            
                            	Throttle request period (in secs)
                            	**type**\: int
                            
                            	**range:** 1..100
                            
                            	**units**\: second
                            
                            .. attribute:: block
                            
                            	Throttle blocking period (in secs)
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', YLeaf(YType.uint32, 'limit')),
                                    ('request', YLeaf(YType.uint32, 'request')),
                                    ('block', YLeaf(YType.uint32, 'block')),
                                ])
                                self.limit = None
                                self.request = None
                                self.block = None
                                self._segment_path = lambda: "throttle"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle, ['limit', 'request', 'block'], name, value)


            class Server(Entity):
                """
                None
                
                .. attribute:: sessions
                
                	Change sessions configuration
                	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Sessions>`
                
                .. attribute:: dns_servers
                
                	DNS servers
                	**type**\:  :py:class:`DnsServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.DnsServers>`
                
                .. attribute:: classes
                
                	Table of Class
                	**type**\:  :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes>`
                
                .. attribute:: lease
                
                	lease
                	**type**\:  :py:class:`Lease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Lease>`
                
                .. attribute:: dhcpv6_options
                
                	DHCPv6 options
                	**type**\:  :py:class:`Dhcpv6Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Dhcpv6Options>`
                
                .. attribute:: address_pool
                
                	Address pool name
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: aftr_name
                
                	AFTR name
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: domain_name
                
                	Domain name
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: preference
                
                	DHCP Server Preference
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: rapid_commit
                
                	Allow RAPID Commit
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Server
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: prefix_pool
                
                	Prefix pool name
                	**type**\: str
                
                	**length:** 1..64
                
                

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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("sessions", ("sessions", Dhcpv6.Profiles.Profile.Server.Sessions)), ("dns-servers", ("dns_servers", Dhcpv6.Profiles.Profile.Server.DnsServers)), ("classes", ("classes", Dhcpv6.Profiles.Profile.Server.Classes)), ("lease", ("lease", Dhcpv6.Profiles.Profile.Server.Lease)), ("dhcpv6-options", ("dhcpv6_options", Dhcpv6.Profiles.Profile.Server.Dhcpv6Options))])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('address_pool', YLeaf(YType.str, 'address-pool')),
                        ('aftr_name', YLeaf(YType.str, 'aftr-name')),
                        ('domain_name', YLeaf(YType.str, 'domain-name')),
                        ('preference', YLeaf(YType.uint32, 'preference')),
                        ('rapid_commit', YLeaf(YType.empty, 'rapid-commit')),
                        ('enable', YLeaf(YType.empty, 'enable')),
                        ('prefix_pool', YLeaf(YType.str, 'prefix-pool')),
                    ])
                    self.address_pool = None
                    self.aftr_name = None
                    self.domain_name = None
                    self.preference = None
                    self.rapid_commit = None
                    self.enable = None
                    self.prefix_pool = None

                    self.sessions = Dhcpv6.Profiles.Profile.Server.Sessions()
                    self.sessions.parent = self
                    self._children_name_map["sessions"] = "sessions"
                    self._children_yang_names.add("sessions")

                    self.dns_servers = Dhcpv6.Profiles.Profile.Server.DnsServers()
                    self.dns_servers.parent = self
                    self._children_name_map["dns_servers"] = "dns-servers"
                    self._children_yang_names.add("dns-servers")

                    self.classes = Dhcpv6.Profiles.Profile.Server.Classes()
                    self.classes.parent = self
                    self._children_name_map["classes"] = "classes"
                    self._children_yang_names.add("classes")

                    self.lease = Dhcpv6.Profiles.Profile.Server.Lease()
                    self.lease.parent = self
                    self._children_name_map["lease"] = "lease"
                    self._children_yang_names.add("lease")

                    self.dhcpv6_options = Dhcpv6.Profiles.Profile.Server.Dhcpv6Options()
                    self.dhcpv6_options.parent = self
                    self._children_name_map["dhcpv6_options"] = "dhcpv6-options"
                    self._children_yang_names.add("dhcpv6-options")
                    self._segment_path = lambda: "server"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Profiles.Profile.Server, ['address_pool', 'aftr_name', 'domain_name', 'preference', 'rapid_commit', 'enable', 'prefix_pool'], name, value)


                class Sessions(Entity):
                    """
                    Change sessions configuration
                    
                    .. attribute:: mac
                    
                    	Throttle DHCP sessions based on MAC address
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Sessions.Mac>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.Sessions, self).__init__()

                        self.yang_name = "sessions"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("mac", ("mac", Dhcpv6.Profiles.Profile.Server.Sessions.Mac))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

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
                        	**type**\:  :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Server.Sessions.Mac, self).__init__()

                            self.yang_name = "mac"
                            self.yang_parent_name = "sessions"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("throttle", ("throttle", Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.throttle = Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle()
                            self.throttle.parent = self
                            self._children_name_map["throttle"] = "throttle"
                            self._children_yang_names.add("throttle")
                            self._segment_path = lambda: "mac"


                        class Throttle(Entity):
                            """
                            Throttle DHCP sessions from any one MAC
                            address
                            
                            .. attribute:: limit
                            
                            	Number of solicits at which to throttle
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: request
                            
                            	Throttle request period (in secs)
                            	**type**\: int
                            
                            	**range:** 1..100
                            
                            	**units**\: second
                            
                            .. attribute:: block
                            
                            	Throttle blocking period (in secs)
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', YLeaf(YType.uint32, 'limit')),
                                    ('request', YLeaf(YType.uint32, 'request')),
                                    ('block', YLeaf(YType.uint32, 'block')),
                                ])
                                self.limit = None
                                self.request = None
                                self.block = None
                                self._segment_path = lambda: "throttle"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle, ['limit', 'request', 'block'], name, value)


                class DnsServers(Entity):
                    """
                    DNS servers
                    
                    .. attribute:: dns_server
                    
                    	Server's IPv6 address
                    	**type**\: union of the below types:
                    
                    		**type**\: list of str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: list of str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.DnsServers, self).__init__()

                        self.yang_name = "dns-servers"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('dns_server', YLeafList(YType.str, 'dns-server')),
                        ])
                        self.dns_server = []
                        self._segment_path = lambda: "dns-servers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Server.DnsServers, ['dns_server'], name, value)


                class Classes(Entity):
                    """
                    Table of Class
                    
                    .. attribute:: class_
                    
                    	None
                    	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes.Class>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.Classes, self).__init__()

                        self.yang_name = "classes"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("class", ("class_", Dhcpv6.Profiles.Profile.Server.Classes.Class))])
                        self._leafs = OrderedDict()

                        self.class_ = YList(self)
                        self._segment_path = lambda: "classes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Classes, [], name, value)


                    class Class(Entity):
                        """
                        None
                        
                        .. attribute:: class_name  (key)
                        
                        	class name
                        	**type**\: str
                        
                        	**length:** 1..128
                        
                        .. attribute:: dns_servers
                        
                        	DNS servers
                        	**type**\:  :py:class:`DnsServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers>`
                        
                        .. attribute:: address_pool
                        
                        	Address pool name
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: domain_name
                        
                        	Domain name
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: preference
                        
                        	DHCP Server Preference
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        .. attribute:: prefix_pool
                        
                        	Prefix pool name
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Server.Classes.Class, self).__init__()

                            self.yang_name = "class"
                            self.yang_parent_name = "classes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['class_name']
                            self._child_container_classes = OrderedDict([("dns-servers", ("dns_servers", Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('class_name', YLeaf(YType.str, 'class-name')),
                                ('address_pool', YLeaf(YType.str, 'address-pool')),
                                ('domain_name', YLeaf(YType.str, 'domain-name')),
                                ('preference', YLeaf(YType.uint32, 'preference')),
                                ('prefix_pool', YLeaf(YType.str, 'prefix-pool')),
                            ])
                            self.class_name = None
                            self.address_pool = None
                            self.domain_name = None
                            self.preference = None
                            self.prefix_pool = None

                            self.dns_servers = Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers()
                            self.dns_servers.parent = self
                            self._children_name_map["dns_servers"] = "dns-servers"
                            self._children_yang_names.add("dns-servers")
                            self._segment_path = lambda: "class" + "[class-name='" + str(self.class_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Classes.Class, ['class_name', 'address_pool', 'domain_name', 'preference', 'prefix_pool'], name, value)


                        class DnsServers(Entity):
                            """
                            DNS servers
                            
                            .. attribute:: dns_server
                            
                            	Server's IPv6 address
                            	**type**\: union of the below types:
                            
                            		**type**\: list of str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: list of str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers, self).__init__()

                                self.yang_name = "dns-servers"
                                self.yang_parent_name = "class"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dns_server', YLeafList(YType.str, 'dns-server')),
                                ])
                                self.dns_server = []
                                self._segment_path = lambda: "dns-servers"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers, ['dns_server'], name, value)


                class Lease(Entity):
                    """
                    lease
                    
                    .. attribute:: days
                    
                    	Days
                    	**type**\: int
                    
                    	**range:** 0..365
                    
                    	**units**\: day
                    
                    .. attribute:: hours
                    
                    	Hours
                    	**type**\: int
                    
                    	**range:** 0..23
                    
                    	**units**\: hour
                    
                    .. attribute:: minutes
                    
                    	Minutes
                    	**type**\: int
                    
                    	**range:** 1..59
                    
                    	**units**\: minute
                    
                    .. attribute:: infinite
                    
                    	Set string
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.Lease, self).__init__()

                        self.yang_name = "lease"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('days', YLeaf(YType.uint32, 'days')),
                            ('hours', YLeaf(YType.uint32, 'hours')),
                            ('minutes', YLeaf(YType.uint32, 'minutes')),
                            ('infinite', YLeaf(YType.str, 'infinite')),
                        ])
                        self.days = None
                        self.hours = None
                        self.minutes = None
                        self.infinite = None
                        self._segment_path = lambda: "lease"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Lease, ['days', 'hours', 'minutes', 'infinite'], name, value)


                class Dhcpv6Options(Entity):
                    """
                    DHCPv6 options
                    
                    .. attribute:: vendor_options
                    
                    	Vendor options
                    	**type**\:  :py:class:`VendorOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.Dhcpv6Options, self).__init__()

                        self.yang_name = "dhcpv6-options"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("vendor-options", ("vendor_options", Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

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
                        	**type**\: str
                        
                        .. attribute:: vendor_options
                        
                        	Vendor options
                        	**type**\: str
                        
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
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('type', YLeaf(YType.str, 'type')),
                                ('vendor_options', YLeaf(YType.str, 'vendor-options')),
                            ])
                            self.type = None
                            self.vendor_options = None
                            self._segment_path = lambda: "vendor-options"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions, ['type', 'vendor_options'], name, value)


    class Interfaces(Entity):
        """
        Table of Interface
        
        .. attribute:: interface
        
        	None
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Dhcpv6.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "dhcpv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("interface", ("interface", Dhcpv6.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Dhcpv6.Interfaces, [], name, value)


        class Interface(Entity):
            """
            None
            
            .. attribute:: interface_name  (key)
            
            	Interface to configure
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: pppoe
            
            	PPPoE subscriber interface
            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Pppoe>`
            
            .. attribute:: proxy
            
            	Assign a proxy profile to interface
            	**type**\:  :py:class:`Proxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Proxy>`
            
            .. attribute:: base
            
            	Assign a base profile to interface
            	**type**\:  :py:class:`Base <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Base>`
            
            .. attribute:: server
            
            	Assign a server profile to interface
            	**type**\:  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Server>`
            
            .. attribute:: relay
            
            	Assign a relay profile to interface
            	**type**\:  :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Relay>`
            
            

            """

            _prefix = 'ipv6-new-dhcpv6d-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Dhcpv6.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_container_classes = OrderedDict([("pppoe", ("pppoe", Dhcpv6.Interfaces.Interface.Pppoe)), ("proxy", ("proxy", Dhcpv6.Interfaces.Interface.Proxy)), ("base", ("base", Dhcpv6.Interfaces.Interface.Base)), ("server", ("server", Dhcpv6.Interfaces.Interface.Server)), ("relay", ("relay", Dhcpv6.Interfaces.Interface.Relay))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_name', YLeaf(YType.str, 'interface-name')),
                ])
                self.interface_name = None

                self.pppoe = Dhcpv6.Interfaces.Interface.Pppoe()
                self.pppoe.parent = self
                self._children_name_map["pppoe"] = "pppoe"
                self._children_yang_names.add("pppoe")

                self.proxy = Dhcpv6.Interfaces.Interface.Proxy()
                self.proxy.parent = self
                self._children_name_map["proxy"] = "proxy"
                self._children_yang_names.add("proxy")

                self.base = Dhcpv6.Interfaces.Interface.Base()
                self.base.parent = self
                self._children_name_map["base"] = "base"
                self._children_yang_names.add("base")

                self.server = Dhcpv6.Interfaces.Interface.Server()
                self.server.parent = self
                self._children_name_map["server"] = "server"
                self._children_yang_names.add("server")

                self.relay = Dhcpv6.Interfaces.Interface.Relay()
                self.relay.parent = self
                self._children_name_map["relay"] = "relay"
                self._children_yang_names.add("relay")
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Dhcpv6.Interfaces.Interface, ['interface_name'], name, value)


            class Pppoe(Entity):
                """
                PPPoE subscriber interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\: str
                
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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile', YLeaf(YType.str, 'profile')),
                    ])
                    self.profile = None
                    self._segment_path = lambda: "pppoe"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Pppoe, ['profile'], name, value)


            class Proxy(Entity):
                """
                Assign a proxy profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\: str
                
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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile', YLeaf(YType.str, 'profile')),
                    ])
                    self.profile = None
                    self._segment_path = lambda: "proxy"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Proxy, ['profile'], name, value)


            class Base(Entity):
                """
                Assign a base profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\: str
                
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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile', YLeaf(YType.str, 'profile')),
                    ])
                    self.profile = None
                    self._segment_path = lambda: "base"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Base, ['profile'], name, value)


            class Server(Entity):
                """
                Assign a server profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\: str
                
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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile', YLeaf(YType.str, 'profile')),
                    ])
                    self.profile = None
                    self._segment_path = lambda: "server"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Server, ['profile'], name, value)


            class Relay(Entity):
                """
                Assign a relay profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\: str
                
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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile', YLeaf(YType.str, 'profile')),
                    ])
                    self.profile = None
                    self._segment_path = lambda: "relay"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Relay, ['profile'], name, value)

    def clone_ptr(self):
        self._top_entity = Dhcpv6()
        return self._top_entity

