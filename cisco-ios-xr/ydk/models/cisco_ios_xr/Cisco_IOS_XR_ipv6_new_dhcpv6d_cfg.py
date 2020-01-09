""" Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-new\-dhcpv6d package configuration.

This module contains definitions
for the following management objects\:
  dhcpv6\: None

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



class Action(Enum):
    """
    Action (Enum Class)

    Action

    .. data:: allow = 0

    	Allow vendor specific DHCP Solicit

    .. data:: drop = 1

    	Drop vendor specific DHCP Solicit

    """

    allow = Enum.YLeaf(0, "allow")

    drop = Enum.YLeaf(1, "drop")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
        return meta._meta_table['Action']


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

    .. data:: received_nodefault = 3

    	No default Interface ID

    """

    local = Enum.YLeaf(0, "local")

    received = Enum.YLeaf(1, "received")

    pppoe = Enum.YLeaf(2, "pppoe")

    received_nodefault = Enum.YLeaf(3, "received-nodefault")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
        return meta._meta_table['Insert']


class Ipv6dhcpDefaultMode(Enum):
    """
    Ipv6dhcpDefaultMode (Enum Class)

    Ipv6dhcp default mode

    .. data:: server = 1

    	Specify mode-class based Server option

    """

    server = Enum.YLeaf(1, "server")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
        return meta._meta_table['Ipv6dhcpDefaultMode']


class Ipv6dhcpMode(Enum):
    """
    Ipv6dhcpMode (Enum Class)

    Ipv6dhcp mode

    .. data:: server = 1

    	Specify mode-class based Server option

    .. data:: proxy = 2

    	Specify mode-class based Proxy option

    """

    server = Enum.YLeaf(1, "server")

    proxy = Enum.YLeaf(2, "proxy")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
        return meta._meta_table['Ipv6dhcpMode']


class LinkLayerAddr(Enum):
    """
    LinkLayerAddr (Enum Class)

    Link layer addr

    .. data:: set = 4

    	Insert Received LinkLayerAddr Value from SADB

    """

    set = Enum.YLeaf(4, "set")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
        return meta._meta_table['LinkLayerAddr']


class SubscriberId(Enum):
    """
    SubscriberId (Enum Class)

    Subscriber id

    .. data:: pppoe = 3

    	Insert Received Subscriber-ID Value from SADB

    """

    pppoe = Enum.YLeaf(3, "pppoe")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
        return meta._meta_table['SubscriberId']



class Dhcpv6(_Entity_):
    """
    None
    
    .. attribute:: database
    
    	Enable DHCP binding database storage to file system
    	**type**\:  :py:class:`Database <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Database>`
    
    .. attribute:: rate_limit_solicit
    
    	Rate limit ingress packets
    	**type**\:  :py:class:`RateLimitSolicit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.RateLimitSolicit>`
    
    .. attribute:: profiles
    
    	Table of Profile
    	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles>`
    
    .. attribute:: interfaces
    
    	Table of Interface
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces>`
    
    .. attribute:: inner_cos
    
    	Inner cos values for DHCPv6 packets to wards clients
    	**type**\: int
    
    	**range:** 0..7
    
    .. attribute:: enable
    
    	Enable None. Deletion of this object also causes deletion of all associated objects under DHCPv6
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    	**mandatory**\: True
    
    .. attribute:: allow_duid_change
    
    	For BNG session, allow duid change for a client MAC
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: outer_cos
    
    	Configure outer cos values for DHCPv6 packet to wards client
    	**type**\: int
    
    	**range:** 0..7
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv6-new-dhcpv6d-cfg'
    _revision = '2017-09-12'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Dhcpv6, self).__init__()
        self._top_entity = None

        self.yang_name = "dhcpv6"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("database", ("database", Dhcpv6.Database)), ("rate-limit-solicit", ("rate_limit_solicit", Dhcpv6.RateLimitSolicit)), ("profiles", ("profiles", Dhcpv6.Profiles)), ("interfaces", ("interfaces", Dhcpv6.Interfaces))])
        self.is_presence_container = True
        self._leafs = OrderedDict([
            ('inner_cos', (YLeaf(YType.uint32, 'inner-cos'), ['int'])),
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ('allow_duid_change', (YLeaf(YType.empty, 'allow-duid-change'), ['Empty'])),
            ('outer_cos', (YLeaf(YType.uint32, 'outer-cos'), ['int'])),
        ])
        self.inner_cos = None
        self.enable = None
        self.allow_duid_change = None
        self.outer_cos = None

        self.database = Dhcpv6.Database()
        self.database.parent = self
        self._children_name_map["database"] = "database"

        self.rate_limit_solicit = Dhcpv6.RateLimitSolicit()
        self.rate_limit_solicit.parent = self
        self._children_name_map["rate_limit_solicit"] = "rate-limit-solicit"

        self.profiles = Dhcpv6.Profiles()
        self.profiles.parent = self
        self._children_name_map["profiles"] = "profiles"

        self.interfaces = Dhcpv6.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Dhcpv6, ['inner_cos', 'enable', 'allow_duid_change', 'outer_cos'], name, value)


    class Database(_Entity_):
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
        _revision = '2017-09-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Dhcpv6.Database, self).__init__()

            self.yang_name = "database"
            self.yang_parent_name = "dhcpv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('proxy', (YLeaf(YType.empty, 'proxy'), ['Empty'])),
                ('server', (YLeaf(YType.empty, 'server'), ['Empty'])),
                ('relay', (YLeaf(YType.empty, 'relay'), ['Empty'])),
                ('full_write_interval', (YLeaf(YType.uint32, 'full-write-interval'), ['int'])),
                ('incremental_write_interval', (YLeaf(YType.uint32, 'incremental-write-interval'), ['int'])),
            ])
            self.proxy = None
            self.server = None
            self.relay = None
            self.full_write_interval = None
            self.incremental_write_interval = None
            self._segment_path = lambda: "database"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Dhcpv6.Database, ['proxy', 'server', 'relay', 'full_write_interval', 'incremental_write_interval'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
            return meta._meta_table['Dhcpv6.Database']['meta_info']


    class RateLimitSolicit(_Entity_):
        """
        Rate limit ingress packets
        
        .. attribute:: num_period
        
        	Period in msec (Default\: 200 msec)
        	**type**\: int
        
        	**range:** 1..1000
        
        .. attribute:: num_solicit
        
        	Number of Solicit packets (Default\: 100, 0\: No limit)
        	**type**\: int
        
        	**range:** 0..1000
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2017-09-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Dhcpv6.RateLimitSolicit, self).__init__()

            self.yang_name = "rate-limit-solicit"
            self.yang_parent_name = "dhcpv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('num_period', (YLeaf(YType.uint32, 'num-period'), ['int'])),
                ('num_solicit', (YLeaf(YType.uint32, 'num-solicit'), ['int'])),
            ])
            self.num_period = None
            self.num_solicit = None
            self._segment_path = lambda: "rate-limit-solicit"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Dhcpv6.RateLimitSolicit, ['num_period', 'num_solicit'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
            return meta._meta_table['Dhcpv6.RateLimitSolicit']['meta_info']


    class Profiles(_Entity_):
        """
        Table of Profile
        
        .. attribute:: profile
        
        	None
        	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2017-09-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Dhcpv6.Profiles, self).__init__()

            self.yang_name = "profiles"
            self.yang_parent_name = "dhcpv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("profile", ("profile", Dhcpv6.Profiles.Profile))])
            self._leafs = OrderedDict()

            self.profile = YList(self)
            self._segment_path = lambda: "profiles"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Dhcpv6.Profiles, [], name, value)


        class Profile(_Entity_):
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
            _revision = '2017-09-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Dhcpv6.Profiles.Profile, self).__init__()

                self.yang_name = "profile"
                self.yang_parent_name = "profiles"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['profile_name']
                self._child_classes = OrderedDict([("relay", ("relay", Dhcpv6.Profiles.Profile.Relay)), ("base", ("base", Dhcpv6.Profiles.Profile.Base)), ("proxy", ("proxy", Dhcpv6.Profiles.Profile.Proxy)), ("server", ("server", Dhcpv6.Profiles.Profile.Server))])
                self._leafs = OrderedDict([
                    ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                ])
                self.profile_name = None

                self.relay = None
                self._children_name_map["relay"] = "relay"

                self.base = None
                self._children_name_map["base"] = "base"

                self.proxy = None
                self._children_name_map["proxy"] = "proxy"

                self.server = None
                self._children_name_map["server"] = "server"
                self._segment_path = lambda: "profile" + "[profile-name='" + str(self.profile_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/profiles/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Dhcpv6.Profiles.Profile, ['profile_name'], name, value)


            class Relay(_Entity_):
                """
                None
                
                .. attribute:: helper_addresses
                
                	Table of HelperAddress
                	**type**\:  :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay.HelperAddresses>`
                
                .. attribute:: option
                
                	Specify relay option configuration
                	**type**\:  :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay.Option>`
                
                .. attribute:: link_address
                
                	IPv6 address to be filled in link\-address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: src_intf_name
                
                	Relay profile Source Interface Name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Relay
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: iana_route_add
                
                	Enable route addition for IANA
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: relay_route_add_disable
                
                	RouteDisable
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-09-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Dhcpv6.Profiles.Profile.Relay, self).__init__()

                    self.yang_name = "relay"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("helper-addresses", ("helper_addresses", Dhcpv6.Profiles.Profile.Relay.HelperAddresses)), ("option", ("option", Dhcpv6.Profiles.Profile.Relay.Option))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('link_address', (YLeaf(YType.str, 'link-address'), ['str','str'])),
                        ('src_intf_name', (YLeaf(YType.str, 'src-intf-name'), ['str'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ('iana_route_add', (YLeaf(YType.empty, 'iana-route-add'), ['Empty'])),
                        ('relay_route_add_disable', (YLeaf(YType.empty, 'relay-route-add-disable'), ['Empty'])),
                    ])
                    self.link_address = None
                    self.src_intf_name = None
                    self.enable = None
                    self.iana_route_add = None
                    self.relay_route_add_disable = None

                    self.helper_addresses = Dhcpv6.Profiles.Profile.Relay.HelperAddresses()
                    self.helper_addresses.parent = self
                    self._children_name_map["helper_addresses"] = "helper-addresses"

                    self.option = Dhcpv6.Profiles.Profile.Relay.Option()
                    self.option.parent = self
                    self._children_name_map["option"] = "option"
                    self._segment_path = lambda: "relay"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Profiles.Profile.Relay, ['link_address', 'src_intf_name', 'enable', 'iana_route_add', 'relay_route_add_disable'], name, value)


                class HelperAddresses(_Entity_):
                    """
                    Table of HelperAddress
                    
                    .. attribute:: helper_address
                    
                    	Specify the server helper address
                    	**type**\: list of  		 :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Relay.HelperAddresses, self).__init__()

                        self.yang_name = "helper-addresses"
                        self.yang_parent_name = "relay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("helper-address", ("helper_address", Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress))])
                        self._leafs = OrderedDict()

                        self.helper_address = YList(self)
                        self._segment_path = lambda: "helper-addresses"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Relay.HelperAddresses, [], name, value)


                    class HelperAddress(_Entity_):
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
                        
                        .. attribute:: enable
                        
                        	Enable
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: src_intf_name
                        
                        	Helper\-address Specific Source Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-09-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress, self).__init__()

                            self.yang_name = "helper-address"
                            self.yang_parent_name = "helper-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vrf_name','helper_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ('helper_address', (YLeaf(YType.str, 'helper-address'), ['str'])),
                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                ('src_intf_name', (YLeaf(YType.str, 'src-intf-name'), ['str'])),
                            ])
                            self.vrf_name = None
                            self.helper_address = None
                            self.enable = None
                            self.src_intf_name = None
                            self._segment_path = lambda: "helper-address" + "[vrf-name='" + str(self.vrf_name) + "']" + "[helper-address='" + str(self.helper_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress, ['vrf_name', 'helper_address', 'enable', 'src_intf_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Relay.HelperAddresses']['meta_info']


                class Option(_Entity_):
                    """
                    Specify relay option configuration
                    
                    .. attribute:: remote_id
                    
                    	Enter remote\-id value
                    	**type**\: str
                    
                    	**length:** 1..256
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Relay.Option, self).__init__()

                        self.yang_name = "option"
                        self.yang_parent_name = "relay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str'])),
                        ])
                        self.remote_id = None
                        self._segment_path = lambda: "option"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Relay.Option, ['remote_id'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Relay.Option']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Profiles.Profile.Relay']['meta_info']


            class Base(_Entity_):
                """
                None
                
                .. attribute:: dhcpv6_to_aaa
                
                	Enable to provide the list of options need to send to aaa
                	**type**\:  :py:class:`Dhcpv6ToAaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa>`
                
                .. attribute:: match_default
                
                	Default match option
                	**type**\:  :py:class:`MatchDefault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.MatchDefault>`
                
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
                _revision = '2017-09-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Dhcpv6.Profiles.Profile.Base, self).__init__()

                    self.yang_name = "base"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("dhcpv6-to-aaa", ("dhcpv6_to_aaa", Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa)), ("match-default", ("match_default", Dhcpv6.Profiles.Profile.Base.MatchDefault)), ("match", ("match", Dhcpv6.Profiles.Profile.Base.Match))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.enable = None

                    self.dhcpv6_to_aaa = Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa()
                    self.dhcpv6_to_aaa.parent = self
                    self._children_name_map["dhcpv6_to_aaa"] = "dhcpv6-to-aaa"

                    self.match_default = Dhcpv6.Profiles.Profile.Base.MatchDefault()
                    self.match_default.parent = self
                    self._children_name_map["match_default"] = "match-default"

                    self.match = Dhcpv6.Profiles.Profile.Base.Match()
                    self.match.parent = self
                    self._children_name_map["match"] = "match"
                    self._segment_path = lambda: "base"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Profiles.Profile.Base, ['enable'], name, value)


                class Dhcpv6ToAaa(_Entity_):
                    """
                    Enable to provide the list of options need to
                    send to aaa
                    
                    .. attribute:: base_option
                    
                    	option type
                    	**type**\:  :py:class:`BaseOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa.BaseOption>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa, self).__init__()

                        self.yang_name = "dhcpv6-to-aaa"
                        self.yang_parent_name = "base"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("base-option", ("base_option", Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa.BaseOption))])
                        self._leafs = OrderedDict()

                        self.base_option = Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa.BaseOption()
                        self.base_option.parent = self
                        self._children_name_map["base_option"] = "base-option"
                        self._segment_path = lambda: "dhcpv6-to-aaa"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa, [], name, value)


                    class BaseOption(_Entity_):
                        """
                        option type
                        
                        .. attribute:: list
                        
                        	List of options
                        	**type**\:  :py:class:`List <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa.BaseOption.List>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-09-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa.BaseOption, self).__init__()

                            self.yang_name = "base-option"
                            self.yang_parent_name = "dhcpv6-to-aaa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("list", ("list", Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa.BaseOption.List))])
                            self._leafs = OrderedDict()

                            self.list = Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa.BaseOption.List()
                            self.list.parent = self
                            self._children_name_map["list"] = "list"
                            self._segment_path = lambda: "base-option"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa.BaseOption, [], name, value)


                        class List(_Entity_):
                            """
                            List of options
                            
                            .. attribute:: option_all
                            
                            	Set constant integer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: option_number
                            
                            	Option number
                            	**type**\: list of int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-09-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa.BaseOption.List, self).__init__()

                                self.yang_name = "list"
                                self.yang_parent_name = "base-option"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('option_all', (YLeaf(YType.uint32, 'option-all'), ['int'])),
                                    ('option_number', (YLeafList(YType.uint32, 'option-number'), ['int'])),
                                ])
                                self.option_all = None
                                self.option_number = []
                                self._segment_path = lambda: "list"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa.BaseOption.List, ['option_all', 'option_number'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa.BaseOption.List']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa.BaseOption']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Base.Dhcpv6ToAaa']['meta_info']


                class MatchDefault(_Entity_):
                    """
                    Default match option
                    
                    .. attribute:: profile
                    
                    	None
                    	**type**\:  :py:class:`Profile_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.MatchDefault.Profile_>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Base.MatchDefault, self).__init__()

                        self.yang_name = "match-default"
                        self.yang_parent_name = "base"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("profile", ("profile", Dhcpv6.Profiles.Profile.Base.MatchDefault.Profile_))])
                        self._leafs = OrderedDict()

                        self.profile = Dhcpv6.Profiles.Profile.Base.MatchDefault.Profile_()
                        self.profile.parent = self
                        self._children_name_map["profile"] = "profile"
                        self._segment_path = lambda: "match-default"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Base.MatchDefault, [], name, value)


                    class Profile_(_Entity_):
                        """
                        None
                        
                        .. attribute:: profile_name
                        
                        	Profile name
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: default_mode
                        
                        	Set constant integer
                        	**type**\:  :py:class:`Ipv6dhcpDefaultMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Ipv6dhcpDefaultMode>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-09-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Dhcpv6.Profiles.Profile.Base.MatchDefault.Profile_, self).__init__()

                            self.yang_name = "profile"
                            self.yang_parent_name = "match-default"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                ('default_mode', (YLeaf(YType.enumeration, 'default-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Ipv6dhcpDefaultMode', '')])),
                            ])
                            self.profile_name = None
                            self.default_mode = None
                            self._segment_path = lambda: "profile"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Base.MatchDefault.Profile_, ['profile_name', 'default_mode'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Base.MatchDefault.Profile_']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Base.MatchDefault']['meta_info']


                class Match(_Entity_):
                    """
                    Enter match option
                    
                    .. attribute:: mode_classes
                    
                    	Table of ModeClass
                    	**type**\:  :py:class:`ModeClasses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match.ModeClasses>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Base.Match, self).__init__()

                        self.yang_name = "match"
                        self.yang_parent_name = "base"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("mode-classes", ("mode_classes", Dhcpv6.Profiles.Profile.Base.Match.ModeClasses))])
                        self._leafs = OrderedDict()

                        self.mode_classes = Dhcpv6.Profiles.Profile.Base.Match.ModeClasses()
                        self.mode_classes.parent = self
                        self._children_name_map["mode_classes"] = "mode-classes"
                        self._segment_path = lambda: "match"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Match, [], name, value)


                    class ModeClasses(_Entity_):
                        """
                        Table of ModeClass
                        
                        .. attribute:: mode_class
                        
                        	Specify PPP/IPoE class option
                        	**type**\: list of  		 :py:class:`ModeClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-09-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses, self).__init__()

                            self.yang_name = "mode-classes"
                            self.yang_parent_name = "match"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("mode-class", ("mode_class", Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass))])
                            self._leafs = OrderedDict()

                            self.mode_class = YList(self)
                            self._segment_path = lambda: "mode-classes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses, [], name, value)


                        class ModeClass(_Entity_):
                            """
                            Specify PPP/IPoE class option
                            
                            .. attribute:: class_name  (key)
                            
                            	Class name
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            .. attribute:: profile
                            
                            	Enter proxy or server profile
                            	**type**\:  :py:class:`Profile_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile_>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-09-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass, self).__init__()

                                self.yang_name = "mode-class"
                                self.yang_parent_name = "mode-classes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['class_name']
                                self._child_classes = OrderedDict([("profile", ("profile", Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile_))])
                                self._leafs = OrderedDict([
                                    ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                ])
                                self.class_name = None

                                self.profile = Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile_()
                                self.profile.parent = self
                                self._children_name_map["profile"] = "profile"
                                self._segment_path = lambda: "mode-class" + "[class-name='" + str(self.class_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass, ['class_name'], name, value)


                            class Profile_(_Entity_):
                                """
                                Enter proxy or server profile
                                
                                .. attribute:: profile_name
                                
                                	Profile name
                                	**type**\: str
                                
                                	**length:** 1..64
                                
                                .. attribute:: mode
                                
                                	Set constant integer
                                	**type**\:  :py:class:`Ipv6dhcpMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Ipv6dhcpMode>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2017-09-12'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile_, self).__init__()

                                    self.yang_name = "profile"
                                    self.yang_parent_name = "mode-class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                        ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Ipv6dhcpMode', '')])),
                                    ])
                                    self.profile_name = None
                                    self.mode = None
                                    self._segment_path = lambda: "profile"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile_, ['profile_name', 'mode'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                    return meta._meta_table['Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile_']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Base.Match.ModeClasses']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Base.Match']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Profiles.Profile.Base']['meta_info']


            class Proxy(_Entity_):
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
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Proxy
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-09-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Dhcpv6.Profiles.Profile.Proxy, self).__init__()

                    self.yang_name = "proxy"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interfaces", ("interfaces", Dhcpv6.Profiles.Profile.Proxy.Interfaces)), ("relay", ("relay", Dhcpv6.Profiles.Profile.Proxy.Relay)), ("vrfs", ("vrfs", Dhcpv6.Profiles.Profile.Proxy.Vrfs)), ("authentication", ("authentication", Dhcpv6.Profiles.Profile.Proxy.Authentication)), ("classes", ("classes", Dhcpv6.Profiles.Profile.Proxy.Classes)), ("sessions", ("sessions", Dhcpv6.Profiles.Profile.Proxy.Sessions))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('linkaddress_from_ra_enable', (YLeaf(YType.empty, 'linkaddress-from-ra-enable'), ['Empty'])),
                        ('route_add_disable', (YLeaf(YType.empty, 'route-add-disable'), ['Empty'])),
                        ('link_address', (YLeaf(YType.str, 'link-address'), ['str','str'])),
                        ('src_intf_name', (YLeaf(YType.str, 'src-intf-name'), ['str'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.linkaddress_from_ra_enable = None
                    self.route_add_disable = None
                    self.link_address = None
                    self.src_intf_name = None
                    self.enable = None

                    self.interfaces = Dhcpv6.Profiles.Profile.Proxy.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"

                    self.relay = Dhcpv6.Profiles.Profile.Proxy.Relay()
                    self.relay.parent = self
                    self._children_name_map["relay"] = "relay"

                    self.vrfs = Dhcpv6.Profiles.Profile.Proxy.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"

                    self.authentication = Dhcpv6.Profiles.Profile.Proxy.Authentication()
                    self.authentication.parent = self
                    self._children_name_map["authentication"] = "authentication"

                    self.classes = Dhcpv6.Profiles.Profile.Proxy.Classes()
                    self.classes.parent = self
                    self._children_name_map["classes"] = "classes"

                    self.sessions = Dhcpv6.Profiles.Profile.Proxy.Sessions()
                    self.sessions.parent = self
                    self._children_name_map["sessions"] = "sessions"
                    self._segment_path = lambda: "proxy"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy, ['linkaddress_from_ra_enable', 'route_add_disable', 'link_address', 'src_intf_name', 'enable'], name, value)


                class Interfaces(_Entity_):
                    """
                    Table of Interface
                    
                    .. attribute:: interface
                    
                    	None
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Proxy.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface", ("interface", Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Interfaces, [], name, value)


                    class Interface(_Entity_):
                        """
                        None
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface to configure
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: interface_id
                        
                        	Physical interface ID
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-09-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('interface_id', (YLeaf(YType.str, 'interface-id'), ['str'])),
                            ])
                            self.interface_name = None
                            self.interface_id = None
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface, ['interface_name', 'interface_id'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Interfaces']['meta_info']


                class Relay(_Entity_):
                    """
                    Specify relay configuration
                    
                    .. attribute:: option
                    
                    	Specify relay option configuration
                    	**type**\:  :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Relay.Option>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Proxy.Relay, self).__init__()

                        self.yang_name = "relay"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("option", ("option", Dhcpv6.Profiles.Profile.Proxy.Relay.Option))])
                        self._leafs = OrderedDict()

                        self.option = Dhcpv6.Profiles.Profile.Proxy.Relay.Option()
                        self.option.parent = self
                        self._children_name_map["option"] = "option"
                        self._segment_path = lambda: "relay"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Relay, [], name, value)


                    class Option(_Entity_):
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
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_id
                        
                        	Enter remote\-id value
                        	**type**\: str
                        
                        	**length:** 1..256
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-09-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Dhcpv6.Profiles.Profile.Proxy.Relay.Option, self).__init__()

                            self.yang_name = "option"
                            self.yang_parent_name = "relay"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface-id", ("interface_id", Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId))])
                            self._leafs = OrderedDict([
                                ('subscriber_id', (YLeaf(YType.enumeration, 'subscriber-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'SubscriberId', '')])),
                                ('link_layer_addr', (YLeaf(YType.enumeration, 'link-layer-addr'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'LinkLayerAddr', '')])),
                                ('remote_i_dreceived', (YLeaf(YType.uint32, 'remote-i-dreceived'), ['int'])),
                                ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str'])),
                            ])
                            self.subscriber_id = None
                            self.link_layer_addr = None
                            self.remote_i_dreceived = None
                            self.remote_id = None

                            self.interface_id = Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId()
                            self.interface_id.parent = self
                            self._children_name_map["interface_id"] = "interface-id"
                            self._segment_path = lambda: "option"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Relay.Option, ['subscriber_id', 'link_layer_addr', 'remote_i_dreceived', 'remote_id'], name, value)


                        class InterfaceId(_Entity_):
                            """
                            Interface Id option
                            
                            .. attribute:: insert
                            
                            	Configure InterfaceID insert type
                            	**type**\:  :py:class:`Insert <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Insert>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-09-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId, self).__init__()

                                self.yang_name = "interface-id"
                                self.yang_parent_name = "option"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('insert', (YLeaf(YType.enumeration, 'insert'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Insert', '')])),
                                ])
                                self.insert = None
                                self._segment_path = lambda: "interface-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId, ['insert'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay.Option']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay']['meta_info']


                class Vrfs(_Entity_):
                    """
                    VRF related configuration
                    
                    .. attribute:: vrf
                    
                    	IPv6 DHCP proxy VRF name
                    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Proxy.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("vrf", ("vrf", Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf))])
                        self._leafs = OrderedDict()

                        self.vrf = YList(self)
                        self._segment_path = lambda: "vrfs"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Vrfs, [], name, value)


                    class Vrf(_Entity_):
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
                        _revision = '2017-09-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vrf_name']
                            self._child_classes = OrderedDict([("helper-addresses", ("helper_addresses", Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses))])
                            self._leafs = OrderedDict([
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ])
                            self.vrf_name = None

                            self.helper_addresses = Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses()
                            self.helper_addresses.parent = self
                            self._children_name_map["helper_addresses"] = "helper-addresses"
                            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf, ['vrf_name'], name, value)


                        class HelperAddresses(_Entity_):
                            """
                            Table of HelperAddress
                            
                            .. attribute:: helper_address
                            
                            	DHCPv6 Helper Address
                            	**type**\: list of  		 :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-09-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses, self).__init__()

                                self.yang_name = "helper-addresses"
                                self.yang_parent_name = "vrf"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("helper-address", ("helper_address", Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress))])
                                self._leafs = OrderedDict()

                                self.helper_address = YList(self)
                                self._segment_path = lambda: "helper-addresses"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses, [], name, value)


                            class HelperAddress(_Entity_):
                                """
                                DHCPv6 Helper Address
                                
                                .. attribute:: helper_address  (key)
                                
                                	DHCPv6 Helper Address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: out_interface
                                
                                	DHCPv6 HelperAddress Specific Output Interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: any_out_interface
                                
                                	DHCPv6 HelperAddress Output Interface
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2017-09-12'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__init__()

                                    self.yang_name = "helper-address"
                                    self.yang_parent_name = "helper-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['helper_address']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('helper_address', (YLeaf(YType.str, 'helper-address'), ['str'])),
                                        ('out_interface', (YLeaf(YType.str, 'out-interface'), ['str'])),
                                        ('any_out_interface', (YLeaf(YType.empty, 'any-out-interface'), ['Empty'])),
                                    ])
                                    self.helper_address = None
                                    self.out_interface = None
                                    self.any_out_interface = None
                                    self._segment_path = lambda: "helper-address" + "[helper-address='" + str(self.helper_address) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, ['helper_address', 'out_interface', 'any_out_interface'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                    return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs']['meta_info']


                class Authentication(_Entity_):
                    """
                    Authentication username format
                    
                    .. attribute:: username
                    
                    	Set username as DUID
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Proxy.Authentication, self).__init__()

                        self.yang_name = "authentication"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('username', (YLeaf(YType.empty, 'username'), ['Empty'])),
                        ])
                        self.username = None
                        self._segment_path = lambda: "authentication"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Authentication, ['username'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Authentication']['meta_info']


                class Classes(_Entity_):
                    """
                    Table of Class
                    
                    .. attribute:: class_
                    
                    	None
                    	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes.Class>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Proxy.Classes, self).__init__()

                        self.yang_name = "classes"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("class", ("class_", Dhcpv6.Profiles.Profile.Proxy.Classes.Class))])
                        self._leafs = OrderedDict()

                        self.class_ = YList(self)
                        self._segment_path = lambda: "classes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Classes, [], name, value)


                    class Class(_Entity_):
                        """
                        None
                        
                        .. attribute:: class_name  (key)
                        
                        	Class name
                        	**type**\: str
                        
                        	**length:** 1..64
                        
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
                        _revision = '2017-09-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class, self).__init__()

                            self.yang_name = "class"
                            self.yang_parent_name = "classes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['class_name']
                            self._child_classes = OrderedDict([("helper-addresses", ("helper_addresses", Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses))])
                            self._leafs = OrderedDict([
                                ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                ('link_address', (YLeaf(YType.str, 'link-address'), ['str','str'])),
                            ])
                            self.class_name = None
                            self.link_address = None

                            self.helper_addresses = Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses()
                            self.helper_addresses.parent = self
                            self._children_name_map["helper_addresses"] = "helper-addresses"
                            self._segment_path = lambda: "class" + "[class-name='" + str(self.class_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Classes.Class, ['class_name', 'link_address'], name, value)


                        class HelperAddresses(_Entity_):
                            """
                            Table of HelperAddress
                            
                            .. attribute:: helper_address
                            
                            	Specify the server helper address
                            	**type**\: list of  		 :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-09-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses, self).__init__()

                                self.yang_name = "helper-addresses"
                                self.yang_parent_name = "class"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("helper-address", ("helper_address", Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress))])
                                self._leafs = OrderedDict()

                                self.helper_address = YList(self)
                                self._segment_path = lambda: "helper-addresses"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses, [], name, value)


                            class HelperAddress(_Entity_):
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
                                _revision = '2017-09-12'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress, self).__init__()

                                    self.yang_name = "helper-address"
                                    self.yang_parent_name = "helper-addresses"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['vrf_name','helper_address']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                        ('helper_address', (YLeaf(YType.str, 'helper-address'), ['str'])),
                                    ])
                                    self.vrf_name = None
                                    self.helper_address = None
                                    self._segment_path = lambda: "helper-address" + "[vrf-name='" + str(self.vrf_name) + "']" + "[helper-address='" + str(self.helper_address) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress, ['vrf_name', 'helper_address'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                    return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes']['meta_info']


                class Sessions(_Entity_):
                    """
                    Change sessions configuration
                    
                    .. attribute:: mac
                    
                    	Throttle DHCP sessions based on MAC address
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Proxy.Sessions, self).__init__()

                        self.yang_name = "sessions"
                        self.yang_parent_name = "proxy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("mac", ("mac", Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac))])
                        self._leafs = OrderedDict()

                        self.mac = Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac()
                        self.mac.parent = self
                        self._children_name_map["mac"] = "mac"
                        self._segment_path = lambda: "sessions"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Sessions, [], name, value)


                    class Mac(_Entity_):
                        """
                        Throttle DHCP sessions based on MAC address
                        
                        .. attribute:: throttle
                        
                        	Throttle DHCP sessions from any one MAC address
                        	**type**\:  :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-09-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac, self).__init__()

                            self.yang_name = "mac"
                            self.yang_parent_name = "sessions"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("throttle", ("throttle", Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle))])
                            self._leafs = OrderedDict()

                            self.throttle = Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle()
                            self.throttle.parent = self
                            self._children_name_map["throttle"] = "throttle"
                            self._segment_path = lambda: "mac"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac, [], name, value)


                        class Throttle(_Entity_):
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
                            _revision = '2017-09-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle, self).__init__()

                                self.yang_name = "throttle"
                                self.yang_parent_name = "mac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                                    ('request', (YLeaf(YType.uint32, 'request'), ['int'])),
                                    ('block', (YLeaf(YType.uint32, 'block'), ['int'])),
                                ])
                                self.limit = None
                                self.request = None
                                self.block = None
                                self._segment_path = lambda: "throttle"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle, ['limit', 'request', 'block'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy']['meta_info']


            class Server(_Entity_):
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
                
                .. attribute:: dhcpv6duid
                
                	Client DUID
                	**type**\:  :py:class:`Dhcpv6duid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Dhcpv6duid>`
                
                .. attribute:: aaa_server
                
                	Enable aaa dhcpv6 option force\-insert
                	**type**\:  :py:class:`AaaServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.AaaServer>`
                
                .. attribute:: options
                
                	DHCPv6 match
                	**type**\:  :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Options>`
                
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
                _revision = '2017-09-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Dhcpv6.Profiles.Profile.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sessions", ("sessions", Dhcpv6.Profiles.Profile.Server.Sessions)), ("dns-servers", ("dns_servers", Dhcpv6.Profiles.Profile.Server.DnsServers)), ("classes", ("classes", Dhcpv6.Profiles.Profile.Server.Classes)), ("lease", ("lease", Dhcpv6.Profiles.Profile.Server.Lease)), ("dhcpv6duid", ("dhcpv6duid", Dhcpv6.Profiles.Profile.Server.Dhcpv6duid)), ("aaa-server", ("aaa_server", Dhcpv6.Profiles.Profile.Server.AaaServer)), ("options", ("options", Dhcpv6.Profiles.Profile.Server.Options)), ("dhcpv6-options", ("dhcpv6_options", Dhcpv6.Profiles.Profile.Server.Dhcpv6Options))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('address_pool', (YLeaf(YType.str, 'address-pool'), ['str'])),
                        ('aftr_name', (YLeaf(YType.str, 'aftr-name'), ['str'])),
                        ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                        ('preference', (YLeaf(YType.uint32, 'preference'), ['int'])),
                        ('rapid_commit', (YLeaf(YType.empty, 'rapid-commit'), ['Empty'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ('prefix_pool', (YLeaf(YType.str, 'prefix-pool'), ['str'])),
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

                    self.dns_servers = Dhcpv6.Profiles.Profile.Server.DnsServers()
                    self.dns_servers.parent = self
                    self._children_name_map["dns_servers"] = "dns-servers"

                    self.classes = Dhcpv6.Profiles.Profile.Server.Classes()
                    self.classes.parent = self
                    self._children_name_map["classes"] = "classes"

                    self.lease = Dhcpv6.Profiles.Profile.Server.Lease()
                    self.lease.parent = self
                    self._children_name_map["lease"] = "lease"

                    self.dhcpv6duid = Dhcpv6.Profiles.Profile.Server.Dhcpv6duid()
                    self.dhcpv6duid.parent = self
                    self._children_name_map["dhcpv6duid"] = "dhcpv6duid"

                    self.aaa_server = Dhcpv6.Profiles.Profile.Server.AaaServer()
                    self.aaa_server.parent = self
                    self._children_name_map["aaa_server"] = "aaa-server"

                    self.options = Dhcpv6.Profiles.Profile.Server.Options()
                    self.options.parent = self
                    self._children_name_map["options"] = "options"

                    self.dhcpv6_options = Dhcpv6.Profiles.Profile.Server.Dhcpv6Options()
                    self.dhcpv6_options.parent = self
                    self._children_name_map["dhcpv6_options"] = "dhcpv6-options"
                    self._segment_path = lambda: "server"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Profiles.Profile.Server, ['address_pool', 'aftr_name', 'domain_name', 'preference', 'rapid_commit', 'enable', 'prefix_pool'], name, value)


                class Sessions(_Entity_):
                    """
                    Change sessions configuration
                    
                    .. attribute:: mac
                    
                    	Throttle DHCP sessions based on MAC address
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Sessions.Mac>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Server.Sessions, self).__init__()

                        self.yang_name = "sessions"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("mac", ("mac", Dhcpv6.Profiles.Profile.Server.Sessions.Mac))])
                        self._leafs = OrderedDict()

                        self.mac = Dhcpv6.Profiles.Profile.Server.Sessions.Mac()
                        self.mac.parent = self
                        self._children_name_map["mac"] = "mac"
                        self._segment_path = lambda: "sessions"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Sessions, [], name, value)


                    class Mac(_Entity_):
                        """
                        Throttle DHCP sessions based on MAC address
                        
                        .. attribute:: throttle
                        
                        	Throttle DHCP sessions from any one MAC address
                        	**type**\:  :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-09-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Dhcpv6.Profiles.Profile.Server.Sessions.Mac, self).__init__()

                            self.yang_name = "mac"
                            self.yang_parent_name = "sessions"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("throttle", ("throttle", Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle))])
                            self._leafs = OrderedDict()

                            self.throttle = Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle()
                            self.throttle.parent = self
                            self._children_name_map["throttle"] = "throttle"
                            self._segment_path = lambda: "mac"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Sessions.Mac, [], name, value)


                        class Throttle(_Entity_):
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
                            _revision = '2017-09-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle, self).__init__()

                                self.yang_name = "throttle"
                                self.yang_parent_name = "mac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                                    ('request', (YLeaf(YType.uint32, 'request'), ['int'])),
                                    ('block', (YLeaf(YType.uint32, 'block'), ['int'])),
                                ])
                                self.limit = None
                                self.request = None
                                self.block = None
                                self._segment_path = lambda: "throttle"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle, ['limit', 'request', 'block'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Sessions.Mac']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Sessions']['meta_info']


                class DnsServers(_Entity_):
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
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Server.DnsServers, self).__init__()

                        self.yang_name = "dns-servers"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('dns_server', (YLeafList(YType.str, 'dns-server'), ['str','str'])),
                        ])
                        self.dns_server = []
                        self._segment_path = lambda: "dns-servers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Server.DnsServers, ['dns_server'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Server.DnsServers']['meta_info']


                class Classes(_Entity_):
                    """
                    Table of Class
                    
                    .. attribute:: class_
                    
                    	None
                    	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes.Class>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Server.Classes, self).__init__()

                        self.yang_name = "classes"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("class", ("class_", Dhcpv6.Profiles.Profile.Server.Classes.Class))])
                        self._leafs = OrderedDict()

                        self.class_ = YList(self)
                        self._segment_path = lambda: "classes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Classes, [], name, value)


                    class Class(_Entity_):
                        """
                        None
                        
                        .. attribute:: class_name  (key)
                        
                        	class name
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: dns_servers
                        
                        	DNS servers
                        	**type**\:  :py:class:`DnsServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers>`
                        
                        .. attribute:: lease
                        
                        	lease
                        	**type**\:  :py:class:`Lease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes.Class.Lease>`
                        
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
                        _revision = '2017-09-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Dhcpv6.Profiles.Profile.Server.Classes.Class, self).__init__()

                            self.yang_name = "class"
                            self.yang_parent_name = "classes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['class_name']
                            self._child_classes = OrderedDict([("dns-servers", ("dns_servers", Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers)), ("lease", ("lease", Dhcpv6.Profiles.Profile.Server.Classes.Class.Lease))])
                            self._leafs = OrderedDict([
                                ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                ('address_pool', (YLeaf(YType.str, 'address-pool'), ['str'])),
                                ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                                ('preference', (YLeaf(YType.uint32, 'preference'), ['int'])),
                                ('prefix_pool', (YLeaf(YType.str, 'prefix-pool'), ['str'])),
                            ])
                            self.class_name = None
                            self.address_pool = None
                            self.domain_name = None
                            self.preference = None
                            self.prefix_pool = None

                            self.dns_servers = Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers()
                            self.dns_servers.parent = self
                            self._children_name_map["dns_servers"] = "dns-servers"

                            self.lease = Dhcpv6.Profiles.Profile.Server.Classes.Class.Lease()
                            self.lease.parent = self
                            self._children_name_map["lease"] = "lease"
                            self._segment_path = lambda: "class" + "[class-name='" + str(self.class_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Classes.Class, ['class_name', 'address_pool', 'domain_name', 'preference', 'prefix_pool'], name, value)


                        class DnsServers(_Entity_):
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
                            _revision = '2017-09-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers, self).__init__()

                                self.yang_name = "dns-servers"
                                self.yang_parent_name = "class"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dns_server', (YLeafList(YType.str, 'dns-server'), ['str','str'])),
                                ])
                                self.dns_server = []
                                self._segment_path = lambda: "dns-servers"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers, ['dns_server'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers']['meta_info']


                        class Lease(_Entity_):
                            """
                            lease
                            
                            .. attribute:: infinite
                            
                            	Set string
                            	**type**\: str
                            
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
                            
                            	**range:** 0..59
                            
                            	**units**\: minute
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-09-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Dhcpv6.Profiles.Profile.Server.Classes.Class.Lease, self).__init__()

                                self.yang_name = "lease"
                                self.yang_parent_name = "class"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('infinite', (YLeaf(YType.str, 'infinite'), ['str'])),
                                    ('days', (YLeaf(YType.uint32, 'days'), ['int'])),
                                    ('hours', (YLeaf(YType.uint32, 'hours'), ['int'])),
                                    ('minutes', (YLeaf(YType.uint32, 'minutes'), ['int'])),
                                ])
                                self.infinite = None
                                self.days = None
                                self.hours = None
                                self.minutes = None
                                self._segment_path = lambda: "lease"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Classes.Class.Lease, ['infinite', 'days', 'hours', 'minutes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Classes.Class.Lease']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Classes.Class']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Classes']['meta_info']


                class Lease(_Entity_):
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
                    
                    	**range:** 0..59
                    
                    	**units**\: minute
                    
                    .. attribute:: infinite
                    
                    	Set string
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Server.Lease, self).__init__()

                        self.yang_name = "lease"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('days', (YLeaf(YType.uint32, 'days'), ['int'])),
                            ('hours', (YLeaf(YType.uint32, 'hours'), ['int'])),
                            ('minutes', (YLeaf(YType.uint32, 'minutes'), ['int'])),
                            ('infinite', (YLeaf(YType.str, 'infinite'), ['str'])),
                        ])
                        self.days = None
                        self.hours = None
                        self.minutes = None
                        self.infinite = None
                        self._segment_path = lambda: "lease"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Lease, ['days', 'hours', 'minutes', 'infinite'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Lease']['meta_info']


                class Dhcpv6duid(_Entity_):
                    """
                    Client DUID
                    
                    .. attribute:: allowed_type
                    
                    	Type of DUID to be allowed
                    	**type**\: int
                    
                    	**range:** 1..4
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Server.Dhcpv6duid, self).__init__()

                        self.yang_name = "dhcpv6duid"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('allowed_type', (YLeaf(YType.uint32, 'allowed-type'), ['int'])),
                        ])
                        self.allowed_type = None
                        self._segment_path = lambda: "dhcpv6duid"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Dhcpv6duid, ['allowed_type'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Dhcpv6duid']['meta_info']


                class AaaServer(_Entity_):
                    """
                    Enable aaa dhcpv6 option force\-insert
                    
                    .. attribute:: dhcpv6_option
                    
                    	Enable aaa dhcpv6 option force\-insert
                    	**type**\:  :py:class:`Dhcpv6Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.AaaServer.Dhcpv6Option>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Server.AaaServer, self).__init__()

                        self.yang_name = "aaa-server"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("dhcpv6-option", ("dhcpv6_option", Dhcpv6.Profiles.Profile.Server.AaaServer.Dhcpv6Option))])
                        self._leafs = OrderedDict()

                        self.dhcpv6_option = Dhcpv6.Profiles.Profile.Server.AaaServer.Dhcpv6Option()
                        self.dhcpv6_option.parent = self
                        self._children_name_map["dhcpv6_option"] = "dhcpv6-option"
                        self._segment_path = lambda: "aaa-server"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Server.AaaServer, [], name, value)


                    class Dhcpv6Option(_Entity_):
                        """
                        Enable aaa dhcpv6 option force\-insert
                        
                        .. attribute:: force_insert
                        
                        	Enable aaa dhcpv6 option force\-insert
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-09-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Dhcpv6.Profiles.Profile.Server.AaaServer.Dhcpv6Option, self).__init__()

                            self.yang_name = "dhcpv6-option"
                            self.yang_parent_name = "aaa-server"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('force_insert', (YLeaf(YType.empty, 'force-insert'), ['Empty'])),
                            ])
                            self.force_insert = None
                            self._segment_path = lambda: "dhcpv6-option"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Server.AaaServer.Dhcpv6Option, ['force_insert'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Server.AaaServer.Dhcpv6Option']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Server.AaaServer']['meta_info']


                class Options(_Entity_):
                    """
                    DHCPv6 match
                    
                    .. attribute:: option
                    
                    	DHCPv6 match option
                    	**type**\: list of  		 :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Options.Option>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Server.Options, self).__init__()

                        self.yang_name = "options"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("option", ("option", Dhcpv6.Profiles.Profile.Server.Options.Option))])
                        self._leafs = OrderedDict()

                        self.option = YList(self)
                        self._segment_path = lambda: "options"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Options, [], name, value)


                    class Option(_Entity_):
                        """
                        DHCPv6 match option
                        
                        .. attribute:: type  (key)
                        
                        	Set string
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: format  (key)
                        
                        	Set constant integer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: value  (key)
                        
                        	Set string
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: enterprise_id
                        
                        	match enterprise number
                        	**type**\:  :py:class:`EnterpriseId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId>`
                        
                        .. attribute:: vendor_class
                        
                        	match vendor class
                        	**type**\:  :py:class:`VendorClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2017-09-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Dhcpv6.Profiles.Profile.Server.Options.Option, self).__init__()

                            self.yang_name = "option"
                            self.yang_parent_name = "options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['type','format','value']
                            self._child_classes = OrderedDict([("enterprise-id", ("enterprise_id", Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId)), ("vendor-class", ("vendor_class", Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass))])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.str, 'type'), ['str'])),
                                ('format', (YLeaf(YType.uint32, 'format'), ['int'])),
                                ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ])
                            self.type = None
                            self.format = None
                            self.value = None

                            self.enterprise_id = Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId()
                            self.enterprise_id.parent = self
                            self._children_name_map["enterprise_id"] = "enterprise-id"

                            self.vendor_class = Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass()
                            self.vendor_class.parent = self
                            self._children_name_map["vendor_class"] = "vendor-class"
                            self._segment_path = lambda: "option" + "[type='" + str(self.type) + "']" + "[format='" + str(self.format) + "']" + "[value='" + str(self.value) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Options.Option, ['type', 'format', 'value'], name, value)


                        class EnterpriseId(_Entity_):
                            """
                            match enterprise number
                            
                            .. attribute:: hex_enterprise_id
                            
                            	defaut action for enterprise number
                            	**type**\:  :py:class:`HexEnterpriseId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId.HexEnterpriseId>`
                            
                            .. attribute:: default_enterprise_id
                            
                            	defaut action for enterprise number
                            	**type**\:  :py:class:`DefaultEnterpriseId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId.DefaultEnterpriseId>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-09-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId, self).__init__()

                                self.yang_name = "enterprise-id"
                                self.yang_parent_name = "option"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("hex-enterprise-id", ("hex_enterprise_id", Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId.HexEnterpriseId)), ("default-enterprise-id", ("default_enterprise_id", Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId.DefaultEnterpriseId))])
                                self._leafs = OrderedDict()

                                self.hex_enterprise_id = Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId.HexEnterpriseId()
                                self.hex_enterprise_id.parent = self
                                self._children_name_map["hex_enterprise_id"] = "hex-enterprise-id"

                                self.default_enterprise_id = Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId.DefaultEnterpriseId()
                                self.default_enterprise_id.parent = self
                                self._children_name_map["default_enterprise_id"] = "default-enterprise-id"
                                self._segment_path = lambda: "enterprise-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId, [], name, value)


                            class HexEnterpriseId(_Entity_):
                                """
                                defaut action for enterprise number
                                
                                .. attribute:: action
                                
                                	Configure Action to be take on match
                                	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Action>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2017-09-12'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId.HexEnterpriseId, self).__init__()

                                    self.yang_name = "hex-enterprise-id"
                                    self.yang_parent_name = "enterprise-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Action', '')])),
                                    ])
                                    self.action = None
                                    self._segment_path = lambda: "hex-enterprise-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId.HexEnterpriseId, ['action'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                    return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId.HexEnterpriseId']['meta_info']


                            class DefaultEnterpriseId(_Entity_):
                                """
                                defaut action for enterprise number
                                
                                .. attribute:: action
                                
                                	Configure Action to be take on match
                                	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Action>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2017-09-12'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId.DefaultEnterpriseId, self).__init__()

                                    self.yang_name = "default-enterprise-id"
                                    self.yang_parent_name = "enterprise-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Action', '')])),
                                    ])
                                    self.action = None
                                    self._segment_path = lambda: "default-enterprise-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId.DefaultEnterpriseId, ['action'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                    return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId.DefaultEnterpriseId']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Options.Option.EnterpriseId']['meta_info']


                        class VendorClass(_Entity_):
                            """
                            match vendor class
                            
                            .. attribute:: str_vendor_class
                            
                            	string action for vendor number
                            	**type**\:  :py:class:`StrVendorClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass.StrVendorClass>`
                            
                            .. attribute:: default_vendor_class
                            
                            	default action for enterprise number
                            	**type**\:  :py:class:`DefaultVendorClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass.DefaultVendorClass>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2017-09-12'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass, self).__init__()

                                self.yang_name = "vendor-class"
                                self.yang_parent_name = "option"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("str-vendor-class", ("str_vendor_class", Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass.StrVendorClass)), ("default-vendor-class", ("default_vendor_class", Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass.DefaultVendorClass))])
                                self._leafs = OrderedDict()

                                self.str_vendor_class = Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass.StrVendorClass()
                                self.str_vendor_class.parent = self
                                self._children_name_map["str_vendor_class"] = "str-vendor-class"

                                self.default_vendor_class = Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass.DefaultVendorClass()
                                self.default_vendor_class.parent = self
                                self._children_name_map["default_vendor_class"] = "default-vendor-class"
                                self._segment_path = lambda: "vendor-class"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass, [], name, value)


                            class StrVendorClass(_Entity_):
                                """
                                string action for vendor number
                                
                                .. attribute:: action
                                
                                	Configure Action to be take on match
                                	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Action>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2017-09-12'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass.StrVendorClass, self).__init__()

                                    self.yang_name = "str-vendor-class"
                                    self.yang_parent_name = "vendor-class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Action', '')])),
                                    ])
                                    self.action = None
                                    self._segment_path = lambda: "str-vendor-class"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass.StrVendorClass, ['action'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                    return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass.StrVendorClass']['meta_info']


                            class DefaultVendorClass(_Entity_):
                                """
                                default action for enterprise number
                                
                                .. attribute:: action
                                
                                	Configure Action to be take on match
                                	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Action>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2017-09-12'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass.DefaultVendorClass, self).__init__()

                                    self.yang_name = "default-vendor-class"
                                    self.yang_parent_name = "vendor-class"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg', 'Action', '')])),
                                    ])
                                    self.action = None
                                    self._segment_path = lambda: "default-vendor-class"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass.DefaultVendorClass, ['action'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                    return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass.DefaultVendorClass']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Options.Option.VendorClass']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Options.Option']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Options']['meta_info']


                class Dhcpv6Options(_Entity_):
                    """
                    DHCPv6 options
                    
                    .. attribute:: vendor_options
                    
                    	Vendor options
                    	**type**\:  :py:class:`VendorOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2017-09-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Dhcpv6.Profiles.Profile.Server.Dhcpv6Options, self).__init__()

                        self.yang_name = "dhcpv6-options"
                        self.yang_parent_name = "server"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("vendor-options", ("vendor_options", Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions))])
                        self._leafs = OrderedDict()

                        self.vendor_options = Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions()
                        self.vendor_options.parent = self
                        self._children_name_map["vendor_options"] = "vendor-options"
                        self._segment_path = lambda: "dhcpv6-options"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Dhcpv6Options, [], name, value)


                    class VendorOptions(_Entity_):
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
                        _revision = '2017-09-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions, self).__init__()

                            self.yang_name = "vendor-options"
                            self.yang_parent_name = "dhcpv6-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.str, 'type'), ['str'])),
                                ('vendor_options', (YLeaf(YType.str, 'vendor-options'), ['str'])),
                            ])
                            self.type = None
                            self.vendor_options = None
                            self._segment_path = lambda: "vendor-options"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions, ['type', 'vendor_options'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Dhcpv6Options']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Profiles.Profile.Server']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                return meta._meta_table['Dhcpv6.Profiles.Profile']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
            return meta._meta_table['Dhcpv6.Profiles']['meta_info']


    class Interfaces(_Entity_):
        """
        Table of Interface
        
        .. attribute:: interface
        
        	None
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2017-09-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Dhcpv6.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "dhcpv6"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Dhcpv6.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Dhcpv6.Interfaces, [], name, value)


        class Interface(_Entity_):
            """
            None
            
            .. attribute:: interface_name  (key)
            
            	Interface to configure
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
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
            _revision = '2017-09-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Dhcpv6.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("pppoe", ("pppoe", Dhcpv6.Interfaces.Interface.Pppoe)), ("proxy", ("proxy", Dhcpv6.Interfaces.Interface.Proxy)), ("base", ("base", Dhcpv6.Interfaces.Interface.Base)), ("server", ("server", Dhcpv6.Interfaces.Interface.Server)), ("relay", ("relay", Dhcpv6.Interfaces.Interface.Relay))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.interface_name = None

                self.pppoe = Dhcpv6.Interfaces.Interface.Pppoe()
                self.pppoe.parent = self
                self._children_name_map["pppoe"] = "pppoe"

                self.proxy = Dhcpv6.Interfaces.Interface.Proxy()
                self.proxy.parent = self
                self._children_name_map["proxy"] = "proxy"

                self.base = Dhcpv6.Interfaces.Interface.Base()
                self.base.parent = self
                self._children_name_map["base"] = "base"

                self.server = Dhcpv6.Interfaces.Interface.Server()
                self.server.parent = self
                self._children_name_map["server"] = "server"

                self.relay = Dhcpv6.Interfaces.Interface.Relay()
                self.relay.parent = self
                self._children_name_map["relay"] = "relay"
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Dhcpv6.Interfaces.Interface, ['interface_name'], name, value)


            class Pppoe(_Entity_):
                """
                PPPoE subscriber interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-09-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Dhcpv6.Interfaces.Interface.Pppoe, self).__init__()

                    self.yang_name = "pppoe"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                    ])
                    self.profile = None
                    self._segment_path = lambda: "pppoe"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Pppoe, ['profile'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Interfaces.Interface.Pppoe']['meta_info']


            class Proxy(_Entity_):
                """
                Assign a proxy profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-09-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Dhcpv6.Interfaces.Interface.Proxy, self).__init__()

                    self.yang_name = "proxy"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                    ])
                    self.profile = None
                    self._segment_path = lambda: "proxy"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Proxy, ['profile'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Interfaces.Interface.Proxy']['meta_info']


            class Base(_Entity_):
                """
                Assign a base profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-09-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Dhcpv6.Interfaces.Interface.Base, self).__init__()

                    self.yang_name = "base"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                    ])
                    self.profile = None
                    self._segment_path = lambda: "base"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Base, ['profile'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Interfaces.Interface.Base']['meta_info']


            class Server(_Entity_):
                """
                Assign a server profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-09-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Dhcpv6.Interfaces.Interface.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                    ])
                    self.profile = None
                    self._segment_path = lambda: "server"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Server, ['profile'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Interfaces.Interface.Server']['meta_info']


            class Relay(_Entity_):
                """
                Assign a relay profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2017-09-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Dhcpv6.Interfaces.Interface.Relay, self).__init__()

                    self.yang_name = "relay"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                    ])
                    self.profile = None
                    self._segment_path = lambda: "relay"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dhcpv6.Interfaces.Interface.Relay, ['profile'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Interfaces.Interface.Relay']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                return meta._meta_table['Dhcpv6.Interfaces.Interface']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
            return meta._meta_table['Dhcpv6.Interfaces']['meta_info']

    def clone_ptr(self):
        self._top_entity = Dhcpv6()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
        return meta._meta_table['Dhcpv6']['meta_info']


