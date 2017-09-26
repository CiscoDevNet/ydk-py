""" Cisco_IOS_XR_ipv4_dhcpd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-dhcpd package configuration.

This module contains definitions
for the following management objects\:
  ipv4\-dhcpd\: DHCP IPV4 configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BaseAction(Enum):
    """
    BaseAction

    Base action

    .. data:: allow = 0

    	Allow vendor specific DHCP Discover

    .. data:: drop = 1

    	Drop vendor specific DHCP Discover

    """

    allow = Enum.YLeaf(0, "allow")

    drop = Enum.YLeaf(1, "drop")


class Dhcpv4AuthUsername(Enum):
    """
    Dhcpv4AuthUsername

    Dhcpv4 auth username

    .. data:: auth_username_mac = 1

    	Authentication Username formating mac

    .. data:: auth_username_giaddr = 2

    	Authentication Username formating giaddr

    """

    auth_username_mac = Enum.YLeaf(1, "auth-username-mac")

    auth_username_giaddr = Enum.YLeaf(2, "auth-username-giaddr")


class Dhcpv4LimitLease1(Enum):
    """
    Dhcpv4LimitLease1

    Dhcpv4 limit lease1

    .. data:: interface = 1

    	Interface

    .. data:: circuit_id = 2

    	Circuit ID

    .. data:: remote_id = 3

    	Remote ID

    .. data:: circuit_id_remote_id = 4

    	Circuit ID Remote ID

    """

    interface = Enum.YLeaf(1, "interface")

    circuit_id = Enum.YLeaf(2, "circuit-id")

    remote_id = Enum.YLeaf(3, "remote-id")

    circuit_id_remote_id = Enum.YLeaf(4, "circuit-id-remote-id")


class Dhcpv4MatchOption(Enum):
    """
    Dhcpv4MatchOption

    Dhcpv4 match option

    .. data:: Y_60__FWD_SLASH__60 = 60

    	Vendor class ID

    .. data:: Y_77__FWD_SLASH__77 = 77

    	77 User class

    .. data:: Y_124__FWD_SLASH__124 = 124

    	Vendor identifying class

    .. data:: Y_125__FWD_SLASH__125 = 125

    	Vendor specific information

    """

    Y_60__FWD_SLASH__60 = Enum.YLeaf(60, "60/60")

    Y_77__FWD_SLASH__77 = Enum.YLeaf(77, "77/77")

    Y_124__FWD_SLASH__124 = Enum.YLeaf(124, "124/124")

    Y_125__FWD_SLASH__125 = Enum.YLeaf(125, "125/125")


class Ipv4dhcpdBroadcastFlagPolicy(Enum):
    """
    Ipv4dhcpdBroadcastFlagPolicy

    Ipv4dhcpd broadcast flag policy

    .. data:: ignore = 0

    	Ignore

    .. data:: check = 1

    	check

    .. data:: unicast_always = 2

    	Unicast always

    """

    ignore = Enum.YLeaf(0, "ignore")

    check = Enum.YLeaf(1, "check")

    unicast_always = Enum.YLeaf(2, "unicast-always")


class Ipv4dhcpdFmt(Enum):
    """
    Ipv4dhcpdFmt

    Ipv4dhcpd fmt

    .. data:: no_format = 0

    	Not a Format String

    .. data:: format = 1

    	Format String

    """

    no_format = Enum.YLeaf(0, "no-format")

    format = Enum.YLeaf(1, "format")


class Ipv4dhcpdFmtSpecifier(Enum):
    """
    Ipv4dhcpdFmtSpecifier

    Ipv4dhcpd fmt specifier

    .. data:: physical_chassis = 1

    	Physical chassis

    .. data:: physical_slot = 2

    	Physical slot

    .. data:: physical_sub_slot = 3

    	Physical sub-slot

    .. data:: physical_port = 4

    	Physical port

    .. data:: physical_sub_port = 5

    	Physical sub-port

    .. data:: inner_vlan_id = 6

    	Inner VLAN ID

    .. data:: outer_vlan_id = 7

    	Outer VLAN ID

    .. data:: l2_interface = 8

    	L2 Interface

    """

    physical_chassis = Enum.YLeaf(1, "physical-chassis")

    physical_slot = Enum.YLeaf(2, "physical-slot")

    physical_sub_slot = Enum.YLeaf(3, "physical-sub-slot")

    physical_port = Enum.YLeaf(4, "physical-port")

    physical_sub_port = Enum.YLeaf(5, "physical-sub-port")

    inner_vlan_id = Enum.YLeaf(6, "inner-vlan-id")

    outer_vlan_id = Enum.YLeaf(7, "outer-vlan-id")

    l2_interface = Enum.YLeaf(8, "l2-interface")


class Ipv4dhcpdGiaddrPolicy(Enum):
    """
    Ipv4dhcpdGiaddrPolicy

    Ipv4dhcpd giaddr policy

    .. data:: giaddr_policy_keep = 1

    	Giaddr Policy Keep

    """

    giaddr_policy_keep = Enum.YLeaf(1, "giaddr-policy-keep")


class Ipv4dhcpdLayer(Enum):
    """
    Ipv4dhcpdLayer

    Ipv4dhcpd layer

    .. data:: layer2 = 2

    	Layer2

    .. data:: layer3 = 3

    	Layer3

    """

    layer2 = Enum.YLeaf(2, "layer2")

    layer3 = Enum.YLeaf(3, "layer3")


class Ipv4dhcpdMode(Enum):
    """
    Ipv4dhcpdMode

    Ipv4dhcpd mode

    .. data:: base = 0

    	Base

    .. data:: relay = 1

    	Relay

    .. data:: snoop = 2

    	Snoop

    .. data:: server = 3

    	Server

    .. data:: proxy = 4

    	Proxy

    .. data:: base2 = 5

    	Base2

    """

    base = Enum.YLeaf(0, "base")

    relay = Enum.YLeaf(1, "relay")

    snoop = Enum.YLeaf(2, "snoop")

    server = Enum.YLeaf(3, "server")

    proxy = Enum.YLeaf(4, "proxy")

    base2 = Enum.YLeaf(5, "base2")


class Ipv4dhcpdRelayInfoOptionAuthenticate(Enum):
    """
    Ipv4dhcpdRelayInfoOptionAuthenticate

    Ipv4dhcpd relay info option authenticate

    .. data:: received = 0

    	Received

    .. data:: inserted = 1

    	Inserted

    """

    received = Enum.YLeaf(0, "received")

    inserted = Enum.YLeaf(1, "inserted")


class Ipv4dhcpdRelayInfoOptionPolicy(Enum):
    """
    Ipv4dhcpdRelayInfoOptionPolicy

    Ipv4dhcpd relay info option policy

    .. data:: replace = 0

    	Replace

    .. data:: keep = 1

    	Keep

    .. data:: drop = 2

    	Drop

    .. data:: encapsulate = 3

    	Encapsulate

    """

    replace = Enum.YLeaf(0, "replace")

    keep = Enum.YLeaf(1, "keep")

    drop = Enum.YLeaf(2, "drop")

    encapsulate = Enum.YLeaf(3, "encapsulate")


class Ipv4dhcpdRelayInfoOptionvpnMode(Enum):
    """
    Ipv4dhcpdRelayInfoOptionvpnMode

    Ipv4dhcpd relay info optionvpn mode

    .. data:: rfc = 0

    	RFC

    .. data:: cisco = 1

    	Cisco

    """

    rfc = Enum.YLeaf(0, "rfc")

    cisco = Enum.YLeaf(1, "cisco")


class LeaseLimitValue(Enum):
    """
    LeaseLimitValue

    Lease limit value

    .. data:: per_interface = 1

    	Insert the limit lease type interface

    .. data:: per_circuit_id = 2

    	Insert the limit lease type circuit-id

    .. data:: per_remote_id = 3

    	Insert the limit lease type remote-id

    """

    per_interface = Enum.YLeaf(1, "per-interface")

    per_circuit_id = Enum.YLeaf(2, "per-circuit-id")

    per_remote_id = Enum.YLeaf(3, "per-remote-id")


class MacMismatchAction(Enum):
    """
    MacMismatchAction

    Mac mismatch action

    .. data:: forward = 0

    	Forward

    .. data:: drop = 1

    	Drop

    """

    forward = Enum.YLeaf(0, "forward")

    drop = Enum.YLeaf(1, "drop")


class Matchaction(Enum):
    """
    Matchaction

    Matchaction

    .. data:: allow = 0

    	Allow DHCP Discover

    .. data:: drop = 1

    	Drop DHCP Discover

    """

    allow = Enum.YLeaf(0, "allow")

    drop = Enum.YLeaf(1, "drop")


class Matchoption(Enum):
    """
    Matchoption

    Matchoption

    .. data:: circuitid = 1

    	Match circuit id of option 82 Relay-agent

    	specific class

    .. data:: remoteid = 2

    	Match remote id of option 82 Relay-agent

    	specific class

    .. data:: Y_60 = 60

    	Match option 60 vendor class id

    .. data:: Y_77 = 77

    	Match option 77 user class

    .. data:: Y_124 = 124

    	Match option 124 vendor-identifying vendor

    	class

    .. data:: Y_125 = 125

    	Match option 125 vendor-indentifying

    	vendor-specific info

    """

    circuitid = Enum.YLeaf(1, "circuitid")

    remoteid = Enum.YLeaf(2, "remoteid")

    Y_60 = Enum.YLeaf(60, "60")

    Y_77 = Enum.YLeaf(77, "77")

    Y_124 = Enum.YLeaf(124, "124")

    Y_125 = Enum.YLeaf(125, "125")


class Policy(Enum):
    """
    Policy

    Policy

    .. data:: ignore = 0

    	Ignore the broadcast policy

    .. data:: check = 1

    	Check for broadcast flag

    .. data:: unicastalways = 2

    	Always Unicast the reply

    """

    ignore = Enum.YLeaf(0, "ignore")

    check = Enum.YLeaf(1, "check")

    unicastalways = Enum.YLeaf(2, "unicastalways")


class ProxyAction(Enum):
    """
    ProxyAction

    Proxy action

    .. data:: allow = 0

    	Allow vendor specific DHCP Discover

    .. data:: drop = 1

    	Drop vendor specific DHCP Discover

    """

    allow = Enum.YLeaf(0, "allow")

    drop = Enum.YLeaf(1, "drop")



class Ipv4Dhcpd(Entity):
    """
    DHCP IPV4 configuration
    
    .. attribute:: allow_client_id_change
    
    	For BNG session, allow client id change for a client MAC
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: database
    
    	Enable DHCP binding database storage to file system
    	**type**\:   :py:class:`Database <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Database>`
    
    .. attribute:: duplicate_mac_allowed
    
    	Allow Duplicate MAC Address
    	**type**\:   :py:class:`DuplicateMacAllowed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.DuplicateMacAllowed>`
    
    	**presence node**\: True
    
    .. attribute:: enable
    
    	DHCP IPV4 configuration
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: inner_cos
    
    	Configure inner cos values for dhcp packets
    	**type**\:  int
    
    	**range:** 0..7
    
    .. attribute:: interfaces
    
    	DHCP IPV4 Interface Table
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces>`
    
    .. attribute:: outer_cos
    
    	Configure outer cos values for dhcp packets
    	**type**\:  int
    
    	**range:** 0..7
    
    .. attribute:: profiles
    
    	DHCP IPV4 Profile Table
    	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles>`
    
    .. attribute:: rate_limit
    
    	Rate limit ingress packets
    	**type**\:   :py:class:`RateLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.RateLimit>`
    
    .. attribute:: vrfs
    
    	VRF Table
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Vrfs>`
    
    

    """

    _prefix = 'ipv4-dhcpd-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Ipv4Dhcpd, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-dhcpd"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-dhcpd-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"database" : ("database", Ipv4Dhcpd.Database), "duplicate-mac-allowed" : ("duplicate_mac_allowed", Ipv4Dhcpd.DuplicateMacAllowed), "interfaces" : ("interfaces", Ipv4Dhcpd.Interfaces), "profiles" : ("profiles", Ipv4Dhcpd.Profiles), "rate-limit" : ("rate_limit", Ipv4Dhcpd.RateLimit), "vrfs" : ("vrfs", Ipv4Dhcpd.Vrfs)}
        self._child_list_classes = {}

        self.allow_client_id_change = YLeaf(YType.empty, "allow-client-id-change")

        self.enable = YLeaf(YType.empty, "enable")

        self.inner_cos = YLeaf(YType.uint32, "inner-cos")

        self.outer_cos = YLeaf(YType.uint32, "outer-cos")

        self.database = Ipv4Dhcpd.Database()
        self.database.parent = self
        self._children_name_map["database"] = "database"
        self._children_yang_names.add("database")

        self.duplicate_mac_allowed = None
        self._children_name_map["duplicate_mac_allowed"] = "duplicate-mac-allowed"
        self._children_yang_names.add("duplicate-mac-allowed")

        self.interfaces = Ipv4Dhcpd.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.profiles = Ipv4Dhcpd.Profiles()
        self.profiles.parent = self
        self._children_name_map["profiles"] = "profiles"
        self._children_yang_names.add("profiles")

        self.rate_limit = Ipv4Dhcpd.RateLimit()
        self.rate_limit.parent = self
        self._children_name_map["rate_limit"] = "rate-limit"
        self._children_yang_names.add("rate-limit")

        self.vrfs = Ipv4Dhcpd.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd"

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv4Dhcpd, ['allow_client_id_change', 'enable', 'inner_cos', 'outer_cos'], name, value)


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
        
        .. attribute:: server
        
        	Enable DHCP server binding database storage to file system
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: snoop
        
        	Enable DHCP snoop binding database storage to file system
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv4Dhcpd.Database, self).__init__()

            self.yang_name = "database"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.full_write_interval = YLeaf(YType.uint32, "full-write-interval")

            self.incremental_write_interval = YLeaf(YType.uint32, "incremental-write-interval")

            self.proxy = YLeaf(YType.empty, "proxy")

            self.server = YLeaf(YType.empty, "server")

            self.snoop = YLeaf(YType.empty, "snoop")
            self._segment_path = lambda: "database"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Dhcpd.Database, ['full_write_interval', 'incremental_write_interval', 'proxy', 'server', 'snoop'], name, value)


    class DuplicateMacAllowed(Entity):
        """
        Allow Duplicate MAC Address
        
        .. attribute:: duplicate_mac
        
        	Duplicate mac is allowed
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        .. attribute:: exclude_vlan
        
        	Exclude vlan
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: include_giaddr
        
        	Include giaddr
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv4Dhcpd.DuplicateMacAllowed, self).__init__()

            self.yang_name = "duplicate-mac-allowed"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.duplicate_mac = YLeaf(YType.empty, "duplicate-mac")

            self.exclude_vlan = YLeaf(YType.empty, "exclude-vlan")

            self.include_giaddr = YLeaf(YType.empty, "include-giaddr")
            self._segment_path = lambda: "duplicate-mac-allowed"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Dhcpd.DuplicateMacAllowed, ['duplicate_mac', 'exclude_vlan', 'include_giaddr'], name, value)


    class Interfaces(Entity):
        """
        DHCP IPV4 Interface Table
        
        .. attribute:: interface
        
        	DHCP IPV4 Interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv4Dhcpd.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", Ipv4Dhcpd.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Dhcpd.Interfaces, [], name, value)


        class Interface(Entity):
            """
            DHCP IPV4 Interface
            
            .. attribute:: interface_name  <key>
            
            	Interface Name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: base_interface
            
            	DHCP IPv4 Base profile information
            	**type**\:   :py:class:`BaseInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.BaseInterface>`
            
            .. attribute:: profile
            
            	Profile name and mode
            	**type**\:   :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.Profile>`
            
            	**presence node**\: True
            
            .. attribute:: proxy_interface
            
            	DHCP IPv4 proxy information
            	**type**\:   :py:class:`ProxyInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ProxyInterface>`
            
            .. attribute:: relay_interface
            
            	DHCP IPv4 relay information
            	**type**\:   :py:class:`RelayInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.RelayInterface>`
            
            .. attribute:: server_interface
            
            	DHCP IPv4 Server information
            	**type**\:   :py:class:`ServerInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ServerInterface>`
            
            .. attribute:: snoop_interface
            
            	DHCP IPv4 snoop information
            	**type**\:   :py:class:`SnoopInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.SnoopInterface>`
            
            .. attribute:: static_mode
            
            	Static Table Entries containing MAC address to IP address bindings
            	**type**\:   :py:class:`StaticMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.StaticMode>`
            
            

            """

            _prefix = 'ipv4-dhcpd-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv4Dhcpd.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"base-interface" : ("base_interface", Ipv4Dhcpd.Interfaces.Interface.BaseInterface), "profile" : ("profile", Ipv4Dhcpd.Interfaces.Interface.Profile), "proxy-interface" : ("proxy_interface", Ipv4Dhcpd.Interfaces.Interface.ProxyInterface), "relay-interface" : ("relay_interface", Ipv4Dhcpd.Interfaces.Interface.RelayInterface), "server-interface" : ("server_interface", Ipv4Dhcpd.Interfaces.Interface.ServerInterface), "snoop-interface" : ("snoop_interface", Ipv4Dhcpd.Interfaces.Interface.SnoopInterface), "static-mode" : ("static_mode", Ipv4Dhcpd.Interfaces.Interface.StaticMode)}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.base_interface = Ipv4Dhcpd.Interfaces.Interface.BaseInterface()
                self.base_interface.parent = self
                self._children_name_map["base_interface"] = "base-interface"
                self._children_yang_names.add("base-interface")

                self.profile = None
                self._children_name_map["profile"] = "profile"
                self._children_yang_names.add("profile")

                self.proxy_interface = Ipv4Dhcpd.Interfaces.Interface.ProxyInterface()
                self.proxy_interface.parent = self
                self._children_name_map["proxy_interface"] = "proxy-interface"
                self._children_yang_names.add("proxy-interface")

                self.relay_interface = Ipv4Dhcpd.Interfaces.Interface.RelayInterface()
                self.relay_interface.parent = self
                self._children_name_map["relay_interface"] = "relay-interface"
                self._children_yang_names.add("relay-interface")

                self.server_interface = Ipv4Dhcpd.Interfaces.Interface.ServerInterface()
                self.server_interface.parent = self
                self._children_name_map["server_interface"] = "server-interface"
                self._children_yang_names.add("server-interface")

                self.snoop_interface = Ipv4Dhcpd.Interfaces.Interface.SnoopInterface()
                self.snoop_interface.parent = self
                self._children_name_map["snoop_interface"] = "snoop-interface"
                self._children_yang_names.add("snoop-interface")

                self.static_mode = Ipv4Dhcpd.Interfaces.Interface.StaticMode()
                self.static_mode.parent = self
                self._children_name_map["static_mode"] = "static-mode"
                self._children_yang_names.add("static-mode")
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface, ['interface_name'], name, value)


            class BaseInterface(Entity):
                """
                DHCP IPv4 Base profile information
                
                .. attribute:: base_dhcp_circuit_id
                
                	Circuit ID value
                	**type**\:   :py:class:`BaseDhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId>`
                
                	**presence node**\: True
                
                .. attribute:: profile
                
                	Interface profile name
                	**type**\:  str
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.BaseInterface, self).__init__()

                    self.yang_name = "base-interface"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"base-dhcp-circuit-id" : ("base_dhcp_circuit_id", Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId)}
                    self._child_list_classes = {}

                    self.profile = YLeaf(YType.str, "profile")

                    self.base_dhcp_circuit_id = None
                    self._children_name_map["base_dhcp_circuit_id"] = "base-dhcp-circuit-id"
                    self._children_yang_names.add("base-dhcp-circuit-id")
                    self._segment_path = lambda: "base-interface"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.BaseInterface, ['profile'], name, value)


                class BaseDhcpCircuitId(Entity):
                    """
                    Circuit ID value
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:   :py:class:`Ipv4dhcpdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmt>`
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId, self).__init__()

                        self.yang_name = "base-dhcp-circuit-id"
                        self.yang_parent_name = "base-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.argument1 = YLeaf(YType.enumeration, "argument1")

                        self.argument10 = YLeaf(YType.enumeration, "argument10")

                        self.argument11 = YLeaf(YType.enumeration, "argument11")

                        self.argument12 = YLeaf(YType.enumeration, "argument12")

                        self.argument13 = YLeaf(YType.enumeration, "argument13")

                        self.argument14 = YLeaf(YType.enumeration, "argument14")

                        self.argument15 = YLeaf(YType.enumeration, "argument15")

                        self.argument16 = YLeaf(YType.enumeration, "argument16")

                        self.argument2 = YLeaf(YType.enumeration, "argument2")

                        self.argument3 = YLeaf(YType.enumeration, "argument3")

                        self.argument4 = YLeaf(YType.enumeration, "argument4")

                        self.argument5 = YLeaf(YType.enumeration, "argument5")

                        self.argument6 = YLeaf(YType.enumeration, "argument6")

                        self.argument7 = YLeaf(YType.enumeration, "argument7")

                        self.argument8 = YLeaf(YType.enumeration, "argument8")

                        self.argument9 = YLeaf(YType.enumeration, "argument9")

                        self.circuit_id = YLeaf(YType.str, "circuit-id")

                        self.format = YLeaf(YType.enumeration, "format")
                        self._segment_path = lambda: "base-dhcp-circuit-id"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId, ['argument1', 'argument10', 'argument11', 'argument12', 'argument13', 'argument14', 'argument15', 'argument16', 'argument2', 'argument3', 'argument4', 'argument5', 'argument6', 'argument7', 'argument8', 'argument9', 'circuit_id', 'format'], name, value)


            class Profile(Entity):
                """
                Profile name and mode
                
                .. attribute:: mode
                
                	DHCP mode
                	**type**\:   :py:class:`Ipv4dhcpdMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdMode>`
                
                	**mandatory**\: True
                
                .. attribute:: profile_name
                
                	Profile name
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.Profile, self).__init__()

                    self.yang_name = "profile"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.mode = YLeaf(YType.enumeration, "mode")

                    self.profile_name = YLeaf(YType.str, "profile-name")
                    self._segment_path = lambda: "profile"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.Profile, ['mode', 'profile_name'], name, value)


            class ProxyInterface(Entity):
                """
                DHCP IPv4 proxy information
                
                .. attribute:: dhcp_circuit_id
                
                	Circuit ID value
                	**type**\:   :py:class:`DhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId>`
                
                	**presence node**\: True
                
                .. attribute:: profile
                
                	Interface profile name
                	**type**\:  str
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.ProxyInterface, self).__init__()

                    self.yang_name = "proxy-interface"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"dhcp-circuit-id" : ("dhcp_circuit_id", Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId)}
                    self._child_list_classes = {}

                    self.profile = YLeaf(YType.str, "profile")

                    self.dhcp_circuit_id = None
                    self._children_name_map["dhcp_circuit_id"] = "dhcp-circuit-id"
                    self._children_yang_names.add("dhcp-circuit-id")
                    self._segment_path = lambda: "proxy-interface"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.ProxyInterface, ['profile'], name, value)


                class DhcpCircuitId(Entity):
                    """
                    Circuit ID value
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:   :py:class:`Ipv4dhcpdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmt>`
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId, self).__init__()

                        self.yang_name = "dhcp-circuit-id"
                        self.yang_parent_name = "proxy-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.argument1 = YLeaf(YType.enumeration, "argument1")

                        self.argument10 = YLeaf(YType.enumeration, "argument10")

                        self.argument11 = YLeaf(YType.enumeration, "argument11")

                        self.argument12 = YLeaf(YType.enumeration, "argument12")

                        self.argument13 = YLeaf(YType.enumeration, "argument13")

                        self.argument14 = YLeaf(YType.enumeration, "argument14")

                        self.argument15 = YLeaf(YType.enumeration, "argument15")

                        self.argument16 = YLeaf(YType.enumeration, "argument16")

                        self.argument2 = YLeaf(YType.enumeration, "argument2")

                        self.argument3 = YLeaf(YType.enumeration, "argument3")

                        self.argument4 = YLeaf(YType.enumeration, "argument4")

                        self.argument5 = YLeaf(YType.enumeration, "argument5")

                        self.argument6 = YLeaf(YType.enumeration, "argument6")

                        self.argument7 = YLeaf(YType.enumeration, "argument7")

                        self.argument8 = YLeaf(YType.enumeration, "argument8")

                        self.argument9 = YLeaf(YType.enumeration, "argument9")

                        self.circuit_id = YLeaf(YType.str, "circuit-id")

                        self.format = YLeaf(YType.enumeration, "format")
                        self._segment_path = lambda: "dhcp-circuit-id"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId, ['argument1', 'argument10', 'argument11', 'argument12', 'argument13', 'argument14', 'argument15', 'argument16', 'argument2', 'argument3', 'argument4', 'argument5', 'argument6', 'argument7', 'argument8', 'argument9', 'circuit_id', 'format'], name, value)


            class RelayInterface(Entity):
                """
                DHCP IPv4 relay information
                
                .. attribute:: relay_dhcp_circuit_id
                
                	Circuit ID value
                	**type**\:   :py:class:`RelayDhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.RelayInterface, self).__init__()

                    self.yang_name = "relay-interface"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"relay-dhcp-circuit-id" : ("relay_dhcp_circuit_id", Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId)}
                    self._child_list_classes = {}

                    self.relay_dhcp_circuit_id = None
                    self._children_name_map["relay_dhcp_circuit_id"] = "relay-dhcp-circuit-id"
                    self._children_yang_names.add("relay-dhcp-circuit-id")
                    self._segment_path = lambda: "relay-interface"


                class RelayDhcpCircuitId(Entity):
                    """
                    Circuit ID value
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:   :py:class:`Ipv4dhcpdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmt>`
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId, self).__init__()

                        self.yang_name = "relay-dhcp-circuit-id"
                        self.yang_parent_name = "relay-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.argument1 = YLeaf(YType.enumeration, "argument1")

                        self.argument10 = YLeaf(YType.enumeration, "argument10")

                        self.argument11 = YLeaf(YType.enumeration, "argument11")

                        self.argument12 = YLeaf(YType.enumeration, "argument12")

                        self.argument13 = YLeaf(YType.enumeration, "argument13")

                        self.argument14 = YLeaf(YType.enumeration, "argument14")

                        self.argument15 = YLeaf(YType.enumeration, "argument15")

                        self.argument16 = YLeaf(YType.enumeration, "argument16")

                        self.argument2 = YLeaf(YType.enumeration, "argument2")

                        self.argument3 = YLeaf(YType.enumeration, "argument3")

                        self.argument4 = YLeaf(YType.enumeration, "argument4")

                        self.argument5 = YLeaf(YType.enumeration, "argument5")

                        self.argument6 = YLeaf(YType.enumeration, "argument6")

                        self.argument7 = YLeaf(YType.enumeration, "argument7")

                        self.argument8 = YLeaf(YType.enumeration, "argument8")

                        self.argument9 = YLeaf(YType.enumeration, "argument9")

                        self.circuit_id = YLeaf(YType.str, "circuit-id")

                        self.format = YLeaf(YType.enumeration, "format")
                        self._segment_path = lambda: "relay-dhcp-circuit-id"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId, ['argument1', 'argument10', 'argument11', 'argument12', 'argument13', 'argument14', 'argument15', 'argument16', 'argument2', 'argument3', 'argument4', 'argument5', 'argument6', 'argument7', 'argument8', 'argument9', 'circuit_id', 'format'], name, value)


            class ServerInterface(Entity):
                """
                DHCP IPv4 Server information
                
                .. attribute:: profile
                
                	Interface profile name
                	**type**\:  str
                
                .. attribute:: server_dhcp_circuit_id
                
                	Circuit ID value
                	**type**\:   :py:class:`ServerDhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.ServerInterface, self).__init__()

                    self.yang_name = "server-interface"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"server-dhcp-circuit-id" : ("server_dhcp_circuit_id", Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId)}
                    self._child_list_classes = {}

                    self.profile = YLeaf(YType.str, "profile")

                    self.server_dhcp_circuit_id = None
                    self._children_name_map["server_dhcp_circuit_id"] = "server-dhcp-circuit-id"
                    self._children_yang_names.add("server-dhcp-circuit-id")
                    self._segment_path = lambda: "server-interface"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.ServerInterface, ['profile'], name, value)


                class ServerDhcpCircuitId(Entity):
                    """
                    Circuit ID value
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:   :py:class:`Ipv4dhcpdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmt>`
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId, self).__init__()

                        self.yang_name = "server-dhcp-circuit-id"
                        self.yang_parent_name = "server-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.argument1 = YLeaf(YType.enumeration, "argument1")

                        self.argument10 = YLeaf(YType.enumeration, "argument10")

                        self.argument11 = YLeaf(YType.enumeration, "argument11")

                        self.argument12 = YLeaf(YType.enumeration, "argument12")

                        self.argument13 = YLeaf(YType.enumeration, "argument13")

                        self.argument14 = YLeaf(YType.enumeration, "argument14")

                        self.argument15 = YLeaf(YType.enumeration, "argument15")

                        self.argument16 = YLeaf(YType.enumeration, "argument16")

                        self.argument2 = YLeaf(YType.enumeration, "argument2")

                        self.argument3 = YLeaf(YType.enumeration, "argument3")

                        self.argument4 = YLeaf(YType.enumeration, "argument4")

                        self.argument5 = YLeaf(YType.enumeration, "argument5")

                        self.argument6 = YLeaf(YType.enumeration, "argument6")

                        self.argument7 = YLeaf(YType.enumeration, "argument7")

                        self.argument8 = YLeaf(YType.enumeration, "argument8")

                        self.argument9 = YLeaf(YType.enumeration, "argument9")

                        self.circuit_id = YLeaf(YType.str, "circuit-id")

                        self.format = YLeaf(YType.enumeration, "format")
                        self._segment_path = lambda: "server-dhcp-circuit-id"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId, ['argument1', 'argument10', 'argument11', 'argument12', 'argument13', 'argument14', 'argument15', 'argument16', 'argument2', 'argument3', 'argument4', 'argument5', 'argument6', 'argument7', 'argument8', 'argument9', 'circuit_id', 'format'], name, value)


            class SnoopInterface(Entity):
                """
                DHCP IPv4 snoop information
                
                .. attribute:: snoop_circuit_id
                
                	Configure circuit ID for snoop 1. Hex 2. ASCII
                	**type**\:   :py:class:`SnoopCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId>`
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.SnoopInterface, self).__init__()

                    self.yang_name = "snoop-interface"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"snoop-circuit-id" : ("snoop_circuit_id", Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId)}
                    self._child_list_classes = {}

                    self.snoop_circuit_id = Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId()
                    self.snoop_circuit_id.parent = self
                    self._children_name_map["snoop_circuit_id"] = "snoop-circuit-id"
                    self._children_yang_names.add("snoop-circuit-id")
                    self._segment_path = lambda: "snoop-interface"


                class SnoopCircuitId(Entity):
                    """
                    Configure circuit ID for snoop 1. Hex 2.
                    ASCII
                    
                    .. attribute:: circuit_id_value
                    
                    	Enter circuit\-id value
                    	**type**\:  str
                    
                    .. attribute:: format_type
                    
                    	Format type, 1. Hex 2. ASCII
                    	**type**\:  int
                    
                    	**range:** 1..2
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId, self).__init__()

                        self.yang_name = "snoop-circuit-id"
                        self.yang_parent_name = "snoop-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.circuit_id_value = YLeaf(YType.str, "circuit-id-value")

                        self.format_type = YLeaf(YType.uint32, "format-type")
                        self._segment_path = lambda: "snoop-circuit-id"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId, ['circuit_id_value', 'format_type'], name, value)


            class StaticMode(Entity):
                """
                Static Table Entries containing MAC address to
                IP address bindings
                
                .. attribute:: statics
                
                	Static Table Entries containing MAC address to IP address bindings
                	**type**\:   :py:class:`Statics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics>`
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.StaticMode, self).__init__()

                    self.yang_name = "static-mode"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"statics" : ("statics", Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics)}
                    self._child_list_classes = {}

                    self.statics = Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics()
                    self.statics.parent = self
                    self._children_name_map["statics"] = "statics"
                    self._children_yang_names.add("statics")
                    self._segment_path = lambda: "static-mode"


                class Statics(Entity):
                    """
                    Static Table Entries containing MAC address
                    to IP address bindings
                    
                    .. attribute:: static
                    
                    	DHCP static binding of Mac address to IP address
                    	**type**\: list of    :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics, self).__init__()

                        self.yang_name = "statics"
                        self.yang_parent_name = "static-mode"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"static" : ("static", Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static)}

                        self.static = YList(self)
                        self._segment_path = lambda: "statics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics, [], name, value)


                    class Static(Entity):
                        """
                        DHCP static binding of Mac address to IP
                        address
                        
                        .. attribute:: mac_address  <key>
                        
                        	MACAddress
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: client_id  <key>
                        
                        	Client Id
                        	**type**\:  int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: layer  <key>
                        
                        	DHCP IPV4 Static layer
                        	**type**\:   :py:class:`Ipv4dhcpdLayer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdLayer>`
                        
                        .. attribute:: static_address
                        
                        	IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static, self).__init__()

                            self.yang_name = "static"
                            self.yang_parent_name = "statics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.mac_address = YLeaf(YType.str, "mac-address")

                            self.client_id = YLeaf(YType.uint32, "client-id")

                            self.layer = YLeaf(YType.enumeration, "layer")

                            self.static_address = YLeaf(YType.str, "static-address")
                            self._segment_path = lambda: "static" + "[mac-address='" + self.mac_address.get() + "']" + "[client-id='" + self.client_id.get() + "']" + "[layer='" + self.layer.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static, ['mac_address', 'client_id', 'layer', 'static_address'], name, value)


    class Profiles(Entity):
        """
        DHCP IPV4 Profile Table
        
        .. attribute:: profile
        
        	DHCP IPV4 Profile
        	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile>`
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv4Dhcpd.Profiles, self).__init__()

            self.yang_name = "profiles"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"profile" : ("profile", Ipv4Dhcpd.Profiles.Profile)}

            self.profile = YList(self)
            self._segment_path = lambda: "profiles"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Dhcpd.Profiles, [], name, value)


        class Profile(Entity):
            """
            DHCP IPV4 Profile
            
            .. attribute:: profile_name  <key>
            
            	Profile Name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: modes
            
            	DHCP IPV4 Profile modes
            	**type**\:   :py:class:`Modes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes>`
            
            

            """

            _prefix = 'ipv4-dhcpd-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv4Dhcpd.Profiles.Profile, self).__init__()

                self.yang_name = "profile"
                self.yang_parent_name = "profiles"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"modes" : ("modes", Ipv4Dhcpd.Profiles.Profile.Modes)}
                self._child_list_classes = {}

                self.profile_name = YLeaf(YType.str, "profile-name")

                self.modes = Ipv4Dhcpd.Profiles.Profile.Modes()
                self.modes.parent = self
                self._children_name_map["modes"] = "modes"
                self._children_yang_names.add("modes")
                self._segment_path = lambda: "profile" + "[profile-name='" + self.profile_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/profiles/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile, ['profile_name'], name, value)


            class Modes(Entity):
                """
                DHCP IPV4 Profile modes
                
                .. attribute:: mode
                
                	DHCP IPV4 Profile mode
                	**type**\: list of    :py:class:`Mode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode>`
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4Dhcpd.Profiles.Profile.Modes, self).__init__()

                    self.yang_name = "modes"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"mode" : ("mode", Ipv4Dhcpd.Profiles.Profile.Modes.Mode)}

                    self.mode = YList(self)
                    self._segment_path = lambda: "modes"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes, [], name, value)


                class Mode(Entity):
                    """
                    DHCP IPV4 Profile mode
                    
                    .. attribute:: mode  <key>
                    
                    	DHCP IPV4 Profile mode
                    	**type**\:   :py:class:`Ipv4dhcpdMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdMode>`
                    
                    .. attribute:: base
                    
                    	DHCP Base Profile
                    	**type**\:   :py:class:`Base <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base>`
                    
                    .. attribute:: enable
                    
                    	Enable the DHCP IPV4 Profile mode
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: proxy
                    
                    	DHCP proxy profile
                    	**type**\:   :py:class:`Proxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy>`
                    
                    .. attribute:: relay
                    
                    	DHCP Relay profile
                    	**type**\:   :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay>`
                    
                    .. attribute:: server
                    
                    	DHCP Server profile
                    	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server>`
                    
                    .. attribute:: snoop
                    
                    	DHCP Snoop profile
                    	**type**\:   :py:class:`Snoop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode, self).__init__()

                        self.yang_name = "mode"
                        self.yang_parent_name = "modes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"base" : ("base", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base), "proxy" : ("proxy", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy), "relay" : ("relay", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay), "server" : ("server", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server), "snoop" : ("snoop", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop)}
                        self._child_list_classes = {}

                        self.mode = YLeaf(YType.enumeration, "mode")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.base = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base()
                        self.base.parent = self
                        self._children_name_map["base"] = "base"
                        self._children_yang_names.add("base")

                        self.proxy = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy()
                        self.proxy.parent = self
                        self._children_name_map["proxy"] = "proxy"
                        self._children_yang_names.add("proxy")

                        self.relay = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay()
                        self.relay.parent = self
                        self._children_name_map["relay"] = "relay"
                        self._children_yang_names.add("relay")

                        self.server = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server()
                        self.server.parent = self
                        self._children_name_map["server"] = "server"
                        self._children_yang_names.add("server")

                        self.snoop = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop()
                        self.snoop.parent = self
                        self._children_name_map["snoop"] = "snoop"
                        self._children_yang_names.add("snoop")
                        self._segment_path = lambda: "mode" + "[mode='" + self.mode.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode, ['mode', 'enable'], name, value)


                    class Base(Entity):
                        """
                        DHCP Base Profile
                        
                        .. attribute:: base_match
                        
                        	Insert match keyword
                        	**type**\:   :py:class:`BaseMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch>`
                        
                        .. attribute:: base_relay_opt
                        
                        	Insert Relay Agent Information circuit ID and remote ID suboptions in client request
                        	**type**\:   :py:class:`BaseRelayOpt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt>`
                        
                        .. attribute:: default_profile
                        
                        	Enable the default profile
                        	**type**\:   :py:class:`DefaultProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile>`
                        
                        .. attribute:: enable
                        
                        	Enable the DHCP IPv4 Base Profile
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: match
                        
                        	Insert match keyword
                        	**type**\:   :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base, self).__init__()

                            self.yang_name = "base"
                            self.yang_parent_name = "mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"base-match" : ("base_match", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch), "base-relay-opt" : ("base_relay_opt", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt), "default-profile" : ("default_profile", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile), "match" : ("match", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match)}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")

                            self.base_match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch()
                            self.base_match.parent = self
                            self._children_name_map["base_match"] = "base-match"
                            self._children_yang_names.add("base-match")

                            self.base_relay_opt = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt()
                            self.base_relay_opt.parent = self
                            self._children_name_map["base_relay_opt"] = "base-relay-opt"
                            self._children_yang_names.add("base-relay-opt")

                            self.default_profile = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile()
                            self.default_profile.parent = self
                            self._children_name_map["default_profile"] = "default-profile"
                            self._children_yang_names.add("default-profile")

                            self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match()
                            self.match.parent = self
                            self._children_name_map["match"] = "match"
                            self._children_yang_names.add("match")
                            self._segment_path = lambda: "base"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base, ['enable'], name, value)


                        class BaseMatch(Entity):
                            """
                            Insert match keyword
                            
                            .. attribute:: options
                            
                            	Specify match option
                            	**type**\:   :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch, self).__init__()

                                self.yang_name = "base-match"
                                self.yang_parent_name = "base"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"options" : ("options", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options)}
                                self._child_list_classes = {}

                                self.options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options()
                                self.options.parent = self
                                self._children_name_map["options"] = "options"
                                self._children_yang_names.add("options")
                                self._segment_path = lambda: "base-match"


                            class Options(Entity):
                                """
                                Specify match option
                                
                                .. attribute:: option
                                
                                	none
                                	**type**\: list of    :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options, self).__init__()

                                    self.yang_name = "options"
                                    self.yang_parent_name = "base-match"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"option" : ("option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option)}

                                    self.option = YList(self)
                                    self._segment_path = lambda: "options"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options, [], name, value)


                                class Option(Entity):
                                    """
                                    none
                                    
                                    .. attribute:: opt60  <key>
                                    
                                    	none
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: opt60_hex_str  <key>
                                    
                                    	Enter hex pattern string
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: format  <key>
                                    
                                    	Set constant integer
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: option_profile
                                    
                                    	Enter a profile
                                    	**type**\:   :py:class:`OptionProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option, self).__init__()

                                        self.yang_name = "option"
                                        self.yang_parent_name = "options"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"option-profile" : ("option_profile", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile)}
                                        self._child_list_classes = {}

                                        self.opt60 = YLeaf(YType.int32, "opt60")

                                        self.opt60_hex_str = YLeaf(YType.str, "opt60-hex-str")

                                        self.format = YLeaf(YType.int32, "format")

                                        self.option_profile = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile()
                                        self.option_profile.parent = self
                                        self._children_name_map["option_profile"] = "option-profile"
                                        self._children_yang_names.add("option-profile")
                                        self._segment_path = lambda: "option" + "[opt60='" + self.opt60.get() + "']" + "[opt60-hex-str='" + self.opt60_hex_str.get() + "']" + "[format='" + self.format.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option, ['opt60', 'opt60_hex_str', 'format'], name, value)


                                    class OptionProfile(Entity):
                                        """
                                        Enter a profile
                                        
                                        .. attribute:: profile_mode
                                        
                                        	none
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: profile_name
                                        
                                        	Profile name
                                        	**type**\:  str
                                        
                                        	**length:** 1..64
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile, self).__init__()

                                            self.yang_name = "option-profile"
                                            self.yang_parent_name = "option"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.profile_mode = YLeaf(YType.int32, "profile-mode")

                                            self.profile_name = YLeaf(YType.str, "profile-name")
                                            self._segment_path = lambda: "option-profile"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile, ['profile_mode', 'profile_name'], name, value)


                        class BaseRelayOpt(Entity):
                            """
                            Insert Relay Agent Information circuit ID
                            and remote ID suboptions in client request
                            
                            .. attribute:: authenticate
                            
                            	Specify Relay Agent Information Option authenticate
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: remote_id
                            
                            	Enter remote\-id value
                            	**type**\:  str
                            
                            	**length:** 1..256
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt, self).__init__()

                                self.yang_name = "base-relay-opt"
                                self.yang_parent_name = "base"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.authenticate = YLeaf(YType.int32, "authenticate")

                                self.remote_id = YLeaf(YType.str, "remote-id")
                                self._segment_path = lambda: "base-relay-opt"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt, ['authenticate', 'remote_id'], name, value)


                        class DefaultProfile(Entity):
                            """
                            Enable the default profile
                            
                            .. attribute:: profile_mode
                            
                            	none
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: profile_name
                            
                            	Profile name
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile, self).__init__()

                                self.yang_name = "default-profile"
                                self.yang_parent_name = "base"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.profile_mode = YLeaf(YType.int32, "profile-mode")

                                self.profile_name = YLeaf(YType.str, "profile-name")
                                self._segment_path = lambda: "default-profile"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile, ['profile_mode', 'profile_name'], name, value)


                        class Match(Entity):
                            """
                            Insert match keyword
                            
                            .. attribute:: def_options
                            
                            	Table of Option
                            	**type**\:   :py:class:`DefOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions>`
                            
                            .. attribute:: option_filters
                            
                            	Table of Option
                            	**type**\:   :py:class:`OptionFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match, self).__init__()

                                self.yang_name = "match"
                                self.yang_parent_name = "base"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"def-options" : ("def_options", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions), "option-filters" : ("option_filters", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters)}
                                self._child_list_classes = {}

                                self.def_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions()
                                self.def_options.parent = self
                                self._children_name_map["def_options"] = "def-options"
                                self._children_yang_names.add("def-options")

                                self.option_filters = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters()
                                self.option_filters.parent = self
                                self._children_name_map["option_filters"] = "option-filters"
                                self._children_yang_names.add("option-filters")
                                self._segment_path = lambda: "match"


                            class DefOptions(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: def_option
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`DefOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions, self).__init__()

                                    self.yang_name = "def-options"
                                    self.yang_parent_name = "match"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"def-option" : ("def_option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption)}

                                    self.def_option = YList(self)
                                    self._segment_path = lambda: "def-options"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions, [], name, value)


                                class DefOption(Entity):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: def_matchoption  <key>
                                    
                                    	Match option 60
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: def_matchaction
                                    
                                    	Vendor action
                                    	**type**\:   :py:class:`BaseAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.BaseAction>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption, self).__init__()

                                        self.yang_name = "def-option"
                                        self.yang_parent_name = "def-options"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.def_matchoption = YLeaf(YType.int32, "def-matchoption")

                                        self.def_matchaction = YLeaf(YType.enumeration, "def-matchaction")
                                        self._segment_path = lambda: "def-option" + "[def-matchoption='" + self.def_matchoption.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption, ['def_matchoption', 'def_matchaction'], name, value)


                            class OptionFilters(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: option_filter
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`OptionFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters, self).__init__()

                                    self.yang_name = "option-filters"
                                    self.yang_parent_name = "match"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"option-filter" : ("option_filter", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter)}

                                    self.option_filter = YList(self)
                                    self._segment_path = lambda: "option-filters"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters, [], name, value)


                                class OptionFilter(Entity):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: matchoption  <key>
                                    
                                    	Match option 60
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: pattern  <key>
                                    
                                    	Enter hex pattern string
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: format  <key>
                                    
                                    	Set constant integer
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: option_action
                                    
                                    	Vendor action
                                    	**type**\:   :py:class:`BaseAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.BaseAction>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter, self).__init__()

                                        self.yang_name = "option-filter"
                                        self.yang_parent_name = "option-filters"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.matchoption = YLeaf(YType.int32, "matchoption")

                                        self.pattern = YLeaf(YType.str, "pattern")

                                        self.format = YLeaf(YType.int32, "format")

                                        self.option_action = YLeaf(YType.enumeration, "option-action")
                                        self._segment_path = lambda: "option-filter" + "[matchoption='" + self.matchoption.get() + "']" + "[pattern='" + self.pattern.get() + "']" + "[format='" + self.format.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter, ['matchoption', 'pattern', 'format', 'option_action'], name, value)


                    class Proxy(Entity):
                        """
                        DHCP proxy profile
                        
                        .. attribute:: auth_username
                        
                        	Authentication Username formating
                        	**type**\:   :py:class:`AuthUsername <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.AuthUsername>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: broadcast_flag
                        
                        	Specify broadcast flag
                        	**type**\:   :py:class:`BroadcastFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag>`
                        
                        .. attribute:: classes
                        
                        	DHCP class table
                        	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes>`
                        
                        .. attribute:: delayed_authen_proxy
                        
                        	For BNG session, delay the authentication
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: enable
                        
                        	DHCP IPV4 profile mode enable
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: giaddr
                        
                        	Specify gateway address policy
                        	**type**\:   :py:class:`Giaddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Giaddr>`
                        
                        .. attribute:: lease_proxy
                        
                        	DHCPv4 lease proxy
                        	**type**\:   :py:class:`LeaseProxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy>`
                        
                        .. attribute:: limit_lease
                        
                        	Proxy limit lease
                        	**type**\:   :py:class:`LimitLease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: match
                        
                        	Insert match keyword
                        	**type**\:   :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match>`
                        
                        .. attribute:: proxy_allow_move
                        
                        	Allow dhcp subscriber move
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: relay_information
                        
                        	Relay agent information option
                        	**type**\:   :py:class:`RelayInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation>`
                        
                        .. attribute:: secure_arp
                        
                        	DHCP IPV4 profile proxy secure\-arp enable
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: sessions
                        
                        	Change sessions configuration
                        	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions>`
                        
                        .. attribute:: vrfs
                        
                        	List of VRFs
                        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy, self).__init__()

                            self.yang_name = "proxy"
                            self.yang_parent_name = "mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"auth-username" : ("auth_username", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.AuthUsername), "broadcast-flag" : ("broadcast_flag", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag), "classes" : ("classes", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes), "giaddr" : ("giaddr", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Giaddr), "lease-proxy" : ("lease_proxy", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy), "limit-lease" : ("limit_lease", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease), "match" : ("match", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match), "relay-information" : ("relay_information", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation), "sessions" : ("sessions", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions), "vrfs" : ("vrfs", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs)}
                            self._child_list_classes = {}

                            self.delayed_authen_proxy = YLeaf(YType.empty, "delayed-authen-proxy")

                            self.enable = YLeaf(YType.empty, "enable")

                            self.proxy_allow_move = YLeaf(YType.empty, "proxy-allow-move")

                            self.secure_arp = YLeaf(YType.empty, "secure-arp")

                            self.auth_username = None
                            self._children_name_map["auth_username"] = "auth-username"
                            self._children_yang_names.add("auth-username")

                            self.broadcast_flag = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag()
                            self.broadcast_flag.parent = self
                            self._children_name_map["broadcast_flag"] = "broadcast-flag"
                            self._children_yang_names.add("broadcast-flag")

                            self.classes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes()
                            self.classes.parent = self
                            self._children_name_map["classes"] = "classes"
                            self._children_yang_names.add("classes")

                            self.giaddr = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Giaddr()
                            self.giaddr.parent = self
                            self._children_name_map["giaddr"] = "giaddr"
                            self._children_yang_names.add("giaddr")

                            self.lease_proxy = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy()
                            self.lease_proxy.parent = self
                            self._children_name_map["lease_proxy"] = "lease-proxy"
                            self._children_yang_names.add("lease-proxy")

                            self.limit_lease = None
                            self._children_name_map["limit_lease"] = "limit-lease"
                            self._children_yang_names.add("limit-lease")

                            self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match()
                            self.match.parent = self
                            self._children_name_map["match"] = "match"
                            self._children_yang_names.add("match")

                            self.relay_information = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation()
                            self.relay_information.parent = self
                            self._children_name_map["relay_information"] = "relay-information"
                            self._children_yang_names.add("relay-information")

                            self.sessions = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions()
                            self.sessions.parent = self
                            self._children_name_map["sessions"] = "sessions"
                            self._children_yang_names.add("sessions")

                            self.vrfs = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs()
                            self.vrfs.parent = self
                            self._children_name_map["vrfs"] = "vrfs"
                            self._children_yang_names.add("vrfs")
                            self._segment_path = lambda: "proxy"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy, ['delayed_authen_proxy', 'enable', 'proxy_allow_move', 'secure_arp'], name, value)


                        class AuthUsername(Entity):
                            """
                            Authentication Username formating
                            
                            .. attribute:: arg1
                            
                            	Username Formatting first argument 
                            	**type**\:   :py:class:`Dhcpv4AuthUsername <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Dhcpv4AuthUsername>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: arg2
                            
                            	Username Formatting second argument 
                            	**type**\:   :py:class:`Dhcpv4AuthUsername <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Dhcpv4AuthUsername>`
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.AuthUsername, self).__init__()

                                self.yang_name = "auth-username"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.arg1 = YLeaf(YType.enumeration, "arg1")

                                self.arg2 = YLeaf(YType.enumeration, "arg2")
                                self._segment_path = lambda: "auth-username"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.AuthUsername, ['arg1', 'arg2'], name, value)


                        class BroadcastFlag(Entity):
                            """
                            Specify broadcast flag
                            
                            .. attribute:: policy
                            
                            	Broadcast flag policy
                            	**type**\:   :py:class:`Ipv4dhcpdBroadcastFlagPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdBroadcastFlagPolicy>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag, self).__init__()

                                self.yang_name = "broadcast-flag"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.policy = YLeaf(YType.enumeration, "policy")
                                self._segment_path = lambda: "broadcast-flag"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag, ['policy'], name, value)


                        class Classes(Entity):
                            """
                            DHCP class table
                            
                            .. attribute:: class_
                            
                            	DHCP class
                            	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes, self).__init__()

                                self.yang_name = "classes"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"class" : ("class_", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_)}

                                self.class_ = YList(self)
                                self._segment_path = lambda: "classes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes, [], name, value)


                            class Class_(Entity):
                                """
                                DHCP class
                                
                                .. attribute:: class_name  <key>
                                
                                	Class name
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: enable
                                
                                	Enable the DHCP IPV4 proxy class
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: match
                                
                                	Match option
                                	**type**\:   :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match>`
                                
                                .. attribute:: vrfs
                                
                                	List of VRFs
                                	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_, self).__init__()

                                    self.yang_name = "class"
                                    self.yang_parent_name = "classes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"match" : ("match", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match), "vrfs" : ("vrfs", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs)}
                                    self._child_list_classes = {}

                                    self.class_name = YLeaf(YType.str, "class-name")

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match()
                                    self.match.parent = self
                                    self._children_name_map["match"] = "match"
                                    self._children_yang_names.add("match")

                                    self.vrfs = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs()
                                    self.vrfs.parent = self
                                    self._children_name_map["vrfs"] = "vrfs"
                                    self._children_yang_names.add("vrfs")
                                    self._segment_path = lambda: "class" + "[class-name='" + self.class_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_, ['class_name', 'enable'], name, value)


                                class Match(Entity):
                                    """
                                    Match option
                                    
                                    .. attribute:: option
                                    
                                    	Match option
                                    	**type**\:   :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option>`
                                    
                                    .. attribute:: vrf
                                    
                                    	Match VRF name
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match, self).__init__()

                                        self.yang_name = "match"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"option" : ("option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option)}
                                        self._child_list_classes = {}

                                        self.vrf = YLeaf(YType.str, "vrf")

                                        self.option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option()
                                        self.option.parent = self
                                        self._children_name_map["option"] = "option"
                                        self._children_yang_names.add("option")
                                        self._segment_path = lambda: "match"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match, ['vrf'], name, value)


                                    class Option(Entity):
                                        """
                                        Match option
                                        
                                        .. attribute:: bit_mask
                                        
                                        	Bit mask pattern
                                        	**type**\:  str
                                        
                                        .. attribute:: option_type
                                        
                                        	Match option
                                        	**type**\:   :py:class:`Dhcpv4MatchOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Dhcpv4MatchOption>`
                                        
                                        .. attribute:: pattern
                                        
                                        	Hex pattern string
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option, self).__init__()

                                            self.yang_name = "option"
                                            self.yang_parent_name = "match"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.bit_mask = YLeaf(YType.str, "bit-mask")

                                            self.option_type = YLeaf(YType.enumeration, "option-type")

                                            self.pattern = YLeaf(YType.str, "pattern")
                                            self._segment_path = lambda: "option"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option, ['bit_mask', 'option_type', 'pattern'], name, value)


                                class Vrfs(Entity):
                                    """
                                    List of VRFs
                                    
                                    .. attribute:: vrf
                                    
                                    	VRF name
                                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs, self).__init__()

                                        self.yang_name = "vrfs"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"vrf" : ("vrf", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf)}

                                        self.vrf = YList(self)
                                        self._segment_path = lambda: "vrfs"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs, [], name, value)


                                    class Vrf(Entity):
                                        """
                                        VRF name
                                        
                                        .. attribute:: vrf_name  <key>
                                        
                                        	VRF name
                                        	**type**\:  str
                                        
                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                        
                                        .. attribute:: helper_addresses
                                        
                                        	Helper addresses
                                        	**type**\:   :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf, self).__init__()

                                            self.yang_name = "vrf"
                                            self.yang_parent_name = "vrfs"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"helper-addresses" : ("helper_addresses", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses)}
                                            self._child_list_classes = {}

                                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                                            self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses()
                                            self.helper_addresses.parent = self
                                            self._children_name_map["helper_addresses"] = "helper-addresses"
                                            self._children_yang_names.add("helper-addresses")
                                            self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf, ['vrf_name'], name, value)


                                        class HelperAddresses(Entity):
                                            """
                                            Helper addresses
                                            
                                            .. attribute:: helper_address
                                            
                                            	Helper address
                                            	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                                            
                                            

                                            """

                                            _prefix = 'ipv4-dhcpd-cfg'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses, self).__init__()

                                                self.yang_name = "helper-addresses"
                                                self.yang_parent_name = "vrf"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {"helper-address" : ("helper_address", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress)}

                                                self.helper_address = YList(self)
                                                self._segment_path = lambda: "helper-addresses"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses, [], name, value)


                                            class HelperAddress(Entity):
                                                """
                                                Helper address
                                                
                                                .. attribute:: server_address  <key>
                                                
                                                	IPv4 address
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: gateway_address
                                                
                                                	Gateway address
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                	**mandatory**\: True
                                                
                                                

                                                """

                                                _prefix = 'ipv4-dhcpd-cfg'
                                                _revision = '2017-05-01'

                                                def __init__(self):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__init__()

                                                    self.yang_name = "helper-address"
                                                    self.yang_parent_name = "helper-addresses"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.server_address = YLeaf(YType.str, "server-address")

                                                    self.gateway_address = YLeaf(YType.str, "gateway-address")
                                                    self._segment_path = lambda: "helper-address" + "[server-address='" + self.server_address.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress, ['server_address', 'gateway_address'], name, value)


                        class Giaddr(Entity):
                            """
                            Specify gateway address policy
                            
                            .. attribute:: policy
                            
                            	Gateway address policy
                            	**type**\:   :py:class:`Ipv4dhcpdGiaddrPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdGiaddrPolicy>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Giaddr, self).__init__()

                                self.yang_name = "giaddr"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.policy = YLeaf(YType.enumeration, "policy")
                                self._segment_path = lambda: "giaddr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Giaddr, ['policy'], name, value)


                        class LeaseProxy(Entity):
                            """
                            DHCPv4 lease proxy
                            
                            .. attribute:: client_lease_time
                            
                            	Specify client lease proxy time
                            	**type**\:  int
                            
                            	**range:** 300..4294967295
                            
                            .. attribute:: set_server_options
                            
                            	Set DHCP server sent options in lease proxy generating ACK
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy, self).__init__()

                                self.yang_name = "lease-proxy"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.client_lease_time = YLeaf(YType.uint32, "client-lease-time")

                                self.set_server_options = YLeaf(YType.empty, "set-server-options")
                                self._segment_path = lambda: "lease-proxy"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy, ['client_lease_time', 'set_server_options'], name, value)


                        class LimitLease(Entity):
                            """
                            Proxy limit lease
                            
                            .. attribute:: limit_lease_count
                            
                            	Limit lease count
                            	**type**\:  int
                            
                            	**range:** 1..240000
                            
                            	**mandatory**\: True
                            
                            .. attribute:: limit_type
                            
                            	Lease limit type
                            	**type**\:   :py:class:`Dhcpv4LimitLease1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Dhcpv4LimitLease1>`
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease, self).__init__()

                                self.yang_name = "limit-lease"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.limit_lease_count = YLeaf(YType.uint32, "limit-lease-count")

                                self.limit_type = YLeaf(YType.enumeration, "limit-type")
                                self._segment_path = lambda: "limit-lease"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease, ['limit_lease_count', 'limit_type'], name, value)


                        class Match(Entity):
                            """
                            Insert match keyword
                            
                            .. attribute:: def_options
                            
                            	Table of Option
                            	**type**\:   :py:class:`DefOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions>`
                            
                            .. attribute:: option_filters
                            
                            	Table of Option
                            	**type**\:   :py:class:`OptionFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match, self).__init__()

                                self.yang_name = "match"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"def-options" : ("def_options", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions), "option-filters" : ("option_filters", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters)}
                                self._child_list_classes = {}

                                self.def_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions()
                                self.def_options.parent = self
                                self._children_name_map["def_options"] = "def-options"
                                self._children_yang_names.add("def-options")

                                self.option_filters = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters()
                                self.option_filters.parent = self
                                self._children_name_map["option_filters"] = "option-filters"
                                self._children_yang_names.add("option-filters")
                                self._segment_path = lambda: "match"


                            class DefOptions(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: def_option
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`DefOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions, self).__init__()

                                    self.yang_name = "def-options"
                                    self.yang_parent_name = "match"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"def-option" : ("def_option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption)}

                                    self.def_option = YList(self)
                                    self._segment_path = lambda: "def-options"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions, [], name, value)


                                class DefOption(Entity):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: def_matchoption  <key>
                                    
                                    	Match option 60
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: def_matchaction
                                    
                                    	Vendor action
                                    	**type**\:   :py:class:`ProxyAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.ProxyAction>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption, self).__init__()

                                        self.yang_name = "def-option"
                                        self.yang_parent_name = "def-options"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.def_matchoption = YLeaf(YType.int32, "def-matchoption")

                                        self.def_matchaction = YLeaf(YType.enumeration, "def-matchaction")
                                        self._segment_path = lambda: "def-option" + "[def-matchoption='" + self.def_matchoption.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption, ['def_matchoption', 'def_matchaction'], name, value)


                            class OptionFilters(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: option_filter
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`OptionFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters, self).__init__()

                                    self.yang_name = "option-filters"
                                    self.yang_parent_name = "match"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"option-filter" : ("option_filter", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter)}

                                    self.option_filter = YList(self)
                                    self._segment_path = lambda: "option-filters"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters, [], name, value)


                                class OptionFilter(Entity):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: matchoption  <key>
                                    
                                    	Match option 60
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: pattern  <key>
                                    
                                    	Enter hex pattern string
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: format  <key>
                                    
                                    	Set constant integer
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: matchaction
                                    
                                    	Vendor action
                                    	**type**\:   :py:class:`ProxyAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.ProxyAction>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter, self).__init__()

                                        self.yang_name = "option-filter"
                                        self.yang_parent_name = "option-filters"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.matchoption = YLeaf(YType.int32, "matchoption")

                                        self.pattern = YLeaf(YType.str, "pattern")

                                        self.format = YLeaf(YType.int32, "format")

                                        self.matchaction = YLeaf(YType.enumeration, "matchaction")
                                        self._segment_path = lambda: "option-filter" + "[matchoption='" + self.matchoption.get() + "']" + "[pattern='" + self.pattern.get() + "']" + "[format='" + self.format.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter, ['matchoption', 'pattern', 'format', 'matchaction'], name, value)


                        class RelayInformation(Entity):
                            """
                            Relay agent information option
                            
                            .. attribute:: allow_untrusted
                            
                            	Forward untrusted packets
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: authenticate
                            
                            	Relay information option authenticate
                            	**type**\:   :py:class:`Ipv4dhcpdRelayInfoOptionAuthenticate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdRelayInfoOptionAuthenticate>`
                            
                            .. attribute:: check
                            
                            	Check relay agent information option in server reply
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: circuit_id
                            
                            	Insert Circuit\-id sub\-option
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: option
                            
                            	Insert relay rgent information circuit ID and remote ID suboptions in client requests
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy
                            
                            	Relay information option policy
                            	**type**\:   :py:class:`Ipv4dhcpdRelayInfoOptionPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdRelayInfoOptionPolicy>`
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\:  str
                            
                            .. attribute:: remote_id_suppress
                            
                            	Suppress Remote ID
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: remote_id_xr
                            
                            	Insert Remote\-id sub\-option
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: vpn
                            
                            	Insert VPN options
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: vpn_mode
                            
                            	VPN Mode
                            	**type**\:   :py:class:`Ipv4dhcpdRelayInfoOptionvpnMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdRelayInfoOptionvpnMode>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation, self).__init__()

                                self.yang_name = "relay-information"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.allow_untrusted = YLeaf(YType.empty, "allow-untrusted")

                                self.authenticate = YLeaf(YType.enumeration, "authenticate")

                                self.check = YLeaf(YType.empty, "check")

                                self.circuit_id = YLeaf(YType.empty, "circuit-id")

                                self.option = YLeaf(YType.empty, "option")

                                self.policy = YLeaf(YType.enumeration, "policy")

                                self.remote_id = YLeaf(YType.str, "remote-id")

                                self.remote_id_suppress = YLeaf(YType.empty, "remote-id-suppress")

                                self.remote_id_xr = YLeaf(YType.empty, "remote-id-xr")

                                self.vpn = YLeaf(YType.empty, "vpn")

                                self.vpn_mode = YLeaf(YType.enumeration, "vpn-mode")
                                self._segment_path = lambda: "relay-information"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation, ['allow_untrusted', 'authenticate', 'check', 'circuit_id', 'option', 'policy', 'remote_id', 'remote_id_suppress', 'remote_id_xr', 'vpn', 'vpn_mode'], name, value)


                        class Sessions(Entity):
                            """
                            Change sessions configuration
                            
                            .. attribute:: proxy_throttle_type
                            
                            	Throttle DHCP sessions based on MAC address
                            	**type**\:   :py:class:`ProxyThrottleType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions, self).__init__()

                                self.yang_name = "sessions"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"proxy-throttle-type" : ("proxy_throttle_type", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType)}
                                self._child_list_classes = {}

                                self.proxy_throttle_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType()
                                self.proxy_throttle_type.parent = self
                                self._children_name_map["proxy_throttle_type"] = "proxy-throttle-type"
                                self._children_yang_names.add("proxy-throttle-type")
                                self._segment_path = lambda: "sessions"


                            class ProxyThrottleType(Entity):
                                """
                                Throttle DHCP sessions based on MAC
                                address
                                
                                .. attribute:: proxy_mac_throttle
                                
                                	Throttle DHCP sessions from any one MAC address
                                	**type**\:   :py:class:`ProxyMacThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType, self).__init__()

                                    self.yang_name = "proxy-throttle-type"
                                    self.yang_parent_name = "sessions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"proxy-mac-throttle" : ("proxy_mac_throttle", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle)}
                                    self._child_list_classes = {}

                                    self.proxy_mac_throttle = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle()
                                    self.proxy_mac_throttle.parent = self
                                    self._children_name_map["proxy_mac_throttle"] = "proxy-mac-throttle"
                                    self._children_yang_names.add("proxy-mac-throttle")
                                    self._segment_path = lambda: "proxy-throttle-type"


                                class ProxyMacThrottle(Entity):
                                    """
                                    Throttle DHCP sessions from any one MAC
                                    address
                                    
                                    .. attribute:: num_block
                                    
                                    	Throttle blocking period (in secs)
                                    	**type**\:  int
                                    
                                    	**range:** 1..100
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: num_discover
                                    
                                    	Number of discovers at which to throttle
                                    	**type**\:  int
                                    
                                    	**range:** 1..65535
                                    
                                    .. attribute:: num_request
                                    
                                    	Throttle request period (in secs)
                                    	**type**\:  int
                                    
                                    	**range:** 1..100
                                    
                                    	**units**\: second
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle, self).__init__()

                                        self.yang_name = "proxy-mac-throttle"
                                        self.yang_parent_name = "proxy-throttle-type"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.num_block = YLeaf(YType.uint32, "num-block")

                                        self.num_discover = YLeaf(YType.uint32, "num-discover")

                                        self.num_request = YLeaf(YType.uint32, "num-request")
                                        self._segment_path = lambda: "proxy-mac-throttle"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle, ['num_block', 'num_discover', 'num_request'], name, value)


                        class Vrfs(Entity):
                            """
                            List of VRFs
                            
                            .. attribute:: vrf
                            
                            	VRF name
                            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs, self).__init__()

                                self.yang_name = "vrfs"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"vrf" : ("vrf", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf)}

                                self.vrf = YList(self)
                                self._segment_path = lambda: "vrfs"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs, [], name, value)


                            class Vrf(Entity):
                                """
                                VRF name
                                
                                .. attribute:: vrf_name  <key>
                                
                                	VRF name
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: helper_addresses
                                
                                	Helper addresses
                                	**type**\:   :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf, self).__init__()

                                    self.yang_name = "vrf"
                                    self.yang_parent_name = "vrfs"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"helper-addresses" : ("helper_addresses", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses)}
                                    self._child_list_classes = {}

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                                    self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses()
                                    self.helper_addresses.parent = self
                                    self._children_name_map["helper_addresses"] = "helper-addresses"
                                    self._children_yang_names.add("helper-addresses")
                                    self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf, ['vrf_name'], name, value)


                                class HelperAddresses(Entity):
                                    """
                                    Helper addresses
                                    
                                    .. attribute:: helper_address
                                    
                                    	Helper address
                                    	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses, self).__init__()

                                        self.yang_name = "helper-addresses"
                                        self.yang_parent_name = "vrf"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"helper-address" : ("helper_address", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress)}

                                        self.helper_address = YList(self)
                                        self._segment_path = lambda: "helper-addresses"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses, [], name, value)


                                    class HelperAddress(Entity):
                                        """
                                        Helper address
                                        
                                        .. attribute:: server_address  <key>
                                        
                                        	IPv4 address
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: gateway_address
                                        
                                        	Gateway address
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__init__()

                                            self.yang_name = "helper-address"
                                            self.yang_parent_name = "helper-addresses"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.server_address = YLeaf(YType.str, "server-address")

                                            self.gateway_address = YLeaf(YType.str, "gateway-address")
                                            self._segment_path = lambda: "helper-address" + "[server-address='" + self.server_address.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, ['server_address', 'gateway_address'], name, value)


                    class Relay(Entity):
                        """
                        DHCP Relay profile
                        
                        .. attribute:: broadcast_policy
                        
                        	Broadcast Flag policy
                        	**type**\:   :py:class:`BroadcastPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy>`
                        
                        .. attribute:: gi_addr_policy
                        
                        	GIADDR policy
                        	**type**\:   :py:class:`GiAddrPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy>`
                        
                        .. attribute:: mac_mismatch_action
                        
                        	Action to take if L2 header source Mac and dhcp header mac address don't match
                        	**type**\:   :py:class:`MacMismatchAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.MacMismatchAction>`
                        
                        .. attribute:: relay_information_option
                        
                        	Relay agent information option
                        	**type**\:   :py:class:`RelayInformationOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption>`
                        
                        .. attribute:: vrfs
                        
                        	VRF Helper Addresses
                        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay, self).__init__()

                            self.yang_name = "relay"
                            self.yang_parent_name = "mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"broadcast-policy" : ("broadcast_policy", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy), "gi-addr-policy" : ("gi_addr_policy", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy), "relay-information-option" : ("relay_information_option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption), "vrfs" : ("vrfs", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs)}
                            self._child_list_classes = {}

                            self.mac_mismatch_action = YLeaf(YType.enumeration, "mac-mismatch-action")

                            self.broadcast_policy = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy()
                            self.broadcast_policy.parent = self
                            self._children_name_map["broadcast_policy"] = "broadcast-policy"
                            self._children_yang_names.add("broadcast-policy")

                            self.gi_addr_policy = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy()
                            self.gi_addr_policy.parent = self
                            self._children_name_map["gi_addr_policy"] = "gi-addr-policy"
                            self._children_yang_names.add("gi-addr-policy")

                            self.relay_information_option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption()
                            self.relay_information_option.parent = self
                            self._children_name_map["relay_information_option"] = "relay-information-option"
                            self._children_yang_names.add("relay-information-option")

                            self.vrfs = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs()
                            self.vrfs.parent = self
                            self._children_name_map["vrfs"] = "vrfs"
                            self._children_yang_names.add("vrfs")
                            self._segment_path = lambda: "relay"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay, ['mac_mismatch_action'], name, value)


                        class BroadcastPolicy(Entity):
                            """
                            Broadcast Flag policy
                            
                            .. attribute:: policy
                            
                            	Broadcast flag policy
                            	**type**\:   :py:class:`Ipv4dhcpdBroadcastFlagPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdBroadcastFlagPolicy>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy, self).__init__()

                                self.yang_name = "broadcast-policy"
                                self.yang_parent_name = "relay"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.policy = YLeaf(YType.enumeration, "policy")
                                self._segment_path = lambda: "broadcast-policy"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy, ['policy'], name, value)


                        class GiAddrPolicy(Entity):
                            """
                            GIADDR policy
                            
                            .. attribute:: policy
                            
                            	GIADDR policy
                            	**type**\:   :py:class:`Ipv4dhcpdGiaddrPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdGiaddrPolicy>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy, self).__init__()

                                self.yang_name = "gi-addr-policy"
                                self.yang_parent_name = "relay"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.policy = YLeaf(YType.enumeration, "policy")
                                self._segment_path = lambda: "gi-addr-policy"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy, ['policy'], name, value)


                        class RelayInformationOption(Entity):
                            """
                            Relay agent information option
                            
                            .. attribute:: allow_untrusted
                            
                            	Forward untrusted packets
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: check
                            
                            	Check Relay Agent Information Option in server reply
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: insert
                            
                            	Insert Relay Agent Information circuit ID and remote ID suboptions in client requests
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy
                            
                            	Relay information option policy
                            	**type**\:   :py:class:`Ipv4dhcpdRelayInfoOptionPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdRelayInfoOptionPolicy>`
                            
                            .. attribute:: subscriber_id
                            
                            	Subscriber ID
                            	**type**\:  str
                            
                            .. attribute:: vpn
                            
                            	Insert VPN options
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: vpn_mode
                            
                            	VPN Mode
                            	**type**\:   :py:class:`Ipv4dhcpdRelayInfoOptionvpnMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdRelayInfoOptionvpnMode>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption, self).__init__()

                                self.yang_name = "relay-information-option"
                                self.yang_parent_name = "relay"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.allow_untrusted = YLeaf(YType.empty, "allow-untrusted")

                                self.check = YLeaf(YType.empty, "check")

                                self.insert = YLeaf(YType.empty, "insert")

                                self.policy = YLeaf(YType.enumeration, "policy")

                                self.subscriber_id = YLeaf(YType.str, "subscriber-id")

                                self.vpn = YLeaf(YType.empty, "vpn")

                                self.vpn_mode = YLeaf(YType.enumeration, "vpn-mode")
                                self._segment_path = lambda: "relay-information-option"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption, ['allow_untrusted', 'check', 'insert', 'policy', 'subscriber_id', 'vpn', 'vpn_mode'], name, value)


                        class Vrfs(Entity):
                            """
                            VRF Helper Addresses
                            
                            .. attribute:: vrf
                            
                            	VRF Name
                            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs, self).__init__()

                                self.yang_name = "vrfs"
                                self.yang_parent_name = "relay"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"vrf" : ("vrf", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf)}

                                self.vrf = YList(self)
                                self._segment_path = lambda: "vrfs"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs, [], name, value)


                            class Vrf(Entity):
                                """
                                VRF Name
                                
                                .. attribute:: vrf_name  <key>
                                
                                	VRF Name
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: helper_addresses
                                
                                	Helper Addresses
                                	**type**\:   :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf, self).__init__()

                                    self.yang_name = "vrf"
                                    self.yang_parent_name = "vrfs"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"helper-addresses" : ("helper_addresses", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses)}
                                    self._child_list_classes = {}

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                                    self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses()
                                    self.helper_addresses.parent = self
                                    self._children_name_map["helper_addresses"] = "helper-addresses"
                                    self._children_yang_names.add("helper-addresses")
                                    self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf, ['vrf_name'], name, value)


                                class HelperAddresses(Entity):
                                    """
                                    Helper Addresses
                                    
                                    .. attribute:: helper_address
                                    
                                    	Helper Address
                                    	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses, self).__init__()

                                        self.yang_name = "helper-addresses"
                                        self.yang_parent_name = "vrf"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"helper-address" : ("helper_address", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress)}

                                        self.helper_address = YList(self)
                                        self._segment_path = lambda: "helper-addresses"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses, [], name, value)


                                    class HelperAddress(Entity):
                                        """
                                        Helper Address
                                        
                                        .. attribute:: ip_address  <key>
                                        
                                        	IPV4 Address
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: enable
                                        
                                        	Enable helper \- deprecated
                                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: gateway_address
                                        
                                        	GatewayAddress
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__init__()

                                            self.yang_name = "helper-address"
                                            self.yang_parent_name = "helper-addresses"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.ip_address = YLeaf(YType.str, "ip-address")

                                            self.enable = YLeaf(YType.empty, "enable")

                                            self.gateway_address = YLeaf(YType.str, "gateway-address")
                                            self._segment_path = lambda: "helper-address" + "[ip-address='" + self.ip_address.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress, ['ip_address', 'enable', 'gateway_address'], name, value)


                    class Server(Entity):
                        """
                        DHCP Server profile
                        
                        .. attribute:: aaa_server
                        
                        	Enable aaa dhcp option force\-insert
                        	**type**\:   :py:class:`AaaServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer>`
                        
                        .. attribute:: boot_filename
                        
                        	Boot Filename
                        	**type**\:  str
                        
                        	**length:** 1..128
                        
                        .. attribute:: broadcast_flag
                        
                        	None
                        	**type**\:   :py:class:`BroadcastFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag>`
                        
                        .. attribute:: classes
                        
                        	Table of Class
                        	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes>`
                        
                        .. attribute:: default_routers
                        
                        	default routers
                        	**type**\:   :py:class:`DefaultRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters>`
                        
                        .. attribute:: dns_servers
                        
                        	DNS servers
                        	**type**\:   :py:class:`DnsServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers>`
                        
                        .. attribute:: domain_name
                        
                        	Domain name
                        	**type**\:  str
                        
                        	**length:** 1..256
                        
                        .. attribute:: infinite_lease
                        
                        	Infinite lease
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: lease
                        
                        	lease
                        	**type**\:   :py:class:`Lease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease>`
                        
                        .. attribute:: lease_limit
                        
                        	Specify limit lease
                        	**type**\:   :py:class:`LeaseLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit>`
                        
                        .. attribute:: match
                        
                        	Insert match keyword
                        	**type**\:   :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match>`
                        
                        .. attribute:: net_bios_name_servers
                        
                        	NetBIOS name servers
                        	**type**\:   :py:class:`NetBiosNameServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers>`
                        
                        .. attribute:: netbios_node_type
                        
                        	NetBIOS node type
                        	**type**\:   :py:class:`NetbiosNodeType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType>`
                        
                        .. attribute:: next_server
                        
                        	Configure the tftp\-server IP to be used by the client
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: option_codes
                        
                        	Table of OptionCode
                        	**type**\:   :py:class:`OptionCodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes>`
                        
                        .. attribute:: pool
                        
                        	Specify the Pool name
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: relay
                        
                        	Specify Relay Agent Information Option configuration
                        	**type**\:   :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay>`
                        
                        .. attribute:: requested_ip_address
                        
                        	Validate Requested IP Address
                        	**type**\:   :py:class:`RequestedIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress>`
                        
                        .. attribute:: secure_arp
                        
                        	Enable Secure Arp
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: server_allow_move
                        
                        	Allow dhcp subscriber move
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: server_id_check
                        
                        	Validate server ID check
                        	**type**\:   :py:class:`ServerIdCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck>`
                        
                        .. attribute:: session
                        
                        	Change sessions configuration
                        	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session>`
                        
                        .. attribute:: subnet_mask
                        
                        	Configure Subnet Mask
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server, self).__init__()

                            self.yang_name = "server"
                            self.yang_parent_name = "mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"aaa-server" : ("aaa_server", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer), "broadcast-flag" : ("broadcast_flag", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag), "classes" : ("classes", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes), "default-routers" : ("default_routers", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters), "dns-servers" : ("dns_servers", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers), "lease" : ("lease", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease), "lease-limit" : ("lease_limit", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit), "match" : ("match", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match), "net-bios-name-servers" : ("net_bios_name_servers", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers), "netbios-node-type" : ("netbios_node_type", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType), "option-codes" : ("option_codes", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes), "relay" : ("relay", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay), "requested-ip-address" : ("requested_ip_address", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress), "server-id-check" : ("server_id_check", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck), "session" : ("session", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session)}
                            self._child_list_classes = {}

                            self.boot_filename = YLeaf(YType.str, "boot-filename")

                            self.domain_name = YLeaf(YType.str, "domain-name")

                            self.infinite_lease = YLeaf(YType.empty, "infinite-lease")

                            self.next_server = YLeaf(YType.str, "next-server")

                            self.pool = YLeaf(YType.str, "pool")

                            self.secure_arp = YLeaf(YType.empty, "secure-arp")

                            self.server_allow_move = YLeaf(YType.empty, "server-allow-move")

                            self.subnet_mask = YLeaf(YType.str, "subnet-mask")

                            self.aaa_server = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer()
                            self.aaa_server.parent = self
                            self._children_name_map["aaa_server"] = "aaa-server"
                            self._children_yang_names.add("aaa-server")

                            self.broadcast_flag = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag()
                            self.broadcast_flag.parent = self
                            self._children_name_map["broadcast_flag"] = "broadcast-flag"
                            self._children_yang_names.add("broadcast-flag")

                            self.classes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes()
                            self.classes.parent = self
                            self._children_name_map["classes"] = "classes"
                            self._children_yang_names.add("classes")

                            self.default_routers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters()
                            self.default_routers.parent = self
                            self._children_name_map["default_routers"] = "default-routers"
                            self._children_yang_names.add("default-routers")

                            self.dns_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers()
                            self.dns_servers.parent = self
                            self._children_name_map["dns_servers"] = "dns-servers"
                            self._children_yang_names.add("dns-servers")

                            self.lease = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease()
                            self.lease.parent = self
                            self._children_name_map["lease"] = "lease"
                            self._children_yang_names.add("lease")

                            self.lease_limit = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit()
                            self.lease_limit.parent = self
                            self._children_name_map["lease_limit"] = "lease-limit"
                            self._children_yang_names.add("lease-limit")

                            self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match()
                            self.match.parent = self
                            self._children_name_map["match"] = "match"
                            self._children_yang_names.add("match")

                            self.net_bios_name_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers()
                            self.net_bios_name_servers.parent = self
                            self._children_name_map["net_bios_name_servers"] = "net-bios-name-servers"
                            self._children_yang_names.add("net-bios-name-servers")

                            self.netbios_node_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType()
                            self.netbios_node_type.parent = self
                            self._children_name_map["netbios_node_type"] = "netbios-node-type"
                            self._children_yang_names.add("netbios-node-type")

                            self.option_codes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes()
                            self.option_codes.parent = self
                            self._children_name_map["option_codes"] = "option-codes"
                            self._children_yang_names.add("option-codes")

                            self.relay = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay()
                            self.relay.parent = self
                            self._children_name_map["relay"] = "relay"
                            self._children_yang_names.add("relay")

                            self.requested_ip_address = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress()
                            self.requested_ip_address.parent = self
                            self._children_name_map["requested_ip_address"] = "requested-ip-address"
                            self._children_yang_names.add("requested-ip-address")

                            self.server_id_check = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck()
                            self.server_id_check.parent = self
                            self._children_name_map["server_id_check"] = "server-id-check"
                            self._children_yang_names.add("server-id-check")

                            self.session = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session()
                            self.session.parent = self
                            self._children_name_map["session"] = "session"
                            self._children_yang_names.add("session")
                            self._segment_path = lambda: "server"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server, ['boot_filename', 'domain_name', 'infinite_lease', 'next_server', 'pool', 'secure_arp', 'server_allow_move', 'subnet_mask'], name, value)


                        class AaaServer(Entity):
                            """
                            Enable aaa dhcp option force\-insert
                            
                            .. attribute:: dhcp_option
                            
                            	Enable aaa dhcp option force\-insert
                            	**type**\:   :py:class:`DhcpOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer.DhcpOption>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer, self).__init__()

                                self.yang_name = "aaa-server"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"dhcp-option" : ("dhcp_option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer.DhcpOption)}
                                self._child_list_classes = {}

                                self.dhcp_option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer.DhcpOption()
                                self.dhcp_option.parent = self
                                self._children_name_map["dhcp_option"] = "dhcp-option"
                                self._children_yang_names.add("dhcp-option")
                                self._segment_path = lambda: "aaa-server"


                            class DhcpOption(Entity):
                                """
                                Enable aaa dhcp option force\-insert
                                
                                .. attribute:: force_insert
                                
                                	Enable aaa dhcp option force\-insert
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer.DhcpOption, self).__init__()

                                    self.yang_name = "dhcp-option"
                                    self.yang_parent_name = "aaa-server"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.force_insert = YLeaf(YType.empty, "force-insert")
                                    self._segment_path = lambda: "dhcp-option"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer.DhcpOption, ['force_insert'], name, value)


                        class BroadcastFlag(Entity):
                            """
                            None
                            
                            .. attribute:: policy
                            
                            	Specify broadcast flag policy
                            	**type**\:   :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Policy>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag, self).__init__()

                                self.yang_name = "broadcast-flag"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.policy = YLeaf(YType.enumeration, "policy")
                                self._segment_path = lambda: "broadcast-flag"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag, ['policy'], name, value)


                        class Classes(Entity):
                            """
                            Table of Class
                            
                            .. attribute:: class_
                            
                            	Create or enter server profile class
                            	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes, self).__init__()

                                self.yang_name = "classes"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"class" : ("class_", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_)}

                                self.class_ = YList(self)
                                self._segment_path = lambda: "classes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes, [], name, value)


                            class Class_(Entity):
                                """
                                Create or enter server profile class
                                
                                .. attribute:: class_name  <key>
                                
                                	class name
                                	**type**\:  str
                                
                                	**length:** 1..128
                                
                                .. attribute:: boot_filename
                                
                                	Boot Filename
                                	**type**\:  str
                                
                                	**length:** 1..128
                                
                                .. attribute:: class_match
                                
                                	Insert match keyword
                                	**type**\:   :py:class:`ClassMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch>`
                                
                                .. attribute:: default_routers
                                
                                	default routers
                                	**type**\:   :py:class:`DefaultRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters>`
                                
                                .. attribute:: dns_servers
                                
                                	DNS servers
                                	**type**\:   :py:class:`DnsServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers>`
                                
                                .. attribute:: domain_name
                                
                                	Domain name
                                	**type**\:  str
                                
                                	**length:** 1..256
                                
                                .. attribute:: enable
                                
                                	Enable Create or enter server profile class. Deletion of this object also causes deletion of all associated objects under Class
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: infinite_lease
                                
                                	Infinite lease
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: lease
                                
                                	lease
                                	**type**\:   :py:class:`Lease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease>`
                                
                                .. attribute:: net_bios_name_servers
                                
                                	NetBIOS name servers
                                	**type**\:   :py:class:`NetBiosNameServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers>`
                                
                                .. attribute:: netbios_node_type
                                
                                	NetBIOS node type
                                	**type**\:   :py:class:`NetbiosNodeType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType>`
                                
                                .. attribute:: next_server
                                
                                	Configure the tftp\-server IP to be used by the client
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: option_codes
                                
                                	Table of OptionCode
                                	**type**\:   :py:class:`OptionCodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes>`
                                
                                .. attribute:: pool
                                
                                	Specify the pool
                                	**type**\:  str
                                
                                .. attribute:: subnet_mask
                                
                                	Configure Subnet Mask
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_, self).__init__()

                                    self.yang_name = "class"
                                    self.yang_parent_name = "classes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"class-match" : ("class_match", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch), "default-routers" : ("default_routers", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters), "dns-servers" : ("dns_servers", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers), "lease" : ("lease", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease), "net-bios-name-servers" : ("net_bios_name_servers", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers), "netbios-node-type" : ("netbios_node_type", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType), "option-codes" : ("option_codes", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes)}
                                    self._child_list_classes = {}

                                    self.class_name = YLeaf(YType.str, "class-name")

                                    self.boot_filename = YLeaf(YType.str, "boot-filename")

                                    self.domain_name = YLeaf(YType.str, "domain-name")

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.infinite_lease = YLeaf(YType.empty, "infinite-lease")

                                    self.next_server = YLeaf(YType.str, "next-server")

                                    self.pool = YLeaf(YType.str, "pool")

                                    self.subnet_mask = YLeaf(YType.str, "subnet-mask")

                                    self.class_match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch()
                                    self.class_match.parent = self
                                    self._children_name_map["class_match"] = "class-match"
                                    self._children_yang_names.add("class-match")

                                    self.default_routers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters()
                                    self.default_routers.parent = self
                                    self._children_name_map["default_routers"] = "default-routers"
                                    self._children_yang_names.add("default-routers")

                                    self.dns_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers()
                                    self.dns_servers.parent = self
                                    self._children_name_map["dns_servers"] = "dns-servers"
                                    self._children_yang_names.add("dns-servers")

                                    self.lease = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease()
                                    self.lease.parent = self
                                    self._children_name_map["lease"] = "lease"
                                    self._children_yang_names.add("lease")

                                    self.net_bios_name_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers()
                                    self.net_bios_name_servers.parent = self
                                    self._children_name_map["net_bios_name_servers"] = "net-bios-name-servers"
                                    self._children_yang_names.add("net-bios-name-servers")

                                    self.netbios_node_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType()
                                    self.netbios_node_type.parent = self
                                    self._children_name_map["netbios_node_type"] = "netbios-node-type"
                                    self._children_yang_names.add("netbios-node-type")

                                    self.option_codes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes()
                                    self.option_codes.parent = self
                                    self._children_name_map["option_codes"] = "option-codes"
                                    self._children_yang_names.add("option-codes")
                                    self._segment_path = lambda: "class" + "[class-name='" + self.class_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_, ['class_name', 'boot_filename', 'domain_name', 'enable', 'infinite_lease', 'next_server', 'pool', 'subnet_mask'], name, value)


                                class ClassMatch(Entity):
                                    """
                                    Insert match keyword
                                    
                                    .. attribute:: class_options
                                    
                                    	Table of Class\-Option
                                    	**type**\:   :py:class:`ClassOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions>`
                                    
                                    .. attribute:: l2_interface
                                    
                                    	Specify match l2\-interface
                                    	**type**\:  str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                                    
                                    .. attribute:: vrf
                                    
                                    	Specify match VRF
                                    	**type**\:  str
                                    
                                    	**length:** 1..32
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch, self).__init__()

                                        self.yang_name = "class-match"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"class-options" : ("class_options", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions)}
                                        self._child_list_classes = {}

                                        self.l2_interface = YLeaf(YType.str, "l2-interface")

                                        self.vrf = YLeaf(YType.str, "vrf")

                                        self.class_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions()
                                        self.class_options.parent = self
                                        self._children_name_map["class_options"] = "class-options"
                                        self._children_yang_names.add("class-options")
                                        self._segment_path = lambda: "class-match"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch, ['l2_interface', 'vrf'], name, value)


                                    class ClassOptions(Entity):
                                        """
                                        Table of Class\-Option
                                        
                                        .. attribute:: class_option
                                        
                                        	Specify match option
                                        	**type**\: list of    :py:class:`ClassOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions, self).__init__()

                                            self.yang_name = "class-options"
                                            self.yang_parent_name = "class-match"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"class-option" : ("class_option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption)}

                                            self.class_option = YList(self)
                                            self._segment_path = lambda: "class-options"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions, [], name, value)


                                        class ClassOption(Entity):
                                            """
                                            Specify match option
                                            
                                            .. attribute:: matchoption  <key>
                                            
                                            	Match options
                                            	**type**\:   :py:class:`Matchoption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Matchoption>`
                                            
                                            .. attribute:: bit_mask
                                            
                                            	Enter bit mask pattern string
                                            	**type**\:  str
                                            
                                            	**length:** 1..64
                                            
                                            .. attribute:: pattern
                                            
                                            	Enter hex pattern string
                                            	**type**\:  str
                                            
                                            	**length:** 1..64
                                            
                                            

                                            """

                                            _prefix = 'ipv4-dhcpd-cfg'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption, self).__init__()

                                                self.yang_name = "class-option"
                                                self.yang_parent_name = "class-options"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.matchoption = YLeaf(YType.enumeration, "matchoption")

                                                self.bit_mask = YLeaf(YType.str, "bit-mask")

                                                self.pattern = YLeaf(YType.str, "pattern")
                                                self._segment_path = lambda: "class-option" + "[matchoption='" + self.matchoption.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption, ['matchoption', 'bit_mask', 'pattern'], name, value)


                                class DefaultRouters(Entity):
                                    """
                                    default routers
                                    
                                    .. attribute:: default_router
                                    
                                    	Router's IP address
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters, self).__init__()

                                        self.yang_name = "default-routers"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.default_router = YLeafList(YType.str, "default-router")
                                        self._segment_path = lambda: "default-routers"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters, ['default_router'], name, value)


                                class DnsServers(Entity):
                                    """
                                    DNS servers
                                    
                                    .. attribute:: dns_server
                                    
                                    	DNS Server's IP address
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers, self).__init__()

                                        self.yang_name = "dns-servers"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.dns_server = YLeafList(YType.str, "dns-server")
                                        self._segment_path = lambda: "dns-servers"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers, ['dns_server'], name, value)


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
                                    
                                    	**range:** 0..59
                                    
                                    	**units**\: minute
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease, self).__init__()

                                        self.yang_name = "lease"
                                        self.yang_parent_name = "class"
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
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease, ['days', 'hours', 'infinite', 'minutes'], name, value)


                                class NetBiosNameServers(Entity):
                                    """
                                    NetBIOS name servers
                                    
                                    .. attribute:: net_bios_name_server
                                    
                                    	NetBIOSNameServer's IP address
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers, self).__init__()

                                        self.yang_name = "net-bios-name-servers"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.net_bios_name_server = YLeafList(YType.str, "net-bios-name-server")
                                        self._segment_path = lambda: "net-bios-name-servers"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers, ['net_bios_name_server'], name, value)


                                class NetbiosNodeType(Entity):
                                    """
                                    NetBIOS node type
                                    
                                    .. attribute:: broadcast_node
                                    
                                    	Set string
                                    	**type**\:  str
                                    
                                    .. attribute:: hexadecimal
                                    
                                    	Hexadecimal number
                                    	**type**\:  str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                                    
                                    .. attribute:: hybrid_node
                                    
                                    	Set string
                                    	**type**\:  str
                                    
                                    .. attribute:: mixed_node
                                    
                                    	Set string
                                    	**type**\:  str
                                    
                                    .. attribute:: peer_to_peer_node
                                    
                                    	Set string
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType, self).__init__()

                                        self.yang_name = "netbios-node-type"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.broadcast_node = YLeaf(YType.str, "broadcast-node")

                                        self.hexadecimal = YLeaf(YType.str, "hexadecimal")

                                        self.hybrid_node = YLeaf(YType.str, "hybrid-node")

                                        self.mixed_node = YLeaf(YType.str, "mixed-node")

                                        self.peer_to_peer_node = YLeaf(YType.str, "peer-to-peer-node")
                                        self._segment_path = lambda: "netbios-node-type"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType, ['broadcast_node', 'hexadecimal', 'hybrid_node', 'mixed_node', 'peer_to_peer_node'], name, value)


                                class OptionCodes(Entity):
                                    """
                                    Table of OptionCode
                                    
                                    .. attribute:: option_code
                                    
                                    	DHCP option code
                                    	**type**\: list of    :py:class:`OptionCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes, self).__init__()

                                        self.yang_name = "option-codes"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"option-code" : ("option_code", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode)}

                                        self.option_code = YList(self)
                                        self._segment_path = lambda: "option-codes"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes, [], name, value)


                                    class OptionCode(Entity):
                                        """
                                        DHCP option code
                                        
                                        .. attribute:: option_code  <key>
                                        
                                        	DHCP option code
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: ascii_string
                                        
                                        	ASCII string
                                        	**type**\:  str
                                        
                                        .. attribute:: force_insert
                                        
                                        	Set constant integer
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        .. attribute:: hex_string
                                        
                                        	Hexadecimal string
                                        	**type**\:  str
                                        
                                        .. attribute:: ip_address
                                        
                                        	Server's IP address
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode, self).__init__()

                                            self.yang_name = "option-code"
                                            self.yang_parent_name = "option-codes"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.option_code = YLeaf(YType.uint32, "option-code")

                                            self.ascii_string = YLeaf(YType.str, "ascii-string")

                                            self.force_insert = YLeaf(YType.int32, "force-insert")

                                            self.hex_string = YLeaf(YType.str, "hex-string")

                                            self.ip_address = YLeafList(YType.str, "ip-address")
                                            self._segment_path = lambda: "option-code" + "[option-code='" + self.option_code.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode, ['option_code', 'ascii_string', 'force_insert', 'hex_string', 'ip_address'], name, value)


                        class DefaultRouters(Entity):
                            """
                            default routers
                            
                            .. attribute:: default_router
                            
                            	Router's IP address
                            	**type**\:  list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters, self).__init__()

                                self.yang_name = "default-routers"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.default_router = YLeafList(YType.str, "default-router")
                                self._segment_path = lambda: "default-routers"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters, ['default_router'], name, value)


                        class DnsServers(Entity):
                            """
                            DNS servers
                            
                            .. attribute:: dns_server
                            
                            	DNS Server's IP address
                            	**type**\:  list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers, self).__init__()

                                self.yang_name = "dns-servers"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.dns_server = YLeafList(YType.str, "dns-server")
                                self._segment_path = lambda: "dns-servers"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers, ['dns_server'], name, value)


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
                            
                            	**range:** 0..59
                            
                            	**units**\: minute
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease, self).__init__()

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
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease, ['days', 'hours', 'infinite', 'minutes'], name, value)


                        class LeaseLimit(Entity):
                            """
                            Specify limit lease
                            
                            .. attribute:: lease_limit_value
                            
                            	Configure Lease limit value
                            	**type**\:   :py:class:`LeaseLimitValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.LeaseLimitValue>`
                            
                            .. attribute:: range
                            
                            	Value of limit lease count in Decimal
                            	**type**\:  int
                            
                            	**range:** 1..240000
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit, self).__init__()

                                self.yang_name = "lease-limit"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.lease_limit_value = YLeaf(YType.enumeration, "lease-limit-value")

                                self.range = YLeaf(YType.uint32, "range")
                                self._segment_path = lambda: "lease-limit"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit, ['lease_limit_value', 'range'], name, value)


                        class Match(Entity):
                            """
                            Insert match keyword
                            
                            .. attribute:: option_defaults
                            
                            	Table of OptionDefault
                            	**type**\:   :py:class:`OptionDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults>`
                            
                            .. attribute:: options
                            
                            	Table of Option
                            	**type**\:   :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match, self).__init__()

                                self.yang_name = "match"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"option-defaults" : ("option_defaults", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults), "options" : ("options", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options)}
                                self._child_list_classes = {}

                                self.option_defaults = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults()
                                self.option_defaults.parent = self
                                self._children_name_map["option_defaults"] = "option-defaults"
                                self._children_yang_names.add("option-defaults")

                                self.options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options()
                                self.options.parent = self
                                self._children_name_map["options"] = "options"
                                self._children_yang_names.add("options")
                                self._segment_path = lambda: "match"


                            class OptionDefaults(Entity):
                                """
                                Table of OptionDefault
                                
                                .. attribute:: option_default
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`OptionDefault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults, self).__init__()

                                    self.yang_name = "option-defaults"
                                    self.yang_parent_name = "match"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"option-default" : ("option_default", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault)}

                                    self.option_default = YList(self)
                                    self._segment_path = lambda: "option-defaults"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults, [], name, value)


                                class OptionDefault(Entity):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: matchoption  <key>
                                    
                                    	Match option 60
                                    	**type**\:   :py:class:`Matchoption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Matchoption>`
                                    
                                    .. attribute:: matchaction
                                    
                                    	Vendor action
                                    	**type**\:   :py:class:`Matchaction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Matchaction>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault, self).__init__()

                                        self.yang_name = "option-default"
                                        self.yang_parent_name = "option-defaults"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.matchoption = YLeaf(YType.enumeration, "matchoption")

                                        self.matchaction = YLeaf(YType.enumeration, "matchaction")
                                        self._segment_path = lambda: "option-default" + "[matchoption='" + self.matchoption.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault, ['matchoption', 'matchaction'], name, value)


                            class Options(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: option
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options, self).__init__()

                                    self.yang_name = "options"
                                    self.yang_parent_name = "match"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"option" : ("option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option)}

                                    self.option = YList(self)
                                    self._segment_path = lambda: "options"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options, [], name, value)


                                class Option(Entity):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: matchoption  <key>
                                    
                                    	Match option 60
                                    	**type**\:   :py:class:`Matchoption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Matchoption>`
                                    
                                    .. attribute:: pattern  <key>
                                    
                                    	Enter hex pattern string
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: format  <key>
                                    
                                    	Set constant integer
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: matchaction
                                    
                                    	Vendor action
                                    	**type**\:   :py:class:`Matchaction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Matchaction>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option, self).__init__()

                                        self.yang_name = "option"
                                        self.yang_parent_name = "options"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.matchoption = YLeaf(YType.enumeration, "matchoption")

                                        self.pattern = YLeaf(YType.str, "pattern")

                                        self.format = YLeaf(YType.int32, "format")

                                        self.matchaction = YLeaf(YType.enumeration, "matchaction")
                                        self._segment_path = lambda: "option" + "[matchoption='" + self.matchoption.get() + "']" + "[pattern='" + self.pattern.get() + "']" + "[format='" + self.format.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option, ['matchoption', 'pattern', 'format', 'matchaction'], name, value)


                        class NetBiosNameServers(Entity):
                            """
                            NetBIOS name servers
                            
                            .. attribute:: net_bios_name_server
                            
                            	NetBIOSNameServer's IP address
                            	**type**\:  list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers, self).__init__()

                                self.yang_name = "net-bios-name-servers"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.net_bios_name_server = YLeafList(YType.str, "net-bios-name-server")
                                self._segment_path = lambda: "net-bios-name-servers"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers, ['net_bios_name_server'], name, value)


                        class NetbiosNodeType(Entity):
                            """
                            NetBIOS node type
                            
                            .. attribute:: broadcast_node
                            
                            	Set string
                            	**type**\:  str
                            
                            .. attribute:: hexadecimal
                            
                            	Hexadecimal number
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: hybrid_node
                            
                            	Set string
                            	**type**\:  str
                            
                            .. attribute:: mixed_node
                            
                            	Set string
                            	**type**\:  str
                            
                            .. attribute:: peer_to_peer_node
                            
                            	Set string
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType, self).__init__()

                                self.yang_name = "netbios-node-type"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.broadcast_node = YLeaf(YType.str, "broadcast-node")

                                self.hexadecimal = YLeaf(YType.str, "hexadecimal")

                                self.hybrid_node = YLeaf(YType.str, "hybrid-node")

                                self.mixed_node = YLeaf(YType.str, "mixed-node")

                                self.peer_to_peer_node = YLeaf(YType.str, "peer-to-peer-node")
                                self._segment_path = lambda: "netbios-node-type"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType, ['broadcast_node', 'hexadecimal', 'hybrid_node', 'mixed_node', 'peer_to_peer_node'], name, value)


                        class OptionCodes(Entity):
                            """
                            Table of OptionCode
                            
                            .. attribute:: option_code
                            
                            	DHCP option code
                            	**type**\: list of    :py:class:`OptionCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes, self).__init__()

                                self.yang_name = "option-codes"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"option-code" : ("option_code", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode)}

                                self.option_code = YList(self)
                                self._segment_path = lambda: "option-codes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes, [], name, value)


                            class OptionCode(Entity):
                                """
                                DHCP option code
                                
                                .. attribute:: option_code  <key>
                                
                                	DHCP option code
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: ascii_string
                                
                                	ASCII string
                                	**type**\:  str
                                
                                .. attribute:: force_insert
                                
                                	Set constant integer
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: hex_string
                                
                                	Hexadecimal string
                                	**type**\:  str
                                
                                .. attribute:: ip_address
                                
                                	Server's IP address
                                	**type**\:  list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode, self).__init__()

                                    self.yang_name = "option-code"
                                    self.yang_parent_name = "option-codes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.option_code = YLeaf(YType.uint32, "option-code")

                                    self.ascii_string = YLeaf(YType.str, "ascii-string")

                                    self.force_insert = YLeaf(YType.int32, "force-insert")

                                    self.hex_string = YLeaf(YType.str, "hex-string")

                                    self.ip_address = YLeafList(YType.str, "ip-address")
                                    self._segment_path = lambda: "option-code" + "[option-code='" + self.option_code.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode, ['option_code', 'ascii_string', 'force_insert', 'hex_string', 'ip_address'], name, value)


                        class Relay(Entity):
                            """
                            Specify Relay Agent Information Option
                            configuration
                            
                            .. attribute:: authenticate
                            
                            	Specify Relay Agent Information Option authenticate
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay, self).__init__()

                                self.yang_name = "relay"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.authenticate = YLeaf(YType.int32, "authenticate")
                                self._segment_path = lambda: "relay"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay, ['authenticate'], name, value)


                        class RequestedIpAddress(Entity):
                            """
                            Validate Requested IP Address
                            
                            .. attribute:: check
                            
                            	specify requested\-ip\-address\-check disable
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress, self).__init__()

                                self.yang_name = "requested-ip-address"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.check = YLeaf(YType.empty, "check")
                                self._segment_path = lambda: "requested-ip-address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress, ['check'], name, value)


                        class ServerIdCheck(Entity):
                            """
                            Validate server ID check
                            
                            .. attribute:: check
                            
                            	specify server\-id\-check disable
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck, self).__init__()

                                self.yang_name = "server-id-check"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.check = YLeaf(YType.empty, "check")
                                self._segment_path = lambda: "server-id-check"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck, ['check'], name, value)


                        class Session(Entity):
                            """
                            Change sessions configuration
                            
                            .. attribute:: throttle_type
                            
                            	Throttle DHCP sessions based on MAC address
                            	**type**\:   :py:class:`ThrottleType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session, self).__init__()

                                self.yang_name = "session"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"throttle-type" : ("throttle_type", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType)}
                                self._child_list_classes = {}

                                self.throttle_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType()
                                self.throttle_type.parent = self
                                self._children_name_map["throttle_type"] = "throttle-type"
                                self._children_yang_names.add("throttle-type")
                                self._segment_path = lambda: "session"


                            class ThrottleType(Entity):
                                """
                                Throttle DHCP sessions based on MAC
                                address
                                
                                .. attribute:: mac_throttle
                                
                                	Throttle DHCP sessions from any one MAC address
                                	**type**\:   :py:class:`MacThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType, self).__init__()

                                    self.yang_name = "throttle-type"
                                    self.yang_parent_name = "session"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"mac-throttle" : ("mac_throttle", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle)}
                                    self._child_list_classes = {}

                                    self.mac_throttle = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle()
                                    self.mac_throttle.parent = self
                                    self._children_name_map["mac_throttle"] = "mac-throttle"
                                    self._children_yang_names.add("mac-throttle")
                                    self._segment_path = lambda: "throttle-type"


                                class MacThrottle(Entity):
                                    """
                                    Throttle DHCP sessions from any one MAC
                                    address
                                    
                                    .. attribute:: num_block
                                    
                                    	Throttle blocking period (in secs)
                                    	**type**\:  int
                                    
                                    	**range:** 1..100
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: num_discover
                                    
                                    	Number of discovers at which to throttle
                                    	**type**\:  int
                                    
                                    	**range:** 1..65535
                                    
                                    .. attribute:: num_request
                                    
                                    	Throttle request period (in secs)
                                    	**type**\:  int
                                    
                                    	**range:** 1..100
                                    
                                    	**units**\: second
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle, self).__init__()

                                        self.yang_name = "mac-throttle"
                                        self.yang_parent_name = "throttle-type"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.num_block = YLeaf(YType.uint32, "num-block")

                                        self.num_discover = YLeaf(YType.uint32, "num-discover")

                                        self.num_request = YLeaf(YType.uint32, "num-request")
                                        self._segment_path = lambda: "mac-throttle"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle, ['num_block', 'num_discover', 'num_request'], name, value)


                    class Snoop(Entity):
                        """
                        DHCP Snoop profile
                        
                        .. attribute:: relay_information_option
                        
                        	DHCP Snoop profile
                        	**type**\:   :py:class:`RelayInformationOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption>`
                        
                        .. attribute:: trusted
                        
                        	Trusted sources
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop, self).__init__()

                            self.yang_name = "snoop"
                            self.yang_parent_name = "mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"relay-information-option" : ("relay_information_option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption)}
                            self._child_list_classes = {}

                            self.trusted = YLeaf(YType.empty, "trusted")

                            self.relay_information_option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption()
                            self.relay_information_option.parent = self
                            self._children_name_map["relay_information_option"] = "relay-information-option"
                            self._children_yang_names.add("relay-information-option")
                            self._segment_path = lambda: "snoop"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop, ['trusted'], name, value)


                        class RelayInformationOption(Entity):
                            """
                            DHCP Snoop profile
                            
                            .. attribute:: allow_untrusted
                            
                            	Forward untrusted packets
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: insert
                            
                            	Insert Relay Agent Information circuit ID and remote ID suboptions in client request
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy
                            
                            	Relay information option policy
                            	**type**\:   :py:class:`Ipv4dhcpdRelayInfoOptionPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdRelayInfoOptionPolicy>`
                            
                            .. attribute:: remote_id
                            
                            	Enter remote\-id value
                            	**type**\:   :py:class:`RemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption, self).__init__()

                                self.yang_name = "relay-information-option"
                                self.yang_parent_name = "snoop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"remote-id" : ("remote_id", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId)}
                                self._child_list_classes = {}

                                self.allow_untrusted = YLeaf(YType.empty, "allow-untrusted")

                                self.insert = YLeaf(YType.empty, "insert")

                                self.policy = YLeaf(YType.enumeration, "policy")

                                self.remote_id = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId()
                                self.remote_id.parent = self
                                self._children_name_map["remote_id"] = "remote-id"
                                self._children_yang_names.add("remote-id")
                                self._segment_path = lambda: "relay-information-option"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption, ['allow_untrusted', 'insert', 'policy'], name, value)


                            class RemoteId(Entity):
                                """
                                Enter remote\-id value
                                
                                .. attribute:: format_type
                                
                                	Format type, 1. Hex 2. ASCII
                                	**type**\:  int
                                
                                	**range:** 1..2
                                
                                .. attribute:: remote_id_value
                                
                                	Enter remote\-id value
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId, self).__init__()

                                    self.yang_name = "remote-id"
                                    self.yang_parent_name = "relay-information-option"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.format_type = YLeaf(YType.uint32, "format-type")

                                    self.remote_id_value = YLeaf(YType.str, "remote-id-value")
                                    self._segment_path = lambda: "remote-id"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId, ['format_type', 'remote_id_value'], name, value)


    class RateLimit(Entity):
        """
        Rate limit ingress packets
        
        .. attribute:: num_discover
        
        	Max DISCOVER packets per rate\-limiter period (default 100)
        	**type**\:  int
        
        	**range:** 0..1000
        
        	**default value**\: 100
        
        .. attribute:: num_period
        
        	Rate limiter period in msec (default\: 200 msec)
        	**type**\:  int
        
        	**range:** 1..1000
        
        	**default value**\: 200
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv4Dhcpd.RateLimit, self).__init__()

            self.yang_name = "rate-limit"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.num_discover = YLeaf(YType.uint32, "num-discover")

            self.num_period = YLeaf(YType.uint32, "num-period")
            self._segment_path = lambda: "rate-limit"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Dhcpd.RateLimit, ['num_discover', 'num_period'], name, value)


    class Vrfs(Entity):
        """
        VRF Table
        
        .. attribute:: vrf
        
        	VRF table
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Ipv4Dhcpd.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vrf" : ("vrf", Ipv4Dhcpd.Vrfs.Vrf)}

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Dhcpd.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            VRF table
            
            .. attribute:: vrf_name  <key>
            
            	VRF Name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: profile
            
            	Profile name and mode
            	**type**\:   :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Vrfs.Vrf.Profile>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ipv4-dhcpd-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Ipv4Dhcpd.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"profile" : ("profile", Ipv4Dhcpd.Vrfs.Vrf.Profile)}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.profile = None
                self._children_name_map["profile"] = "profile"
                self._children_yang_names.add("profile")
                self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Dhcpd.Vrfs.Vrf, ['vrf_name'], name, value)


            class Profile(Entity):
                """
                Profile name and mode
                
                .. attribute:: mode
                
                	Dhcp mode
                	**type**\:   :py:class:`Ipv4dhcpdMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdMode>`
                
                	**mandatory**\: True
                
                .. attribute:: vrf_profile_name
                
                	Profile name
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Ipv4Dhcpd.Vrfs.Vrf.Profile, self).__init__()

                    self.yang_name = "profile"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.mode = YLeaf(YType.enumeration, "mode")

                    self.vrf_profile_name = YLeaf(YType.str, "vrf-profile-name")
                    self._segment_path = lambda: "profile"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Vrfs.Vrf.Profile, ['mode', 'vrf_profile_name'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv4Dhcpd()
        return self._top_entity

